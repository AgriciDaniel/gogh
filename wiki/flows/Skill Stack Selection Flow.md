---
type: "flow"
title: "Skill Stack Selection Flow"
status: "developing"
created: "2026-07-07"
updated: "2026-07-07"
tags: ["gogh/stack", "note/flow"]
domain: "stack"
confidence: "evidence-based"
related: ["[[Design Skills Mechanism Map]]", "[[Full Stack Build Flow]]", "[[Audit Pipeline Flow]]", "[[Skill Stack Decision One-Pager]]", "[[The Three Dials]]", "[[UI UX Pro Max Repo|UI UX Pro Max (Skill)]]", "[[Impeccable (Toolchain)]]", "[[Reception Sources|Vercel Web Design Guidelines]]"]
source_urls: ["https://raw.githubusercontent.com/Leonxlnx/taste-skill/main/skills/taste-skill/SKILL.md (retrieved 2026-07-07)", "https://raw.githubusercontent.com/anthropics/skills/main/skills/frontend-design/SKILL.md (retrieved 2026-07-07)", "https://github.com/nextlevelbuilder/ui-ux-pro-max-skill (retrieved 2026-07-07)", "https://github.com/pbakaus/impeccable (retrieved 2026-07-07)", "https://raw.githubusercontent.com/vercel-labs/agent-skills/main/skills/web-design-guidelines/SKILL.md (retrieved 2026-07-07)"]
sources: ["[[Canonical Skill File]]", "[[Anthropic Frontend Design Skill and Post]]", "[[UI UX Pro Max Repo]]", "[[Impeccable Repo and Site]]", "[[Reception Sources]]"]
---
Skill Stack Selection Flow is the operator decision tree that mirrors the local `scripts/render_stack_advisor.py` rules.

## What it is
This flow translates project_type, brand_maturity, motion, density, and accessibility into a Gogh stack.
The local stack advisor accepts project_type values landing, portfolio, redesign, dashboard, app, and editorial.
The local stack advisor accepts brand_maturity values none, partial, and mature.
The local stack advisor accepts motion values static, restrained, rich, and cinematic.
The local stack advisor accepts density values airy, balanced, and dense.
The local stack advisor accepts accessibility values standard and strict.
The advisor recommends Taste Skill and Anthropic frontend-design for landing, portfolio, redesign, and editorial.
The advisor recommends UI UX Pro Max when brand maturity is none or partial.
The advisor recommends MIFB when motion is restrained, rich, or cinematic.
The advisor appends Impeccable for every valid brief.
The advisor appends Vercel web-design-guidelines for strict accessibility and for landing, redesign, app, and dashboard.
The advisor also calculates DESIGN_VARIANCE, MOTION_INTENSITY, and VISUAL_DENSITY.
The flow ends with running `gogh-brain advise` because the SKILL.md command map names that advisory command.

## How it works
0. Classify ambition before anything else: refresh (keep direction, tighten
   craft), evolve (keep brand, push variance), transform (new direction
   required; "impress me", "redesign", "make it special"). Ambition maps to
   DESIGN_VARIANCE: refresh 3 to 4, evolve 5 to 7, transform 8 to 9, and
   transform makes [[Aesthetic Direction Commitment]] mandatory.
1. Classify project_type first.
2. If project_type is landing, portfolio, redesign, or editorial, include Taste Skill and Anthropic frontend-design.
3. If project_type is dashboard or app, do not auto-include Taste Skill by the current advisor rule.
4. Classify brand_maturity second.
5. If brand_maturity is none or partial, include UI UX Pro Max for retrieval.
6. If brand_maturity is mature, preserve the brand before retrieving new style candidates.
7. Classify motion third.
8. If motion is restrained, rich, or cinematic, include MIFB for feel and micro-interactions.
9. If motion is static, keep MIFB optional for non-motion craft details.
10. Always include Impeccable in the current local advisor recommendation.
11. Include Vercel web-design-guidelines when accessibility is strict.
12. Include Vercel web-design-guidelines for landing, redesign, app, and dashboard project types.
13. Derive DESIGN_VARIANCE from project_type and brand_maturity.
14. Cap DESIGN_VARIANCE at 6 when accessibility is strict.
15. Derive MOTION_INTENSITY from the motion field.
16. Derive VISUAL_DENSITY from the density field.
17. Review conflicts before starting implementation.
18. Run `gogh-brain advise --vault <path> --brief <file>` after the brief is encoded.

