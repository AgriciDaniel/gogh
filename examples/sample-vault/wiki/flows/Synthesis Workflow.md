---
type: "flow"
title: "Synthesis Workflow"
status: "seed"
created: "2026-07-07"
updated: "2026-07-07"
tags: ["gogh/ops", "note/flow"]
domain: "ops"
confidence: "practitioner"
related: ["[[Index]]", "[[Dashboard]]", "[[CONVENTIONS]]", "[[Tag Taxonomy]]", "[[Source Intake Workflow]]", "[[Health Scorecard]]"]
source_urls: []
sources: ["[[Source Manifest Guide]]"]
approval_status: "proposed"
risk_level: "medium"
rollback_note: "Rerun synthesis from the same raw manifest or restore the prior generated notes."
---

# Synthesis Workflow

The synthesis workflow turns source notes into cited deliverables without inventing claims.

## What it is

This flow separates evidence, interpretation, recommendations, and rollback paths.

## How it works

1. Read source notes and `.raw/.manifest.json`.
2. Separate facts, interpretation, and recommendations.
3. Add confidence and failure path to recommendations.
4. Link recommendations to [[Approval Queue]] and [[Action Roadmap]].

## Best practice

- Separate facts from recommendations. EVIDENCE-BASED
- Link recommendations to approval status. PRACTITIONER
- Keep generated deliverables reproducible. PRACTITIONER

## Pitfalls

- Do not promote scaffold prose into source-backed claims.
- Do not write recommendations without confidence and rollback.
- Do not overwrite demo vault files by hand.

## Sources

- [[Source Manifest Guide]]

## Related

- [[Source Intake Workflow]] provides raw evidence.
- [[Health Scorecard]] reports current readiness.
- [[Best Practices Kernel]] defines review rules.
- [[Approval Queue]] controls decisions.
- [[Action Roadmap]] receives next actions.
- [[CONVENTIONS]] defines flow fields.
- [[Tag Taxonomy]] defines ops tagging.
- [[Index]] keeps the flow discoverable.

## Next actions

- Run synthesis after source intake and before report rendering.
