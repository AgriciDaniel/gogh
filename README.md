# Gogh

<p align="center">
  <img src="assets/cover.webp" alt="Gogh: design judgment for AI coding agents" width="100%"/>
</p>

Source cited Obsidian operating brain that turns six frontend design skills into one advisable stack.

Gogh is an evidence-gated Obsidian brain for AI coding agents that need better
frontend design judgment than a single prompt can provide. It combines six
curated skills into stack advice: which skill to use when, how to combine them,
how to resolve conflicts, and how to keep a unified anti-slop rulebook tied to
dated sources.

**Current maturity:** market-ready pending the release gate. The structural
audit passes at market-ready; the final release is cut by the operator
procedure.

## Promise

Turn six frontend design skills into one source-cited operating brain for
stacking taste prompting, micro-interaction execution, toolchain enforcement,
retrieval, and audit work.

## Buyer

Developers, indie hackers, design engineers, and agencies who build frontends with AI coding agents (Claude Code, Cursor, Codex, Windsurf) and want the output to look intentional and brand-fit rather than templated AI slop.

## Six Skills

| Skill | Author | Mechanism | License |
|---|---|---|---|
| taste-skill v2, `design-taste-frontend` | Leon Lin | Taste prompting for macro aesthetic direction, three dials at 8/6/4, and Section 14 pre-flight | MIT |
| make-interfaces-feel-better | Jakub Krehel | Micro-interaction execution for press states, concentric radii, and motion values | MIT (README-declared) |
| Impeccable v3.9.1 | Paul Bakaus | Toolchain enforcement through commands, PRODUCT.md and DESIGN.md contracts, a deterministic 45-rule detector, and edit-time hooks | Apache-2.0 |
| Anthropic frontend-design | Anthropic | Taste prompting baseline with committed aesthetic direction | Apache-2.0 (per-skill LICENSE.txt) |
| ui-ux-pro-max v2.10.2 | nextlevelbuilder | Retrieval database for styles, palettes, font pairings, and UX rules | MIT |
| Vercel web-design-guidelines | Vercel Labs | Audit layer with runtime-fetched rules and file:line findings | MIT (ruleset repo; skill wrapper README-declared) |

Mechanism map: taste prompting from taste-skill and Anthropic
frontend-design, micro-interaction execution from make-interfaces-feel-better,
toolchain enforcement from Impeccable, retrieval from ui-ux-pro-max, and audit
from Vercel web-design-guidelines.

## Showcase

Six message-match variants of one landing page, each a distinct editorial
format instead of a generic template. Full source in
[`examples/aimh-pro-landing-variants/`](examples/aimh-pro-landing-variants/),
live at [agricidaniel.github.io/gogh-brain](https://agricidaniel.github.io/gogh-brain/examples/aimh-pro-landing-variants/).

<p align="center">
  <img src="assets/screenshots/aimh-serp-brutalism.webp" alt="SERP Brutalism variant: a search-results-page landing format" width="49%"/>
  <img src="assets/screenshots/aimh-the-gazette.webp" alt="The Gazette variant: a broadsheet newspaper front page" width="49%"/>
</p>

<p align="center">
  <img src="assets/screenshots/aimh-2026-annual-report.webp" alt="2026 Annual Report variant: a Swiss corporate report to members" width="49%"/>
  <img src="assets/screenshots/aimh-working-collection.webp" alt="The Working Collection variant: a museum exhibition catalog" width="49%"/>
</p>

<p align="center">
  <img src="assets/screenshots/aimh-operators-catalog.webp" alt="Operator's Catalog No.30 variant: a mail-order catalog format" width="60%"/>
</p>

## Outputs

- `assets/template-brain/`, the distributable Obsidian template vault
- `SKILL.md` plus scripts, the agent-facing operating layer
- Stack advisor reports that translate a project brief into recommended skills,
  order of use, dial settings, conflicts, and audit checks
- Cheat sheet, stack decision one-pager, unified pre-flight mega-checklist, and
  quickstart
- Registry diff reports for upstream captures when the adapter wave lands

## Quick Start

```bash
python -m pip install -e .
gogh-brain demo
gogh-brain lint --vault examples/sample-vault
gogh-brain report --vault examples/sample-vault --html-only
```

To create a client vault:

```bash
gogh-brain new acme --client-name "Acme Co" --owner "Daniel Agrici" --out-dir ~/gogh-vaults
gogh-brain ingest --vault ~/gogh-vaults/acme --file tests/fixtures/sample-source.md
gogh-brain synthesize --vault ~/gogh-vaults/acme
gogh-brain visuals --vault ~/gogh-vaults/acme
gogh-brain report --vault ~/gogh-vaults/acme --html-only
gogh-brain next --vault ~/gogh-vaults/acme
```

## Boundaries

V1 is advisory and read-only. It does not mutate accounts, systems, books,
pipelines, publishing tools, customer records, or live production data.

Gogh records conflicts between skills instead of hiding them. Impeccable
detector results remain upstream Impeccable results, not Gogh-owned findings.
License, version, star, and rule claims are treated as current only when backed
by the source ledger.

## Maturity Gates

1. Scaffolded: product shell, vault, source pack, scripts, tests, and demo exist.
2. Researched: dated trustworthy sources replace placeholder research.
3. Domain-adapted: real domain importer, synthesis, reports, fixtures, and tests exist.
4. Demo-verified: sample vault regenerates deterministically and reports cite sources.
5. Market-ready: audit score is at least 90 with no critical failures.

Scores are capped by maturity. A scaffold cannot become market-ready by edited
markdown alone.

## Research Policy

Use official, primary, or vendor documentation first. Use market or practitioner
sources only as supporting evidence. Do not treat blog roundups or AI summaries
as primary truth. Record evidence in `references/source-ledger.json`; prose-only
research notes do not satisfy the gate.

## Release

```bash
python scripts/package_release.py --version 1.0.0 --release-type market-ready
```

Release packaging scans for secrets, local paths, symlinks, untracked drift,
and unsafe ZIP entries before writing `dist/RELEASE_MANIFEST.json` and
`dist/SHA256SUMS`. Market-ready packaging also runs `scripts/audit_brain.py`.
