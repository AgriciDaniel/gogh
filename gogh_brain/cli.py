from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parent.parent
PY = sys.executable


def run_script(script: str, args: list[str]) -> int:
    return subprocess.call([PY, str(REPO / "scripts" / script), *args], cwd=REPO)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="gogh-brain", description="Operate Gogh.")
    sub = parser.add_subparsers(dest="command", required=True)
    p_new = sub.add_parser("new")
    p_new.add_argument("client")
    p_new.add_argument("--client-name", default="")
    p_new.add_argument("--owner", default="Daniel Agrici")
    p_new.add_argument("--out-dir", default="~/gogh-vaults")
    p_ingest = sub.add_parser("ingest")
    p_ingest.add_argument("--vault", required=True)
    p_ingest.add_argument("--file", required=True)
    p_synth = sub.add_parser("synthesize")
    p_synth.add_argument("--vault", required=True)
    p_report = sub.add_parser("report")
    p_report.add_argument("--vault", required=True)
    p_report.add_argument("--out", default="")
    p_report.add_argument("--html-only", action="store_true")
    p_visuals = sub.add_parser("visuals")
    p_visuals.add_argument("--vault", required=True)
    p_lint = sub.add_parser("lint")
    p_lint.add_argument("--vault", required=True)
    p_lint.add_argument("--template", action="store_true")
    p_next = sub.add_parser("next")
    p_next.add_argument("--vault", required=True)
    p_registry = sub.add_parser("registry")
    p_registry.add_argument("--raw-dir", default=".raw/skills")
    p_registry.add_argument("--manifest", default=".raw/.manifest.json")
    p_registry.add_argument("--out", default="references/skill-registry.json")
    p_diff = sub.add_parser("diff")
    p_diff.add_argument("--old", required=True)
    p_diff.add_argument("--new", required=True)
    p_advise = sub.add_parser("advise")
    p_advise.add_argument("--brief", required=True)
    p_advise.add_argument("--registry", default="references/skill-registry.json")
    p_advise.add_argument("--out", default="")
    sub.add_parser("demo")
    args = parser.parse_args(argv)
    if args.command == "new":
        call = ["--client", args.client, "--client-name", args.client_name or args.client, "--owner", args.owner, "--out-dir", args.out_dir]
        return run_script("scaffold_vault.py", call)
    if args.command == "ingest":
        return run_script("ingest_source.py", ["--vault", args.vault, "--file", args.file])
    if args.command == "synthesize":
        return run_script("synthesize_brain.py", ["--vault", args.vault])
    if args.command == "report":
        call = ["--vault", args.vault]
        if args.out:
            call += ["--out", args.out]
        if args.html_only:
            call.append("--html-only")
        return run_script("render_brain_report.py", call)
    if args.command == "visuals":
        return run_script("generate_vault_visuals.py", ["--vault", args.vault])
    if args.command == "lint":
        call = ["--vault", args.vault]
        if args.template:
            call.append("--template")
        return run_script("lint_vault.py", call)
    if args.command == "next":
        return run_script("guide_next_action.py", ["--vault", args.vault])
    if args.command == "registry":
        return run_script("import_skill_capture.py", ["build-registry", "--raw-dir", args.raw_dir, "--manifest", args.manifest, "--out", args.out])
    if args.command == "diff":
        return run_script("import_skill_capture.py", ["diff", "--old", args.old, "--new", args.new])
    if args.command == "advise":
        call = ["--brief", args.brief, "--registry", args.registry]
        if args.out:
            call += ["--out", args.out]
        return run_script("render_stack_advisor.py", call)
    if args.command == "demo":
        return run_script("build_demo_vault.py", [])
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
