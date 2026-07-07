---
type: "note"
title: "Open Questions"
created: "2026-07-06"
updated: "2026-07-06"
status: "active"
confidence: "CONTESTED"
---

# Open Questions

Confidence tag: CONTESTED (these are the deliberately-unsettled items).

## Compiled Truth

1. **Section 14 item count.** Is it really "60 items"? The vendor never states a count; [[neodrop.ai - v2 deep dive|neodrop]] does. Resolve on a v2.0.0 stable release. -> [[Pre-Flight Check (Section 14)]]
2. **[[Leon Lin]]'s age.** "16-year-old from Munich" is widely repeated but not primary-verified. Munich is confirmed; the age is not.
3. **The premise: can taste be installed?** Genuinely contested (Mark Chen, designative.info vs the moat thesis). The brain's working answer: the skill **raises the floor**, it does not manufacture top-tier taste. -> [[Taste as the Moat]], [[Reception and Criticism]]
4. **§12 Block Library.** The contract is defined but the `blocks/` directory is not yet populated in the repo. Watch for it to land.
5. **v2 -> v2.0.0 stability.** Install name and dial baseline (8/6/4) are expected to lock at stable; both could change before then. -> [[Taste Skill Changelog]]
6. **Framework-agnostic in practice.** The claim vs the React/Next-heavy examples is unresolved; no strong evidence of production Vue/Svelte/Astro use. -> [[Architecture and Stack]]
7. **X/Twitter blog threads.** The four `@LexnLin` blog posts return HTTP 402 to automated fetching, so their full text is uncaptured - a manual read would fill this gap. -> [[Taste Skill Official Site]]
8. **No verification layer.** The audits are self-reported; there is no tests / visual-regression proof the rules were followed. An external checker (a lint that greps for banned hex, em-dashes, `h-screen`, scroll listeners) would be a natural extension. -> [[Design Review as Infrastructure]]

## Related

- [[Hot]] | [[Source Manifest Guide]] | [[Dashboard]]

## Timeline

- 2026-07-06 - Note created.
