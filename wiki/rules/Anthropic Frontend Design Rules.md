---
type: "rule"
title: "Anthropic Frontend Design Rules"
status: "developing"
created: "2026-07-07"
updated: "2026-07-07"
tags: ["gogh/frontend-design", "note/rule"]
domain: "frontend-design"
confidence: "evidence-based"
related: ["[[Anthropic Frontend Design Skill]]", "[[Distributional Convergence]]", "[[AI Slop]]", "[[Constraint Beats Coaxing]]", "[[Hero Discipline]]", "[[AI Tells (Forbidden Patterns)]]", "[[Scope and Context]]", "[[Required Audits]]"]
source_urls: ["https://raw.githubusercontent.com/anthropics/skills/main/skills/frontend-design/SKILL.md (retrieved 2026-07-07)", "https://claude.com/blog/improving-frontend-design-through-skills (retrieved 2026-07-07)", "https://prg.sh/ramblings/Why-Your-AI-Keeps-Building-the-Same-Purple-Gradient-Website (retrieved 2026-07-06)"]
sources: ["[[Anthropic Frontend Design Skill and Post]]", "[[Design Theory Sources]]"]
---

Anthropic Frontend Design Rules turn the official skill into an operational rule surface: commit to one grounded direction, avoid named template clusters, and critique the plan before code.

## What it is

This rule note distills the current Anthropic `frontend-design` capture.

It also preserves the launch blog's narrower rule surface for comparison.

The current `SKILL.md` is the controlling artifact for current behavior.

The launch post is evidence for the skill's original compact prompt.

The current skill is broader than the launch prompt.

The current skill centers studio-like judgment.

The launch blog centers four implementable frontend dimensions.

Those four launch dimensions are typography, animations or motion, backgrounds, and themes.

The current skill adds explicit subject grounding.

The current skill adds a two-pass planning and critique process.

The current skill adds a writing-in-design section.

The current skill adds named slop clusters beyond the launch blog's purple-gradient default.

## How it works

The first rule is committed aesthetic direction.

The agent must identify the concrete subject before designing.

The agent must identify the subject's audience.

The agent must identify the page's single job.

The hero must open with the most characteristic thing in the subject's world.

The hero can be a headline, image, animation, live demo, or interactive moment.

The hero should not default to a big stat with a gradient accent unless that is truly the best option.

Typography must carry personality.

Display and body faces must be paired deliberately.

The skill asks agents not to reuse the same type families across projects.

Structure must encode true information.

Numbered markers are valid only when sequence matters.

Motion must serve the subject.

One orchestrated motion moment usually lands harder than scattered effects.

Excess animation can make the design read as AI-generated.

Maximalist directions need elaborate execution.

Minimal directions need precision in spacing, type, and detail.

The current named default cluster one is warm cream near `#F4F1EA`, high-contrast serif display type, and terracotta accent.

The current named default cluster two is near-black with acid-green or vermilion accent.

The current named default cluster three is broadsheet layout with hairline rules, zero radius, and dense newspaper-like columns.

The current skill says all three clusters can be legitimate for some briefs.

The current skill says those clusters become defaults when they appear regardless of subject.

The launch blog's font bans include Inter, Roboto, Open Sans, Lato, Arial, and default system fonts in its examples.

The launch blog's preferred font examples include JetBrains Mono, Fira Code, Space Grotesk, Playfair Display, Crimson Pro, IBM Plex family, Source Sans 3, Bricolage Grotesque, and Newsreader.

The launch blog warns against purple gradients on white backgrounds.

The launch blog warns against predictable layouts and cookie-cutter patterns.

The launch blog says aesthetic guidance works best when it maps to frontend code.

The current skill requires a compact token plan with color, type, layout, and signature.

The current skill asks for 4-6 named hex values in the color plan.

The current skill requires critique against the brief before code.

The current skill requires critique again while building.

The current skill tells the agent to revise plan parts that read like a generic default.

The current skill says copy should make the interface easier to understand.

The current skill prefers active voice and consistent action names.

## Best practice

- Begin by stating the subject, audience, and single job before naming visual choices. EVIDENCE-BASED
- Pick one direction and derive color, type, layout, and signature from that direction. EVIDENCE-BASED
- Treat the cream `#F4F1EA`, near-black accent, and broadsheet clusters as defaults to avoid unless the brief asks for them. EVIDENCE-BASED
- Avoid Inter, Roboto, Open Sans, Lato, Arial, and default system fonts when applying the launch-era font guidance. EVIDENCE-BASED
- Put motion into one appropriate moment before adding scattered effects. EVIDENCE-BASED
- Use numbered markers only when order is information, not when decoration is needed. EVIDENCE-BASED
- Critique the plan before code and revise anything that could fit a similar prompt unchanged. EVIDENCE-BASED
- Pair these rules with later audits because the skill itself is not a deterministic checker. PRACTITIONER

## Pitfalls

Treating launch-era font examples as a complete current skill misses the newer studio-practice sections.

Treating the named default clusters as universal bans misses the brief-wins clause.

Treating a bold palette as sufficient misses the required subject grounding.

Adding many animations conflicts with the skill's warning about excess animation.

Using numbers as visual texture conflicts with the structure-as-information rule.

Writing generic marketing copy can make the interface feel templated even when the palette changes.

Skipping the pre-code critique removes the skill's main anti-default check.

Flattening this note into Taste Skill rules would hide the lighter Anthropic mechanism.

## Sources

Anthropic, https://raw.githubusercontent.com/anthropics/skills/main/skills/frontend-design/SKILL.md, retrieved 2026-07-07.

Anthropic, https://claude.com/blog/improving-frontend-design-through-skills, retrieved 2026-07-07.

Prg.sh, https://prg.sh/ramblings/Why-Your-AI-Keeps-Building-the-Same-Purple-Gradient-Website, retrieved 2026-07-06.

Local capture, `.raw/skills/anthropic-frontend-design/SKILL.md`, captured 2026-07-07.

Local capture, `.raw/skills/anthropic-frontend-design/blog-post.md`, captured 2026-07-07.

Claim pack, `references/claim-packs/claim-pack-anthropic-frontend-design.md`, generated 2026-07-07.

## Related

[[Anthropic Frontend Design Skill]] is the anchor that owns this rule note.

[[Distributional Convergence]] explains why repeated defaults appear.

[[AI Slop]] names the visual cluster these rules push against.

[[Constraint Beats Coaxing]] explains why a committed direction matters.

[[Hero Discipline]] overlaps with the skill's hero-as-thesis guidance.

[[AI Tells (Forbidden Patterns)]] is the stricter Taste Skill ban surface for common tells.

[[Scope and Context]] helps prevent applying design rules outside their intended surface.

[[Required Audits]] is where post-build verification belongs.

[[Anthropic Frontend Design Skill and Post]] records the capture and launch comparison.

## Next actions

Watch the upstream `SKILL.md` for changes to named default clusters.

Keep launch-blog rules separate from current `SKILL.md` rules.

Add detector mapping only if an upstream tool introduces machine-checkable Anthropic rules.

Use this rule note as the reference for Anthropic-specific style guidance in stack advice.
