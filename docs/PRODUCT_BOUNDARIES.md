# Product Boundaries

Gogh is an advisory, read-only Obsidian brain for Giving AI coding agents good taste in frontend design using the open-source Taste Skill framework by Leon Lin — an anti-slop SKILL.md ruleset with three design dials (DESIGN_VARIANCE, MOTION_INTENSITY, VISUAL_DENSITY), audit-first redesigns, an image-first reference pipeline, anti-laziness rules, and a strict pre-flight check that make Claude Code, Cursor, and Codex produce distinctive, non-templated interfaces instead of generic AI slop..

## It Does

- Preserve raw sources under `.raw/`.
- Synthesize source-cited notes and deliverables.
- Maintain action queues, reports, and next actions.
- Keep decisions auditable through source links and rollback notes.
- Gate maturity through `references/source-ledger.json`,
  `references/adapter-manifest.json`, and `scripts/audit_brain.py`.

## It Does Not

- No invented rules, thresholds, or dial values — every rule cites the canonical SKILL.md or tasteskill.dev, and unverified claims are marked as such
- No shipping past a failed audit or an unrun Section 14 pre-flight check
- On redesigns, no destruction of existing URLs, routes, or brand identity without an explicit modernization-mode decision
- No copying of a client's real API keys, private briefs, or unreleased assets into brain notes

## Safety Risks

- Stale rules or dial values after an upstream Taste Skill release (thresholds drift, v2-experimental changes)
- Cargo-culting the rules into contexts where they do not fit (e.g. forcing 'real images only' on a data-heavy dashboard)
- Treating the skill as a component library rather than a constraint layer, or shipping without running the audits
- Leaking a client's private brief, URLs, or credentials into notes

## Maturity Boundary

This repo starts as `scaffolded`. Market-ready quality requires current
research, domain adapters, deterministic demo verification, source citations,
Obsidian graph hygiene, and release scans. The audit score is capped below 90
until those stages are complete.
