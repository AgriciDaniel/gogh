---
type: "flow"
title: "Aesthetic Direction Commitment"
status: "developing"
created: "2026-07-07"
updated: "2026-07-07"
tags: ["gogh/stack", "note/flow"]
domain: "stack"
confidence: "evidence-based"
related: ["[[Design Skills Mechanism Map]]", "[[Full Stack Build Flow]]", "[[Skill Stack Selection Flow]]", "[[Distinctiveness Audit]]", "[[DESIGN_VARIANCE]]", "[[Retrieval Database Skills]]", "[[Anthropic Frontend Design Rules]]", "[[Modernization Modes]]"]
source_urls: ["https://raw.githubusercontent.com/Leonxlnx/taste-skill/main/skills/taste-skill/SKILL.md (retrieved 2026-07-07)", "https://raw.githubusercontent.com/anthropics/skills/main/skills/frontend-design/SKILL.md (retrieved 2026-07-07)", "https://raw.githubusercontent.com/nextlevelbuilder/ui-ux-pro-max-skill/main/.claude/skills/ui-ux-pro-max/data/styles.csv (retrieved 2026-07-07)", "https://github.com/pbakaus/impeccable (retrieved 2026-07-07)"]
sources: ["[[Canonical Skill File]]", "[[Anthropic Frontend Design Skill and Post]]", "[[UI UX Pro Max Repo]]", "[[Impeccable Repo and Site]]"]
---

Commit to a named aesthetic direction before writing any code, because rule
compliance can only prevent bad output while a committed direction is the only
thing that produces memorable output.

## What it is

- The mandatory first step of every Gogh-guided build or redesign.
- A short written commitment made before any file is edited.
- It names four things: the direction, the signature element, the five-second
  memory, and the nearest banned default being avoided.
- The direction is a specific named style, not an adjective. "Terminal noir
  ledger" commits; "clean and modern" does not.
- The signature element is the one move the page owns: a layout device, a
  type treatment, a data object, a color behavior.
- The five-second memory is what a visitor would describe after five seconds.
- It exists because of a measured failure: the claude-ads landing run of
  2026-07-07 passed every ban, every detector, and every checklist, and the
  operator scored it 3 out of 10 because it kept the incumbent style.
- The lesson from that run: the stack's negative space (bans, audits) was
  executed and its positive space (direction, variance, style selection) was
  never invoked.
- Upstream basis: taste-skill opens by forcing an aesthetic commitment before
  code and dials variance up to 10; the Anthropic skill's core instruction is
  a bold, committed direction; ui-ux-pro-max ships 84 named styles so agents
  stop defaulting; Impeccable's live mode generates three variants per element
  because one attempt rarely lands.

## How it works

- Read the brief and classify ambition: refresh (keep direction, tighten
  craft), evolve (keep the brand, push variance), transform (new direction;
  "impress me", "redesign", "make it special" all mean transform).
- For transform, treat the work as greenfield with brand constraints, the
  Overhaul stance in [[Modernization Modes]]; the incumbent design is input
  evidence, never the default answer.
- Query the direction vocabulary: the captured style database at
  .raw/skills/ui-ux-pro-max/styles.csv (84 named styles with palettes,
  best-for and do-not-use-for columns, era, prompt keywords).
- `gogh-brain advise` with `"ambition": "transform"` surfaces three candidate
  directions from that database, spread across style categories.
- Draft two or three direction candidates, each one line: name, signature
  element, five-second memory.
- Kill any candidate that matches the incumbent site's current style; if it
  survives that test, it is a refresh, not a transform.
- Check the chosen direction against [[Unified Anti-Slop Rulebook]]: a
  direction may deliberately use a banned default only with a brief-led
  exception recorded in writing.
- Write the commitment at the top of the working plan, then build under it;
  every later craft decision (radius, motion, palette) serves the direction.
- Gate the result with [[Distinctiveness Audit]] before shipping; a page that
  fails the five-second test goes back to the direction step, not to polish.

## Best practice

- Never start building from an inherited style when the brief says impress,
  redesign, or transform. PRACTITIONER
- Name the direction in three words or fewer plus a signature element before
  the first edit. EVIDENCE-BASED
- Pull candidates from the captured 84-style database instead of improvising
  from memory. EVIDENCE-BASED
- Generate at least two candidate directions before choosing; one attempt is
  exploration zero. EVIDENCE-BASED
- Match DESIGN_VARIANCE to ambition: refresh 3 to 4, evolve 5 to 7, transform
  8 to 9. EVIDENCE-BASED
- Keep the brand's non-negotiables (logo, voice, one accent) listed inside the
  commitment so the direction change stays shippable. PRACTITIONER
- Record the rejected candidates in the plan; they are the variant record.
  PRACTITIONER
- Treat detector and checklist passes as the floor, never the goal.
  EVIDENCE-BASED

## Pitfalls

- Compliance theater: a page can pass every audit and still be forgettable;
  that is exactly the 3-out-of-10 failure this flow exists to prevent.
- Adjective directions ("modern", "clean", "premium") commit to nothing and
  regress to the training-data mean, the [[Distributional Convergence]] trap.
- Treating brand_maturity partial as permission to keep everything; partial
  brand constrains colors and voice, not layout, type scale, or composition.
- Choosing a direction and then sanding it off during craft passes until the
  signature element disappears.
- Querying the style database and picking the first row instead of the row
  whose do-not-use-for column clears the brief.
- Skipping the commitment because the deadline is short; the commitment is
  four lines and saves a full rebuild.

## Sources

- taste-skill v2 SKILL.md, aesthetic commitment and DESIGN_VARIANCE sections,
  capture .raw/skills/taste-skill-v2/SKILL.md, retrieved 2026-07-07.
- Anthropic frontend-design SKILL.md, committed direction requirement, capture
  .raw/skills/anthropic-frontend-design/SKILL.md, retrieved 2026-07-07.
- ui-ux-pro-max styles database, 84 styles, capture
  .raw/skills/ui-ux-pro-max/styles.csv, retrieved 2026-07-07.
- Impeccable live mode, three variants per element, capture
  .raw/skills/impeccable/README.md, retrieved 2026-07-07.
- Operator retrospective, claude-ads landing run 1 scored 3/10, 2026-07-07.

## Related

- [[Full Stack Build Flow]] - this flow is now its step zero.
- [[Skill Stack Selection Flow]] - ambition classification feeds the advisor.
- [[Distinctiveness Audit]] - the exit gate that enforces this entry gate.
- [[Design Skills Mechanism Map]] - where direction sits among mechanisms.
- [[DESIGN_VARIANCE]] - the dial this flow sets by ambition.
- [[Modernization Modes]] - Overhaul mode is the transform stance.
- [[Retrieval Database Skills]] - why the style database beats memory.
- [[Anthropic Frontend Design Rules]] - the official committed-direction rule.
- [[Unified Anti-Slop Rulebook]] - the floor the direction must still clear.
- [[Distributional Convergence]] - the failure mode this flow interrupts.

## Next actions

- Apply this flow to the claude-ads landing rerun and record the score delta.
- Add an ambition classification example set from real operator briefs.
- Consider capturing the ui-ux-pro-max palettes CSV as companion vocabulary.
