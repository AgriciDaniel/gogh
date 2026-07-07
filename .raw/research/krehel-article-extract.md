# Krehel Article Extract
Captured: 2026-07-07
Sources: https://jakub.kr/writing/details-that-make-interfaces-feel-better (retrieved 2026-07-07); https://jakub.kr/ (retrieved 2026-07-07 via search); https://cz.linkedin.com/in/jakubkrehel (retrieved 2026-07-07 via search); https://github.com/jakubkrehel/make-interfaces-feel-better (retrieved 2026-07-07)
Source type: primary

## Author and Publication
- Author: Jakub Krehel, founding design engineer at Interfere (per LinkedIn). Publishes Interfaces, a design engineering magazine (interfaces.dev), covering animation, typography, layout, and color.
- Article page does not display an explicit publication date; the derived skill repo was created 2026-03-13, placing the article no later than March 2026.
- The article is the upstream source that Krehel distilled into the make-interfaces-feel-better Agent Skill: `npx skills add jakubkrehel/make-interfaces-feel-better` is promoted in the article itself.
- Interactive web article: each technique ships with live before/after examples.

## Argument Structure
- Thesis: interface quality compounds from small details, not one big move. Quote: "It's usually a collection of small things that compound into a great experience" (Krehel).
- Closing framing: "Great design is invisible. It guides users without them ever noticing" (Krehel).
- Body: 11 numbered techniques, each with concrete CSS/Motion values and a demo.

## Technique 1: Text Wrapping
- `text-wrap: balance` for titles, `text-wrap: pretty` for paragraphs; combined approach recommended.
- Demo tested at 215-220px container width to show orphan prevention.

## Technique 2: Concentric Border Radius
- Rule: outer radius = inner radius + padding. Worked example: outer 20px = inner 12px + padding 8px.

## Technique 3: Animate Icons Contextually
- Animate opacity, scale, and blur together on contextual icon swaps (e.g. copy-confirmation checkmark).
- Motion library preferred; CSS-only fallback shown.

## Technique 4: Make Text Crisp
- `-webkit-font-smoothing: antialiased` (Tailwind `antialiased`), applied to the whole layout via body; grayscale antialiasing renders thinner on macOS.

## Technique 5: Use Tabular Numbers
- `font-variant-numeric: tabular-nums` (Tailwind `tabular-nums`) so digits are equal width and dynamic values do not shift layout. Caveat: some fonts (Inter) visibly alter numerals.

## Technique 6: Make Animations Interruptible
- CSS transitions interpolate toward the latest state and are interruptible; keyframe animations run a fixed timeline and are not.
- Rule: transitions for interactions, keyframes for staged one-shot sequences. Rationale: "Users often change their intent mid-interaction" (Krehel).

## Technique 7: Split and Stagger Entering Elements
- Animate title, description, and buttons individually instead of as one block.
- Values in the article demo: from `opacity: 0`, `translateY(8px)`, `blur(8px)`; duration 800ms; easing `cubic-bezier(0.25, 0.46, 0.45, 0.94)`; stagger 100ms between sections, 80ms between text spans.
- Note: the derived skill normalizes these to 300-400ms, translateY(12px), blur(4px); the article demo values above are the originals.

## Technique 8: Make Exit Animations Subtle
- Two approaches: full slide-out via `x: calc(-100% - 4px)`, or subtle opacity+blur exit (recommended).
- Spring transition: `type: "spring", duration: 0.45, bounce: 0`.
- Principle: "Exit animations often work better when they're more subtle than enter animations" (Krehel).

## Technique 9: Align Optically, Not Geometrically
- Icon+text buttons: reduce padding on the icon side relative to the text side.
- Best practice: fix asymmetry in the SVG itself (margins/padding inside the asset) rather than per-use CSS.

## Technique 10: Use Shadows Instead of Borders
- Rest state 3-layer shadow: `0px 0px 0px 1px rgba(0,0,0,0.06)`, `0px 1px 2px -1px rgba(0,0,0,0.06)`, `0px 2px 4px 0px rgba(0,0,0,0.04)`.
- Hover state darkens layers to 0.08/0.08/0.06 alphas; animate via `transition-[box-shadow]`.
- Advantage: transparent shadow stacks adapt to varied backgrounds where solid borders do not.

## Technique 11: Add Outline to Images
- `outline: 1px solid rgba(0, 0, 0, 0.1)` with `outline-offset: -1px`; dark mode `outline-color: rgba(255, 255, 255, 0.1)`. Purpose: depth and consistency over photos of any brightness.

## Relation to the Skill
- The skill (captured separately in mifb-skill-extract) adds prescriptions absent or looser in the article: exact icon values scale 0.25 to 1 and blur 4px to 0, spring duration 0.3 bounce 0, `cubic-bezier(0.2, 0, 0, 1)` cross-fade, `scale(0.96)` press floor 0.95, 40x40px hit areas, `initial={false}`, and the performance rules (`transition: all` ban, `will-change` whitelist).
