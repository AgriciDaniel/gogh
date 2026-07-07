---
type: "skill"
title: "UI UX Pro Max (Skill)"
status: "developing"
created: "2026-07-07"
updated: "2026-07-07"
tags: ["gogh/ui-ux-pro-max", "note/skill"]
domain: "ui-ux-pro-max"
confidence: "contested"
related: ["[[Retrieval Database Skills]]", "[[UX Rules Database (99 Rules)]]", "[[Design System Generation Flow]]", "[[Agent Skills Format]]", "[[Deterministic Design Detection]]", "[[Install and Load]]", "[[Impeccable (Toolchain)]]", "[[Taste Skill (Project)]]"]
source_urls: ["https://github.com/nextlevelbuilder/ui-ux-pro-max-skill (retrieved 2026-07-07)", "https://raw.githubusercontent.com/nextlevelbuilder/ui-ux-pro-max-skill/main/README.md (retrieved 2026-07-07)", "https://raw.githubusercontent.com/nextlevelbuilder/ui-ux-pro-max-skill/main/.claude/skills/ui-ux-pro-max/SKILL.md (retrieved 2026-07-07)", "https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/releases (retrieved 2026-07-07)", "https://api.github.com/repos/nextlevelbuilder/ui-ux-pro-max-skill (retrieved 2026-07-07)", "https://snyk.io/articles/top-claude-skills-ui-ux-engineers/ (retrieved 2026-07-07)", "https://github.com/wilwaldon/Claude-Code-Frontend-Design-Toolkit (retrieved 2026-07-07)", "https://lobehub.com/skills/terminalskills-skills-ui-ux-pro-max (retrieved 2026-07-07)"]
sources: ["[[UI UX Pro Max Repo]]", "[[Reception Sources]]"]
---
UI UX Pro Max is the retrieval database skill in the Gogh stack, using searchable CSV data and BM25 ranking for style, palette, typography, UX, chart, and stack guidance.

## What it is
UI UX Pro Max is published by the GitHub org handle NextLevelBuilder as `nextlevelbuilder/ui-ux-pro-max-skill`.
The assigned claim pack records no named individual maintainer in the reviewed repo or directory listings as of 2026-07-07.
The source ledger records the repository homepage as `www.uupm.cc`.
The claim pack records the repository creation date as 2025-11-30.
The current release observation is v2.10.2, published on 2026-07-06.
The release capture records eight releases between 2026-06-24 and 2026-07-06.
The license is MIT by GitHub detection and by the repository README as retrieved on 2026-07-07.
The third-party notice records NextLevelBuilder as the publishing org and says the exact LICENSE copyright line was not captured.
The install path is `npm install -g ui-ux-pro-max-cli`, then `uipro init --ai [platform]`.
The CLI package is `ui-ux-pro-max-cli`, while the installed command is `uipro`.
The README also records Claude Marketplace plugin commands for Claude Code.
The mechanism category is retrieval and audit support, not taste prompting alone.
The source ledger records 102,037 stars as of 2026-07-07.
The S5e brief and claim pack frame that count as the largest skill-specific repo count in the covered six-skill set.
The ecosystem pack separately records the broader `anthropics/skills` monorepo at 159,044 stars as of 2026-07-07, so star comparisons need scope.
The README counts as of 2026-07-07 are 67 UI styles, 161 color palettes, 57 font pairings, 99 UX guidelines, 161 reasoning rules, 25 chart types, and 22 tech stacks.
The README breaks the 67 UI styles into 49 general styles, 8 landing page styles, and 10 BI or analytics dashboard styles.
The Snyk-era snapshot records 50+ styles, 97 color palettes, 57 font pairings, 99 UX guidelines, 25 chart types, and 9 technology stacks.
The captured SKILL.md frontmatter still says 50+ styles and 10 stacks, while the README says 67 styles and 22 tech stacks as of 2026-07-07.
The skill should be used when work changes how a feature looks, feels, moves, or is interacted with.
The captured SKILL.md says to skip the skill for pure backend logic, API work, database design, infrastructure, DevOps, and non-visual automation.

> [!contradiction]
> Database counts drift across sources: Snyk records 50+ styles and 97 palettes in its early 2026 snapshot, the captured SKILL.md still says 50+ styles, and the current README records 67 styles and 161 palettes on 2026-07-07.

## How it works
The skill ships data files and Python search scripts rather than only a static prose prompt.
The claim pack says CSV data files are queried by a BM25 search engine implemented in `search.py`.
The README describes five parallel searches for product type, style recommendations, color palette selection, landing page patterns, and typography pairing.
The README says the reasoning engine matches product to UI category rules.
The README says the reasoning engine applies style priorities with BM25 ranking.
The README says the reasoning engine filters anti-patterns for the industry.
The README says the reasoning engine processes decision rules with JSON conditions.
The repository tree records `ui-reasoning.csv` as a captured data file path in the source repository.
The Design System Generator outputs pattern, style, colors, typography, effects, anti-patterns, and a pre-delivery checklist.
The captured SKILL.md requires `--design-system` as the starting step for new project or page work.
Domain searches can supplement the design system through `--domain style`, `--domain color`, `--domain typography`, `--domain chart`, and `--domain ux`.
Stack searches can add framework guidance with `--stack react`, `--stack nextjs`, `--stack shadcn`, `--stack vue`, `--stack swiftui`, and other captured stack names.
The README records 18 supported platforms including Claude Code, Cursor, Windsurf, Antigravity, Copilot, Kiro, Codex CLI, Continue, Gemini CLI, OpenCode, Qoder, CodeBuddy, Droid, KiloCode, Warp, Augment, Roo Code, and Trae.
The skill can persist a generated system to `design-system/MASTER.md`.
The skill can also persist page-level overrides under `design-system/pages/`.
The stack role is to retrieve a grounded design starting point, then hand off to taste prompting, micro-interaction craft, contracts, and audits where those layers apply.

