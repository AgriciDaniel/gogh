---
type: "deliverable"
title: "Design Skills Cheat Sheet"
status: "developing"
created: "2026-07-07"
updated: "2026-07-07"
tags: ["gogh/stack", "note/deliverable"]
domain: "stack"
confidence: "evidence-based"
related: ["[[Design Skills Mechanism Map]]", "[[Skill Stack Selection Flow]]", "[[Unified Anti-Slop Rulebook]]", "[[Install Surface and Format Portability]]", "[[Taste Skill (Project)]]", "[[Anthropic Frontend Design Skill]]", "[[Make Interfaces Feel Better (Skill)]]", "[[Impeccable (Toolchain)]]"]
source_urls: ["https://raw.githubusercontent.com/Leonxlnx/taste-skill/main/skills/taste-skill/SKILL.md (retrieved 2026-07-07)", "https://raw.githubusercontent.com/anthropics/skills/main/skills/frontend-design/SKILL.md (retrieved 2026-07-07)", "https://github.com/jakubkrehel/make-interfaces-feel-better (retrieved 2026-07-07)", "https://github.com/pbakaus/impeccable (retrieved 2026-07-07)", "https://github.com/nextlevelbuilder/ui-ux-pro-max-skill (retrieved 2026-07-07)", "https://raw.githubusercontent.com/vercel-labs/agent-skills/main/skills/web-design-guidelines/SKILL.md (retrieved 2026-07-07)"]
sources: ["[[Canonical Skill File]]", "[[Anthropic Frontend Design Skill and Post]]", "[[MIFB Repo and Skill File]]", "[[Impeccable Repo and Site]]", "[[UI UX Pro Max Repo]]", "[[Reception Sources]]"]
---
Design Skills Cheat Sheet puts the six Gogh skills on one page with mechanism, install command, when to use, and three source-backed rules each.

## What it is
This deliverable summarizes the six-skill Gogh stack.
The mechanisms follow claim-pack-ecosystem E001.
The install commands follow each per-skill claim pack or README capture.
The rules are selected from captured source files retrieved on 2026-07-07.
The counts in this deliverable are dated observations.
The sheet is a working aid, not a replacement for the source notes.
The sheet uses source labels in each row.
The sheet keeps UI UX Pro Max as retrieval and Vercel as audit.
The sheet keeps Impeccable as toolchain enforcement.
The sheet keeps MIFB as micro-interaction execution.
The sheet keeps Taste Skill and Anthropic as taste prompting layers.
The sheet should be refreshed after any upstream release.

## How it works
| Skill | Mechanism | Install | Reach for it when | Source |
|---|---|---|---|---|
| [[Taste Skill (Project)]] | Taste prompting with dials and pre-flight | `npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend"` | Landing pages, portfolios, and redesigns need strong anti-slop direction | T004, T014 |
| [[Anthropic Frontend Design Skill]] | Taste prompting baseline | `npx skills add https://github.com/anthropics/skills --skill frontend-design` | A compact subject-grounded aesthetic baseline is enough | A008, A011 |
| [[Make Interfaces Feel Better (Skill)]] | Micro-interaction execution | `npx skills add jakubkrehel/make-interfaces-feel-better` | Components need tactile polish, surface precision, and motion details | M005, M016 |
| [[Impeccable (Toolchain)]] | Toolchain enforcement | `npx impeccable install`, then `/impeccable init` | Teams need contracts, commands, hooks, and detector gates | I006, I009, I011 |
| [[UI UX Pro Max Repo|UI UX Pro Max (Skill)]] | Retrieval database | `npm install -g ui-ux-pro-max-cli`, then `uipro init --ai [platform]` | Brand maturity is low and style, palette, typography, or UX retrieval is useful | U008, U010 |
| [[Reception Sources|Vercel Web Design Guidelines]] | Runtime audit | `npx skills add vercel-labs/agent-skills --skill web-design-guidelines` | Existing UI code needs file:line accessibility and UX findings | V003, V004, V005 |

