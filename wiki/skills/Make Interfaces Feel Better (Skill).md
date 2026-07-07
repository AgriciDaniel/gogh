---
type: "skill"
title: "Make Interfaces Feel Better (Skill)"
status: "developing"
created: "2026-07-07"
updated: "2026-07-07"
tags: ["gogh/mifb", "note/skill"]
domain: "mifb"
confidence: "evidence-based"
related: ["[[MIFB Typography and Numbers Rules]]", "[[MIFB Surface and Shadow Rules]]", "[[MIFB Motion and Feedback Rules]]", "[[MIFB Performance Rules]]", "[[MIFB Review Checklist]]", "[[Optical Alignment]]", "[[Jakub Krehel]]", "[[MIFB Repo and Skill File]]"]
source_urls: ["https://github.com/jakubkrehel/make-interfaces-feel-better (retrieved 2026-07-07)", "https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/skills/make-interfaces-feel-better/SKILL.md (retrieved 2026-07-07)", "https://jakub.kr/writing/details-that-make-interfaces-feel-better (retrieved 2026-07-07)"]
sources: ["[[MIFB Repo and Skill File]]"]
---
Make Interfaces Feel Better is the MIFB micro-interaction execution skill for turning small interface details into visible polish.

## What it is

- Make Interfaces Feel Better is an Agent Skill named `make-interfaces-feel-better`.
- Jakub Krehel is the author identified by the MIFB claim pack and article extract.
- The mechanism category is micro-interaction execution inside the Gogh stack.
- The captured README says the skill is based on Krehel's article `Details that make interfaces feel better`.
- The repository was created on 2026-03-13, according to the claim pack.
- The repository had 2,241 GitHub stars as of 2026-07-07, according to the source ledger.
- The skills.sh registry reported 39.2K installs as of 2026-07-07, according to the ecosystem claim pack.
- The captured SKILL.md frontmatter did not include a version field as retrieved on 2026-07-07.
- The README declares MIT as the license.
- The source ledger reports no detected LICENSE file as of 2026-07-07.
- The safest license wording is README-declared MIT with a missing-standard-license caveat.
- The install command in the captured README is `npx skills add jakubkrehel/make-interfaces-feel-better`.
- The long install form in the claim pack is `npx skills add https://github.com/jakubkrehel/make-interfaces-feel-better --skill make-interfaces-feel-better`.
- The manual invocation in the captured README is `/make-interfaces-feel-better`.
- The skill targets UI components, frontend code review, animations, hover states, shadows, borders, typography, micro-interactions, enter animations, exit animations, and visual detail work.
- The skill is a craft layer and not a full aesthetic-direction framework.
- The claim pack says MIFB has no dials, no pre-flight gate, and no aesthetic-direction step.
- In the stack, reach for it after direction exists and detailed interface execution matters.

## How it works

- The SKILL.md loads a compact core rule set and points to four supporting files on demand.
- The typography file covers text wrapping, font smoothing, and tabular numbers.
- The surfaces file covers radius math, optical alignment, shadows, image outlines, and hit areas.
- The animations file covers interruptible transitions, split enter animations, subtle exits, icon swaps, and press feedback.
- The performance file covers transition specificity and restrained `will-change` use.
- The skill's quick reference maps each category to the kind of detail work it handles.
- The core principles include concentric border radius.
- The core principles include optical over geometric alignment.
- The core principles include shadows over borders.
- The core principles include interruptible animations.
- The core principles include split and stagger enter animations.
- The core principles include subtle exit animations.
- The core principles include contextual icon animations.
- The core principles include root font smoothing.
- The core principles include tabular numbers.
- The core principles include text wrapping.
- The core principles include image outlines.
- The core principles include scale on press.
- The core principles include skipping default page-load animation.
- The core principles include avoiding `transition: all`.
- The core principles include restrained `will-change`.
- The core principles include minimum hit areas.
- The review format requires markdown tables with Before and After columns grouped by principle.
- The captured checklist has 14 review items.

## Best practice

