---
type: "flow"
title: "Source Intake Workflow"
status: "seed"
created: "{{date}}"
updated: "{{date}}"
tags: ["gogh/ops", "note/flow"]
domain: "ops"
confidence: "practitioner"
related: ["[[Index]]", "[[Dashboard]]", "[[CONVENTIONS]]", "[[Tag Taxonomy]]", "[[Source Manifest Guide]]", "[[Research Refresh Workflow]]"]
source_urls: []
sources: ["[[Source Manifest Guide]]"]
approval_status: "proposed"
risk_level: "medium"
rollback_note: "Remove the source note and manifest entry if provenance is invalid."
---

# Source Intake Workflow

The source intake workflow preserves raw evidence before any synthesized advice changes.

## What it is

This flow is the path from raw source material to a linked source note.

## How it works

1. Store raw source under `.raw/sources/`.
2. Record source path, hash, owner, and retrieval date.
3. Create a note under `wiki/sources/`.
4. Link affected entities and deliverables.

## Best practice

- Store raw material before summarizing it. EVIDENCE-BASED
- Record sha256 hashes for raw files. EVIDENCE-BASED
- Link source notes back to affected deliverables. PRACTITIONER

## Pitfalls

- Do not mutate `.raw/` source material after ingest.
- Do not ingest credentials or private secrets.
- Do not cite source notes that do not point to raw evidence.

## Sources

- [[Source Manifest Guide]]

## Related

- [[wiki/sources/_index|Sources Hub]] catalogs source notes.
- [[Source Manifest Guide]] defines source fields.
- [[Best Practices Kernel]] defines review rules.
- [[Research Refresh Workflow]] explains freshness.
- [[Synthesis Workflow]] consumes source notes.
- [[Health Scorecard]] reports provenance readiness.
- [[CONVENTIONS]] defines flow fields.
- [[Tag Taxonomy]] defines ops tagging.

## Next actions

- Add source notes only after the raw file and manifest entry exist.
