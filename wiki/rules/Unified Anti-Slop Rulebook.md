---
type: "rule"
title: "Unified Anti-Slop Rulebook"
status: "developing"
created: "2026-07-07"
updated: "2026-07-07"
tags: ["gogh/stack", "note/rule"]
domain: "stack"
confidence: "contested"
related: ["[[Design Skills Mechanism Map]]", "[[AI Tells (Forbidden Patterns)]]", "[[Em-Dash Ban]]", "[[Hero Discipline]]", "[[Font Ban Conflicts]]", "[[Motion Doctrine Conflicts]]", "[[Enforcement Layer Overlap]]", "[[Prompt Layer vs Toolchain]]"]
source_urls: ["https://raw.githubusercontent.com/Leonxlnx/taste-skill/main/skills/taste-skill/SKILL.md (retrieved 2026-07-07)", "https://raw.githubusercontent.com/anthropics/skills/main/skills/frontend-design/SKILL.md (retrieved 2026-07-07)", "https://claude.com/blog/improving-frontend-design-through-skills (retrieved 2026-07-07)", "https://github.com/pbakaus/impeccable (retrieved 2026-07-07)", "https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/skills/make-interfaces-feel-better/SKILL.md (retrieved 2026-07-07)", "https://raw.githubusercontent.com/nextlevelbuilder/ui-ux-pro-max-skill/main/.claude/skills/ui-ux-pro-max/SKILL.md (retrieved 2026-07-07)", "https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md (retrieved 2026-07-07)"]
sources: ["[[Canonical Skill File]]", "[[Anthropic Frontend Design Skill and Post]]", "[[Impeccable Repo and Site]]", "[[MIFB Repo and Skill File]]", "[[UI UX Pro Max Repo]]", "[[Reception Sources]]"]
---
Unified Anti-Slop Rulebook is a merged ban table, not a harmonized doctrine, because several skills intentionally disagree on which defaults are always wrong.

## What it is
This rulebook merges bans and avoid-lists from the six covered skills.
The merge uses primary captures and claim packs generated on 2026-07-07.
The table keeps source sections visible for each row.
Rows use the confidence tags from the relevant claim packs.
Taste Skill contributes the strongest explicit bans through Sections 3, 4, 5, 8, 9, 11, and 14.
Anthropic contributes avoid-default guidance through the current SKILL.md and the launch blog.
Impeccable contributes absolute bans and detector anti-patterns through README, SKILL.md, and repo extract.
MIFB contributes interaction and craft bans such as avoiding non-interruptible controls and `transition: all`.
UI UX Pro Max contributes database and checklist bans such as no emoji structural icons.
Vercel contributes audit-rule bans such as no `transition: all`, no missing focus replacement, and no blocked paste.
The rulebook is contested where a ban in one skill is an allowed style under a brief-led exception in another skill.
The comparison notes are the authority for resolving disagreements in practice.

## How it works
| Ban or constraint | Skills that state it | Exact source section | Confidence |
|---|---|---|---|
| Visible U+2014 and U+2013 characters are banned | Taste Skill | Taste Skill Section 9.G and Section 14 | EVIDENCE-BASED |
| Inter as default is banned or discouraged | Taste Skill, Anthropic blog, Impeccable | Taste Skill Section 4.1 and 9.B, Anthropic blog Typography, Impeccable README Anti-Patterns | CONTESTED |
| Roboto, Open Sans, Lato, Arial, and default system fonts are overused defaults | Anthropic blog, Impeccable | Anthropic blog Typography and general prompt, Impeccable README Anti-Patterns | CONTESTED |
| Serif as default for creative or premium briefs is discouraged | Taste Skill | Taste Skill Section 4.1 | EVIDENCE-BASED |
| Purple or blue glow gradients as automatic defaults are discouraged | Taste Skill, Anthropic blog, Impeccable | Taste Skill Section 0.D and 4.2, Anthropic blog general prompt, Impeccable README Why Impeccable | EVIDENCE-BASED |
| AI purple or pink gradients can be anti-patterns by domain | UI UX Pro Max | UI UX Pro Max README example and SKILL priority table | EVIDENCE-BASED |
| Nested cards are wrong | Impeccable | Impeccable SKILL.md Layout and README Why Impeccable | EVIDENCE-BASED |
| Generic card containers can be banned at high visual density | Taste Skill | Taste Skill Section 4.4 and 7 | EVIDENCE-BASED |
| Gray text on colored backgrounds is a detector target | Impeccable | Impeccable README Why Impeccable and repo extract Detector | EVIDENCE-BASED |
| Div-based fake screenshots and fake product UI are banned | Taste Skill | Taste Skill Section 4.8, Section 9.E, Section 9.F, Section 14 | EVIDENCE-BASED |
| Decorative emoji are discouraged or banned as structural icons | Taste Skill, UI UX Pro Max | Taste Skill Section 3.D, UI UX Pro Max SKILL Style Selection and Pre-Delivery Checklist | EVIDENCE-BASED |
| Hero must fit the viewport and CTA must be visible without scroll | Taste Skill | Taste Skill Section 4.7 and Section 14 | EVIDENCE-BASED |
| Hero metric template is an absolute ban | Impeccable | Impeccable SKILL.md Absolute bans | EVIDENCE-BASED |
| Warm cream near #F4F1EA is a known AI default | Anthropic | Anthropic frontend-design SKILL.md Process section | EVIDENCE-BASED |
| Premium beige plus brass palette is banned as a default | Taste Skill | Taste Skill Section 4.2 and Section 14 | EVIDENCE-BASED |
| No focus outline removal without replacement | Vercel | Vercel command.md Focus States | EVIDENCE-BASED |
| Never block paste in forms | Vercel | Vercel command.md Forms | EVIDENCE-BASED |
| `transition: all` is banned | MIFB, Vercel | MIFB SKILL.md and performance reference, Vercel command.md Animation and Anti-patterns | EVIDENCE-BASED |
| Press scale below 0.95 is banned | MIFB | MIFB animations reference Press Feedback | EVIDENCE-BASED |
| Missing prefers-reduced-motion handling is a failure for motion-heavy work | Taste Skill, Vercel, UI UX Pro Max | Taste Skill Section 6.B and Section 14, Vercel command.md Animation, UI UX Pro Max checklist | EVIDENCE-BASED |