| Skill | Top three rules or checks | Source |
|---|---|---|
| Taste Skill | Set DESIGN_VARIANCE, MOTION_INTENSITY, and VISUAL_DENSITY on 1-10 scales | T007 |
| Taste Skill | Hero headline max 2 lines, subtext max 20 words, CTA visible without scroll | T011 |
| Taste Skill | Any failed Section 14 pre-flight box blocks completion | T009 |
| Anthropic frontend-design | Ground the visual direction in the subject's world | A008 |
| Anthropic frontend-design | Avoid free-axis defaults such as warm cream, near-black acid accent, and broadsheet defaults | A009 |
| Anthropic frontend-design | Build, critique, and remove decoration that does not serve the brief | A010 |
| MIFB | Outer radius equals inner radius plus padding for close nested surfaces | M009 |
| MIFB | Button press feedback uses scale 0.96 and never below 0.95 | M010 |
| MIFB | Interactive elements need at least 40x40px hit areas, with extension for small visible controls | M011 |
| Impeccable | `/impeccable init` writes PRODUCT.md and offers DESIGN.md | I009 |
| Impeccable | Detect runs 45 deterministic rules without an LLM or API keys as of 2026-07-07 | I011 |
| Impeccable | Avoid Inter for everything, purple-to-blue gradients, and nested cards | I013 |
| UI UX Pro Max | Query BM25 searchable CSV databases across design domains | U008 |
| UI UX Pro Max | Use 67 styles, 161 palettes, 57 font pairings, and 99 UX guidelines as dated 2026-07-07 counts | U005 |
| UI UX Pro Max | Use SVG or vector icons rather than emoji as structural icons | UI UX Pro Max SKILL Pre-Delivery Checklist |
| Vercel web-design-guidelines | Fetch current command.md rules at audit time | V004 |
| Vercel web-design-guidelines | Output terse file:line findings grouped by file | V005 |
| Vercel web-design-guidelines | Check focus, forms, reduced motion, image dimensions, state URLs, and semantics | V008 |

## Best practice
- Start with the mechanism column before the install column EVIDENCE-BASED
- Use Taste Skill or Anthropic before MIFB when the direction is missing EVIDENCE-BASED
- Use UI UX Pro Max before implementation when low brand maturity needs retrieval EVIDENCE-BASED
- Use Impeccable when repeated work needs contracts and deterministic detection EVIDENCE-BASED
- Use Vercel when the desired output is audit findings on existing files EVIDENCE-BASED
- Keep all metric counts dated to 2026-07-07 EVIDENCE-BASED
- Treat skills.sh install counts as registry-reported if added later EVIDENCE-BASED
- Keep MIFB license nuance in source notes when distributing beyond this sheet EVIDENCE-BASED
- Use comparison notes when rules conflict CONTESTED
- Refresh this sheet after source-ledger updates EVIDENCE-BASED

## Pitfalls
Using this cheat sheet as the only source would drop claim-pack caveats.
Treating UI UX Pro Max as a generator without retrieval limits would misread its mechanism.
Treating Vercel as a generation skill would misread its audit scope.
Treating MIFB as a full design-direction framework would misread its craft role.
Treating Anthropic's launch prompt as the whole current skill would ignore the current SKILL.md.
Treating Impeccable's detector count as timeless would ignore release velocity.
Treating Taste Skill Section 14 item count as 60 without caveat would repeat a contested third-party count.
Treating local install commands as stable forever would ignore upstream churn.
Treating all rule rows as equal confidence would hide contested font policy.
Treating stars or installs as undated would violate the ecosystem metric rule.

## Sources
- Taste Skill SKILL.md, https://raw.githubusercontent.com/Leonxlnx/taste-skill/main/skills/taste-skill/SKILL.md, retrieved 2026-07-07.
- Anthropic frontend-design SKILL.md, https://raw.githubusercontent.com/anthropics/skills/main/skills/frontend-design/SKILL.md, retrieved 2026-07-07.
- MIFB README and SKILL.md, https://github.com/jakubkrehel/make-interfaces-feel-better, retrieved 2026-07-07.
- Impeccable README and releases, https://github.com/pbakaus/impeccable, retrieved 2026-07-07.
- UI UX Pro Max README and SKILL.md, https://github.com/nextlevelbuilder/ui-ux-pro-max-skill, retrieved 2026-07-07.
- Vercel web-design-guidelines SKILL.md, https://raw.githubusercontent.com/vercel-labs/agent-skills/main/skills/web-design-guidelines/SKILL.md, retrieved 2026-07-07.
- Claim packs, references/claim-packs, generated 2026-07-07.

## Related
- [[Design Skills Mechanism Map]] explains the mechanism categories.
- [[Skill Stack Selection Flow]] turns the sheet into a decision tree.
- [[Unified Anti-Slop Rulebook]] merges the bans.
- [[Install Surface and Format Portability]] explains install caveats.
- [[Taste Skill (Project)]] is the Taste Skill anchor.
- [[Anthropic Frontend Design Skill]] is the Anthropic anchor.
- [[Make Interfaces Feel Better (Skill)]] is the MIFB anchor.
- [[Impeccable (Toolchain)]] is the Impeccable anchor.
- [[UI UX Pro Max Repo|UI UX Pro Max (Skill)]] is the retrieval source anchor.
- [[Reception Sources|Vercel Web Design Guidelines]] is the audit source context.

## Next actions
- Recheck all commands before release packaging.
- Keep the sheet synchronized with source-ledger refreshes.
- Add missing dedicated Vercel anchor links only after that note exists.
- Use this deliverable as the quick reference before running stack advice.
- Do not treat this deliverable as market-ready without audit.

