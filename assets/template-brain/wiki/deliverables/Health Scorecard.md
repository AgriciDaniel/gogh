---
type: "deliverable"
title: "Health Scorecard"
status: "seed"
created: "{{date}}"
updated: "{{date}}"
tags: ["gogh/ops", "note/deliverable"]
domain: "ops"
confidence: "practitioner"
related: ["[[Index]]", "[[Dashboard]]", "[[CONVENTIONS]]", "[[Tag Taxonomy]]", "[[Action Roadmap]]", "[[Weekly Report]]"]
source_urls: []
sources: ["[[Source Manifest Guide]]"]
---

# Health Scorecard

The health scorecard summarizes source provenance, research freshness, and reporting readiness.

## What it is

This deliverable is a compact readiness view for the scaffolded vault.

## How it works

Each row points to the note or workflow that explains the current state.

## Best practice

- Cite the evidence note for every row. EVIDENCE-BASED
- Keep low confidence visible until source intake is complete. PRACTITIONER
- Recheck readiness after synthesis writes deliverables. PRACTITIONER

## Pitfalls

- Do not mark source provenance as ready without `.raw/.manifest.json`.
- Do not mark research fresh from scaffold prose alone.
- Do not remove low confidence without replacing it with dated evidence.

| Area | Status | Evidence | Confidence |
|---|---|---|---:|
| Source provenance | Needs source intake | [[Source Manifest Guide]] | low |
| Research freshness | Needs refresh | [[Research Refresh Workflow]] | low |
| Reporting readiness | Draft | [[Weekly Report]] | low |

## Sources

- [[Source Manifest Guide]]

## Related

- [[Action Roadmap]] turns scorecard gaps into work.
- [[Weekly Report]] summarizes the current week.
- [[Research Refresh Workflow]] explains freshness checks.
- [[Source Intake Workflow]] explains source capture.
- [[CONVENTIONS]] defines deliverable structure.
- [[Tag Taxonomy]] defines ops tagging.
- [[Index]] keeps this scorecard discoverable.
- [[Dashboard]] keeps the active operator links visible.

## Next actions

- Refresh this scorecard after each source intake or synthesis run.