> [!contradiction]
> Some rows are not universal bans. Anthropic's current skill says the brief's own words win, Taste Skill allows purple when the brand asks for purple, and Impeccable supports ignores for brand fonts.

## Best practice
- Use this table as a pre-flight merge, not as a new upstream source EVIDENCE-BASED
- Follow Taste Skill's explicit visible character ban when writing public copy EVIDENCE-BASED
- Route font disagreements to [[Font Ban Conflicts]] CONTESTED
- Route motion value disagreements to [[Motion Doctrine Conflicts]] CONTESTED
- Route detector and audit overlap to [[Enforcement Layer Overlap]] EVIDENCE-BASED
- Keep brief-led exceptions visible when a skill allows them EVIDENCE-BASED
- Prefer primary captures over directory summaries for rule content EVIDENCE-BASED
- Date all counts and detector totals in any companion text EVIDENCE-BASED
- Treat UI UX Pro Max row-level database claims as unavailable unless the CSV body is captured EVIDENCE-BASED
- Use Vercel rows as audit checks, not generation style rules EVIDENCE-BASED

## Pitfalls
Do not claim all six skills ban the same fonts.
Do not treat Anthropic's launch blog prompt as identical to the current SKILL.md.
Do not flatten Taste Skill's purple override into a total purple ban.
Do not treat UI UX Pro Max style examples as universal bans.
Do not make Vercel web-design-guidelines a taste-direction skill.
Do not treat MIFB craft thresholds as whole-page aesthetic doctrine.
Do not cite Impeccable detector families without dating the 45-rule count.
Do not use stale third-party detector counts from May 2026.
Do not use Snyk's older UI UX Pro Max counts as current.
Do not erase contested rows just to make a clean checklist.

## Sources
- Taste Skill SKILL.md, https://raw.githubusercontent.com/Leonxlnx/taste-skill/main/skills/taste-skill/SKILL.md, retrieved 2026-07-07.
- Anthropic frontend-design SKILL.md, https://raw.githubusercontent.com/anthropics/skills/main/skills/frontend-design/SKILL.md, retrieved 2026-07-07.
- Anthropic blog, https://claude.com/blog/improving-frontend-design-through-skills, retrieved 2026-07-07.
- Impeccable README and SKILL.md, https://github.com/pbakaus/impeccable, retrieved 2026-07-07.
- MIFB SKILL.md and references, https://github.com/jakubkrehel/make-interfaces-feel-better, retrieved 2026-07-07.
- UI UX Pro Max README and SKILL.md, https://github.com/nextlevelbuilder/ui-ux-pro-max-skill, retrieved 2026-07-07.
- Vercel command.md, https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md, retrieved 2026-07-07.
- Claim packs, references/claim-packs, generated 2026-07-07.

## Related
- [[Design Skills Mechanism Map]] explains why bans come from different mechanisms.
- [[AI Tells (Forbidden Patterns)]] is the existing Taste Skill anti-slop rule note.
- [[Em-Dash Ban]] is the existing Taste Skill character rule note.
- [[Hero Discipline]] covers the strict Taste Skill hero rows.
- [[Font Ban Conflicts]] resolves font disagreement across skills.
- [[Motion Doctrine Conflicts]] resolves dial versus fixed-value motion guidance.
- [[Enforcement Layer Overlap]] maps checks to pipeline stages.
- [[Prompt Layer vs Toolchain]] explains when a prompt ban needs persistent enforcement.
- [[Impeccable Rule Set (45 Detectors)]] provides detector-specific context.
- [[MIFB Motion and Feedback Rules]] provides MIFB values behind interaction rows.

## Next actions
- Update this table after any source-ledger refresh that changes a rule or detector count.
- Add rows only when a primary capture or claim pack supports them.
- Keep contested rows linked to comparison notes.
- Re-check Vercel command.md because it is fetched at runtime by the skill.
- Re-check Impeccable releases before repeating detector totals.

