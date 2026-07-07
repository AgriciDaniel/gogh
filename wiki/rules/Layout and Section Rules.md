---
type: "note"
title: "Layout and Section Rules"
created: "2026-07-06"
updated: "2026-07-06"
status: "active"
confidence: "EVIDENCE-BASED"
---

# Layout and Section Rules

Confidence tag: EVIDENCE-BASED (canonical `SKILL.md` §4.3, §4.7, §4.8, §4.9, §10).

## Compiled Truth

**Composition (§4.3):** a centered hero is avoided when [[DESIGN_VARIANCE]] > 4 - force split-screen, asymmetric, or scroll-pinned.

**Section discipline (§4.7):**
- **Section-Layout-Repetition Ban:** each layout family appears at most **once**; a page with **8 sections uses >=4 different layout families.** This is the [[Section-layout-repetition audit]].
- **Zigzag alternation cap:** max **2 consecutive** image+text-split sections; the 3rd is a pre-flight Fail.
- **Eyebrow restraint** ("#1 violated rule in production tests"): **max 1 eyebrow per 3 sections**, hero counts as 1. Mechanical check: count `uppercase tracking` labels; if `count > ceil(sectionCount / 3)`, the output fails.
- **Split-header ban:** the "left big headline + right small explainer paragraph" section header is banned as a default; stack vertically at `max-width 65ch`.

**Bento grids:** exactly **N cells for N items** - no empty cell in the middle or end. Background diversity: >=2-3 cells need real visual variation.

**Cards / materiality (§4.4):** cards only when elevation communicates real hierarchy; at [[VISUAL_DENSITY]] > 7, generic card containers are banned. One radius scale ([[The Three Locks|Shape Lock]]). **No 3-column equal feature cards** (§9.C).

**Images (§4.8):** real images only, priority order - (1) image-gen tool first (must use if any available), (2) real web images via `https://picsum.photos/seed/{seed}/{w}/{h}`, (3) last resort labeled placeholder + tell the user. Even minimalist sites need >=2-3 images. Real logos via Simple Icons (`cdn.simpleicons.org/{slug}/ffffff`) or devicon, logo-only (no category labels). **Div-based fake screenshots are banned** ("the #1 LLM-design Tell").

**Content density (§4.9):** per section, headline <=8 words + sub-paragraph <=25 words + one asset/CTA. Lists > 5 items need a different UI component (not `<ul>` + `divide-y`). Mandatory copy self-audit before ship; flag fake-precise numbers.

**Sizing (§3):** `min-h-[100dvh]` never `h-screen`; Grid over flex-math (never `w-[calc(33%-1rem)]`); contain with `max-w-[1400px] mx-auto` or `max-w-7xl`. Breakpoints sm640 / md768 / lg1024 / xl1280 / 2xl1536; mobile collapse is explicit per section (<768px).

## §10 Reference vocabulary (named catalog, not a library)

Heroes (Asymmetric Split, Editorial Manifesto, Media Mask, Kinetic-Type, Curtain-Reveal, Scroll-Pinned), Nav (Dock Magnification, Magnetic Button, Dynamic Island, Mega Menu), Grids (Bento, Masonry, Chroma Grid, Split-Screen Scroll, Sticky-Stack), Cards (Parallax Tilt, Spotlight Border, Glassmorphism, Holographic Foil, Morphing Modal), Type (Kinetic Marquee, Text Mask, Scramble, Circular Path).

## Related

- [[Hero Discipline]] | [[DESIGN_VARIANCE]] | [[AI Tells (Forbidden Patterns)]] | [[Motion and Performance Rules]]
- Source: [[Canonical Skill File|Canonical SKILL.md]]

## Timeline

- 2026-07-06 - Note created.
