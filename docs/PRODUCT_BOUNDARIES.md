# Product Boundaries

Gogh is an advisory, read-only Obsidian brain for stacking six frontend design
skills for AI coding agents: taste-skill v2,
make-interfaces-feel-better, Impeccable, Anthropic frontend-design,
ui-ux-pro-max, and Vercel web-design-guidelines. It recommends which skill to
use when, how to combine them, where they conflict, and which audits should
gate shipping.

## It Does

- Preserve raw sources under `.raw/`.
- Synthesize source-cited notes and deliverables.
- Maintain action queues, reports, and next actions.
- Keep decisions auditable through source links and rollback notes.
- Produce advisory stack guidance, dial settings, conflict notes, and
  pre-flight checklists.
- Gate maturity through `references/source-ledger.json`,
  `references/adapter-manifest.json`, and `scripts/audit_brain.py`.

## It Does Not

- Invent rules, thresholds, dial values, licenses, or version claims without a
  dated source.
- Hide conflicts between upstream skills.
- Treat Impeccable detector results as Gogh-owned findings.
- Ship past a failed audit or an unrun required pre-flight check.
- Destroy existing URLs, routes, or brand identity without an explicit
  modernization-mode decision.
- Copy a client's real API keys, private briefs, or unreleased assets into
  brain notes.
- Mutate accounts, systems, repositories, production apps, customer records, or
  publishing pipelines in V1.

## Safety Risks

- Stale rules after any of the six upstream skills releases new guidance.
- Conflicting guidance between skills. Gogh records conflicts, it does not hide
  them.
- Impeccable detector results are upstream's, not ours.
- Cargo-culting the stack into contexts where one or more skills do not fit.
- Treating the brain as a component library rather than an advisory constraint
  and audit layer.
- Leaking a client's private brief, URLs, or credentials into notes

## Maturity Boundary

This repo is currently `researched`. Market-ready quality requires current
six-skill research, domain adapters, deterministic demo verification, source
citations, Obsidian graph hygiene, and release scans. The audit score is capped
below 90 until those stages are complete.
