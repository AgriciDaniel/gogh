---
type: "decision"
title: "{{title}}"
status: "seed"
created: "{{date}}"
updated: "{{date}}"
tags: ["gogh/ops", "note/decision"]
domain: "ops"
confidence: "practitioner"
related: ["[[Index]]", "[[Dashboard]]", "[[Approval Queue]]", "[[CONVENTIONS]]", "[[Tag Taxonomy]]", "[[Source Manifest Guide]]"]
source_urls: []
sources: ["[[Source Manifest Guide]]"]
approval_status: "proposed"
risk_level: "medium"
rollback_note: "Describe the exact rollback path before approval."
---

# {{title}}

Answer first: state the decision in one sentence before adding context.

## What it is

Describe the decision and the operating context it affects.

## How it works

Explain how the decision changes operator behavior, vault structure, or generated output.

## Best practice

- Tie the decision to dated evidence. EVIDENCE-BASED
- Record approval before mutation. PRACTITIONER
- Keep rollback concrete and testable. PRACTITIONER

## Pitfalls

- Do not approve unsupported domain claims.
- Do not hide risk level.
- Do not leave rollback blank.

## Sources

- [[Source Manifest Guide]]

## Related

- [[Approval Queue]] explains approval state.
- [[CONVENTIONS]] defines decision fields.
- [[Tag Taxonomy]] defines domain tags.
- [[Index]] keeps the note discoverable.
- [[Dashboard]] links the operator surface.
- [[Source Intake Workflow]] explains evidence capture.
- [[Synthesis Workflow]] explains downstream use.
- [[Action Roadmap]] records next work.

## Next actions

- Add approver, risk, and rollback details before acting.
