# Impeccable Contracts and Vocabulary

Title: Impeccable design contracts, commands, and detector vocabulary
Author: Paul Bakaus
Year: 2025 initial repository, current captured skill version 3.9.1 in 2026
Distillation status: primary captures, with contract details captured through README and SKILL.md rather than standalone PRODUCT.md or DESIGN.md examples
Source URLs:
- https://github.com/pbakaus/impeccable, retrieved 2026-07-07
- https://impeccable.style/, retrieved 2026-07-07
- https://github.com/pbakaus/impeccable/releases, retrieved 2026-07-07
Capture paths:
- .raw/skills/impeccable/SKILL.md
- .raw/skills/impeccable/README.md
- .raw/research/impeccable-repo-extract.md

## Why canonical

Impeccable is canonical for Gogh because it moves design help from a passive prompt into a toolchain: setup context, command vocabulary, detector hooks, live iteration, and standalone CI-capable scans. Its PRODUCT.md and DESIGN.md pattern gives agents a durable contract for audience, lane, voice, anti-references, colors, type, and components. Its detector vocabulary gives Gogh a concrete language for naming and gating AI slop.

## Distilled principles

1. Initialize design context before design work. The agent should know audience, product lane, voice, anti-references, palette, typography, and component system.
2. Separate brand register from product register. Marketing pages optimize story and resonance; tools and dashboards optimize tasks and usage.
3. Make the design contract persistent so every later command reads the same context.
4. Use PRODUCT.md for the durable brief and DESIGN.md for portable design-system specifics.
5. Route work through named commands such as craft, shape, critique, audit, polish, animate, colorize, typeset, layout, bolder, quieter, distill, harden, onboard, optimize, and live.
6. Treat commands as vocabulary shared between humans and agents, not just shortcuts.
7. Read existing project code before inventing a new design system.
8. Use provider hooks to surface detector findings where the agent edits UI files.
9. Let deterministic detector rules catch obvious anti-patterns without using an LLM or API key.
10. Keep ignores explicit, reasoned, and reviewable when a rule must be waived.
11. Name anti-slop families concretely: overused fonts, purple gradients, card nesting, side stripes, dark glows, bounce easing, decorative grids, gradient text, cramped padding, and small touch targets.
12. Use live variant mode only when a running dev server and source-writing loop make visual iteration real.
13. Respect existing design systems before making work bolder or quieter.
14. Treat "production-grade" as code, responsiveness, performance, accessibility, and brand fit together.
15. Do not conflate detector output with universal design law; detector rules are Impeccable's current upstream rules.

## How Gogh uses it

This work underpins wiki/skills/Impeccable (Toolchain).md, wiki/concepts/Impeccable Design Contracts.md, wiki/concepts/Deterministic Design Detection.md, wiki/flows/Impeccable Project Lifecycle.md, wiki/audits/Impeccable Audit and Detect.md, and wiki/rules/Impeccable Rule Set (45 Detectors).md.

Mechanically, Gogh uses it as the enforcement and vocabulary layer: project contracts, register selection, named commands, hooks, detector scans, explicit waivers, and anti-pattern taxonomy.
