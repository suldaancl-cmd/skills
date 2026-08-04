---
name: read-link
description: When the user pastes any social-media or video URL (TikTok, Instagram, YouTube, X/Twitter, Facebook, Reddit, Vimeo, generic video page) and you cannot natively read it via WebFetch, invoke this skill BEFORE answering. It downloads the media + metadata locally so you can actually see what's in the link instead of guessing or apologizing. Always use this skill when ≥1 URL pointing to a social-media post, short-form video, livestream replay, or any .mp4/.webm/.mov file appears in the user's message — even if WebFetch returns *some* HTML, because that HTML almost never contains the actual video, full caption, or rendered post.
---

# read-link — make Claude actually see social/video links

## Why this exists

`WebFetch` reads static HTML. Social platforms serve login walls, JS shells, or anti-bot pages to non-browser clients, and even when HTML loads it doesn't contain video frames or audio. Without this skill you end up saying "I can't access that link" — which is exactly what the user got tired of hearing.

## When to invoke

- Any TikTok / Instagram / YouTube / Twitter (X) / Facebook / Reddit / Threads / Vimeo / Twitch / Bilibili URL
- Any direct video file URL (`.mp4`, `.webm`, `.mov`, `.m3u8`)
- Any "I want you to look at this" link to a post that contains media
- When the user says "watch this", "see this video", "check this reel/short/clip"

If the URL is a plain article (no embedded video, no anti-bot wall), prefer `WebFetch` — this skill is overkill for that.

## yt-dlp invocation note

Installed via `winget install yt-dlp.yt-dlp`. Binary at `C:\Users\user\AppData\Local\Microsoft\WinGet\Links\yt-dlp.exe`.

Use plain `yt-dlp` in commands. If PATH hasn't refreshed yet (fresh install, current shell), use the absolute path. Both forms work — pick whichever doesn't 127.

**JS runtime warning:** YouTube extraction prefers a JS runtime. Node is already installed (`node --version`), so add `--js-runtimes "node:C:/Program Files/nodejs/node.exe"` to YouTube commands if a `No supported JavaScript runtime` warning blocks a format. For TikTok/IG/X this isn't needed.

## Pipeline (3-tier fallback)

### Tier 1 — yt-dlp (default)

```bash
URL="<the url>"
HASH=$(echo -n "$URL" | sha1sum | cut -c1-12)
DIR="$HOME/.claude/tmp/links/$HASH"
mkdir -p "$DIR"

yt-dlp \
  -o "$DIR/%(id)s.%(ext)s" \
  --write-info-json \
  --write-thumbnail \
  --write-auto-subs --sub-langs "en,ar" --convert-subs srt \
  --no-playlist \
  --restrict-filenames \
  "$URL"
```

Result: video file + thumbnail.jpg + info.json + subtitles.srt in `$DIR`.

### Tier 2 — auth fallback

If Tier 1 errors with `Login required`, `Private video`, `403`, or returns 0 bytes:

```bash
yt-dlp \
  --cookies-from-browser chrome \
  -o "$DIR/%(id)s.%(ext)s" \
  --write-info-json --write-thumbnail \
  --write-auto-subs --sub-langs "en,ar" --convert-subs srt \
  "$URL"
```

If Chrome isn't the user's primary browser, try `firefox`, `edge`, `brave` in that order.

### Tier 3 — Playwright MCP (last resort)

If both yt-dlp tiers fail (rare — e.g., paywalled blog with embedded video, custom CDN):

```
mcp__playwright__browser_navigate { url: "$URL" }
mcp__playwright__browser_snapshot       # accessibility tree
mcp__playwright__browser_take_screenshot # save PNG to $DIR/page.png
```

Read the screenshot + snapshot text. Note: this gets the *page*, not the video — usable for caption/description but not for "see what's in the video".

## Reading the downloaded media

After Tier 1 or 2 succeeds:

```bash
VIDEO=$(ls "$DIR"/*.mp4 "$DIR"/*.webm "$DIR"/*.mov 2>/dev/null | head -1)
ffmpeg -y -i "$VIDEO" -vf "fps=1/2,scale=720:-1" "$DIR/frame_%03d.jpg" 2>&1 | tail -3
```

This yields ~1 frame every 2 seconds at 720p — small enough to read fast, dense enough to follow what's happening.

Then read in this order:
1. `info.json` → title, description, uploader, duration, view count, hashtags
2. `*.srt` → transcript / captions (if available)
3. Each `frame_*.jpg` via the Read tool → visual content
4. `*.jpg` (thumbnail) → poster frame

Synthesize: describe what's happening visually + quote the most important caption/transcript line + state platform + uploader.

## Special-case URLs

| Domain | Notes |
|---|---|
| `instagram.com/reel/`, `/p/`, `/stories/` | Often needs Tier 2 cookies. Stories expire — fail gracefully. |
| `tiktok.com/@user/video/`, `vm.tiktok.com/` | Tier 1 usually works. For region-blocked, add `--geo-bypass-country US`. |
| `x.com/.../status/`, `twitter.com/.../status/` | Tier 1 works for public tweets with media. For protected accounts → Tier 2. |
| `youtube.com/shorts/`, `youtu.be/`, `youtube.com/watch` | Tier 1 always works for public. Members-only → Tier 2. |
| `facebook.com/.../videos/`, `fb.watch/` | Often needs Tier 2. |
| Direct `.mp4` / `.m3u8` | yt-dlp handles both. For HLS, downloads + concatenates segments. |

