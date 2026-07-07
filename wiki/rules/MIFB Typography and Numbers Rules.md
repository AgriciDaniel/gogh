---
type: "rule"
title: "MIFB Typography and Numbers Rules"
status: "developing"
created: "2026-07-07"
updated: "2026-07-07"
tags: ["gogh/mifb", "note/rule"]
domain: "mifb"
confidence: "evidence-based"
related: ["[[Make Interfaces Feel Better (Skill)]]", "[[MIFB Surface and Shadow Rules]]", "[[MIFB Motion and Feedback Rules]]", "[[MIFB Performance Rules]]", "[[MIFB Review Checklist]]", "[[Optical Alignment]]", "[[Jakub Krehel]]", "[[MIFB Repo and Skill File]]"]
source_urls: ["https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/skills/make-interfaces-feel-better/typography.md (retrieved 2026-07-07)", "https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/skills/make-interfaces-feel-better/SKILL.md (retrieved 2026-07-07)", "https://jakub.kr/writing/details-that-make-interfaces-feel-better (retrieved 2026-07-07)"]
sources: ["[[MIFB Repo and Skill File]]"]
---
MIFB Typography and Numbers Rules capture the skill's text wrapping, root font smoothing, and tabular numeral guidance.

## What it is

- This rule note covers the typography reference file in the MIFB skill.
- The captured typography reference says its topic is typography rendering details.
- The rule set has three main parts: text wrapping, font smoothing, and tabular numbers.
- The captured SKILL.md maps typography to text wrapping, font smoothing, and tabular numbers.
- The Krehel article extract lists text wrapping as technique 1.
- The Krehel article extract lists text crispness as technique 4.
- The Krehel article extract lists tabular numbers as technique 5.
- `text-wrap: balance` is used for headings and short title blocks.
- `text-wrap: pretty` is used for short-to-medium paragraphs, descriptions, captions, list items, and card text.
- The typography reference says long text of 10 or more lines should use default wrapping.
- The typography reference says code blocks and pre-formatted text should not use balance or pretty.
- The typography reference says Chromium limits balance to blocks of 6 lines or fewer.
- The typography reference says Firefox limits balance to blocks of 10 lines or fewer.
- Root font smoothing uses `-webkit-font-smoothing: antialiased` and `-moz-osx-font-smoothing: grayscale`.
- The typography reference says font smoothing affects macOS rendering and other platforms ignore the properties.
- Tabular numbers use `font-variant-numeric: tabular-nums`.
- The typography reference says tabular numbers prevent layout shift as dynamic values change.
- The typography reference says Inter can visibly alter the digit `1` when tabular numbers are enabled.

## How it works

- `text-wrap: balance` distributes short blocks more evenly across lines.
- `text-wrap: balance` is intended for headings, titles, and short text where even distribution matters.
- `text-wrap: pretty` adjusts paragraph breaks to avoid a single short last-line word.
- `text-wrap: pretty` does not try to equalize line lengths.
- Tailwind maps balance to `text-balance`.
- Tailwind maps pretty to `text-pretty`.
- Font smoothing belongs on the root layout, not scattered across individual elements.
- Tailwind maps the root smoothing pattern to the `antialiased` class.
- Tabular numbers make all digits equal width.
- Tabular numbers are appropriate for counters, timers, updating prices, numeric table columns, animated number transitions, scoreboards, and dashboards.
- The typography reference says static display numbers do not need tabular numbers.
- The typography reference says decorative large numbers do not need tabular numbers.
- The typography reference says phone numbers, zip codes, and version numbers are not the intended tabular-nums targets.
- The MIFB checklist includes dynamic numbers, font smoothing, and heading balance as review items.
- The MIFB common mistakes table maps number layout shift to applying `tabular-nums`.
- The MIFB common mistakes table maps heavy macOS text to applying `antialiased` at the root.

## Best practice

- Use `text-wrap: balance` on headings and titles where even line distribution matters. EVIDENCE-BASED
- Avoid `text-wrap: balance` on long paragraphs because the reference says browsers limit or ignore it. EVIDENCE-BASED
- Use `text-wrap: pretty` for short-to-medium prose, captions, descriptions, list items, and card text. EVIDENCE-BASED
- Leave 10 or more line prose, code blocks, and pre-formatted text on default wrapping. EVIDENCE-BASED
- Apply font smoothing once at the root layout instead of per element. EVIDENCE-BASED
- Use Tailwind `antialiased` at the root when Tailwind is the project convention. EVIDENCE-BASED
- Apply `tabular-nums` to counters, timers, prices, numeric columns, animated numbers, scoreboards, and dashboards. EVIDENCE-BASED
- Skip `tabular-nums` for static display numbers, decorative numbers, phone numbers, zip codes, and version strings. EVIDENCE-BASED
- Verify the chosen font after enabling tabular numbers because Inter changes numeral appearance. EVIDENCE-BASED
- Review headings, dynamic numerals, and root smoothing together during a MIFB typography pass. EVIDENCE-BASED

## Pitfalls

- Applying `text-wrap: balance` to long body copy can silently waste intent because engines limit balancing.
- Using default wrapping on short headings can leave visually weak orphan words.
- Applying smoothing to only some elements can make text weight inconsistent in the same interface.
- Treating font smoothing as cross-platform visual control overstates what the reference claims.
- Forgetting `tabular-nums` on an animated counter can cause layout shift.
- Applying tabular numbers to decorative numerals can make typography look less intentional.
- Assuming the digit shape will stay identical can miss the Inter caveat in the reference file.
- Treating these rules as a full typography system overstates MIFB's scope.

## Sources

- Raw GitHub typography reference, https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/skills/make-interfaces-feel-better/typography.md, retrieved 2026-07-07.
- Raw GitHub SKILL.md, https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/skills/make-interfaces-feel-better/SKILL.md, retrieved 2026-07-07.
- Jakub Krehel, https://jakub.kr/writing/details-that-make-interfaces-feel-better, retrieved 2026-07-07.
- Local MIFB skill extract, .raw/research/mifb-skill-extract.md, captured 2026-07-07.
- Local Krehel article extract, .raw/research/krehel-article-extract.md, captured 2026-07-07.
- Local source ledger, references/source-ledger.json, generated 2026-07-06 and containing MIFB entries retrieved 2026-07-07.

## Related

- [[Make Interfaces Feel Better (Skill)]]: anchors this rule inside the MIFB skill.
- [[MIFB Surface and Shadow Rules]]: covers the surface rules that often sit around text blocks.
- [[MIFB Motion and Feedback Rules]]: covers motion rules for counters and interactive labels.
- [[MIFB Performance Rules]]: covers transition and hit-area review that can touch text controls.
- [[MIFB Review Checklist]]: includes dynamic numbers, font smoothing, and heading balance.
- [[Optical Alignment]]: complements typography because text and icons often need optical correction.
- [[Jakub Krehel]]: identifies the author of the article and skill.
- [[MIFB Repo and Skill File]]: stores the captured typography source and retrieval date.
- [[Encoded Design Principles]]: connects rule encoding to reusable agent guidance.
- [[Design Review as Infrastructure]]: frames this rule as reviewable craft rather than taste vibes.

## Next actions

- Re-check typography.md before updating line-count limits.
- Re-check SKILL.md before changing checklist mappings.
- Add examples only when they are traceable to the captured typography reference.
- Keep `text-wrap: balance` limited to short heading contexts.
- Keep `text-wrap: pretty` limited to short-to-medium prose contexts.
- Keep root smoothing described as macOS-focused.
- Keep tabular numbers scoped to dynamic numeric UI.
- Re-run the MIFB checklist after applying typography fixes.
