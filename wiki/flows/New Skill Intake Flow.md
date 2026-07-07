---
type: "flow"
title: "New Skill Intake Flow"
status: "developing"
created: "2026-07-07"
updated: "2026-07-07"
tags: ["gogh/ops", "note/flow"]
domain: "ops"
confidence: "evidence-based"
related: ["[[Brain Refresh Flow]]", "[[Claim Verification Flow]]", "[[Agent Skills Format]]", "[[Design Skills Mechanism Map]]", "[[Unified Anti-Slop Rulebook]]", "[[Install Surface and Format Portability]]", "[[Source Manifest Guide]]", "[[Adoption and Metrics]]"]
source_urls: ["https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills (retrieved 2026-07-06)", "https://github.com/Leonxlnx/taste-skill (retrieved 2026-07-07)", "https://github.com/pbakaus/impeccable (retrieved 2026-07-07)", "https://github.com/nextlevelbuilder/ui-ux-pro-max-skill (retrieved 2026-07-07)"]
sources: ["[[Design Theory Sources]]", "[[Source Manifest Guide]]", "[[Canonical Skill File]]", "[[Impeccable Repo and Site]]", "[[UI UX Pro Max Repo]]"]
---
New Skill Intake Flow is the repeatable procedure for turning a design skill capture into source-cited Gogh notes, comparisons, and registry coverage.

## What it is
The flow describes the procedure instantiated by this six-skill build.
The raw manifest records captured files with sha256 values.
The skill registry records skill ids, captures, dials, headings, coverage tags, and source files.
The source ledger records URLs, retrieval dates, refresh due dates, confidence, and claim coverage.
Claim packs record adversarial verdicts for each skill and cross-skill theme.
Wiki notes consume claim packs, raw captures, and source-ledger URLs.
The flow preserves `.raw/` as immutable source material.
The flow keeps source notes separate from skill anchors and rule notes.
The flow updates comparisons when a new skill changes stack conflicts.
The flow updates the Unified Anti-Slop Rulebook when a new ban or detector target is supported.
The flow rebuilds the registry so stack advice has coverage tags.
The flow adds graph tags through frontmatter domain and type tags.

## How it works
1. Pick a stable skill id for `.raw/skills/<id>/`.
2. Capture the upstream SKILL.md and any required support files.
3. Add provenance headers with URL, retrieved date, and license context when captures support it.
4. Record each captured path in `.raw/.manifest.json`.
5. Compute and store sha256 for each captured file.
6. Add source-ledger rows with URL, source_type, retrieved, refresh_due, confidence, and claims.
7. Draft a claim pack that distinguishes primary, official, supporting, market, and practitioner sources.
8. Apply adversarial verification before moving claims into notes.
9. Mark same-author agreement as consistency rather than independent corroboration.
10. Create or update a source note under `wiki/sources/` when the slice owns it.
11. Create or update the skill anchor note.
12. Create rule, audit, flow, entity, reception, comparison, question, gap, or deliverable notes as needed.
13. Update comparison notes when the new skill disagrees with existing rules.
14. Update Unified Anti-Slop Rulebook when the new evidence contains a supported ban.
15. Rebuild `references/skill-registry.json`.
16. Run vault lint.
17. Run audit before making maturity claims.

## Best practice
- Capture raw source files before writing interpretive notes EVIDENCE-BASED
- Store sha256 in `.raw/.manifest.json` for each captured file EVIDENCE-BASED
- Add source-ledger rows before turning claims into durable wiki prose EVIDENCE-BASED
- Separate same-author consistency from independent corroboration EVIDENCE-BASED
- Use claim pack verdicts to assign confidence labels EVIDENCE-BASED
- Create source notes before dependent skill and rule notes when the slice owns them PRACTITIONER
- Update comparisons when a new rule conflicts with existing rules EVIDENCE-BASED
- Update the anti-slop rulebook only from captured evidence EVIDENCE-BASED
- Rebuild the registry after adding a new skill EVIDENCE-BASED
- Preserve graph hygiene with exact domain and note tags EVIDENCE-BASED

## Pitfalls
Writing wiki prose before raw capture can create uncited claims.
Editing raw captures can invalidate sha256 provenance.
Using directory descriptions as rule proof can overstate independent evidence.
Treating same-author docs as second sourcing can inflate confidence.
Adding a source note outside slice ownership can violate parallel authoring rules.
Adding a skill anchor without updating comparisons can hide conflicts.
Adding a ban without updating the unified rulebook can split operator guidance.
Adding registry rows without coverage tags can weaken stack advice.
Calling a scaffolded intake market-ready can violate audit rules.
Ignoring license nuance can create inaccurate install and reuse guidance.

## Sources
- .raw/.manifest.json, read locally 2026-07-07.
- references/source-ledger.json, generated 2026-07-06 and read 2026-07-07.
- references/skill-registry.json, generated 2026-07-07.
- scripts/import_skill_capture.py, read locally 2026-07-07.
- Anthropic Agent Skills article, https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills, retrieved 2026-07-06.
- Claim packs under references/claim-packs, generated 2026-07-07.
- Source Manifest Guide, wiki/sources/Source Manifest Guide.md, read locally 2026-07-07.
- README.md and SKILL.md, read locally 2026-07-07.

## Related
- [[Brain Refresh Flow]] refreshes existing intakes.
- [[Claim Verification Flow]] defines the adversarial verdict step.
- [[Agent Skills Format]] explains SKILL.md progressive disclosure.
- [[Design Skills Mechanism Map]] consumes registry coverage.
- [[Unified Anti-Slop Rulebook]] consumes new ban evidence.
- [[Install Surface and Format Portability]] consumes install evidence.
- [[Source Manifest Guide]] anchors raw provenance expectations.
- [[Adoption and Metrics]] consumes dated stars and installs.
- [[Reception and Criticism]] consumes practitioner and market reactions.
- [[Design Review as Infrastructure]] explains why reusable review artifacts matter.
- [[Open Design Local Collection]] is an unindexed local backlog that can feed this intake flow.

## Next actions
- Use this flow for the next design skill candidate.
- Do not write new source notes unless the slice brief owns them.
- Add open gaps when raw bodies are too large to capture.
- Re-run registry generation after any new capture.
- Re-run lint and audit after intake changes.
