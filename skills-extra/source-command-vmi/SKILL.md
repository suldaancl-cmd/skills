---
name: "source-command-vmi"
description: "Dispatch the rest of this prompt to Codex on vmi VPS (47GB RAM) — run heavy task on the server, stream output back. Saves local RAM."
---

# source-command-vmi

Use this skill when the user asks to run the migrated source command `vmi`.

## Command Template

# /vmi — run task on the VPS

You are dispatching the user's task to Codex on the **vmi VPS** (37.60.243.30, 47 GB RAM, Codex 2.1.114) instead of running it locally. This frees up local RAM for the user's other work.

**The task to dispatch is everything after `/vmi` in the user message.** Treat it as a complete, self-contained prompt for a fresh Codex session running on vmi — that session has no memory of this conversation.

## What to do

1. Take the user's prompt (everything after `/vmi`).
2. Pipe it into the vmi `cv-run` wrapper via SSH:
   ```
   echo "<task>" | ssh vmi 'CV_CWD=/root/work /root/bin/cv-run'
   ```
   Use a heredoc / single `Bash` tool call. Do not split into many SSH calls.
3. Stream the output back to the user verbatim.
4. After it finishes, tell the user the log path on vmi (cv-run prints it as the last line) and that it will mirror back to `~/.Codex/from-vmi/logs/cv/` within 30 minutes via the `ClaudeSyncFromVmi` task.

## When to use vs. not use

- **Use `/vmi` for:** long codebase scans, multi-file refactors, big test runs, RAM-hungry MCP tools, anything you'd hesitate to run locally.
- **Do not use `/vmi` for:** edits to local files (vmi can't see them), interactive flows that need follow-up turns (cv-run is one-shot), tasks that need local browser/preview tools.

If you need vmi for working on a specific repo, set `CV_CWD` to that path. The user's vmi has these likely workspaces: `/root/work` (default scratch), `/root/.hermes/`, `/root/vault/`, `/root/.Codex/`.

## If the user passed no task

If `/vmi` is invoked with no arguments, just print:
- `cv "<task>"` from any PowerShell to dispatch from outside Codex
- `cv -Interactive` for an SSH session into Codex on vmi
- `cv -Tail` to follow the most recent vmi cv log
