---
name: gogh-brain
description: >
  Scaffold and operate Gogh, a source-cited Obsidian brain about
  the open-source Taste Skill framework by Leon Lin — the anti-slop SKILL.md
  ruleset that gives AI coding agents (Claude Code, Cursor, Codex) good frontend
  taste via three design dials (DESIGN_VARIANCE, MOTION_INTENSITY, VISUAL_DENSITY),
  audit-first redesigns, an image-first reference pipeline, anti-laziness rules,
  and a strict pre-flight check. Use when the user says "gogh-brain",
  "Gogh", "taste skill", "anti-slop frontend", asks about the three
  dials, the redesign audit, the pre-flight check, or wants to install, load, and
  operate the Taste Skill in an agent, or maintain this vault-backed brain.
argument-hint: "new | ingest | synthesize | report | visuals | lint | next"
license: Apache-2.0
---

# Gogh

Operate the vault first. Read `CODEX.md`, `wiki/hot.md`, and `wiki/index.md`
before changing notes.

## Commands

```bash
/gogh-brain new <client-slug> --owner <name>
/gogh-brain ingest --vault <path> --file <source>
/gogh-brain synthesize --vault <path>
/gogh-brain report --vault <path>
/gogh-brain visuals --vault <path>
/gogh-brain lint --vault <path>
/gogh-brain next --vault <path>
```

Source checkout equivalent:

```bash
gogh-brain new <client-slug> --owner <name>
gogh-brain ingest --vault <path> --file <source>
gogh-brain synthesize --vault <path>
gogh-brain report --vault <path> --html-only
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

- `new` -> `python scripts/scaffold_vault.py`
- `ingest` -> `python scripts/ingest_source.py`
- `synthesize` -> `python scripts/synthesize_brain.py`
- `report` -> `python scripts/render_brain_report.py`
- `visuals` -> `python scripts/generate_vault_visuals.py`
- `lint` -> `python scripts/lint_vault.py`
- `next` -> `python scripts/guide_next_action.py`

## Quality Gates

- No invented rules, thresholds, or dial values — every rule cites the canonical SKILL.md or tasteskill.dev, and unverified claims are marked as such
- No shipping past a failed audit or an unrun Section 14 pre-flight check
- On redesigns, no destruction of existing URLs, routes, or brand identity without an explicit modernization-mode decision
- No copying of a client's real API keys, private briefs, or unreleased assets into brain notes

Do not call this brain market-ready unless `scripts/audit_brain.py --require
market-ready` passes. A scaffold is not a finished brain.

## Research Refresh

on-changelog for github.com/Leonxlnx/taste-skill and tasteskill.dev/changelog; monthly for the SKILL.md rules and the three dials; quarterly for ecosystem coverage (Emil Kowalski, Developers Digest, skill directories) and the Anthropic Agent Skills / SKILL.md format
