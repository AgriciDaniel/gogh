# Anthropic Frontend Design Skill Extract
Captured: 2026-07-07
Sources: https://claude.com/blog/improving-frontend-design-through-skills (retrieved 2026-07-07); https://raw.githubusercontent.com/anthropics/skills/main/skills/frontend-design/SKILL.md (retrieved 2026-07-07); https://snyk.io/articles/top-claude-skills-ui-ux-engineers/ (retrieved 2026-07-07); https://composio.dev/content/top-design-skills (retrieved 2026-07-07); https://impeccable.style (retrieved 2026-07-07)
Source type: official

## Blog Post: Improving Frontend Design Through Skills
- Published 2025-11-12 on claude.com, category Claude Code, 5-minute read.
- Authors: Prithvi Rajasekaran, Justin Wei, Alexander Bricken (Applied AI team), with Molly Vorwerck and Ryan Whitehead.
- Problem name: "distributional convergence". Models predict tokens from training-data patterns where safe design choices dominate web data.
- Resulting default look: Inter fonts, purple gradients on white backgrounds, minimal animations.
- Consequence per the blog: interfaces immediately recognizable and dismissible as AI-generated; brand identity and creative distinction lost.
- Quote: "Without direction, Claude samples from this high-probability center" (Anthropic blog).
- Skill mechanics: roughly 400 tokens of markdown, stored in a designated skills directory, loaded just-in-time.
- Claude autonomously loads the skill when it detects frontend-building work; no permanent context overhead.
- Stated design goal: resolve the tension between steerability and token efficiency by delivering specialized context on demand.

## What the Skill Enforced at Launch (per the blog)
- Typography: avoid Inter, Roboto, Open Sans, Lato.
- Typography: prefer distinctive faces such as JetBrains Mono, Playfair Display, Bricolage Grotesque, IBM Plex family.
- Color/theme: commit to one cohesive aesthetic; define CSS variables; dominant colors with sharp accents over timid palettes.
- Motion: CSS-only for HTML outputs; Motion library for React; prioritize high-impact orchestrated moments over scattered effects.
- Backgrounds: build atmospheric depth with gradients, patterns, and contextual effects instead of flat solid colors.
- Anti-slop rules: reject generic font families, cliched purple gradients, cookie-cutter layouts, predictable component shapes.

## Companion Skill and Demos (same blog)
- web-artifacts-builder: multi-file React apps with Tailwind CSS and shadcn/ui; setup scripts automate boilerplate; Parcel bundles to a single-file artifact.
- Whiteboard demo: without the skill, basic UI; with it, shape and text drawing tools appeared.
- Task manager demo: gained form components with category and due-date assignment.
- Evaluation is qualitative only: before/after screenshots (SaaS landing page, blog layout, admin dashboard) across typography, color cohesion, motion, background depth.
- No quantitative metrics (user satisfaction scores, benchmarks) published in the post.

## Current SKILL.md (anthropics/skills, retrieved 2026-07-07)
- Frontmatter: name `frontend-design`; description covers distinctive, intentional visual design for new or reshaped UI; license via LICENSE.txt.
- Framing has evolved from launch: design as studio practice; make deliberate, opinionated palette/typography/layout choices specific to the brief.
- Mandate: take one real aesthetic risk you can justify.
- Process step 1: name the concrete subject, its audience, and the page's single job before designing.
- Process step 2: two passes; a compact design plan (color, type, layout, signature element), then a critique against the brief before writing code.
- Design thesis rule: open with the most characteristic thing in the subject's world.
- Typography: pair display and body faces deliberately with a clear type scale; do not repeat the same families across projects.
- Structure: numbered markers only when order genuinely carries information; interrogate decorative choices.
- Motion: orchestrated moments serve the subject. Quote: "extra animation contributes to the feeling that the design is AI-generated" (SKILL.md).
- Named anti-slop clusters (three generic defaults to avoid):
  1. Cream background #F4F1EA with serif display type and terracotta accents.
  2. Near-black with acid-green or vermilion accents.
  3. Broadsheet layouts with hairline rules and dense columns.
- Copy rules: words exist "to make it easier to understand"; active voice, plain language, specific descriptions, never vague or apologetic.

## Install Base
- 277,000+ installs as of March 2026: figure circulates via Composio and paddo.dev. Correction 2026-07-07: direct fetches of Snyk's "Top 8 Claude Skills for UI/UX Engineers" contain no install counts at all (zero occurrences of the figure), so the common Snyk attribution is wrong. The skills.sh registry showed 634.0K installs on 2026-07-07; 277k is plausible as a stale March snapshot with an unstated measurement basis.
- Snyk ranks it #1 of 8; its table shows 65,847 stars for the anthropics/skills repo.

## Third-Party Positioning
- Snyk: the other seven ranked skills "complement rather than compete"; Anthropic covers aesthetics, Vercel guidelines cover correctness, UI/UX Pro Max covers design-system intelligence.
- Composio (2026-05-05): keeps frontend-design at #1 but calls the root issue "a training-data problem, not a design philosophy".
- Impeccable's homepage title positions it as the missing upgrade to Anthropic's built-in design skill (impeccable.style page title in search results, retrieved 2026-07-07).
- UX Planet (Nick Babich) repeats Anthropic's convergence framing when explaining why unskilled Claude Code output looks identical across users.
