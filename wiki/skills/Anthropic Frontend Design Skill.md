---
type: "skill"
title: "Anthropic Frontend Design Skill"
status: "developing"
created: "2026-07-07"
updated: "2026-07-07"
tags: ["gogh/frontend-design", "note/skill"]
domain: "frontend-design"
confidence: "contested"
related: ["[[Anthropic Frontend Design Rules]]", "[[Distributional Convergence]]", "[[Official Baseline Positioning]]", "[[Agent Skills Format]]", "[[AI Slop]]", "[[Constraint Beats Coaxing]]", "[[Coding Agents]]", "[[Install and Load]]"]
source_urls: ["https://raw.githubusercontent.com/anthropics/skills/main/skills/frontend-design/SKILL.md (retrieved 2026-07-07)", "https://raw.githubusercontent.com/anthropics/skills/main/skills/frontend-design/LICENSE.txt (retrieved 2026-07-07)", "https://claude.com/blog/improving-frontend-design-through-skills (retrieved 2026-07-07)", "https://www.skills.sh/anthropics/skills/frontend-design (retrieved 2026-07-07)", "https://snyk.io/articles/top-claude-skills-ui-ux-engineers/ (retrieved 2026-07-07)", "https://composio.dev/content/top-design-skills (retrieved 2026-07-07)"]
sources: ["[[Anthropic Frontend Design Skill and Post]]", "[[Design Theory Sources]]", "[[Reception Sources]]"]
---

Anthropic Frontend Design Skill is the official frontend-design baseline skill for Claude-style agent workflows, and its strongest evidence-backed use is early aesthetic direction before stricter rulebooks, detectors, or audits take over.

## What it is

Anthropic Frontend Design Skill is named `frontend-design` in the captured `SKILL.md`.

The captured frontmatter says it guides distinctive and intentional visual design for new or reshaped UI.

The skill lives in the public `anthropics/skills` repository according to the S5d claim pack.

The S5d claim pack records the repository as created on 2025-09-22.

The same claim pack records 159,044 stars for `anthropics/skills` as of 2026-07-07.

The skill folder uses Apache-2.0 through its sibling `LICENSE.txt`.

The `SKILL.md` frontmatter says license terms are in `LICENSE.txt`.

GitHub detected no single repository-level license for `anthropics/skills` in the claim pack.

The companion launch post was published by Anthropic on 2025-11-12.

The launch post names Prithvi Rajasekaran, Justin Wei, and Alexander Bricken from the Applied AI team.

The launch post describes a compact launch-era frontend aesthetics skill of about 400 tokens.

The current captured `SKILL.md` is roughly 1,300 to 1,400 words.

That means the current skill has grown well past the launch-era prompt described in the blog.

The mechanism category is taste prompting.

It provides judgment scaffolding, not deterministic detectors.

It belongs near the beginning of the Gogh stack.

It sets a design direction before audits or lower-level craft passes inspect details.

## How it works

The skill asks the agent to behave like a small-studio design lead.

It tells the agent to ground the design in the subject, audience, and single job.

It treats the subject's materials, instruments, artifacts, and vernacular as the source of distinctiveness.

It makes the hero a thesis for the page.

It asks for one justified aesthetic risk.

It requires deliberate palette, typography, and layout choices.

It frames typography as part of the page personality.

It asks for display and body faces to be paired deliberately.

It warns against repeating the same font families across projects.

It treats structure as information.

It says numbered markers are appropriate only when order carries meaning.

It treats motion as a subject-serving choice.

It favors one orchestrated moment over scattered animation.

The process is brainstorm, explore, plan, critique, build, then critique again.

The plan includes color, type, layout, and a signature element.

The color plan uses 4-6 named hex values.

The critique checks whether the design reads like a default for a similar prompt.

The implementation should follow the revised plan exactly.

The writing guidance treats copy as design material.

The copy guidance prefers active voice, plain language, and specific labels.

The install command recorded in the claim pack is `npx skills add https://github.com/anthropics/skills --skill frontend-design`.

The claim pack also records a Claude Code plugin distribution channel.

