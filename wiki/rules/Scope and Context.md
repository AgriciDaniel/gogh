---
type: "note"
title: "Scope and Context"
created: "2026-07-06"
updated: "2026-07-06"
status: "active"
confidence: "EVIDENCE-BASED"
---

# Scope and Context

Confidence tag: EVIDENCE-BASED (canonical `SKILL.md` scope statement, §0, §13).

## Compiled Truth

**What it is for:** landing pages, portfolios, and redesigns.

**What it is NOT for (§13, out of scope):**
- Dashboards and dense product UI.
- Data tables (use TanStack Table / AG Grid).
- Multi-step forms and wizards.
- Code editors (use Monaco / CodeMirror).
- Native mobile (follow Apple HIG / Material).
- Realtime collaboration UIs.

**The meta-rule:** every rule in the skill is **contextual**, and *"none of it fires automatically."* The agent first reads the room (§0 [[Greenfield Build (Prompt 1)|Brief Inference]]) and applies rules that fit. This is the antidote to cargo-culting - the rules are defaults for a *marketing/portfolio* context, not universal laws.

## Why this matters for the brain

The biggest misuse risk is applying Taste Skill's rules where they do not belong - e.g. forcing "real images only" or "no data-dump sections" onto a genuine analytics dashboard, which the skill itself says is out of scope. The high end of [[VISUAL_DENSITY]] (cockpit) is for density *within* a marketing context, not a substitute for a real data-table library. When in doubt, honor §13 and reach for the right tool. This connects to the [[Reception and Criticism]] point that rules can "become trend-chasing" if applied without judgment.

## Related

- [[VISUAL_DENSITY]] | [[Greenfield Build (Prompt 1)]] | [[Constraint Beats Coaxing]] | [[Rules and Audits Reference Card]]
- Source: [[Canonical Skill File|Canonical SKILL.md]]

## Timeline

- 2026-07-06 - Note created.