## Best practice
- Reach for UI UX Pro Max when a project needs a style, palette, font pairing, UX rule, chart type, or stack-specific recommendation from a large database EVIDENCE-BASED
- Treat every count as a dated observation because this skill's database counts changed between Snyk's snapshot and the 2026-07-07 README EVIDENCE-BASED
- Install through `ui-ux-pro-max-cli` and the `uipro` command when using current assets EVIDENCE-BASED
- Start new page and project work with `--design-system` before narrower domain searches EVIDENCE-BASED
- Use domain searches after the generated design system when one dimension needs more detail EVIDENCE-BASED
- Use stack searches when implementation guidance depends on React, Next.js, shadcn/ui, SwiftUI, Flutter, or another captured stack EVIDENCE-BASED
- Pair this skill with [[Taste Skill (Project)]] when the project needs higher-level taste dials and aesthetic constraints PRACTITIONER
- Pair this skill with [[Impeccable (Toolchain)]] when the retrieved design system needs PRODUCT.md and DESIGN.md enforcement PRACTITIONER
- Keep the author field as NextLevelBuilder unless a future primary source names an individual maintainer EVIDENCE-BASED
- Use the MIT license statement with the third-party notice nuance that the exact LICENSE copyright line was not captured EVIDENCE-BASED

## Pitfalls
Do not repeat Snyk-era counts without dating them.
Do not merge 50+ styles, 67 styles, and 240+ styles into one undated claim.
Do not treat directory descriptions as independent rule content when the claim pack says they derive from the repository.
Do not call the 102,037-star observation a universal ecosystem maximum without explaining the `anthropics/skills` monorepo scope.
Do not treat the Design System Generator as visual verification.
The local research extract records superdesign.dev criticism that the skill cannot render or verify its own output.
The local research extract records superdesign.dev criticism that retrieval quality depends on keyword hits.
The local research extract records wilwaldon counts of 240+ styles and 127 font pairings, but says those figures exceeded the README and were not verified at capture.
Do not use the skill for backend, API, database, infrastructure, DevOps, or non-visual automation work unless the UI changes are part of the task.
Do not assume the current README counts will survive a future release.
Do not treat generated design tokens or persisted design-system files as production contracts until another layer reviews them.

## Sources
- GitHub repo, https://github.com/nextlevelbuilder/ui-ux-pro-max-skill, retrieved 2026-07-07.
- Raw GitHub README, https://raw.githubusercontent.com/nextlevelbuilder/ui-ux-pro-max-skill/main/README.md, retrieved 2026-07-07.
- Raw GitHub SKILL.md, https://raw.githubusercontent.com/nextlevelbuilder/ui-ux-pro-max-skill/main/.claude/skills/ui-ux-pro-max/SKILL.md, retrieved 2026-07-07.
- GitHub releases, https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/releases, retrieved 2026-07-07.
- GitHub API repo metadata, https://api.github.com/repos/nextlevelbuilder/ui-ux-pro-max-skill, retrieved 2026-07-07.
- Snyk market snapshot, https://snyk.io/articles/top-claude-skills-ui-ux-engineers/, retrieved 2026-07-07.
- wilwaldon toolkit, https://github.com/wilwaldon/Claude-Code-Frontend-Design-Toolkit, retrieved 2026-07-07.
- LobeHub directory, https://lobehub.com/skills/terminalskills-skills-ui-ux-pro-max, retrieved 2026-07-07.
- Local claim pack, references/claim-packs/claim-pack-ui-ux-pro-max.md, generated 2026-07-07.
- Local ecosystem pack, references/claim-packs/claim-pack-ecosystem.md, generated 2026-07-07.
- Local source extract, .raw/research/ui-ux-pro-max-extract.md, captured 2026-07-07.
- Local third-party notices, THIRD_PARTY_NOTICES.md, verified 2026-07-07.

## Related
Rules:
- [[UX Rules Database (99 Rules)]] explains the rule database this anchor relies on.
- [[Required Audits]] gives the cross-skill audit destination for retrieved UX guidance.
- [[AI Tells (Forbidden Patterns)]] overlaps with the skill's anti-pattern output.
Audits:
- [[Required Audits]] is the broader Gogh gate after retrieval work.
- [[Vercel Guidelines Audit]] is a downstream audit layer for runtime-fetched web rules.
Flows:
- [[Design System Generation Flow]] maps the brief-to-system workflow.
- [[Install and Load]] decides how this retrieval layer enters an agent workspace.
- [[Greenfield Build (Prompt 1)]] places retrieval before implementation and audit.
Sources:
- [[UI UX Pro Max Repo]] is the source note for repo, README, SKILL.md, release, and tree provenance.
- [[Reception Sources]] gives wider directory and practitioner context.
Entities:
- [[Coding Agents]] are the target operators that load the skill.
- [[The 13 Skills]] provides wider skill ecosystem context.
Concepts:
- [[Retrieval Database Skills]] names the mechanism class.
- [[Agent Skills Format]] gives the packaging context for retrieval beside other skill mechanisms.

## Next actions
- Refresh the GitHub API, README, and release page before repeating stars, versions, or database counts.
- Reconcile README, SKILL.md frontmatter, and source-ledger count drift after the next upstream release.
- Keep unverified 240+ style and 127 font-pairing figures out of anchor prose unless a future source confirms them.
- Add a dedicated NextLevelBuilder entity note only if a later slice adds it to the link registry.
- Route implementation contracts to [[Impeccable (Toolchain)]] after a design system is generated.
- Route final web audit work to [[Vercel Guidelines Audit]] when the project needs file-level findings.
