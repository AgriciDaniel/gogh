---
type: "note"
title: "Audit-First Redesign (Prompt 2)"
created: "2026-07-06"
updated: "2026-07-06"
status: "active"
confidence: "EVIDENCE-BASED"
---

# Audit-First Redesign (Prompt 2)

Confidence tag: EVIDENCE-BASED (verbatim from `tasteskill.dev/guide?view=full`; canonical `SKILL.md` §11).

## Compiled Truth

The official workflow for redesigning an existing site **without breaking it**. It is audit-first and gated at every step. Verbatim prompt:

```
I have loaded tasteskill v2 (experimental) as my only source of design rules.

Brief:
- Site: <URL or repo path>
- Mode: <preserve brand / overhaul / unsure>
- Audience: <who reads this>
- What works today: <2 to 3 specifics you want kept>
- What is broken today: <2 to 3 specifics you want fixed>
- SEO constraint: <which routes, headings, or anchors must not change>

Step 1. Run the Section 11 audit (Section 11.B in the skill):
- Brand tokens currently in use (primary, accent, type stack, radii)
- Information architecture (page tree, nav, conversion paths)
- Patterns to preserve (signature interactions, recognisable hero, copy voice)
- Patterns to retire (slop tells, broken layouts, dead links)
- Inferred dial reading of the current site (DESIGN_VARIANCE, MOTION_INTENSITY, VISUAL_DENSITY)
- SEO baseline (ranking pages, titles, anchors)
Post the audit in writing. Stop.

Step 2 (after my OK). Declare the mode (Preserve, Overhaul, or Greenfield-with-content-preserved)
        and which modernisation levers from Section 11.D you will apply, in priority order. Stop.

Step 3 (after my OK). Implement the changes. Keep URL structure, primary nav labels,
        form field names, brand logo, and legal copy unchanged unless I explicitly approve a change.

Step 4. Run in writing:
- Em-dash audit
- Pre-Flight Check (Section 14)
- Preservation audit: list every URL, nav label, form field, and anchor changed.
  Should be empty unless I approved.
- Brand fidelity audit: confirm the existing brand accent color, type stack, and logo treatment survived.

Any Fail blocks completion.
```

## Why audit-first

*"SEO migration is the #1 redesign risk"* (§11.B). The skill forces a written audit and an explicit mode decision *before* any change, and enforces [[Modernization Modes|preservation rules]] so a redesign cannot silently destroy what already works. The two extra audits here - **preservation** and **brand fidelity** - do not exist in the greenfield flow. See [[Required Audits]].

## The gated flow

Step 1 audit -> Stop -> your OK -> Step 2 mode + levers -> Stop -> your OK -> Step 3 implement -> Step 4 audits. Three explicit stop points keep a human in the loop before anything ships. Pick the mode with [[Modernization Modes]].

## Related

- [[Modernization Modes]] | [[Required Audits]] | [[Brand fidelity audit]] | [[Preservation audit]] | [[Pre-Flight Check (Section 14)]]
- Source: [[Taste Skill Official Site]], [[Canonical Skill File|Canonical SKILL.md]]

## Timeline

- 2026-07-06 - Note created.