> [!contradiction]
> Install-base claims are contested. Skills.sh showed 634.0K installs on 2026-07-07 with an unstated basis. Composio reported 277,000+ installs as of March 2026, and paddo.dev repeated 277k. Two direct Snyk fetches on 2026-07-07 found no install counts in the Snyk UI/UX article, so the common Snyk attribution is unsupported.

## Best practice

- Reach for this skill when a project needs a first-pass aesthetic direction, not when it needs a deterministic rule audit. EVIDENCE-BASED
- Use it before [[Anthropic Frontend Design Rules]] so the rule note can evaluate the direction it created. PRACTITIONER
- Pair it with [[Distributional Convergence]] when explaining why vague beauty prompts return common design defaults. EVIDENCE-BASED
- Follow the brief's own visual direction when the brief is explicit, even if the direction matches one of the skill's named defaults. EVIDENCE-BASED
- Keep install-count language dated and qualified because the skills.sh basis and 277k figure basis are not independently auditable. CONTESTED
- Treat the Apache-2.0 license as per-skill folder evidence, not as a repository-wide GitHub license finding. EVIDENCE-BASED
- Use the skill as taste prompting, then add stack tools for micro-details, retrieval, detectors, or runtime audits. EVIDENCE-BASED
- Re-check the upstream `SKILL.md` before market-ready claims because the path changed after the blog baseline. EVIDENCE-BASED

## Pitfalls

Calling the launch blog's about 400-token prompt the current skill is stale.

Calling the 277,000+ install figure a Snyk number is unsupported by the 2026-07-07 correction record.

Treating the skills.sh 634.0K install counter as independently audited would overstate the evidence.

Treating this skill as a detector would misstate its mechanism.

Using it after a strict audit pass can waste its primary value, which is early direction.

Copying its named defaults as bans would overstate the text, because the skill says the brief wins when it asks for one of those looks.

Assuming the whole `anthropics/skills` repository is Apache-2.0 would exceed the per-skill license evidence.

Ignoring the writing section would miss part of the current `SKILL.md`.

## Sources

Anthropic, https://raw.githubusercontent.com/anthropics/skills/main/skills/frontend-design/SKILL.md, retrieved 2026-07-07.

Anthropic, https://raw.githubusercontent.com/anthropics/skills/main/skills/frontend-design/LICENSE.txt, retrieved 2026-07-07.

Anthropic, https://claude.com/blog/improving-frontend-design-through-skills, retrieved 2026-07-07.

Skills.sh, https://www.skills.sh/anthropics/skills/frontend-design, retrieved 2026-07-07.

Snyk, https://snyk.io/articles/top-claude-skills-ui-ux-engineers/, retrieved 2026-07-07.

Composio, https://composio.dev/content/top-design-skills, retrieved 2026-07-07.

Local capture, `.raw/skills/anthropic-frontend-design/SKILL.md`, captured 2026-07-07.

Local extract, `.raw/research/anthropic-frontend-design-extract.md`, captured 2026-07-07.

## Related

Rules: [[Anthropic Frontend Design Rules]] explains the concrete rule surface that this anchor summarizes.

Concepts: [[Distributional Convergence]] explains the model behavior the launch blog names.

Concepts: [[AI Slop]] names the visible failure pattern this skill counters.

Concepts: [[Constraint Beats Coaxing]] explains why constraints outperform vague quality prompts.

Sources: [[Anthropic Frontend Design Skill and Post]] records capture provenance and corrections.

Reception: [[Official Baseline Positioning]] places the skill in the wider ecosystem.

Format: [[Agent Skills Format]] explains why `SKILL.md` files load on demand.

Operators: [[Install and Load]] is the existing install and activation pathway in the vault.

Entities: [[Coding Agents]] is the user category that applies these skill files.

Audits: [[Required Audits]] is where stricter post-build checks belong.

## Next actions

Re-check the upstream skill path before any release that claims current behavior.

Keep the install-base contradiction visible until a source publishes an auditable basis.

Link future Impeccable, Vercel, UI UX Pro Max, and MIFB notes once those registry titles exist locally.

Use this anchor as the landing note for Anthropic-specific frontend-design guidance.
