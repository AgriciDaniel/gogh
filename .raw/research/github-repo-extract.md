# Raw research capture — GitHub repo (Leonxlnx/taste-skill)

> Immutable source capture. Retrieved 2026-07-06 by parallel research agent from GitHub API + raw files. Do not edit; synthesize into wiki notes.

## Metadata
- Full name: `Leonxlnx/taste-skill` (case-insensitive alias leonxlnx/…)
- GitHub description: "Taste-Skill - gives your AI good taste. stops the AI from generating boring, generic slop"
- README tagline: "The Anti-Slop Frontend Framework for AI Agents"
- Homepage: https://tasteskill.dev
- Stars: 58,435 · Forks: 3,985 · Watchers: 58,435 · Open issues: 42
- Primary language: JavaScript (only the README asset scripts)
- License: MIT, © 2026 Leonxlnx
- Created 2026-02-19 · Updated 2026-07-06 · Pushed 2026-07-04 · Size 4,677 KB · Default branch main
- Releases/Tags: NONE (versioning via CHANGELOG.md only). plugin.json self-labels version 1.0.0 (stale) while content is v2-experimental.
- Topics: agent, ai, coding, lowcode, nocode, skill, skills, vibecoding, claude, claude-code, codex, design, frontend
- Funding: GitHub Sponsors Leonxlnx. Sponsors incl. Emil Kowalski / animations.dev, Vercel OSS Program.
- Contact: X @lexnlin, @blueemi99; hello@tasteskill.dev

