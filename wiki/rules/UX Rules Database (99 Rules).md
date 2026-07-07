---
type: "rule"
title: "UX Rules Database (99 Rules)"
status: "developing"
created: "2026-07-07"
updated: "2026-07-07"
tags: ["gogh/ui-ux-pro-max", "note/rule"]
domain: "ui-ux-pro-max"
confidence: "evidence-based"
related: ["[[UI UX Pro Max (Skill)]]", "[[Retrieval Database Skills]]", "[[Design System Generation Flow]]", "[[Required Audits]]", "[[MIFB Surface and Shadow Rules]]", "[[MIFB Motion and Feedback Rules]]", "[[MIFB Performance Rules]]", "[[Vercel Web Design Guidelines]]"]
source_urls: ["https://raw.githubusercontent.com/nextlevelbuilder/ui-ux-pro-max-skill/main/README.md (retrieved 2026-07-07)", "https://raw.githubusercontent.com/nextlevelbuilder/ui-ux-pro-max-skill/main/.claude/skills/ui-ux-pro-max/SKILL.md (retrieved 2026-07-07)", "https://github.com/nextlevelbuilder/ui-ux-pro-max-skill (retrieved 2026-07-07)", "https://github.com/wilwaldon/Claude-Code-Frontend-Design-Toolkit (retrieved 2026-07-07)", "https://lobehub.com/skills/terminalskills-skills-ui-ux-pro-max (retrieved 2026-07-07)"]
sources: ["[[UI UX Pro Max Repo]]"]
---
UX Rules Database (99 Rules) is the searchable UX guideline layer inside UI UX Pro Max, designed to retrieve relevant checks instead of loading a large rulebook into every prompt.

## What it is
The README records 99 UX Guidelines as of 2026-07-07.
The claim pack says the 99 UX guideline count is independently corroborated by the wilwaldon toolkit.
The captured SKILL.md describes the skill as containing 99 UX guidelines across priority categories.
The rule database is part of a larger bundle with 161 reasoning rules as of the 2026-07-07 README.
The 99 UX guidelines cover best practices, anti-patterns, and accessibility rules.
The captured SKILL.md priority table orders rule categories from 1 to 10.
Priority 1 is Accessibility.
Priority 2 is Touch and Interaction.
Priority 3 is Performance.
Priority 4 is Style Selection.
Priority 5 is Layout and Responsive.
Priority 6 is Typography and Color.
Priority 7 is Animation.
Priority 8 is Forms and Feedback.
Priority 9 is Navigation Patterns.
Priority 10 is Charts and Data.
Representative accessibility rules include `color-contrast`, `focus-states`, `alt-text`, `aria-labels`, `keyboard-nav`, and `reduced-motion`.
Representative touch rules include `touch-target-size`, `touch-spacing`, `hover-vs-tap`, `loading-buttons`, `cursor-pointer`, and `press-feedback`.
Representative performance rules include `image-optimization`, `image-dimension`, `font-loading`, `critical-css`, `virtualize-lists`, and `main-thread-budget`.
Representative layout rules include `viewport-meta`, `mobile-first`, `breakpoint-consistency`, `horizontal-scroll`, and `spacing-scale`.
Representative animation rules include `duration-timing`, `transform-performance`, `motion-meaning`, `interruptible`, and `no-blocking-animation`.
Representative forms rules include `input-labels`, `error-placement`, `submit-feedback`, `inline-validation`, and `focus-management`.
Representative navigation rules include `bottom-nav-limit`, `back-behavior`, `deep-linking`, `modal-escape`, and `state-preservation`.
Representative chart rules include `chart-type`, `color-guidance`, `data-table`, `legend-visible`, and `screen-reader-summary`.

## How it works
The UX rules are surfaced through search commands rather than pasted wholesale into every interaction.
The captured SKILL.md tells operators to use domain searches after generating a design system when more detail is needed.
The captured SKILL.md lists `ux` as a domain for best practices and anti-patterns.
The example domain command is `python3 skills/ui-ux-pro-max/scripts/search.py "<keyword>" --domain <domain> [-n <max_results>]`.
The captured SKILL.md recommends `--domain ux "animation accessibility z-index loading"` as a UX validation pass before implementation.
The claim pack describes the skill as a searchable design database rather than a prose rulebook.
The source ledger says CSV databases are searched with a BM25 engine across five domains in parallel.
The source ledger also says JSON reasoning rules are used for filtering and ranking.
The README describes the reasoning engine as processing decision rules with JSON conditions.
The tree capture records `ux-guidelines.csv` and `ui-reasoning.csv` as data files in the repository.
The reasoning-rules layer maps product categories to style priorities, color mood, typography mood, key effects, and anti-patterns.
The UX rule layer supplies implementation checks for accessibility, interaction, performance, layout, typography, animation, forms, navigation, and data visualization.
The Design System Generator can include pre-delivery checklist items that draw from these rule families.
The rule layer is therefore used both during generation and during final UI validation.