- Use MIFB when an existing direction needs sharper interface details. EVIDENCE-BASED
- Use MIFB during component implementation, frontend review, animation work, and polish passes. EVIDENCE-BASED
- Pair MIFB with a direction-setting skill when the page still lacks a brand or aesthetic stance. EVIDENCE-BASED
- Load the typography reference when line wrapping, macOS rendering, or dynamic numerals are involved. EVIDENCE-BASED
- Load the surfaces reference when nested radii, image edges, shadows, icons, or hit areas are involved. EVIDENCE-BASED
- Load the animations reference when state changes, icon swaps, enter motion, exit motion, or press feedback are involved. EVIDENCE-BASED
- Load the performance reference before adding broad transitions or GPU hints. EVIDENCE-BASED
- Report MIFB review changes in Before and After tables grouped by principle. EVIDENCE-BASED
- State repository metrics only as dated observations from the 2026-07-07 source pass. EVIDENCE-BASED
- State the license as README-declared MIT with the missing LICENSE caveat. EVIDENCE-BASED

## Pitfalls

- MIFB does not choose an aesthetic direction for a project.
- MIFB does not provide the three dials used by Taste Skill.
- MIFB does not provide a blocking pre-flight release gate.
- MIFB rule values are often single-source because the skill and article share Jakub Krehel as author.
- The README license statement and GitHub license detection do not fully align in the 2026-07-07 evidence.
- The skills.sh install count is registry-reported and should not be treated as independently audited.
- The absence of a version field in the captured SKILL.md should not be converted into a version number.
- The skill should not be used as a replacement for accessibility review, product scope, or brand preservation.

> [!key-insight]
> MIFB is most useful when design intent already exists and the interface still feels imprecise.

## Sources

- GitHub, https://github.com/jakubkrehel/make-interfaces-feel-better, retrieved 2026-07-07.
- Raw GitHub SKILL.md, https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/skills/make-interfaces-feel-better/SKILL.md, retrieved 2026-07-07.
- Raw GitHub README, https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/README.md, retrieved 2026-07-07.
- Jakub Krehel, https://jakub.kr/writing/details-that-make-interfaces-feel-better, retrieved 2026-07-07.
- Local MIFB claim pack, references/claim-packs/claim-pack-make-interfaces-feel-better.md, generated 2026-07-07.
- Local ecosystem claim pack, references/claim-packs/claim-pack-ecosystem.md, generated 2026-07-07.
- Local source ledger, references/source-ledger.json, generated 2026-07-06 and containing MIFB entries retrieved 2026-07-07.

## Related

- Rules, [[MIFB Typography and Numbers Rules]]: covers the text rendering part of the skill.
- Rules, [[MIFB Surface and Shadow Rules]]: covers radius, shadow, outline, and surface depth details.
- Rules, [[MIFB Motion and Feedback Rules]]: covers the skill's animation and tactile feedback values.
- Rules, [[MIFB Performance Rules]]: covers transition specificity, GPU hints, and hit area checks.
- Audits, [[MIFB Review Checklist]]: turns the skill into a repeatable review pass.
- Sources, [[MIFB Repo and Skill File]]: holds the raw file provenance and license caveat.
- Entities, [[Jakub Krehel]]: identifies the skill author and article publisher context.
- Concepts, [[Optical Alignment]]: expands the skill's optical-over-geometric alignment rule.
- Concepts, [[MIFB Surface and Shadow Rules|Concentric Radii]]: carries the local rule details until the S5g concept note lands.
- Concepts, [[MIFB Motion and Feedback Rules|Interruptible Animation]]: carries the local transition rule details until the S5g concept note lands.
- Concepts, [[MIFB Performance Rules|Press Feedback and Hit Areas]]: carries the local hit area details until the S5g concept note lands.
- Flows, [[Install and Load]]: provides the broader install workflow used by the stack.
- Flows, [[Greenfield Build (Prompt 1)]]: shows where MIFB fits after direction-setting work.
- Flows, [[Audit-First Redesign (Prompt 2)]]: shows where MIFB can support redesign review.

## Next actions

- Re-check the repository metadata before restating stars or license status.
- Re-check skills.sh before restating install counts.
- Re-check the captured SKILL.md if the repo changes after 2026-07-07.
- Pair this anchor with the four rule notes during stack selection.
- Use the checklist note when applying MIFB as a review pass.
- Keep MIFB positioned as execution polish rather than taste direction.
- Keep the missing LICENSE caveat visible in source and skill summaries.
- Route future MIFB changes through [[Brain Refresh Flow]] when that flow note is integrated.
