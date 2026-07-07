---
type: "note"
title: "Typography Rules"
created: "2026-07-06"
updated: "2026-07-06"
status: "active"
confidence: "EVIDENCE-BASED"
---

# Typography Rules

Confidence tag: EVIDENCE-BASED (canonical `SKILL.md` §4.1).

## Compiled Truth

- **Display default:** `text-4xl md:text-6xl tracking-tighter leading-none`.
- **Body default:** `text-base text-gray-600 leading-relaxed max-w-[65ch]` (the 65-character measure comes straight from Butterick's line-length guidance - see [[Encoded Design Principles]]).
- **`Inter` is discouraged** as the default display face. Prefer Geist, Outfit, Cabinet Grotesk, or Satoshi.
- **Serif discipline (very discouraged as default).** "Creative brief = serif" is called *"the single most-tested AI tell in production rounds."* Use serif only if the brand names a serif OR the family is genuinely editorial / luxury / heritage with an articulated reason. **`Fraunces` and `Instrument_Serif` are specifically BANNED as defaults.**
- **Emphasis via italic or bold of the SAME font.** Mixing a second family for emphasis is called "amateur."
- **Italic descender clearance (mandatory):** italic display words containing `y g j p q` need `leading-[1.1]` minimum plus `pb-1`/`mb-1` reserve, or the descenders clip.

## Why it is opinionated (and contested)

Banning Inter and specific serifs is the clearest example critics point to when they say the skill encodes *opinions*, not laws - andrew.ooo: *"'Inter is banned for creative vibes' is a defensible opinion, but it is an opinion."* Because the `SKILL.md` is "fully editable," a team that loves Inter is expected to edit the file. See [[Reception and Criticism]].

## Related

- [[Color Rules]] | [[Hero Discipline]] | [[Encoded Design Principles]] | [[Rules and Audits Reference Card]]
- Source: [[Canonical Skill File|Canonical SKILL.md]]

## Timeline

- 2026-07-06 - Note created.
