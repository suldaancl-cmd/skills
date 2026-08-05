#!/usr/bin/env bash
# Mirror this skill to Codex and the vmi (Hermes) server.
#
# ~/.claude/skills/ is already Syncthing-live to vmi, so the rsync is a
# verification pass that reports drift rather than the primary transport.
# Codex keeps its own copy and does need the explicit copy.
set -uo pipefail

SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
NAME="$(basename "$SKILL_DIR")"

echo "syncing skill: $NAME"
echo "source: $SKILL_DIR"
echo

# ── Codex ────────────────────────────────────────────────────────────────────
CODEX="$HOME/.codex/skills"
if [ -d "$CODEX" ]; then
  mkdir -p "$CODEX/$NAME"
  cp -r "$SKILL_DIR/." "$CODEX/$NAME/"
  echo "codex   OK  -> $CODEX/$NAME ($(find "$CODEX/$NAME" -type f | wc -l) files)"
else
  echo "codex   SKIP (no $CODEX on this machine)"
fi

# ── vmi / Hermes ─────────────────────────────────────────────────────────────
# Two targets: the Claude skill dir the fleet loads, and the Hermes knowledge
# mount so Markdown-job agents can read the same workflow.
# Git Bash on Windows ships no rsync, so prefer it when present and fall back
# to a tar-over-ssh stream, which needs nothing but ssh on both ends.
push() {  # push <local-dir> <remote-dir>
  ssh vmi "mkdir -p '$2'" 2>/dev/null || return 1
  if command -v rsync >/dev/null 2>&1; then
    rsync -az --delete "$1/" "vmi:$2/"
  else
    tar -C "$1" -cf - . | ssh vmi "tar -C '$2' -xf -"
  fi
}

if ssh -o ConnectTimeout=8 -o BatchMode=yes vmi true 2>/dev/null; then
  push "$SKILL_DIR" "/root/.claude/skills/$NAME" \
    && echo "vmi     OK  -> /root/.claude/skills/$NAME" \
    || echo "vmi     FAIL (see error above)"

  if ssh vmi "[ -d /root/.hermes/workspace/knowledge/skills ]" 2>/dev/null; then
    ssh vmi "mkdir -p /root/.hermes/workspace/knowledge/skills/$NAME" 2>/dev/null
    tar -C "$SKILL_DIR" -cf - SKILL.md references | \
      ssh vmi "tar -C /root/.hermes/workspace/knowledge/skills/$NAME -xf -" \
      && echo "hermes  OK  -> knowledge/skills/$NAME (SKILL.md + references)"
  else
    echo "hermes  SKIP (knowledge/skills not present)"
  fi

  echo
  echo "remote file count: $(ssh vmi "find /root/.claude/skills/$NAME -type f | wc -l" 2>/dev/null || echo '?')"
  echo "local  file count: $(find "$SKILL_DIR" -type f | wc -l)"
  echo "(counts should match; a mismatch means Syncthing drift, not a copy failure)"
else
  echo "vmi     SKIP (ssh vmi unreachable — Syncthing will carry it when the box is up)"
fi
