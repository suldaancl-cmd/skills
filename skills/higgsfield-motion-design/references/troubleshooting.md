# Troubleshooting

Runbook for the failure modes that show up most often during the Pinterest → Storyboard → Seedance pipeline. Use this before re-running anything from scratch — most failures fall into one of these buckets and have a 30-second fix.

---

## Pinterest scrape returns 0 images

**Likely cause:** firecrawl-search hit a Pinterest interstitial / login wall, or the query is too narrow.

**Fixes (in order):**
1. Broaden the query — drop the most specific adjective. *"samurai sumi-e ink wash painting moodboard"* → *"samurai aesthetic"*.
2. Switch source — search `site:pinterest.com OR site:behance.net OR site:dribbble.com`.
3. Use WebSearch (not firecrawl) and pull the first 5–8 image URLs from the result snippets directly.
4. As a last resort, skip Phase 1 entirely and pass `--no-pinterest` — the theme + style anchors in the Phase 2 prompt are enough on their own. The result will be a notch less branded but still usable.

Don't waste cycles trying to force the same query — Pinterest A/B tests bot-detection aggressively.

---

## firecrawl is rate-limited or unavailable

Switch to plain `curl` with realistic browser headers as a fallback:

```bash
curl -L -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" \
     -H "Accept: text/html,application/xhtml+xml" \
     "https://www.pinterest.com/search/pins/?q=<urlencoded_query>" \
     -o /tmp/pin_search.html
```

Then extract image URLs from `og:image` and `<img>` tags. Not pretty, but it gets the job done when the MCP path is down.

---

## Higgsfield MCP returns 401 / balance is $0

**401 or session-expired:** the MCP token has rotated. Ask the user to re-auth in the Higgsfield app and refresh the MCP connection. Don't try to work around it — there's no other path.

**Balance is $0:** stop immediately. Tell the user the cost is gated. Quote the estimated cost of completing the run (Phase 2: 6 × GPT Image 2 jobs; Phase 3: 6 × Seedance 2.0 jobs) so they can decide whether to top up. Get explicit confirmation before resuming.

---

## GPT Image 2 produces non-text image even though "on-screen text" was specified

GPT Image 2 sometimes treats the on-screen text as a stylistic hint, not a hard render constraint. Forcing functions:

1. Put the literal text **inside double quotes** in the prompt, not single quotes or backticks.
2. Add the line *"the text MUST appear in the rendered image, baked into the composition"*.
3. Reduce the line to 1–3 words. GPT Image 2's typography reliability degrades sharply past ~4 words.
4. Try a regen with `reference_image=None` (sometimes a reference image dominates and suppresses the text instruction).

If 3 regens still produce no text, switch the affected scene to a different image model (e.g. `nano_banana_pro` or `seedream_4_5`) for that single frame. The style will drift slightly but you'll get the text.

---

## Storyboard frames feel visually inconsistent across scenes

**Cause:** style-anchor drift. The model anchored on different aspects of the anchor list for different scenes.

**Fix:** pick the strongest frame from your batch and feed it back as a `reference_image` to all other regens. Add *"strictly match the style, palette, and rendering medium of the attached reference"* to the prompt. This forces visual lock-in.

---

## Seedance clip is too short / too long

Seedance 2.0 reliable range is 4–10 seconds. If you asked for 6 seconds and got 5, that's normal — don't regenerate over a 0.5–1s delta. Pick it up in the ffmpeg concat by trimming/padding:

```bash
# Trim a clip to exactly 5s
ffmpeg -y -i input.mp4 -t 5 -c copy trimmed.mp4

# Pad a 4s clip out to 5s by repeating the last frame
ffmpeg -y -i input.mp4 -vf "tpad=stop_mode=clone:stop_duration=1" padded.mp4
```

---

## Seedance produces a glitchy / morphing video

Most common cause: the storyboard frame's composition is too rigid (subject locked dead-center, no negative space). Seedance has nowhere to apply motion and starts hallucinating.

**Fix:** regenerate the underlying storyboard frame with explicit off-center composition (see prompt-templates.md → Master template, `composition_rule` slot). Then re-animate.

Second cause: the prompt asked for two compound camera moves at once (e.g. "dolly in AND pan left"). Pick one.

---

## ffmpeg concat: clips look the same but the final output is corrupt

Almost always a codec or pixel-format mismatch between clips. Higgsfield's Seedance output codec can vary slightly between runs.

**Fix:** drop `-c copy` and let ffmpeg re-encode:

```bash
ffmpeg -y -f concat -safe 0 -i concat.txt \
       -c:v libx264 -crf 18 -pix_fmt yuv420p -preset slow \
       -c:a aac -b:a 192k \
       final.mp4
```

Re-encoding takes ~30s for a 30s output on a modern laptop. Always cleaner than chasing codec ghosts.

---

## The final video doesn't tell a story

Not really a technical failure — the lines/visual arc didn't land. Step back and:

1. Read all 6 lines aloud in order. Is there an arc — setup, tension, resolution? Or are they 6 disconnected one-liners?
2. Look at the 6 storyboard frames as a 2×3 grid. Does the eye move naturally across them?
3. Ask: does scene 6 *answer* scene 1?

If any answer is no, rewrite the 6 lines first (cheap), then regenerate the affected frames. Don't try to fix narrative failures with prettier visuals.

---

## You used $X on a run that didn't deliver

Log the failure to `~/.claude/outputs/motion-design/_failures.log` with date, theme, what broke, and what it cost. Three of those in a week and we know there's a systemic pattern (model regression, MCP drift, prompt template stale) — without the log, you'll repeat it.
