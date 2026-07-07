---
type: "concept"
title: "Agent Skills and SKILL.md Format"
created: "2026-07-06"
updated: "2026-07-06"
status: "active"
confidence: "EVIDENCE-BASED"
---

# Agent Skills and SKILL.md Format

Confidence tag: EVIDENCE-BASED (from Anthropic's engineering docs).

## Compiled Truth

**Agent Skills** (Anthropic) are *"organized folders of instructions, scripts, and resources that agents can discover and load dynamically to perform better at specific tasks."* Minimally, a skill is a directory with a `SKILL.md` whose YAML frontmatter carries a required `name` and `description`, followed by a Markdown body of instructions; the folder may bundle scripts, references, and templates. Markdown was chosen deliberately: the file "must be both machine-parseable and human-readable." Anthropic published it as an **open standard** for cross-platform portability, which is why one file loads into Claude Code, Cursor, and Codex alike. See [[Coding Agents]].

## Progressive disclosure (the key mechanism)

Skills manage context in tiers so they do not bloat every prompt:
- **Level 1 - Discovery:** at startup only each skill's `name` + `description` is preloaded - "just enough information for Claude to know when each skill should be used without loading all of it into context."
- **Level 2 - Activation:** if relevant, the agent "load[s] the skill by reading its full SKILL.md into context."
- **Level 3 - Execution:** bundled files are read *only when the specific task calls for them*.

## Why a portable design ruleset fits perfectly

The mapping to Taste Skill is almost one-to-one:
- A design ruleset is **static, opinionated instructions** - exactly what a Markdown body is for. The skill is "fully editable"; the agent reads it on each run.
- Its **~800 lines** would bloat every prompt if always loaded; progressive disclosure loads the rules *only when a frontend task fires* (L2), and heavy assets (GSAP skeletons, per-variant rules, the image-gen sub-skills) only when their branch is hit (L3). This is **why the project is a suite of 13 separately-discoverable skills**, not one monolith - see [[The 13 Skills]].
- **Portability = distribution of taste.** Because SKILL.md is an open standard, one ruleset propagates to every compatible agent via `npx skills add` - the concrete delivery mechanism for the [[Taste as the Moat|"taste as a dependency"]] idea.
- **Composability.** Skills can bundle scripts, so the [[Image-First Pipeline]] and the [[Pre-Flight Check (Section 14)]] can live in the same loadable unit as the rules.

In short, SKILL.md gives an aesthetic ruleset a *loading model* (progressive disclosure), a *distribution model* (open-standard portability), and a *composition model* (bundled scripts + references) - the three things a "taste as infrastructure" tool needs to exist at all.

## Related

- [[The 13 Skills]] | [[Coding Agents]] | [[Install and Load]] | [[Design Review as Infrastructure]]
- Source: [[Design Theory Sources]]

## Timeline

- 2026-07-06 - Note created.
