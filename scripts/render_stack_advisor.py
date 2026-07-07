#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


REPO = Path(__file__).resolve().parent.parent
TAXONOMY: tuple[tuple[str, str], ...] = (
    ("taste_direction", "Taste Direction"),
    ("motion", "Motion"),
    ("density", "Density"),
    ("accessibility", "Accessibility"),
    ("typography", "Typography"),
    ("color", "Color"),
    ("layout", "Layout"),
    ("interaction", "Interaction"),
    ("audit", "Audit"),
    ("retrieval", "Retrieval"),
    ("enforcement", "Enforcement"),
    ("sources", "Sources"),
)
AMBITION_VALUES = {"refresh", "evolve", "transform"}
STYLE_DB = Path(".raw/skills/ui-ux-pro-max/styles.csv")
STYLE_KEYWORD_BY_TYPE = {
    "landing": "landing",
    "portfolio": "portfolio",
    "redesign": "landing",
    "dashboard": "dashboard",
    "app": "app",
    "editorial": "magazine",
}
ENUMS = {
    "project_type": {"landing", "portfolio", "redesign", "dashboard", "app", "editorial"},
    "brand_maturity": {"none", "partial", "mature"},
    "motion": {"static", "restrained", "rich", "cinematic"},
    "density": {"airy", "balanced", "dense"},
    "accessibility": {"standard", "strict"},
}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Render a Gogh stack advisor report.")
    parser.add_argument("--brief", required=True)
    parser.add_argument("--registry", default="references/skill-registry.json")
    parser.add_argument("--out", default="")
    args = parser.parse_args(argv)
    try:
        brief = load_brief(Path(args.brief))
        registry = load_registry(Path(args.registry))
        report = render_report(brief, registry)
        if args.out:
            resolve_path(Path(args.out)).write_text(report, encoding="utf-8")
        else:
            print(report, end="")
    except AdvisorError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    return 0


class AdvisorError(Exception):
    pass


def load_brief(path: Path) -> dict[str, str]:
    full = resolve_path(path)
    if not full.exists():
        raise AdvisorError(f"missing project brief: {display_path(path)}")
    try:
        data = json.loads(full.read_text(encoding="utf-8"))
    except ValueError as exc:
        raise AdvisorError(f"invalid project brief JSON: {exc}") from exc
    if not isinstance(data, dict):
        raise AdvisorError("project brief must be an object")
    brief: dict[str, str] = {}
    for field, allowed in ENUMS.items():
        value = data.get(field)
        if not isinstance(value, str) or value not in allowed:
            allowed_values = ", ".join(sorted(allowed))
            raise AdvisorError(f"brief field {field} must be one of: {allowed_values}")
        brief[field] = value
    ambition = data.get("ambition", "evolve")
    if not isinstance(ambition, str) or ambition not in AMBITION_VALUES:
        raise AdvisorError(f"brief field ambition must be one of: {', '.join(sorted(AMBITION_VALUES))}")
    brief["ambition"] = ambition
    unknown = set(data) - set(ENUMS) - {"ambition"}
    if unknown:
        raise AdvisorError(f"brief unknown field: {', '.join(sorted(unknown))}")
    return brief


def load_registry(path: Path) -> dict[str, Any]:
    full = resolve_path(path)
    if not full.exists():
        raise AdvisorError(f"missing skill registry: {display_path(path)}")
    try:
        data = json.loads(full.read_text(encoding="utf-8"))
    except ValueError as exc:
        raise AdvisorError(f"invalid skill registry JSON: {exc}") from exc
    if not isinstance(data, dict) or not isinstance(data.get("skills"), list) or not data["skills"]:
        raise AdvisorError("skill registry must contain a non-empty skills array")
    return data


def render_report(brief: dict[str, str], registry: dict[str, Any]) -> str:
    skills = sorted(registry["skills"], key=lambda skill: str(skill.get("id", "")))
    recommended = recommend_stack(brief, skills)
    dials = dial_settings(brief)

    lines = [
        "# Gogh Stack Advisor",
        "",
        "## Project Brief",
        f"- Project type: {brief['project_type']}",
        f"- Brand maturity: {brief['brand_maturity']}",
        f"- Motion: {brief['motion']}",
        f"- Density: {brief['density']}",
        f"- Accessibility: {brief['accessibility']}",
        f"- Ambition: {brief['ambition']}",
        "",
        "## Recommended Stack",
    ]
    for skill in recommended:
        lines.append(f"- {skill['id']}: {skill.get('title') or skill.get('name') or skill['id']}")

    lines.extend(
        [
            "",
            "## Dial Settings",
            f"- DESIGN_VARIANCE: {dials['DESIGN_VARIANCE']}",
            f"- MOTION_INTENSITY: {dials['MOTION_INTENSITY']}",
            f"- VISUAL_DENSITY: {dials['VISUAL_DENSITY']}",
            *direction_commitment(brief),
            "",
            "## Coverage Matrix",
            "| Taxonomy | Skills |",
            "|---|---|",
        ]
    )
    for tag, label in TAXONOMY:
        carriers = [skill["id"] for skill in skills if tag in skill.get("coverage_tags", [])]
        lines.append(f"| {label} | {', '.join(carriers) if carriers else 'gap'} |")

    lines.extend(["", "## Sources"])
    for skill in skills:
        capture = skill.get("capture", {}) if isinstance(skill.get("capture"), dict) else {}
        url = capture.get("url") or "unspecified capture"
        retrieved = capture.get("retrieved") or "unknown date"
        license_name = capture.get("license") or "unknown license"
        lines.append(f"- {skill['id']}: {url} (retrieved {retrieved}, license {license_name})")

    return clean_report("\n".join(lines) + "\n")


