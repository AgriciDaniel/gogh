# Gogh Vault Instructions

Scope: six frontend design skills stacked into source-cited guidance for AI
coding agents.

## Read Order

1. `wiki/hot.md`
2. `wiki/index.md`
3. The relevant folder hub `_index.md`
4. The specific workflow, source, entity, decision, canvas, or deliverable note

## Vault Rules

- Preserve `.raw/` as immutable source material.
- Use flat YAML frontmatter and wikilinks.
- Keep `hot`, `index`, `overview`, and `log` current.
- Keep recommendations source-cited.
- Do not store credentials, tokens, cookies, or private secrets.
- Do not make domain-specific claims without dated trustworthy sources.
- Do not use em dash or en dash glyphs in visible prose; refer to the codepoints
  as `U+2014` and `U+2013` when documenting the rule.
- Preserve claim-ledger verdicts exactly: `CONFIRMED`,
  `CONFIRMED-AS-REPORTED`, `CONTESTED`, and `SINGLE-SOURCE`.
- Apply `shipping-rules.md` before release-affecting changes.

## Adapter Quick Commands

```bash
python scripts/import_skill_capture.py parse <capture.md> --out <parsed.json>
python scripts/import_skill_capture.py build-registry --raw-dir .raw/skills --manifest .raw/.manifest.json --out references/skill-registry.json
python scripts/import_skill_capture.py diff --old <old-capture.md> --new <new-capture.md>
python scripts/render_stack_advisor.py --brief <project-brief.json> --registry references/skill-registry.json --out <report.md>
```
