# MISSING: CHANGELOG for pbakaus/impeccable

No CHANGELOG file exists in the repository. Checked on 2026-07-07:

- Full recursive git tree of `pbakaus/impeccable@main` via
  `https://api.github.com/repos/pbakaus/impeccable/git/trees/main?recursive=1`
  (2617 paths, not truncated) contains no file matching CHANGELOG in any
  directory or case.
- URL variants tried or ruled out by the tree listing:
  - https://raw.githubusercontent.com/pbakaus/impeccable/main/CHANGELOG.md (not in tree)
  - https://raw.githubusercontent.com/pbakaus/impeccable/main/CHANGELOG (not in tree)
- The closest thing is a changelog page on the project website, built from
  `site/pages/changelog.astro` in the repo, rendered at https://impeccable.style
  It is a website page, not a repo CHANGELOG document, so it was not captured
  as CHANGELOG.md.

Version information is instead embedded in the skill frontmatter
(`version: 3.9.1` in the captured SKILL.md).

Note on the captured SKILL.md: the repo ships the skill to many agent runtimes
(.agents/, .claude/, .codex/, .cursor/, .gemini/, etc.) plus a source file at
`skill/SKILL.src.md`. The Claude distribution
`.claude/skills/impeccable/SKILL.md` was captured as the main skill definition.
