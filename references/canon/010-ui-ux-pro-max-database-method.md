# UI UX Pro Max Database Method

Title: UI UX Pro Max design intelligence and retrieval database method
Author: NextLevelBuilder
Year: 2025 initial repository, current captured release v2.10.2 in 2026
Distillation status: primary captures
Source URLs:
- https://github.com/nextlevelbuilder/ui-ux-pro-max-skill, retrieved 2026-07-07
- https://raw.githubusercontent.com/nextlevelbuilder/ui-ux-pro-max-skill/main/README.md, retrieved 2026-07-07
- https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/releases, retrieved 2026-07-07
Capture paths:
- .raw/skills/ui-ux-pro-max/SKILL.md
- .raw/skills/ui-ux-pro-max/README.md
- .raw/skills/ui-ux-pro-max/tree.txt
- .raw/research/ui-ux-pro-max-extract.md

## Why canonical

UI UX Pro Max is canonical because it represents a different design-skill architecture: retrieval rather than only rules or prose. It ships searchable databases for styles, palettes, font pairings, UX guidelines, chart types, product reasoning, and stack advice, then returns only the relevant slice for the task. Gogh uses it as the retrieval-database layer that expands available aesthetic options without loading every option into context.

## Distilled principles

1. Store design intelligence as searchable data when the option space is too large for a single prompt.
2. Query by product type, industry, style keywords, stack, and UI need before choosing a design direction.
3. Start with a generated design system for new pages so style, color, typography, layout, effects, and anti-patterns align.
4. Use domain searches for details after the main system is chosen: style, color, typography, chart, UX, landing, stack, web, prompt, or fonts.
5. Use BM25-style search and reasoning rules to keep retrieved context bounded and relevant.
6. Prefer retrieved design options over improvised taste when the project asks for a specific domain or platform.
7. Persist a master design system when cross-session consistency matters.
8. Use page-level overrides only for deliberate deviations from the master system.
9. Add dials for variance, motion, and density only as tuners over retrieval, not as a replacement for requirements.
10. Match the stack. React, Next.js, Vue, Svelte, Astro, SwiftUI, Flutter, React Native, Tailwind, shadcn, and HTML/CSS have different implementation constraints.
11. Use UX guidelines and anti-pattern checks before delivery, not only during planning.
12. Treat counts as dated. Styles, palettes, reasoning rules, and releases change quickly.
13. Recognize the limitation: retrieved recommendations are text and data; they do not render or visually verify themselves.
14. Combine retrieval with taste-skill or Anthropic guidance when the project still needs a committed aesthetic voice.
15. Combine retrieval with Vercel or Impeccable audits when the project needs correctness and enforcement.

## How Gogh uses it

This work underpins wiki/skills/UI UX Pro Max (Skill).md, wiki/concepts/Retrieval Database Skills.md, wiki/flows/Design System Generation Flow.md, wiki/rules/UX Rules Database (99 Rules).md, wiki/reception/Ecosystem and Alternatives.md, and wiki/sources/UI UX Pro Max Repo.md.

Mechanically, Gogh uses it as the retrieval layer: style search, palette selection, font pairing lookup, UX-rule retrieval, stack-specific guidance, design-system persistence, and dated count tracking.