## File tree (main)
.claude-plugin/{marketplace.json, plugin.json}; .github/{FUNDING.yml, copilot-instructions.md (Anti-Slop Manifesto)}; CHANGELOG.md; LICENSE (MIT); README.md; assets/…; examples/floria-{top,bottom,full}.webp; research/{README.md, laziness/{README, findings/{empirical-results,references}, remediation/{architectural-patterns,parameter-tuning,prompt-engineering,reference-prompts}, root-causes/{cognitive-shortcuts,output-limits,rlhf-and-compute,training-data-bias}}}; scripts/*.mjs (asset processing only); skill.sh (bash registry of 13 skills); skills/{llms.txt, taste-skill/SKILL.md (CANONICAL v2, 1207 lines), taste-skill-v1/SKILL.md, gpt-tasteskill, image-to-code-skill, imagegen-frontend-web, imagegen-frontend-mobile, brandkit, minimalist-skill, brutalist-skill, soft-skill, output-skill, redesign-skill, stitch-skill/{SKILL.md,DESIGN.md}}.

## Canonical SKILL.md (skills/taste-skill/SKILL.md)
Frontmatter name: `design-taste-frontend`. Description: "Anti-slop frontend skill for landing pages, portfolios, and redesigns. The agent reads the brief, infers the right design direction, and ships interfaces that do not look templated. Real design systems when applicable, audit-first on redesigns, strict pre-flight check."
Title: "tasteskill: Anti-Slop Frontend Skill." Scope: "Landing pages, portfolios, and redesigns. Not dashboards, not data tables, not multi-step product UI. Every rule below is contextual. None of it fires automatically."

### §0 Brief Inference ("Read the Room")
Signals: page kind, vibe words, reference signals, audience ("audience picks the aesthetic, not your taste"), existing brand assets, quiet constraints (OVERRIDE aesthetics). 0.B output one-line Design Read: "Reading this as: <page kind> for <audience>, with a <vibe> language, leaning toward <design system/aesthetic family>." 0.C if ambiguous ask EXACTLY ONE question. 0.D Anti-Default: no AI-purple gradients, centered hero over dark mesh, three equal feature cards, generic glassmorphism, infinite-loop micro-animations, Inter + slate-900.

### §1 THE THREE DIALS — baseline 8 / 6 / 4
- DESIGN_VARIANCE: 8 (1=Perfect Symmetry, 10=Artsy Chaos)
- MOTION_INTENSITY: 6 (1=Static, 10=Cinematic/Physics)
- VISUAL_DENSITY: 4 (1=Art Gallery/Airy, 10=Cockpit/Packed Data)
Overrides conversational, never by editing file.
1.A Inference table: minimalist/editorial/Linear 5-6 / 3-4 / 2-3; premium consumer/Apple/luxury 7-8 / 5-7 / 3-4; playful/Dribbble/Awwwards/agency 9-10 / 8-10 / 3-4; landing/portfolio default 7-9 / 6-8 / 3-5; trust-first/public-sector/a11y 3-4 / 2-3 / 4-5; redesign-preserve match/+1/match; redesign-overhaul +2/+2/match.
1.B Presets: Landing SaaS 7/6/4; Landing Agency 9/8/3; Landing Premium 7/6/3; Portfolio Designer 8/7/3; Portfolio Developer 6/5/4; Editorial/Blog 6/4/3; Public-sector 3/2/5.
§7 technical bands: VARIANCE 1-3 predictable/4-7 offset/8-10 asymmetric (mobile 4-10 collapse single-col <768px). MOTION 1-3 static/4-7 fluid CSS (transition all 0.3s cubic-bezier(0.16,1,0.3,1))/8-10 scroll-driven GSAP (window scroll listener HARD BAN). DENSITY 1-3 art gallery py-32..py-48 / 4-7 daily app py-16..py-24 / 8-10 cockpit 1px lines, font-mono for numbers.

### §2 Brief → Design System Map
2.A official packages: Microsoft→@fluentui/react-components|web-components; Material→@material/web + M3; IBM→@carbon/react+@carbon/styles; Shopify→Polaris; Atlassian→@atlaskit/*; GitHub→@primer/css | @primer/react-brand; UK gov→govuk-frontend; US gov→uswds; local MVP→Bootstrap 5.3; accessible React→@radix-ui/themes; owned comps→shadcn/ui; Tailwind SaaS→Tailwind v4 + dark:. Honesty rule: install official pkg, don't recreate CSS, don't override 90% tokens. ONE system per project.
2.B no official pkg (native CSS+Tailwind): glassmorphism, bento, brutalism, editorial, dark tech, aurora/mesh, kinetic type, Apple Liquid Glass ("no official liquid-glass.css" — label approximation).

### §3 Default Architecture
React/Next.js, RSC default; interactivity in 'use client' leaves. Tailwind v4 default (use @tailwindcss/postcss). Animation Motion (import { motion } from "motion/react"; framer-motion legacy alias). Fonts next/font or self-host @font-face + font-display:swap; never <link> Google Fonts in prod. STATE: never useState for continuous input — use useMotionValue/useTransform/useScroll. Icons priority @phosphor-icons/react, hugeicons-react, @radix-ui/react-icons, @tabler/icons-react; lucide-react discouraged; never hand-roll SVG icons; one family/project; standardize strokeWidth (1.5 or 2.0). Emoji discouraged. Breakpoints sm640/md768/lg1024/xl1280/2xl1536; contain max-w-[1400px] mx-auto or max-w-7xl; never h-screen → min-h-[100dvh]; Grid over flex-math (never w-[calc(33%-1rem)]). Verify deps vs package.json.

### §4 Design Engineering Directives (thresholds)
4.1 Type: display text-4xl md:text-6xl tracking-tighter leading-none; body text-base text-gray-600 leading-relaxed max-w-[65ch]. Inter discouraged (prefer Geist/Outfit/Cabinet Grotesk/Satoshi). SERIF DISCIPLINE — "creative brief = serif" is "the single most-tested AI tell"; serif only if brand names one OR genuinely editorial/luxury/heritage. Fraunces + Instrument_Serif BANNED as defaults. Emphasis via italic/bold SAME font. Italic descender clearance (mandatory): y g j p q need leading-[1.1] min + pb-1/mb-1.
4.2 Color: MAX 1 accent, saturation <80% default. THE LILA RULE — AI purple/blue glow discouraged; neutral bases (Zinc/Slate/Stone) + one accent. Color Consistency Lock (one accent whole page). PREMIUM-CONSUMER PALETTE BAN ("second-most-recurring AI-tell") — beige/cream + brass/clay/oxblood/ochre + espresso banned. Banned hex bg: #f5f1ea #f7f5f1 #fbf8f1 #efeae0 #ece6db #faf7f1 #e8dfcb; accents #b08947 #b6553a #9a2436 #9c6e2a #bc7c3a #7d5621; text #1a1714 #1a1814 #1b1814. Rotate alternatives (Cold Luxury, Forest, Black-and-Tan, Cobalt+Cream, Terracotta+Slate, Olive+Brick+Paper, mono+pop); don't ship same warm-craft palette twice.
4.3 Layout: centered hero avoided when VARIANCE>4 (split-screen/asymmetric/scroll-pinned).
4.4 Materiality: cards only when elevation = real hierarchy; VISUAL_DENSITY>7 generic card containers banned; Shape Consistency Lock (one radius scale/page).
4.5 Interactive states: Button Contrast Check WCAG AA 4.5:1 body / 3:1 large 18px+; white-on-white banned. CTA Button Wrap Ban: one line desktop, 3 words max primary (ideally 1-2), wrapped CTA = Fail. No Duplicate CTA Intent (same intent = Fail). Form Contrast Check WCAG AA all parts. 4.6 label ABOVE input, error BELOW, gap-2; no placeholder-as-label ever.
4.7 Layout Discipline (hard rules): Hero MUST fit initial viewport — headline max 2 lines desktop, subtext max 20 words AND 3-4 lines, CTAs no-scroll. Hero font default text-4xl md:text-5xl lg:text-6xl; text-6xl md:text-7xl only 3-5 word headlines. "4-line hero headline is always a font-size error." HERO TOP PADDING CAP pt-24 (~6rem) desktop. HERO STACK max 4 text elements (eyebrow/brand-strip/neither, headline, subtext, CTAs 1 primary+max1 secondary). Banned in hero: tagline below CTAs, trust micro-strip, pricing teaser, feature bullets, avatar row. "Used by/Trusted by" logo wall UNDER hero. Nav single line desktop, ≤80px, default 64-72px. Bento Cell Count: exactly N cells for N items, no empty. Section-Layout-Repetition Ban: each family ≤once; 8 sections → ≥4 families. ZIGZAG CAP: max 2 consecutive image+text splits, 3rd = Fail. EYEBROW RESTRAINT ("#1 violated rule"): max 1 eyebrow per 3 sections, hero=1; if count > ceil(sectionCount/3) → Fail. SPLIT-HEADER BAN (left headline+right explainer) → stack vertical max-width 65ch. Bento bg diversity ≥2-3 cells vary. Mobile collapse explicit per section <768px.
4.8 Image strategy priority: (1) image-gen tool first (MUST if available), (2) real web images picsum.photos/seed/{seed}/{w}/{h}, (3) last resort labeled placeholder + tell user. Even minimalist ≥2-3 images. Real logos via Simple Icons cdn.simpleicons.org/{slug}/ffffff or devicon; LOGO-ONLY (no category labels). Div-based fake screenshots BANNED ("#1 LLM-design Tell").
4.9 Content Density: per section headline ≤8 words + sub ≤25 words + one asset/CTA. Lists >5 items need different UI (not ul+divide-y). COPY SELF-AUDIT mandatory: re-read every string; flag broken/unclear/hallucinated/pseudo-thoughtful. Fake-precise numbers flagged (92%, 4.1×, 5.8mm) unless real or <!-- mock -->. One copy register/page.
4.10 Quotes: body ≤3 lines; NO em-dashes; attribution name+role(+company) never name-only; real typographic quotes or none.
4.11 Page Theme Lock: one theme whole page; no section invert (exception one Color Block Story/Theme Switch, once).

### §5 Context-Aware Proactivity
None auto. Magnetic micro-physics only MOTION>5 + premium/playful/agency via useMotionValue/useTransform (never useState). Spring type:"spring" stiffness:100 damping:20 (no linear). "Motion claimed, motion shown" — MOTION>4 must actually animate else drop to 3. MOTION MUST BE MOTIVATED. MARQUEE MAX-ONE-PER-PAGE. 5.A/5.B GSAP Sticky-Stack + Horizontal-Pan skeletons (start "top top", pin true, scrub). 5.C Motion whileInView stagger. 5.D Forbidden: window.addEventListener("scroll"), window.scrollY in React state, rAF loops touching React state.

### §6 Performance & A11y
Animate only transform/opacity (never top/left/width/height). Reduced motion mandatory for MOTION>3. Dark mode mandatory consumer pages. CWV: LCP<2.5s, INP<200ms, CLS<0.1. Grain/noise only fixed pointer-events-none. Z-index restraint.

### §8 Dark Mode Protocol
Dual-mode default. Tailwind dark: OR CSS vars (pick one). Contrast WCAG AA body / AAA hero. No pure #000000/#ffffff — off-black zinc-950, off-white. Test both modes.

### §9 AI Tells (Forbidden)
9.A no neon glows/pure black/oversaturated/custom cursors. 9.C no 3-col equal feature cards. 9.D Jane Doe: no generic names/avatars, no fake-perfect numbers (99.99%,50%), no slop names (Acme/Nexus/SmartFlow), no filler verbs (Elevate/Seamless/Unleash/Next-Gen/Revolutionize).
9.F Production-Test Tells (hard bans): hero version labels (V0.6/BETA/INVITE-ONLY); "Brand · No. 01"; section-number eyebrows (00/INDEX, 001·Capabilities, 06·how it works); 01/4 pagination; numbered scroll cues; middle-dot · max 1/line; decorative colored status dots (zero default); <br>-broken italic headlines; vertical rotated text; crosshair/hairline decoration; div fake product UI; fake version footers; "Quietly in use at/trusted by"; poetic labels (From the field/Field notes/On our desks); weather/locale strips; micro-meta under eyebrows; generic step labels (Stage 1/2/3, Phase 01/02/03); pills/labels on images; photo-credit captions decoration; version footers (v1.4.2/Build 0048) marketing; live-stock counters; hero-bottom decoration strips (BRAND. MOTION. SPATIAL.); floating top-right subtext; border-t+border-b every row; scoring bars filled tracks; locale/city/time/weather strips; scroll cues (Scroll/↓ scroll/Scroll to explore).
9.G EM-DASH BAN (verbatim): "Em-dash (—) is COMPLETELY banned. There is no 'limited use' allowance, no 'natural language frequency' allowance, no 'in body copy is fine' allowance. None." Banned headlines/eyebrows/labels/pills/buttons/captions/nav/body/attribution AND en-dash – as separator (ranges use hyphen -). Only hyphen - and math minus. "If your output contains a single — or – anywhere visible to the user, the output fails the Pre-Flight Check. Zero em-dashes."

### §10 Reference Vocabulary (named catalog, not a library)
Heroes: Asymmetric Split, Editorial Manifesto, Video/Media Mask, Kinetic-Type, Curtain-Reveal, Scroll-Pinned. Nav: Dock Magnification, Magnetic Button, Gooey Menu, Dynamic Island, Radial, Speed Dial, Mega Menu. Grids: Bento, Masonry, Chroma Grid, Split-Screen Scroll, Sticky-Stack. Cards: Parallax Tilt, Spotlight Border, Glassmorphism, Holographic Foil, Tinder Swipe, Morphing Modal. Type: Kinetic Marquee, Text Mask, Scramble, Circular Path. Library choice: Motion default; GSAP+ScrollTrigger for scrolltelling; Three.js/WebGL for 3D — NEVER mix GSAP/Three.js with Motion in same component tree.

### §11 REDESIGN PROTOCOL (modes)
11.A modes: Greenfield (no site/overhaul approved, dial baseline §1); Redesign-Preserve (modernize without breaking brand; audit, extract tokens, evolve gradually); Redesign-Overhaul (new visual language on existing content; treat visuals as greenfield, preserve content+IA). Ambiguous → ask once: "Should this redesign preserve the existing brand, or are we starting visually from scratch?"
11.B Audit before touching: brand tokens, IA, content blocks, patterns-to-preserve, patterns-to-retire, dial reading, SEO baseline ("SEO migration is the #1 redesign risk").
11.C Preservation: don't change IA unless asked; extract brand colors before §4.2 (purple brand stays purple); preserve copy voice; honor a11y wins; respect analytics events.
11.D Modernisation Levers (priority, stop when brief satisfied): 1 Typography refresh → 2 Spacing & rhythm → 3 Color recalibration → 4 Motion layer → 5 Hero/key-section recomposition → 6 Full block replacement (only if unsalvageable).
11.E Decision Tree: IA/content/SEO sound → targeted evolution (Levers 1-4, "~70% value at ~40% risk"); structural visual debt → full redesign w/ content preservation; brand changing → greenfield.
11.F Never changes silently (without approval): URL structure/route slugs, primary nav labels, form field names/order, brand logo/wordmark, legal/consent/cookie copy.

### §12 Block Library (contract, dir not yet populated)
skills/taste-skill/blocks/{hero,feature,social-proof,pricing,cta,footer,navigation,portfolio,transition}/. Frontmatter: name, category, dial_compatibility{variance/motion/density ranges}, when_to_use, not_for, stack. Body: visual sketch, props API, code sketch, mobile fallback, motion variants per band, dark-mode, anti-patterns, references.

### §13 Out of Scope
Not for dashboards/dense product UI, data tables (→TanStack/AG Grid), multi-step forms/wizards, code editors (→Monaco/CodeMirror), native mobile (→HIG/Material), realtime collab.

### §14 FINAL PRE-FLIGHT CHECK
"THIS IS NOT OPTIONAL. Run every box. If any box fails, the output is not done." Re-verifies every threshold: ZERO em-dashes; eyebrow count ≤ceil(sectionCount/3) (hero=1); nav one line ≤80px; hero headline ≤2 lines, subtext ≤20 words AND ≤4 lines, pt-24 max, ≤4 text elements; ≥4 layout families across 8 sections; no 3+ consecutive zigzag; N items→N bento cells; CTA ≤1 line no duplicate-intent; WCAG AA button+form contrast; one accent/one radius/one theme lock; serif not Fraunces/Instrument_Serif; premium-consumer palette not beige+brass; italic descender leading-[1.1]+pb-1; quotes ≤3 lines; CWV LCP<2.5s/INP<200ms/CLS<0.1; min-h-[100dvh] never h-screen; no window scroll listener; reduced motion for MOTION>3; one design system/project. Closing: "If a single checkbox cannot be honestly ticked, the page is not done."
Appendices: A real npm/npx commands per §2 system; B official doc URLs per system; C Apple Liquid Glass honest CSS approximation (backdrop-filter blur(24px) saturate(180%) contrast(1.05), reduced-transparency fallback, "not an Apple package").

## Installation
Vercel `npx skills add` CLI (github.com/vercel-labs/agent-skills) scans skills/.
- All: npx skills add https://github.com/Leonxlnx/taste-skill
- One by INSTALL NAME: npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend"
- v1: --skill "design-taste-frontend-v1"
- Into Codex: npx skills add Leonxlnx/taste-skill -a codex
Primary install name design-taste-frontend (folder skills/taste-skill/). Claude Code via .claude-plugin. Copilot reads .github/copilot-instructions.md. skill.sh local bash resolver. Framework-agnostic.

## 13 skills (folder | install name | role)
taste-skill | design-taste-frontend | v2 canonical.
taste-skill-v1 | design-taste-frontend-v1 | original, same 8/6/4 dials, leaner, framer-motion/lucide, serif BANNED for dashboards.
gpt-tasteskill | gpt-taste | stricter GPT/Codex, Python "true randomization" in <design_plan>, AIDA, no emojis.
image-to-code-skill | image-to-code | image-first generate→analyze→implement.
imagegen-frontend-web | imagegen-frontend-web | one horizontal image PER section (8=8 images).
imagegen-frontend-mobile | imagegen-frontend-mobile | phone-mockup screen concepts, images only.
brandkit | brandkit | brand boards logo/palette/type/mockups, images only.
soft-skill | high-end-visual-design | "$150k+ agency" look, "Absolute Zero" anti-pattern, spring motion.
minimalist-skill | minimalist-ui | Notion/Linear editorial, bans Inter/Roboto/Open Sans.
brutalist-skill | industrial-brutalist-ui | Swiss + terminal, CRT scanlines (Beta).
output-skill | full-output-enforcement | anti-laziness: bans // ... // TODO "for brevity"; [PAUSED — X of Y complete] continuation.
redesign-skill | redesign-existing-projects | Scan→Diagnose→Fix for existing codebases.
stitch-skill | stitch-design-taste | Google Stitch-compatible, exports DESIGN.md.

## research/laziness (backs output-skill)
Findings: Dec-2025 controlled study (GPT-4 variants, DeepSeek) — no model natively satisfies length + all sub-parts; truncation is a deliberate behavioral choice not decoding failure; models resilient over 200-turn tests. Microsoft Research stimulus table: "$200 tip" +45% length; "take a deep breath" 34%→80% logic; "critical to my career" +10%; combined up to +115%. Nov-Dec 2023 vs Jan-Mar 2024 seasonal output-length dip documented.
Root causes: RLHF/compute brevity bias, training-data placeholder propagation, cognitive shortcuts, output-limit asymmetry (2M input vs ~8k output cap; consumer middleware ~32k history cap; dev API bypasses).
Remediation: parameter tuning, prompt engineering (syntax binding, XML frameworks, verification loops), architectural patterns (MCP, lazy-loaded skills), reference prompts.

## CHANGELOG
v2 (experimental): substantial rewrite, still PRE-RELEASE toward v2.0.0 stable (install-name/dials lock at stable). New §0/§2/§8/§11/§12/§13/§14. Hardened bans (§9.G em-dash, section-number eyebrows, hero version labels, decoration strips, image pills, marketing version footers, locale/scroll cues, decorative dots, per-row hairlines, filled progress tracks, div fake-UI). Locks (color/shape/theme), hero + nav discipline, ≥4 layout families, bento cell count, italic descender. Motion standardized (motion/react), §5.A/B/C/D skeletons + reduced-motion. Tailwind v4 default, Phosphor/HugeIcons/Radix/Tabler icons.
v1: original dial-driven philosophy, anti-slop rules, reference vocabulary. Preserved at taste-skill-v1/.

## Sources
github.com/Leonxlnx/taste-skill ; api.github.com/repos/Leonxlnx/taste-skill (+ /git/trees/main?recursive=1, /releases, /tags) ; raw.githubusercontent.com/Leonxlnx/taste-skill/main/{skills/taste-skill/SKILL.md, skills/taste-skill-v1/SKILL.md, README.md, CHANGELOG.md, LICENSE, skill.sh, skills/llms.txt, .claude-plugin/*, .github/*, all sub-skill SKILL.md, research/laziness/*} ; CLI github.com/vercel-labs/agent-skills
