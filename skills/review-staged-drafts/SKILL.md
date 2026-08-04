---
name: review-staged-drafts
description: Review and promote/discard draft memory notes that the SessionEnd hook staged from prior sessions. Use when the user says "review staged drafts", "what got staged", "promote staged notes", "review last session learnings", or when the SessionStart prime mentions N drafts waiting. This is the consent gate for cross-session memory writes — never auto-commit; user picks per-draft.
---

# Review staged drafts — consent gate for cross-session memory

The SessionEnd hook (`~/.claude/hooks/session-end-stage.py`) walks each session's transcript and stages candidate memory notes (feedback_*.md / reference_*.md / playbook_*.md) into `~/.claude/snapshots/staged_writes/<session-id>/`. **Nothing ever lands in the vault automatically.** This skill is the human-in-the-loop step.

## Workflow

### 1. Enumerate

```bash
ls -lt ~/.claude/snapshots/staged_writes/*/*.md
```

If empty: report "no staged drafts" and stop.

### 2. Show each draft, one at a time

For each `.md` file:

```
---
Draft N/M: <filename>
Session: <parent-dir>
Type: <feedback / reference / playbook> (inferred from prefix)

Preview (first ~15 lines):
<head of file>

Existing related vault note (if any): <path>
---
```

Use Glob `~/.claude/projects/C--Users-user--claude-skills/memory/<same-prefix>_*.md` to detect a related existing note that this draft could merge into vs. become its own file.

### 3. Per-draft choice (offer 4 options, not multi-select)

| Option | Action |
|---|---|
| **a** Promote as-is | Move file to vault root with same name. If a vault file with the same name exists, MERGE — append the new content under a `## YYYY-MM-DD update` heading. Update MEMORY.md with a new index line if it's a brand-new file. |
| **b** Edit then promote | Show the draft in full; let user inline-edit the content via chat; then perform option (a) on the edited version |
| **c** Discard | `rm` the staged file |
| **d** Skip for now | Leave the staged file in place; user revisits next session |

After each choice, move to the next draft. At the end: clean up the empty session-id subdirs.

## Iron rules

- **Never write to the vault without explicit per-draft user approval.** "Promote all" is NOT an option — each draft gets its own decision.
- **Never delete a draft without explicit "discard" or successful promote.** Option (d) leaves it in place.
- **Always check for an existing related vault note before promoting** as a brand-new file. Merging into an existing `feedback_*.md` is usually right — keeps the vault tight.
- **MEMORY.md updates are additive only.** Per the user's standing `feedback_merge_never_replace.md` rule.
- **Promoted file path = vault root**, e.g. `~/.claude/projects/C--Users-user--claude-skills/memory/feedback_<topic>.md`. Never a subfolder.

## Output style

Tight. One draft at a time. No essays. The user has been clear they want minimal vault writes — your job is to make sure each write earns its keep.

## After completion

Report:
- N drafts promoted (with vault paths)
- N drafts merged into existing notes
- N drafts discarded
- N drafts skipped (still in staging)
- MEMORY.md update summary (new index lines added)
