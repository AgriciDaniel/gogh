#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path


REPO = Path(__file__).resolve().parent.parent
PY = sys.executable
FIXTURE_CAPTURE = REPO / "tests" / "fixtures" / "skill-capture-excerpt.md"
FIXTURE_BRIEF = REPO / "tests" / "fixtures" / "project-brief.json"
SAMPLE_REGISTRY = REPO / "references" / "schemas" / "skill-registry.sample.json"


def run(args: list[str], *, ok: bool = True) -> subprocess.CompletedProcess[str]:
    proc = subprocess.run([PY, *args], cwd=REPO, text=True, capture_output=True, env=os.environ.copy(), check=False)
    if ok and proc.returncode:
        print(proc.stdout)
        print(proc.stderr, file=sys.stderr)
        raise AssertionError(f"command failed: {' '.join(args)}")
    if not ok and proc.returncode != 2:
        print(proc.stdout)
        print(proc.stderr, file=sys.stderr)
        raise AssertionError(f"expected exit 2 from: {' '.join(args)}")
    return proc


def parse_json_stdout(proc: subprocess.CompletedProcess[str]) -> dict:
    data = json.loads(proc.stdout)
    assert isinstance(data, dict)
    return data


def no_output_leaks(*values: str) -> None:
    for value in values:
        assert "\u2014" not in value
        assert "/var/home" not in value
        assert "/home/" not in value


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_manifest(path: Path, entries: list[Path], raw_parent: Path, *, bad_sha: bool = False) -> None:
    sources = []
    for entry in entries:
        digest = "0" * 64 if bad_sha and not sources else sha256(entry)
        sources.append(
            {
                "path": entry.relative_to(raw_parent).as_posix(),
                "sha256": digest,
                "retrieved": "2026-07-07",
                "source_type": "fixture",
            }
        )
    path.write_text(json.dumps({"sources": sources}, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def test_parse_fixture() -> str:
    proc = run(["scripts/import_skill_capture.py", "parse", str(FIXTURE_CAPTURE)])
    parsed = parse_json_stdout(proc)
    assert parsed["dials"] == {"DESIGN_VARIANCE": 7, "MOTION_INTENSITY": 3}
    assert len(parsed["coverage_tags"]) >= 4
    assert parsed["h1"] == "Fixture Design Skill"
    assert len(parsed["headings"]) >= 4
    text = json.dumps(parsed, sort_keys=True)
    assert str(FIXTURE_CAPTURE) not in text
    no_output_leaks(proc.stdout, text)
    return proc.stdout


def test_build_registry() -> str:
    with tempfile.TemporaryDirectory(prefix="gogh-adapters-") as tmp:
        root = Path(tmp)
        raw_dir = root / "skills"
        skill_a = raw_dir / "alpha" / "SKILL.md"
        skill_b = raw_dir / "beta" / "SKILL.md"
        skill_a.parent.mkdir(parents=True)
        skill_b.parent.mkdir(parents=True)
        skill_a.write_text(FIXTURE_CAPTURE.read_text(encoding="utf-8"), encoding="utf-8")
        skill_b.write_text(FIXTURE_CAPTURE.read_text(encoding="utf-8").replace("Fixture Design Skill", "Second Fixture Skill"), encoding="utf-8")
        manifest = root / ".manifest.json"
        write_manifest(manifest, [skill_a, skill_b], root)

        out_a = root / "registry-a.json"
        out_b = root / "registry-b.json"
        run(["scripts/import_skill_capture.py", "build-registry", "--raw-dir", str(raw_dir), "--manifest", str(manifest), "--out", str(out_a)])
        run(["scripts/import_skill_capture.py", "build-registry", "--raw-dir", str(raw_dir), "--manifest", str(manifest), "--out", str(out_b)])
        assert out_a.read_bytes() == out_b.read_bytes()
        registry = json.loads(out_a.read_text(encoding="utf-8"))
        assert [skill["id"] for skill in registry["skills"]] == ["alpha", "beta"]

        bad_manifest = root / ".bad-manifest.json"
        write_manifest(bad_manifest, [skill_a, skill_b], root, bad_sha=True)
        bad = run(
            ["scripts/import_skill_capture.py", "build-registry", "--raw-dir", str(raw_dir), "--manifest", str(bad_manifest), "--out", str(root / "bad.json")],
            ok=False,
        )
        assert "sha256 mismatch" in bad.stderr
        output = out_a.read_text(encoding="utf-8") + out_b.read_text(encoding="utf-8")
        no_output_leaks(output)
        return out_a.read_text(encoding="utf-8")


def test_diff() -> str:
    with tempfile.TemporaryDirectory(prefix="gogh-adapter-diff-") as tmp:
        root = Path(tmp)
        old = root / "old.md"
        new = root / "new.md"
        text = FIXTURE_CAPTURE.read_text(encoding="utf-8")
        old.write_text(text, encoding="utf-8")
        new.write_text(text.replace("DESIGN_VARIANCE: 7", "DESIGN_VARIANCE: 9") + "\n## Added Test Section\n\nMore audit detail.\n", encoding="utf-8")
        changed = run(["scripts/import_skill_capture.py", "diff", "--old", str(old), "--new", str(new)])
        assert "Dials changed" in changed.stdout
        assert "Headings added" in changed.stdout
        identical = run(["scripts/import_skill_capture.py", "diff", "--old", str(old), "--new", str(old)])
        assert "identical" in identical.stdout
        no_output_leaks(changed.stdout, identical.stdout)
        return changed.stdout + identical.stdout


def test_failure_modes() -> None:
    with tempfile.TemporaryDirectory(prefix="gogh-adapter-fail-") as tmp:
        root = Path(tmp)
        missing = run(["scripts/import_skill_capture.py", "parse", str(root / "missing.md")], ok=False)
        assert "missing capture file" in missing.stderr
        empty = root / "empty.md"
        empty.write_text("", encoding="utf-8")
        empty_proc = run(["scripts/import_skill_capture.py", "parse", str(empty)], ok=False)
        assert "empty capture file" in empty_proc.stderr

        bad_brief = root / "bad-brief.json"
        bad_brief.write_text(
            json.dumps(
                {
                    "project_type": "landing",
                    "brand_maturity": "partial",
                    "motion": "explosive",
                    "density": "airy",
                    "accessibility": "strict",
                }
            ),
            encoding="utf-8",
        )
        bad_enum = run(["scripts/render_stack_advisor.py", "--brief", str(bad_brief), "--registry", str(SAMPLE_REGISTRY)], ok=False)
        assert "brief field motion" in bad_enum.stderr
        missing_registry = run(["scripts/render_stack_advisor.py", "--brief", str(FIXTURE_BRIEF), "--registry", str(root / "missing-registry.json")], ok=False)
        assert "missing skill registry" in missing_registry.stderr


def test_advisor_render() -> str:
    proc = run(["scripts/render_stack_advisor.py", "--brief", str(FIXTURE_BRIEF), "--registry", str(SAMPLE_REGISTRY)])
    report = proc.stdout
    assert "## Recommended Stack" in report
    assert "## Coverage Matrix" in report
    assert "## Sources" in report
    assert "- taste-skill-v2:" in report
    assert "- DESIGN_VARIANCE: 6" in report
    assert "- MOTION_INTENSITY: 8" in report
    assert "- VISUAL_DENSITY: 3" in report

    matrix = report.split("## Coverage Matrix", 1)[1].split("## Sources", 1)[0]
    rows = [line for line in matrix.splitlines() if line.startswith("| ") and not line.startswith("|---") and "Taxonomy" not in line]
    assert len(rows) == 12

    registry = json.loads(SAMPLE_REGISTRY.read_text(encoding="utf-8"))
    sources = report.split("## Sources", 1)[1]
    source_lines = [line for line in sources.splitlines() if line.startswith("- ")]
    assert len(source_lines) == len(registry["skills"])
    no_output_leaks(report)
    return report


def main() -> int:
    generated = [
        test_parse_fixture(),
        test_build_registry(),
        test_diff(),
        test_advisor_render(),
    ]
    test_failure_modes()
    no_output_leaks(*generated)
    print("Adapter tests passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
