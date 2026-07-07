# Raw research capture — Community reception & mentions

> Immutable source capture. Retrieved 2026-07-06 by parallel research agent. Do not edit; synthesize into wiki reception/entities.

## Summary
One of the breakout Agent Skills of 2026 — ~58k stars, top of GitHub Trending, built by a teenager; praised as first project to treat AI design slop as a solvable engineering problem; parallel skepticism that "you can't install taste."

## Adoption metrics (star timeline; snapshots)
- Feb 19 2026 repo created. Apr 10 2026: 7,896 (andrew.ooo). May 27 2026: #1 daily repo all languages on Trendshift. May 30 2026: ~28.5K (dev.to). Jun 4 2026: ~33K, ~190K installs (neodrop). Jun 22 2026: peaked #2 GitHub Trending. ~Jun/Jul: 37.4K (+181% vs March). Jul 2026 live: 57,967 (SkillsLLM) / 58.4k (GitHub) / 58.7k (Trendshift). MIT license.
- "56.7k★" (SkillsLLM cached title) = verified stale snapshot; live 57,967.
- Installs (crossaitools): 854.6k total across 13 skills; design-taste-frontend 102.8k; high-end-visual-design 87.4k. neodrop: ~190K + #222 on skills.sh.
- Directory ranking (pasqualepillitteri "18 Best Claude Code Skills for UI/UX"): #3 (37.4K) behind Anthropic official Frontend Design (130.9k) and UI/UX Pro Max (88.7k), ahead of Impeccable (35.8k).
- Trending: Trendshift #1 daily all-langs May 27; #3 weekly wk22; #3 monthly JS May; GitHub Trending peak #2 Jun 22.
- HN reality check: only substantive submission (by steveharing1, May 28 2026) = 3 points, 0 comments. Virality lived on X + GitHub Trending, not HN.

## Notable coverage
- Developers Digest "Taste Skills Are Turning Agent Review Into Infrastructure" (May 30 2026, upd Jun 3). "Teams are turning review taste into runnable infrastructure." "A taste skill is a review checklist, a style contract, and a calibration artifact that the agent must route through before it claims the work is done." "The future of agent quality is not just better generation. It is better review, moved earlier, written down, and reused." "The winning developer agent stack will not be one model plus one chat box. It will be a set of portable controls around model behavior." Family: Taste Skill + Stop Slop + Compound Engineering Plugin. Skeptic rebuttal included: measure if the skill changes review outcomes; else delete it. Concedes "a frontend taste checklist can become trend-chasing."
- andrew.ooo "Taste Skill Review" (Apr 10 2026) — most substantive indep review. "Taste Skill is the first frontend skill that treats 'AI slop' as a solvable engineering problem rather than a vibes problem." Criticism: "Opinions are very strong. 'Inter is banned for creative vibes' is a defensible opinion, but it is an opinion"; framework bias (React/Next assumed); "No automated tests or visual regression." Compared to shadcn/ui, v0.dev, Vercel skills.
- neodrop.ai "taste-skill v2: 3 dials and a 60-item preflight check" (Jun 4 2026). Rewrite ~500 lines → 25,000+ words across 14 sections. §0 Brief Inference forces "commit to a direction before touching layout." "kills the worst defaults, which is already a huge win." Notes designers argued it oversimplifies aesthetic judgment.
- dev.to Tenglong AI (May 30 2026): 5/5 innovation. "Tired of AI-generated UIs that all look the same? White background, blue button, generic sans-serif, no soul?" Contrasts with stop-slop (7.1K).
- knightli.com Guide (Jun 6 2026): "not... another UI component library, but... a set of 'aesthetic constraints'... it can raise the default lower limit."
- daniliants.com (Jul 2 2026): "50,000+ stars"; "suite of skills, not a single skill"; "output visibly differs from default Claude Code pages."
- Others: YouTube (mWXMUM3KPeE), Snyk "Top 8 Claude Skills for UI/UX Engineers", explainx.ai, x-cmd.com, daily.dev repost, Chinese mirrors.

## "Taste skills as infrastructure" thesis (Developers Digest)
Quality control moves LEFT — from post-hoc human review to codified machine-enforced review BEFORE the agent declares done. 3 moves: (1) taste becomes artifact not vibe (runnable gate self-applied); (2) review > generation as the frontier; (3) stack = portable controls around model behavior, not one model.

## Emil Kowalski "Agents with Taste"
Who: respected design engineer — Linear Web team, ex-Vercel design; creator of animations.dev, Sonner, Vaul, index.how. Date: undated, early May 2026 (predates Roger Wong's May 6 2026 response). Thesis: taste is articulable logic — codify it into per-aspect skill files for agents. "Almost every 'taste' decision has a logical reason if you look close enough." "The more you can package into a skill, the more leverage you can get out of your agents." Built his own emil-design-eng skills via Anthropic skill-creator.
KEY NUANCE: Emil's post + emilkowalski/skills repo = PARALLEL INDEPENDENT effort, NOT Leon's project. BUT linked: animations.dev (Emil) is an OFFICIAL SPONSOR of Taste Skill (alongside Vercel OSS Program). So senior-design-engineer endorsement via sponsorship, though the essay is not a review of Leon's project. Roger Wong follow-up amplified Emil (cited Uber's Ian Guisard, Nick Babich); didn't mention Leon.

