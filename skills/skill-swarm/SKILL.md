---
name: skill-swarm
description: Exhaustive skill coverage for one topic — finds EVERY skill in the library relevant to the prompt (hundreds if that is what matches) and makes all of them reach the answer via three tiers, instead of the router's usual 4-6. Use when the user says "use all the skills", "every skill related to this", "all 78 skills", "maximum skills", "don't miss any skill", or when a task is broad enough that a 6-skill chain provably under-covers it. Reports a coverage line so under-use is visible.
---

# Skill swarm

The router gives you 4–6 skills. That is right for a narrow task and wrong for a broad one:
"immersive web design" has **65 genuinely relevant skills** in this library, and a 6-skill
chain silently discards 59 of them.

## The constraint you must not pretend away

Invoking 65 skills through the Skill tool loads 65 full `SKILL.md` files — measured at
~4k tokens each, so **~260k tokens** before you write a word. That crowds out the work
itself and the output gets worse, not better.

So "use all of them" means **all of them reach the answer**, not all of them get loaded
whole. Three tiers do that. Never claim you invoked a tier-2 or tier-3 skill.

## Run it

```bash
python ~/.claude/skills/skill-swarm/scripts/swarm.py --topic "<the topic>" \
       --out _projects/<slug>/SWARM.md          # omit --out to print to stdout
```

Flags: `--tier1 8` (invoked) · `--tier2 40` (digested) · `--floor 0.15` (relevance cut,
`0` disables) · `--selftest`.

Inside an existing `_projects/<slug>/` write `SWARM.md` next to `SKILLS.md` — `SKILLS.md`
ranks the library, `SWARM.md` is the loading plan. Regenerate after installing skills.

## The three tiers

| Tier | Count | What you do |
|---|---|---|
| 1 | ~8 | **Invoke via the Skill tool.** Full procedure. |
| 2 | ~40 | **Read the digest in `SWARM.md`.** Headings = procedure, rule lines = constraints. Do NOT invoke. |
| 3 | rest | **Named only.** Invoke one the moment the work actually reaches it. |

Tier 2 is what makes coverage real. Those skills' hard rules bind you exactly as if you
had loaded them — a `NEVER` line in a tier-2 digest is not advisory.

## Rules

1. **Report the coverage line verbatim** from the bottom of `SWARM.md`:
   `65 matched · 8 invoked · 40 digested · 17 named`. This is what makes under-coverage
   visible instead of invisible. Never inflate it.
2. **Surface contradictions, do not resolve them silently.** At this breadth skills WILL
   disagree — this library has `ai-studio-today-design` (light theme, Arial Black) sitting
   next to `premium-design-laws` and a locked dark Royal Plum system. Name both and say
   which one governs and why; the project's `CLAUDE.md` and the second brain outrank any skill.
3. **Promote on contact.** A tier-3 name that turns out to matter gets invoked right then.
   Tiering is a budget, not a verdict.
4. **The floor is relative, not absolute.** It cuts at 15% of the top unpinned score, so it
   adapts per topic. It cannot tell you a whole topic is meaningless — if every match looks
   irrelevant, the topic string is too generic. Rephrase it, don't lower the floor.
5. **Domain rules still bind.** The `skill-routes.json` chain is pinned to the top of tier 1
   and its hard rule (deck-first, Verification Lock, MERGE-never-replace, …) is unchanged.

## Verify before saying done

- `python ~/.claude/skills/skill-swarm/scripts/swarm.py --selftest` → `selftest OK`
- The coverage line in your answer matches `SWARM.md`.
- Every tier-1 skill you claimed appears as an actual Skill invocation in the transcript.
