#!/usr/bin/env bash
# Rebuild the 6 archives lost when D: dropped. Sources are all on C: (healthy SSD).
# Stages on C: — deliberately NOT D:, which is corrupting.
set -u
H="/c/Users/user"
OUT="/c/Users/user/AppData/Local/Temp/win-archives"
RC="/c/Users/user/AppData/Local/Microsoft/WinGet/Links/rclone.exe"
DEST="contabo:contabo/backup/2026-07-23/windows-archives"
mkdir -p "$OUT"

EXCL=(--exclude='node_modules' --exclude='.venv' --exclude='venv' --exclude='__pycache__'
      --exclude='.cache' --exclude='.next' --exclude='dist' --exclude='build' --exclude='out'
      --exclude='.turbo' --exclude='target' --exclude='coverage' --exclude='.pytest_cache'
      --exclude='.expo' --exclude='*.log' --exclude='ms-playwright'
      --exclude='.env' --exclude='*.env' --exclude='keys.env' --exclude='api_keys.json'
      --exclude='*token*' --exclude='*credential*' --exclude='*.pem' --exclude='*.key'
      --exclude='id_rsa*' --exclude='id_ed25519*' --exclude='*oauth*' --exclude='*.p12')

# tar one archive, upload it, delete local copy (keeps peak C: usage low)
push(){
  local name="$1"; shift
  echo "--- $name  $(date +%H:%M:%S)"
  tar "${EXCL[@]}" -czf "$OUT/$name.tar.gz" "$@" 2>/dev/null
  local sz; sz=$(du -h "$OUT/$name.tar.gz" 2>/dev/null | cut -f1)
  echo "    built $sz -> uploading"
  "$RC" copy "$OUT/$name.tar.gz" "$DEST" --tpslimit 4 --transfers 2 \
      --s3-chunk-size 64M --s3-upload-concurrency 4 --retries 5 --low-level-retries 20 \
      --stats 60s --stats-one-line 2>&1 | tail -1
  rm -f "$OUT/$name.tar.gz"
  echo "    uploaded + local copy removed"
}

push codex        -C "$H" .codex
push agents-dot   -C "$H" .agents
push adal-dot     -C "$H" .adal

# top-level .claude config files
cfg=$(cd "$H/.claude" && ls CLAUDE.md settings.json settings.local.json skill-routes.json skill-usage.jsonl 2>/dev/null)
push claude-config -C "$H/.claude" $cfg

# home project folders (keep .git, drop node_modules)
mapfile -t proj < <(cd "$H" && for d in */; do
  case "$d" in AppData/|OneDrive/|Documents/|Downloads/|Desktop/|Videos/|Music/|Pictures/|Contacts/|Favorites/|Links/|Searches/|"Saved Games"/|node_modules/|_projects/) continue;; esac
  echo "${d%/}"
done)
push home-projects -C "$H" "${proj[@]}"

# agent config dot-dirs (skip huge regenerable)
mapfile -t dots < <(cd "$H" && for d in .*/; do
  n="${d%/}"
  case "$n" in .|..|.npm-cache|.vscode|.u2net|.local|.git|.m2|.npm|.cache|.thumbnails|.claude|.codex|.agents|.adal) continue;; esac
  [ -L "$H/$n" ] && continue
  echo "$n"
done)
push agent-configs -C "$H" "${dots[@]}"

echo "=== REMAINING ARCHIVES DONE $(date +%H:%M:%S) ==="
"$RC" ls "$DEST" --tpslimit 3 2>&1 | awk '{printf "  %8.1f MB  %s\n", $1/1048576, $2}'
