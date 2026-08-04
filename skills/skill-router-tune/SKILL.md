---
name: skill-router-tune
description: Tune the skill-routing system from real usage data. Reads ~/.claude/skill-usage.jsonl (what skills actually got used per prompt), the vault playbooks, and staged feedback, then proposes concrete edits to ~/.claude/skill-routes.json. Invoke when the user says "tune the router", "improve skill routing", "which skills am I actually using", or during a weekly /si:review pass.
---

# Skill Router Tune

The routing system has three parts:
- `~/.claude/skill-routes.json` — the routing table (domains → keywords → ranked skill chain + playbooks + rule)
- `~/.claude/hooks/skill-router.py` — UserPromptSubmit hook that matches each prompt and injects the best-fit chain
- `~/.claude/skill-usage.jsonl` — appended by the Stop hook every turn: prompt head, skills/agents used, blocked flag

This skill is the learning loop: usage data in, better routing table out.

## Procedure

1. **Read the data.** Load `~/.claude/skill-usage.jsonl`. If it has fewer than ~30 entries, say so and stop — not enough signal to tune.

2. **Mine four signals:**
   - **Misses**: entries with `blocked: true` or empty `skills` on substantive prompts → the prompt's keywords belong in some domain's `keywords` list (new or existing).
   - **Winning chains**: skill sequences that recur for a prompt pattern but aren't in the table → candidate new domain or reorder of an existing chain.
   - **Dead weight**: table skills that never appear in the log across many matched prompts → demote or remove from the chain.
   - **Drift**: skills referenced in the table that no longer exist in `~/.claude/skills/` (check the folder) → remove or replace.

3. **Cross-check the second brain.** Scan `MEMORY.md` for playbooks/feedback notes added since `skill-routes.json`'s `updated` date. New playbooks → attach to the matching domain's `playbooks`. New feedback notes with hard rules → fold into the domain's `rule`.

4. **Propose, then apply.** Present the proposed diff to skill-routes.json as a short table (domain / change / evidence line from the log). Apply after the user confirms. Bump the `updated` field. Do NOT edit the vault — only skill-routes.json.

5. **Verify.** Run each changed domain through the router with a representative prompt:
   `echo '{"prompt":"<sample>"}' | python ~/.claude/hooks/skill-router.py`
   and confirm the expected chain appears.

## Constraints

- Keep the table under ~25 domains and each chain under 6 skills — the router injects into every prompt; bloat here is bloat everywhere.
- Keywords must be specific enough not to false-positive on greetings/short prompts.
- Never remove the mandatory pair (`using-superpowers`, `karpathy-coder`) — that lives in the router script, not the table.
