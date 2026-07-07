---
type: "concept"
title: "The Three Dials"
created: "2026-07-06"
updated: "2026-07-06"
status: "active"
confidence: "EVIDENCE-BASED"
---

# The Three Dials

Confidence tag: EVIDENCE-BASED (dial names/scales from the canonical `SKILL.md` §1 and `llms.txt`).

## Compiled Truth

The heart of Taste Skill (§1 of the canonical `SKILL.md`). Three 1-10 dials the agent sets from the brief and declares before writing any code:

| Dial | 1 | 10 | Baseline |
|---|---|---|---|
| [[DESIGN_VARIANCE]] | Perfect Symmetry | Artsy Chaos | **8** |
| [[MOTION_INTENSITY]] | Static | Cinematic / Physics | **6** |
| [[VISUAL_DENSITY]] | Art Gallery / Airy | Cockpit / Packed Data | **4** |

**Baseline is `8 / 6 / 4`.** Overrides happen conversationally (e.g. "build a dashboard, VISUAL_DENSITY 9, MOTION_INTENSITY 2"), **never by editing the file** - the file stays canonical; the conversation tunes it. The model is described as "an audio equalizer on the AI design output."

## Why reducing aesthetics to three axes works

High-dimensional aesthetic spaces are hard to specify in prose and collapse to the mean when underspecified ([[AI Slop]]). Projecting them onto three human-legible, monotonic axes gives:
- a **communication protocol** between human intent and agent output;
- **coverage** - the same ruleset produces an airy art-gallery landing page *and* a packed cockpit dashboard;
- a **sampling constraint** that pushes off the median ([[Constraint Beats Coaxing]]).

**Conceptual lineage** (see [[Encoded Design Principles]]): the dials fuse three ideas - design-token *style axes* (the W3C Design Tokens spec reached first stable status Oct 2025 and now tokenizes motion and density too), *variable-font parametric axes* (a low-dimensional continuous space over a high-dimensional design space), and *controllable generation* / disentangled sliders in generative ML. The dials are essentially **meta-tokens**: one scalar that selects a coordinated bundle of underlying values, expressed as a natural-language integer instead of a latent-space slider.

**The cost of the reduction (kept honest):** the axes are not truly independent - high variance and high density fight each other - and taste that lives *between* the notches is lost. This is part of why critics say it "oversimplifies aesthetic judgment" ([[Reception and Criticism]]).

## How the dials drive output

Each dial maps to concrete technical bands (§7); see the individual notes and [[Motion and Performance Rules]]. Values also come from an inference table and use-case presets - see the [[Dial Tuning Guide]].

## Related

- [[DESIGN_VARIANCE]] | [[MOTION_INTENSITY]] | [[VISUAL_DENSITY]] | [[Dial Tuning Guide]]
- Source: [[Canonical Skill File|Canonical SKILL.md]], [[Design Theory Sources]]

## Timeline

- 2026-07-06 - Note created.
