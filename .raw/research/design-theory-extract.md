# Raw research capture — Design theory / concepts

> Immutable source capture. Retrieved 2026-07-06 by parallel research agent. Do not edit; synthesize into wiki concepts.

## 1. AI slop = distributional convergence to the mean
Cluster of unprompted defaults: purple→blue gradients, Inter, centered hero + subhead + 2 buttons, 3-card feature grid, untouched shadcn zinc/slate, rounded-2xl shadow-lg backdrop-blur everywhere, gradient text bg-clip-text, three-tier pricing, 4-col footers, worn lucide icons (Sparkles/ArrowRight/Zap), emoji bullets, filler copy ("Elevate", "Seamless", "Get Started"). avoid-ai-design skill enumerates "tells".
Root cause: models sample the STATISTICAL CENTER of training corpus. "Why Your AI Keeps Building the Same Purple Gradient Website": "LLMs are excellent at generating code, but they're not designers, they're statistical pattern matchers." "When you prompt an LLM to build a UI, it reaches for purple... because purple is statistically common in the training corpus." Purple traced to Tailwind's demo default bg-indigo-500 saturating tutorials → "modern web design = purple buttons" baked into training data. "Taste requires lived experience... LLMs... have statistical correlations between tokens." Fix is CONSTRAINT (forbidden lists, references, one direction), not "make it beautiful" prompts. Em-dash overuse + emoji bullets are the prose analog.

## 2. Taste as the moat when models commoditize
VC Corner "Why Taste Is the New Moat": "Creation has become frictionless... infinite and cheap, built in bulk by machines that never tire." "When technology commoditizes creation, judgment becomes the last remaining edge. Taste is what decides which ideas deserve to exist, which details are worth sweating, and which defaults communicate care." "design has become a real credibility signal... how users decide what, and who, to trust." "When everything can be made, filters outrank generators."
Julie Zhuo "When AI Has Better Taste Than You": taste = "our values and preferences"; great taste is sophisticated prediction — "If excellent taste operates through pattern recognition across vast cultural knowledge, then it isn't a stretch to imagine that AI systems can replicate this process." Reserved human edge = cultural courage, not daily aesthetic judgment.
Dissent (balance): taste itself commoditizes into a threshold bar not a permanent moat (Ruiqi Zhou; Hilde Dybdahl Johannessen).
=> ideological basis for Taste Skill: taste = codified pattern recognition => packageable/distributable to agents. "Taste as a dependency you can npm install."

## 3. Three-dials model = reducing aesthetics to controllable axes
DESIGN_VARIANCE (1 Perfect Symmetry → 10 Artsy Chaos): layout experimentation centered→asymmetric.
MOTION_INTENSITY (1 Static → 10 Cinematic/Physics): hover→scroll/magnetic.
VISUAL_DENSITY (1 Art Gallery/Airy → 10 Cockpit/Packed Data): info per viewport.
Per-prompt overridable; "audio equalizer on the AI design output."
Lineage fused from 3 fields: (1) design tokens / style axes — W3C Design Tokens CG first STABLE spec Oct 2025: token = "expressing design decisions in a platform-agnostic way"; tokens now cover motion (timing/easing) and density (spacing) → map to the dials; dials are META-TOKENS (scalar selects coordinated bundle). (2) variable-font parametric axes — "arbitrary custom axes" over continuous design params. (3) controllable generation / disentangled sliders (TokenDial continuous motion modulation; Brickify direct token manipulation). Dials = prompt-space analog of a latent slider.
Why it works: high-dim aesthetic spaces collapse to mean when underspecified; projecting onto 3 legible monotonic axes gives communication protocol + coverage (airy landing AND packed dashboard from one ruleset) + sampling constraint off the median. Cost: axes not truly independent (variance+density fight); between-notch taste lost.

## 4. Encoded design principles (primary sources)
Visual hierarchy (Refactoring UI, Wathan & Schoger): hierarchy via size/color/weight/placement is "the most effective tool... for making something feel 'designed.'" Slop fails by being FLAT.
Whitespace/density (Refactoring UI): "start with too much" whitespace and remove — theory under VISUAL_DENSITY, default airy.
Typographic scale/measure (Butterick Practical Typography): body 15-25px, line spacing 120-145%, line length 45-90 chars → skill's max-w-[65ch]. Ban Inter + mandate display face = pairing/contrast.
Motion restraint (Material 3; WCAG): motion functional, expresses hierarchy; "Standard" scheme minimal bounce, expressive only for hero moments. Floor = prefers-reduced-motion (WCAG C39). Theory behind MOTION as dial + animate only transform/opacity.
Bento grids: modular variable-size CSS Grid tiles (Apple keynotes) — "big box = big deal", asymmetry with structure = high-DESIGN_VARIANCE vocabulary.
Color theory: dominant/secondary/accent (60-30-10); indigo default is artifact not choice.
Anti-clutter (Rams "Good design is as little design as possible"; Tufte data-ink ratio / chartjunk "ink that does not tell the viewer anything new"). Caveat: users sometimes prefer moderate ornament → anti-clutter rules are DEFAULTS not laws.

