---
type: "meta"
title: "CONVENTIONS"
status: "seed"
created: "2026-07-07"
updated: "2026-07-07"
tags: ["gogh/ops", "note/meta"]
domain: "ops"
confidence: "practitioner"
related: ["[[Index]]", "[[Dashboard]]", "[[Hot]]", "[[Overview]]", "[[Tag Taxonomy]]", "[[Source Manifest Guide]]"]
source_urls: []
sources: ["[[Source Manifest Guide]]"]
---

# CONVENTIONS

This page is the Gogh master contract for distributable Obsidian vault notes.

## Frontmatter

Every page uses flat YAML frontmatter.

Required fields:

- `type`: one of `skill`, `entity`, `concept`, `rule`, `audit`, `flow`, `comparison`, `reception`, `source`, `decision`, `deliverable`, `question`, `gap`, `experiment`, or `meta`.
- `title`: quoted Title Case, unique, and matching the filename unless a required filename uses another case.
- `status`: one of `seed`, `developing`, `mature`, or `evergreen`.
- `created`: ISO date.
- `updated`: ISO date.
- `tags`: exactly one `gogh/<domain>` tag plus one `note/<type>` tag.
- `domain`: one of `taste-skill`, `mifb`, `impeccable`, `frontend-design`, `ui-ux-pro-max`, `web-design-guidelines`, `stack`, `theory`, or `ops`.
- `confidence`: one of `evidence-based`, `practitioner`, `contested`, or `folklore`.
- `related`: minimum 6 quoted wikilinks.
- `source_urls`: source URLs ending with `(retrieved YYYY-MM-DD)`.
- `sources`: quoted wikilinks to notes in `wiki/sources/`.

Decision and flow notes that recommend mutations also include:

- `approval_status`
- `risk_level`
- `rollback_note`

## Body Contract

Atomic notes open with an answer-first sentence.

Atomic notes then use these sections in order:

1. `## What it is`
2. `## How it works`
3. `## Best practice`
4. `## Pitfalls`
5. `## Sources`
6. `## Related`
7. `## Next actions`

Every `Best practice` bullet ends with one evidence marker:

- `EVIDENCE-BASED`
- `PRACTITIONER`
- `CONTESTED`
- `FOLKLORE`

Atomic notes have a 90 line floor. Hubs and meta pages are exempt from that floor.

## Hub Contract

Each typed folder has one `_index.md` hub page.

Each hub page uses `type: "meta"` and contains:

- A one-line purpose.
- A `## Catalog` section.
- An otherwise empty catalog with a template row.

## Callouts

Allowed callouts:

> [!contradiction]

> [!gap]

> [!key-insight]

> [!stale]

## Quotes

Quotes copied verbatim are capped at 15 words and need attribution.

## Naming

Filenames use Title Case unless a required project file has a fixed name.

Folders use lowercase.

Wikilinks are path-less except cross-folder hub links.

Visible prose never uses the em dash glyph. Refer to the codepoint by name as `U+2014` when documenting the rule.

## Related

- [[Tag Taxonomy]] sets the allowed domain tags and graph colors.
- [[Source Manifest Guide]] defines raw source provenance expectations.
- [[Index]] links the active hub set.
- [[Dashboard]] gives operators the current navigation surface.
- [[Hot]] points to the next operating action.
- [[Overview]] states the product context.

## Next Actions

- Apply this contract to newly created atomic notes.
- Keep generated scaffold notes contract-compatible where scripts allow it.
- Use `python scripts/lint_vault.py --vault assets/template-brain --template` before release packaging.
