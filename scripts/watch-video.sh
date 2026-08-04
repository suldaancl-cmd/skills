#!/usr/bin/env bash
# Reusable: turn any video URL or file path into still frames Claude can read.
# Usage:
#   ./watch-video.sh <URL-or-path> [slug] [fps]
# Output:
#   ~/.claude/shared-videos/<slug>/frame_%03d.jpg + meta.txt
# fps default 1 (1 frame per second). For short reels use 2; for trailers 0.5.

set -e

INPUT="${1:?usage: watch-video.sh <URL-or-path> [slug] [fps]}"
SLUG="${2:-clip-$(date +%s)}"
FPS="${3:-1}"

ROOT="$HOME/.claude/shared-videos/$SLUG"
mkdir -p "$ROOT"
cd "$ROOT"

FFMPEG="/c/Users/user/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe/ffmpeg-8.1-full_build/bin/ffmpeg.exe"

if [[ "$INPUT" =~ ^https?:// ]]; then
  echo ">> downloading $INPUT"
  python -m yt_dlp \
    --no-playlist \
    --no-warnings \
    --restrict-filenames \
    --merge-output-format mp4 \
    -o "source.%(ext)s" \
    --write-info-json --write-description \
    "$INPUT" 2>&1 | tail -10
  SRC="$(ls source.* 2>/dev/null | grep -E '\.(mp4|mov|mkv|webm)$' | head -1)"
else
  cp "$INPUT" ./source.mp4
  SRC="source.mp4"
fi

if [[ -z "$SRC" || ! -f "$SRC" ]]; then
  echo "!! no source video produced — login wall, geo block, or bad URL"
  echo "   alternatives: open the link in a browser, save the .mp4, then pass that path."
  exit 1
fi

echo ">> probing"
"$FFMPEG" -hide_banner -i "$SRC" 2>&1 | grep -E "(Duration|Stream)" | head -5 > meta.txt
cat meta.txt

echo ">> extracting frames at ${FPS} fps"
rm -f frame_*.jpg
"$FFMPEG" -y -i "$SRC" -vf "fps=${FPS},scale='min(1280,iw)':'-2':flags=lanczos" -q:v 4 frame_%03d.jpg 2>&1 | tail -3

COUNT=$(ls frame_*.jpg 2>/dev/null | wc -l)
echo "DONE — $COUNT frames in $ROOT"
ls frame_*.jpg | head -5
