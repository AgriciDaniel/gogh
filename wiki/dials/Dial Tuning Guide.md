---
type: "note"
title: "Dial Tuning Guide"
created: "2026-07-06"
updated: "2026-07-06"
status: "active"
confidence: "EVIDENCE-BASED"
---

# Dial Tuning Guide

Confidence tag: EVIDENCE-BASED (canonical `SKILL.md` §1.A inference table and §1.B presets).

## Compiled Truth

You rarely set dials by hand. The skill infers them from brief signals, then you nudge conversationally. Baseline if nothing else applies: **8 / 6 / 4** ([[The Three Dials]]).

## §1.A - Inference table (signal -> VARIANCE / MOTION / DENSITY)

| Brief signal | VARIANCE | MOTION | DENSITY |
|---|---|---|---|
| minimalist / clean / calm / editorial / Linear-style | 5-6 | 3-4 | 2-3 |
| premium consumer / Apple-y / luxury / brand | 7-8 | 5-7 | 3-4 |
| playful / wild / Dribbble / Awwwards / experimental / agency | 9-10 | 8-10 | 3-4 |
| landing page / portfolio / marketing (default) | 7-9 | 6-8 | 3-5 |
| trust-first / public-sector / regulated / a11y-critical | 3-4 | 2-3 | 4-5 |
| redesign - preserve | match existing | +1 | match existing |
| redesign - overhaul | +2 | +2 | match existing |

## §1.B - Use-case presets

| Use case | Dials (V / M / D) |
|---|---|
| Landing - SaaS | 7 / 6 / 4 |
| Landing - Agency | 9 / 8 / 3 |
| Landing - Premium consumer | 7 / 6 / 3 |
| Portfolio - Designer | 8 / 7 / 3 |
| Portfolio - Developer | 6 / 5 / 4 |
| Editorial / Blog | 6 / 4 / 3 |
| Public-sector | 3 / 2 / 5 |

## How to use it

1. Let the skill read the brief and propose a Design Read + three dial values with one-line reasoning ([[Greenfield Build (Prompt 1)]] Step 1).
2. Sanity-check against the table above.
3. Override in conversation, not by editing the file: *"bump MOTION_INTENSITY to 8, this is an agency site."*
4. Remember the interactions: high VARIANCE forces non-centered heroes; MOTION > 4 must actually animate; DENSITY > 7 bans generic cards. See each dial note.

## Related

- [[The Three Dials]] | [[DESIGN_VARIANCE]] | [[MOTION_INTENSITY]] | [[VISUAL_DENSITY]]
- Source: [[Canonical Skill File|Canonical SKILL.md]]

## Timeline

- 2026-07-06 - Note created.
