---
type: "concept"
title: "Concentric Radii"
status: "developing"
created: "2026-07-07"
updated: "2026-07-07"
tags: ["gogh/mifb", "note/concept"]
domain: "mifb"
confidence: "evidence-based"
related: ["[[Make Interfaces Feel Better (Skill)]]", "[[MIFB Surface and Shadow Rules]]", "[[Optical Alignment]]", "[[Press Feedback and Hit Areas]]", "[[Interruptible Animation]]", "[[MIFB Review Checklist]]", "[[Jakub Krehel]]", "[[MIFB Repo and Skill File]]"]
source_urls: ["https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/skills/make-interfaces-feel-better/SKILL.md (retrieved 2026-07-07)", "https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/skills/make-interfaces-feel-better/surfaces.md (retrieved 2026-07-07)", "https://jakub.kr/writing/details-that-make-interfaces-feel-better (retrieved 2026-07-07)"]
sources: ["[[MIFB Repo and Skill File]]"]
---
Concentric Radii is the MIFB surface rule that nested rounded shapes should keep mathematically related curves so the interface does not feel subtly off.

## What it is
The MIFB claim pack states the rule as outer radius equals inner radius plus padding.
The surfaces capture states the same rule for nested rounded elements.
The surfaces capture gives a 20px outer radius, 12px inner radius, and 8px padding example.
The claim pack marks this rule evidence-based but single-source for independent corroboration.
The single-source caveat exists because the skill and article share Jakub Krehel as author.
The rule applies to nested surfaces that are visually close together.
The surfaces capture says padding larger than 24px should be treated as separate surfaces instead of strict radius math.
The concept is part of the MIFB surface and shadow family.
The rule is not a full design system by itself.
The rule is a local craft correction used after an interface direction already exists.
The MIFB skill calls mismatched nested radii one of the common causes of an interface feeling off.
The source ledger records the MIFB SKILL.md and supporting files as retrieved on 2026-07-07.

## How it works
Identify the outer container radius.
Identify the padding between outer and inner surfaces.
Set the inner radius to outer radius minus padding.
Use the equivalent expression outer radius equals inner radius plus padding.
Apply the math when the nested surfaces are close enough to be read as one object.
Do not force strict math when the layers are separated by large spacing.
Use the same radius relationship in buttons, cards, popovers, and framed media when they nest.
Check the visual curve, not only the utility class name.
Tailwind utility names can obscure the actual pixel values.
The surfaces capture shows same-radius nesting as the bad pattern.
Same-radius nesting makes the inner curve appear too round relative to the outer shell.
The rule pairs naturally with optical alignment because both address details that look wrong before users can name why.
The rule pairs naturally with image outlines because both protect edges on nested surfaces.
The rule should be checked in both light and dark surfaces when the edge contrast changes.

## Best practice
- Calculate inner radius as outer radius minus padding EVIDENCE-BASED
- Use strict concentric math for nested surfaces that are visually close EVIDENCE-BASED
- Treat layers with padding above 24px as separate surfaces EVIDENCE-BASED
- Check the actual pixel radii behind utility classes EVIDENCE-BASED
- Use one corner-radius system unless a documented rule explains the exception PRACTITIONER
- Pair radius review with the MIFB shadows and image outline pass EVIDENCE-BASED
- Use screenshots or visual inspection when a component still feels off PRACTITIONER
- Mark the rule as MIFB-specific instead of claiming universal measured evidence EVIDENCE-BASED
- Keep same-author article agreement labeled as consistency evidence EVIDENCE-BASED
- Avoid inventing new radius numbers beyond the captured examples EVIDENCE-BASED

## Pitfalls
Using `rounded-xl` on both parent and child can break concentricity.
Using a pill button inside a square card can break a page's shape system.
Mixing radii without a documented rule conflicts with Taste Skill's shape consistency lock.
Applying strict math across large gaps can make unrelated surfaces look artificially coupled.
Ignoring padding changes at responsive breakpoints can break the relationship on mobile.
Changing only one radius token can leave nested components visually stale.
Treating utility names as numbers can hide a mismatch.
Using border thickness as if it were padding can produce the wrong inner curve.
Forgetting dark-mode edges can make the curve relationship harder to inspect.
Calling the rule independently proven would exceed the claim pack's single-source caveat.

> [!key-insight]
> The MIFB rule is simple because the eye compares curves as one object: padding and radius need to agree.

## Sources
- MIFB SKILL.md, https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/skills/make-interfaces-feel-better/SKILL.md, retrieved 2026-07-07.
- MIFB surfaces reference, https://raw.githubusercontent.com/jakubkrehel/make-interfaces-feel-better/main/skills/make-interfaces-feel-better/surfaces.md, retrieved 2026-07-07.
- Jakub Krehel article, https://jakub.kr/writing/details-that-make-interfaces-feel-better, retrieved 2026-07-07.
- Local claim pack, references/claim-packs/claim-pack-make-interfaces-feel-better.md, generated 2026-07-07.
- Local source ledger, references/source-ledger.json, generated 2026-07-06 with MIFB entries retrieved 2026-07-07.
- Local source note, wiki/sources/MIFB Repo and Skill File.md, updated 2026-07-07.

## Related
- [[Make Interfaces Feel Better (Skill)]] is the skill anchor for this craft rule.
- [[MIFB Surface and Shadow Rules]] is the broader surface rule note.
- [[Optical Alignment]] covers another MIFB visual-correction pattern.
- [[Press Feedback and Hit Areas]] covers tactile interaction values from the same skill.
- [[Interruptible Animation]] covers the motion-side equivalent of this precise execution rule.
- [[MIFB Review Checklist]] is where this rule becomes a review item.
- [[Jakub Krehel]] provides author context for the article and skill.
- [[The Three Locks]] shows the related Taste Skill page-level shape lock.
- [[Impeccable Design Contracts]] shows where radius tokens can be persisted in a toolchain.
- [[MIFB Repo and Skill File]] is the provenance note for this source bundle.

## Next actions
- Use this concept in any stack advice that includes MIFB surface polish.
- Re-check the surfaces capture before adding new examples.
- Keep the 24px separation caveat visible in implementation notes.
- Do not promote the rule beyond evidence-based single-source status without independent evidence.
- Connect this concept to future visual examples only if the raw asset source is recorded.

