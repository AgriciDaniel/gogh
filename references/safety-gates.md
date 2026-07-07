# Safety Gates

V1 is read-only and advisory unless a future release explicitly adds approved,
reversible mutation.

## Refusal Rules

- No invented rules, thresholds, or dial values. Every rule cites the canonical SKILL.md or tasteskill.dev, and unverified claims are marked as such
- No shipping past a failed audit or an unrun Section 14 pre-flight check
- On redesigns, no destruction of existing URLs, routes, or brand identity without an explicit modernization-mode decision
- No copying of a client's real API keys, private briefs, or unreleased assets into brain notes
- No credentials, tokens, cookies, or secrets are ever stored in the vault (this brain is read-only and advisory)

## Safety Risks

- Stale rules or dial values after an upstream Taste Skill release (thresholds drift, v2-experimental changes)
- Cargo-culting the rules into contexts where they do not fit (e.g. forcing 'real images only' on a data-heavy dashboard)
- Treating the skill as a component library rather than a constraint layer, or shipping without running the audits
- Leaking a client's private brief, URLs, or credentials into notes

## Release-Blocking Gates

- Current trustworthy sources are missing.
- Raw source provenance is missing.
- Deliverables contain unsupported claims.
- Credentials or private client data are present.
- A mutation path exists without approval and rollback.
