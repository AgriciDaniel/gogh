# Gogh Operator Kit

Gogh turns six frontend design skills into one source-cited operating brain for
AI coding agents. Use it to select a stack, set taste and motion guidance,
retrieve design references, enforce contracts, and run audits without losing
the source trail.

## Five-Minute Path

```bash
python -m pip install -e .
gogh-brain demo
gogh-brain lint --vault examples/sample-vault
gogh-brain report --vault examples/sample-vault --html-only
```

Open `examples/sample-vault/` in Obsidian and read:

1. `CODEX.md`
2. `wiki/hot.md`
3. `wiki/index.md`
4. `wiki/meta/dashboard.md`

## Client Vault

```bash
gogh-brain new acme --client-name "Acme Co" --owner "Daniel Agrici" --out-dir ~/gogh-vaults
gogh-brain ingest --vault ~/gogh-vaults/acme --file tests/fixtures/sample-source.md
gogh-brain synthesize --vault ~/gogh-vaults/acme
gogh-brain report --vault ~/gogh-vaults/acme --html-only
```

## Stack Selection

Start with the project brief. Pick taste-skill v2 and Anthropic
frontend-design for aesthetic direction, add make-interfaces-feel-better when
micro-interactions matter, add Impeccable when contracts and detector hooks are
needed, use ui-ux-pro-max for retrieval, and use Vercel
web-design-guidelines for audit findings.

Record conflicts explicitly. Gogh should explain which guidance wins for the
current project instead of flattening six upstream skills into one anonymous
rule list.

## Research Rule

Refresh current official or primary sources before turning this researched
brain into a market-ready release. Each of the six upstream skills can change
rules, versions, licenses, examples, commands, or detector behavior.

Research evidence must be written into `references/source-ledger.json` with
source URL, source type, retrieved date, refresh due date, confidence, and claim
coverage. Markdown research notes alone do not satisfy market-ready release.

## Adapter Rule

Domain-adapted status requires `references/adapter-manifest.json` to name real
schemas, importer paths, synthesis modules, report renderers, fixtures, and
tests. Generic scaffold scripts are intentionally capped below market-ready.

The `registry`, `diff`, and `advise` subcommands land in the adapter wave.
Until then, stack advice is documented prose and not a completed adapter.
