# Source Map

## Raw Sources

- The canonical SKILL.md and README in github.com/Leonxlnx/taste-skill, the tasteskill.dev guide/docs/changelog/blog, and the design brief plus target URL supplied by the operator

## Enrichment Sources

- github.com/Leonxlnx/taste-skill (SKILL.md, README, releases, changelog)
- tasteskill.dev/guide?view=full, /docs, /changelog, /blog (official positioning and rules)
- Emil Kowalski 'Agents with Taste' (emilkowal.ski/ui/agents-with-taste) and Developers Digest 'Taste Skills Are Turning Agent Review Into Infrastructure'
- Anthropic Agent Skills / SKILL.md format docs and the skills directories (SkillsLLM, claudemod, crossaitools) for adoption context
- Design-craft primary sources for the encoded principles (Refactoring UI, Practical Typography, Apple HIG, Material) used only to explain the rules

## Import Strategy

- Copy raw source files into `.raw/sources/`.
- Record path, hash, retrieval date, owner, and source type.
- Record external research sources in `references/source-ledger.json`.
- Record implemented schemas and adapters in `references/adapter-manifest.json`.
- Create a source note under `wiki/sources/`.
- Link affected entities, workflows, and deliverables.
