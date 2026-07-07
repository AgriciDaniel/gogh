# Vercel Web Interface Guidelines

Title: Web Interface Guidelines
Author: Vercel
Year: 2025, based on guideline repository creation in local evidence
Distillation status: primary capture
Source URLs:
- https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md, retrieved 2026-07-07
- https://raw.githubusercontent.com/vercel-labs/agent-skills/main/skills/web-design-guidelines/SKILL.md, retrieved 2026-07-07
- https://vercel.com/design/guidelines, retrieved 2026-07-07
Capture paths:
- .raw/skills/vercel-web-design-guidelines/command.md
- .raw/skills/vercel-web-design-guidelines/SKILL.md
- .raw/research/vercel-web-design-guidelines-extract.md

## Why canonical

Vercel's guidelines are Gogh's audit-first correctness layer. The skill wrapper fetches the latest ruleset at runtime, so the canonical substance lives in the guideline document rather than the thin skill file. It is canonical because it turns broad interface quality into terse, file-line findings across accessibility, forms, focus, performance, state, content, locale, hydration, and motion.

## Distilled principles

1. Prefer native semantics before ARIA. Use buttons for actions, links for navigation, labels for controls, and tables for tabular data.
2. Icon-only buttons need accessible names, and decorative icons should be hidden from assistive tech.
3. Focus states must remain visible. Removing outlines without replacement is a failure.
4. Form controls need labels, meaningful names, correct types, autocomplete, inline errors, and first-error focus.
5. Do not block paste. Password managers, autofill, and user agency are part of the interface.
6. Motion must honor reduced-motion preferences and should animate compositor-friendly properties.
7. Avoid `transition: all`; list the properties that change.
8. Text containers must survive long, short, empty, and user-generated content.
9. Images need dimensions, lazy loading below the fold, and priority treatment when critical.
10. Large lists need virtualization or a content-visibility strategy before they become performance bugs.
11. URL state should reflect filters, tabs, pagination, and expanded panels when deep linking matters.
12. Destructive actions need confirmation or undo, never immediate irreversible behavior.
13. Safe-area insets, dark-mode metadata, and native select styling matter on real devices.
14. Dates, numbers, and currency should use `Intl` rather than hardcoded formats.
15. Hydration warnings should be rare and justified, not a way to silence mismatches.
16. Output should be terse, grouped by file, and tied to file-line locations.

## How Gogh uses it

This work underpins wiki/skills/Vercel Web Design Guidelines.md, wiki/concepts/Runtime Rule Fetch.md, wiki/audits/Vercel Guidelines Audit.md, wiki/rules/Vercel Interface Rule Categories.md, and wiki/audits/Required Audits.md.

Mechanically, Gogh uses it as an audit shim: fetch current rules, inspect target files, produce high-signal file-line findings, and treat Vercel findings as upstream guideline findings rather than Gogh-owned judgments.
