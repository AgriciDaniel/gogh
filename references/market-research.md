# Market Research

Status: researched. Reception and positioning captured 2026-07-06 from dated third-party sources. Refresh quarterly.

## Buyer Hypothesis

Developers, indie hackers, design engineers, and agencies who build frontends with AI coding agents (Claude Code, Cursor, Codex, Windsurf) and want the output to look intentional and brand-fit rather than templated AI slop.

## What the demand signals show

- The pain is real and widely felt: the "white background, blue button, generic sans-serif, no soul" default is a shared complaint across every AI-coding-agent community.
- The value is "raise the floor" reliability: reviewers agree the skill kills the worst defaults even if it does not manufacture top-tier design.
- The distribution is frictionless: one `npx skills add` line works across many agents, so adoption cost is near zero.
- The recurring loop is the audit: teams come back because the pre-flight check and redesign audit give a repeatable, written pass/fail gate.

## Evidence Log

| Evidence | Source | Retrieved | Confidence | Notes |
|---|---|---|---|---|
| ~58,435 GitHub stars; top of GitHub Trending (peaked #2, 2026-06-22; #1 Trendshift daily 2026-05-27) | GitHub API; Trendshift repo 21681 | 2026-07-06 | high | Genuine viral adoption |
| ~854.6k total installs across the 13 skills; design-taste-frontend ~102.8k | crossaitools.com | 2026-07-06 | medium | Directory-reported |
| Ranked #3 among Claude Code UI/UX skills, behind Anthropic official (130.9k) and UI/UX Pro Max (88.7k) | pasqualepillitteri.it | 2026-07-06 | medium | Positioning vs incumbents |
| Sponsored by Vercel OSS Program and animations.dev (Emil Kowalski) | tasteskill.dev; github.com/sponsors/Leonxlnx | 2026-07-06 | high | Credible design-world backing |
| "First frontend skill that treats AI slop as a solvable engineering problem" | andrew.ooo review, 2026-04-10 | 2026-07-06 | medium | Core praise |
| "Skills as infrastructure": review moved earlier, written down, reused | Developers Digest, 2026-05-30 | 2026-07-06 | medium | Category thesis |
| Premise critique: "you can't install taste"; rules are opinions; no verification layer | Mark Chen 2026-05-29; andrew.ooo | 2026-07-06 | medium | Held CONTESTED |
| HN engagement near zero (3 pts, 0 comments, 2026-05-28) despite star count | news.ycombinator.com | 2026-07-06 | high | Virality lived on X + GitHub, not HN |

## Competitive frame

- Complements, not competes: Taste Skill is a judgment/rules layer, distinct from component libraries (shadcn/ui), hosted generators (v0.dev), and the vendor baseline (Anthropic frontend-design). See `wiki/reception/Ecosystem and Alternatives.md`.
- The nearest substitute is Anthropic's own frontend-design skill; Taste Skill positions as a finer-control taste layer on top of that baseline.
