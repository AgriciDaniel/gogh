---
type: "entity"
title: "The 13 Skills"
created: "2026-07-06"
updated: "2026-07-06"
status: "active"
confidence: "EVIDENCE-BASED"
---

# The 13 Skills

Confidence tag: EVIDENCE-BASED (repo `skill.sh` / `llms.txt` / `tasteskill.dev`).

## Compiled Truth

Taste Skill is a **suite**, not a single file - a design consequence of [[Agent Skills Format|progressive disclosure]] (each is a separately discoverable skill). Folder | install name | role:

| Skill | Install name | Role |
|---|---|---|
| `taste-skill` | `design-taste-frontend` | **v2 canonical** - the main anti-slop ruleset. |
| `taste-skill-v1` | `design-taste-frontend-v1` | Original v1, preserved; same 8/6/4 dials, leaner rules. |
| `gpt-tasteskill` | `gpt-taste` | Stricter GPT/Codex variant; Python "true randomization" in a `<design_plan>`, AIDA structure, no emojis. |
| `image-to-code-skill` | `image-to-code` | Image-first: generate references -> analyze -> implement to match. |
| `imagegen-frontend-web` | `imagegen-frontend-web` | Premium website reference images, one horizontal per section. |
| `imagegen-frontend-mobile` | `imagegen-frontend-mobile` | Phone-mockup screen concepts (images only). |
| `brandkit` | `brandkit` | Brand-kit boards: logo, palette, type, mockups (images only). |
| `soft-skill` | `high-end-visual-design` | "$150k+ agency" look; spring motion; "Absolute Zero" anti-pattern. |
| `minimalist-skill` | `minimalist-ui` | Notion/Linear editorial; bans Inter/Roboto/Open Sans. |
| `brutalist-skill` | `industrial-brutalist-ui` | Swiss type + terminal; CRT scanlines (Beta). |
| `output-skill` | `full-output-enforcement` | Anti-laziness: bans `// ...`, placeholder-comment stubs, and "for brevity"; `[PAUSED - X of Y]` continuation. |
| `redesign-skill` | `redesign-existing-projects` | Scan -> Diagnose -> Fix for existing codebases. |
| `stitch-skill` | `stitch-design-taste` | Google Stitch-compatible; exports a `DESIGN.md`. |

The image skills (`imagegen-*`, `brandkit`, `image-to-code`) power the [[Image-First Pipeline]]. `output-skill` is the anti-laziness enforcer backed by the repo's `research/laziness/` study - see [[Anti-Laziness Research]].

## Related

- [[Taste Skill (Project)]] | [[Image-First Pipeline]] | [[Anti-Laziness Research]] | [[Install and Load]]
- Source: [[Canonical Skill File|Canonical SKILL.md]]

## Timeline

- 2026-07-06 - Note created.
