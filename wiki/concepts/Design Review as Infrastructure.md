---
type: "concept"
title: "Design Review as Infrastructure"
created: "2026-07-06"
updated: "2026-07-06"
status: "active"
confidence: "EVIDENCE-BASED"
---

# Design Review as Infrastructure

Confidence tag: EVIDENCE-BASED.

## Compiled Truth

Instead of relying on a human to catch slop after the fact, encode design judgment as **rules the agent runs on itself** - pre-flight checks, forbidden-pattern audits, and a redesign/audit protocol. This is the thesis Developers Digest named: quality control moves **left**, from post-hoc human review to codified, machine-enforced review that runs *before* the agent declares a task done.

- *"A taste skill is a review checklist, a style contract, and a calibration artifact that the agent must route through before it claims the work is done."*
- *"The future of agent quality is not just better generation. It is better review, moved earlier, written down, and reused."*
- *"The winning developer agent stack will not be one model plus one chat box. It will be a set of portable controls around model behavior."*

Taste Skill's concrete instances of this are the [[Pre-Flight Check (Section 14)]] and the [[Required Audits]].

## Three converging traditions

1. **Design linting / design-as-code.** Linting is automated rule-checking; design linters (e.g. `@lapidist/design-lint`, Figma's Design System Linter) flag raw values against token constraints. A Taste Skill audit is a lint pass whose rules are *aesthetic* ("no centered hero at high variance," "no `h-screen`," "no emoji bullets") rather than syntactic - inheriting linting's apparatus of rules, violations, and waivers-with-rationale.
2. **Design systems as code / tokens as single source of truth.** Once decisions are tokens, conformance is checkable. Taste Skill leans on this with [[The Three Locks]] (color, shape, theme) so consistency is *verifiable*, not vibes.
3. **Eval-driven generation & LLM/Agent-as-Judge.** The research frontier (LLM-as-a-Judge; Agent-as-a-Judge, which "observes intermediate steps... and reasons over the agent's action log"; the WebDevJudge benchmark) treats UI quality as an eval. A pre-flight check is a lightweight, *in-loop* instance: the same model that generated the UI judges it against an explicit rubric before finishing.

## Why it matters

Generation without a check-back reverts to the mean ([[AI Slop]]). Encoding taste as a machine-checkable pass/fail gate turns "good design" from an unverifiable aspiration into a gate the agent enforces on itself, at zero marginal human cost and infinite scale - the same reason CI linting beat manual style review.

**Live critique (kept):** critics note Taste Skill's audits are *self-reported* - there is "no automated tests or visual regression" proving the rules were actually followed ([[Reception and Criticism]]). The gate is only as honest as the agent running it.

## Related

- [[Pre-Flight Check (Section 14)]] | [[Required Audits]] | [[The Three Locks]] | [[Constraint Beats Coaxing]]
- Source: [[Developers Digest - Taste Skills as Infrastructure]], [[Design Theory Sources]]

## Timeline

- 2026-07-06 - Note created.
