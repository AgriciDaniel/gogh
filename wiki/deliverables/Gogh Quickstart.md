---
type: "deliverable"
title: "Gogh Quickstart"
status: "developing"
created: "2026-07-07"
updated: "2026-07-07"
tags: ["gogh/stack", "note/deliverable"]
domain: "stack"
confidence: "evidence-based"
related: ["[[Design Skills Cheat Sheet]]", "[[Skill Stack Decision One-Pager]]", "[[Full Stack Build Flow]]", "[[Audit Pipeline Flow]]", "[[Install Surface and Format Portability]]", "[[Design Skills Mechanism Map]]", "[[Unified Pre-Flight Mega-Checklist]]", "[[Skill Stack Selection Flow]]"]
source_urls: ["https://www.tasteskill.dev/guide?view=full (retrieved 2026-07-07)", "https://www.skills.sh/anthropics/skills/frontend-design (retrieved 2026-07-07)", "https://github.com/jakubkrehel/make-interfaces-feel-better (retrieved 2026-07-07)", "https://github.com/pbakaus/impeccable (retrieved 2026-07-07)", "https://github.com/nextlevelbuilder/ui-ux-pro-max-skill (retrieved 2026-07-07)", "https://www.skills.sh/vercel-labs/agent-skills/web-design-guidelines (retrieved 2026-07-07)"]
sources: ["[[Taste Skill Official Site]]", "[[Anthropic Frontend Design Skill and Post]]", "[[MIFB Repo and Skill File]]", "[[Impeccable Repo and Site]]", "[[UI UX Pro Max Repo]]", "[[Reception Sources]]"]
---
Gogh Quickstart is the first-project operator guide: install the six skills, choose the stack, build in the recommended order, and run `gogh-brain advise`.

## What it is
This quickstart is a stack-level deliverable for Gogh operators.
The install commands come from the captured sources and per-skill claim packs.
The recommended order comes from Full Stack Build Flow.
The decision step comes from Skill Stack Selection Flow.
The audit step comes from Audit Pipeline Flow.
The source URLs were retrieved on 2026-07-07 unless noted in source notes.
The guide does not mutate production systems.
The guide does not call the brain market-ready.
The guide assumes a project brief can be encoded for `gogh-brain advise`.
The guide keeps UI UX Pro Max on its own CLI path.
The guide keeps Vercel as a runtime audit wrapper.
The guide keeps Impeccable hook approval caveats in the portability note.

## How it works
Install commands:

| Skill | Command | Source |
|---|---|---|
| Taste Skill v2 | `npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend"` | T004 |
| Anthropic frontend-design | `npx skills add https://github.com/anthropics/skills --skill frontend-design` | A011 |
| MIFB | `npx skills add jakubkrehel/make-interfaces-feel-better` | M005 |
| Impeccable | `npx impeccable install`, then `/impeccable init` | I006 |
| UI UX Pro Max | `npm install -g ui-ux-pro-max-cli`, then `uipro init --ai [platform]` | U010 |
| Vercel web-design-guidelines | `npx skills add vercel-labs/agent-skills --skill web-design-guidelines` | V003 |

First-project walkthrough:

1. Write a brief with project_type, brand_maturity, motion, density, and accessibility.
2. Run `gogh-brain advise --vault <path> --brief <file>`.
3. Use Skill Stack Decision One-Pager to confirm the selected skills.
4. Start direction with Taste Skill dials and Anthropic subject-grounding where appropriate.
5. Query UI UX Pro Max if brand maturity is none or partial.
6. Build the first complete page or surface.
7. Apply MIFB for concentric radii, interruptible motion, press feedback, and hit areas.
8. Run `/impeccable init` if contracts are useful for the project.
9. Run Impeccable commands or detect for toolchain enforcement.
10. Run Vercel web-design-guidelines on target files.
11. Run the Unified Pre-Flight Mega-Checklist.
12. Resolve conflicts through comparison notes.
13. Re-run gates after fixes.
14. Keep the report source-cited.

Recommended stack order:

| Order | Layer | Skill |
|---|---|---|
| 1 | Direction | Taste Skill v2 |
| 2 | Direction baseline | Anthropic frontend-design |
| 3 | Retrieval when needed | UI UX Pro Max |
| 4 | Feel pass | MIFB |
| 5 | Contracts and detection | Impeccable |
| 6 | File:line audit | Vercel web-design-guidelines |
| 7 | Final merge check | Unified Pre-Flight Mega-Checklist |

## Best practice
- Install from the official captured command for each skill EVIDENCE-BASED
- Use `gogh-brain advise` before starting implementation EVIDENCE-BASED
- Set direction before feel polish PRACTITIONER
- Retrieve style data before implementation when brand maturity is low EVIDENCE-BASED
- Run Impeccable init before relying on project-specific Impeccable commands EVIDENCE-BASED
- Run Vercel audit on real target files EVIDENCE-BASED
- Run the mega-checklist after the page or surface exists EVIDENCE-BASED
- Re-run deterministic gates after fixes PRACTITIONER
- Keep source dates visible in reports EVIDENCE-BASED
- Do not call the result market-ready unless the audit gate passes EVIDENCE-BASED

## Pitfalls
Installing all skills does not mean every skill should run on every task.
Running MIFB before direction can polish a weak concept.
Running Vercel before files exist can produce no useful audit.
Running Impeccable without init can miss project context.
Installing UI UX Pro Max through the wrong channel can miss its database assets.
Skipping Codex hook approval can leave Impeccable hooks inactive.
Skipping source dates can stale install and count claims.
Skipping conflict notes can hide font and motion disagreements.
Skipping Section 14 after a Taste Skill build violates Taste Skill guidance.
Skipping audit and package gates can misstate maturity.

## Sources
- Taste Skill guide, https://www.tasteskill.dev/guide?view=full, retrieved 2026-07-07.
- Anthropic frontend-design skills.sh page, https://www.skills.sh/anthropics/skills/frontend-design, retrieved 2026-07-07.
- MIFB README, https://github.com/jakubkrehel/make-interfaces-feel-better, retrieved 2026-07-07.
- Impeccable README, https://github.com/pbakaus/impeccable, retrieved 2026-07-07.
- UI UX Pro Max README, https://github.com/nextlevelbuilder/ui-ux-pro-max-skill, retrieved 2026-07-07.
- Vercel skills.sh page, https://www.skills.sh/vercel-labs/agent-skills/web-design-guidelines, retrieved 2026-07-07.
- Local stack advisor, scripts/render_stack_advisor.py, read 2026-07-07.
- Claim packs, references/claim-packs, generated 2026-07-07.

## Related
- [[Design Skills Cheat Sheet]] gives the compact skill table.
- [[Skill Stack Decision One-Pager]] gives the brief-to-stack decision sheet.
- [[Full Stack Build Flow]] gives the recommended order.
- [[Audit Pipeline Flow]] gives the verification order.
- [[Install Surface and Format Portability]] gives channel and hook caveats.
- [[Design Skills Mechanism Map]] explains why the order works.
- [[Unified Pre-Flight Mega-Checklist]] provides the final release screen.
- [[Skill Stack Selection Flow]] mirrors the advisor code.
- [[Prompt Layer vs Toolchain]] explains when Impeccable setup pays off.
- [[Brain Refresh Flow]] explains when to refresh this guide.

## Next actions
- Keep all install commands refreshed before release.
- Add provider-specific walkthroughs only after source evidence exists.
- Run `gogh-brain advise` with a real project brief before first use.
- Keep the quickstart linked to the decision one-pager and mega-checklist.
- Re-run lint and audit after deliverable changes.

