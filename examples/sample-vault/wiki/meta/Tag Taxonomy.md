---
type: "meta"
title: "Tag Taxonomy"
status: "seed"
created: "2026-07-07"
updated: "2026-07-07"
tags: ["gogh/ops", "note/meta"]
domain: "ops"
confidence: "practitioner"
related: ["[[CONVENTIONS]]", "[[Index]]", "[[Dashboard]]", "[[Hot]]", "[[Overview]]", "[[Source Manifest Guide]]"]
source_urls: []
sources: ["[[Source Manifest Guide]]"]
---

# Tag Taxonomy

Gogh uses one domain tag and one note type tag on every contract-aware note.

## Domain Tags

| Tag | Scope | Color |
|---|---|---|
| `gogh/taste-skill` | Taste Skill v2 rules, dials, pre-flight checks, and anti-slop prompting. | `#F76707` |
| `gogh/mifb` | Make Interfaces Feel Better interaction, surface, motion, performance, and typography guidance. | `#12B886` |
| `gogh/impeccable` | Impeccable commands, detector rules, design contracts, and hook behavior. | `#7950F2` |
| `gogh/frontend-design` | Anthropic frontend-design guidance and baseline taste prompting. | `#E64980` |
| `gogh/ui-ux-pro-max` | ui-ux-pro-max retrieval, palettes, styles, font pairings, and UX rule references. | `#1C7ED6` |
| `gogh/web-design-guidelines` | Vercel web-design-guidelines audit rules and file-line findings. | `#74B816` |
| `gogh/stack` | Cross-skill sequencing, conflicts, stack recommendations, and advisor outputs. | `#FA5252` |
| `gogh/theory` | Design theory, reusable judgment models, and supporting principles. | `#FAB005` |
| `gogh/ops` | Vault operations, provenance, linting, reports, templates, and release gates. | `#868E96` |

## Add Tag Then Color Then Notes Procedure

1. Add exactly one `gogh/<domain>` tag to frontmatter.
2. Add exactly one `note/<type>` tag that matches the `type` field.
3. Confirm `assets/template-brain/.obsidian/graph.json` has the matching tag query and color.
4. Add or update notes only after the tag and graph color are in place.
5. Run the vault linter after editing the note set.

## Related

- [[CONVENTIONS]] defines the required frontmatter and body rules.
- [[Index]] lists the active hubs that use these tags.
- [[Dashboard]] links the operator surface.
- [[Source Manifest Guide]] records source provenance expectations.
- [[Hot]] names the current action path.
- [[Overview]] keeps the product scope visible.
