---
type: "note"
title: "Motion and Performance Rules"
created: "2026-07-06"
updated: "2026-07-06"
status: "active"
confidence: "EVIDENCE-BASED"
---

# Motion and Performance Rules

Confidence tag: EVIDENCE-BASED (canonical `SKILL.md` §5, §6, §7).

## Compiled Truth

Motion is governed by the [[MOTION_INTENSITY]] dial and a set of hard technical rules.

**Motion honesty:**
- **"Motion claimed, motion shown"** - if MOTION_INTENSITY > 4 the page must actually animate, else drop the dial to 3.
- **Motion must be motivated** - hierarchy, storytelling, feedback, or state transition. "It looked cool" is invalid.
- **Marquee: max one per page.**

**How to animate (§5):**
- Spring physics: `type: "spring", stiffness: 100, damping: 20` - no linear easing.
- Magnetic micro-physics only when MOTION_INTENSITY > 5 and premium/playful/agency, via `useMotionValue` / `useTransform`.
- Canonical GSAP skeletons for scrolltelling (§5.A Sticky-Stack, §5.B Horizontal-Pan): require `start: "top top"`, `pin: true`, correct `scrub`. §5.C is a lighter Motion `whileInView` stagger.

**Forbidden (§5.D) - hard bans:**
- `window.addEventListener("scroll")`
- `window.scrollY` held in React state
- `requestAnimationFrame` loops that touch React state
- `useState` for any continuous input (mouse/scroll/pointer)

Approved scroll primitives instead: Motion `useScroll`, GSAP `ScrollTrigger`, `IntersectionObserver`, or CSS scroll-driven animations.

**Performance & a11y (§6):**
- Animate only `transform` and `opacity` - never `top`/`left`/`width`/`height`.
- **Reduced motion is mandatory** for anything MOTION_INTENSITY > 3 (`prefers-reduced-motion`).
- **Core Web Vitals targets: LCP < 2.5s, INP < 200ms, CLS < 0.1.**
- Grain/noise only on `fixed pointer-events-none` pseudo-elements. Z-index restraint.

**Library boundary (§10):** Motion is the default; GSAP + ScrollTrigger for scrolltelling; Three.js/WebGL for 3D. **Never mix GSAP/Three.js with Motion in the same component tree.**

## Why

Encodes motion restraint and compositor-friendly animation from [[Encoded Design Principles]] (Material 3 functional motion, WCAG C39 reduced-motion). The `useState`/scroll-listener bans are the "concrete engineering craft" reviewers praise ([[Reception and Criticism]]).

## Related

- [[MOTION_INTENSITY]] | [[Architecture and Stack]] | [[Dark Mode Protocol]] | [[Rules and Audits Reference Card]]
- Source: [[Canonical Skill File|Canonical SKILL.md]]

## Timeline

- 2026-07-06 - Note created.
