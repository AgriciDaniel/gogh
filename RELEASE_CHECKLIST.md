# Release Checklist

## Product

- [ ] README states buyer, promise, outputs, boundaries, quick start, and honest market-ready pending release status.
- [ ] `SKILL.md` maps commands accurately.
- [ ] License is finalized as Apache-2.0.
- [ ] Third-party names and upstream ownership are preserved.
- [ ] Six skill anchors are present: taste-skill v2, make-interfaces-feel-better, Impeccable, Anthropic frontend-design, ui-ux-pro-max, and Vercel web-design-guidelines.

## Gogh Bars

- [ ] Claim-ledger row count reconciles with source packs.
- [ ] `.raw/.manifest.json` sha256 values verify against raw files.
- [ ] Zero dead wikilinks across template, sample, and root vaults.
- [ ] Zero em dashes or en dashes in `wiki/`.
- [ ] Upstream names are never rebranded. Spot check `tasteskill.dev`, `Leonxlnx`, and `design-taste-frontend`.
- [ ] Second Brain loop closeout is complete: capture, synthesize, link, review, decide, and update next actions.

## Verification

- [ ] `python -m compileall -q scripts gogh_brain tests`
- [ ] `python tests/test_adapters.py`
- [ ] `python tests/test_pipeline.py`
- [ ] `python scripts/lint_vault.py --vault assets/template-brain`
- [ ] `python scripts/lint_vault.py --vault examples/sample-vault`
- [ ] `python scripts/lint_vault.py --vault .`
- [ ] `python scripts/audit_brain.py --require market-ready`
- [ ] `python scripts/package_release.py --version 1.0.0 --release-type market-ready` on a clean tree.
- [ ] No secrets, private client data, local absolute paths, or unsafe release artifacts.
