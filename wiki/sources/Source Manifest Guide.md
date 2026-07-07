---
type: "source"
title: "Source Manifest Guide"
created: "2026-07-06"
updated: "2026-07-06"
status: "active"
---

# Source Manifest Guide

How this brain records evidence, so claims stay checkable.

Every source note (and every row in `references/source-ledger.json`) carries:

- **URL or path** - where it lives.
- **Retrieved date** - when it was captured (all current captures: 2026-07-06).
- **Source type** - `official` / `primary` / `vendor` (authoritative) or `secondary` (coverage).
- **Confidence** - EVIDENCE-BASED, PRACTITIONER, CONTESTED, or FOLKLORE.
- **What it proves and does not prove** - scope of the claim it can support.

Rules of the house:
- Primary (canonical `SKILL.md`, `tasteskill.dev`) outranks secondary for any factual claim.
- Two facts are held CONTESTED: [[Leon Lin]]'s age, and the [[Taste as the Moat|taste-as-a-file premise]].
- One number is vendor-unstated: the "60-item" count for the [[Pre-Flight Check (Section 14)]].
- Raw captures live in `.raw/research/` and are immutable; wiki notes synthesize them.

Related: [[wiki/sources/_index|Sources Hub]] | [[Dashboard]]
