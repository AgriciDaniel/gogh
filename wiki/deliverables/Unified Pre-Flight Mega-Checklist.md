---
type: "deliverable"
title: "Unified Pre-Flight Mega-Checklist"
status: "developing"
created: "2026-07-07"
updated: "2026-07-07"
tags: ["gogh/stack", "note/deliverable"]
domain: "stack"
confidence: "evidence-based"
related: ["[[Enforcement Layer Overlap]]", "[[Audit Pipeline Flow]]", "[[Pre-Flight Check (Section 14)]]", "[[MIFB Review Checklist]]", "[[Impeccable Audit and Detect]]", "[[Required Audits]]", "[[Unified Anti-Slop Rulebook]]", "[[Full Stack Build Flow]]"]
source_urls: ["https://raw.githubusercontent.com/Leonxlnx/taste-skill/main/skills/taste-skill/SKILL.md (retrieved 2026-07-07)", "https://github.com/pbakaus/impeccable (retrieved 2026-07-07)", "https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md (retrieved 2026-07-07)", "https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/skills/make-interfaces-feel-better/SKILL.md (retrieved 2026-07-07)", "https://github.com/nextlevelbuilder/ui-ux-pro-max-skill (retrieved 2026-07-07)"]
sources: ["[[Canonical Skill File]]", "[[Impeccable Repo and Site]]", "[[MIFB Repo and Skill File]]", "[[UI UX Pro Max Repo]]", "[[Reception Sources]]"]
---
Unified Pre-Flight Mega-Checklist merges Section 14, MIFB review, Impeccable detect, Vercel guidelines, and UI UX Pro Max checklist rows into one deduplicated release screen.

## What it is
This deliverable is a merged checklist.
The merge follows Enforcement Layer Overlap.
Taste Skill rows are blocking when Taste Skill is active.
Impeccable rows are gate rows when detect or hooks are configured.
Vercel rows are audit rows for file:line findings.
MIFB rows are advisory polish rows unless promoted by project policy.
UI UX Pro Max rows are retrieval or checklist rows.
The checklist avoids duplicating the same motion, touch, or focus requirement under multiple headings.
Each row carries a source skill tag.
The checklist is not a new upstream rule source.
The checklist should be refreshed after source-ledger updates.
The checklist keeps exact counts dated where they appear.

## How it works
| Gate | Check | Source skill |
|---|---|---|
| Block | Section 14 boxes are all Pass when Taste Skill was used | Taste Skill |
| Block | Hero headline is max 2 lines | Taste Skill |
| Block | Hero subtext is max 20 words and CTA is visible without scroll | Taste Skill |
| Block | Hero top padding does not exceed `pt-24` on desktop | Taste Skill |
| Block | Hero contains max 4 text elements | Taste Skill |
| Block | No visible U+2014 or U+2013 characters | Taste Skill |
| Block | No div-based fake screenshots or fake product UI | Taste Skill |
| Block | Real images or explicit placeholder slots are used | Taste Skill |
| Block | No AI-purple default gradient or automatic purple glow | Taste Skill |
| Block | Premium consumer palette is not default beige plus brass unless brief-led | Taste Skill |
| Block | Shape consistency lock is followed | Taste Skill |
| Block | Bento grids have exactly as many cells as content items | Taste Skill |
| Block | An 8-section page uses at least 4 layout families | Taste Skill |
| Block | Motion above low intensity honors reduced motion | Taste Skill |
| Gate | Run Impeccable detect on relevant UI files when installed | Impeccable |
| Gate | Resolve overused font detector findings or record an ignore reason | Impeccable |
| Gate | Resolve purple gradient and gradient text findings | Impeccable |
| Gate | Resolve nested card and card-overuse findings | Impeccable |
| Gate | Resolve gray text on color and contrast findings | Impeccable |
| Gate | Resolve small touch target findings | Impeccable |
| Gate | Keep PRODUCT.md and DESIGN.md context current when Impeccable is used | Impeccable |
| Gate | Run Vercel web-design-guidelines on changed files or target pattern | Vercel |
| Gate | Icon-only buttons have accessible labels | Vercel |
| Gate | Focus outlines are not removed without replacement | Vercel |
| Gate | Forms do not block paste and report inline errors | Vercel |
| Gate | Animation honors prefers-reduced-motion | Vercel |
| Gate | No `transition: all` remains in audited UI | Vercel |
| Gate | Large lists are virtualized when Vercel rule applies | Vercel |
| Gate | Images reserve width and height to prevent CLS | Vercel |
| Advise | Nested radii are concentric for close surfaces | MIFB |
| Advise | Buttons use press scale 0.96 and not below 0.95 | MIFB |
| Advise | Interactive elements have at least 40x40px hit areas | MIFB |
| Advise | Enter and exit animations are interruptible where interactive | MIFB |
| Advise | Icon swaps use opacity, scale, and blur values from MIFB when applicable | MIFB |
| Advise | Shadows are preferred over borders when surface depth is intended | MIFB |
| Advise | Tabular numbers are used for changing or comparable numbers | MIFB |
| Advise | Search or retrieve style, palette, typography, UX, chart, or stack guidance when brand maturity is low | UI UX Pro Max |
| Advise | No emoji are used as structural icons | UI UX Pro Max |
| Advise | Touch target and semantic native control checklist rows are reviewed | UI UX Pro Max |

