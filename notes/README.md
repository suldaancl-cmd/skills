# notes — the git-backed slice of the second brain

The Obsidian vault lives at `~/.claude/projects/C--Users-user--claude-skills/memory/` and is deliberately excluded from this repo (see the rationale in `.gitignore`): it holds session transcripts, staged drafts, and credentials.

This folder is the narrow exception. Cloud sessions — Claude Code on the web, GitHub-triggered runs, the vmi mirror — cannot reach the Windows vault, so link-derived and research-derived notes written from those sessions land here instead, and reach the vault by `git pull`.

Rules:

- **Distilled notes only.** No transcripts, no raw captures, no credentials, no prompt logs. If it would be unsafe on GitHub, it does not belong here.
- **Vault naming applies:** `playbook_*.md`, `reference_*.md`, `feedback_*.md`.
- **MERGE, never replace.** A note that already exists in the vault gets extended, not overwritten.
- Promote into the vault and link from `MEMORY.md` on the next local session; attach to its domain in `skill-routes.json` so the router surfaces it.
