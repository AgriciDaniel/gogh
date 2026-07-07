---
type: "entity"
title: "Coding Agents"
created: "2026-07-06"
updated: "2026-07-06"
status: "active"
confidence: "EVIDENCE-BASED"
---

# Coding Agents

Confidence tag: EVIDENCE-BASED (`tasteskill.dev`, repo integration files).

## Compiled Truth

The tools Taste Skill plugs into. It works with **anything that reads `SKILL.md`** ([[Agent Skills Format|Agent Skills and SKILL.md Format]]) - "one install," portable across:

- **Claude Code** (Anthropic) - loads via the repo's `.claude-plugin/` manifest or `npx skills add`.
- **Cursor** - reads project skill files.
- **Codex** (OpenAI) - `npx skills add ... -a codex`; the `gpt-taste` variant is tuned for it.
- **Gemini CLI** and **AI Studio** (Google).
- **v0** and **Lovable** - hosted generators.
- **OpenCode**, **Windsurf**, **GitHub Copilot** (auto-reads `.github/copilot-instructions.md`).

Framework-agnostic in principle: React, Vue, Svelte, Astro, any stack - "the rules target design intent, not a single framework API." In practice the code sketches assume **React/Next.js** (see [[Architecture and Stack]] and the framework-bias critique in [[Reception and Criticism]]).

**Ecosystem note:** Taste Skill is the highest-profile *third-party* skill of the 2026 Agent Skills wave, sitting alongside vendor skills like Anthropic's own `frontend-design`. See [[Ecosystem and Alternatives]].

## Related

- [[Agent Skills Format|Agent Skills and SKILL.md Format]] | [[Install and Load]] | [[Ecosystem and Alternatives]]
- Source: [[Taste Skill Official Site]]

## Timeline

- 2026-07-06 - Note created.
