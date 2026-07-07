# Raw research capture — Official site (tasteskill.dev)

> Immutable source capture. Retrieved 2026-07-06 by parallel research agent. Do not edit; synthesize into wiki notes instead.

## Positioning
- Title/hero: "Taste Skill — The Anti-Slop Frontend Framework for AI Agents"
- Tagline: "Less slop, designs pop."
- Description: "Open-source skill files that stop Cursor, Claude Code, Codex, Gemini CLI, v0, Lovable, and more from generating generic frontends."
- GitHub one-liner: "Taste-Skill (High-Agency Frontend) — gives your AI good taste. stops the AI from generating boring, generic, 'slop'."
- "One install. Cursor, Claude Code, Codex, Gemini CLI, v0, Lovable, OpenCode and more. Taste Skill plugs into any tool that supports SKILL.md files."
- License: MIT, free, open source (MIT file added 2026-04-28). Framework-agnostic: React, Vue, Svelte, Astro, any stack.
- Compatible agents: Codex, Claude Code, Cursor, OpenCode, Gemini CLI, AI Studio, v0, Lovable.

## Guide sections: 1 Setup → 2 Creating a new website → 3 Redesigning an existing website → 4 Quick reminders
Setup: "Load the skill once at the top of your session, then use one of the two prompts below."
Install: `npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend"`

