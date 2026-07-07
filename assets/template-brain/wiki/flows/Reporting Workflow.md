---
type: "flow"
title: "Reporting Workflow"
status: "seed"
created: "{{date}}"
updated: "{{date}}"
tags: ["gogh/ops", "note/flow"]
domain: "ops"
confidence: "practitioner"
related: ["[[Index]]", "[[Dashboard]]", "[[CONVENTIONS]]", "[[Tag Taxonomy]]", "[[Weekly Report]]", "[[Approval Queue]]"]
source_urls: []
sources: ["[[Source Manifest Guide]]"]
approval_status: "proposed"
risk_level: "low"
rollback_note: "Rerun synthesis or restore the prior report file from version control."
---

# Reporting Workflow

The reporting workflow turns sourced vault state into a shareable weekly report.

## What it is

This flow defines the minimum checks before rendering a report.

## How it works

1. Read [[Health Scorecard]] and [[Action Roadmap]].
2. Confirm every claim points to a source note or raw hash.
3. Render [[Weekly Report]].
4. Remove local paths and private data before sharing.

## Best practice

- Confirm source links before rendering. EVIDENCE-BASED
- Remove local paths before sharing. PRACTITIONER
- Keep report generation script-driven. PRACTITIONER

## Pitfalls

- Do not share reports with unresolved local paths.
- Do not cite unsupported claims.
- Do not hand-edit generated demo reports.

## Sources

- [[Source Manifest Guide]]

## Related

- [[Weekly Report]] is the target report.
- [[Health Scorecard]] provides readiness context.
- [[Action Roadmap]] provides next actions.
- [[Approval Queue]] controls release-affecting decisions.
- [[CONVENTIONS]] defines flow fields.
- [[Tag Taxonomy]] defines ops tagging.
- [[Index]] keeps the flow discoverable.
- [[Dashboard]] keeps the workflow visible.

## Next actions

- Run reporting only after source and synthesis checks pass.
