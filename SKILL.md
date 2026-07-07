---
name: gogh-brain
description: >
  Scaffold and operate Gogh, a source-cited Obsidian brain for design skill stack
  advice across six frontend design skills: taste-skill v2,
  make-interfaces-feel-better, Impeccable, Anthropic frontend-design,
  ui-ux-pro-max, and Vercel web-design-guidelines. Use when the user says
  "gogh", "gogh-brain", "design skill stack", "anti-slop frontend",
  "which design skill", "stack design skills", any of the six skill names, or
  wants stack recommendations, conflict resolution, unified anti-slop rules,
  audits, or a maintained vault-backed design skill brain.
argument-hint: "new | ingest | synthesize | report | visuals | lint | next | registry | diff | advise"
license: Apache-2.0
---

# Gogh

Gogh is a six-skill frontend design stack brain for AI coding agents. It helps
operators choose which design skill to use when, combine them into one advisable
stack, resolve conflicts, and keep anti-slop frontend guidance source-cited.

Operate the vault first. Read `CODEX.md`, `wiki/hot.md`, and `wiki/index.md`
before changing notes.

Buyer, outputs, boundaries, quick start, and maturity details live in
`README.md`.

## Commands

```bash
/gogh-brain new <client-slug> --owner <name>
/gogh-brain ingest --vault <path> --file <source>
/gogh-brain synthesize --vault <path>
/gogh-brain report --vault <path>
/gogh-brain visuals --vault <path>
/gogh-brain lint --vault <path>
/gogh-brain next --vault <path>
/gogh-brain registry --vault <path>
/gogh-brain diff --vault <path> --against <capture>
/gogh-brain advise --vault <path> --brief <file>
```

Source checkout equivalent:

```bash
gogh-brain new <client-slug> --owner <name>
gogh-brain ingest --vault <path> --file <source>
gogh-brain synthesize --vault <path>
gogh-brain report --vault <path> --html-only
gogh-brain advise --vault <path> --brief <file>
```

## Required Operating Rules

1. Read `<vault>/CODEX.md`.
2. Read `<vault>/wiki/hot.md`.
3. Read `<vault>/wiki/index.md`.
4. Preserve `.raw/` as immutable source material.
5. Never store credentials in the vault.
6. Never make domain-specific claims without dated trustworthy sources.
7. Keep `hot`, `index`, `overview`, and `log` current.
8. Record research evidence in `references/source-ledger.json`.
9. Record domain adapter completion in `references/adapter-manifest.json`.

## Script Mapping

| Command | Script | Note |
|---|---|---|
| `new` | `python scripts/scaffold_vault.py` |  |
| `ingest` | `python scripts/ingest_source.py` |  |
| `synthesize` | `python scripts/synthesize_brain.py` |  |
| `report` | `python scripts/render_brain_report.py` |  |
| `visuals` | `python scripts/generate_vault_visuals.py` |  |
| `lint` | `python scripts/lint_vault.py` |  |
| `next` | `python scripts/guide_next_action.py` |  |
| `registry` | `python scripts/import_skill_capture.py` | (land in the adapter wave) |
| `diff` | `python scripts/import_skill_capture.py` | (land in the adapter wave) |
| `advise` | `python scripts/render_stack_advisor.py` | (land in the adapter wave) |

## Quality Gates

- No invented rules, thresholds, or dial values. Every rule cites a canonical upstream capture or source-ledger entry, and unverified claims are marked as such
- No shipping past a failed audit or an unrun Section 14 pre-flight check
- On redesigns, no destruction of existing URLs, routes, or brand identity without an explicit modernization-mode decision
- No copying of a client's real API keys, private briefs, or unreleased assets into brain notes

Do not call this brain market-ready unless `scripts/audit_brain.py --require
market-ready` passes. A scaffold is not a finished brain.

## Research Refresh

on-changelog or release watch for taste-skill, make-interfaces-feel-better,
Impeccable, Anthropic frontend-design, ui-ux-pro-max, and Vercel
web-design-guidelines; monthly for rule captures, stack conflicts, and dial
defaults; quarterly for ecosystem coverage and the Agent Skills / SKILL.md
format
