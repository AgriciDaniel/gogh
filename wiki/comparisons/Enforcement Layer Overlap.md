---
type: "comparison"
title: "Enforcement Layer Overlap"
status: "developing"
created: "2026-07-07"
updated: "2026-07-07"
tags: ["gogh/stack", "note/comparison"]
domain: "stack"
confidence: "evidence-based"
related: ["[[Pre-Flight Check (Section 14)]]", "[[Impeccable Audit and Detect]]", "[[Impeccable Rule Set (45 Detectors)]]", "[[MIFB Review Checklist]]", "[[Required Audits]]", "[[Audit Pipeline Flow]]", "[[Unified Pre-Flight Mega-Checklist]]", "[[Design Review as Infrastructure]]"]
source_urls: ["https://raw.githubusercontent.com/Leonxlnx/taste-skill/main/skills/taste-skill/SKILL.md (retrieved 2026-07-07)", "https://github.com/pbakaus/impeccable (retrieved 2026-07-07)", "https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md (retrieved 2026-07-07)", "https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/skills/make-interfaces-feel-better/SKILL.md (retrieved 2026-07-07)"]
sources: ["[[Canonical Skill File]]", "[[Impeccable Repo and Site]]", "[[MIFB Repo and Skill File]]", "[[Reception Sources]]"]
---
Enforcement Layer Overlap maps what each check family catches so teams can gate once and avoid repeated manual review loops.

## What it is
Taste Skill Section 14 is a mandatory pre-flight check.
Taste Skill says any failed Section 14 box blocks completion.
Impeccable detect has 45 deterministic detector rules as of 2026-07-07.
Impeccable detect runs without an LLM or API keys, per claim-pack-impeccable I011.
Vercel web-design-guidelines reports findings in terse file:line format.
The Vercel local extract counted roughly 85 discrete guidelines in command.md.
The Vercel claim pack phrases the command.md volume as roughly 90-110 rules across 16+ categories.
MIFB provides a review checklist and Before and After review format.
The overlap is strongest around motion, focus, touch targets, typography, card overuse, and anti-slop patterns.
The overlap is weakest around aesthetic direction, because Vercel is audit-only and MIFB is micro-detail-focused.
This note uses check families instead of exact rule counts where counts are contested.
The dedupe rule is to run the cheapest deterministic gates before broad LLM critique.

## How it works
| Check family | Taste Skill Section 14 | Impeccable detect | Vercel guidelines | MIFB checklist | Pipeline stage |
|---|---|---|---|---|---|
| AI slop tells | Blocks completion | Deterministic anti-pattern families | Anti-pattern category | Advises craft fixes | Pre-merge gate |
| Typography | Hero, body, Inter, fake numbers | Overused fonts and line length | Tabular numbers and content rules | Font smoothing and tabular numbers | Gate plus polish |
| Color and contrast | Accent lock, CTA contrast, palette bans | Gray on color and palette issues | Accessibility contrast cues | Image outlines and shadows | Gate plus polish |
| Motion | Motivated motion and reduced motion | Bounce and easing families | Reduced motion and no transition all | Interruptible transitions and press scale | Gate plus feel pass |
| Layout repetition | Section layout and bento checks | Card nesting and cramped padding | Navigation and safe areas | Radius and optical alignment | Gate plus feel pass |
| Touch and focus | CTA visibility and form contrast | Small touch targets | Focus, keyboard, touch | 40x40px or 44x44px hit areas | Gate |
| Assets | Real images and no fake screenshots | Visual anti-patterns | Image dimensions and CLS | Image outlines | Gate plus polish |
| Contracts | Not covered as files | PRODUCT.md and DESIGN.md | Not a contract layer | Not a contract layer | Setup |
| File:line reporting | Manual checklist | CLI JSON and hook findings | Required output format | Review table | CI or PR review |
| Brand preservation | Redesign protocol | Product and design context | Not primary | Not primary | Redesign setup |

