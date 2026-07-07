---
type: "comparison"
title: "Install Surface and Format Portability"
status: "developing"
created: "2026-07-07"
updated: "2026-07-07"
tags: ["gogh/stack", "note/comparison"]
domain: "stack"
confidence: "evidence-based"
related: ["[[Agent Skills Format]]", "[[Install and Load]]", "[[Design Skills Mechanism Map]]", "[[Impeccable (Toolchain)]]", "[[Taste Skill (Project)]]", "[[Make Interfaces Feel Better (Skill)]]", "[[Anthropic Frontend Design Skill]]", "[[UI UX Pro Max Repo|UI UX Pro Max (Skill)]]"]
source_urls: ["https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills (retrieved 2026-07-06)", "https://www.tasteskill.dev/guide?view=full (retrieved 2026-07-07)", "https://github.com/pbakaus/impeccable (retrieved 2026-07-07)", "https://github.com/jakubkrehel/make-interfaces-feel-better (retrieved 2026-07-07)", "https://github.com/nextlevelbuilder/ui-ux-pro-max-skill (retrieved 2026-07-07)", "https://raw.githubusercontent.com/vercel-labs/agent-skills/main/skills/web-design-guidelines/SKILL.md (retrieved 2026-07-07)"]
sources: ["[[Design Theory Sources]]", "[[Taste Skill Official Site]]", "[[Impeccable Repo and Site]]", "[[MIFB Repo and Skill File]]", "[[UI UX Pro Max Repo]]", "[[Reception Sources]]"]
---
Install Surface and Format Portability compares how the six skills move across Claude Code, Cursor, Codex, and adjacent harnesses.

## What it is
Anthropic's Agent Skills format uses folders with SKILL.md and progressive disclosure.
The ecosystem claim pack says the format rests on Anthropic's open standard.
Taste Skill installs through `npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend"`.
Anthropic frontend-design installs through `npx skills add https://github.com/anthropics/skills --skill frontend-design`.
MIFB installs through `npx skills add jakubkrehel/make-interfaces-feel-better`.
Vercel web-design-guidelines installs through `npx skills add vercel-labs/agent-skills --skill web-design-guidelines`.
Impeccable has several paths, including `npx impeccable install`, Claude Code plugin marketplace, and `npx skills add pbakaus/impeccable`.
UI UX Pro Max uses `npm install -g ui-ux-pro-max-cli` and then `uipro init --ai [platform]`.
Impeccable installs provider-native hook manifests on Claude Code, GitHub Copilot, Codex, and Cursor.
Codex requires approving the project hook after Impeccable install or update, according to the captured README.
UI UX Pro Max lists 18 platforms in its README as of 2026-07-07.
Install comparability is therefore channel-specific, not one universal metric.

## How it works
| Skill | Install surface | Provider coverage in evidence | Hook or runtime caveat |
|---|---|---|---|
| Taste Skill v2 | `npx skills add ... --skill "design-taste-frontend"` | Site lists Claude Code, Cursor, Codex, Gemini CLI, v0, Lovable, OpenCode | No hook layer in captured evidence |
| Anthropic frontend-design | `npx skills add ... --skill frontend-design` and Claude plugin | skills.sh and Claude plugin surfaces in claim pack | Apache-2.0 per skill folder |
| MIFB | `npx skills add jakubkrehel/make-interfaces-feel-better` | Claim pack says Claude Code, Codex, Cursor, and other SKILL.md harnesses | README-declared MIT with missing LICENSE caveat |
| Impeccable | `npx impeccable install`, plugin marketplace, or `npx skills add` | README lists Cursor, Claude Code, GitHub Copilot, Gemini CLI, Codex CLI, OpenCode, Pi, Kiro, Trae, Rovo Dev, Qoder | Hooks differ by provider |
| UI UX Pro Max | `npm install -g ui-ux-pro-max-cli`, then `uipro init --ai [platform]` | README lists 18 platforms | Uses own CLI, not npx skills registry flow |
| Vercel web-design-guidelines | `npx skills add vercel-labs/agent-skills --skill web-design-guidelines` | Live page lists several agents in Integrate with Agents | Fetches command.md at runtime |

