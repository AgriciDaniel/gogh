---
type: "note"
title: "Pre-Flight Check (Section 14)"
created: "2026-07-06"
updated: "2026-07-06"
status: "active"
confidence: "EVIDENCE-BASED"
---

# Pre-Flight Check (Section 14)

Confidence tag: EVIDENCE-BASED (canonical `SKILL.md` §14). The "60-item" count is CONTESTED - see below.

## Compiled Truth

The master gate. §14 opens: *"THIS IS NOT OPTIONAL. Run every box. If any box fails, the output is not done."* It mechanically re-verifies every threshold in the skill, each box marked **Pass or Fail with a one-line justification**. It closes with: *"If a single checkbox cannot be honestly ticked, the page is not done."*

**Load-bearing mechanical items (each links to its rule):**
- **Zero em-dashes** anywhere. -> [[Em-Dash Ban]]
- **Eyebrow count <= `ceil(sectionCount / 3)`** (hero counts as 1). -> [[Layout and Section Rules]]
- **Nav one line, <= 80px.** -> [[Navigation Discipline]]
- **Hero headline <= 2 lines, subtext <= 20 words AND <= 4 lines, `pt-24` max, <= 4 text elements.** -> [[Hero Discipline]]
- **>= 4 layout families across 8 sections; no 3+ consecutive zigzag; N items -> N bento cells.** -> [[Layout and Section Rules]]
- **CTA <= 1 line, no duplicate-intent CTAs.**
- **WCAG AA button + form contrast** (4.5:1 body, 3:1 large).
- **One accent / one radius / one theme lock.** -> [[The Three Locks]]
- **Serif not `Fraunces`/`Instrument_Serif`; premium-consumer palette not beige+brass.** -> [[Typography Rules]], [[Color Rules]]
- **Italic descender `leading-[1.1]` + `pb-1`; quotes <= 3 lines.**
- **CWV: LCP < 2.5s, INP < 200ms, CLS < 0.1.** -> [[Motion and Performance Rules]]
- **`min-h-[100dvh]` never `h-screen`; no `window.addEventListener('scroll')`; reduced motion for MOTION_INTENSITY > 3.**
- **One design system per project.** -> [[Architecture and Stack]]

## The "60-item" question

Third-party coverage (neodrop.ai) describes §14 as a **"60-item preflight check."** The **official site does not state a count**, and the canonical `SKILL.md` frames it as "every box," not a fixed number. Treat "60" as a reported figure, not a vendor-stated fact. Watch for the skill to publish a count at v2.0.0 stable. See [[Hot]].

## Why it exists

It is the in-loop [[Design Review as Infrastructure|self-judge]] - the same model that generated the page scores it against an explicit rubric before finishing. Without this check-back, output reverts to [[AI Slop|the mean]].

## Related

- [[Required Audits]] | [[Rules and Audits Reference Card]] | [[Design Review as Infrastructure]]
- Source: [[Canonical Skill File|Canonical SKILL.md]], [[neodrop.ai - v2 deep dive]]

## Timeline

- 2026-07-06 - Note created.
