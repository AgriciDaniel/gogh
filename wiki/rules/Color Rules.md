---
type: "note"
title: "Color Rules"
created: "2026-07-06"
updated: "2026-07-06"
status: "active"
confidence: "EVIDENCE-BASED"
---

# Color Rules

Confidence tag: EVIDENCE-BASED (canonical `SKILL.md` §4.2).

## Compiled Truth

- **Max 1 accent color, saturation < 80% by default.** Enforced by the [[The Three Locks|Color Consistency Lock]] (one accent across the whole page).
- **The Lila Rule.** AI purple/blue glow is discouraged. Use neutral bases (Zinc, Slate, Stone) plus one high-contrast accent. (This directly targets the indigo-default artifact described in [[AI Slop]].)
- **No pure `#000000` or `#ffffff`** - use off-black (e.g. `zinc-950`) and off-white. See [[Dark Mode Protocol]].

## The Premium-Consumer Palette Ban (mandatory)

Called the *"second-most-recurring AI-tell."* The beige/cream + brass/clay/oxblood/ochre + espresso family is banned as a default. Concretely banned hex values:
- **Backgrounds:** `#f5f1ea` `#f7f5f1` `#fbf8f1` `#efeae0` `#ece6db` `#faf7f1` `#e8dfcb`
- **Accents:** `#b08947` `#b6553a` `#9a2436` `#9c6e2a` `#bc7c3a` `#7d5621`
- **Text:** `#1a1714` `#1a1814` `#1b1814`

Rotate alternatives instead: Cold Luxury, Forest, Black-and-Tan, Cobalt + Cream, Terracotta + Slate, Olive + Brick + Paper, or monochrome + a single pop. Do not ship the same warm-craft palette twice in a row.

## Why

Palette discipline (dominant / secondary / accent) from [[Encoded Design Principles]], plus the specific observation that the purple and beige-brass defaults are *statistical artifacts*, not choices. The banned-hex list is the sharpest example of [[Design Review as Infrastructure|design review as machine-checkable rules]] - you can grep for these values.

## Related

- [[The Three Locks]] | [[Typography Rules]] | [[Dark Mode Protocol]] | [[AI Slop]]
- Source: [[Canonical Skill File|Canonical SKILL.md]]

## Timeline

- 2026-07-06 - Note created.
