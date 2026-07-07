---
type: "flow"
title: "Brain Refresh Flow"
status: "developing"
created: "2026-07-07"
updated: "2026-07-07"
tags: ["gogh/ops", "note/flow"]
domain: "ops"
confidence: "evidence-based"
related: ["[[Claim Verification Flow]]", "[[New Skill Intake Flow]]", "[[Design Skills Mechanism Map]]", "[[Taste Skill Changelog]]", "[[Adoption and Metrics]]", "[[Reception and Criticism]]", "[[Required Audits]]", "[[Source Manifest Guide]]"]
source_urls: ["https://github.com/pbakaus/impeccable/releases (retrieved 2026-07-07)", "https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/releases (retrieved 2026-07-07)", "https://github.com/Leonxlnx/taste-skill (retrieved 2026-07-07)", "https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md (retrieved 2026-07-07)"]
sources: ["[[Impeccable Repo and Site]]", "[[UI UX Pro Max Repo]]", "[[Canonical Skill File]]", "[[Reception Sources]]", "[[Source Manifest Guide]]"]
---
Brain Refresh Flow keeps Gogh current by following refresh_due, re-verifying fast-moving counts, and demoting stale claims instead of silently preserving them.

## What it is
The source ledger was generated on 2026-07-06.
Most six-skill captures in the ledger were retrieved on 2026-07-07.
The skill registry was generated on 2026-07-07.
The claim packs were generated on 2026-07-07.
The README says the metamorphosis wave is moving the repo toward market-ready.
The README also says the repo is not market-ready until adapters, demo verification, audit, and release gates pass.
The adapter manifest declares domain-adapted status in the local file read on 2026-07-07.
The product boundaries still say the repo is currently researched.
This status tension should be resolved by running the audit, not by editing prose alone.
Impeccable and UI UX Pro Max are the fastest movers in the July 2026 evidence.
Impeccable detector counts changed from 27 in May snapshots to 45 on 2026-07-01.
UI UX Pro Max moved to v2.10.2 on 2026-07-06 after eight releases between 2026-06-24 and 2026-07-06.

## How it works
1. Read `references/source-ledger.json`.
2. Sort sources by `refresh_due`.
3. Re-fetch official, primary, or repo sources before supporting sources.
4. Re-verify stars, installs, versions, rule counts, and database counts as dated observations.
5. Re-capture raw files under `.raw/skills/<id>/` or `.raw/research/` with provenance headers.
6. Update `.raw/.manifest.json` with sha256 values for changed captures.
7. Update source-ledger rows with retrieved, refresh_due, confidence, and claim coverage.
8. Regenerate or update claim packs with adversarial verdicts.
9. Mark changed or unsupported claims CONTESTED, SINGLE-SOURCE, or stale in notes.
10. Add `> [!stale]` callouts where an old count remains for historical context.
11. Update source notes before dependent concept, rule, flow, and deliverable notes.
12. Update `wiki/hot.md` and `wiki/log.md` only in a slice that owns those files.
13. Rebuild the skill registry.
14. Run vault lint.
15. Run `python scripts/audit_brain.py --json`.
16. Run release packaging only after the requested release gate is appropriate.

## Best practice
- Use `refresh_due` as the first refresh queue EVIDENCE-BASED
- Date every repeated star, install, version, detector, and database count EVIDENCE-BASED
- Refresh Impeccable releases before repeating detector counts EVIDENCE-BASED
- Refresh UI UX Pro Max README and releases before repeating database counts EVIDENCE-BASED
- Treat Vercel command.md as runtime-moving audit content EVIDENCE-BASED
- Demote unsupported claims instead of preserving stale prose PRACTITIONER
- Preserve `.raw/` as immutable source material and write new captures rather than editing old captures EVIDENCE-BASED
- Update source-ledger evidence before updating dependent wiki claims EVIDENCE-BASED
- Run lint and audit before calling the brain market-ready EVIDENCE-BASED
- Do not edit hot or log from a slice that does not own them EVIDENCE-BASED

## Pitfalls
Refreshing wiki prose without source-ledger rows fails the research gate.
Refreshing stars without dates violates the metric rule.
Refreshing UI UX Pro Max from old Snyk counts would reintroduce stale figures.
Refreshing Impeccable from May listicles would miss rule 45.
Refreshing Vercel by reinstalling the wrapper can miss the runtime command.md behavior.
Editing `.raw/` source bodies breaks provenance.
Updating hot and log from the wrong slice violates the shared authoring spec.
Calling researched or domain-adapted status market-ready would violate the audit rule.
Ignoring status tension between README and adapter manifest can confuse operators.
Skipping audit after source changes can hide maturity regressions.

> [!stale]
> Baseline dates are 2026-07-06 for the original source ledger and 2026-07-07 for the six-skill claim packs, registry, and most raw captures.

## Sources
- README.md, read locally 2026-07-07.
- references/source-ledger.json, generated 2026-07-06 and read 2026-07-07.
- references/adapter-manifest.json, read 2026-07-07.
- references/skill-registry.json, generated 2026-07-07.
- Claim packs under references/claim-packs, generated 2026-07-07.
- Impeccable releases, https://github.com/pbakaus/impeccable/releases, retrieved 2026-07-07.
- UI UX Pro Max releases, https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/releases, retrieved 2026-07-07.
- Vercel command.md, https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md, retrieved 2026-07-07.

## Related
- [[Claim Verification Flow]] defines verdict handling after refresh.
- [[New Skill Intake Flow]] defines how a new source enters the brain.
- [[Design Skills Mechanism Map]] is the first dependent stack anchor.
- [[Taste Skill Changelog]] is the existing release-watch note for Taste Skill.
- [[Adoption and Metrics]] is where refreshed counts roll up.
- [[Reception and Criticism]] is where changed market evidence rolls up.
- [[Required Audits]] anchors the release audit layer.
- [[Source Manifest Guide]] records provenance expectations.
- [[wiki/gaps/_index|Installs Figure Basis]] is where registry-count caveats belong.
- [[wiki/gaps/_index|No Cross-Skill Benchmark Data]] is where missing benchmark evidence belongs.

## Next actions
- Run this flow before any market-ready release attempt.
- Prioritize Impeccable and UI UX Pro Max on the next refresh cycle.
- Resolve the researched versus domain-adapted status tension through audit output.
- Keep stale callouts in place until source-ledger evidence is refreshed.
- Do not edit hot or log from this S5g slice.
