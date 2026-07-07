---
type: "note"
title: "The Three Locks"
created: "2026-07-06"
updated: "2026-07-06"
status: "active"
confidence: "EVIDENCE-BASED"
---

# The Three Locks

Confidence tag: EVIDENCE-BASED (canonical `SKILL.md` §4.2/4.4/4.11; `tasteskill.dev` docs).

## Compiled Truth

Three consistency locks make a page cohere, and they are what turns "looks consistent" into a *verifiable* property (the point of [[Design Review as Infrastructure]]).

1. **Color Consistency Lock (§4.2).** One accent color locked across the whole page. Max 1 accent, saturation < 80% by default. See [[Color Rules]].
2. **Shape Consistency Lock (§4.4).** One corner-radius / radii scale per page. Cards only when elevation communicates real hierarchy; at [[VISUAL_DENSITY]] > 7, generic card containers are banned.
3. **Page Theme Lock (§4.11).** One theme (light, dark, or auto) chosen once at page level. Sections do **not** invert - "no light/dark flips mid-page." The single exception: one deliberate "Color Block Story" / "Theme Switch on Scroll," used at most once per page.

These three are explicit pre-flight items: "one accent / one radius / one theme lock." They complement the [[Dark Mode Protocol]] (dual-mode by default, but the *theme lock* governs a single render).

## Related

- [[Color Rules]] | [[Layout and Section Rules]] | [[Dark Mode Protocol]] | [[Rules and Audits Reference Card]]
- Source: [[Canonical Skill File|Canonical SKILL.md]]

## Timeline

- 2026-07-06 - Note created.
