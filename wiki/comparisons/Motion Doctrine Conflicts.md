---
type: "comparison"
title: "Motion Doctrine Conflicts"
status: "developing"
created: "2026-07-07"
updated: "2026-07-07"
tags: ["gogh/stack", "note/comparison"]
domain: "stack"
confidence: "contested"
related: ["[[The Three Dials]]", "[[MOTION_INTENSITY]]", "[[MIFB Motion and Feedback Rules]]", "[[Interruptible Animation]]", "[[Press Feedback and Hit Areas]]", "[[Anthropic Frontend Design Rules]]", "[[Unified Anti-Slop Rulebook]]", "[[Full Stack Build Flow]]"]
source_urls: ["https://raw.githubusercontent.com/Leonxlnx/taste-skill/main/skills/taste-skill/SKILL.md (retrieved 2026-07-07)", "https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/skills/make-interfaces-feel-better/animations.md (retrieved 2026-07-07)", "https://raw.githubusercontent.com/anthropics/skills/main/skills/frontend-design/SKILL.md (retrieved 2026-07-07)", "https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md (retrieved 2026-07-07)"]
sources: ["[[Canonical Skill File]]", "[[MIFB Repo and Skill File]]", "[[Anthropic Frontend Design Skill and Post]]", "[[Reception Sources]]"]
---
Motion Doctrine Conflicts resolves the difference between Taste Skill's tunable motion ambition and MIFB's fixed execution values.

## What it is
Taste Skill defines MOTION_INTENSITY on a 1-10 scale.
Taste Skill baseline dials are 8 for design variance, 6 for motion intensity, and 4 for visual density.
Taste Skill says higher motion needs motivated animation and reduced-motion handling.
MIFB gives fixed values for several micro-interactions.
MIFB button press feedback uses scale 0.96 and never below 0.95.
MIFB contextual icon animation uses scale 0.25 to 1 with opacity and blur.
MIFB Motion spring values use duration 0.3 and bounce 0.
MIFB prefers CSS transitions for interactive state changes.
Anthropic says one well-orchestrated motion moment can land harder than scattered effects.
Vercel command.md audits prefers-reduced-motion and bans `transition: all`.
The conflict is not a contradiction when the layers are separated.
The recommended resolution is: dial sets ambition, MIFB sets execution values.

## How it works
| Situation | Taste Skill role | MIFB role | Resolution |
|---|---|---|---|
| Project asks for static UI | MOTION_INTENSITY 1-3 allows only hover and active states | Press feedback still uses restrained values if used | Keep motion minimal |
| Project asks for rich landing page | MOTION_INTENSITY 4-7 or 8-10 raises ambition | Buttons and icon swaps still use fixed MIFB values | Rich page, precise controls |
| Button press feels weak | Dial does not name exact press scale | MIFB says scale 0.96 | Use MIFB value |
| Icon swap feels clumsy | Dial says whether motion should exist | MIFB says scale 0.25, opacity, blur, duration 0.3, bounce 0 | Use MIFB values |
| Scroll storytelling is requested | Taste Skill supplies GSAP and Motion skeletons | MIFB focuses on state transitions and subtle exits | Use Taste Skill pattern and MIFB polish |
| Motion is scattered | Anthropic warns excess animation reads AI-generated | MIFB still permits micro feedback | Keep one orchestrated moment and tactile controls |
| Reduced motion is required | Taste Skill makes it mandatory above low motion | Vercel audits it | Gate release on reduced-motion behavior |
| CSS transition is too broad | Taste Skill cares about quality and performance | MIFB and Vercel reject `transition: all` | List properties explicitly |

> [!key-insight]
> The dial answers how much the page should move; MIFB answers how a specific control should move.

## Best practice
- Set MOTION_INTENSITY from the project brief before choosing motion patterns EVIDENCE-BASED
- Use MIFB's 0.96 press scale when implementing tactile buttons EVIDENCE-BASED
- Keep press scale at or above 0.95 EVIDENCE-BASED
- Use MIFB's bounce 0 value for contextual icon springs EVIDENCE-BASED
- Prefer transitions over keyframes for interactive state changes EVIDENCE-BASED
- Use Taste Skill's motivated-motion rule to decide whether an animation should exist EVIDENCE-BASED
- Use Anthropic's one-orchestrated-moment guidance to avoid scattered animation PRACTITIONER
- Run Vercel or checklist review for prefers-reduced-motion coverage EVIDENCE-BASED
- Treat MIFB values as execution defaults, not whole-page motion strategy PRACTITIONER
- Document any deliberate departure from fixed MIFB values in the design contract PRACTITIONER

## Pitfalls
Raising MOTION_INTENSITY does not justify changing press scale to 0.90.
Using MIFB fixed values does not satisfy a cinematic brief by itself.
Using keyframes for interactive hover can break mid-animation reversal.
Adding scroll effects without a communicative reason conflicts with Taste Skill.
Adding many small loops can conflict with Anthropic's scattered-effects warning.
Forgetting reduced-motion handling can fail Taste Skill and Vercel checks.
Using `transition: all` can fail MIFB and Vercel guidance.
Treating Motion library availability as a reason to animate everything conflicts with Taste Skill.
Treating static pages as finished when the dial says motion above 4 conflicts with Taste Skill.
Treating MIFB as independent empirical truth would exceed its single-source caveats.

## Sources
- Taste Skill SKILL.md, https://raw.githubusercontent.com/Leonxlnx/taste-skill/main/skills/taste-skill/SKILL.md, retrieved 2026-07-07.
- MIFB animations reference, https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/skills/make-interfaces-feel-better/animations.md, retrieved 2026-07-07.
- Anthropic frontend-design SKILL.md, https://raw.githubusercontent.com/anthropics/skills/main/skills/frontend-design/SKILL.md, retrieved 2026-07-07.
- Vercel command.md, https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md, retrieved 2026-07-07.
- Claim pack taste-skill-v2, references/claim-packs/claim-pack-taste-skill-v2.md, generated 2026-07-07.
- Claim pack MIFB, references/claim-packs/claim-pack-make-interfaces-feel-better.md, generated 2026-07-07.
- Claim pack theory, references/claim-packs/claim-pack-theory.md, generated 2026-07-07.

## Related
- [[The Three Dials]] defines the dial system.
- [[MOTION_INTENSITY]] is the specific Taste Skill motion dial.
- [[MIFB Motion and Feedback Rules]] holds the fixed MIFB values.
- [[Interruptible Animation]] explains the transition-over-keyframe rule.
- [[Press Feedback and Hit Areas]] explains tactile press values.
- [[Anthropic Frontend Design Rules]] covers concentrated motion guidance.
- [[Unified Anti-Slop Rulebook]] records shared motion bans.
- [[Full Stack Build Flow]] shows ordering for direction then feel pass.
- [[Audit Pipeline Flow]] shows where reduced-motion checks gate release.
- [[Design Skills Mechanism Map]] explains the mechanism split behind the conflict.

## Next actions
- Use this comparison whenever a stack report includes Taste Skill and MIFB together.
- Add screenshots or timing traces only when source provenance is recorded.
- Re-check MIFB animations.md before changing fixed values.
- Re-check Taste Skill Section 5 and 7 before changing dial interpretation.
- Keep reduced-motion checks in the audit pipeline for any non-static motion plan.

