---
type: "note"
title: "Modernization Modes"
created: "2026-07-06"
updated: "2026-07-06"
status: "active"
confidence: "EVIDENCE-BASED"
---

# Modernization Modes

Confidence tag: EVIDENCE-BASED (canonical `SKILL.md` §11.A-F).

## Compiled Truth

Before any redesign, the skill picks a **mode** (§11.A). If ambiguous, it asks exactly once: *"Should this redesign preserve the existing brand, or are we starting visually from scratch?"*

| Mode | When | Behavior |
|---|---|---|
| **Greenfield** | No existing site, or full overhaul approved | Dial baseline from §1 (8 / 6 / 4). |
| **Redesign - Preserve** | Modernize without breaking the brand | Audit first, extract brand tokens, evolve gradually. Dials: match existing, MOTION +1. |
| **Redesign - Overhaul** | New visual language on existing content | Treat visuals as greenfield; preserve content + IA. Dials: VARIANCE +2, MOTION +2, DENSITY match. |

(The redesign prompt also names a third label, "Greenfield-with-content-preserved," which is the Overhaul path taken to its logical end: new visuals, same content and IA.)

## §11.D - Modernisation levers (priority order)

Apply in order, stop when the brief is satisfied:
1. **Typography refresh**
2. **Spacing & rhythm**
3. **Color recalibration**
4. **Motion layer**
5. **Hero / key-section recomposition**
6. **Full block replacement** (only when unsalvageable)

## §11.E - Decision tree

- IA / content / SEO sound -> **targeted evolution** (Levers 1-4): "~70% of the value at ~40% of the risk."
- Structural visual debt -> **full redesign with content preservation.**
- Brand is changing -> **greenfield.**

## §11.C / §11.F - Preservation guardrails

Preserve copy voice, existing accessibility wins, and analytics events. Extract brand colors *before* applying the [[Color Rules]] (a purple brand stays purple). **Never change silently without explicit approval:** URL structure / route slugs, primary nav labels, form field names/order, brand logo/wordmark, legal/consent/cookie copy. These are checked by the [[Preservation audit]] and [[Brand fidelity audit]].

## Related

- [[Audit-First Redesign (Prompt 2)]] | [[Required Audits]] | [[Color Rules]]
- Source: [[Canonical Skill File|Canonical SKILL.md]]

## Timeline

- 2026-07-06 - Note created.
