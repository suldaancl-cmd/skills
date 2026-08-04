#!/usr/bin/env bash
# Re-archive the trees that lost data to over-broad secret patterns.
#
# BUG being fixed: '*token*' matched design-token/, tokens.css, tokenizer.py (1306 paths);
# '*credential*' and '*oauth*' matched library/source files (574 paths). ~1880 legit paths
# were silently dropped. Real secrets are a small, NAMED set — match those, not substrings.
set -u
H="/c/Users/user"
OUT="/c/Users/user/AppData/Local/Temp/win-archives-v2"
RC="/c/Users/user/AppData/Local/Microsoft/WinGet/Links/rclone.exe"
DEST="contabo:contabo/backup/2026-07-23/windows-archives"
mkdir -p "$OUT"

# Precise secret excludes — exact filenames + true key material only.
EXCL=(--exclude='node_modules' --exclude='.venv' --exclude='venv' --exclude='__pycache__'
      --exclude='.cache' --exclude='.next' --exclude='dist' --exclude='build' --exclude='out'
      --exclude='.turbo' --exclude='target' --exclude='coverage' --exclude='.pytest_cache'
      --exclude='.expo' --exclude='*.log' --exclude='ms-playwright'
      # --- real secrets, named exactly ---
      --exclude='.env' --exclude='.env.*' --exclude='*.env'
      --exclude='keys.env' --exclude='api_keys.json' --exclude='secrets.json'
      --exclude='credentials'          # aws credentials file (exact name)
      --exclude='credentials.json'
      --exclude='token.json' --exclude='tokens.json'
      --exclude='*_token.txt' --exclude='access_token*' --exclude='refresh_token*'
      --exclude='oauth_creds.json' --exclude='*_oauth.json'
      --exclude='id_rsa*' --exclude='id_ed25519*' --exclude='id_ecdsa*'
      --exclude='*.pem' --exclude='*.p12' --exclude='*.pfx' --exclude='*.keystore')

push(){
  local name="$1"; shift
  echo "--- $name  $(date +%H:%M:%S)"
  tar "${EXCL[@]}" --ignore-failed-read -czf "$OUT/$name.tar.gz" "$@" 2>/dev/null
  echo "    built $(du -h "$OUT/$name.tar.gz" | cut -f1) -> uploading"
  "$RC" copy "$OUT/$name.tar.gz" "$DEST" --tpslimit 4 --transfers 2 \
      --s3-chunk-size 64M --s3-upload-concurrency 4 --retries 5 --low-level-retries 20 \
      --stats 60s --stats-one-line 2>&1 | tail -1
  rm -f "$OUT/$name.tar.gz"
  echo "    done"
}

push claude-skills    -C "$H/.claude" skills
push claude-_projects -C "$H/.claude" _projects
push codex            -C "$H" .codex
push agents-dot       -C "$H" .agents

echo "=== V2 ARCHIVES DONE $(date +%H:%M:%S) ==="
