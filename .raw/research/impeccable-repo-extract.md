# Impeccable Repo Extract
Captured: 2026-07-07
Sources: https://github.com/pbakaus/impeccable (retrieved 2026-07-07); https://impeccable.style (retrieved 2026-07-07); https://github.com/pbakaus/impeccable/releases (retrieved 2026-07-07); https://hn.algolia.com/api/v1/search?query=impeccable.style (retrieved 2026-07-07); https://emelia.io/hub/impeccable-design-skill-review (retrieved 2026-07-07)
Source type: primary

## Identity and Stats
- Repo: pbakaus/impeccable. Tagline: "The design language that makes your AI harness better at design. 1 skill, 23 commands, live browser iteration, and 45 deterministic detector rules".
- Stars 44.1k, forks 2.5k, 861 commits on main, Apache 2.0 license (repo page, 2026-07-07). 30+ documented releases; latest Skill 3.9.1 (2026-07-01).
- Creator: Paul Bakaus, jQuery UI creator and former Google Developer Advocate (emelia.io, 2026-04-01). Crossed 15,000 stars within days of release (emelia.io).
- Premise quote: "It's why AI frontends all share one look" (impeccable.style). Position: a skill clears "the reflexes that make its output look generated" (impeccable.style).

## The 23 Commands (via `/impeccable <command> <target>`)
1. craft: shape-then-build UX/UI flow with visual iteration
2. init: establishes design context, writes PRODUCT.md and DESIGN.md
3. document: generate DESIGN.md from existing code
4. extract: pull reusable components and tokens
5. shape: plan UX/UI before coding
6. critique: design review of hierarchy, clarity, resonance
7. audit: technical checks (a11y, performance, responsive)
8. polish: final pass and shipping readiness
9. bolder: amplify understated designs
10. quieter: tone down overly bold work
11. distill: strip to essence
12. harden: error handling, i18n, edge cases
13. onboard: first-run flows, empty states
14. animate: purposeful motion
15. colorize: strategic color introduction
16. typeset: font choices and hierarchy
17. layout: spacing and visual rhythm
18. delight: moments of joy
19. overdrive: technically extraordinary effects
20. clarify: improve UX copy clarity
21. adapt: multidevice adaptation
22. optimize: performance improvements
23. live: visual variant mode in the browser

## Init Interview and the Design Contract
- `/impeccable init` asks: Brand vs Product lane (marketing/landing vs app UI/dashboard); audience; brand voice; anti-references; color palette; typography; component system.
- PRODUCT.md: captures the brief once (users/metrics, task context, brand voice such as "Calm, clinical, no hype", anti-references such as purple gradients and glassmorphism); every command reads it before designing.
- DESIGN.md: portable design system spec in Google Stitch format, "Readable by every DESIGN.md-aware tool" (impeccable.style). Example contents: `Primary: oklch(78% .12 82)`, wordmark/body font specs (Avenir Next), component count (34 in the site example).
- Brand mode optimizes storytelling; Product mode optimizes usage metrics and task efficiency.

## .impeccable/ File Inventory
- Tracked in git: `config.json`, `live/config.json` (framework wiring), `design.json`, `critique/*.md`.
- Gitignored/ephemeral: `config.local.json`, `hook.cache.json`, `*.png`, `live/server.json`, `live/sessions/`, `live/previews/`, `live/annotations/`, `live/cache/`, `live/manual-edit-*`, `live/pending-manual-edits.json`.

## Deterministic Detector
- 45 deterministic rules, zero LLM; JSON output and build-readable exit codes for CI/PR gates (site example: 3 anti-patterns found, exits 1).
- CLI: `npx impeccable detect src/` (directory), `detect index.html` (file), `detect https://example.com` (URL via Puppeteer), `--json` for CI, `--no-config` for raw scan.
- Ignore management: `npx impeccable ignores list | add-file "src/legacy/**" | add-value overused-font Inter --reason "Brand font"`; inline `<!-- impeccable-disable overused-font: reason -->`.
- Rule targets: AI slop signatures (side-tab/side-stripe borders, purple-to-blue gradients, gradient-text, ai-color-palette, bounce/elastic easing, dark glows, decorative grid backgrounds since 3.9.0), quality (line length, cramped padding, small touch targets, skipped headings, overused fonts like Inter/Arial), color (gray on color, untinted pure black/gray, card nesting).
- Chrome extension distributes the detector; Extension 1.2.1 released 2026-06-19.

## Provider Hooks
- Claude Code: `.claude/settings.local.json` + `.claude/skills/impeccable/scripts/hook.mjs` (findings surfaced after edits).
- GitHub Copilot: `.github/hooks/impeccable.json` + `.github/skills/impeccable/scripts/hook.mjs` (post-edit findings; hooks added in Skill 3.8.0).
- Cursor: `.cursor/hooks.json` + `hook-before-edit.mjs` (blocks problematic writes pre-commit).
- Codex: `.codex/hooks.json` + `.agents/skills/impeccable/scripts/hook.mjs` (post-edit; 3.9.1 fixed Codex plugin hook loading).
- Provider builds carry tailored rules (impeccable.style examples: Gemini build removes image-on-hover; Codex build refuses ghost-cards).

## /impeccable live (Beta)
- Interactive element selection against the running dev server; generates three variants via framework HMR; chosen diffs are written back to source files. State lives under `.impeccable/live/`.

## Install Methods
1. `npx impeccable install` (recommended; auto-detects ~/.claude, ~/.codex, .cursor; `npx impeccable update` to refresh). Requires Node 24+.
2. Claude Code plugin: `/plugin marketplace add pbakaus/impeccable`.
3. Git submodule: `git submodule add https://github.com/pbakaus/impeccable .impeccable` then `npx impeccable link --source=.impeccable --providers=claude,cursor`.
4. Website ZIP download per provider, or manual copy; `npx skills add pbakaus/impeccable` also works.
- Supported providers: Claude Code, Cursor, GitHub Copilot, Gemini CLI, Codex CLI, OpenCode, Pi, Kiro, Trae (intl `~/.trae/skills/`, China `~/.trae-cn/skills/`), Rovo Dev, Qoder.

## Release History (releases page, retrieved 2026-07-07)
- Skill 3.9.1 (2026-07-01): Codex loads the plugin design hook again.
- Skill 3.9.0 + CLI 3.2.0 (2026-07-01): decorative grid backgrounds become a named detection; bolder respects existing design systems; grid-line background detector rule.
- Skill 3.8.0 + CLI 3.1.0 (2026-06-21): GitHub Copilot design hooks; monorepo per-app context resolution; inline ignore comments.
- Extension 1.2.1 (2026-06-19): badge count matches popup findings.
- CLI 3.0.3 (2026-06-17); Skill 3.7.1 (2026-06-16): bundled detector config-module fix.
- Skill 3.7.0 + CLI 3.0.2 (2026-06-16): design-aware hook detections check documented palettes; shared ignore config; Node 24+ install fix.

## Reception Snapshot (see ecosystem extract for full reception)
- Hacker News story "Impeccable Style" 2026-01-12: 103 points, 64 comments. HN comment: "a great approach to identifying slop" (nyxtom, 2026-06-12).
- Free; site testimonials include "Can't believe it's free" (impeccable.style, 25+ testimonials).