### Prompt 1 — Greenfield (verbatim)
"I have loaded tasteskill v2 (experimental) as my only source of design rules.
Brief:
- Page kind: <landing / portfolio / marketing>
- Product: <name and one-line description>
- Audience: <who reads this, concrete adjectives>
- Vibe words: <2 to 4 concrete adjectives, e.g. "minimalist, editorial, restrained">
- References: <real URLs or product names that anchor the aesthetic>
- Avoid: <explicit slop patterns the brief should NOT default to>
Step 1. Declare your design read in one sentence and the three dial values with one-line reasoning each. Stop.
Step 2 (after my OK). Ship a single Next.js page with at least 8 sections. Pick the sections that actually fit the product. At least 4 different layout families across the page. Use real images (gen-tool first, then Picsum-seed). Lock one theme for the whole page.
Step 3. Run in writing:
- Em-dash audit (zero em-dashes U+2014 or en-dashes U+2013 anywhere)
- Pre-Flight Check (Section 14, every box marked Pass or Fail with one-line justification)
- Section-Layout-Repetition audit (list each section's layout family)
- Hero discipline audit (headline lines, subtext words, CTA visibility)
Any Fail blocks completion."

### Prompt 2 — Redesign (verbatim)
"I have loaded tasteskill v2 (experimental) as my only source of design rules.
Brief:
- Site: <URL or repo path>
- Mode: <preserve brand / overhaul / unsure>
- Audience: <who reads this>
- What works today: <2 to 3 specifics you want kept>
- What is broken today: <2 to 3 specifics you want fixed>
- SEO constraint: <which routes, headings, or anchors must not change>
Step 1. Run the Section 11 audit (Section 11.B in the skill):
- Brand tokens currently in use (primary, accent, type stack, radii)
- Information architecture (page tree, nav, conversion paths)
- Patterns to preserve (signature interactions, recognisable hero, copy voice)
- Patterns to retire (slop tells, broken layouts, dead links)
- Inferred dial reading of the current site (DESIGN_VARIANCE, MOTION_INTENSITY, VISUAL_DENSITY)
- SEO baseline (ranking pages, titles, anchors)
Post the audit in writing. Stop.
Step 2 (after my OK). Declare the mode (Preserve, Overhaul, or Greenfield-with-content-preserved) and which modernisation levers from Section 11.D you will apply, in priority order. Stop.
Step 3 (after my OK). Implement the changes. Keep URL structure, primary nav labels, form field names, brand logo, and legal copy unchanged unless I explicitly approve a change.
Step 4. Run in writing:
- Em-dash audit
- Pre-Flight Check (Section 14)
- Preservation audit: list every URL, nav label, form field, and anchor changed. Should be empty unless I approved.
- Brand fidelity audit: confirm the existing brand accent color, type stack, and logo treatment survived the redesign.
Any Fail blocks completion."

Build rules: single Next.js page, >=8 sections fit to product, >=4 layout families, real images (gen-tool first then Picsum-seed), one theme locked.
Section 11.B = redesign audit; 11.D = modernisation levers. Section 14 = hard pre-flight check, every box Pass/Fail w/ justification; must honestly pass before ship. (neodrop.ai calls it "60-item"; not stated on-site.)

### Quick reminders (verbatim full list)
- Zero em-dashes anywhere. Hyphen only.
- Hero headline max 2 lines. Subtext max 20 words. CTA visible without scroll.
- Navigation max 80 pixels tall, one line at desktop.
- Bento grid: N items equals N cells. No empty cells.
- One theme for the whole page (no light/dark flips mid-page).
- Real images, no div-based fake screenshots, no hand-rolled SVG illustrations.
- No section-numbering eyebrows, no version labels in hero, no scroll cues, no locale strips, no decorative status dots.
- "If MOTION_INTENSITY is greater than 4, the page actually animates. Otherwise drop the dial."

## Exact thresholds
Hero headline max 2 lines (desktop). Subtext max 20 words (docs also "twenty words and four lines"). CTA visible without scroll. Nav max 80px, single line desktop. Bento N items = N cells. One theme per page. >=4 layout families/page. No three-equal-card rows by default. Real images only (gen-tool first, then Picsum-seed). Em/en-dash: zero anywhere, hyphen only.

## Anti-slop bans (§9)
No section-numbering eyebrows; no version labels in hero (unless launch brief); no scroll cues; no locale strips; no decorative status dots; no pills overlaid on images; no AI-purple / mesh-blob gradient defaults.

## Animation
If MOTION_INTENSITY > 4 the page actually animates, else drop the dial. No hand-rolled scroll listeners; required: Motion useScroll, GSAP ScrollTrigger, IntersectionObserver, or CSS scroll-driven animations. §5 canonical GSAP skeletons (sticky-stack, horizontal-pan, scroll-reveal stagger) w/ forbidden patterns.

## Three Locks (docs)
1. Color Consistency Lock — single accent throughout page.
2. Shape Consistency Lock — one corner-radius/radii system per page.
3. Page Theme Lock — light/dark/auto selected once at page level.

## Dark mode protocol (§8)
WCAG AA contrast, hierarchy parity, brand fidelity in both themes. Off-black and off-white, never pure values. Dual-mode by default.

## Stack
Tailwind v4; Motion recommended; specific icon libraries only.

## Three Dials (llms.txt, all 1–10)
- DESIGN_VARIANCE (1–10): layout centered → experimental.
- MOTION_INTENSITY (1–10): simple hover → complex scroll-triggered; animate only if > 4.
- VISUAL_DENSITY (1–10): spacing luxury → dense dashboards.
No published defaults; agent infers from brief. Guide names dials; only llms.txt states scales.

## Docs install commands
- Default v2: `npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend"`
- Legacy v1: `npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend-v1"`
- Full bundle: `npx skills add Leonxlnx/taste-skill`
- Into Codex: `npx skills add Leonxlnx/taste-skill -a codex`
v2 reads the brief first; infers layout variance/motion/density from cues (minimalist, editorial, SaaS, portfolio). Design-system map recognizes: Material, Fluent, Carbon, Polaris, Atlassian, Primer, GOV.UK, USWDS, Bootstrap, Radix, shadcn, Tailwind. SKILL.md fully editable in project root.

## Changelog
v2 experimental — May 2026 (latest): retitled "tasteskill: Anti-Slop Frontend Skill"; same install cmd now v2; §0 Brief inference; §2 brief→design-system map; §8 dark-mode protocol; §11 redesign protocol; §12 block library schema; §14 hard pre-flight; §9 em-dash ban + prohibitions; color/shape/page-theme locks; hero + nav discipline; §5 GSAP skeletons. v1 preserved. Stack Tailwind v4 + Motion.
v1.2 — May 2026: imagegen-frontend-web hero composition, one horizontal ref image/section, brief-adaptation cues, background modes + gradient discipline, concept spine, second-read cues.
v1.1 — Apr 2026: README shields; gpt-tasteskill stricter GPT rules (2026-04-16); images-taste-skill→image-to-code-skill (2026-04-25); imagegen web/mobile; brandkit image boards (2026-04-25); MIT license (2026-04-28); npx skills add documented.
v1.0 — Mar 2026: migrated to npx skills layout (2026-03-20); stitch-skill (03-20); brutalist-skill beta (03-19); minimalist-skill (03-17); soft-skill (03-15→16); core split into multiple skills (03-01); seven implementation skills by end of March.
v0.1 — Feb 2026: single primary SKILL.md; three-dial system, creative arsenal, anti-slop enforcement.

## Blog
Embedded X threads by @LexnLin (402 to fetch). URLs: x.com/LexnLin/status/2050179260892029179, /2048791596137632126, /2047088354164982155, /2036579702471598543.

## 13 skills (name + verbatim one-liner)
1. taste-skill (v2 exp) — "Reads the brief, infers the right design direction, and ships interfaces that do not look templated."
2. taste-skill-v1 — "The original v1 of taste-skill, preserved for projects depending on its exact behavior."
3. gpt-tasteskill — "Stricter variant for GPT and Codex models with stronger layout variance and motion direction."
4. image-to-code-skill — "Generates design references first, analyzes them deeply, then implements the frontend closely."
5. redesign-skill — "For existing projects that need a proper visual audit and cleaner redesign pass."
6. soft-skill — "For calm, expensive-looking interfaces with softer contrast, whitespace, and smooth motion."
7. output-skill — "Keeps outputs complete. Prevents placeholders, skipped sections, and half-finished work."
8. minimalist-skill — "Cleaner editorial product UI with restrained color, sharp structure, and tighter hierarchy."
9. brutalist-skill — "Harder mechanical visual language: Swiss typography, raw structure, and sharper contrast."
10. stitch-skill — "Google Stitch-compatible semantic design rules with an extra DESIGN.md export format."
11. imagegen-frontend-web — "Premium website reference images: strong art direction, typography, spacing, and anti-slop discipline."
12. imagegen-frontend-mobile — "Premium mobile screen concepts and flows with clean hierarchy and multi-screen consistency."
13. brandkit — "Brand-kit overview images with logo concepts, color systems, typography, and mockups."

## v2 feature blocks (home, verbatim)
§0 Brief inference — "The agent reads the room before generating: industry, audience, mood, motion depth, layout family."
§2 Brief to design system map — "When to reach for Material, Fluent, Carbon, Polaris, Atlassian, Primer, GOV.UK, USWDS, Bootstrap, Radix, shadcn, Tailwind official, versus native CSS."
§8 Dark mode protocol — "Dual-mode by default. Contrast and hierarchy parity across themes."
§11 Redesign protocol — "Audit-first on existing projects. Preservation rules and explicit modernisation levers."
§12 Block library schema — "Contract for iterative block additions so the library stays coherent."
§14 Hard pre-flight check — "Every checkbox must honestly pass before the agent ships output."

## People / projects
Built by Leon Lin (@lexnlin) + blueemi (@blueemi99). © 2026 Taste Skill. GitHub github.com/Leonxlnx/taste-skill. Sponsor github.com/sponsors/Leonxlnx (14 sponsors). Contact: hello@tasteskill.dev (per snippet, unverified). Projects built with it: Floria (floria-landing-page.vercel.app), Collective OS (collectiveos.vercel.app). No public roadmap/Discord.

## Sources
tasteskill.dev/ , /guide?view=full , /guide , /docs , /changelog , /blog , /llms.txt ; github.com/Leonxlnx/taste-skill ; x.com/LexnLin/status/{2050179260892029179,2048791596137632126,2047088354164982155,2036579702471598543} ; neodrop.ai/post/s3mGLbLqiNd (secondary)
