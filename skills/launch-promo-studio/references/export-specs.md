# Export Specs & Master-and-Derive

Render once, derive everywhere. Full matrix + sources in the studio's
`research/04-editing-post-workflow.md`. All commands use the bundled ffmpeg at
`C:\Users\user\aistudiotoday-promo\node_modules\@remotion\compositor-win32-x64-msvc\ffmpeg.exe`.

## Universal encoding (every platform)

- **Codec:** H.264 (`libx264`). X/Twitter blocks H.265; H.264 is the universal safe choice.
- **Audio:** AAC-LC, 320k, 48kHz.
- **Pixel format:** `yuv420p` (required for device compatibility).
- **Container:** MP4, `-movflags +faststart` (moov atom at head for web playback).
- **Color:** BT.709. **Quality:** `-preset slow -crf 18` (or 2-pass bitrate below).
- **Bitrate guidance:** 1080p 8–12 Mbps; 4K30 35–45 Mbps.
- **Loudness:** −14 LUFS integrated, −1.5 dBTP true peak (see `motion-sound-design`).

## Aspect ratio → platform

| Ratio | Px (1080 base) | Where |
|---|---|---|
| 16:9 | 1920×1080 / 3840×2160 | YouTube, X landscape, web hero, LinkedIn |
| 9:16 | 1080×1920 | TikTok, Reels, Shorts, Stories, X vertical |
| 1:1 | 1080×1080 | Instagram feed, LinkedIn square |
| 4:5 | 1080×1350 | Instagram feed portrait (most feed real estate) |

**Strategy:** master at **4K 16:9**, derive the rest. Never re-render per format. Keep the hero
subject/text inside the center-safe column so center-crops don't clip it (or render a dedicated
9:16 comp in Remotion when text would crop).

## Derive commands (master_4k.mp4 → social)

```bash
# 1080p 16:9 (the web/YouTube master)
ffmpeg -i master_4k.mp4 -vf "scale=1920:1080" -c:v libx264 -preset slow -crf 18 \
  -pix_fmt yuv420p -movflags +faststart -c:a aac -b:a 320k out_16x9_1080.mp4

# 9:16 vertical (center-crop)  607 = 1080 * 9/16
ffmpeg -i master_4k.mp4 -vf "scale=1920:1080,crop=607:1080:656:0,scale=1080:1920" \
  -c:v libx264 -preset slow -crf 18 -pix_fmt yuv420p -movflags +faststart \
  -c:a aac -b:a 320k out_9x16.mp4

# 1:1 square (center-crop)
ffmpeg -i master_4k.mp4 -vf "scale=1920:1080,crop=1080:1080:420:0,scale=1080:1080" \
  -c:v libx264 -preset slow -crf 18 -pix_fmt yuv420p -movflags +faststart \
  -c:a aac -b:a 320k out_1x1.mp4

# 4:5 portrait (center-crop)
ffmpeg -i master_4k.mp4 -vf "scale=1920:1080,crop=864:1080:528:0,scale=1080:1350" \
  -c:v libx264 -preset slow -crf 18 -pix_fmt yuv420p -movflags +faststart \
  -c:a aac -b:a 320k out_4x5.mp4

# 1:1 with letterbox pad instead of crop (when nothing may be cut)
ffmpeg -i master_4k.mp4 \
  -vf "scale=1080:1080:force_original_aspect_ratio=decrease,pad=1080:1080:(ow-iw)/2:(oh-ih)/2:black" \
  -c:v libx264 -preset slow -crf 18 -pix_fmt yuv420p -movflags +faststart \
  -c:a aac -b:a 320k out_1x1_pad.mp4
```

Alternatives to ffmpeg crops: Adobe MCP `video_resize`, Higgsfield MCP `reframe` (content-aware).

## Pre-ship QA checklist

- [ ] First frame is not black (it's the thumbnail).
- [ ] Text legible at mobile scale; inside title-safe margins (~5% inset).
- [ ] Loudness verified ≈ −14 LUFS, true peak < −1 dBTP (`ffmpeg ... loudnorm print_format=json`).
- [ ] `yuv420p` confirmed: `ffprobe -show_entries stream=pix_fmt out.mp4`.
- [ ] `+faststart` present (plays before fully downloaded).
- [ ] Each aspect ratio: hero subject not clipped by the crop.
- [ ] Captions burned in for sound-off social autoplay (Descript MCP can generate/burn).
- [ ] File size within platform limits.
- [ ] Versions rendered: 16:9 master + 9:16 + 1:1 (+ 4:5 if Instagram feed).
