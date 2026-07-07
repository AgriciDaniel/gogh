#!/usr/bin/env python3
from __future__ import annotations

import argparse
import html
import json
import re
from pathlib import Path
from typing import Any


BRAIN_TITLE = "Gogh"
BRAIN_DOMAIN = "Giving AI coding agents good taste in frontend design using the open-source Taste Skill framework by Leon Lin \u2014 an anti-slop SKILL.md ruleset with three design dials (DESIGN_VARIANCE, MOTION_INTENSITY, VISUAL_DENSITY), audit-first redesigns, an image-first reference pipeline, anti-laziness rules, and a strict pre-flight check that make Claude Code, Cursor, and Codex produce distinctive, non-templated interfaces instead of generic AI slop."
BRAIN_TAGLINE = "Source cited Obsidian operating brain for Giving AI coding agents good taste in frontend design using the open-source Taste Skill framework by Leon Lin \u2014 an anti-slop SKILL.md ruleset with three design dials (DESIGN_VARIANCE, MOTION_INTENSITY, VISUAL_DENSITY), audit-first redesigns, an image-first reference pipeline, anti-laziness rules, and a strict pre-flight check that make Claude Code, Cursor, and Codex produce distinctive, non-templated interfaces instead of generic AI slop.."

CB = "#1A73E8"
CR = "#D93025"
CY = "#F9AB00"
CG = "#1E8E3E"
OB = "#0B57D0"
TB = "#D3E3FD"
TR = "#FAD2CF"
TY = "#FEEFC3"
TG = "#CEEAD6"
NB = "#0B57D0"
NR = "#C5221F"
NY = "#976800"
NG = "#137333"
INK = "#202124"
SUB = "#5F6368"
LINE = "#E8EAED"
PANEL = "#F8F9FA"
FONT = '"Google Sans","Product Sans",Roboto,"Segoe UI",Arial,sans-serif'
REDUCED = "@media (prefers-reduced-motion:reduce){*{animation:none!important}}"


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def doc(w: int, h: int, title: str, desc: str, style: str, body: str, bg: str = "#fff") -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" '
        f'aria-labelledby="title desc" font-family=\'{FONT}\'>\n'
        f'<title id="title">{esc(title)}</title>\n'
        f'<desc id="desc">{esc(desc)}</desc>\n'
        f"<style>\n  {REDUCED}\n{style}\n</style>\n"
        f'<rect width="{w}" height="{h}" fill="{bg}"/>\n{body}\n</svg>\n'
    )


def card(w: int, h: int, bg: str = "#fff", border: str = LINE, r: int = 26) -> str:
    return f'<rect x="10" y="10" width="{w - 20}" height="{h - 20}" rx="{r}" fill="{bg}" stroke="{border}"/>'


def wrap(value: object, limit: int, max_lines: int) -> list[str]:
    words = " ".join(str(value).split()).split()
    if not words:
        return []
    lines: list[str] = []
    current = ""
    for word in words:
        candidate = f"{current} {word}".strip()
        if len(candidate) <= limit or not current:
            current = candidate
            continue
        lines.append(current)
        current = word
        if len(lines) == max_lines:
            break
    if current and len(lines) < max_lines:
        lines.append(current)
    return lines[:max_lines]


def load_json(path: Path) -> dict[str, Any] | None:
    if not path.exists():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    return data if isinstance(data, dict) else None


def count_json_sources(path: Path) -> int | None:
    data = load_json(path)
    if data is None:
        return None
    for key in ("sources", "entries"):
        value = data.get(key)
        if isinstance(value, list):
            return len([item for item in value if isinstance(item, dict)])
    return None


def source_metric(vault: Path, repo: Path) -> tuple[int | None, str]:
    candidates = [
        (vault / "references" / "source-ledger.json", "source ledger entries"),
        (repo / "references" / "source-ledger.json", "source ledger entries"),
        (vault / ".raw" / ".manifest.json", "raw manifest sources"),
    ]
    for path, label in candidates:
        count = count_json_sources(path)
        if count is not None and count > 0:
            return count, label
    return None, ""


def concept_metric(vault: Path) -> int | None:
    folder = vault / "wiki" / "concepts"
    if not folder.exists():
        return None
    count = len([path for path in folder.glob("*.md") if path.name != "_index.md"])
    return count if count > 0 else None


def canon_index_count(path: Path) -> int | None:
    if not path.exists():
        return None
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError:
        return None
    count = 0
    for line in lines:
        item = line.strip()
        if not item.startswith("- "):
            continue
        lowered = item.lower()
        if "placeholder" in lowered or "add researched" in lowered or "template" in lowered:
            continue
        if re.search(r"\[[^\]]+\]\((?!NNN-)[^)]+\.md\)", item):
            count += 1
    return count if count > 0 else None


def canon_metric(vault: Path, repo: Path) -> int | None:
    for root in (vault, repo):
        folder = root / "references" / "canon"
        if not folder.exists():
            continue
        files = [path for path in folder.glob("*.md") if path.name != "_index.md"]
        if files:
            return len(files)
        indexed = canon_index_count(folder / "_index.md")
        if indexed is not None:
            return indexed
    return None


