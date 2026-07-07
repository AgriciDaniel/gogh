# Gogh Adapter Plan

Status: required before domain-adapted maturity.

## Raw Input Types

- The canonical SKILL.md and README in github.com/Leonxlnx/taste-skill, the tasteskill.dev guide/docs/changelog/blog, and the design brief plus target URL supplied by the operator

## Required Implementation

- Define one schema per raw input type.
- Build at least one real domain importer or ingestion path.
- Build one domain-specific synthesis module.
- Build one report renderer with source citations.
- Add sanitized fixtures and tests for every supported input type.

## Safety Refusals

- No invented rules, thresholds, or dial values — every rule cites the canonical SKILL.md or tasteskill.dev, and unverified claims are marked as such
- No shipping past a failed audit or an unrun Section 14 pre-flight check
- On redesigns, no destruction of existing URLs, routes, or brand identity without an explicit modernization-mode decision
- No copying of a client's real API keys, private briefs, or unreleased assets into brain notes

## Completion Gate

This plan is complete only when domain-specific importer, synthesis, report,
fixtures, and tests replace the generic scaffold.
