---
type: "experiment"
title: "UIZZE Finish Gate Interoperability Probe"
status: "developing"
created: "2026-07-22"
updated: "2026-07-22"
tags: ["gogh/stack", "note/experiment"]
domain: "stack"
confidence: "evidence-based"
related: ["[[No Cross-Skill Benchmark Data]]", "[[Stack Order Probe]]", "[[Required Audits]]", "[[Design Review as Infrastructure]]"]
source_urls: ["https://raw.githubusercontent.com/uizze/uizze/main/skills/anti-ui-slop/SKILL.md (retrieved 2026-07-22)", "https://uizze.com (retrieved 2026-07-22)"]
sources: []
---
UIZZE Finish Gate Interoperability Probe defines a controlled way to test whether a UIZZE finish-gate pass adds measurable value after a Gogh-advised design stack has produced an interface.

## What it is
- A protocol, not a claim that one workflow is better.
- A companion experiment that leaves Gogh's current six-skill scope unchanged.
- A comparison between a Gogh-advised implementation and the same implementation followed by the free UIZZE finish gate.
- A response to [[No Cross-Skill Benchmark Data]], focused on incremental review value rather than popularity or install counts.
- A test of observable defects: missing states, inert controls, accidental responsive behavior, design-system drift, filler content, and interchangeable layout.

## How it works
1. Freeze one public fixture, product brief, starting commit, coding agent, model, context, viewport set, and time budget.
2. Create three branches from the same commit: control, Gogh stack, and Gogh plus UIZZE finish gate.
3. Leave the control unchanged. Run the chosen Gogh workflow on both treatment branches with the same prompt and tool access.
4. On only the final branch, run the free UIZZE workflow after implementation. Record every reference consulted, design-contract change, blocking finding, and resulting patch.
5. Capture the same screenshots and interaction states from all branches.
6. Run the same repository tests, accessibility checks, and responsive checks on both treatment branches.
7. Have a reviewer who does not know the branch labels score the outputs with the rubric below.
8. Publish raw observations before interpreting the result. Keep failures, null results, and regressions.

## Measurement rubric

| Measure | Recording rule |
| --- | --- |
| Required states | Count brief-required loading, empty, error, disabled, success, and recovery states that can be exercised. |
| Primary flow | Record whether every visible control in the main task has a clear and working outcome. |
| Responsive behavior | Test the same named viewport widths and record overflow, collapse, reordering, and touch-target failures. |
| Product specificity | Ask whether the layout could fit an unrelated product after changing only labels, then record the evidence behind the verdict. |
| Design-system fit | Count new tokens or components that duplicate an established project primitive without a documented reason. |
| Verification cost | Record elapsed review time, agent tokens when available, commands run, and patch size. |
| Regression risk | Record test failures and behavior lost while addressing finish-gate findings. |

## Interpretation gate
- The experiment is complete only when prompts, commits, screenshots, commands, findings, and rubric scores are preserved for all conditions.
- Incremental evidence exists when the final pass identifies and fixes a reproducible blocker missed by the Gogh-only branch without introducing a regression.
- No difference is a valid result. Record it without adding a promotional conclusion.
- A larger or slower patch is not automatically better. Review cost and regressions remain part of the result.
- One fixture cannot establish a general ranking. Repeat across at least one product UI and one brand or landing-page UI before changing stack advice.

## Best practice
- Use a fixture whose required states and primary task are explicit before the run. EVIDENCE-BASED
- Keep branch conditions identical until the finish-gate step. EVIDENCE-BASED
- Preserve the exact UIZZE skill revision used in the run. EVIDENCE-BASED
- Blind the final reviewer to branch labels. PRACTITIONER
- Treat catalogue references as evidence inputs, not layouts to copy. EVIDENCE-BASED
- Keep UIZZE outside the core stack unless a separate sourced intake changes Gogh's product boundary. EVIDENCE-BASED

## Pitfalls
- Using different prompts, models, or time budgets makes the comparison uninterpretable.
- Selecting only a favorable screenshot hides interaction and state regressions.
- Counting subjective preference without recording observable evidence turns the probe into a testimonial.
- Letting the finish-gate branch rewrite product identity confounds review with redesign.
- Treating one successful run as a universal ranking overstates the evidence.

## Sources
- UIZZE anti-ui-slop skill, raw canonical file, retrieved 2026-07-22.
- UIZZE public catalogue, retrieved 2026-07-22.
- [[No Cross-Skill Benchmark Data]] records the unresolved benchmark gap this probe addresses.
- [[Stack Order Probe]] supplies the existing controlled-comparison precedent.

## Related
- [[No Cross-Skill Benchmark Data]] defines the unresolved evidence gap.
- [[Stack Order Probe]] tests order within the current stack.
- [[Required Audits]] routes the existing blocking reviews.
- [[Design Review as Infrastructure]] explains why a reusable finish gate may be tested separately from generation.

## Next actions
- Choose one permissively licensed fixture with explicit UI states.
- Freeze the prompt, model, commit, viewport set, and scoring sheet before running.
- Store the observations as dated evidence instead of editing this protocol into a result.
- Update the benchmark gap only after at least one complete run.