#!/usr/bin/env python3
from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


REPO = Path(__file__).resolve().parent.parent
PY = sys.executable


def run(args: list[str]) -> None:
    subprocess.run([PY, *args], cwd=REPO, check=True)


def main() -> int:
    os.environ.setdefault("GOGH_BRAIN_TODAY", "2026-07-07")
    demo_parent = REPO / "examples"
    demo = demo_parent / "sample-vault"
    if demo.exists():
        shutil.rmtree(demo)
    run(["scripts/scaffold_vault.py", "--client", "sample-vault", "--client-name", "Sample Client", "--owner", "Daniel Agrici", "--out-dir", str(demo_parent)])
    with tempfile.TemporaryDirectory(prefix="gogh-demo-source-") as temp_dir:
        demo_source = Path(temp_dir) / "sample-source.md"
        source_text = (REPO / "tests" / "fixtures" / "sample-source.md").read_text(encoding="utf-8")
        demo_source.write_text(source_text.replace("\u2013", "-").replace("\u2014", "-"), encoding="utf-8")
        run(["scripts/ingest_source.py", "--vault", str(demo), "--file", str(demo_source), "--source-type", "fixture"])
    run(["scripts/synthesize_brain.py", "--vault", str(demo)])
    run(["scripts/generate_vault_visuals.py", "--vault", str(demo)])
    run(["scripts/render_brain_report.py", "--vault", str(demo), "--html-only"])
    run(["scripts/lint_vault.py", "--vault", str(demo)])
    print(demo)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
