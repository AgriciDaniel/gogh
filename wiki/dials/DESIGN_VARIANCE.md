---
type: "note"
title: "DESIGN_VARIANCE"
created: "2026-07-06"
updated: "2026-07-06"
status: "active"
confidence: "EVIDENCE-BASED"
---

# DESIGN_VARIANCE

Confidence tag: EVIDENCE-BASED (canonical `SKILL.md` §1, §7).

## Compiled Truth

Controls **layout experimentation** - how far the composition moves from centered/symmetric toward asymmetric/experimental.

- Scale: **1 = Perfect Symmetry -> 10 = Artsy Chaos.** Baseline **8**.
- Lower = centered, clean, predictable. Higher = asymmetric, modern, offset.

**Technical bands (§7):**
- **1-3 predictable** - conventional centered layouts.
- **4-7 offset** - deliberate asymmetry, split compositions.
- **8-10 asymmetric** - strong asymmetry, scroll-pinned, experimental.
- **Mobile override:** levels 4-10 must collapse to a strict single column below 768px.

**Key downstream rules:**
- A **centered hero is avoided when DESIGN_VARIANCE > 4** - force split-screen, asymmetric, or scroll-pinned instead (§4.3). This is a [[Pre-Flight Check (Section 14)]]-adjacent constraint and one of the most-cited examples of the dial changing generation logic.
- High variance pairs with the bento / asymmetric grid vocabulary - see [[Layout and Section Rules]].

## Related

- [[The Three Dials]] | [[Dial Tuning Guide]] | [[Layout and Section Rules]]
- Source: [[Canonical Skill File|Canonical SKILL.md]]

## Timeline

- 2026-07-06 - Note created.
