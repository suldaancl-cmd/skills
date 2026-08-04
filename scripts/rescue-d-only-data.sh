#!/usr/bin/env bash
# Rescue the ~5 GB that exists ONLY on the flaky D: drive.
# Reads D: once -> tars to C: (healthy) -> uploads -> deletes local copy.
# --ignore-failed-read so one unreadable file can't kill a whole archive.
set -u
OUT="/c/Users/user/AppData/Local/Temp/d-rescue"
RC="/c/Users/user/AppData/Local/Microsoft/WinGet/Links/rclone.exe"
DEST="contabo:contabo/backup/2026-07-23/d-drive-only"
mkdir -p "$OUT"

EXCL=(--exclude='node_modules' --exclude='__pycache__' --exclude='.venv' --exclude='venv'
      --exclude='*.log' --exclude='.env' --exclude='*.env' --exclude='*token*'
      --exclude='*credential*' --exclude='*.pem' --exclude='*.key' --exclude='id_rsa*')

push(){
  local name="$1" src="$2"
  [ -d "$src" ] || { echo "SKIP missing: $src"; return; }
  echo "--- $name  $(date +%H:%M:%S)"
  tar "${EXCL[@]}" --ignore-failed-read -czf "$OUT/$name.tar.gz" -C "$(dirname "$src")" "$(basename "$src")" 2>/dev/null
  local rc=$?
  local sz; sz=$(du -h "$OUT/$name.tar.gz" 2>/dev/null | cut -f1)
  echo "    built $sz (tar rc=$rc) -> uploading"
  "$RC" copy "$OUT/$name.tar.gz" "$DEST" --tpslimit 4 --transfers 2 \
      --s3-chunk-size 64M --s3-upload-concurrency 4 --retries 5 --low-level-retries 20 \
      --stats 60s --stats-one-line 2>&1 | tail -1
  rm -f "$OUT/$name.tar.gz"
  echo "    done"
}

push backups-dir        "/d/_BACKUPS"
push ugc-recovered      "/d/UGC-recovered"
push site-mirrors       "/d/site-mirrors"
push user-d             "/d/user d"
push webjoud            "/d/webjoud"
push claude-backup-old  "/d/ClaudeBackup"
push ai-web             "/d/Ai web"
push videoediting-rec   "/d/videoediting-recovery"

echo "=== D-RESCUE DONE $(date +%H:%M:%S) ==="
"$RC" ls "$DEST" --tpslimit 3 2>&1 | awk '{printf "  %8.1f MB  %s\n", $1/1048576, $2}'
