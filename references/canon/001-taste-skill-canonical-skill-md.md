# Taste Skill Canonical SKILL.md

Title: tasteskill: Anti-Slop Frontend Skill
Author: Leon Lin
Year: 2026
Distillation status: primary capture
Source URLs:
- https://raw.githubusercontent.com/Leonxlnx/taste-skill/main/skills/taste-skill/SKILL.md, retrieved 2026-07-07
- https://www.tasteskill.dev/guide?view=full, retrieved 2026-07-07
- https://github.com/Leonxlnx/taste-skill, retrieved 2026-07-07
Capture paths:
- .raw/skills/taste-skill-v2/SKILL.md
- .raw/research/official-site-extract.md
- .raw/research/github-repo-extract.md

## Why canonical

This is Gogh's primary upstream ruleset for stopping landing pages, portfolios, and redesigns from collapsing into templated AI output. It matters because it converts taste into explicit operating constraints: read the brief, set three dials, preserve identity on redesigns, ban known tells, and block completion until the final pre-flight passes. It also defines Gogh's main boundary: useful for marketing and portfolio surfaces, not a universal dashboard or product-UI rulebook.

## Distilled principles

1. Read the room before touching layout. Page kind, audience, brand assets, references, regulatory context, and vibe words determine the design direction.
2. Declare a one-line design read before implementation so the aesthetic premise is explicit and reviewable.
3. Ask one clarifying question when the brief genuinely forks; otherwise proceed from the inferred design read.
4. Treat the three dials as conversational controls, not file edits: `DESIGN_VARIANCE`, `MOTION_INTENSITY`, and `VISUAL_DENSITY`.
5. Use the baseline 8 / 6 / 4 for marketing work, then adjust by page type, audience risk, and project constraints.
6. Use real design systems when the brief names an ecosystem or regulated context; otherwise choose an aesthetic family directly.
7. Avoid AI defaults unless the brief justifies them: purple glow, centered mesh hero, three equal feature cards, glass everywhere, infinite loops, and default Inter.
8. Lock color, shape, and page theme. One accent, one radius system, and one light or dark strategy should govern the whole page.
9. Make hero sections fit the first viewport: short headline, short subtext, visible CTA, restrained top padding, and no trust-logo clutter inside the hero.
10. Keep desktop navigation on one line with a tight height cap.
11. Vary section layout families. An eight-section page needs at least four families, and repeated zigzags or repeated card grids fail the brief.
12. Match bento cell count to content count. Empty cells are a planning bug, not a design feature.
13. Use real visuals. Text-only marketing pages, CSS-only fake screenshots, and product previews made from random divs are treated as incomplete.
14. Respect motion claims. If the motion dial is above 4, the page must actually move, and motion above 3 must honor reduced-motion preferences.
15. For redesigns, detect mode first: Greenfield, Preserve, or Overhaul. Preserve slugs, IA, primary nav labels, key flows, and accessibility wins unless asked.
16. Ban visible em dash and en dash characters. Use ASCII hyphens for ranges and separators.
17. Run Section 14 as a blocking final gate. Any failed box means the work is not done.
18. Say when a request is out of scope, then apply only the parts that fit the surface.

## How Gogh uses it

This work underpins wiki/skills/Taste Skill (Project).md, wiki/concepts/The Three Dials.md, wiki/concepts/DESIGN_VARIANCE.md, wiki/concepts/MOTION_INTENSITY.md, wiki/concepts/VISUAL_DENSITY.md, wiki/concepts/Constraint Beats Coaxing.md, wiki/flows/Greenfield Build (Prompt 1).md, wiki/flows/Audit-First Redesign (Prompt 2).md, wiki/flows/Modernization Modes.md, and wiki/audits/Pre-Flight Check (Section 14).md.

Mechanically, Gogh uses it as the macro taste layer: dial tuning, anti-default bans, hero and nav discipline, layout variance, redesign preservation, image-first expectations, and the final blocking audit.
