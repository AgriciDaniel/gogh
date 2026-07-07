---
type: "concept"
title: "Encoded Design Principles"
created: "2026-07-06"
updated: "2026-07-06"
status: "active"
confidence: "EVIDENCE-BASED"
---

# Encoded Design Principles

Confidence tag: EVIDENCE-BASED (each rule maps to a named canonical design source).

## Compiled Truth

Taste Skill's ~800 lines of constraints are largely a *compression of canonical design literature into machine-enforceable rules*. The principles behind the rules:

- **Visual hierarchy (Refactoring UI - Wathan & Schoger).** Size, color, weight, and placement to signal importance is *"the most effective tool you have for making something feel 'designed.'"* Slop fails because it is **flat** - uniform spacing, equal-weight cards, no dominant element. This grounds [[Hero Discipline]] and the ban on 3-equal feature cards.
- **Whitespace / density (Refactoring UI).** *"To make something look great, you will often need more whitespace than you initially thought."* Start airy and remove - the theory under [[VISUAL_DENSITY]].
- **Typographic scale & measure (Butterick, Practical Typography).** Body 15-25px, line spacing 120-145%, line length 45-90 characters - which is exactly the skill's `max-w-[65ch]` body rule. Banning Inter and mandating a display face encodes the workhorse-body-vs-characterful-display pairing. See [[Typography Rules]].
- **Motion restraint (Material 3; WCAG).** Motion should be functional and express hierarchy; the accessibility floor is `prefers-reduced-motion` (WCAG technique C39). This grounds [[MOTION_INTENSITY]] being a *dial* (not always-on) and the rule to animate only `transform`/`opacity`. See [[Motion and Performance Rules]].
- **Bento grids.** Modular, variable-size CSS Grid tiles (popularized by Apple keynotes) legitimized *asymmetry with structure* - "big box = big deal" - the vocabulary for the high-[[DESIGN_VARIANCE]] end. See [[Layout and Section Rules]].
- **Color theory.** Dominant / secondary / accent discipline (e.g. 60-30-10); the indigo default is an artifact, not a choice. Grounds [[Color Rules]].
- **The case against decorative clutter (Rams; Tufte).** Dieter Rams: *"Good design is as little design as possible."* Edward Tufte's data-ink ratio / **chartjunk** - *"ink that does not tell the viewer anything new"* - argues for erasing non-informative ornament. Reflexive glassmorphism, glows, and shadow-on-everything are the UI equivalent. Grounds the [[AI Tells (Forbidden Patterns)]].

## The honest caveat

Empirical studies find users sometimes *prefer* moderate "chartjunk" and ornament (Nielsen Norman on clutter is mixed). So the anti-clutter and minimalism rules are **defaults, not laws** - the same posture as [[Constraint Beats Coaxing]]. This is also why critics call some rules "opinions" (see [[Reception and Criticism]]).

## Related

- [[Typography Rules]] | [[Color Rules]] | [[Layout and Section Rules]] | [[Motion and Performance Rules]]
- Source: [[Design Theory Sources]]

## Timeline

- 2026-07-06 - Note created.
