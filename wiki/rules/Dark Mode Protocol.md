---
type: "note"
title: "Dark Mode Protocol"
created: "2026-07-06"
updated: "2026-07-06"
status: "active"
confidence: "EVIDENCE-BASED"
---

# Dark Mode Protocol

Confidence tag: EVIDENCE-BASED (canonical `SKILL.md` §8).

## Compiled Truth

- **Dual-mode by default.** A consumer-facing page ships both light and dark.
- **Token strategy:** Tailwind `dark:` OR CSS variables - pick one, do not mix.
- **Contrast:** WCAG **AA** for body, **AAA** for the hero. Hierarchy parity and brand fidelity must survive in *both* themes.
- **No pure values:** off-black (e.g. `zinc-950`) and off-white, never `#000000` / `#ffffff`.
- **Test both modes** before finishing.

Note the interaction with the [[The Three Locks|Page Theme Lock]] (§4.11): dual-mode support is the *capability*, but any single render locks to one theme for the whole page - sections do not invert mid-page.

Dark mode is **mandatory** for consumer-facing pages (§6).

## Related

- [[The Three Locks]] | [[Color Rules]] | [[Motion and Performance Rules]]
- Source: [[Canonical Skill File|Canonical SKILL.md]]

## Timeline

- 2026-07-06 - Note created.
