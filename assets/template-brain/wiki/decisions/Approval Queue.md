---
type: "decision"
title: "Approval Queue"
status: "seed"
created: "{{date}}"
updated: "{{date}}"
tags: ["gogh/ops", "note/decision"]
domain: "ops"
confidence: "practitioner"
related: ["[[Index]]", "[[Dashboard]]", "[[CONVENTIONS]]", "[[Tag Taxonomy]]", "[[Action Roadmap]]", "[[Best Practices Kernel]]"]
source_urls: []
sources: ["[[Source Manifest Guide]]"]
approval_status: "proposed"
risk_level: "medium"
rollback_note: "Leave the proposed action unchanged until a sourced rollback path exists."
---

# Approval Queue

No action is approved until it has source, confidence, owner, status, and rollback.

## What it is

The approval queue is the control point for decisions that may change vault outputs or operator behavior.

## How it works

Add proposed changes here before applying them to release-affecting notes, reports, or workflows.

## Best practice

- Require an owner before approval. PRACTITIONER
- Require a dated source before approval. EVIDENCE-BASED
- Record rollback before implementation. PRACTITIONER

## Pitfalls

- Do not treat an empty rollback as an approved rollback.
- Do not approve mutation decisions from unsupported claims.
- Do not skip this queue for release-affecting workflow changes.

## Queue

| Action | Source | Confidence | Owner | Status | Rollback |
|---|---|---:|---|---|---|
| Confirm first source pack | [[Source Manifest Guide]] | practitioner | {{owner}} | proposed | Leave scaffold notes unchanged |

## Sources

- [[Source Manifest Guide]]

## Related

- [[Action Roadmap]] lists planned work.
- [[Best Practices Kernel]] gives the review rule set.
- [[CONVENTIONS]] defines decision frontmatter.
- [[Tag Taxonomy]] defines the ops tag.
- [[Health Scorecard]] shows source readiness.
- [[Reporting Workflow]] describes report gates.
- [[Synthesis Workflow]] describes synthesis gates.
- [[Index]] keeps the queue discoverable.

## Next actions

- Add one proposed row for each release-affecting decision.
