---
type: "concept"
title: "Anti-Laziness Research"
created: "2026-07-06"
updated: "2026-07-06"
status: "active"
confidence: "EVIDENCE-BASED"
---

# Anti-Laziness Research

Confidence tag: EVIDENCE-BASED (repo `research/laziness/`; underlying studies are third-party).

## Compiled Truth

The repo ships a `research/laziness/` folder that is the empirical backing for the `output-skill` (`full-output-enforcement`) - the skill that bans placeholder-comment stubs (`// ...` and the like, "for brevity") and half-finished output, and defines a `[PAUSED - X of Y complete...]` continuation protocol. This is the "anti-laziness rules for agents" pillar of the framework.

**Findings.** A Dec-2025 controlled study (GPT-4 variants, DeepSeek): no model natively satisfied both a length target and all sub-part instructions; truncation is a **deliberate behavioral choice, not a decoding failure**; models stayed resilient over 200-turn tests (context loss is not the primary cause). A Microsoft Research prompt-stimulus table is cited: "$200 tip" +45% length; "take a deep breath" 34% -> 80% logic accuracy; "critical to my career" +10%; combined up to +115%. A seasonal output-length dip (Nov-Dec 2023 vs Jan-Mar 2024) is documented.

**Root causes** (per the folder): RLHF/compute brevity bias, training-data placeholder propagation, cognitive shortcuts, and output-limit asymmetry (large input windows vs a small ~8k output cap; consumer middleware caps history ~32k tokens; the developer API bypasses truncation).

**Remediation:** parameter tuning, prompt engineering (syntax binding, XML frameworks, verification loops), architectural patterns (MCP, lazy-loaded skills), and reference prompts.

## Why it matters here

It shows the project treats "slop" as *two* problems - **aesthetic** slop (the design rules) and **effort** slop (unfinished output) - both fixed by the same move: explicit constraint and a self-check ([[Constraint Beats Coaxing]], [[Design Review as Infrastructure]]). It also lends the framework empirical credibility beyond aesthetics.

## Related

- [[The 13 Skills]] | [[Constraint Beats Coaxing]] | [[Design Review as Infrastructure]]
- Source: [[Canonical Skill File|Canonical SKILL.md]]

## Timeline

- 2026-07-06 - Note created.
