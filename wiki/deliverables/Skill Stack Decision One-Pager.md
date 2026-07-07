---
type: "deliverable"
title: "Skill Stack Decision One-Pager"
status: "developing"
created: "2026-07-07"
updated: "2026-07-07"
tags: ["gogh/stack", "note/deliverable"]
domain: "stack"
confidence: "evidence-based"
related: ["[[Skill Stack Selection Flow]]", "[[Design Skills Mechanism Map]]", "[[The Three Dials]]", "[[Full Stack Build Flow]]", "[[Audit Pipeline Flow]]", "[[Design Skills Cheat Sheet]]", "[[Gogh Quickstart]]", "[[Install Surface and Format Portability]]"]
source_urls: ["https://raw.githubusercontent.com/Leonxlnx/taste-skill/main/skills/taste-skill/SKILL.md (retrieved 2026-07-07)", "https://github.com/nextlevelbuilder/ui-ux-pro-max-skill (retrieved 2026-07-07)", "https://github.com/pbakaus/impeccable (retrieved 2026-07-07)", "https://raw.githubusercontent.com/vercel-labs/agent-skills/main/skills/web-design-guidelines/SKILL.md (retrieved 2026-07-07)"]
sources: ["[[Canonical Skill File]]", "[[UI UX Pro Max Repo]]", "[[Impeccable Repo and Site]]", "[[Reception Sources]]"]
---
Skill Stack Decision One-Pager is the printable selection guide backed by the local stack advisor and Skill Stack Selection Flow.

## What it is
This one-pager compresses the stack advisor into a human-readable decision sheet.
The decision fields are project_type, brand_maturity, motion, density, and accessibility.
The field values come from `scripts/render_stack_advisor.py`.
The skill order follows the same script.
The dial defaults come from the same script and Taste Skill's dial model.
The one-pager is a guide for selecting the stack before implementation.
The one-pager is not a substitute for source-specific conflict notes.
The one-pager should end with `gogh-brain advise`.
The one-pager keeps all recommendations advisory under Gogh V1.
The one-pager is printable because it uses short rows and source labels.
The one-pager should be refreshed if advisor rules change.
The one-pager should be used with the cheat sheet for install commands.

## How it works
| Question | If yes | Add or adjust | Source |
|---|---|---|---|
| Is project_type landing, portfolio, redesign, or editorial | Yes | Add Taste Skill and Anthropic frontend-design | stack advisor |
| Is project_type dashboard or app | Yes | Start restrained and rely on Impeccable, Vercel, and UI-specific retrieval | stack advisor |
| Is brand_maturity none | Yes | Add UI UX Pro Max and raise DESIGN_VARIANCE by 1 | stack advisor |
| Is brand_maturity partial | Yes | Add UI UX Pro Max and lower DESIGN_VARIANCE by 1 | stack advisor |
| Is brand_maturity mature | Yes | Preserve brand and lower DESIGN_VARIANCE by 2 | stack advisor |
| Is motion restrained | Yes | Add MIFB and set MOTION_INTENSITY 4 | stack advisor |
| Is motion rich | Yes | Add MIFB and set MOTION_INTENSITY 8 | stack advisor |
| Is motion cinematic | Yes | Add MIFB and set MOTION_INTENSITY 9 | stack advisor |
| Is motion static | Yes | Set MOTION_INTENSITY 1 | stack advisor |
| Is density airy | Yes | Set VISUAL_DENSITY 3 | stack advisor |
| Is density balanced | Yes | Set VISUAL_DENSITY 4 | stack advisor |
| Is density dense | Yes | Set VISUAL_DENSITY 7 | stack advisor |
| Is accessibility strict | Yes | Cap DESIGN_VARIANCE at 6 and add Vercel | stack advisor |
| Is project_type landing, redesign, app, or dashboard | Yes | Add Vercel web-design-guidelines | stack advisor |
| Is any valid brief provided | Yes | Add Impeccable in current local advisor | stack advisor |

Run line: `gogh-brain advise --vault <path> --brief <file>`.

## Best practice
- Fill every advisor field before selecting the stack EVIDENCE-BASED
- Use project_type as the first branch EVIDENCE-BASED
- Use brand_maturity to decide retrieval and variance EVIDENCE-BASED
- Use motion to decide MIFB and MOTION_INTENSITY EVIDENCE-BASED
- Use density to decide VISUAL_DENSITY EVIDENCE-BASED
- Use strict accessibility to cap DESIGN_VARIANCE and add Vercel EVIDENCE-BASED
- Keep Impeccable in the recommendation while still choosing enforcement depth PRACTITIONER
- Run `gogh-brain advise` after the one-pager decision EVIDENCE-BASED
- Link conflict notes when a selected skill disagrees with another PRACTITIONER
- Re-check advisor code before changing this one-pager EVIDENCE-BASED

## Pitfalls
Skipping project_type can choose Taste Skill outside the local advisor branch.
Skipping brand_maturity can over-retrieve or under-retrieve UI UX Pro Max guidance.
Skipping motion can omit MIFB from a motion-heavy build.
Skipping density can set the wrong VISUAL_DENSITY.
Skipping accessibility can overrun strict variance.
Treating the one-pager as an audit report can confuse selection with verification.
Treating the one-pager as a mutation command would exceed Gogh V1 boundaries.
Treating Impeccable inclusion as mandatory hook activation can overstate the advisor.
Treating Vercel as aesthetic direction can misuse the audit layer.
Treating the one-pager as stable after code changes can stale the deliverable.

## Sources
- Local stack advisor, scripts/render_stack_advisor.py, read 2026-07-07.
- Skill registry, references/skill-registry.json, generated 2026-07-07.
- Taste Skill SKILL.md, https://raw.githubusercontent.com/Leonxlnx/taste-skill/main/skills/taste-skill/SKILL.md, retrieved 2026-07-07.
- UI UX Pro Max README, https://github.com/nextlevelbuilder/ui-ux-pro-max-skill, retrieved 2026-07-07.
- Impeccable README, https://github.com/pbakaus/impeccable, retrieved 2026-07-07.
- Vercel SKILL.md, https://raw.githubusercontent.com/vercel-labs/agent-skills/main/skills/web-design-guidelines/SKILL.md, retrieved 2026-07-07.
- Claim pack ecosystem, references/claim-packs/claim-pack-ecosystem.md, generated 2026-07-07.

## Related
- [[Skill Stack Selection Flow]] is the full flow backing this one-pager.
- [[Design Skills Mechanism Map]] explains the mechanism categories.
- [[The Three Dials]] explains the Taste Skill dial model.
- [[Full Stack Build Flow]] applies the selected stack to greenfield builds.
- [[Audit Pipeline Flow]] applies the selected stack to verification.
- [[Design Skills Cheat Sheet]] gives install commands and top rules.
- [[Gogh Quickstart]] uses this one-pager in the first-project walkthrough.
- [[Install Surface and Format Portability]] explains channel-specific install caveats.
- [[Prompt Layer vs Toolchain]] helps decide enforcement depth after selection.
- [[wiki/gaps/_index|Stack Order Probe]] records that ordering still lacks benchmark evidence.

## Next actions
- Keep this one-pager synced with `scripts/render_stack_advisor.py`.
- Re-run stack advisor tests after any rule change.
- Use this one-pager before installing unnecessary skills.
- Pair it with the cheat sheet for source-backed commands.
- Keep the final command visible for operators.
