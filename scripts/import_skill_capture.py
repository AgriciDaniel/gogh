#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import date
from pathlib import Path
from typing import Any


REPO = Path(__file__).resolve().parent.parent
DIAL_NAMES = ("DESIGN_VARIANCE", "MOTION_INTENSITY", "VISUAL_DENSITY")
TAXONOMY: tuple[tuple[str, str, tuple[str, ...]], ...] = (
    ("taste_direction", "Taste Direction", ("taste", "aesthetic", "brand", "design read", "variance", "distinctive", "anti-slop", "style")),
    ("motion", "Motion", ("motion", "animation", "transition", "spring", "stagger", "micro-interaction", "reduced-motion")),
    ("density", "Density", ("density", "airy", "dense", "spacing", "whitespace", "packed", "layout")),
    ("accessibility", "Accessibility", ("accessibility", "aria", "focus", "contrast", "keyboard", "hit area", "reduced-motion")),
    ("typography", "Typography", ("typography", "font", "headline", "type", "serif", "sans", "line length", "text")),
    ("color", "Color", ("color", "palette", "accent", "contrast", "hex", "gradient", "oklch")),
    ("layout", "Layout", ("layout", "grid", "hero", "section", "responsive", "cards", "bento")),
    ("interaction", "Interaction", ("interaction", "hover", "state", "button", "cursor", "pointer", "touch", "press")),
    ("audit", "Audit", ("audit", "checklist", "pre-flight", "finding", "review", "lint", "detector")),
    ("retrieval", "Retrieval", ("retrieval", "database", "registry", "bm25", "search", "reference", "palette")),
    ("enforcement", "Enforcement", ("enforcement", "rule", "contract", "hook", "command", "deterministic", "required")),
    ("sources", "Sources", ("source", "citation", "capture", "license", "retrieved", "provenance", "sha256")),
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Import and compare Gogh skill captures.")
    sub = parser.add_subparsers(dest="command", required=True)

    p_parse = sub.add_parser("parse", help="Parse one captured skill markdown file.")
    p_parse.add_argument("file")
    p_parse.add_argument("--out", default="")

    p_registry = sub.add_parser("build-registry", help="Build a deterministic registry from .raw/skills.")
    p_registry.add_argument("--raw-dir", default=".raw/skills")
    p_registry.add_argument("--manifest", default=".raw/.manifest.json")
    p_registry.add_argument("--out", default="references/skill-registry.json")

    p_diff = sub.add_parser("diff", help="Compare two parsed or markdown captures.")
    p_diff.add_argument("--old", required=True)
    p_diff.add_argument("--new", required=True)

    args = parser.parse_args(argv)
    try:
        if args.command == "parse":
            parsed = parse_capture(Path(args.file))
            return write_json(parsed, args.out)
        if args.command == "build-registry":
            registry = build_registry(Path(args.raw_dir), Path(args.manifest))
            return write_json(registry, args.out)
        if args.command == "diff":
            return diff_captures(Path(args.old), Path(args.new))
    except AdapterError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    return 2


class AdapterError(Exception):
    pass


def parse_capture(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise AdapterError(f"missing capture file: {display_path(path)}")
    text = path.read_text(encoding="utf-8", errors="replace")
    if not text.strip():
        raise AdapterError(f"empty capture file: {display_path(path)}")

    header = parse_capture_header(text)
    frontmatter = parse_frontmatter(text)
    h1 = first_heading(text, level=1)
    h2 = headings(text, level=2)
    dials = extract_dials(text)
    tags = coverage_tags(text)

    return sanitize_json(
        {
            "schema": "gogh/skill-capture-parse@1",
            "source_file": path.name,
            "capture": header,
            "frontmatter": frontmatter,
            "name": frontmatter.get("name") or h1 or path.stem,
            "h1": h1,
            "headings": h2,
            "dials": dials,
            "coverage_tags": tags,
            "heading_count": len(h2),
            "sha256": sha256_file(path),
        }
    )


def parse_capture_header(text: str) -> dict[str, str]:
    match = re.search(
        r"<!--\s*capture:\s*(?P<url>.*?)\s*\|\s*retrieved:\s*(?P<retrieved>\d{4}-\d{2}-\d{2})\s*\|\s*license:\s*(?P<license>.*?)\s*-->",
        text,
        flags=re.I | re.S,
    )
    if not match:
        return {}
    return {key: clean_text(value.strip()) for key, value in match.groupdict().items()}


def parse_frontmatter(text: str) -> dict[str, str]:
    lines = text.splitlines()
    start = None
    for index, line in enumerate(lines[:8]):
        if line.strip() == "---":
            start = index
            break
    if start is None:
        return {}
    end = None
    for index in range(start + 1, len(lines)):
        if lines[index].strip() == "---":
            end = index
            break
    if end is None:
        return {}

    data: dict[str, str] = {}
    for line in lines[start + 1 : end]:
        if ":" not in line or line.startswith(" "):
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and value:
            data[key] = clean_text(value)
    return data


def first_heading(text: str, *, level: int) -> str:
    prefix = "#" * level
    pattern = re.compile(rf"^{re.escape(prefix)}\s+(?!#)(.+?)\s*$", flags=re.M)
    match = pattern.search(text)
    return clean_heading(match.group(1)) if match else ""


def headings(text: str, *, level: int) -> list[str]:
    prefix = "#" * level
    pattern = re.compile(rf"^{re.escape(prefix)}\s+(?!#)(.+?)\s*$", flags=re.M)
    return [clean_heading(match.group(1)) for match in pattern.finditer(text)]


def clean_heading(value: str) -> str:
    value = re.sub(r"\s+#*$", "", value)
    value = value.replace("`", "")
    value = re.sub(r"[*_]+", "", value)
    return clean_text(value.strip())


def extract_dials(text: str) -> dict[str, int]:
    dials: dict[str, int] = {}
    for match in re.finditer(r"\b(DESIGN_VARIANCE|MOTION_INTENSITY|VISUAL_DENSITY)\b`?\s*[:=]\s*`?(\d{1,2})\b", text):
        name, raw_value = match.groups()
        if name not in dials:
            dials[name] = int(raw_value)
    return {name: dials[name] for name in DIAL_NAMES if name in dials}


def coverage_tags(text: str) -> list[str]:
    lowered = text.lower()
    tags = []
    for tag, _label, keywords in TAXONOMY:
        if any(keyword in lowered for keyword in keywords):
            tags.append(tag)
    return tags


def build_registry(raw_dir: Path, manifest_path: Path) -> dict[str, Any]:
    raw_root = resolve_path(raw_dir)
    if not raw_root.exists() or not raw_root.is_dir():
        raise AdapterError(f"missing raw skills directory: {display_path(raw_dir)}")
    manifest = load_manifest(resolve_path(manifest_path))

    skills = []
    for skill_dir in sorted(path for path in raw_root.iterdir() if path.is_dir()):
        primary = pick_primary_capture(skill_dir)
        parsed = parse_capture(primary)
        source_files = source_files_for_skill(skill_dir, raw_root, manifest)
        skills.append(
            {
                "id": skill_dir.name,
                "name": parsed["name"],
                "title": parsed["h1"],
                "capture": parsed["capture"],
                "dials": parsed["dials"],
                "coverage_tags": parsed["coverage_tags"],
                "headings": parsed["headings"],
                "source_files": source_files,
            }
        )

    if not skills:
        raise AdapterError(f"no skill captures found under {display_path(raw_dir)}")
    generated_at = latest_retrieved(skills) or date.today().isoformat()
    return sanitize_json(
        {
            "schema": "gogh/skill-registry@1",
            "generated_at": generated_at,
            "skill_count": len(skills),
            "skills": skills,
            "taxonomy": [{"tag": tag, "label": label} for tag, label, _keywords in TAXONOMY],
        }
    )


def load_manifest(path: Path) -> dict[str, dict[str, str]]:
    if not path.exists():
        raise AdapterError(f"missing manifest: {display_path(path)}")
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except ValueError as exc:
        raise AdapterError(f"invalid manifest JSON: {exc}") from exc
    sources = data.get("sources")
    if not isinstance(sources, list):
        raise AdapterError("manifest must contain a sources array")

    by_path: dict[str, dict[str, str]] = {}
    for source in sources:
        if not isinstance(source, dict):
            continue
        raw_path = source.get("path")
        sha = source.get("sha256")
        if not isinstance(raw_path, str) or not isinstance(sha, str):
            continue
        normalized = normalize_manifest_path(raw_path)
        by_path[normalized] = {
            "path": normalized,
            "sha256": sha,
            "retrieved": str(source.get("retrieved", "")),
            "source_type": str(source.get("source_type", "")),
        }
    return by_path


def source_files_for_skill(skill_dir: Path, raw_root: Path, manifest: dict[str, dict[str, str]]) -> list[dict[str, str]]:
    files = []
    for path in sorted(item for item in skill_dir.rglob("*") if item.is_file()):
        rel = path.relative_to(raw_root).as_posix()
        manifest_entry = find_manifest_entry(path, raw_root, rel, manifest)
        digest = sha256_file(path)
        if manifest_entry is None:
            raise AdapterError(f"manifest missing sha256 for {rel}")
        if manifest_entry["sha256"] != digest:
            raise AdapterError(f"sha256 mismatch for {rel}: manifest {manifest_entry['sha256']} != actual {digest}")
        files.append(
            {
                "path": rel,
                "sha256": digest,
                "retrieved": manifest_entry.get("retrieved", ""),
                "source_type": manifest_entry.get("source_type", ""),
            }
        )
    return files


def find_manifest_entry(path: Path, raw_root: Path, rel: str, manifest: dict[str, dict[str, str]]) -> dict[str, str] | None:
    parent = raw_root.parent.name
    root_name = raw_root.name
    candidates = {
        rel,
        f"{root_name}/{rel}",
        f"{parent}/{root_name}/{rel}",
        f"./{root_name}/{rel}",
        f"./{parent}/{root_name}/{rel}",
        path.as_posix(),
    }
    try:
        candidates.add(path.relative_to(REPO).as_posix())
    except ValueError:
        pass
    for candidate in candidates:
        entry = manifest.get(normalize_manifest_path(candidate))
        if entry is not None:
            return entry
    return None


def pick_primary_capture(skill_dir: Path) -> Path:
    for name in ("SKILL.md", "README.md"):
        candidate = skill_dir / name
        if candidate.exists():
            return candidate
    markdown = sorted(skill_dir.glob("*.md"))
    if not markdown:
        raise AdapterError(f"skill directory has no markdown captures: {skill_dir.name}")
    return markdown[0]


def latest_retrieved(skills: list[dict[str, Any]]) -> str:
    dates = []
    for skill in skills:
        retrieved = skill.get("capture", {}).get("retrieved")
        if isinstance(retrieved, str) and re.fullmatch(r"\d{4}-\d{2}-\d{2}", retrieved):
            dates.append(retrieved)
    return max(dates) if dates else ""


def diff_captures(old_path: Path, new_path: Path) -> int:
    old = load_capture_or_parse(old_path)
    new = load_capture_or_parse(new_path)
    lines: list[str] = []

    old_dials = old.get("dials", {})
    new_dials = new.get("dials", {})
    dial_changes = []
    for name in DIAL_NAMES:
        if old_dials.get(name) != new_dials.get(name):
            dial_changes.append(f"- {name}: {old_dials.get(name, 'missing')} -> {new_dials.get(name, 'missing')}")
    if dial_changes:
        lines.append("Dials changed")
        lines.extend(dial_changes)

    old_headings = set(old.get("headings", []))
    new_headings = set(new.get("headings", []))
    added = sorted(new_headings - old_headings)
    removed = sorted(old_headings - new_headings)
    if added:
        lines.append("Headings added")
        lines.extend(f"- {heading}" for heading in added)
    if removed:
        lines.append("Headings removed")
        lines.extend(f"- {heading}" for heading in removed)

    old_tags = set(old.get("coverage_tags", []))
    new_tags = set(new.get("coverage_tags", []))
    if old_tags != new_tags:
        lines.append("Coverage tags changed")
        for tag in sorted(new_tags - old_tags):
            lines.append(f"- added {tag}")
        for tag in sorted(old_tags - new_tags):
            lines.append(f"- removed {tag}")

    if not lines:
        print("No differences; captures are identical.")
    else:
        print("\n".join(lines))
    return 0


def load_capture_or_parse(path: Path) -> dict[str, Any]:
    if path.suffix.lower() == ".json":
        if not path.exists():
            raise AdapterError(f"missing parsed capture: {display_path(path)}")
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except ValueError as exc:
            raise AdapterError(f"invalid parsed capture JSON: {exc}") from exc
        if not isinstance(data, dict):
            raise AdapterError("parsed capture JSON must be an object")
        return data
    return parse_capture(path)


def write_json(data: dict[str, Any], out: str) -> int:
    payload = json.dumps(data, indent=2, sort_keys=True, ensure_ascii=True) + "\n"
    if out:
        resolve_path(Path(out)).write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")
    return 0


def sanitize_json(value: Any) -> Any:
    if isinstance(value, str):
        return clean_text(value)
    if isinstance(value, list):
        return [sanitize_json(item) for item in value]
    if isinstance(value, dict):
        return {clean_text(str(key)): sanitize_json(item) for key, item in value.items()}
    return value


def clean_text(value: str) -> str:
    return value.replace("\u2014", "-").replace("\u2013", "-")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def normalize_manifest_path(value: str) -> str:
    return value.replace("\\", "/").removeprefix("./")


def resolve_path(path: Path) -> Path:
    return path if path.is_absolute() else REPO / path


def display_path(path: Path) -> str:
    try:
        return path.resolve().relative_to(REPO).as_posix()
    except ValueError:
        return path.name


if __name__ == "__main__":
    raise SystemExit(main())
