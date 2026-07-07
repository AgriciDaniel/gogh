---
type: "flow"
title: "Audit Pipeline Flow"
status: "developing"
created: "2026-07-07"
updated: "2026-07-07"
tags: ["gogh/stack", "note/flow"]
domain: "stack"
confidence: "evidence-based"
related: ["[[Enforcement Layer Overlap]]", "[[Pre-Flight Check (Section 14)]]", "[[Impeccable Audit and Detect]]", "[[MIFB Review Checklist]]", "[[Required Audits]]", "[[Unified Pre-Flight Mega-Checklist]]", "[[Full Stack Build Flow]]", "[[Design Review as Infrastructure]]"]
source_urls: ["https://raw.githubusercontent.com/Leonxlnx/taste-skill/main/skills/taste-skill/SKILL.md (retrieved 2026-07-07)", "https://github.com/pbakaus/impeccable (retrieved 2026-07-07)", "https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md (retrieved 2026-07-07)", "https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/skills/make-interfaces-feel-better/SKILL.md (retrieved 2026-07-07)"]
sources: ["[[Canonical Skill File]]", "[[Impeccable Repo and Site]]", "[[MIFB Repo and Skill File]]", "[[Reception Sources]]"]
---
Audit Pipeline Flow orders the stack checks so deterministic gates run before advisory craft review.

## What it is
The pipeline is CI-ready where the underlying tools are installed.
Taste Skill Section 14 is a blocking pre-flight for Taste Skill builds.
Impeccable detect is deterministic and runs without an LLM or API keys.
Impeccable detect has 45 deterministic rules as of 2026-07-07.
The Impeccable repo extract says detector output includes build-readable exit codes.
The Impeccable repo extract gives a site example where three anti-patterns exit 1.
Vercel web-design-guidelines reports file:line findings.
MIFB review produces Before and After tables grouped by principle.
MIFB is advisory in the captured evidence because no blocking release gate is defined.
The flow separates merge gates from improvement advice.
The flow keeps Impeccable findings attributed to Impeccable.
The flow does not mutate code by itself.

## How it works
1. Confirm the build used Taste Skill before requiring Taste Skill Section 14.
2. Run Section 14 pre-flight and block completion on any failed box.
3. Run `npx impeccable detect` or the bundled detector path when Impeccable is installed.
4. Treat detector findings as a merge gate when project policy enables the gate.
5. Use JSON output for CI when the Impeccable CLI is used.
6. Record detector waivers through Impeccable ignore mechanisms, not in Gogh prose alone.
7. Run Vercel web-design-guidelines on the changed files or route pattern.
8. Treat Vercel file:line findings as required fixes for accessibility, forms, motion, image, performance, and state issues.
9. Run MIFB review for tactile, motion, typography, surface, and performance polish.
10. Treat MIFB rows as advisory unless the project explicitly promotes them to gate status.
11. Re-run deterministic gates after fixes.
12. Re-run Vercel when file:line findings touched accessibility, forms, images, or motion.
13. Update the review report with remaining advisory items.
14. If a gate conflicts with brand evidence, route the conflict to the design contract or comparison note.
15. Do not call the audit passed if a configured gate was not run.

## Best practice
- Run Section 14 when Taste Skill directed the build EVIDENCE-BASED
- Run Impeccable detect before subjective review when installed EVIDENCE-BASED
- Use Impeccable JSON output for CI-friendly detector reporting EVIDENCE-BASED
- Treat Vercel file:line findings as high-signal review output EVIDENCE-BASED
- Use MIFB after gates for detail polish EVIDENCE-BASED
- Keep MIFB advisory unless a project contract makes it blocking PRACTITIONER
- Keep detector waivers inside Impeccable ignore mechanisms EVIDENCE-BASED
- Attribute exit-code behavior to Impeccable source evidence only EVIDENCE-BASED
- Re-run gates after fixes that touch UI files PRACTITIONER
- Keep audit results source-cited in the final report EVIDENCE-BASED

## Pitfalls
Running MIFB before deterministic gates can waste polish work on failing surfaces.
Skipping Section 14 after a Taste Skill build violates the source rule.
Using an old Impeccable detector count can make CI docs stale.
Assuming every Impeccable finding exits the same way without current CLI evidence can overstate exit behavior.
Treating Vercel's fetched rules as fixed after install can miss runtime changes.
Treating Vercel as a style generator misuses the audit skill.
Treating MIFB checklist output as a no-LLM detector overstates the source.
Treating waivers as chat-only decisions can make gates fail again later.
Treating a clean detector run as proof of visual excellence can miss taste issues.
Treating unrun checks as passed violates the brain operating rules.

## Sources
- Taste Skill SKILL.md, https://raw.githubusercontent.com/Leonxlnx/taste-skill/main/skills/taste-skill/SKILL.md, retrieved 2026-07-07.
- Impeccable README, https://github.com/pbakaus/impeccable, retrieved 2026-07-07.
- Impeccable repo extract, .raw/research/impeccable-repo-extract.md, captured 2026-07-07.
- Vercel command.md, https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md, retrieved 2026-07-07.
- MIFB SKILL.md, https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/skills/make-interfaces-feel-better/SKILL.md, retrieved 2026-07-07.
- Claim pack Impeccable, references/claim-packs/claim-pack-impeccable.md, generated 2026-07-07.
- Claim pack Vercel, references/claim-packs/claim-pack-vercel-web-design-guidelines.md, generated 2026-07-07.
- Claim pack MIFB, references/claim-packs/claim-pack-make-interfaces-feel-better.md, generated 2026-07-07.

## Related
- [[Enforcement Layer Overlap]] explains the dedupe matrix.
- [[Pre-Flight Check (Section 14)]] is the Taste Skill gate.
- [[Impeccable Audit and Detect]] is the Impeccable audit note.
- [[MIFB Review Checklist]] is the advisory craft review.
- [[Required Audits]] is the existing audit reference.
- [[Unified Pre-Flight Mega-Checklist]] merges these checks into a deliverable.
- [[Full Stack Build Flow]] shows where audit follows implementation.
- [[Design Review as Infrastructure]] explains the broader review thesis.
- [[Deterministic Design Detection]] covers no-LLM detection.
- [[Gogh Quickstart]] gives first-run operator steps.

## Next actions
- Re-check Impeccable CLI docs before documenting exact exit-code policy beyond the captured example.
- Keep Vercel command.md refreshed before CI rollout.
- Use this flow to update the mega-checklist.
- Keep MIFB advisory status visible until a source defines a hard gate.
- Do not mark market-ready without the project audit command passing.

