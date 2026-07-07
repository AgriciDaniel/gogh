# Make Interfaces Feel Better Skill Extract
Captured: 2026-07-07
Sources: https://github.com/jakubkrehel/make-interfaces-feel-better (retrieved 2026-07-07); https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/skills/make-interfaces-feel-better/SKILL.md (retrieved 2026-07-07); https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/README.md (retrieved 2026-07-07); https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/skills/make-interfaces-feel-better/typography.md (retrieved 2026-07-07); https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/skills/make-interfaces-feel-better/surfaces.md (retrieved 2026-07-07); https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/skills/make-interfaces-feel-better/animations.md (retrieved 2026-07-07); https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/skills/make-interfaces-feel-better/performance.md (retrieved 2026-07-07); https://api.github.com/repos/jakubkrehel/make-interfaces-feel-better (retrieved 2026-07-07)
Source type: primary

## Identity and Stats
- Repo: jakubkrehel/make-interfaces-feel-better. Description: "An agent skill based on the 'Details that make interfaces feel better' article".
- Stars 2,241, forks 78 (GitHub API, 2026-07-07). Created 2026-03-13, last push 2026-04-19.
- License: README states MIT License; the GitHub API reports no license file detected (discrepancy noted at capture).
- Install: `npx skills add jakubkrehel/make-interfaces-feel-better`. Manual invocation: `/make-interfaces-feel-better`. Auto-applies during UI building, frontend code review, and animation work.
- Skill description triggers on: UI polish, design details, "make it feel better", "feels off", stagger animations, border radius, optical alignment, font smoothing, tabular numbers, image outlines, box shadows.

## Repository Structure
- `.gitignore`, `README.md`
- `skills/make-interfaces-feel-better/SKILL.md` (core skill)
- `skills/make-interfaces-feel-better/animations.md`, `performance.md`, `surfaces.md`, `typography.md` (4 reference files)

## Core Principles with Values (15, across 4 categories)
Surfaces:
1. Concentric border radius: `outerRadius = innerRadius + padding`. Example: outer 20px, padding 8px, inner 12px. Apply when nesting padding is 24px or less; larger gaps are separate surfaces. Mismatched concentric radii named the primary culprit behind interfaces that "feel off".
2. Optical alignment over geometric: icon-side padding = text-side padding minus 2px on icon+text buttons; play-button triangle shifted 2px right (`margin-left: 2px`); prefer fixing asymmetric icons in the SVG viewBox/path itself.
3. Shadows instead of borders. Light mode 3-layer stack: `0px 0px 0px 1px rgba(0,0,0,0.06), 0px 1px 2px -1px rgba(0,0,0,0.06), 0px 2px 4px 0px rgba(0,0,0,0.04)`. Dark mode single ring: `0 0 0 1px rgba(255,255,255,0.08)`. Hover transitions via `transition-[box-shadow] 150ms ease-out`. Keep real borders for dividers, table cells, input outlines.
4. Image outlines: `outline: 1px solid rgba(0,0,0,0.1)` with `outline-offset: -1px` (inset); dark mode `rgba(255,255,255,0.1)`. Pure black/white only, never palette grays or accent colors.
5. Hit areas: WCAG standard 44x44px, practical minimum 40x40px; extend small controls with an `::after` pseudo-element; avoid overlapping hit areas.
Typography:
6. `text-wrap: balance` on headings (engine limits: 6 lines Chromium, 10 lines Firefox); `text-wrap: pretty` on paragraphs/captions/card text; default wrapping for 10+ line text and code blocks.
7. Font smoothing at root only: `-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale` (macOS effect; other platforms ignore).
8. Tabular numbers: `font-variant-numeric: tabular-nums` for counters, prices, tables; skip for static numbers and version strings. Inter intentionally alters digit 1 width under tabular-nums.
Animations:
9. Interruptible animations: CSS transitions for interactive state changes (retargetable mid-animation); keyframes reserved for one-shot sequences.
10. Enter animations: split into logical groups, stagger ~100ms per group (80ms for individual words); from `opacity: 0; translateY(12px); blur(4px)` to identity; 300-400ms, ease-out.
11. Exit animations softer than enters: 150ms ease-in (vs 300ms enter), `opacity: 0; translateY(-12px); blur(4px)`; avoid full-height collapse.
12. Contextual icon animations, exact mandated values: scale 0.25 to 1, opacity 0 to 1, blur 4px to 0px; spring `{ type: "spring", duration: 0.3, bounce: 0 }` with Motion/AnimatePresence; CSS-only fallback keeps both icons in DOM and cross-fades with `cubic-bezier(0.2, 0, 0, 1)`. SKILL.md: "do not deviate".
13. Scale on press: exactly `scale(0.96)`; never below 0.95 (below "feels exaggerated"); `transition: scale 150ms ease-out` so release mid-press interrupts smoothly.
14. Skip animation on page load: `initial={false}` on `AnimatePresence` for default-state elements (toggles, tabs), not entrance sequences.
Performance:
15. Transition specificity and `will-change`: never `transition: all`; list properties (`transition-[scale,background-color]`); `will-change` only on GPU-compositable properties (transform, opacity, filter, clip-path), only when first-frame stutter is observed, never `will-change: all`.

