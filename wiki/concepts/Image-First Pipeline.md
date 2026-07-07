---
type: "concept"
title: "Image-First Pipeline"
created: "2026-07-06"
updated: "2026-07-06"
status: "active"
confidence: "EVIDENCE-BASED"
---

# Image-First Pipeline

Confidence tag: EVIDENCE-BASED.

## Compiled Truth

An optional but signature workflow: *"generate reference frames, analyze them, then implement the frontend to match."* Three phases the user requests in the prompt:

1. **Generate** reference frames with an image model. The suite ships dedicated image skills for this: `imagegen-frontend-web` (one horizontal image *per section*), `imagegen-frontend-mobile`, and `brandkit`; plus `image-to-code-skill` and the `gpt-taste` variant. See [[The 13 Skills]].
2. **Analyze** the rendered design - extract palette, type, layout, spacing.
3. **Implement** code faithful to the visual spec.

## Why it beats standard text-to-UI

Plain text->code forces the model to hold the entire aesthetic in latent space and emit it directly, which - underspecified - collapses to the mean ([[AI Slop]]). Inserting an image stage changes the problem in three ways:

1. **A concrete target replaces an abstract instruction.** The mockup "isn't a pixel-perfect spec. It's a visual conversation about intent" and "becomes the shared language between design intent and code." Coding-to-match a fixed reference is a *narrower, more constrained* task than inventing from prose.
2. **Cheap iteration in the right medium.** Aesthetic disagreement is resolved on images *before* any code is written (typically ~2 mockup rounds) - the design-industry comp->build handoff reconstructed inside one agent session.
3. **Grounded generation.** Reference-driven UI research (SpecifyUI, Prototype2Code) shows "specification-based generation more faithfully captures reference intent than prompt-based baselines."

The net move: convert an open-ended **generation** problem (mean-seeking) into a bounded **reproduction** problem (match this target), where agents are strongest - and let the human exercise [[Taste as the Moat|taste]] at the cheapest possible stage, an image, rather than debugging aesthetics in code. This is [[Constraint Beats Coaxing]] applied to the pipeline itself.

See the playbook: [[Image-First Reference Pipeline]].

## Related

- [[The 13 Skills]] | [[Image-First Reference Pipeline]] | [[AI Slop]]
- Source: [[Design Theory Sources]]

## Timeline

- 2026-07-06 - Note created.
