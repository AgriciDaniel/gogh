# Gogh Agent Instructions

The canonical agent entrypoint is `SKILL.md`; this file exists for agent
runtimes that load project-level `AGENTS.md` instructions.

Gogh is a six-skill frontend design stack brain for AI coding agents.

## Read Order

1. `SKILL.md`
2. `README.md`
3. `docs/OPERATOR_KIT.md`
4. `docs/PRODUCT_BOUNDARIES.md`
5. `references/product-spec.md`
6. `references/source-ledger.json`
7. `references/adapter-manifest.json`
8. `references/claim-ledger.md`
9. `references/skill-registry.json`

## Operating Rules

- Do not call this brain market-ready unless `scripts/audit_brain.py --require
  market-ready` passes.
- A scaffold is not a finished brain.
- Domain-specific claims require dated trustworthy sources.
- Research evidence must be recorded in `references/source-ledger.json`.
- Adapter completion must be recorded in `references/adapter-manifest.json`.
- Preserve `.raw/` as immutable source material.
- Keep Obsidian `wiki/`, `CODEX.md`, dashboards, canvases, frontmatter,
  wikilinks, graph hygiene, and source citations healthy.
- V1 is advisory and read-only unless a future release defines approval and
  rollback for mutations.

## Verification

Run the package command only from a clean tree.

```bash
python -m compileall scripts gogh_brain tests
python tests/test_adapters.py
python tests/test_pipeline.py
python scripts/lint_vault.py --vault .
python scripts/audit_brain.py --json
python scripts/package_release.py --version 1.0.0 --release-type market-ready
```
