---
type: "note"
title: "Rules and Audits Reference Card"
created: "2026-07-06"
updated: "2026-07-06"
status: "active"
confidence: "EVIDENCE-BASED"
---

# Rules and Audits Reference Card

Confidence tag: EVIDENCE-BASED (canonical v2 `SKILL.md`, all sections; and `tasteskill.dev` Quick Reminders).

The whole skill on one page. Every item links to its detail note. Section numbers refer to the canonical `SKILL.md`.

## The dials (§1) - baseline 8 / 6 / 4

| [[DESIGN_VARIANCE]] | [[MOTION_INTENSITY]] | [[VISUAL_DENSITY]] |
|---|---|---|
| 1 symmetry -> 10 chaos (8) | 1 static -> 10 cinematic (6) | 1 airy -> 10 cockpit (4) |

Set conversationally, never by editing the file. See [[Dial Tuning Guide]].

## Hard thresholds (mechanical, checked at pre-flight)

- **Em-dashes: ZERO.** No `—` (U+2014) or en-dash `–` (U+2013) anywhere visible. Ranges use hyphen `-`. See [[Em-Dash Ban]].
- **Hero headline:** max **2 lines** desktop. **Subtext:** max **20 words** AND max 3-4 lines. **CTA:** visible without scroll. **Hero top padding:** `pt-24` (~6rem) max. **Hero stack:** max **4 text elements**. See [[Hero Discipline]].
- **Navigation:** single line at desktop, height **<=80px** (default 64-72px). See [[Navigation Discipline]].
- **Layout families:** each family appears at most **once**; an 8-section page uses **>=4 different families**. See [[Layout and Section Rules]].
- **Zigzag cap:** max **2 consecutive** image+text split sections; the 3rd fails.
- **Eyebrows:** max **1 per 3 sections** (hero counts as 1); if count > `ceil(sectionCount / 3)`, output fails. ("#1 violated rule in production tests.")
- **Bento:** exactly **N cells for N items** - no empty cell.
- **CTA:** fits **one line**, **3 words max** for primary (ideally 1-2); no two same-intent CTAs on a page.
- **Contrast:** WCAG **AA** - **4.5:1** body, **3:1** large text (18px+), for buttons and all form parts.
- **Locks:** **one accent, one radius scale, one page theme.** See [[The Three Locks]].
- **Quotes:** body max **3 lines**; no em-dashes; attribution = name + role, never name-only.
- **CWV:** LCP < **2.5s**, INP < **200ms**, CLS < **0.1**.
- **Sizing:** `min-h-[100dvh]` never `h-screen`; Grid over flex-math.

## Do-not (bans)

- No AI-purple / mesh-blob gradient defaults; no neon glows; no pure `#000`/`#fff`. See [[Color Rules]].
- No `Inter` as default display; no `Fraunces` or `Instrument_Serif` as default serif; serif only with a real reason. See [[Typography Rules]].
- No 3-equal feature cards; no split-header (big headline + right explainer); no generic card containers at density > 7.
- No div-based fake screenshots or hand-rolled SVG illustrations or icons. **Real images only** (gen-tool first, then `picsum.photos` seed).
- No section-number eyebrows, hero version labels, scroll cues, locale/weather strips, decorative status dots, pills on images, per-row hairlines, filled progress tracks, fake-perfect numbers, marketing version footers. Full list: [[AI Tells (Forbidden Patterns)]].
- No `window.addEventListener('scroll')` / `window.scrollY` in React state; no `useState` for continuous input. See [[Motion and Performance Rules]].

## Defaults (stack, §3)

React/Next.js (RSC default) · **Tailwind v4** · **Motion** (`motion/react`) · icons from Phosphor / HugeIcons / Radix / Tabler (`lucide` discouraged, one family, standard `strokeWidth`) · fonts via `next/font` or self-host (never `<link>` Google Fonts in prod) · **one design system per project**. See [[Architecture and Stack]].

## Scope (§0, §13)

For **landing pages, portfolios, redesigns.** Not dashboards, data tables, multi-step forms, code editors, native mobile, realtime collab. Every rule is contextual; none fires automatically. See [[Scope and Context]].

## The gates

1. Redesign only: [[Audit-First Redesign (Prompt 2)|the §11 audit]] before touching anything.
2. Always: the [[Pre-Flight Check (Section 14)]] - every box Pass/Fail with a one-line justification; any Fail blocks completion.
3. The [[Required Audits]]: em-dash, hero discipline, section-layout-repetition, brand fidelity, preservation.

## Related

- [[Index]] | [[The Three Dials]] | [[Pre-Flight Check (Section 14)]]
- Source: [[Canonical Skill File|Canonical SKILL.md]], [[Taste Skill Official Site]]

## Timeline

- 2026-07-06 - Card created.
