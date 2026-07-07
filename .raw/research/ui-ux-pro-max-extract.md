# UI UX Pro Max Skill Extract
Captured: 2026-07-07
Sources: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill (retrieved 2026-07-07); https://api.github.com/repos/nextlevelbuilder/ui-ux-pro-max-skill (retrieved 2026-07-07); https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/releases (retrieved 2026-07-07); https://snyk.io/articles/top-claude-skills-ui-ux-engineers/ (retrieved 2026-07-07); https://superdesign.dev/blog/design-skills-reviewed (retrieved 2026-07-07); https://github.com/wilwaldon/Claude-Code-Frontend-Design-Toolkit (retrieved 2026-07-07)
Source type: primary

## Identity and Stats
- Repo: nextlevelbuilder/ui-ux-pro-max-skill.
- Description: "An AI SKILL that provide design intelligence for building professional UI/UX multiple platforms".
- License: MIT. Created 2025-11-30. Last updated 2026-07-07.
- GitHub API on 2026-07-07: stars 102,037, forks 10,755, open issues 126.
- Earlier star snapshots: 29,636 in Snyk's table (article dated Feb 2026); ~99k per superdesign.dev (2026-07-02).
- Star trajectory: roughly 3.4x growth between February and July 2026.
- Languages: Python 74%, JavaScript/TypeScript 15.9% combined, HTML 9.7%.

## Versions (releases page, retrieved 2026-07-07)
- v2.10.2: 2026-07-06 (latest, 2 assets).
- v2.10.1: 2026-07-04.
- v2.10.0: 2026-06-29.
- v2.9.0: 2026-06-26.
- v2.8.8: 2026-06-26 (publish under fallback npm package, fixes issue #393).
- v2.7.0: 2026-06-25 (optional GitHub token support for higher API rate limits).
- v2.6.5: 2026-06-24 (replace colon with hyphen in skill names).
- v2.6.4: 2026-06-24 (pinned shadcn version instead of latest).
- v2.6.2: 2026-06-22 (security: HTML-escape user data in slide generator against XSS).
- All releases published by github-actions with verified GPG signatures.

## Retrieval Database Mechanism
- Core idea: instead of one static style prompt, the skill ships a searchable design database.
- Python scripts query the database per request and return only the relevant slice into context, keeping token cost bounded.
- Database as reported by Snyk (Feb/Mar 2026 snapshot): 50+ UI styles, 97 color palettes, 57 font pairings, 99 UX guidelines, 25 chart types, 9 technology stacks.
- Database per repo README (retrieved 2026-07-07):
  - 67 UI styles (Minimalism through Spatial UI)
  - 161 color palettes (industry-aligned)
  - 57 font pairings (Google Fonts integrated)
  - 99 UX guidelines (best practices and accessibility)
  - 25 chart types (dashboard recommendations)
  - 22 technology stacks (React, Vue, SwiftUI, Flutter, etc.)
  - 161 reasoning rules (industry-specific generation logic)
- Search engine: Python 3.x scripts implementing BM25 ranking for semantic matching across design domains.
- superdesign.dev describes the store as searchable CSV data; noted weakness: "keyword matching can fail" and recommendations are text-only.
- Design System Generator: README calls it an AI-powered reasoning engine that generates a complete tailored design system in seconds via multi-domain parallel search plus decision rules. (A "v2" label for the generator was not verifiable in the retrieved README or release notes at capture.)

## Invocation
1. Automatic activation on UI/UX tasks in Claude Code and compatible assistants (frontmatter trigger matching).
2. Slash command: `/ui-ux-pro-max [request]` on platforms supporting it.
3. Direct CLI / Python script invocation for advanced use.

## Install and Structure
- CLI: `npm install -g ui-ux-pro-max-cli`, then `uipro init --ai [platform]`.
- Supported platforms: Claude, Cursor, Windsurf, Antigravity, Copilot, Kiro, Gemini, and others.
- Layout: `src/ui-ux-pro-max/` (database plus search scripts); `cli/` (installer emitting platform-specific files); templates under `.claude/`, `.cursor/`, `.factory/`.

## Reception Notes
- Snyk ranks it #5 among UI/UX skills; positioned as design-system intelligence complementary to Anthropic's frontend-design.
- superdesign.dev (2026-07-02) criticism: it cannot render or verify its own output; retrieval quality depends on keyword hits.
- wilwaldon's toolkit lists it as "240+ styles with 127 font pairings" (retrieved 2026-07-07); those figures exceed the repo README's own counts and were not verifiable against the repo at capture.
