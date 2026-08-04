#!/usr/bin/env bash
# Tar Windows trees into few large archives (keep .git, drop node_modules/caches/secrets).
# Small-file trees as tarballs avoid Contabo per-object 429 rate limits.
set -u
H="/c/Users/user"
OUT="/d/_BACKUP/archives"
mkdir -p "$OUT"

EXCL=(--exclude='node_modules' --exclude='.venv' --exclude='venv' --exclude='__pycache__'
      --exclude='.cache' --exclude='.next' --exclude='dist' --exclude='build' --exclude='out'
      --exclude='.turbo' --exclude='target' --exclude='coverage' --exclude='.pytest_cache'
      --exclude='.expo' --exclude='*.log' --exclude='ms-playwright'
      --exclude='.env' --exclude='*.env' --exclude='keys.env' --exclude='api_keys.json'
      --exclude='*token*' --exclude='*credential*' --exclude='*.pem' --exclude='*.key'
      --exclude='id_rsa*' --exclude='id_ed25519*' --exclude='*oauth*' --exclude='*.p12')

tarit(){ # name  src-parent  src-leaf
  local name="$1" parent="$2" leaf="$3"
  [ -d "$parent/$leaf" ] || { echo "SKIP missing: $parent/$leaf"; return; }
  echo "--- $name $(date +%H:%M:%S)"
  tar "${EXCL[@]}" -czf "$OUT/$name.tar.gz" -C "$parent" "$leaf" 2>/dev/null
  echo "    $(du -h "$OUT/$name.tar.gz" | cut -f1)  $name.tar.gz"
}

tarit claude-skills     "$H/.claude" skills
tarit claude-projects   "$H/.claude" projects
tarit claude-_projects  "$H/.claude" _projects
tarit claude-plugins    "$H/.claude" plugins
tarit claude-snapshots  "$H/.claude" snapshots
tarit notion-backup     "$H/.claude" notion-backup
tarit claude-hooks      "$H/.claude" hooks
tarit claude-scripts    "$H/.claude" scripts
tarit codex             "$H" .codex
tarit agents-dot        "$H" .agents
tarit adal-dot          "$H" .adal

# top-level .claude config files (small)
tar -czf "$OUT/claude-config.tar.gz" -C "$H/.claude" \
  $(cd "$H/.claude" && ls CLAUDE.md settings.json settings.local.json skill-routes.json skill-usage.jsonl 2>/dev/null) 2>/dev/null
echo "    $(du -h "$OUT/claude-config.tar.gz" 2>/dev/null | cut -f1)  claude-config.tar.gz"

# home project folders -> ONE archive (keep .git, drop node_modules)
echo "--- home-projects $(date +%H:%M:%S)"
mapfile -t proj < <(cd "$H" && for d in */; do
  case "$d" in AppData/|OneDrive/|Documents/|Downloads/|Desktop/|Videos/|Music/|Pictures/|Contacts/|Favorites/|Links/|Searches/|"Saved Games"/|node_modules/|_projects/) continue;; esac
  echo "${d%/}"
done)
tar "${EXCL[@]}" -czf "$OUT/home-projects.tar.gz" -C "$H" "${proj[@]}" 2>/dev/null
echo "    $(du -h "$OUT/home-projects.tar.gz" | cut -f1)  home-projects.tar.gz (${#proj[@]} folders)"

# agent config dot-dirs (skip huge regenerable + secrets-heavy)
echo "--- agent-configs $(date +%H:%M:%S)"
mapfile -t dots < <(cd "$H" && for d in .*/; do
  n="${d%/}"
  case "$n" in .|..|.npm-cache|.vscode|.u2net|.local|.git|.m2|.npm|.cache|.thumbnails|.claude|.codex|.agents|.adal) continue;; esac
  [ -L "$H/$n" ] && continue
  echo "$n"
done)
tar "${EXCL[@]}" -czf "$OUT/agent-configs.tar.gz" -C "$H" "${dots[@]}" 2>/dev/null
echo "    $(du -h "$OUT/agent-configs.tar.gz" | cut -f1)  agent-configs.tar.gz (${#dots[@]} dirs)"

echo "=== TAR DONE $(date +%H:%M:%S) ==="
ls -lh "$OUT"/*.tar.gz | awk '{print $5, $9}'
du -sh "$OUT"