## Best practice
- Encode the project brief before selecting skills EVIDENCE-BASED
- Use Taste Skill and Anthropic for direction-heavy public surfaces EVIDENCE-BASED
- Use UI UX Pro Max when brand maturity is absent or partial EVIDENCE-BASED
- Use MIFB when motion or tactile polish matters EVIDENCE-BASED
- Keep Impeccable in the stack when contracts and detection are useful EVIDENCE-BASED
- Add Vercel for strict accessibility or review-heavy project types EVIDENCE-BASED
- Lower design variance when accessibility is strict EVIDENCE-BASED
- Keep dashboard and app choices more restrained unless another note explicitly overrides the advisor PRACTITIONER
- Record conflict notes before implementation begins PRACTITIONER
- End selection with `gogh-brain advise` so the recommendation is reproducible EVIDENCE-BASED

## Pitfalls
Choosing by GitHub stars ignores mechanism fit.
Choosing every skill for every brief can create unnecessary conflict.
Skipping brand_maturity can overuse UI UX Pro Max style retrieval on mature brands.
Skipping motion classification can either omit MIFB or over-animate a static brief.
Skipping accessibility classification can omit Vercel where file:line audit matters.
Treating the advisor as a mutation command would exceed Gogh V1 boundaries.
Treating Taste Skill as in-scope for dashboards by default can conflict with Taste Skill's own scope note.
Treating UI UX Pro Max retrieval as a visual QA gate can overstate its mechanism.
Treating Impeccable detector output as Gogh output violates the product boundary.
Treating the flow as market-ready without audit would violate the brain operating rule.

## Sources
- Local script, scripts/render_stack_advisor.py, read 2026-07-07.
- Skill registry, references/skill-registry.json, generated 2026-07-07.
- Adapter manifest, references/adapter-manifest.json, read 2026-07-07.
- Claim pack ecosystem, references/claim-packs/claim-pack-ecosystem.md, generated 2026-07-07.
- Taste Skill SKILL.md, https://raw.githubusercontent.com/Leonxlnx/taste-skill/main/skills/taste-skill/SKILL.md, retrieved 2026-07-07.
- UI UX Pro Max README, https://github.com/nextlevelbuilder/ui-ux-pro-max-skill, retrieved 2026-07-07.
- Vercel SKILL.md, https://raw.githubusercontent.com/vercel-labs/agent-skills/main/skills/web-design-guidelines/SKILL.md, retrieved 2026-07-07.
- Impeccable README, https://github.com/pbakaus/impeccable, retrieved 2026-07-07.

## Related
- [[Design Skills Mechanism Map]] explains the mechanisms behind the branches.
- [[Full Stack Build Flow]] applies the selected skills to greenfield work.
- [[Audit Pipeline Flow]] applies the selected skills to release checks.
- [[Skill Stack Decision One-Pager]] compresses this flow into a deliverable.
- [[The Three Dials]] gives the Taste Skill dial background.
- [[UI UX Pro Max Repo|UI UX Pro Max (Skill)]] gives the retrieval source evidence.
- [[Impeccable (Toolchain)]] explains why Impeccable is always appended by the local advisor.
- [[Reception Sources|Vercel Web Design Guidelines]] gives audit-layer source context.
- [[Prompt Layer vs Toolchain]] explains when to harden a prompt into a toolchain.
- [[Install Surface and Format Portability]] explains install implications after selection.

## Next actions
- Keep the decision tree synced with `scripts/render_stack_advisor.py`.
- Add tests if advisor selection rules change.
- Re-run registry generation before changing coverage assumptions.
- Keep the final instruction as `run gogh-brain advise`.
- Record project-specific overrides in stack reports.

