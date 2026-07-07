---
type: "overview"
title: "Overview"
created: "2026-07-06"
updated: "2026-07-06"
status: "active"
confidence: "EVIDENCE-BASED"
---

# Overview

Confidence tag: EVIDENCE-BASED (from the canonical `SKILL.md`, `tasteskill.dev`, and GitHub API, retrieved 2026-07-06).

## What Taste Skill is

**Taste Skill** is an open-source [[Agent Skills Format|Agent Skill]] (a portable `SKILL.md` ruleset) that stops AI coding agents from generating generic, templated frontends - what the project calls "slop." It plugs into any tool that reads `SKILL.md` files: Claude Code, Cursor, Codex, Gemini CLI, v0, Lovable, OpenCode, and more. It is not a component library and not a hosted generator; it is a **constraint layer** that rides on top of whatever agent and stack you already use.

- Tagline: **"Less slop, designs pop."** Positioning: "The Anti-Slop Frontend Framework for AI Agents."
- Author: [[Leon Lin]] (`@LexnLin`, GitHub `Leonxlnx`), with `blueemi`. Built in Munich; this was his first-ever skill.
- Repo: `github.com/Leonxlnx/taste-skill`. License **MIT**. Created 2026-02-19. **~58,400 stars** as of 2026-07-06.
- Current version: **v2 (experimental)**, a pre-release iterating toward a v2.0.0 stable that will lock the install name and dials. v1 is preserved.
- Scope: **landing pages, portfolios, and redesigns.** Explicitly not dashboards, data tables, or multi-step product UI. See [[Scope and Context]].

## How it works, in four ideas

1. **Read the room first.** Before any code, the agent infers page kind, audience, vibe, and design system from the brief and declares a one-line "Design Read." See [[Greenfield Build (Prompt 1)]].
2. **The three dials.** It parameterizes aesthetics into [[DESIGN_VARIANCE]], [[MOTION_INTENSITY]], and [[VISUAL_DENSITY]] (each 1-10, baseline **8 / 6 / 4**), set conversationally per project. See [[The Three Dials]].
3. **Hard rules and bans.** ~800 lines / 14 sections of machine-checkable thresholds: a total [[Em-Dash Ban]], [[Hero Discipline]], [[Navigation Discipline]], [[The Three Locks]], and a long list of [[AI Tells (Forbidden Patterns)]].
4. **Audit-first and gated.** Redesigns start with an audit ([[Audit-First Redesign (Prompt 2)]]); everything ends with the [[Pre-Flight Check (Section 14)]]. Any failed box blocks completion.

## Why it matters

Taste Skill is the highest-profile third-party entry in the 2026 "skills as infrastructure" wave: the idea that design judgment can be encoded as a reusable, machine-enforced review standard an agent must pass before it claims the work is done. The underlying theory - that [[AI Slop]] is convergence to the statistical mean and that [[Taste as the Moat|taste is the durable moat]] once production commoditizes - is genuine and cited, and its central premise ("you can't install taste") is genuinely [[Reception and Criticism|contested]].

## Where to go next

New here? Read [[Start Here]]. Want the rules fast? [[Rules and Audits Reference Card]]. Want the why? [[Constraint Beats Coaxing]].
