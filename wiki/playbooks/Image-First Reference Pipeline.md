---
type: "note"
title: "Image-First Reference Pipeline"
created: "2026-07-06"
updated: "2026-07-06"
status: "active"
confidence: "EVIDENCE-BASED"
---

# Image-First Reference Pipeline

Confidence tag: EVIDENCE-BASED (canonical repo skills; `tasteskill.dev/docs`).

## Compiled Truth

An optional workflow (its own set of skills) that generates a visual target *before* writing code. See the concept behind it: [[Image-First Pipeline]].

**The three phases** you request in the prompt ("generate images, then analyze, then code"):

1. **Generate reference frames** with an image model, using a dedicated skill:
   - `imagegen-frontend-web` - premium website reference images, **one horizontal image per section** (8 sections -> 8 images), composition variety, single palette.
   - `imagegen-frontend-mobile` - iOS/Android screen concepts inside phone mockups.
   - `brandkit` - brand-kit boards (logo systems, palette, type, mockups).
   - `image-to-code-skill` (`image-to-code`) or `gpt-taste` for the analyze-and-implement side.
2. **Analyze** the rendered design - extract palette, type, layout, spacing.
3. **Implement** code faithful to the visual spec, under the normal Taste Skill rules.

## When to use it

Reach for this when the aesthetic is hard to specify in words, when you want to lock visual direction cheaply (resolve disagreements on images, ~2 rounds, before any code), or when matching an existing brand board. It converts an open-ended generation problem into a bounded reproduction problem - the reason it produces higher-fidelity output than plain text-to-UI.

## Install

Each image skill installs the same way as the main skill - see [[Install and Load]] and [[The 13 Skills]].

## Related

- [[Image-First Pipeline]] | [[The 13 Skills]] | [[Install and Load]]
- Source: [[Canonical Skill File|Canonical SKILL.md]], [[Taste Skill Official Site]]

## Timeline

- 2026-07-06 - Note created.