def recommend_stack(brief: dict[str, str], skills: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_id = {str(skill.get("id", "")): skill for skill in skills}
    order: list[str] = []
    if brief["project_type"] in {"landing", "portfolio", "redesign", "editorial"}:
        order.extend(["taste-skill-v2", "anthropic-frontend-design"])
    if brief["brand_maturity"] in {"none", "partial"}:
        order.append("ui-ux-pro-max")
    if brief["motion"] in {"restrained", "rich", "cinematic"}:
        order.append("make-interfaces-feel-better")
    order.append("impeccable")
    if brief["accessibility"] == "strict" or brief["project_type"] in {"landing", "redesign", "app", "dashboard"}:
        order.append("vercel-web-design-guidelines")

    selected = []
    seen = set()
    for skill_id in order:
        skill = by_id.get(skill_id)
        if skill is not None and skill_id not in seen:
            selected.append(skill)
            seen.add(skill_id)
    return selected


def dial_settings(brief: dict[str, str]) -> dict[str, int]:
    variance_by_type = {
        "landing": 7,
        "portfolio": 8,
        "redesign": 6,
        "dashboard": 4,
        "app": 5,
        "editorial": 6,
    }
    motion_by_brief = {
        "static": 1,
        "restrained": 4,
        "rich": 8,
        "cinematic": 9,
    }
    density_by_brief = {
        "airy": 3,
        "balanced": 4,
        "dense": 7,
    }
    variance = variance_by_type[brief["project_type"]]
    if brief["brand_maturity"] == "none":
        variance += 1
    elif brief["brand_maturity"] == "partial":
        variance -= 1
    elif brief["brand_maturity"] == "mature":
        variance -= 2
    if brief["accessibility"] == "strict":
        variance = min(variance, 6)
    # Ambition wins last: a transform brief demands a new direction even under
    # strict accessibility; refresh keeps the incumbent direction.
    if brief["ambition"] == "transform":
        variance = max(variance, 8)
    elif brief["ambition"] == "refresh":
        variance = min(variance, 4)
    return {
        "DESIGN_VARIANCE": max(1, min(10, variance)),
        "MOTION_INTENSITY": motion_by_brief[brief["motion"]],
        "VISUAL_DENSITY": density_by_brief[brief["density"]],
    }


def direction_commitment(brief: dict[str, str]) -> list[str]:
    if brief["ambition"] != "transform":
        return []
    lines = [
        "",
        "## Direction Commitment (required before any code)",
        "Transform brief: the incumbent design is evidence, not the answer.",
        "Candidate directions from the captured style database:",
    ]
    candidates = style_candidates(brief["project_type"])
    if candidates:
        lines.extend(candidates)
    else:
        lines.append("- style database not captured; name a direction manually")
    lines.extend(
        [
            "Write the commitment before building:",
            "- Direction (named, three words or fewer):",
            "- Signature element (the one move this page owns):",
            "- Five-second memory (what a visitor describes):",
            "- Nearest banned default being avoided:",
        ]
    )
    return lines


def style_candidates(project_type: str) -> list[str]:
    import csv

    full = resolve_path(STYLE_DB)
    if not full.exists():
        return []
    keyword = STYLE_KEYWORD_BY_TYPE.get(project_type, "landing")
    matches: list[dict[str, str]] = []
    seen_categories: set[str] = set()
    try:
        with full.open(encoding="utf-8", newline="") as handle:
            for row in csv.DictReader(handle):
                best_for = (row.get("Best For") or "").lower()
                category = (row.get("Style Category") or "").strip()
                if keyword not in best_for or not category or category in seen_categories:
                    continue
                seen_categories.add(category)
                matches.append(row)
    except (OSError, ValueError):
        return []
    if not matches:
        return []
    # Spread picks across the whole match list: the first rows of the database
    # are the safest styles, and a transform brief needs range, not safety.
    indexes = sorted({0, len(matches) // 2, len(matches) - 1})
    picks = []
    for i in indexes:
        row = matches[i]
        palette = (row.get("Primary Colors") or "").strip()[:60]
        era = (row.get("Era/Origin") or "").strip()
        picks.append(f"- {row['Style Category'].strip()} ({era}): palette {palette}")
    return picks


def resolve_path(path: Path) -> Path:
    return path if path.is_absolute() else REPO / path


def display_path(path: Path) -> str:
    try:
        return path.resolve().relative_to(REPO).as_posix()
    except ValueError:
        return path.name


def clean_report(value: str) -> str:
    return value.replace("\u2014", "-").replace("\u2013", "-")


if __name__ == "__main__":
    raise SystemExit(main())
