---
type: "flow"
title: "Claim Verification Flow"
status: "developing"
created: "2026-07-07"
updated: "2026-07-07"
tags: ["gogh/ops", "note/flow"]
domain: "ops"
confidence: "evidence-based"
related: ["[[Brain Refresh Flow]]", "[[New Skill Intake Flow]]", "[[Reception and Criticism]]", "[[Adoption and Metrics]]", "[[Font Ban Conflicts]]", "[[Unified Anti-Slop Rulebook]]", "[[wiki/gaps/_index|Installs Figure Basis]]", "[[UI UX Pro Max Repo]]"]
source_urls: ["https://composio.dev/content/top-design-skills (retrieved 2026-07-07)", "https://paddo.dev/blog/impeccable-design-vocabulary/ (retrieved 2026-07-07)", "https://snyk.io/articles/top-claude-skills-ui-ux-engineers/ (retrieved 2026-07-07)", "https://github.com/nextlevelbuilder/ui-ux-pro-max-skill (retrieved 2026-07-07)", "https://github.com/wilwaldon/Claude-Code-Frontend-Design-Toolkit (retrieved 2026-07-07)"]
sources: ["[[Reception Sources]]", "[[UI UX Pro Max Repo]]", "[[Anthropic Frontend Design Skill and Post]]", "[[Source Manifest Guide]]"]
---
Claim Verification Flow is the adversarial second-sourcing procedure that keeps Gogh from turning stale or misattributed claims into facts.

## What it is
The flow uses claim pack verdicts rather than prose confidence alone.
The verdict vocabulary includes CONFIRMED.
The verdict vocabulary includes CONFIRMED-AS-REPORTED.
The verdict vocabulary includes CONTESTED.
The verdict vocabulary includes SINGLE-SOURCE.
The flow treats same-author agreement as consistency, not independent corroboration.
The flow keeps exact counts as dated observations.
The flow allows practitioner claims but labels them practitioner.
The flow demotes claims when the second source conflicts or fails.
The flow keeps both accounts visible when a claim is contested.
The flow uses contradiction callouts when two source accounts matter to operators.
The flow was used across all eight claim packs generated on 2026-07-07.

## How it works
1. Extract the candidate claim from a raw capture, ledger row, or source note.
2. Identify the primary or official source.
3. Identify whether any second source is independent.
4. Reject same-author pages as independent corroboration.
5. Check date, count, version, license, and install basis.
6. Assign CONFIRMED when primary and independent source align.
7. Assign CONFIRMED-AS-REPORTED when the source reports the claim but the basis is internal or not auditable.
8. Assign CONTESTED when current and older sources conflict or attribution is wrong.
9. Assign SINGLE-SOURCE when only one source supports the claim.
10. Write the confidence marker into the wiki note.
11. Add contradiction or stale callouts where useful.
12. Re-check current primary sources before calling a stale third-party number current.
13. Date every metric.
14. Avoid averaging conflicting counts.
15. Preserve the dropped or demoted claim in Next actions only if it still needs follow-up.

## Best practice
- Treat same-author consistency as weaker than independent corroboration EVIDENCE-BASED
- Use CONFIRMED only when the evidence path supports it EVIDENCE-BASED
- Use CONFIRMED-AS-REPORTED for registry counters and practitioner-reported numbers EVIDENCE-BASED
- Use CONTESTED when sources disagree or attribution fails EVIDENCE-BASED
- Use SINGLE-SOURCE when only one evidence source supports the claim EVIDENCE-BASED
- Keep stale counts visible only with dates and stale context EVIDENCE-BASED
- Use contradiction callouts for operator-relevant disagreements EVIDENCE-BASED
- Do not treat directory descriptions as independent rule-content proof EVIDENCE-BASED
- Re-check source-ledger rows before writing durable facts EVIDENCE-BASED
- Prefer primary captures over market listicles for rule content EVIDENCE-BASED

## Pitfalls
Misattributing the 277,000+ Anthropic install figure to Snyk repeats a verified correction error.
The Anthropic claim pack says direct Snyk fetches on 2026-07-07 found no install counts.
The Anthropic claim pack says Composio and paddo.dev repeat 277,000+ with unclear basis.
The Anthropic claim pack says skills.sh showed 634.0K installs on 2026-07-07.
Treating the 277,000+ number as current would ignore the 2026-07-07 skills.sh observation.
Treating UI UX Pro Max's 97 palettes as current would ignore the README's 161 palettes on 2026-07-07.
Treating UI UX Pro Max's 50 styles as current would ignore the README's 67 styles on 2026-07-07.
Treating wilwaldon's larger UI UX Pro Max counts as current repo facts would exceed verification.
Treating Impeccable's May 27-rule snapshot as current would ignore the 45-rule July release.
Treating Vercel's exact rule count as stable would ignore local count variation.

> [!contradiction]
> Worked example: the 277,000+ frontend-design install figure is confirmed as reported by Composio and paddo.dev, but the common Snyk attribution is unsupported by direct 2026-07-07 fetches.

> [!stale]
> Worked example: UI UX Pro Max market snapshots with 97 palettes and 50 styles are stale against the 2026-07-07 README counts of 161 palettes and 67 styles.

## Sources
- Claim pack Anthropic frontend-design, references/claim-packs/claim-pack-anthropic-frontend-design.md, generated 2026-07-07.
- Claim pack UI UX Pro Max, references/claim-packs/claim-pack-ui-ux-pro-max.md, generated 2026-07-07.
- Claim pack ecosystem, references/claim-packs/claim-pack-ecosystem.md, generated 2026-07-07.
- Composio, https://composio.dev/content/top-design-skills, retrieved 2026-07-07.
- paddo.dev, https://paddo.dev/blog/impeccable-design-vocabulary/, retrieved 2026-07-07.
- Snyk, https://snyk.io/articles/top-claude-skills-ui-ux-engineers/, retrieved 2026-07-07.
- UI UX Pro Max README, https://github.com/nextlevelbuilder/ui-ux-pro-max-skill, retrieved 2026-07-07.
- Local source ledger, references/source-ledger.json, generated 2026-07-06.

## Related
- [[Brain Refresh Flow]] runs this process during refresh.
- [[New Skill Intake Flow]] runs this process during intake.
- [[Reception and Criticism]] consumes contested reception claims.
- [[Adoption and Metrics]] consumes dated counts.
- [[Font Ban Conflicts]] is a rule-conflict use case.
- [[Unified Anti-Slop Rulebook]] uses confidence labels per row.
- [[wiki/gaps/_index|Installs Figure Basis]] is the follow-up for registry counters.
- [[UI UX Pro Max Repo]] records the stale-stars and stale-count context.
- [[Anthropic Frontend Design Skill]] records the install-count correction.
- [[Source Manifest Guide]] records provenance expectations.

## Next actions
- Use this flow before adding any new metric to a note.
- Keep the installs-figure correction visible until a better source appears.
- Keep UI UX Pro Max stale snapshot rows dated.
- Add new contradiction callouts when source accounts conflict.
- Do not upgrade single-source claims without a new independent source.
