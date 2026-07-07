---
type: "comparison"
title: "Font Ban Conflicts"
status: "developing"
created: "2026-07-07"
updated: "2026-07-07"
tags: ["gogh/stack", "note/comparison"]
domain: "stack"
confidence: "contested"
related: ["[[Unified Anti-Slop Rulebook]]", "[[Taste Skill Typography Rules]]", "[[Anthropic Frontend Design Rules]]", "[[Impeccable Rule Set (45 Detectors)]]", "[[UI UX Pro Max Repo|UX Rules Database (99 Rules)]]", "[[Prompt Layer vs Toolchain]]", "[[Design Skills Mechanism Map]]", "[[AI Slop]]"]
source_urls: ["https://raw.githubusercontent.com/Leonxlnx/taste-skill/main/skills/taste-skill/SKILL.md (retrieved 2026-07-07)", "https://claude.com/blog/improving-frontend-design-through-skills (retrieved 2026-07-07)", "https://raw.githubusercontent.com/anthropics/skills/main/skills/frontend-design/SKILL.md (retrieved 2026-07-07)", "https://github.com/pbakaus/impeccable (retrieved 2026-07-07)", "https://github.com/nextlevelbuilder/ui-ux-pro-max-skill (retrieved 2026-07-07)"]
sources: ["[[Canonical Skill File]]", "[[Anthropic Frontend Design Skill and Post]]", "[[Impeccable Repo and Site]]", "[[UI UX Pro Max Repo]]", "[[Design Theory Sources]]"]
---
Font Ban Conflicts resolves a real stack disagreement: Taste Skill, Anthropic, Impeccable, and UI UX Pro Max do not apply the same font policy.

## What it is
Taste Skill discourages Inter as the default and gives override cases.
Taste Skill strongly discourages serif as the default for many creative and premium briefs.
Anthropic's launch blog prompt says never use Inter, Roboto, Open Sans, Lato, or default system fonts.
Anthropic's current SKILL.md says the brief's own words win when they pin a visual direction.
Impeccable README says not to use overused fonts such as Arial, Inter, and system defaults.
Impeccable detector ignore examples include an overused-font Inter waiver for a brand font.
UI UX Pro Max records 57 font pairings as of 2026-07-07.
UI UX Pro Max is a retrieval database and not a global font-ban doctrine.
The conflict is therefore between prompt-level avoid lists, toolchain detector targets, and database recommendations.
The claim packs mark several font rows as contested because exceptions and source strength differ.
The safest stack policy is to let brand evidence win, then use the stricter anti-default rule only when the brief is free.
The note exists because flattening these policies would misrepresent the six-skill stack.

## How it works
| Source | Font rule | Exception or caveat | Resolution |
|---|---|---|---|
| Taste Skill Section 4.1 | Avoid Inter as default | Inter is acceptable for neutral, standard, Linear-style, public-sector, or accessibility-first briefs | Brief override wins |
| Taste Skill Section 4.1 | Serif is very discouraged as default | Serif can fit when the brand names it or the domain calls for it | Brand and domain evidence wins |
| Anthropic blog Typography | Never use Inter, Roboto, Open Sans, Lato, or default system fonts | Blog is launch-era prompt evidence | Use as anti-default pressure |
| Anthropic current SKILL.md | Avoid spending free axes on defaults | Brief's own words always win | Current SKILL.md wins over launch prompt |
| Impeccable README | Do not use overused fonts, including Arial, Inter, and system defaults | Detector ignores can waive a brand font | Contract and brand font evidence wins |
| UI UX Pro Max README | 57 font pairings with Google Fonts imports as of 2026-07-07 | Pairings are retrieved recommendations, not global bans | Query for candidates after constraints |
| Theory claim TH02 | Inter is part of the slop signature | Practitioner-level slop framing | Use for rationale, not as a hard brand override |
| Ecosystem claim E012 | Counts decay quickly | Font-pairing count was stable across snapshots, but still date it | Date every count |

> [!contradiction]
> Anthropic's launch prompt says never use several fonts, while Taste Skill and Impeccable both preserve brand or brief exceptions for otherwise overused fonts.

