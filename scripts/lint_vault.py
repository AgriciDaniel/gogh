#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

TYPE_VALUES = {
    "skill",
    "entity",
    "concept",
    "rule",
    "audit",
    "flow",
    "comparison",
    "reception",
    "source",
    "decision",
    "deliverable",
    "question",
    "gap",
    "experiment",
    "meta",
}
DOMAIN_VALUES = {
    "taste-skill",
    "mifb",
    "impeccable",
    "frontend-design",
    "ui-ux-pro-max",
    "web-design-guidelines",
    "stack",
    "theory",
    "ops",
}
STATUS_VALUES = {"seed", "developing", "mature", "evergreen"}
CONFIDENCE_VALUES = {"evidence-based", "practitioner", "contested", "folklore"}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Lint a brain vault.")
    parser.add_argument("--vault", required=True)
    parser.add_argument("--template", action="store_true")
    args = parser.parse_args(argv)
    vault = Path(args.vault).expanduser().resolve()
    errors: list[str] = []
    warnings: list[str] = []
    for rel in ["CODEX.md", "README.md", "shipping-rules.md", ".raw/.manifest.json", "wiki/hot.md", "wiki/index.md", "wiki/overview.md", "wiki/log.md", "wiki/meta/Start Here.md", "wiki/meta/dashboard.md"]:
        if not (vault / rel).exists():
            errors.append(f"missing {rel}")
    check_raw_manifest(vault, errors)
    graph = vault / ".obsidian" / "graph.json"
    if graph.exists():
        data = json.loads(graph.read_text(encoding="utf-8"))
        if len(data.get("colorGroups") or []) < 4:
            errors.append("graph.json has fewer than 4 color groups")
    notes = list((vault / "wiki").rglob("*.md")) if (vault / "wiki").exists() else []
    stems = {p.stem.lower(): p for p in notes}
    rels = {p.relative_to(vault).with_suffix("").as_posix().lower(): p for p in notes}
    incoming = {p: 0 for p in notes}
    outgoing = {p: 0 for p in notes}
    duplicate_stems: dict[str, list[str]] = {}
    for path in notes:
        duplicate_stems.setdefault(path.stem.lower(), []).append(path.relative_to(vault).as_posix())
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            errors.append(f"missing frontmatter: {path.relative_to(vault)}")
        check_em_dash(path, vault, text, errors)
        check_contract(path, vault, text, errors)
        if re.search(r"\{\{(?!date|owner|client_slug|client_name)[^}]+\}\}|__[A-Z0-9_]+__|\bTODO\b", text):
            errors.append(f"unresolved placeholder in {path.relative_to(vault)}")
        if any(part in {"deliverables", "reports"} for part in path.parts) and "[[" not in text and ".raw/" not in text and "sha256" not in text.lower():
            errors.append(f"deliverable/report lacks source citation: {path.relative_to(vault)}")
        for raw in re.findall(r"!?\[\[([^\]]+)\]\]", text):
            raw_target = raw.split("|", 1)[0].split("#", 1)[0].strip()
            target = raw_target.replace(".md", "").replace(".canvas", "").strip()
            if not target:
                continue
            outgoing[path] += 1
            key = target.lower()
            if key in stems:
                incoming[stems[key]] += 1
            elif key in rels:
                incoming[rels[key]] += 1
            elif not (vault / raw_target).exists() and not any(vault.rglob(raw_target)):
                errors.append(f"dead wikilink in {path.relative_to(vault)}: {raw}")
    zero_in = [p.relative_to(vault).as_posix() for p in notes if incoming[p] == 0]
    zero_out = [p.relative_to(vault).as_posix() for p in notes if outgoing[p] == 0]
    if zero_in:
        warnings.append("zero incoming wiki notes: " + ", ".join(zero_in[:20]))
    if zero_out:
        warnings.append("zero outgoing wiki notes: " + ", ".join(zero_out[:20]))
    for stem, paths in duplicate_stems.items():
        if stem != "_index" and len(paths) > 1:
            errors.append(f"duplicate note stem {stem}: {', '.join(paths)}")
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    print("Vault lint passed" if not errors else "Vault lint failed")
    return 1 if errors else 0


