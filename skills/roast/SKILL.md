---
name: roast
description: Stress-test a business idea, plan, or build BEFORE committing — spins up an adversarial council (contrarian, expansionist, first-principles, researcher, buyer, judge) and returns a kill / reshape / green-light verdict plus the single cheapest 48-hour test. Use when the user proposes a product, feature, pricing, campaign, or "should I build X" and you'd otherwise just agree.
---

# roast — adversarial council for ideas and plans

## Why this exists

The default failure mode is sycophancy. Models fail to push back on a user's framing ~88% of
the time (the "ELEPHANT" study), and it gets *worse* the more memory/personalization they have —
i.e. worse the longer you work with one user. Agreement feels productive; it does not make the
decision better. This skill forces a structured fight before any code, money, or time is committed.

Source: distilled from Nate Herk's "make money with Claude Code" video (2026-06-25). The technique
is sound independent of the marketing wrapper around it.

## When to invoke

- User proposes a product, feature, pricing tier, campaign, or content bet
- "Should I build X?", "is this a good idea?", "will people pay for this?"
- Before EnterPlanMode on anything with real cost (money, days of work, a public launch)
- Any time you catch yourself about to say "that's a great idea" — run this instead

Do NOT invoke for trivial reversible choices (variable names, which file to edit). Reserve it for
decisions that are expensive to unwind.

## The three intake questions (ask first, then run)

Before convening the council, get exactly these — keep it to one round:

1. **Who is the actual buyer?** (the specific person who pulls out a card, not "anyone")
2. **What is your edge?** (distribution, audience, unfair advantage, or honestly "none yet")
3. **Constraints — budget, and how fast do you need the first dollar?**

If the user says "keep it broad" or won't narrow, run anyway but have the council punish the
vagueness (no edge + no distribution is itself a finding).

## The council (run these as parallel sub-agents)

Spin up one sub-agent per persona via the Agent tool or `Workflow` — each gets its own clean
context and is told to be ruthless, not balanced. Each returns a 1–10 score + 2–3 sentence reason.

| Persona | Only job |
|---|---|
| **Contrarian** | Find the fatal flaw. Assume it fails — explain why. Default pessimist. |
| **Expansionist** | Find the biggest honest upside and the version of this that's 10x bigger. |
| **First-principles** | No market context, pure logic. Does the value actually exist? Strip the hype. |
| **Researcher** | Pull REAL competitors, pricing, and substitutes off the web. Cite sources. Is there a free alternative? |
| **Buyer** | Role-play the exact target buyer from Q1. Would you pay? At what price? What makes you walk? Be honest. |
| **Judge** | Read all five. Issue ONE verdict + the cheapest 48h test. Does not participate in scoring. |

The Researcher must use real search (WebSearch / the `researcher` agent) — no invented competitors.
The Buyer is the most important persona; a "no" from the buyer outweighs a clever Expansionist pitch.

## The verdict (what the Judge returns)

Always exactly this shape:

- **Verdict:** `GREEN-LIGHT` / `RESHAPE` / `KILL` + confidence (low/med/high)
- **One line:** the verdict in a single blunt sentence
- **Why:** the 2–3 load-bearing reasons
- **Biggest risk:** the one thing most likely to kill it (CAC > LTV, no moat, no distribution, free substitute…)
- **If RESHAPE:** what to keep (the engine/moat) and what to cut, aimed at a narrower paying niche
- **Cheapest 48h test:** the single smallest experiment to learn if it's real BEFORE writing code
  (usually: pick one niche, DM/email 20–30 of them, see if anyone pre-commits). Never "go build the MVP."
- **Scores:** the six numbers, so the user sees the spread

## Honesty rules

- The council critiques the IDEA, not the user. No "you're smart" framing anywhere.
- If the idea is a thin wrapper over a free tool, say so — that's a structural churn problem, not a polish problem.
- A reshaped idea still needs the cheapest test; validation comes before building, always.
- Surface what's NOT being said: hidden CAC, platform risk, regulatory traps, skills assumed.

## Verifiable goal (Karpathy)

The skill succeeded when: three intake questions were asked, all six personas produced a scored
finding, the Researcher cited at least one real competitor/substitute, and the Judge returned a
verdict with a concrete 48-hour test that is cheaper than building. If the user's idea got a
reflexive "yes," the skill failed.

## Related

- `grill-me` / `grill-with-docs` — interrogate the user's understanding (different: tests *them*, not the *idea*)
- `board-meeting`, `executive-mentor:stress-test`, `red-team`, `adversarial-reviewer` — heavier or code-focused variants
- After a GREEN-LIGHT/RESHAPE: hand the validated idea to `experiment-designer` then `business-planner`
