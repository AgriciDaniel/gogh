---
type: "concept"
title: "Press Feedback and Hit Areas"
status: "developing"
created: "2026-07-07"
updated: "2026-07-07"
tags: ["gogh/mifb", "note/concept"]
domain: "mifb"
confidence: "evidence-based"
related: ["[[Make Interfaces Feel Better (Skill)]]", "[[MIFB Motion and Feedback Rules]]", "[[MIFB Surface and Shadow Rules]]", "[[Interruptible Animation]]", "[[Concentric Radii]]", "[[MIFB Review Checklist]]", "[[MIFB Repo and Skill File]]", "[[Reception Sources|Vercel Web Design Guidelines]]"]
source_urls: ["https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/skills/make-interfaces-feel-better/SKILL.md (retrieved 2026-07-07)", "https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/skills/make-interfaces-feel-better/animations.md (retrieved 2026-07-07)", "https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/skills/make-interfaces-feel-better/surfaces.md (retrieved 2026-07-07)", "https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md (retrieved 2026-07-07)"]
sources: ["[[MIFB Repo and Skill File]]", "[[Reception Sources]]"]
---
Press Feedback and Hit Areas is the MIFB interaction rule pair: buttons should feel tactile at scale 0.96, and controls need usable hit areas.

## What it is
The MIFB animations capture says button press feedback should use scale 0.96.
The MIFB animations capture says the value should never go below 0.95.
The MIFB claim pack repeats the 0.96 and 0.95 values.
The MIFB surfaces capture says interactive elements need 44x44px by WCAG or at least 40x40px.
The slice brief emphasizes the 40x40px minimum hit area.
The MIFB surfaces capture says smaller visible elements can extend hit area with a pseudo-element.
The surfaces capture says overlapping hit areas should be avoided.
The Vercel command.md has a touch and interaction category.
UI UX Pro Max also records a 44x44pt touch target in its pre-delivery checklist.
The rule pair belongs to micro-interaction execution because it changes how controls feel under input.
The rule pair does not choose color, type, or layout direction.
The source ledger records the MIFB supporting files as retrieved on 2026-07-07.

## How it works
Use active press scaling for tactile feedback on eligible buttons.
Use scale 0.96 as the MIFB default.
Do not use a press scale smaller than 0.95.
Use a short transform transition so the press can reverse smoothly.
Add a static escape path when press motion would distract or conflict with the component role.
Check whether the visible control is at least 40x40px.
Prefer 44x44px when following the stronger WCAG-style target in the MIFB surfaces note.
Use pseudo-elements or equivalent hit slop when the visible affordance is smaller.
Do not let expanded hit areas overlap neighboring controls.
Test keyboard focus separately because hit area size does not prove accessibility.
Pair the hit-area check with focus-visible checks from Vercel command.md.
Pair the press-motion check with prefers-reduced-motion checks when motion intensity is above low levels.
For icon-only controls, pair hit area with accessible labeling from Vercel command.md.
For mobile controls, test touch behavior and not only pointer hover.

## Best practice
- Use scale 0.96 for button press feedback EVIDENCE-BASED
- Never use press scale below 0.95 EVIDENCE-BASED
- Use CSS transitions for press feedback so release can reverse smoothly EVIDENCE-BASED
- Provide a static option when scale motion would distract EVIDENCE-BASED
- Ensure every interactive element has at least a 40x40px hit area EVIDENCE-BASED
- Prefer 44x44px where the component can support it EVIDENCE-BASED
- Extend small visible controls with pseudo-elements or hit slop EVIDENCE-BASED
- Prevent overlapping expanded hit areas EVIDENCE-BASED
- Pair hit area checks with focus and label checks EVIDENCE-BASED
- Treat touch target sizes as dated source claims from the 2026-07-07 captures EVIDENCE-BASED

## Pitfalls
Scaling below 0.95 can make a button feel exaggerated.
Animating press with non-interruptible keyframes can make release feel broken.
Adding scale to every control can distract on dense or serious product surfaces.
Leaving a 20x20 checkbox with no expanded hit area creates a small target.
Expanding hit area into a neighboring control creates ambiguous taps.
Treating hover feedback as touch feedback misses mobile behavior.
Treating a large visual control as accessible without focus and label checks is incomplete.
Using emoji icons for structural controls conflicts with UI UX Pro Max checklist guidance.
Ignoring reduced-motion rules can conflict with Taste Skill, Vercel, and UI UX Pro Max.
Claiming the exact values are universal would exceed the MIFB evidence base.

> [!key-insight]
> Tactility is a paired rule: the button must respond to press, and the user must be able to hit it comfortably.

## Sources
- MIFB animations reference, https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/skills/make-interfaces-feel-better/animations.md, retrieved 2026-07-07.
- MIFB surfaces reference, https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/skills/make-interfaces-feel-better/surfaces.md, retrieved 2026-07-07.
- MIFB SKILL.md, https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/skills/make-interfaces-feel-better/SKILL.md, retrieved 2026-07-07.
- Vercel command.md, https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md, retrieved 2026-07-07.
- UI UX Pro Max SKILL.md, https://raw.githubusercontent.com/nextlevelbuilder/ui-ux-pro-max-skill/main/.claude/skills/ui-ux-pro-max/SKILL.md, retrieved 2026-07-07.
- Local MIFB claim pack, references/claim-packs/claim-pack-make-interfaces-feel-better.md, generated 2026-07-07.
- Local UI UX Pro Max claim pack, references/claim-packs/claim-pack-ui-ux-pro-max.md, generated 2026-07-07.

## Related
- [[Make Interfaces Feel Better (Skill)]] is the skill anchor for this interaction detail.
- [[MIFB Motion and Feedback Rules]] contains the press feedback values.
- [[MIFB Surface and Shadow Rules]] contains the hit area guidance.
- [[Interruptible Animation]] explains why press return must reverse smoothly.
- [[Concentric Radii]] is the nested-surface detail often checked in the same pass.
- [[MIFB Review Checklist]] turns the rule pair into a review item.
- [[Reception Sources|Vercel Web Design Guidelines]] provides focus and label audit context.
- [[UI UX Pro Max Repo|UX Rules Database (99 Rules)]] provides adjacent checklist evidence.
- [[Unified Pre-Flight Mega-Checklist]] will merge this with other stack checks.
- [[MIFB Repo and Skill File]] is the provenance note for the MIFB captures.

## Next actions
- Use this note when reviewing buttons, icon controls, checkboxes, and touch targets.
- Keep the 0.96 and 0.95 values tied to MIFB evidence.
- Keep the 40x40px floor and 44x44px preference distinct.
- Re-check the MIFB surfaces file before adding platform-specific target sizes.
- Add future screenshots only with recorded source provenance.

