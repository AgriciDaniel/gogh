# Details That Make Interfaces Feel Better

Title: Details That Make Interfaces Feel Better
Author: Jakub Krehel
Year: 2026 or earlier, article date not displayed in local capture
Distillation status: primary article extract plus primary skill captures
Source URLs:
- https://jakub.kr/writing/details-that-make-interfaces-feel-better, retrieved 2026-07-07
- https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/skills/make-interfaces-feel-better/SKILL.md, retrieved 2026-07-07
- https://github.com/jakubkrehel/make-interfaces-feel-better, retrieved 2026-07-07
Capture paths:
- .raw/research/krehel-article-extract.md
- .raw/skills/make-interfaces-feel-better/SKILL.md
- .raw/skills/make-interfaces-feel-better/typography.md
- .raw/skills/make-interfaces-feel-better/surfaces.md
- .raw/skills/make-interfaces-feel-better/animations.md
- .raw/skills/make-interfaces-feel-better/performance.md

## Why canonical

Krehel's article and derived skill define the micro-feel doctrine for Gogh: perceived polish comes from many small details that compound. The work is canonical because it makes that doctrine executable through exact surface, typography, interaction, animation, and performance choices. It complements taste-skill's macro direction by fixing the last 10 percent where interfaces often feel wrong.

## Distilled principles

1. Polish compounds. Do not expect one big visual move to compensate for rough spacing, motion, surfaces, and text rendering.
2. Use `text-wrap: balance` for headings and `text-wrap: pretty` for paragraphs so awkward line breaks do not undercut the composition.
3. Apply root font smoothing where appropriate so text feels crisp on macOS without changing type choices.
4. Use tabular numbers for counters, timers, prices, comparison columns, and animated values that would otherwise shift.
5. Calculate nested radii concentrically: outer radius equals inner radius plus the padding between layers.
6. Align optically when geometric centering looks wrong, especially with icons, play triangles, arrows, and icon-text buttons.
7. Prefer layered transparent shadows over hard borders for cards and buttons when depth is the goal.
8. Keep real borders for cases where borders carry semantics: dividers, table cells, and accessible input outlines.
9. Add a neutral 1px inset outline to images so photos with different brightness values sit consistently in the system.
10. Give interactive elements at least a 40x40px hit area, using a pseudo-element if the visible target is smaller.
11. Make interaction animations interruptible. Use transitions for state changes and reserve keyframes for one-shot sequences.
12. Split enter animations into semantic chunks and stagger them so the composition reads in order.
13. Keep exits subtler and shorter than entrances. A loud exit steals attention from the next state.
14. Animate contextual icons with opacity, scale, and blur rather than sudden swaps.
15. Use a press scale around 0.96, and never exaggerate below 0.95.
16. Avoid `transition: all`; name only the properties that actually change.
17. Use `will-change` sparingly and only for compositable properties such as transform, opacity, and filter.
18. Do not add a motion library just for icon transitions; use CSS cross-fade when the project does not already have Motion.

## How Gogh uses it

This work underpins wiki/skills/Make Interfaces Feel Better (Skill).md, wiki/concepts/Optical Alignment.md, wiki/audits/MIFB Review Checklist.md, wiki/rules/MIFB Typography and Numbers Rules.md, wiki/rules/MIFB Surface and Shadow Rules.md, wiki/rules/MIFB Motion and Feedback Rules.md, and wiki/rules/MIFB Performance Rules.md.

Mechanically, Gogh uses it as the craft layer after macro taste is set: radii math, image outlines, shadows, hit targets, press feedback, tabular numbers, interruptible transitions, and performance-safe animation defaults.
