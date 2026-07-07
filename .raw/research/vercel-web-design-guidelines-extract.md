# Vercel Web Design Guidelines Extract
Captured: 2026-07-07
Sources: https://github.com/vercel-labs/agent-skills (retrieved 2026-07-07); https://raw.githubusercontent.com/vercel-labs/agent-skills/main/skills/web-design-guidelines/SKILL.md (retrieved 2026-07-07); https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md (retrieved 2026-07-07); https://api.github.com/repos/vercel-labs/web-interface-guidelines (retrieved 2026-07-07); https://snyk.io/articles/top-claude-skills-ui-ux-engineers/ (retrieved 2026-07-07)
Source type: official

## Host Repo: vercel-labs/agent-skills
- Description: "A collection of skills for AI coding agents" in the Agent Skills (SKILL.md) format.
- Stars 28.8k, forks 2.6k, MIT license (repo page, 2026-07-07).
- Languages: JavaScript 97.3%, Shell 1.6%, TypeScript 1.1%.
- 8 skills in the collection:
  1. vercel-optimize (cost, performance, reliability audits of Vercel projects)
  2. react-best-practices (40+ performance rules across 8 categories per repo page; Snyk cites 57 rules)
  3. web-design-guidelines (this extract)
  4. writing-guidelines (prose review against the Vercel handbook)
  5. react-native-guidelines (16 rules, 7 sections)
  6. react-view-transitions (View Transition API)
  7. composition-patterns (React component architecture)
  8. vercel-deploy-claimable (deploys with claim URLs)
- Install: `npx skills add vercel-labs/agent-skills`; skills self-activate on matching tasks.
- Each skill ships SKILL.md plus scripts/ and references/ directories.

## The Audit Mechanism (web-design-guidelines SKILL.md, v1.0.0)
- Triggers: "Review my UI", "Check accessibility", "Audit design", "Review UX".
- Step 1, runtime rule fetch: the agent fetches the current ruleset from `https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md` at audit time.
- Step 2: applies every fetched rule to the user-specified files or glob patterns.
- Step 3: reports findings in `file:line - issue` format, grouped by filename, terse wording, explanations only when non-obvious.
- Compliant files get an explicit pass marker.
- If the user names no files, the agent must ask rather than guess.
- Design consequence: no rules are baked into the skill, so guideline changes propagate to all installs without reinstalling.

## Rule Set (command.md as retrieved 2026-07-07)
- Repo README markets "100+ rules covering accessibility, performance, and UX"; the fetched command.md contained roughly 85 discrete guidelines across 17 categories.
- Category counts and representative rules from capture:
  - Accessibility (9): icon-only buttons need `aria-label`; keyboard handlers on interactive elements; semantic HTML before ARIA.
  - Focus States (4): visible focus via `focus-visible:ring-*`; never `outline: none` without replacement; prefer `:focus-visible`.
  - Forms (11): inputs need `autocomplete` and meaningful `name`; never block paste; inline errors, focus first error on submit.
  - Animation (5): honor `prefers-reduced-motion`; animate only `transform`/`opacity`; never `transition: all`.
  - Typography (6): use the ellipsis character, not three dots; curly quotes; `tabular-nums` for number columns.
  - Content Handling (4)
  - Images (3)
  - Performance (6)
  - Navigation & State (4)
  - Touch & Interaction (4)
  - Safe Areas & Layout (3)
  - Dark Mode & Theming (3)
  - Locale & i18n (4)
  - Hydration Safety (3)
  - Hover & Interactive States (2)
  - Content & Copy (6)
  - Anti-patterns (12 flags)

## Relation to Vercel's Web Interface Guidelines Document
- Upstream repo: vercel-labs/web-interface-guidelines, "Guidelines for building interfaces on the Web".
- Created 2025-09-10; MIT; 697 stars, 48 forks (GitHub API, 2026-07-07); React/Next.js oriented.
- The skill is a thin executable wrapper; command.md in that repo is the single source of truth consumed at runtime.

## Update Cadence
- Guidelines repo last push 2026-04-06 (GitHub API, 2026-07-07); revisions land in every subsequent audit automatically via the runtime fetch.
- Observed rhythm: multi-month document revisions rather than continuous rule churn; the skill wrapper itself remains at v1.0.0.
- Snyk (Feb 2026) ranks web-design-guidelines #2 among UI/UX skills and frames it as the correctness and compliance layer beside Anthropic's aesthetics-focused frontend-design.
