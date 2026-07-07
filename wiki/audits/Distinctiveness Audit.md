---
type: "audit"
title: "Distinctiveness Audit"
status: "developing"
created: "2026-07-07"
updated: "2026-07-07"
tags: ["gogh/stack", "note/audit"]
domain: "stack"
confidence: "practitioner"
related: ["[[Aesthetic Direction Commitment]]", "[[Unified Pre-Flight Mega-Checklist]]", "[[Pre-Flight Check (Section 14)]]", "[[Full Stack Build Flow]]", "[[DESIGN_VARIANCE]]", "[[AI Tells (Forbidden Patterns)]]", "[[Distributional Convergence]]", "[[Enforcement Layer Overlap]]"]
source_urls: ["https://raw.githubusercontent.com/Leonxlnx/taste-skill/main/skills/taste-skill/SKILL.md (retrieved 2026-07-07)", "https://raw.githubusercontent.com/anthropics/skills/main/skills/frontend-design/SKILL.md (retrieved 2026-07-07)", "https://raw.githubusercontent.com/nextlevelbuilder/ui-ux-pro-max-skill/main/.claude/skills/ui-ux-pro-max/data/styles.csv (retrieved 2026-07-07)"]
sources: ["[[Canonical Skill File]]", "[[Anthropic Frontend Design Skill and Post]]", "[[UI UX Pro Max Repo]]"]
---

The Distinctiveness Audit is the boring gate: it fails work that passes every
ban and checklist but would not be remembered five seconds after closing the
tab.

## What it is

- A blocking exit audit that runs after the anti-slop and craft gates.
- It tests the positive space that the other audits cannot see: direction,
  signature, memorability.
- Six questions, each answered in writing, any hard failure blocks shipping.
- Born from a measured failure: the claude-ads landing run of 2026-07-07
  passed the Impeccable detector with zero findings, passed the dash sweep,
  passed the craft checks, and the operator scored it 3 out of 10 with the
  verdict "exact same style, exact same website, nothing special".
- The existing gates are necessary and not sufficient:
  [[Pre-Flight Check (Section 14)]] and the detector catch slop; nothing caught sameness.
- This audit is intentionally uncomfortable: it asks for evidence of a
  decision, not evidence of compliance.

## How it works

The six questions, answered honestly and in writing:

- One: what is the named direction, and where was it committed before the
  build started? No written commitment means automatic fail; go to
  [[Aesthetic Direction Commitment]].
- Two: the five-second test. Cover the logo. Describe what a first-time
  visitor remembers after five seconds. If the answer describes a category
  ("a dark SaaS page") instead of this page, fail.
- Three: the screenshot test. Name the single element a visitor might
  screenshot or describe to a colleague. No candidate, fail.
- Four: the incumbent test, for redesigns. Put the old page beside the new
  one. If the honest description of the change is "the same design, tidied",
  fail against a transform brief; pass only against a refresh brief.
- Five: the template test. Could this exact layout ship for a competitor by
  swapping copy and logo? If yes, the page has no signature element, fail.
- Six: the variance receipt. Which DESIGN_VARIANCE level was set, and do the
  layout choices show it? Variance 8 with uniform centered sections is a
  contradiction, fail.

Scoring: two written passes are required from different reviewers when the
work is client-facing; self-review is acceptable for internal work. Record
the answers in the build plan next to the direction commitment.

## Best practice

- Run this audit only after the mechanical gates pass; it assumes a clean
  floor. EVIDENCE-BASED
- Answer in writing; verbal passes rot into compliance theater. PRACTITIONER
- For transform briefs, require the incumbent test with side-by-side
  screenshots. PRACTITIONER
- Treat a fail as a direction problem, never a polish problem; more craft on
  an uncommitted design deepens the sameness. PRACTITIONER
- Keep the six answers with the shipped work as the taste record for the
  next brief. PRACTITIONER
- Calibrate against the style database: if the page matches no named style
  and no deliberate hybrid, it probably regressed to the mean.
  EVIDENCE-BASED

## Pitfalls

- Passing the audit by argument instead of by page: if the answer needs three
  sentences of justification, the page failed.
- Confusing loudness with distinctiveness; a signature element can be quiet
  (one typographic move) and still own the page.
- Running the audit before the craft gates and blaming direction for what is
  actually sloppy execution.
- Letting the audit inflate variance on refresh briefs where the operator
  asked for continuity; ambition classification comes first.
- Reviewer sameness: the second reviewer must not be the person who wrote the
  direction commitment when the stakes are high.
- Treating one strong hero as distinctiveness while every section below it is
  a template; question five applies per page, not per hero.

## Sources

- Operator retrospective, claude-ads landing run 1, score 3/10 with verdict
  recorded, 2026-07-07. Practitioner evidence, single source.
- taste-skill v2 SKILL.md, variance dial and layout-family rules, capture
  .raw/skills/taste-skill-v2/SKILL.md, retrieved 2026-07-07.
- Anthropic frontend-design SKILL.md, committed direction requirement,
  capture .raw/skills/anthropic-frontend-design/SKILL.md, retrieved
  2026-07-07.
- ui-ux-pro-max styles database, named styles as calibration vocabulary,
  capture .raw/skills/ui-ux-pro-max/styles.csv, retrieved 2026-07-07.

## Related

- [[Aesthetic Direction Commitment]] - the entry gate this audit enforces.
- [[Unified Pre-Flight Mega-Checklist]] - this audit is its final section.
- [[Pre-Flight Check (Section 14)]] - the slop floor that runs before this.
- [[AI Tells (Forbidden Patterns)]] - negative-space companion list.
- [[Full Stack Build Flow]] - where this gate sits in the build order.
- [[DESIGN_VARIANCE]] - the dial question six checks receipts for.
- [[Distributional Convergence]] - the theory of why sameness happens.
- [[Enforcement Layer Overlap]] - where each gate runs in the pipeline.

## Next actions

- Apply to the claude-ads landing rerun and file the before and after
  answers.
- Collect three more operator scores to move this note past single-source
  practitioner evidence.
