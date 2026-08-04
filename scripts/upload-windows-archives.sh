#!/usr/bin/env bash
# Upload Windows tarballs to Contabo. Few large files + heavy throttle = no 429.
# Multipart uploads are resumable; re-run to finish any that failed.
set -u
RC="/c/Users/user/AppData/Local/Microsoft/WinGet/Links/rclone.exe"
SRC="/d/_BACKUP/archives"
DEST="contabo:contabo/backup/2026-07-23/windows-archives"

"$RC" copy "$SRC" "$DEST" \
  --include '*.tar.gz' \
  --tpslimit 4 --transfers 3 --checkers 3 \
  --s3-chunk-size 64M --s3-upload-concurrency 4 \
  --retries 5 --low-level-retries 20 \
  --stats 30s --stats-one-line 2>&1 | tail -30

echo "=== UPLOAD DONE $(date +%H:%M:%S) ==="
"$RC" ls "$DEST" --tpslimit 4 2>&1 | tail -30
