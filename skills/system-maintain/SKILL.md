---
name: system-maintain
description: Weekly maintenance loop for Karim's Claude Code system — router health, skill drift, usage-log mining, memory hygiene, hook health, staged-draft backlog. Invoke when the user says "maintain the system", "system health", "weekly maintenance", "check my setup", or roughly weekly during /si:review. Produces a scorecard and fixes what it can (user-gated where required).
---

# System Maintain

One pass = one scorecard + fixes. The system under maintenance: skill routing (`skill-routes.json` + `hooks/skill-router.py`), enforcement (`hooks/skill-stop-check.py` + usage log), gates (`~/.claude/AGENTS.md`), memory vault, and the session hooks.

## Checklist (run in order, report PASS/FIX/BLOCKED per item)

1. **Hooks alive.** Every hook in `settings.json` points at an existing file and runs clean:
   `echo '{"prompt":"test design prompt"}' | python ~/.claude/hooks/skill-router.py` must emit valid JSON. Do the same smoke test for the Stop hook with a fabricated transcript. A hook that throws = silent loss of the whole enforcement layer.

2. **Router drift.** Every skill named in `skill-routes.json` resolves — a folder in `~/.claude/skills/`, a plugin-namespaced skill, or a session-registered skill. Every playbook path exists in the vault. Broken refs → fix immediately (no consent needed; the table is config, not vault).

3. **Usage mining.** Run the `skill-router-tune` procedure on `~/.claude/skill-usage.jsonl` if it has ≥30 new entries since the table's `updated` date. Its proposals are user-gated.

4. **New knowledge routed.** Diff vault playbook/feedback/reference files newer than `skill-routes.json`'s `updated` field. Each new note that changes how a domain should work → attach to that domain's `playbooks` or fold into its `rule`.

5. **Skill bloat delta.** Compare the skill-quality-gate count against last run (track in the scorecard file). Growth >10% without an install log in MEMORY.md → flag for a categorized audit (pruning itself is always user-confirmed, per feedback_skill_bloat_audit).

6. **Staged-drafts backlog.** Report the count in `~/.claude/snapshots/staged_writes/`. Over ~50 → nudge: the Promote gate is the loop's human bottleneck; offer to run `review-staged-drafts` in batches.

7. **Memory hygiene.** MEMORY.md index lines all point at existing files; no obvious duplicates (if found, propose `consolidate-memory`). Superseded notes marked, not deleted.

8. **Sync health.** `~/.claude/skills/` is Syncthing-mirrored to vmi — spot-check one recently-edited skill file exists on the vmi side (`ssh vmi ls`). Divergence breaks the loader on both machines.

9. **Stale counts.** Grep CLAUDE.md, hook messages, and skills/CLAUDE.md for hardcoded skill counts that no longer match reality; update them.

## Output

Write the scorecard to `~/.claude/snapshots/maintenance_<date>.md` (9 rows: item / status / action taken / evidence) and show it. Fix-in-place what needs no consent; list user-gated items as a short menu at the end. Never edit the vault directly — proposals only.
