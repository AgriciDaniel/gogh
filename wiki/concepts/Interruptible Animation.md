---
type: "concept"
title: "Interruptible Animation"
status: "developing"
created: "2026-07-07"
updated: "2026-07-07"
tags: ["gogh/mifb", "note/concept"]
domain: "mifb"
confidence: "evidence-based"
related: ["[[Make Interfaces Feel Better (Skill)]]", "[[MIFB Motion and Feedback Rules]]", "[[Press Feedback and Hit Areas]]", "[[Concentric Radii]]", "[[MIFB Performance Rules]]", "[[MIFB Review Checklist]]", "[[Motion Doctrine Conflicts]]", "[[MIFB Repo and Skill File]]"]
source_urls: ["https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/skills/make-interfaces-feel-better/SKILL.md (retrieved 2026-07-07)", "https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/skills/make-interfaces-feel-better/animations.md (retrieved 2026-07-07)", "https://jakub.kr/writing/details-that-make-interfaces-feel-better (retrieved 2026-07-07)"]
sources: ["[[MIFB Repo and Skill File]]"]
---
Interruptible Animation is the MIFB rule that interactive state changes should retarget smoothly instead of restarting from a fixed keyframe timeline.

## What it is
The MIFB animations capture contrasts CSS transitions with keyframes.
The capture says transitions interpolate toward the latest state.
The capture says keyframes run on a fixed timeline.
The capture marks transitions as interruptible.
The capture marks keyframes as not interruptible because they restart from the beginning.
The capture says interactive state changes should use CSS transitions.
The capture reserves keyframes for one-shot sequences.
The MIFB claim pack summarizes interruptible animations as a craft default.
The source ledger records the MIFB animations reference as retrieved on 2026-07-07.
The concept applies to hover, toggle, open, close, press, and similar state changes.
The concept does not ban one-shot entrance sequences.
The concept is an execution rule, not an aesthetic direction rule.

## How it works
An interactive transition should have a current state and a target state.
When the user reverses action mid-animation, the transition should retarget from the current visual position.
A hover-out midway through hover-in should return smoothly.
A toggle switched back midway should reverse from the current transform value.
A keyframe animation often restarts when the class or animation state changes.
That restart is why the MIFB capture reserves keyframes for one-shot sequences.
The animations capture recommends explicit transition properties.
The MIFB performance capture also warns against broad `transition: all` usage.
Vercel command.md independently bans `transition: all` in its animation and anti-pattern sections.
Taste Skill allows motion intensity to rise, but MIFB controls the execution values for state changes.
The Motion Doctrine Conflicts note records how dial ambition and fixed execution values fit together.
The interruptibility rule should be checked with real interaction, not only code reading.
The rule is especially visible on buttons, toggles, menus, icon swaps, accordions, and drawers.
The rule is complementary to reduced-motion handling because both protect interaction quality.

## Best practice
- Prefer CSS transitions for hover, toggle, open, close, and press states EVIDENCE-BASED
- Reserve keyframes for one-shot sequences such as enter animations or loading EVIDENCE-BASED
- List transition properties explicitly instead of using `transition: all` EVIDENCE-BASED
- Test mid-animation reversal on interactive components PRACTITIONER
- Use transform and opacity when motion can stay on compositor-friendly properties EVIDENCE-BASED
- Pair interruptibility with prefers-reduced-motion handling EVIDENCE-BASED
- Let Taste Skill's MOTION_INTENSITY set ambition and MIFB set concrete state-change values PRACTITIONER
- Do not add Motion or Framer Motion only for a small icon transition if CSS can cross-fade EVIDENCE-BASED
- Keep bounce at 0 for MIFB contextual icon spring values when Motion is already used EVIDENCE-BASED
- Treat this as MIFB evidence unless another skill states the same exact rule EVIDENCE-BASED

## Pitfalls
Using keyframes for hover can make reversal snap or restart.
Using `transition: all` can animate unintended properties.
Adding a motion dependency for one small icon swap can exceed the MIFB recommendation.
Forgetting reduced-motion handling can conflict with Taste Skill and Vercel accessibility rules.
Using scattered effects can conflict with Anthropic's one-orchestrated-moment guidance.
Treating a high Taste Skill motion dial as permission for janky state motion is a category error.
Animating layout properties can create performance problems.
Skipping real hover and toggle testing can miss non-interruptible behavior.
Using one-shot page-load thinking for controls can make controls feel sluggish.
Claiming this rule is independently measured would exceed the evidence set.

> [!key-insight]
> MIFB separates ambition from mechanics: the animation can be rich, but a control still needs to reverse smoothly.

## Sources
- MIFB SKILL.md, https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/skills/make-interfaces-feel-better/SKILL.md, retrieved 2026-07-07.
- MIFB animations reference, https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/skills/make-interfaces-feel-better/animations.md, retrieved 2026-07-07.
- MIFB performance reference, https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/skills/make-interfaces-feel-better/performance.md, retrieved 2026-07-07.
- Vercel command.md, https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md, retrieved 2026-07-07.
- Local MIFB claim pack, references/claim-packs/claim-pack-make-interfaces-feel-better.md, generated 2026-07-07.
- Local Vercel claim pack, references/claim-packs/claim-pack-vercel-web-design-guidelines.md, generated 2026-07-07.
- Local source ledger, references/source-ledger.json, generated 2026-07-06 with 2026-07-07 captures.

## Related
- [[Make Interfaces Feel Better (Skill)]] is the skill anchor for this rule.
- [[MIFB Motion and Feedback Rules]] contains the broader motion rule family.
- [[Press Feedback and Hit Areas]] uses this rule for active press return behavior.
- [[Concentric Radii]] is the surface-side companion to this execution detail.
- [[MIFB Performance Rules]] explains transition specificity and GPU hint restraint.
- [[MIFB Review Checklist]] turns this into a review item.
- [[Motion Doctrine Conflicts]] resolves fixed MIFB values against Taste Skill's dial.
- [[Anthropic Frontend Design Rules]] provides the one-orchestrated-moment motion context.
- [[Taste Skill Motion Rules|Motion and Performance Rules]] provides the Taste Skill motion context through the existing note.
- [[MIFB Repo and Skill File]] is the provenance note for the MIFB source bundle.

## Next actions
- Use this note when reviewing hover, toggle, menu, accordion, and drawer behavior.
- Keep examples tied to captured values from animations.md.
- Avoid adding new timing numbers without capture evidence.
- Re-check Vercel command.md before treating its transition rule count as current.
- Connect this note to screenshots only after source provenance exists.

