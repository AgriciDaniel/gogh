---
type: "note"
title: "Install and Load"
created: "2026-07-06"
updated: "2026-07-06"
status: "active"
confidence: "EVIDENCE-BASED"
---

# Install and Load

Confidence tag: EVIDENCE-BASED (canonical `SKILL.md`, `tasteskill.dev/docs`).

## Compiled Truth

Taste Skill installs via the Vercel `npx skills add` CLI, which scans the repo's `skills/` folder. The primary skill's **install name is `design-taste-frontend`** (the frontmatter `name:`, not the folder name).

```bash
# The main v2 skill (recommended)
npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend"

# Pin to the legacy v1
npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend-v1"

# Install the whole 13-skill bundle
npx skills add Leonxlnx/taste-skill

# Install into Codex specifically
npx skills add Leonxlnx/taste-skill -a codex
```

**Other ways in:** copy any `SKILL.md` into your project root, or paste it into ChatGPT/Codex. Claude Code can also load it as a plugin via the repo's `.claude-plugin/` manifest; GitHub Copilot auto-reads `.github/copilot-instructions.md`.

**Compatible agents:** Claude Code, Cursor, Codex, Gemini CLI, AI Studio, v0, Lovable, OpenCode, Copilot - see [[Coding Agents]]. Framework-agnostic in principle (React/Vue/Svelte/Astro), though defaults assume React/Next (see [[Architecture and Stack]]).

## Then load it in the session

Per the guide: *"Load the skill once at the top of your session, then use one of the two prompts."* You start a build by declaring: *"I have loaded tasteskill v2 (experimental) as my only source of design rules."* Then run [[Greenfield Build (Prompt 1)]] or [[Audit-First Redesign (Prompt 2)]].

The `SKILL.md` is **fully editable** - open it in your project root to change, add, or remove any rule. This is the intended escape hatch for the opinionated rules (e.g. the Inter ban).

## Related

- [[Greenfield Build (Prompt 1)]] | [[Audit-First Redesign (Prompt 2)]] | [[The 13 Skills]] | [[Agent Skills Format|Agent Skills and SKILL.md Format]]
- Source: [[Canonical Skill File|Canonical SKILL.md]], [[Taste Skill Official Site]]

## Timeline

- 2026-07-06 - Note created.