def check_em_dash(path: Path, vault: Path, text: str, errors: list[str]) -> None:
    in_fence = False
    for line_number, line in enumerate(text.splitlines(), start=1):
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
            continue
        if in_fence or "U+2014" in line:
            continue
        prose = strip_inline_code(line)
        if "\u2014" in prose:
            errors.append(f"em dash in prose: {path.relative_to(vault)}:{line_number}")


def strip_inline_code(line: str) -> str:
    output: list[str] = []
    in_code = False
    for char in line:
        if char == "`":
            in_code = not in_code
            continue
        if not in_code:
            output.append(char)
    return "".join(output)


def check_contract(path: Path, vault: Path, text: str, errors: list[str]) -> None:
    frontmatter = parse_frontmatter(text)
    if not frontmatter or "domain" not in frontmatter:
        return
    rel = path.relative_to(vault)
    note_type = scalar_value(frontmatter.get("type"))
    domain = scalar_value(frontmatter.get("domain"))
    status = scalar_value(frontmatter.get("status"))
    confidence = scalar_value(frontmatter.get("confidence"))
    tags = list_value(frontmatter.get("tags"))

    if note_type not in TYPE_VALUES:
        errors.append(f"invalid contract type in {rel}: {note_type or '<missing>'}")
    if domain not in DOMAIN_VALUES:
        errors.append(f"invalid contract domain in {rel}: {domain or '<missing>'}")
    if status not in STATUS_VALUES:
        errors.append(f"invalid contract status in {rel}: {status or '<missing>'}")
    if confidence and confidence not in CONFIDENCE_VALUES:
        errors.append(f"invalid contract confidence in {rel}: {confidence}")

    gogh_tags = [tag for tag in tags if tag.startswith("gogh/")]
    note_tags = [tag for tag in tags if tag.startswith("note/")]
    expected_gogh = f"gogh/{domain}" if domain else ""
    expected_note = f"note/{note_type}" if note_type else ""
    if len(gogh_tags) != 1 or gogh_tags[0] != expected_gogh:
        errors.append(f"invalid gogh tag in {rel}: expected {expected_gogh or '<valid domain>'}")
    if len(note_tags) != 1 or note_tags[0] != expected_note:
        errors.append(f"invalid note tag in {rel}: expected {expected_note or '<valid type>'}")


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end == -1:
        return {}
    data: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if not line.strip() or line.lstrip().startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip()
    return data


def scalar_value(value: str | None) -> str:
    if value is None:
        return ""
    return value.strip().strip('"').strip("'")


def list_value(value: str | None) -> list[str]:
    if value is None:
        return []
    value = value.strip()
    if value.startswith("[") and value.endswith("]"):
        value = value[1:-1]
    if not value:
        return []
    return [scalar_value(item.strip()) for item in value.split(",") if item.strip()]


def check_raw_manifest(vault: Path, errors: list[str]) -> None:
    manifest_path = vault / ".raw" / ".manifest.json"
    if not manifest_path.exists():
        return
    try:
        data = json.loads(manifest_path.read_text(encoding="utf-8"))
    except ValueError as exc:
        errors.append(f"invalid raw manifest: {exc}")
        return
    sources = data.get("sources", [])
    if not isinstance(sources, list):
        errors.append("raw manifest sources must be a list")
        return
    seen_paths: set[str] = set()
    for index, entry in enumerate(sources, start=1):
        label = f"raw manifest source #{index}"
        if not isinstance(entry, dict):
            errors.append(f"{label} must be an object")
            continue
        rel = entry.get("path")
        expected = entry.get("sha256")
        if not isinstance(rel, str) or not rel.strip():
            errors.append(f"{label} missing path")
            continue
        rel = rel.strip()
        if rel in seen_paths:
            errors.append(f"duplicate raw manifest path: {rel}")
        seen_paths.add(rel)
        if rel.startswith("/") or ".." in Path(rel).parts:
            errors.append(f"{label} has unsafe path: {rel}")
            continue
        source = vault / rel
        if not source.is_file():
            errors.append(f"{label} missing file: {rel}")
            continue
        if not isinstance(expected, str) or not re.fullmatch(r"[0-9a-f]{64}", expected):
            errors.append(f"{label} missing valid sha256")
            continue
        if sha256_file(source) != expected:
            errors.append(f"{label} sha256 mismatch: {rel}")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


if __name__ == "__main__":
    raise SystemExit(main())