## 5. Agent design review as infrastructure (judgment as machine-checkable rules)
Encode judgment as rules the agent runs itself: pre-flight checks, forbidden-pattern audits, redesign/audit protocol. 3 converging traditions:
(1) Design linting / design-as-code: linting = automated rule-checking; @lapidist/design-lint flags raw values vs token constraints; Figma Design System Linter. A Taste audit = lint pass w/ aesthetic rules + waivers-with-rationale.
(2) Design systems as code / tokens as single source of truth: token conformance checkable; skill's color/shape/theme "locks" make consistency verifiable not vibes.
(3) Eval-driven generation & LLM/Agent-as-Judge: Evaluation-driven Development; LLM-as-a-Judge; Agent-as-a-Judge (observes intermediate steps, tools, action log); WebDevJudge benchmark "(M)LLMs as Critiques for Web Development Quality." Pre-flight = lightweight in-loop instance — same model judges its own output vs explicit rubric before finishing.
Why: generation without check-back reverts to mean; encoding taste as pass/fail gate = zero marginal human cost, infinite scale (like CI linting beat manual style review).

## 6. Image-first / reference-driven pipeline
"Generate reference frames, analyze them, then implement the frontend to match." 3 phases: (1) gen reference frames (imagegen-frontend-web/mobile, brandkit, gpt-taste); (2) analyze (palette, type, layout, spacing); (3) implement faithful code.
Why beats text→UI: text→code forces holding whole aesthetic in latent space → collapses to mean. Image stage: (a) concrete target replaces abstract instruction — mockup "isn't a pixel-perfect spec. It's a visual conversation about intent"; coding-to-match is narrower/constrained; (b) cheap iteration in right medium — resolve aesthetics on images before code (~2 mockup rounds), design comp→build handoff inside one session; (c) grounded generation — SpecifyUI, Prototype2Code: "specification-based generation more faithfully captures reference intent than prompt-based baselines" (region segmentation, palette/font detection via VLMs).
Converts open-ended generation (mean-seeking) into bounded reproduction (match target) where agents are strongest; human exercises taste at cheapest stage (an image).

## 7. SKILL.md / Agent Skills format
Anthropic: skills = "organized folders of instructions, scripts, and resources that agents can discover and load dynamically." Min = dir with SKILL.md (YAML frontmatter required name+description) + Markdown body; may bundle scripts/references/templates. Markdown chosen: "must be both machine-parseable and human-readable." Published as OPEN STANDARD for cross-platform portability (Claude Code, Cursor, Codex).
Progressive disclosure (key): L1 Discovery — only name+description preloaded ("just enough... to know when each skill should be used without loading all of it"); L2 Activation — load full SKILL.md when relevant; L3 Execution — bundled files read only when task calls for them.
Why design ruleset fits: static opinionated instructions = Markdown body; ~800 lines would bloat every prompt → progressive disclosure loads only on frontend task (L2), heavy assets (GSAP skeletons, image-gen sub-skills) at L3 → why it's MANY variants not one monolith; portability = distribution of taste via npx skills add; composability — image-first pipeline + pre-flight audit live in same loadable unit.

## Synthesis
AI slop = convergence to mean (§1). Fight it because taste is the moat (§2). Made specifiable by dials (§3) grounded in canonical design principles (§4). Made enforceable by design review as infra (§5), achievable by image-first pipeline (§6), portable/loadable by SKILL.md (§7). Through-line: CONSTRAINT BEATS COAXING — narrow the sampling space and package the narrowing so it travels.

## Sources
prg.sh/ramblings/Why-Your-AI-Keeps-Building-the-Same-Purple-Gradient-Website ; github.com/funboy322/avoid-ai-design ; thevccorner.com/p/why-taste-is-the-new-moat ; lg.substack.com/p/when-ai-has-better-taste-than-you ; w3.org/community/design-tokens (Oct 2025 stable) ; arxiv 2603.27520 (TokenDial), 2502.21219 (Brickify), 2508.02994 (Agent-as-a-Judge), 2510.18560 (WebDevJudge), 2509.07334 (SpecifyUI), 2405.04975 (Prototype2Code) ; refactoringui.com ; practicaltypography.com ; m3.material.io/styles/motion ; WCAG C39 ; infovis-wiki data-ink ; nngroup clutter-charts ; anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills ; platform.claude.com/docs/en/agents-and-tools/agent-skills/overview ; paddo.dev/blog/nano-banana-ux-design-workflow