def metrics(vault: Path, repo: Path) -> list[tuple[int, str, str, str, str]]:
    items: list[tuple[int, str, str, str, str]] = []
    sources, source_label = source_metric(vault, repo)
    if sources is not None:
        items.append((sources, source_label, CB, TB, NB))
    concepts = concept_metric(vault)
    if concepts is not None:
        items.append((concepts, "concept notes", CR, TR, NR))
    canon = canon_metric(vault, repo)
    if canon is not None:
        items.append((canon, "canon entries", CY, TY, NY))
    return items


def metric_row(items: list[tuple[int, str, str, str, str]]) -> str:
    if not items:
        return ""
    x0 = 50
    y = 288
    width = 250
    gap = 18
    row = f'<text class="metric" x="{x0}" y="{y - 14}" font-size="13" letter-spacing="2" font-weight="800" fill="{SUB}">READ FROM VAULT DATA</text>'
    for i, (value, label, solid, tint, on_tint) in enumerate(items[:4]):
        x = x0 + i * (width + gap)
        row += (
            f'<g class="metric" style="animation-delay:{0.86 + i * 0.08:.2f}s">'
            f'<rect x="{x}" y="{y}" width="{width}" height="54" rx="16" fill="{tint}" stroke="{LINE}"/>'
            f'<circle cx="{x + 28}" cy="{y + 27}" r="7" fill="{solid}"/>'
            f'<text x="{x + 48}" y="{y + 24}" font-size="18" font-weight="800" fill="{on_tint}">{value}</text>'
            f'<text x="{x + 48}" y="{y + 42}" font-size="12" font-weight="700" fill="{on_tint}">{esc(label)}</text>'
            f"</g>"
        )
    return row


def build_svg(vault: Path, repo: Path) -> str:
    subtitle = BRAIN_TAGLINE or f"Source cited Obsidian operating brain for {BRAIN_DOMAIN}."
    subtitle_lines = wrap(subtitle, 96, 2)
    subtitle_svg = "".join(
        f'<text class="head" style="animation-delay:{0.08 + i * 0.04:.2f}s" x="50" y="{96 + i * 20}" font-size="14" fill="{SUB}">{esc(line)}</text>'
        for i, line in enumerate(subtitle_lines)
    )
    stages = [
        ("Raw sources", "immutable .raw inputs", CB),
        ("Linked wiki memory", "notes, links, canon", CR),
        ("Checks and gates", "audit, sources, confidence", CY),
        ("Reports and deliverables", "read only outputs", CG),
    ]
    cw = 250
    y = 150
    xs = [50, 350, 650, 950]
    chips = ""
    for i, (label, sub, col) in enumerate(stages):
        x = xs[i]
        chips += (
            f'<g class="chip" style="animation-delay:{0.30 + i * 0.16:.2f}s">'
            f'<rect x="{x}" y="{y}" width="{cw}" height="96" rx="16" fill="#fff" stroke="{LINE}"/>'
            f'<rect x="{x}" y="{y}" width="7" height="96" rx="3.5" fill="{col}"/>'
            f'<circle cx="{x + 34}" cy="{y + 34}" r="9" fill="{col}"/>'
            f'<text x="{x + 56}" y="{y + 40}" font-size="18" font-weight="800" fill="{INK}">{esc(label)}</text>'
            f'<text x="{x + 24}" y="{y + 70}" font-size="13" fill="{SUB}">{esc(sub)}</text>'
            f"</g>"
        )
    arrows = ""
    for i in range(3):
        ax = xs[i] + cw + 10
        arrows += (
            f'<g class="arrow" style="animation-delay:{0.50 + i * 0.16:.2f}s">'
            f'<line x1="{ax}" y1="{y + 48}" x2="{ax + 28}" y2="{y + 48}" stroke="{SUB}" stroke-width="3" stroke-linecap="round"/>'
            f'<path d="M{ax + 24},{y + 42} L{ax + 32},{y + 48} L{ax + 24},{y + 54}" fill="none" stroke="{SUB}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'
            f"</g>"
        )
    style = """  .head,.chip,.arrow,.metric{animation:fu .55s ease backwards}
  @keyframes fu{from{opacity:0;transform:translateY(10px)}}"""
    body = (
        f"{card(1200, 370)}\n"
        f'<text class="head" x="50" y="70" font-size="22" font-weight="800" fill="{INK}">How {esc(BRAIN_TITLE)} works</text>'
        f"{subtitle_svg}{chips}{arrows}{metric_row(metrics(vault, repo))}"
    )
    return doc(1200, 370, f"{BRAIN_TITLE} relationship map", "Source to memory to gated deliverable.", style, body)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate vault visual assets.")
    parser.add_argument("--vault", required=True)
    args = parser.parse_args(argv)
    repo = Path(__file__).resolve().parent.parent
    vault = Path(args.vault).resolve()
    out = vault / "_attachments" / "brain-relationship-map.svg"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(build_svg(vault, repo), encoding="utf-8")
    print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
