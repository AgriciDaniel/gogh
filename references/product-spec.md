# Gogh Product Spec

## Buyer

Developers, indie hackers, design engineers, and agencies who build frontends with AI coding agents (Claude Code, Cursor, Codex, Windsurf) and want the output to look intentional and brand-fit rather than templated AI slop.

## Domain

Giving AI coding agents good taste in frontend design using the open-source Taste Skill framework by Leon Lin — an anti-slop SKILL.md ruleset with three design dials (DESIGN_VARIANCE, MOTION_INTENSITY, VISUAL_DENSITY), audit-first redesigns, an image-first reference pipeline, anti-laziness rules, and a strict pre-flight check that make Claude Code, Cursor, and Codex produce distinctive, non-templated interfaces instead of generic AI slop.

## Core Workflows

- Install and load the Taste Skill into an agent and run the greenfield (new website) prompt
- Audit-first redesign of an existing site: Section 11 audit, pick a modernization mode, implement while protecting URLs and branding
- Set the three dials (DESIGN_VARIANCE, MOTION_INTENSITY, VISUAL_DENSITY) to fit an industry, audience, and mood
- Run the required audits (em-dash, hero discipline, section-layout-repetition, brand fidelity) and the Section 14 pre-flight check before shipping
- Use the image-first reference pipeline: generate reference frames, analyze them, implement the frontend to match

## Deliverables

- Install-and-load quickstart for Claude Code, Cursor, and Codex
- Greenfield build playbook (Prompt 1) end to end
- Audit-first redesign playbook (Prompt 2) with the modernization modes
- The three-dials tuning guide by industry, audience, and mood
- The rules-and-audits reference card (thresholds, em-dash rule, pre-flight check) and an anti-slop concept map

## Promise

Turn raw sources and recurring decisions into a persistent, source-cited
operating brain.

## Non-Promises

- No invented rules, thresholds, or dial values — every rule cites the canonical SKILL.md or tasteskill.dev, and unverified claims are marked as such
- No shipping past a failed audit or an unrun Section 14 pre-flight check
- On redesigns, no destruction of existing URLs, routes, or brand identity without an explicit modernization-mode decision
- No copying of a client's real API keys, private briefs, or unreleased assets into brain notes
