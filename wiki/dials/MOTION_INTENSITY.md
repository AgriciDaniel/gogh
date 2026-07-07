---
type: "note"
title: "MOTION_INTENSITY"
created: "2026-07-06"
updated: "2026-07-06"
status: "active"
confidence: "EVIDENCE-BASED"
---

# MOTION_INTENSITY

Confidence tag: EVIDENCE-BASED (canonical `SKILL.md` §1, §5, §7).

## Compiled Truth

Controls **animation depth** - from static to cinematic, physics-driven motion.

- Scale: **1 = Static -> 10 = Cinematic / Magic Physics.** Baseline **6**.
- Lower = hover/active states only. Higher = scroll-driven, magnetic, choreographed.

**Technical bands (§7):**
- **1-3 static** - hover/active only.
- **4-7 fluid CSS** - `transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1)`.
- **8-10 advanced choreography** - scroll-driven, GSAP; `window.addEventListener('scroll')` is a **hard ban** (use the approved scroll primitives instead).

**Load-bearing rules tied to this dial:**
- **"Motion claimed, motion shown":** if MOTION_INTENSITY > 4 the page must *actually* animate; otherwise drop the dial to 3. (Also stated in the site's Quick Reminders: "If MOTION_INTENSITY is greater than 4, the page actually animates. Otherwise drop the dial.")
- **Motion must be motivated** - hierarchy, storytelling, feedback, or state transition; "it looked cool" is invalid.
- **Reduced motion is mandatory** for anything MOTION_INTENSITY > 3 (`prefers-reduced-motion`).
- Magnetic micro-physics only when MOTION_INTENSITY > 5 *and* premium/playful/agency context, via `useMotionValue`/`useTransform` - **never** `useState` for continuous input.
- Marquee: **max one per page.**

See [[Motion and Performance Rules]] for the full animation ruleset (spring config, forbidden scroll patterns, GSAP skeletons).

## Related

- [[The Three Dials]] | [[Motion and Performance Rules]] | [[Dial Tuning Guide]]
- Source: [[Canonical Skill File|Canonical SKILL.md]]

## Timeline

- 2026-07-06 - Note created.