## Best practice
- Prefer the official install command from the captured source for each skill EVIDENCE-BASED
- Do not compare skills.sh install counts across skills that do not all use skills.sh EVIDENCE-BASED
- Treat `npx skills` as central Vercel infrastructure where the evidence shows adoption EVIDENCE-BASED
- Use Impeccable's CLI installer when provider hooks and updates matter EVIDENCE-BASED
- Approve Codex hooks after Impeccable install or update when the README requires it EVIDENCE-BASED
- Use UI UX Pro Max's `uipro` path for its database assets EVIDENCE-BASED
- Record license nuance for MIFB and Vercel agent-skills when no repo license file is detected EVIDENCE-BASED
- Reinstall or refresh runtime-fetched Vercel rules only when the wrapper changes, because rules fetch at audit time EVIDENCE-BASED
- Treat Claude plugin paths and skill paths as separate distribution channels EVIDENCE-BASED
- Test a moved skill in the target harness before assuming hooks or slash commands survive PRACTITIONER

## Pitfalls
Moving a SKILL.md folder does not automatically move provider-native hooks.
Moving Impeccable to Codex without hook approval can leave the hook inactive.
Moving UI UX Pro Max through `npx skills` would miss its documented CLI path.
Moving Vercel web-design-guidelines offline can break runtime rule fetching.
Moving a skill with supporting files without its references can break progressive disclosure.
Moving between Claude Code and Cursor can change hook behavior for Impeccable.
Moving counts from skills.sh into UI UX Pro Max adoption would be channel confusion.
Moving the Anthropic per-skill license to the whole repo would overstate repo-level license evidence.
Moving MIFB without the license caveat would hide the missing LICENSE-file nuance.
Moving a skill without reviewing bundled scripts conflicts with security guidance in the ecosystem pack.

## Sources
- Anthropic Agent Skills article, https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills, retrieved 2026-07-06.
- Taste Skill official guide, https://www.tasteskill.dev/guide?view=full, retrieved 2026-07-07.
- Impeccable README, https://github.com/pbakaus/impeccable, retrieved 2026-07-07.
- MIFB README, https://github.com/jakubkrehel/make-interfaces-feel-better, retrieved 2026-07-07.
- UI UX Pro Max README, https://github.com/nextlevelbuilder/ui-ux-pro-max-skill, retrieved 2026-07-07.
- Vercel web-design-guidelines SKILL.md, https://raw.githubusercontent.com/vercel-labs/agent-skills/main/skills/web-design-guidelines/SKILL.md, retrieved 2026-07-07.
- Claim pack ecosystem, references/claim-packs/claim-pack-ecosystem.md, generated 2026-07-07.
- Source ledger, references/source-ledger.json, generated 2026-07-06 with 2026-07-07 capture rows.

## Related
- [[Agent Skills Format]] explains SKILL.md progressive disclosure.
- [[Install and Load]] is the existing Taste Skill install flow.
- [[Design Skills Mechanism Map]] explains why install surface is separate from mechanism.
- [[Impeccable (Toolchain)]] is the hook-heavy skill anchor.
- [[Taste Skill (Project)]] is the primary npx skills design-taste install anchor.
- [[Make Interfaces Feel Better (Skill)]] is the MIFB install anchor.
- [[Anthropic Frontend Design Skill]] is the vendor baseline install anchor.
- [[UI UX Pro Max Repo|UI UX Pro Max (Skill)]] documents the `uipro` route.
- [[Reception Sources|Vercel Web Design Guidelines]] documents the runtime fetch-and-audit route.
- [[Prompt Layer vs Toolchain]] explains when install overhead pays off.

## Next actions
- Re-check install commands before any quickstart release.
- Keep channel-specific install metrics separate.
- Add a Vercel source note in a future slice if source-note coverage is expanded.
- Keep hook caveats visible in Codex and Cursor instructions.
- Use this comparison before writing portability claims in deliverables.