## Pass-through to Higgsfield

If the user wants to use the downloaded media as a generation reference:

```
mcp__94e5225e-fb8d-478d-95a9-201307e1a653__media_upload
  with the local file path
→ then mcp__...__generate_video / generate_image
  with the returned media id in `medias`
```

This is the killer feature — user pastes "make me an ad like this TikTok" and the workflow Just Works.

## Deep Dive Analysis Protocol (MANDATORY)

After extraction, ALWAYS do a full deep dive. This is the most important part — extraction without analysis is useless.

### Phase 1: Full Content
1. **Who** — author name, handle, what they do, their background
2. **Full text/transcript** — every word, not a summary. Paste the actual content

### Phase 2: Explain Like I'm Building It
Break down what the person is actually teaching or revealing:

3. **Core message** — what's the ONE thing they're saying?
4. **Step-by-step breakdown** — if they describe a process/method/system, lay it out as numbered steps
5. **Business model deconstruction** — how does this person make money? Revenue streams, pricing, target audience, funnel
6. **Tech stack / tools mentioned** — every software, platform, framework, API they name or imply. Be specific.
7. **Strategy pattern** — what play are they running? (content marketing → course, freemium SaaS, agency arbitrage, etc.)

### Phase 3: Study It
8. **Why it works** — the psychology / mechanics behind their approach
9. **What they SAID vs what they DIDN'T say** — the most important part. Split it into two columns:
   - **Said:** the claims they made out loud
   - **Didn't say:** what they skipped. Check each of these and call out the ones that are missing:
     - Real income numbers (gross vs net, after refunds, after ad spend, after tax)
     - How long it actually took before this worked
     - How many failed tries before this one
     - Starting capital they had
     - Network or connections they used
     - Hidden costs (tools, team, ads, mentor fees, software subscriptions)
     - Failure rate of students or followers who tried the same thing
     - Whether they actually still do this or just teach it now
     - Survivorship bias (how many people tried this, how many failed quietly)
     - Platform risk (one algorithm change kills the whole business)
     - Legal, tax, or regulatory traps
     - Skills they already had before starting (degree, prior career, language, contacts)
10. **Who else does this** — comparable people / companies using the same playbook
11. **Market timing** — why now? What trend are they riding?

### Phase 3.5: Reality Check
12. **Tone audit** — fear, urgency, scarcity, FOMO language? Score 1-10 on manipulation level. Quote the most loaded phrase
13. **Proof check** — did they SHOW evidence (screenshots, dashboards, bank statements, before/after) or just CLAIM? List each piece of proof + verdict (real / staged / unverifiable)
14. **Math check** — do the numbers add up? If "I made $50K in 30 days" → break it down: how many sales, at what price, what conversion rate, what ad spend. Flag any impossible math
15. **Comment vibe** — quick read of top comments: real questions and stories, or generic "amazing!" bot-like replies?
16. **Timing & geography** — is this still relevant in 2026? Does it work in MENA / your country, or only in the US?
17. **Skill gap** — what skills does the creator assume you already have? List the hidden prerequisites
18. **The catch** — the ONE part they made sound easy that actually isn't. Name it directly

### Phase 4: Make It Actionable for Karim
19. **Can Karim replicate this?** — yes / no + what's needed (skills, capital, time, team)
20. **First 3 steps to start** — concrete actions, not vague advice
21. **What to steal** — specific tactics, frameworks, wording, positioning to adapt
22. **What to skip** — parts that don't fit Karim's situation (location, budget, skills)
23. **Revenue estimate** — if Karim executed this well, realistic monthly range in USD
24. **Verdict** — pursue / pass / pursue-with-modification. One line, plain English

### Format (English-only mode — 2026-05-22)
- **English only** for now. Arabic output is paused until Claude Code renders RTL `<div dir="rtl">` blocks reliably. Switch back to bilingual once that works
- **Plain simple English** — short sentences, no jargon walls, no flowery language
- English for everything: prose, technical terms, tool names, code
- **Bold** for key terms, numbers, and the verdict
- Use bullet points, not walls of text
- If the content is shallow, say so honestly — don't inflate garbage
- One direction per block (still applies the moment Arabic returns)

## Verifiable goals (Karpathy)

For a given link, the skill is successful when ALL of:
- Tier 1 or 2 produced a video/image file > 10 KB OR Tier 3 produced a non-empty screenshot
- `info.json` exists and has a `title` field
- I can name at least one concrete visual element in the media
- I can quote either the title, caption, or one transcript line
- **The Deep Dive Analysis (Phases 1-4) is delivered, not skipped**

If any of those fail, state the specific failure — don't pretend success.

## Out of scope

- Local Whisper transcription (heavy install; yt-dlp's auto-subs cover most needs)
- Persistent cache (the temp dir is per-URL; old downloads cleared by user)
- Comments / replies extraction (use Playwright if needed)
- Live-stream real-time capture (only replays after they end)