## Praise vs criticism
Like: names+solves a shared pain; dials + hard-bans + preflight feel rigorous vs "be creative"; portability/no lock-in; concrete engineering craft (useMotionValue perf, min-h-[100dvh], interaction states); prolific 13-skill suite.
Criticize: "it's just prompts/opinions" (andrew: Inter ban is an opinion); framework bias despite "agnostic"; no verification layer (no tests/visual regression); philosophical "you can't install taste" — Mark Chen "You Can't Install Taste" (Medium May 29 2026): tools "make AI stop writing like AI" but not "make AI write well." designative.info "Taste Is the New Bottleneck" (Feb 1 2026), MC Dean "Is Taste Overrated?" — taste resists compression into a checklist; historically a gatekeeping term.
Net: product broadly praised; premise (taste-as-a-file) draws real skepticism.

## Ecosystem context
- SKILL.md / Agent Skills movement (Anthropic + Vercel 2026): portable format major agents auto-load; Taste Skill = highest-profile THIRD-PARTY (non-vendor) skill of the wave.
- Anti-slop family (3 pillars): Taste Skill (frontend design), Stop Slop (Hardik Pandya, ~7.1K, prose/AI-tell removal), Compound Engineering Plugin (engineering loops).
- Vendor incumbent: Anthropic's own frontend-design skill (~130.9k) also targets avoiding "generic AI slop aesthetics" (Nick Porter, Feb 17 2026). Listicles frame Anthropic = baseline, Taste Skill = enhanced fine-control taste layer ("audio equalizer").
- Competitors/complements: UI/UX Pro Max (88.7k), Impeccable (35.8k), Emil's emil-design-eng, same-named-different Dragoon0x/taste-skills.
- vs product tools: Taste Skill = judgment; shadcn/ui = components; v0.dev = hosted generator; Vercel skills = technical baseline. It's a rules/skill LAYER, complements all three.

## Author — Leon Lin (Leonxlnx / @LexnLin)
GitHub Leonxlnx, X @LexnLin, display Leon Lin. Location Munich. Bio "cooking sth." 1.3k followers. own.page/leonlin. GitHub Sponsors (15+ incl Vercel OSS, animations.dev). "16-year-old student from Munich" widely repeated (neodrop, dev.to) and consistent with profile but NOT primary-verified — treat "16" as reported/plausible. Munich verified.
Origin (his X @LexnLin/2025324598401597501): "After a couple hours of work, I finally finished developing my first ever skill. :D Claude's frontend skill tells the AI to 'pick an extreme aesthetic' and 'be creative.' The problem tho is LLMs are just based on probability. Without strict rules, they statistically default to [the most likely patterns]." Taste Skill = his FIRST-EVER skill, born from critique of Anthropic's frontend guidance.
Other repos: taste-skill (~58.4k), stitch-skills (~6.4k), agentic-ai-prompt-research (~2.5k), lumenshaders (~297 WebGL2), prompt-library (~122), todobar (~41). Clusters on AI-agent skills, prompting, frontend/visual tooling.
Posts primarily on X (@LexnLin). Disclaimer: "Taste Skill has no official token, coin, or crypto project."

## Verified vs rumor
Verified: ~58k stars + MIT; trending peaks; Vercel OSS + animations.dev sponsorship; 13-skill suite; ~855k installs; HN 3pts/0comments; Emil's role/credentials; Leon's Munich + repos; v2 architecture (3 dials + 60-item preflight, ~25k words).
Reported not primary-verified: Leon's age "16"; precise install totals; "190K installs" (single dated source).
Misread to avoid: Emil's "Agents with Taste" is NOT a review of Leon's project — parallel thesis by a sponsor.

## Sources
tasteskill.dev/{,docs,changelog} ; github.com/Leonxlnx {,/taste-skill} ; own.page/leonlin ; x.com/LexnLin {,/status/2025324598401597501} ; trendshift.io/repositories/21681 ; developersdigest.tech/blog/taste-skills-ai-agents-design-review ; emilkowal.ski{,/ui/agents-with-taste} ; github.com/emilkowalski/skills ; rogerwong.me/2026/05/agents-taste-skill-files ; andrew.ooo/posts/taste-skill-anti-slop-ai-frontend-review ; knightli.com/en/2026/06/06/taste-skill-ai-frontend-design ; neodrop.ai/post/s3mGLbLqiNd ; dev.to/tenglongai2026/... ; daniliants.com/insights/taste-skill-... ; skillsllm.com/skill/taste-skill ; claudemod.com/mods/taste-skill ; crossaitools.com/skills/leonxlnx/taste-skill ; pasqualepillitteri.it/en/news/576 ; snyk.io/articles/top-claude-skills-ui-ux-engineers ; medium.com/@markchen69/you-cant-install-taste-29a829045bba ; medium.com/@porter.nicholas/... ; designative.info/2026/02/01/taste-is-the-new-bottleneck ; news.ycombinator.com (steveharing1 May 28 2026)
