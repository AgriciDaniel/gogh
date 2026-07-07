---
type: "flow"
title: "Design System Generation Flow"
status: "developing"
created: "2026-07-07"
updated: "2026-07-07"
tags: ["gogh/ui-ux-pro-max", "note/flow"]
domain: "ui-ux-pro-max"
confidence: "evidence-based"
related: ["[[UI UX Pro Max (Skill)]]", "[[Retrieval Database Skills]]", "[[UX Rules Database (99 Rules)]]", "[[Install and Load]]", "[[Greenfield Build (Prompt 1)]]", "[[Dial Tuning Guide]]", "[[Impeccable Project Lifecycle]]", "[[Impeccable (Toolchain)]]"]
source_urls: ["https://raw.githubusercontent.com/nextlevelbuilder/ui-ux-pro-max-skill/main/README.md (retrieved 2026-07-07)", "https://raw.githubusercontent.com/nextlevelbuilder/ui-ux-pro-max-skill/main/.claude/skills/ui-ux-pro-max/SKILL.md (retrieved 2026-07-07)", "https://github.com/nextlevelbuilder/ui-ux-pro-max-skill (retrieved 2026-07-07)", "https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/releases (retrieved 2026-07-07)"]
sources: ["[[UI UX Pro Max Repo]]"]
approval_status: "advisory"
risk_level: "medium"
rollback_note: "Remove generated design-system files or ignore retrieved recommendations if the project adopts another source of truth."
---
Design System Generation Flow turns a short product brief into a retrieved UI system with pattern, style, palette, typography, effects, anti-patterns, and checks.

## What it is
This flow documents the UI UX Pro Max path from user request to generated design system.
The README calls the Design System Generator the flagship feature of v2.0.
The claim pack records the Design System Generator as a v2 flagship feature.
The generator is described as an AI reasoning engine that analyzes project requirements.
The generator produces a complete tailored design system in the captured README example.
The captured SKILL.md says new project and page work should start from Step 1 and Step 2.
Step 1 analyzes user requirements.
Step 2 generates the design system.
Step 2b can persist the design system.
Step 2c can tune output with optional dials.
Step 3 supplements the design system with detailed domain searches.
Step 4 retrieves stack guidelines.
The flow applies to pages, landing pages, dashboards, admin panels, SaaS products, mobile apps, and similar UI work covered by the captured SKILL.md.
The flow does not replace final implementation review.
The flow does not replace product-specific acceptance criteria.
The flow is advisory in Gogh V1 because Gogh is a read-only advisory brain.

## How it works
Start with the user brief.
Extract product type from the brief.
Extract target audience from the brief.
Extract style keywords from the brief.
Extract the implementation stack from the brief when the stack is known.
Invoke the generator with `python3 skills/ui-ux-pro-max/scripts/search.py "<query>" --design-system [-p "Project Name"]`.
The README also shows installed Claude paths such as `.claude/skills/ui-ux-pro-max/scripts/search.py`.
The query should combine product, industry, and style keywords.
The captured SKILL.md recommends multi-dimensional keywords instead of single-word queries.
The generator searches product, style, color, landing, and typography domains in parallel.
The reasoning engine applies product category rules.
The reasoning engine applies style priorities through BM25 ranking.
The reasoning engine filters anti-patterns for the industry.
The reasoning engine processes decision rules.
The output includes pattern.
The output includes style.
The output includes colors.
The output includes typography.
The output includes effects.
The output includes anti-patterns to avoid.
The output includes a pre-delivery checklist.
Use `-f markdown` when documentation output is preferred.
Use `--persist` to create `design-system/MASTER.md`.
Use `--page "dashboard"` or another page name when a page-specific override is needed.
For page work after persistence, read the master file first.
Then check for a matching page override.
If the page override exists, prioritize its deviations.
If the page override does not exist, use the master rules exclusively.
After generation, run narrower domain searches for uncertain areas.
After generation, run stack search for framework-specific guidance.
After generation, hand off to [[Dial Tuning Guide]] or [[Taste Skill (Project)]] when the aesthetic direction needs stack-level taste tuning.
After generation, hand off to [[Impeccable (Toolchain)]] when retrieved choices need PRODUCT.md and DESIGN.md contracts.

