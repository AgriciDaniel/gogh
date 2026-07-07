---
type: "note"
title: "Architecture and Stack"
created: "2026-07-06"
updated: "2026-07-06"
status: "active"
confidence: "EVIDENCE-BASED"
---

# Architecture and Stack

Confidence tag: EVIDENCE-BASED (canonical `SKILL.md` §3; §2 design-system map).

## Compiled Truth

**Default architecture (§3):**
- **Framework:** React / Next.js, React Server Components by default; interactivity isolated in `'use client'` leaves.
- **Styling:** **Tailwind v4** default (use `@tailwindcss/postcss`, not the `tailwindcss` postcss plugin).
- **Animation:** **Motion** - `import { motion } from "motion/react"` (`framer-motion` is the legacy alias). See [[Motion and Performance Rules]].
- **Fonts:** `next/font` or self-host `@font-face` + `font-display: swap`. **Never `<link>` Google Fonts in production.**
- **State:** never `useState` for continuous input - use `useMotionValue` / `useTransform` / `useScroll`.
- **Icons:** priority Phosphor (`@phosphor-icons/react`), HugeIcons, Radix, Tabler; `lucide-react` discouraged; **never hand-roll SVG icons**; one family per project; standardize `strokeWidth` globally (1.5 or 2.0). Emoji discouraged.
- **Sizing:** `min-h-[100dvh]` never `h-screen`; Grid over flex-math; contain to `max-w-[1400px]` / `max-w-7xl`.
- Verify every dependency against `package.json` before importing.

**Design-system map (§2):** when a brand implies an official system, install the real package - don't recreate its CSS or override 90% of its tokens. **One system per project.**

| Brief signal | System / package |
|---|---|
| Microsoft / enterprise | `@fluentui/react-components` (or web-components) |
| Google / Material | `@material/web` + Material 3 |
| IBM / analytics | `@carbon/react` + `@carbon/styles` |
| Shopify | Polaris |
| Atlassian | `@atlaskit/*` |
| GitHub devtool | `@primer/css` / `@primer/react-brand` |
| UK public sector | `govuk-frontend` |
| US public sector | `uswds` |
| Local-business MVP | Bootstrap 5.3 |
| Accessible React | `@radix-ui/themes` |
| Owned components | shadcn/ui |
| Tailwind SaaS | Tailwind v4 utilities + `dark:` |

Aesthetics with **no** official package (glassmorphism, bento, brutalism, editorial, dark tech, aurora/mesh, kinetic type, Apple Liquid Glass) are built honestly with native CSS + Tailwind and labeled as approximations. The `SKILL.md` appendices give real `npm install` commands and official doc URLs per system, plus an honest Liquid Glass CSS skeleton.

## Framework caveat

Although the project claims to be framework-agnostic (React/Vue/Svelte/Astro), the defaults and examples assume **React/Next.js** - a criticism reviewers raise. The rules "target design intent, not a single framework API," but the code sketches are React. See [[Reception and Criticism]].

## Related

- [[Motion and Performance Rules]] | [[Scope and Context]] | [[Rules and Audits Reference Card]]
- Source: [[Canonical Skill File|Canonical SKILL.md]]

## Timeline

- 2026-07-06 - Note created.
