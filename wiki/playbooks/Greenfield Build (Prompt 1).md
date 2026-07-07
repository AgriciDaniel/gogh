---
type: "note"
title: "Greenfield Build (Prompt 1)"
created: "2026-07-06"
updated: "2026-07-06"
status: "active"
confidence: "EVIDENCE-BASED"
---

# Greenfield Build (Prompt 1)

Confidence tag: EVIDENCE-BASED (verbatim from `tasteskill.dev/guide?view=full`).

## Compiled Truth

The official workflow for building a new site. Fill the brief, then let the agent declare its read, stop, and build after your OK. Verbatim prompt:

```
I have loaded tasteskill v2 (experimental) as my only source of design rules.

Brief:
- Page kind: <landing / portfolio / marketing>
- Product: <name and one-line description>
- Audience: <who reads this, concrete adjectives>
- Vibe words: <2 to 4 concrete adjectives, e.g. "minimalist, editorial, restrained">
- References: <real URLs or product names that anchor the aesthetic>
- Avoid: <explicit slop patterns the brief should NOT default to>

Step 1. Declare your design read in one sentence and the three dial values
        with one-line reasoning each. Stop.

Step 2 (after my OK). Ship a single Next.js page with at least 8 sections.
        Pick the sections that actually fit the product. At least 4 different
        layout families across the page. Use real images (gen-tool first, then
        Picsum-seed). Lock one theme for the whole page.

Step 3. Run in writing:
- Em-dash audit (zero em-dashes U+2014 or en-dashes U+2013 anywhere)
- Pre-Flight Check (Section 14, every box marked Pass or Fail with one-line justification)
- Section-Layout-Repetition audit (list each section's layout family)
- Hero discipline audit (headline lines, subtext words, CTA visibility)

Any Fail blocks completion.
```

## The three steps, decoded

1. **Design Read (then Stop).** The agent commits to a direction *before* touching layout - the §0 "Brief Inference" step. It outputs a one-line read ("Reading this as: <page kind> for <audience>, with a <vibe> language, leaning toward <system/aesthetic>") plus the three [[The Three Dials|dial values]] with reasoning. neodrop calls this the fix for the "start coding, figure out the vibe later" failure mode. If the brief is ambiguous, the skill asks **exactly one** question.
2. **Build (after your OK).** One Next.js page, **>=8 sections** chosen to fit the product, **>=4 layout families**, real images (gen-tool first, then `picsum.photos`), one theme locked. All the [[Rules and Audits Reference Card|hard thresholds]] apply.
3. **Audit in writing.** Four audits run explicitly; any Fail blocks completion. See [[Required Audits]] and [[Pre-Flight Check (Section 14)]].

## Related

- [[Dial Tuning Guide]] | [[Hero Discipline]] | [[Layout and Section Rules]] | [[Pre-Flight Check (Section 14)]]
- Source: [[Taste Skill Official Site]]

## Timeline

- 2026-07-06 - Note created.
