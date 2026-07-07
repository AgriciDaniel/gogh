---
type: "concept"
title: "Retrieval Database Skills"
status: "developing"
created: "2026-07-07"
updated: "2026-07-07"
tags: ["gogh/ui-ux-pro-max", "note/concept"]
domain: "ui-ux-pro-max"
confidence: "evidence-based"
related: ["[[UI UX Pro Max (Skill)]]", "[[UX Rules Database (99 Rules)]]", "[[Design System Generation Flow]]", "[[Agent Skills Format]]", "[[Required Audits]]", "[[Deterministic Design Detection]]", "[[Impeccable (Toolchain)]]", "[[Anthropic Frontend Design Skill]]"]
source_urls: ["https://github.com/nextlevelbuilder/ui-ux-pro-max-skill (retrieved 2026-07-07)", "https://raw.githubusercontent.com/nextlevelbuilder/ui-ux-pro-max-skill/main/README.md (retrieved 2026-07-07)", "https://raw.githubusercontent.com/nextlevelbuilder/ui-ux-pro-max-skill/main/.claude/skills/ui-ux-pro-max/SKILL.md (retrieved 2026-07-07)", "https://lobehub.com/skills/terminalskills-skills-ui-ux-pro-max (retrieved 2026-07-07)", "https://github.com/wilwaldon/Claude-Code-Frontend-Design-Toolkit (retrieved 2026-07-07)"]
sources: ["[[UI UX Pro Max Repo]]"]
---
Retrieval Database Skills are agent skills that ship searchable data and retrieval scripts so the agent can pull a relevant design slice on demand instead of carrying every rule in context.

## What it is
UI UX Pro Max is the evidence-backed example of this mechanism in the Gogh stack.
The ecosystem claim pack classifies UI UX Pro Max as a BM25-searchable CSV database.
The source ledger classifies UI UX Pro Max as retrieval for styles, palettes, font pairings, and UX rules.
The mechanism differs from [[Anthropic Frontend Design Skill]], which the ecosystem pack characterizes as judgment prose.
The mechanism differs from [[Taste Skill (Project)]], which the ecosystem pack characterizes as taste prompting with dials and pre-flight guidance.
The mechanism differs from [[Impeccable (Toolchain)]], which the ecosystem pack characterizes as commands, contracts, and deterministic detectors.
The UI UX Pro Max repository tree records data files for styles, colors, typography, products, charts, landing, UX guidelines, app interface guidance, motion, icons, Google Fonts, and stack-specific guidance.
The tree records `search.py`, `core.py`, and `design_system.py` under the skill scripts.
The README says Python 3.x is required for the search script.
The claim pack says the search engine implements BM25 ranking.
The README says the Design System Generator is the v2 flagship feature.
The README says the Design System Generator analyzes project requirements and generates a tailored design system.
The local research extract says Python scripts query the database per request and return only the relevant slice into context.
The local research extract says this keeps token cost bounded.
The repository tree records `google-fonts.csv` at 743,272 bytes under `.claude/skills/ui-ux-pro-max/data/`.
The repository tree records `styles.csv` at 142,605 bytes under `.claude/skills/ui-ux-pro-max/data/`.
The repository tree records `design_system.py` at 57,424 bytes under `.claude/skills/ui-ux-pro-max/scripts/`.
Those sizes explain why retrieval matters at this scale.

## How it works
The agent first analyzes the user request for product type, target audience, style keywords, and stack.
For a new page or project, the captured SKILL.md says Step 2 is to generate a design system.
The design-system command calls `search.py` with a query and `--design-system`.
The README says multi-domain search runs across product, style, color, landing, and typography categories.
The README says the reasoning engine applies product category rules, style priorities, anti-pattern filters, and decision rules.
The output becomes a design-system recommendation rather than a raw list of all records.
After that output, narrower domain searches retrieve details for style, color, typography, chart, UX, Google Fonts, landing, React, web, GSAP, or prompt guidance.
Stack searches retrieve implementation guidance for frameworks and platforms.
The captured SKILL.md lists stacks including React, Next.js, Vue, Nuxt, Svelte, Astro, shadcn/ui, HTML Tailwind, Angular, Laravel, SwiftUI, Flutter, Jetpack Compose, React Native, and Three.js.
The README says persisted outputs can create `design-system/MASTER.md`.
The README says page overrides can be written under `design-system/pages/`.
The local research extract frames the main advantage as bounded context rather than a fixed opinion prompt.
The operator still has to synthesize the retrieved recommendations into code.
The operator still has to verify the generated UI because retrieval does not render or inspect the final interface.

