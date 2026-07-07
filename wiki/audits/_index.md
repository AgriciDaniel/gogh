---
type: "meta"
title: "Audits Hub"
status: "evergreen"
created: "2026-07-07"
updated: "2026-07-07"
tags: ["gogh/ops", "note/meta"]
domain: "ops"
confidence: "evidence-based"
related: ["[[Index]]", "[[Hot]]", "[[Overview]]", "[[Start Here]]", "[[CONVENTIONS]]", "[[Tag Taxonomy]]"]
source_urls: []
sources: []
---

# Audits Hub

Audits holds the checks that decide whether stack output is ready to ship or needs another pass.

## Catalog

### gogh/taste-skill

- [[Brand fidelity audit]] - Brand fidelity audit verifies that a Taste Skill redesign preserved the existing accent color, type stack, and logo treatment unless the user approved an overhaul.
- [[Em-dash audit]] - Em-dash audit is the written Taste Skill check that visible output contains zero U+2014 or U+2013 glyphs.
- [[Hero discipline audit]] - Hero discipline audit verifies that the hero fits the first viewport, has concise copy, and keeps the CTA visible.
- [[Pre-Flight Check (Section 14)]] - Pre-Flight Check (Section 14) is the mandatory Taste Skill v2 final gate: every box must pass, while the popular 60-item count remains contested.
- [[Preservation audit]] - Preservation audit verifies that a Taste Skill redesign did not silently change URLs, navigation, forms, anchors, brand, or legal copy.
- [[Required Audits]] - Required Audits is the taste-skill-scoped list of written audits that run around Section 14 for greenfield and redesign work.
- [[Section-layout-repetition audit]] - Section-layout-repetition audit is the Taste Skill greenfield check that each section layout family is listed and repetition is blocked.

### gogh/mifb

- [[MIFB Review Checklist]] - MIFB Review Checklist turns the skill's 14 review items, common mistake fixes, and Before and After output format into a repeatable audit note.

### gogh/impeccable

- [[Impeccable Audit and Detect]] - Impeccable has two audit surfaces: `/impeccable audit` for technical quality review and `npx impeccable detect` for deterministic detector gating.

### gogh/web-design-guidelines

- [[Distinctiveness Audit]] - Distinctiveness Audit is the boring gate: six written questions (five-second test, screenshot test, incumbent test) that fail pages which pass every ban yet stay forgettable.
- [[Vercel Guidelines Audit]] - Vercel Guidelines Audit is the practical runbook for applying the runtime-fetched Vercel Web Interface Guidelines to specific UI files.

## Related

- [[Index]] returns to the master catalog.
- [[Hot]] shows the current operating state.
- [[Overview]] gives the one-screen product picture.
- [[Start Here]] orients new readers.
- [[CONVENTIONS]] defines note and hub contracts.
- [[Tag Taxonomy]] explains the domain groups used above.
