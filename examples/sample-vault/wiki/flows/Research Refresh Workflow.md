---
type: "flow"
title: "Research Refresh Workflow"
status: "seed"
created: "2026-07-07"
updated: "2026-07-07"
tags: ["gogh/ops", "note/flow"]
domain: "ops"
confidence: "practitioner"
related: ["[[Index]]", "[[Dashboard]]", "[[CONVENTIONS]]", "[[Tag Taxonomy]]", "[[Source Intake Workflow]]", "[[Source Manifest Guide]]"]
source_urls: []
sources: ["[[Source Manifest Guide]]"]
approval_status: "proposed"
risk_level: "medium"
rollback_note: "Keep prior sourced guidance until refreshed evidence is captured."
---

# Research Refresh Workflow

The research refresh workflow keeps fast-moving skill guidance tied to dated sources.

## What it is

Refresh cadence: on-changelog for github.com/Leonxlnx/taste-skill and tasteskill.dev/changelog; monthly for the SKILL.md rules and the three dials; quarterly for ecosystem coverage (Emil Kowalski, Developers Digest, skill directories) and the Anthropic Agent Skills / SKILL.md format.

## How it works

1. Start with official, primary, vendor, regulator, standards-body, or API docs.
2. Record URL, retrieval date, version, deprecation/sunset notes, and confidence.
3. Update `references/current-requirements.md`.
4. Only then update domain-specific recommendations.

## Best practice

- Prefer official and primary sources first. EVIDENCE-BASED
- Record retrieval dates with every source. EVIDENCE-BASED
- Mark contested claims instead of flattening conflicts. PRACTITIONER

## Pitfalls

- Do not treat social summaries as primary evidence.
- Do not refresh recommendations without recording source provenance.
- Do not hide upstream conflict between the six skills.

## Sources

- [[Source Manifest Guide]]

## Related

- [[Source Intake Workflow]] explains raw source capture.
- [[Source Manifest Guide]] defines provenance fields.
- [[Best Practices Kernel]] defines the review rule set.
- [[CONVENTIONS]] defines flow fields.
- [[Tag Taxonomy]] defines ops tagging.
- [[Health Scorecard]] shows freshness status.
- [[Index]] keeps the flow discoverable.
- [[Dashboard]] keeps the workflow visible.

## Next actions

- Refresh source records before changing stack guidance.