## Best practice
- Use the Block rows as hard gates when their source skill is active EVIDENCE-BASED
- Use Impeccable gate rows only when Impeccable detect or hooks are installed EVIDENCE-BASED
- Use Vercel gate rows for target files under audit EVIDENCE-BASED
- Use MIFB rows as advisory polish unless project policy promotes them PRACTITIONER
- Use UI UX Pro Max rows as retrieval and checklist support EVIDENCE-BASED
- Keep duplicate reduced-motion checks as one requirement with multiple sources EVIDENCE-BASED
- Keep duplicate touch target checks as one requirement with source-specific values EVIDENCE-BASED
- Record waivers in contracts or tool ignore mechanisms PRACTITIONER
- Re-run gates after visual or interaction fixes PRACTITIONER
- Do not call a skipped gate passed EVIDENCE-BASED

## Pitfalls
Applying every row to every project can over-gate small changes.
Using MIFB advisory rows as universal blockers can overstate source behavior.
Using Vercel audit rows before files exist can create fake findings.
Using Impeccable rows without install can create unactionable checklist items.
Using Taste Skill hero rows on a dashboard can conflict with Taste Skill scope.
Merging reduced-motion rows can hide the source that made it blocking.
Merging touch target rows can hide the 40x40px versus 44x44px distinction.
Ignoring waivers can make legitimate brand choices fail repeatedly.
Ignoring source dates can stale detector and database counts.
Treating this deliverable as a source would invert the evidence chain.

## Distinctiveness gate (runs last, blocks shipping)

The mechanical sections above are the floor. This section is the bar, added
after the claude-ads run 1 retrospective (operator score 3/10 on a page that
passed every mechanical check). Full procedure: [[Distinctiveness Audit]].

- [ ] A written [[Aesthetic Direction Commitment]] exists and predates the build (source: Gogh)
- [ ] Five-second test passes: the page is describable as itself, not as its category (source: Gogh)
- [ ] One screenshotable signature element is nameable (source: Gogh)
- [ ] Transform briefs only: side-by-side with the incumbent reads as a new direction, not a tidy-up (source: Gogh)
- [ ] The layout could not ship for a competitor with only copy and logo swapped (source: Gogh)
- [ ] DESIGN_VARIANCE receipts: the set variance level is visible in the layout choices (source: taste-skill)

## Sources
- Taste Skill SKILL.md, https://raw.githubusercontent.com/Leonxlnx/taste-skill/main/skills/taste-skill/SKILL.md, retrieved 2026-07-07.
- Impeccable README, https://github.com/pbakaus/impeccable, retrieved 2026-07-07.
- Vercel command.md, https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md, retrieved 2026-07-07.
- MIFB SKILL.md and reference files, https://github.com/jakubkrehel/make-interfaces-feel-better, retrieved 2026-07-07.
- UI UX Pro Max SKILL.md, https://github.com/nextlevelbuilder/ui-ux-pro-max-skill, retrieved 2026-07-07.
- Enforcement Layer Overlap, wiki/comparisons/Enforcement Layer Overlap.md, created 2026-07-07.
- Claim packs, references/claim-packs, generated 2026-07-07.

## Related
- [[Enforcement Layer Overlap]] explains the dedupe matrix.
- [[Audit Pipeline Flow]] gives execution order.
- [[Pre-Flight Check (Section 14)]] is the Taste Skill gate.
- [[MIFB Review Checklist]] is the MIFB review surface.
- [[Impeccable Audit and Detect]] is the detector source.
- [[Required Audits]] is the existing audit reference.
- [[Unified Anti-Slop Rulebook]] supplies merged ban context.
- [[Full Stack Build Flow]] shows where this checklist lands after build.
- [[Gogh Quickstart]] uses this checklist in the first-project walkthrough.
- [[Design Review as Infrastructure]] explains why pre-flight checks matter.

## Next actions
- Re-run this checklist after any UI fix.
- Keep row severity tied to source skill behavior.
- Refresh Impeccable and Vercel rows after upstream release changes.
- Add missing Vercel source-note link when that source note exists.
- Do not use this checklist to bypass source-specific notes.