## Best practice
- Start every new project or page with `--design-system` when using UI UX Pro Max EVIDENCE-BASED
- Build the query from product type, industry, tone, density, and stack instead of one generic noun EVIDENCE-BASED
- Use the generated system as a structured recommendation, not as finished UI verification EVIDENCE-BASED
- Persist `design-system/MASTER.md` when the project needs retrieval across later sessions EVIDENCE-BASED
- Use page overrides only for deviations from the master system EVIDENCE-BASED
- Run domain searches after generation for detailed style, color, typography, chart, or UX questions EVIDENCE-BASED
- Run stack search after generation when implementation choices depend on framework details EVIDENCE-BASED
- Hand off to taste dials when the retrieved system is plausible but not yet brand-fit PRACTITIONER
- Hand off to Impeccable contracts when the retrieved system must become project policy PRACTITIONER
- Keep rollback simple by treating generated files as advisory until the team adopts them PRACTITIONER

## Pitfalls
Do not start with isolated `--domain` searches when the task is a new page or project.
The captured SKILL.md marks `--design-system` as required for that workflow.
Do not assume the generated output has inspected the rendered UI.
The local research extract records that the tool cannot render or verify its own output.
Do not persist a design system if the project already has a stronger source of truth and no migration decision.
Do not let page overrides silently replace the master design system.
The captured workflow says page files override only deviations from the master.
Do not skip stack search when a platform has specific navigation, performance, or accessibility rules.
Do not treat optional UI UX Pro Max dials as a substitute for the broader Gogh stack-selection decision.
Do not hand off to Impeccable before the generated design choices are clear enough to write into contracts.
Do not call generated anti-patterns exhaustive.
Do not skip pre-delivery UX checks after generation.

> [!gap]
> The assigned captures document commands and outputs, but they do not include a rendered-output benchmark proving that generated design systems improve final UI quality.

## Sources
- Raw GitHub README, https://raw.githubusercontent.com/nextlevelbuilder/ui-ux-pro-max-skill/main/README.md, retrieved 2026-07-07.
- Raw GitHub SKILL.md, https://raw.githubusercontent.com/nextlevelbuilder/ui-ux-pro-max-skill/main/.claude/skills/ui-ux-pro-max/SKILL.md, retrieved 2026-07-07.
- GitHub repo, https://github.com/nextlevelbuilder/ui-ux-pro-max-skill, retrieved 2026-07-07.
- GitHub releases, https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/releases, retrieved 2026-07-07.
- Local source extract, .raw/research/ui-ux-pro-max-extract.md, captured 2026-07-07.
- Local claim pack, references/claim-packs/claim-pack-ui-ux-pro-max.md, generated 2026-07-07.
- Local product spec, references/product-spec.md, read during S5e authoring.
- Local operator kit, docs/OPERATOR_KIT.md, read during S5e authoring.

## Related
- [[UI UX Pro Max (Skill)]] is the skill that owns this generation flow.
- [[Retrieval Database Skills]] explains the retrieval mechanism behind the flow.
- [[UX Rules Database (99 Rules)]] supplies the UX checks used during and after generation.
- [[Install and Load]] decides whether this flow belongs in an agent workspace.
- [[Greenfield Build (Prompt 1)]] places this flow in the larger Gogh build order.
- [[Dial Tuning Guide]] is the stack-level tuning handoff after retrieval.
- [[Impeccable Project Lifecycle]] is the contract and command destination for stable choices.
- [[Impeccable (Toolchain)]] enforces choices after the retrieval phase.
- [[Vercel Guidelines Audit]] provides a later web-audit comparison layer.
- [[Image-First Reference Pipeline]] is an alternate input path when visual references lead the brief.

## Next actions
- Refresh command examples when the upstream CLI or install layout changes.
- Add a worked example only if a future slice owns an example note.
- Keep generated design-system files advisory until a project explicitly adopts them.
- Capture benchmark evidence if future research measures generated system quality.
- Record conflicts with taste dials or Impeccable contracts in a comparison note.
- Recheck v2 generator behavior after the next release beyond v2.10.2.
