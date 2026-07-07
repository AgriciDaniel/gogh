# Current Requirements

Status: researched. Facts captured 2026-07-06 from primary and official sources. Refresh on any upstream release.

## Refresh Cadence

on-changelog for github.com/Leonxlnx/taste-skill and tasteskill.dev/changelog; monthly for the SKILL.md rules and the three dials; quarterly for ecosystem coverage (Emil Kowalski, Developers Digest, skill directories) and the Anthropic Agent Skills / SKILL.md format.

## Required Source Standard

Use official, primary, vendor, standards-body, or API documentation first. Record URL, retrieval date, version, deprecation notes, and confidence. Mark anything unverified. Full ledger: `references/source-ledger.json`. Raw captures: `.raw/research/`.

## Current facts (verified 2026-07-06)

| Fact | Value | Source | Retrieved | Confidence |
|---|---|---|---|---|
| Version | v2 (experimental), pre-release toward v2.0.0 stable | tasteskill.dev/changelog; repo CHANGELOG.md | 2026-07-06 | high |
| Install name | design-taste-frontend | canonical SKILL.md frontmatter | 2026-07-06 | high |
| Dial baseline | DESIGN_VARIANCE 8 / MOTION_INTENSITY 6 / VISUAL_DENSITY 4, each 1-10 | canonical SKILL.md section 1 | 2026-07-06 | high |
| License | MIT (c) 2026 | github.com/Leonxlnx/taste-skill LICENSE | 2026-07-06 | high |
| Stars | ~58,435 | GitHub API repos/Leonxlnx/taste-skill | 2026-07-06 | high |
| Created | 2026-02-19 | GitHub API | 2026-07-06 | high |
| Skills in suite | 13 | repo skill.sh and skills/llms.txt | 2026-07-06 | high |
| Scope | landing pages, portfolios, redesigns (not dashboards or data tables) | canonical SKILL.md scope and section 13 | 2026-07-06 | high |
| Em-dash rule | zero em-dashes or en-dashes anywhere visible | canonical SKILL.md section 9.G | 2026-07-06 | high |
| Hero rule | headline max 2 lines, subtext max 20 words, CTA no-scroll, pt-24 cap, max 4 text elements | canonical SKILL.md section 4.7 | 2026-07-06 | high |
| Nav rule | single line at desktop, height cap 80px | canonical SKILL.md section 4.7 | 2026-07-06 | high |
| Layout families | at least 4 different families across an 8-section page | canonical SKILL.md section 4.7 | 2026-07-06 | high |
| Pre-flight | Section 14, every box Pass or Fail; any Fail blocks completion | canonical SKILL.md section 14; tasteskill.dev/guide | 2026-07-06 | high |
| Install command | npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend" | tasteskill.dev/docs | 2026-07-06 | high |

## Known unverified or drifting items

- The "60-item" count for Section 14 is a third-party (neodrop.ai) characterization, not stated by the vendor.
- The install name and dial baseline are expected to lock at the v2.0.0 stable release and could change before then.
- Section 12 Block Library is a defined contract, but the `blocks/` directory is not yet populated in the repo.

See `wiki/gaps/Open Questions.md` for the full open-question list.
