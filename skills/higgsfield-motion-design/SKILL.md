---
version: 0.1.0
name: higgsfield-motion-design
description: Use when the user wants a multi-scene motion-design video with on-screen text — "motion design video/ad", "scroll-stop motion ad", "bushido/stoic/samurai quote video", "kinetic typography ad", "moodboard to video", "Higgsfield motion design", "Claude × Higgsfield motion video", or any short-form aesthetic ad built from 6 scene cards with baked-in copy. NOT for single-shot image-to-video (higgsfield-generate), marketplace product cards (higgsfield-marketplace-cards), or talking-head UGC (higgsfield-generate Marketing Studio).
argument-hint: "<theme> [--lines \"L1|L2|L3|L4|L5|L6\"] [--aspect 9:16|16:9|1:1] [--no-pinterest]"
allowed-tools: Bash, Read, Write
---

# Higgsfield Motion Design

Three-phase pipeline that turns a theme into a finished motion-design video. Built around the workflow Higgsfield AI demoed publicly on 2026-05-18 ([source](https://x.com/higgsfield/status/2056427804531773598)). This skill is an orchestrator — it doesn't reinvent generation, it sequences `mcp__...higgsfield__*` calls plus a Pinterest scrape.

## When this skill fires

Karim's typical asks that land here:
- *"Make me a motion-design ad about discipline."*
- *"Bushido quote video, 30 seconds, 9:16 for IG."*
- *"Time is the only currency — turn it into a Higgsfield motion video."*
- *"Pull samurai refs and make me a Seedance video like that Higgsfield demo."*

If the user only wants a single image or a single image-to-video clip, hand off to `higgsfield-generate` and stop. This skill earns its keep when the deliverable is a multi-scene narrative piece with on-screen text.

## Output contract (verifiable goals)

Skill is successful when ALL of the following are true:

1. A working directory under `~/.claude/outputs/motion-design/<slug>-<timestamp>/` exists.
2. Inside that dir: `references/` has ≥4 Pinterest reference images saved locally.
3. Inside that dir: `storyboard/` has 6 PNGs (`scene_1.png` … `scene_6.png`) each with the intended on-screen text legible.
4. Inside that dir: `video/final.mp4` exists OR a Higgsfield Seedance job URL is recorded in `video/final_url.txt`.
5. The 6 on-screen lines are written verbatim in `storyboard/lines.txt` (one per line, in order).
6. A `MANIFEST.md` summarizing theme, aspect ratio, lines, model IDs, and result URL.

If any of these fail, state the specific failure — don't pretend success.

## Inputs

From the user:
- **Theme / concept** — single sentence, e.g. *"the discipline of a samurai"*, *"time is the only currency"*, *"weekend skate culture in Miami"*.
- **6 on-screen lines** — optional. If absent, generate them (see Phase 2). One short punchy line per scene; 1–5 words each is the strongest move.
- **Aspect ratio** — default `9:16` (IG/TikTok). Accept `16:9`, `1:1`.
- **Pinterest refs** — opt out with `--no-pinterest` if the user wants Claude to skip moodboarding.

Auto-derive a **slug** from the theme (lowercase, kebab) and a **timestamp** (`YYYYMMDD-HHMM`).

## Phase 0 — Bootstrap and gating

Run these once at the top:

1. Confirm the Higgsfield MCP tools are reachable. If `mcp__94e5225e-fb8d-478d-95a9-201307e1a653__balance` is not callable, ask the user to start/refresh the Higgsfield MCP and stop until they confirm.
2. Make the working directory:
   ```bash
   THEME_SLUG=$(echo "<theme>" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]/-/g' | sed 's/-\+/-/g; s/^-\|-$//g')
   TS=$(date +%Y%m%d-%H%M)
   WORKDIR="$HOME/.claude/outputs/motion-design/${THEME_SLUG}-${TS}"
   mkdir -p "$WORKDIR/references" "$WORKDIR/storyboard" "$WORKDIR/video"
   echo "$WORKDIR"
   ```
3. Write a one-line theme + slug record to `$WORKDIR/MANIFEST.md` (you'll append to it as you go).

## Phase 1 — Pinterest references

Goal: 4–12 aesthetic stills that lock the visual language *before* generating storyboard frames. This grounds GPT Image 2 with concrete style cues instead of guesswork.

**Default path — firecrawl-search (no OAuth):**

1. Form a search query from the theme + aesthetic words: *"samurai bushido ink wash painting aesthetic moodboard"*, *"weekend skate park summer aesthetic moodboard pinterest"*, etc. Always append `site:pinterest.com`.
2. Run firecrawl-search with that query, limit ~12 results, scrape the image URLs from each result page.
3. `curl -L -o "$WORKDIR/references/ref_<n>.jpg" <image_url>` for each. Drop any < 30 KB (those are 1×1 trackers or login walls).
4. Append the source URLs to `$WORKDIR/references/sources.txt`.

**Skip on `--no-pinterest`** — go straight to Phase 2 with the user's theme as the only style anchor.

**Fallback if firecrawl is unavailable:** WebSearch the same query, pull the top 5–8 image URLs from the result snippets, `curl` them.

**Why this is worth it:** Without refs, GPT Image 2 picks a generic interpretation of "samurai". With 6+ ink-wash refs in the working dir, you can write the storyboard prompt as *"in the style of the attached references — Japanese sumi-e ink, weathered paper texture, minimal color palette"* and the result is unmistakably on-brand.

## Phase 2 — Storyboard (6 scenes via GPT Image 2)

Goal: 6 PNGs that each carry one short on-screen text line, share a consistent visual language, and can be animated independently in Phase 3.

**Pick the 6 lines first.** If the user provided them, use them verbatim. Otherwise generate them — keep each 1–5 words, escalating emotional weight scene-to-scene. Karim's vault has `playbook_higgsfield_claude_ugc_wave.md` with line examples; mirror that punch.

Save lines to `$WORKDIR/storyboard/lines.txt`, one per line, in order.

**For each scene 1..6:**

```python
# Pseudocode of the loop — execute via mcp__...__generate_image
prompt = f"""{user_theme}. Scene {n}: {LINES[n]}.
Style anchors: <pull 2–3 adjectives from the Pinterest refs — e.g.
sumi-e ink wash, weathered paper, deep indigo on cream>.
Single bold on-screen text reading exactly: "{LINES[n]}" — sans-serif display
weight, all-caps, placed in the negative space, not occluding the focal subject.
Aspect ratio: {aspect}. No watermarks, no extra text, no UI chrome."""

mcp__94e5225e-fb8d-478d-95a9-201307e1a653__generate_image(
    model="gpt_image_2",
    prompt=prompt,
    aspect_ratio=aspect,
    reference_image=ref_path_for_visual_language,  # optional, but strongly recommended
)
```

**Critical:** pass the on-screen text in the prompt with quotation marks and the words *"reading exactly"*. GPT Image 2 handles short typography well; it fails on long paragraphs. If a line breaks across more than two visual lines in the output, shorten it and regenerate.

Save each result as `$WORKDIR/storyboard/scene_<n>.png` (download via `curl -L`).

**Composite preview (optional but recommended):** stitch the 6 PNGs into a 2×3 grid with ImageMagick for human QA before animating:
```bash
magick montage "$WORKDIR/storyboard/scene_"{1..6}.png -tile 3x2 -geometry +8+8 "$WORKDIR/storyboard/_board.jpg"
```
Show this to the user. If a scene is off, regenerate just that one before Phase 3.

## Phase 3 — Animate (Seedance 2.0)

Goal: 6 short clips (4–6s each) animated from the storyboard stills, then concatenated into one final motion piece.

**Per-scene animation:**

```python
# For each scene n in 1..6
mcp__94e5225e-fb8d-478d-95a9-201307e1a653__media_upload(
    file_path=f"{WORKDIR}/storyboard/scene_{n}.png"
)  # returns media_id

mcp__94e5225e-fb8d-478d-95a9-201307e1a653__generate_video(
    model="seedance_2_0",
    duration=5,
    aspect_ratio=aspect,
    medias=[media_id],
    prompt=f"""Subtle cinematic motion on the scene: slow push-in / dolly,
gentle parallax on the foreground subject, ambient particle drift in the
background, on-screen text holds steady and remains legible. Mood matches
the theme: {user_theme}."""
)
```

Poll `mcp__...__job_display` until each video job completes, then `curl -L` the result mp4 into `$WORKDIR/video/clip_<n>.mp4`.

**Concatenate:**

```bash
cd "$WORKDIR/video"
for f in clip_{1..6}.mp4; do echo "file '$f'"; done > concat.txt
ffmpeg -y -f concat -safe 0 -i concat.txt -c copy final.mp4
```

If the codecs differ across clips, drop `-c copy` and let ffmpeg re-encode (slower but bulletproof).

**Final URL:** if the user prefers a hosted URL (Higgsfield-side), instead of concatenating locally, upload `final.mp4` back via `mcp__...__media_upload` and record the returned URL in `video/final_url.txt`.

## Phase 4 — Manifest and delivery

Append to `$WORKDIR/MANIFEST.md`:

```markdown
# Motion Design — <theme>
- Slug: <slug>
- Created: <iso timestamp>
- Aspect ratio: <aspect>
- Pinterest refs: <count> images in references/
- Storyboard model: gpt_image_2
- Animation model: seedance_2_0
- On-screen lines:
  1. <line 1>
  ...
  6. <line 6>
- Final video: <local path or URL>
- Higgsfield job IDs:
  - storyboard: <id_1>..<id_6>
  - video: <id_1>..<id_6>
```

Then to the user, deliver three things only:
1. The path to `final.mp4` (or the hosted URL).
2. A one-line summary: *"6-scene motion piece on <theme> — 9:16, ~30s, ready for IG/TikTok."*
3. The 6 on-screen lines printed inline so the user can verify the message.

Don't dump JSON, don't list every job ID — they're in MANIFEST.md if needed.

## Style notes (so the model and the user stay aligned)

- **One theme per run.** Don't try to do "samurai meets cyberpunk meets nature" — the visual language fractures and the storyboard looks like stock content. If the user gives a hybrid theme, pick the dominant one and ask once if they want a second pass with the other.
- **6 scenes is the sweet spot.** Fewer feels thin; more loses tension. Don't argue with the user if they request 4 or 8 — just match the count and adjust the line-writing rhythm.
- **Text is sacred.** The whole point of this pipeline is that GPT Image 2 can render the text *into* the scene rather than overlaying it in post. If a scene comes back without legible text, regenerate it before animating; never paper over with a CSS overlay later.
- **Seedance hates rigid mid-shot composition.** If a storyboard frame has the subject locked dead-center with no negative space, Seedance has nowhere to move the camera. When generating the storyboard, lean into off-center compositions and breathing room.
- **Per Karim's bilingual rule:** if the theme is Arabic and the lines are Arabic, set the storyboard prompt to use right-to-left text and an Arabic display font (e.g., "in the style of bold Arabic display typography, RTL"). Don't mix Arabic and Latin script in the same scene.

## Reference files

- `references/themes-library.md` — pre-built theme packs (bushido, time, hustle, fitness, finance) with the exact 6 lines + style anchors used in the Higgsfield demo. Lean on this when the user is vague.
- `references/prompt-templates.md` — copy-paste prompt scaffolds for Phase 2 and Phase 3, plus the regen rules for when a scene fails.
- `references/troubleshooting.md` — what to do when GPT Image 2 mangles the text, Seedance produces a glitch, Pinterest scrape returns 0 images, etc.

## Out of scope

- Audio / VO / background music. The output is silent video. If the user wants sound, hand off the final.mp4 to a downstream audio tool — this skill stops at picture.
- More than 6 scenes natively. Loop manually if the user wants 12.
- Editing the final cut (transitions, color grading). Use a video editor downstream.
