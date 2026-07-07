---
type: "note"
title: "VISUAL_DENSITY"
created: "2026-07-06"
updated: "2026-07-06"
status: "active"
confidence: "EVIDENCE-BASED"
---

# VISUAL_DENSITY

Confidence tag: EVIDENCE-BASED (canonical `SKILL.md` §1, §7).

## Compiled Truth

Controls **information per viewport** - spacing from luxury/airy to packed data.

- Scale: **1 = Art Gallery / Airy -> 10 = Pilot Cockpit / Packed Data.** Baseline **4**.
- Lower = generous whitespace, few elements. Higher = dense, data-rich.

**Technical bands (§7):**
- **1-3 art gallery** - large vertical rhythm, `py-32` to `py-48`.
- **4-7 daily app** - `py-16` to `py-24`.
- **8-10 cockpit** - 1px lines, `font-mono` mandatory for all numbers.

**Downstream rules:**
- When **VISUAL_DENSITY > 7**, generic card containers are banned (§4.4) - the layout should read as dense data, not spaced-out cards.
- Grounded in the whitespace principle from [[Encoded Design Principles]] (Refactoring UI: default airy, add density deliberately).

**Scope note:** high-density cockpit output butts against the skill's own scope - Taste Skill is for landing pages, portfolios, and redesigns, "not dashboards, not data tables." A genuine data-dense product UI is [[Scope and Context|out of scope]]; the high end of this dial is for density *within* a marketing/portfolio context, not a true dashboard.

## Related

- [[The Three Dials]] | [[Dial Tuning Guide]] | [[Scope and Context]] | [[Encoded Design Principles]]
- Source: [[Canonical Skill File|Canonical SKILL.md]]

## Timeline

- 2026-07-06 - Note created.