## Best practice
- Use retrieval database skills when the source material is too large or too varied to keep in the working prompt EVIDENCE-BASED
- Start from the broad design-system search before drilling into narrower domains EVIDENCE-BASED
- Treat BM25 results as recommendations that still need synthesis and review EVIDENCE-BASED
- Use explicit product, industry, tone, density, and stack keywords because the captured SKILL.md recommends multi-dimensional queries EVIDENCE-BASED
- Persist `design-system/MASTER.md` when later sessions need the same retrieved system EVIDENCE-BASED
- Add page overrides only when a page differs from the master design system EVIDENCE-BASED
- Hand off to taste prompting when the project needs broader aesthetic direction beyond retrieved matches PRACTITIONER
- Hand off to toolchain enforcement when the retrieved design needs contracts, hooks, or deterministic checks PRACTITIONER
- Re-run retrieval after major brief changes rather than editing an old output by hand PRACTITIONER
- Keep large CSV claims tied to tree captures until the CSV contents are captured directly EVIDENCE-BASED

## Pitfalls
Retrieval can miss a good rule when the query terms are weak.
The local research extract records superdesign.dev's criticism that keyword matching can fail.
Retrieval output can be text-only.
The local research extract records superdesign.dev's criticism that the tool cannot render or verify its own output.
Large data files can drift faster than notes.
The claim pack records database count changes between the Snyk snapshot and the 2026-07-07 README.
Directory pages can repeat repository claims without independent rule verification.
The ecosystem claim pack warns that directory descriptions are often derived from repositories.
Do not treat retrieval as an audit result.
Do not treat persisted `MASTER.md` and page overrides as source of truth unless the project adopts them.
Do not confuse the UI UX Pro Max optional dials with Taste Skill's stack-level taste dial role.
Do not treat the tree listing as a substitute for captured CSV row contents.

> [!key-insight]
> The retrieval mechanism matters because the captured repository lists hundreds of kilobytes of data files, while the workflow retrieves only task-relevant design guidance.

## Sources
- GitHub repo, https://github.com/nextlevelbuilder/ui-ux-pro-max-skill, retrieved 2026-07-07.
- Raw GitHub README, https://raw.githubusercontent.com/nextlevelbuilder/ui-ux-pro-max-skill/main/README.md, retrieved 2026-07-07.
- Raw GitHub SKILL.md, https://raw.githubusercontent.com/nextlevelbuilder/ui-ux-pro-max-skill/main/.claude/skills/ui-ux-pro-max/SKILL.md, retrieved 2026-07-07.
- LobeHub directory, https://lobehub.com/skills/terminalskills-skills-ui-ux-pro-max, retrieved 2026-07-07.
- wilwaldon toolkit, https://github.com/wilwaldon/Claude-Code-Frontend-Design-Toolkit, retrieved 2026-07-07.
- Local tree capture, .raw/skills/ui-ux-pro-max/tree.txt, retrieved 2026-07-07.
- Local source extract, .raw/research/ui-ux-pro-max-extract.md, captured 2026-07-07.
- Local claim pack, references/claim-packs/claim-pack-ui-ux-pro-max.md, generated 2026-07-07.
- Local ecosystem claim pack, references/claim-packs/claim-pack-ecosystem.md, generated 2026-07-07.

## Related
- [[UI UX Pro Max (Skill)]] is the concrete retrieval database skill covered by this slice.
- [[UX Rules Database (99 Rules)]] is one retrieved rule domain inside the skill.
- [[Design System Generation Flow]] shows retrieval in operation.
- [[Required Audits]] gives the audit destination after retrieval-backed rules.
- [[Agent Skills Format]] gives the portable skill packaging context.
- [[Deterministic Design Detection]] distinguishes retrieved recommendations from enforcement layers.
- [[Impeccable (Toolchain)]] is the downstream contract and detector contrast.
- [[Anthropic Frontend Design Skill]] is the judgment-prose contrast.
- [[Taste Skill (Project)]] is the taste-prompting contrast.
- [[Vercel Web Design Guidelines]] is the runtime audit contrast.

## Next actions
- Add a cross-skill comparison if more database-style skills enter the covered set.
- Capture representative CSV rows only if a later slice needs rule-level provenance beyond README and SKILL.md.
- Refresh the tree listing before citing file sizes after the next upstream release.
- Keep retrieval claims separate from visual verification claims.
- Record any future benchmark evidence in [[Ecosystem and Alternatives]] if it becomes available.
- Recheck the Design System Generator behavior when v2.10.2 is no longer current.