## Quick Reference Table (verbatim rows)
| Category | When to Use |
| Typography | Text wrapping, font smoothing, tabular numbers |
| Surfaces | Border radius, optical alignment, shadows, image outlines, hit areas |
| Animations | Interruptible animations, enter/exit transitions, icon animations, scale on press |
| Performance | Transition specificity, `will-change` usage |

## Common Mistakes Table (10 rows retrieved 2026-07-07)
| Mistake | Fix |
| Same border radius on parent and child | Calculate `outerRadius = innerRadius + padding` |
| Icons look off-center | Adjust optically with padding or fix SVG directly |
| Hard borders between sections | Use layered `box-shadow` with transparency |
| Jarring enter/exit animations | Split, stagger, and keep exits subtle |
| Numbers cause layout shift | Apply `tabular-nums` |
| Heavy text on macOS | Apply `antialiased` to root |
| Animation plays on page load | Add `initial={false}` to `AnimatePresence` |
| `transition: all` on elements | Specify exact properties |
| First-frame animation stutter | Add `will-change: transform` (sparingly) |
| Tiny hit areas on small controls | Extend with pseudo-element to 40x40px |

## Review Output Format
Present all changes in markdown tables with Before/After columns; group by principle using headings; one difference per row; omit tables where no changes apply.

## Review Checklist (14 items)
1. Nested rounded elements use concentric border radius
2. Icons are optically centered, not just geometrically
3. Shadows used instead of borders where appropriate
4. Enter animations are split and staggered
5. Exit animations are subtle
6. Dynamic numbers use tabular-nums
7. Font smoothing is applied
8. Headings use text-wrap: balance
9. Images have subtle outlines
10. Buttons use scale on press where appropriate
11. AnimatePresence uses `initial={false}` for default-state elements
12. No `transition: all`, only specific properties
13. `will-change` only on transform/opacity/filter, never `all`
14. Interactive elements have at least 40x40px hit area

## Reference Files (content summaries)
- typography.md: text-wrap balance/pretty with engine line limits, root-level font smoothing CSS, tabular-nums scope and Inter caveat.
- surfaces.md: concentric radius formula plus 24px-padding cutoff, 2px optical-alignment adjustments, 3-layer light / 1-ring dark shadow recipes, inset 1px image outlines, 44px WCAG vs 40px practical hit areas.
- animations.md: transitions-vs-keyframes rule, enter values (12px/4px blur/300-400ms/100ms stagger), exit values (150ms, -12px), exact icon-animation values and spring config, scale(0.96) press, `initial={false}`.
- performance.md: explicit transition-property lists, GPU-compositable `will-change` whitelist, memory cost warning, Safari benefits most from explicit hints.

## Framing Quote
SKILL.md frames polish as "a collection of small details that compound into a great experience" (Jakub Krehel, SKILL.md).