## Best practice
- Query the UX domain for the specific failure mode instead of loading the entire rule list into the working prompt EVIDENCE-BASED
- Run `--domain ux "animation accessibility z-index loading"` before delivery when using this skill's workflow EVIDENCE-BASED
- Treat Accessibility and Touch and Interaction as critical because the captured priority table marks them critical EVIDENCE-BASED
- Treat Performance, Style Selection, Layout and Responsive, and Navigation Patterns as high impact because the captured priority table marks them high impact EVIDENCE-BASED
- Use the representative rules as retrieval keywords when debugging a visible UI problem EVIDENCE-BASED
- Use `color-contrast`, `focus-states`, `aria-labels`, and `keyboard-nav` when auditing accessibility basics EVIDENCE-BASED
- Use `touch-target-size`, `touch-spacing`, and `press-feedback` when reviewing mobile or touch-heavy interfaces EVIDENCE-BASED
- Use `duration-timing`, `transform-performance`, and `interruptible` before adding animation polish EVIDENCE-BASED
- Cross-check retrieved UX guidance against [[MIFB Motion and Feedback Rules]] when micro-interactions are the main risk PRACTITIONER
- Cross-check retrieved UX guidance against [[Vercel Web Design Guidelines]] when web audit findings need file-line specificity PRACTITIONER

## Pitfalls
Do not treat the 99-rule count as timeless.
The README and claim pack date the count to 2026-07-07.
Do not say every rule was independently verified by a second source.
The claim pack independently corroborates the 99 count, not every individual rule body.
Do not treat the UX database as a complete accessibility standard.
The captured rules cite WCAG, Apple HIG, and Material Design in places, but the slice evidence is the skill capture rather than the full standards.
Do not let search terms hide important categories.
A query for animation can miss form, chart, or navigation defects unless the operator asks for them.
Do not collapse UX guidelines and reasoning rules into one count.
The README records 99 UX guidelines and 161 reasoning rules as distinct counts on 2026-07-07.
Do not treat app-specific checklist wording as desktop-web guidance.
The captured SKILL.md labels one common-rules section as app UI scope for iOS, Android, React Native, and Flutter.
Do not ignore reduced-motion checks when using any animation rule.

## Sources
- Raw GitHub README, https://raw.githubusercontent.com/nextlevelbuilder/ui-ux-pro-max-skill/main/README.md, retrieved 2026-07-07.
- Raw GitHub SKILL.md, https://raw.githubusercontent.com/nextlevelbuilder/ui-ux-pro-max-skill/main/.claude/skills/ui-ux-pro-max/SKILL.md, retrieved 2026-07-07.
- GitHub repo, https://github.com/nextlevelbuilder/ui-ux-pro-max-skill, retrieved 2026-07-07.
- wilwaldon toolkit, https://github.com/wilwaldon/Claude-Code-Frontend-Design-Toolkit, retrieved 2026-07-07.
- LobeHub directory, https://lobehub.com/skills/terminalskills-skills-ui-ux-pro-max, retrieved 2026-07-07.
- Local tree capture, .raw/skills/ui-ux-pro-max/tree.txt, retrieved 2026-07-07.
- Local claim pack, references/claim-packs/claim-pack-ui-ux-pro-max.md, generated 2026-07-07.
- Local source ledger, references/source-ledger.json, ui-ux-pro-max row retrieved 2026-07-07.

## Related
- [[UI UX Pro Max (Skill)]] is the anchor note for the skill that ships the rule database.
- [[Retrieval Database Skills]] explains why the rules are retrieved instead of prompt-stuffed.
- [[Design System Generation Flow]] shows where the UX rules enter the generation workflow.
- [[Required Audits]] is the cross-skill home for shared rule pressure.
- [[MIFB Surface and Shadow Rules]] overlaps with touch target and hit area guidance.
- [[MIFB Motion and Feedback Rules]] overlaps with the captured animation rule set.
- [[MIFB Motion and Feedback Rules]] gives a micro-interaction comparison point.
- [[Vercel Web Design Guidelines]] gives an audit-layer comparison point.
- [[MIFB Performance Rules]] overlaps with transform and layout stability guidance.
- [[AI Tells (Forbidden Patterns)]] overlaps with anti-pattern checks.

## Next actions
- Refresh the README and SKILL.md before repeating the 99-rule count.
- Add a separate comparison note if Vercel, MIFB, and UI UX Pro Max disagree on a rule value.
- Keep individual UX rule claims tied to the captured SKILL.md until database CSV captures are added.
- Avoid quoting the full rule list in downstream notes.
- Use the source note to document any future CSV capture plan.
- Verify whether `ui-reasoning.csv` remains the reasoning data file name after the next upstream release.