## Best practice
- Use the project's committed brand font before any generic anti-default ban EVIDENCE-BASED
- If no brand font exists, avoid Inter as the first default EVIDENCE-BASED
- Treat Roboto, Open Sans, Lato, Arial, and system defaults as Anthropic or Impeccable anti-default signals CONTESTED
- Use UI UX Pro Max to retrieve pairings after the brand and ban constraints are known EVIDENCE-BASED
- Prefer Taste Skill's current override language to a total Inter ban in public-sector or accessibility-first briefs EVIDENCE-BASED
- Treat Anthropic's blog prompt as launch-era guidance rather than the only current Anthropic policy EVIDENCE-BASED
- Use Impeccable ignores only with a reason such as an existing brand font EVIDENCE-BASED
- Date UI UX Pro Max font-pairing counts as 57 pairings as of 2026-07-07 EVIDENCE-BASED
- Record the conflict in stack advice when a brand requires a banned font PRACTITIONER
- Avoid inventing a universal font hierarchy beyond the captured sources EVIDENCE-BASED

## Pitfalls
Declaring Inter always forbidden would conflict with Taste Skill's override language.
Declaring serif always premium would conflict with Taste Skill's serif-default warning.
Using Anthropic's launch prompt without the current SKILL.md can overstate a hard ban.
Using UI UX Pro Max pairings as if they were audited brand rules can overstate the database.
Using Impeccable's detector target without a documented ignore path can break a legitimate brand.
Using a font because it is unusual can still violate the brief.
Using too many font families can conflict with hierarchy and performance goals.
Using Google Fonts imports can conflict with Taste Skill's production font-loading guidance.
Treating font taste as independent of product domain can re-create slop in a new costume.
Treating stale counts as current would violate the metrics rule.

## Sources
- Taste Skill SKILL.md, https://raw.githubusercontent.com/Leonxlnx/taste-skill/main/skills/taste-skill/SKILL.md, retrieved 2026-07-07.
- Anthropic blog, https://claude.com/blog/improving-frontend-design-through-skills, retrieved 2026-07-07.
- Anthropic frontend-design SKILL.md, https://raw.githubusercontent.com/anthropics/skills/main/skills/frontend-design/SKILL.md, retrieved 2026-07-07.
- Impeccable README, https://github.com/pbakaus/impeccable, retrieved 2026-07-07.
- UI UX Pro Max README, https://github.com/nextlevelbuilder/ui-ux-pro-max-skill, retrieved 2026-07-07.
- Claim pack Anthropic frontend-design, references/claim-packs/claim-pack-anthropic-frontend-design.md, generated 2026-07-07.
- Claim pack UI UX Pro Max, references/claim-packs/claim-pack-ui-ux-pro-max.md, generated 2026-07-07.
- Claim pack theory, references/claim-packs/claim-pack-theory.md, generated 2026-07-07.

## Related
- [[Unified Anti-Slop Rulebook]] lists the merged font-ban rows.
- [[Taste Skill Typography Rules]] is the existing Taste Skill typography note.
- [[Anthropic Frontend Design Rules]] carries the current Anthropic guidance.
- [[Impeccable Rule Set (45 Detectors)]] explains detector targets and ignores.
- [[UI UX Pro Max Repo|UX Rules Database (99 Rules)]] supplies retrieval context for pairings.
- [[Prompt Layer vs Toolchain]] explains when a prompt ban needs persistent enforcement.
- [[Design Skills Mechanism Map]] places font policy in the taste and retrieval layers.
- [[AI Slop]] explains why neutral font defaults became a recognizable tell.
- [[Distributional Convergence]] explains the training-data convergence backdrop.
- [[Constraint Beats Coaxing]] explains why avoid lists can outperform vague taste prompts.

## Next actions
- Add project-specific font decisions to stack reports when a brand font conflicts with a ban.
- Re-check UI UX Pro Max README before repeating the 57 pairings count.
- Re-check Impeccable detector docs before naming detector rule IDs.
- Keep Anthropic blog and current SKILL.md roles separate.
- Use this comparison before updating the unified rulebook font rows.