> [!contradiction]
> Vercel count language differs by local evidence: the extract counted roughly 85 discrete guidelines, while the claim pack uses roughly 90-110 and notes Snyk's 100+ description.

## Best practice
- Run Impeccable detect before broad manual critique when the project supports it EVIDENCE-BASED
- Use Taste Skill Section 14 as the blocking landing-page pre-flight when Taste Skill is active EVIDENCE-BASED
- Use Vercel web-design-guidelines for file:line accessibility, UX, and performance findings EVIDENCE-BASED
- Use MIFB after gates to improve tactile and surface details EVIDENCE-BASED
- Dedupe repeated motion checks by keeping one gate row and one feel-pass row PRACTITIONER
- Dedupe repeated touch target checks by keeping Vercel or Impeccable as gate and MIFB as implementation advice PRACTITIONER
- Keep detector results attributed to Impeccable, not Gogh EVIDENCE-BASED
- Use count ranges for Vercel until a fresh line count is recorded EVIDENCE-BASED
- Treat Section 14 item count as contested if anyone calls it 60 items CONTESTED
- Record waivers in the project contract when a deterministic detector conflicts with brand evidence PRACTITIONER

## Pitfalls
Running all checks as blockers can slow every change without improving signal.
Letting advisory MIFB notes block merge can overstate the skill's original contract.
Letting Vercel audit replace aesthetic direction can miss brand and hero quality.
Letting Taste Skill replace Vercel can miss form and semantics details.
Letting Impeccable detector findings be renamed as Gogh findings violates the product boundary.
Using old Impeccable detector counts can make the matrix stale.
Using exact Vercel rule counts without stating the count method can create false precision.
Ignoring project contracts can create repeated waivers for legitimate brand choices.
Ignoring manual screenshot review can miss issues no text detector sees.
Ignoring Section 14 after a Taste Skill build conflicts with Taste Skill's blocking rule.

## Sources
- Taste Skill SKILL.md, https://raw.githubusercontent.com/Leonxlnx/taste-skill/main/skills/taste-skill/SKILL.md, retrieved 2026-07-07.
- Impeccable README, https://github.com/pbakaus/impeccable, retrieved 2026-07-07.
- Impeccable releases, https://github.com/pbakaus/impeccable/releases, retrieved 2026-07-07.
- Vercel command.md, https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md, retrieved 2026-07-07.
- MIFB SKILL.md, https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/skills/make-interfaces-feel-better/SKILL.md, retrieved 2026-07-07.
- Claim pack impeccable, references/claim-packs/claim-pack-impeccable.md, generated 2026-07-07.
- Claim pack Vercel, references/claim-packs/claim-pack-vercel-web-design-guidelines.md, generated 2026-07-07.
- Vercel extract, .raw/research/vercel-web-design-guidelines-extract.md, captured 2026-07-07.

## Related
- [[Pre-Flight Check (Section 14)]] is the Taste Skill blocking checklist.
- [[Impeccable Audit and Detect]] explains the Impeccable audit and detector split.
- [[Impeccable Rule Set (45 Detectors)]] is the detector rule note.
- [[MIFB Review Checklist]] is the MIFB advisory review surface.
- [[Required Audits]] is the existing audit hub note.
- [[Audit Pipeline Flow]] turns this comparison into order of operations.
- [[Unified Pre-Flight Mega-Checklist]] deduplicates this overlap into a deliverable.
- [[Design Review as Infrastructure]] supplies the theory context.
- [[Deterministic Design Detection]] explains the no-LLM detector layer.
- [[Prompt Layer vs Toolchain]] explains why persistent enforcement can pay off.

## Next actions
- Use this matrix before updating the mega-checklist.
- Re-count Vercel command.md after any source refresh.
- Re-check Impeccable releases before repeating the 45 detector total.
- Keep MIFB rows advisory unless a later source defines blocking behavior.
- Preserve Section 14 blocking language only when Taste Skill is active.

