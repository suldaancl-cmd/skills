---
name: aistudiotoday-carousel
description: >-
  Create high-converting social-media carousels (Instagram / LinkedIn / TikTok swipe posts)
  in the AI Studio Today (aistudiotoday.com) brand design — dark-violet canvas, bold-condensed
  display type, purple glow, dotted-grid motifs. Uses a proven HYBRID method: one AI-generated
  striking COVER image (via Higgsfield → GPT Image / Nano Banana Pro) plus on-brand HTML BODY
  slides with a live in-browser tweak loop and one-command PNG export at 1080×1350. Trigger this
  whenever the user wants a carousel, slide post, swipe post, multi-slide post, "turn this into a
  carousel", a cover/title slide, or repeatable branded slide content for AI Studio Today — even if
  they never say the word "skill". Prefer this over generic HTML slide-deck generation, which
  produces same-y, low-engagement AI slop. NOT for building a website carousel/slider UI component (a
  React or HTML slider with arrows/autoplay), a PowerPoint / Google Slides deck, plain post captions
  with no slides, or a single standalone image — those are different tasks.
---

# AI Studio Today — Carousel Builder

## Why this exists (read first — it shapes every decision)

Social feeds are drowning in AI-made carousels that all look identical: pure-HTML slide decks
with the same gradient-card look, zero stopping power. They get no engagement because the **cover
never earns the swipe**.

The fix is a **hybrid** approach, and the split is deliberate:

| Slide | Built with | Why |
|---|---|---|
| **Cover** (slide 1) | AI image model (GPT Image / Nano Banana Pro via Higgsfield) | It's the only thing in the feed. It must be *visually striking* enough to stop the scroll. Worth the cost + iteration. |
| **Body** (slides 2–N) | On-brand HTML (this skill's template) | Once they've swiped, they want *value*, not art. HTML is fast, free, editable, and repeatable at scale. |

Spending AI-image budget on every slide is slow and expensive; making every slide pure HTML is
cheap but never stops the scroll. The hybrid gets both: **stopping power on the cover, scalable
value on the body.** Internalize this — it's the whole point.

Everything this skill produces must look like it came off **aistudiotoday.com**. Read
[references/design-system.md](references/design-system.md) before writing any slide markup or
image prompt — it has the exact colors, fonts, motifs, and brand voice. Don't improvise the brand.

## The build (3 steps + export)

Work the steps in order. Don't skip Step 0 — building from a blank slate is where carousels die.

### Step 0 — Inspiration (don't start from zero)

Before generating anything, anchor on a reference so the layout has bones.

- Ask the user for the **topic** and (ideally) a **reference screenshot** of a carousel cover +
  body slide they like — from Instagram/TikTok/LinkedIn, *especially outside the AI niche* so it
  doesn't look like everyone else's.
- If they have none, propose 2–3 concrete layout directions from the template variants below and
  let them pick. Don't copy a reference pixel-for-pixel — take the *structure* (where the eye
  lands, text rhythm, image placement) and re-skin it in the AI Studio Today system.
- Over time the user builds a library of winning templates. When they say "do carousel v7 on
  topic X", skip straight to Step 2 and just swap the copy.

### Step 1 — Cover image (the hook, via AI)

The cover is generated with an outside image model so it has real visual punch. Read
[references/cover-image-prompts.md](references/cover-image-prompts.md) for ready-to-fill prompt
recipes already tuned to the brand (dark violet, purple glow, condensed display headline).

Tooling, in order of preference:
1. **Higgsfield MCP** (already connected this session — tools `mcp__94e5225e-...__generate_image`).
   Use `generate_image` with model `gpt-image` or `nano-banana`. This is the video's method and
   needs no install.
2. **Higgsfield CLI** — if the user prefers terminal: install from higgsfield.ai → "MCP and CLI"
   tab, then `higgsfield login`. Invoke via Bash.
3. **Any other image MCP/tool** the user has — the prompt recipes are model-agnostic.

Rules that make covers actually convert:
- **Aspect ratio 4:5** (target 1080×1350) to match the body slides and maximize feed real estate.
- **Generate 4 variants** per prompt (the model can do more, but 4 is the speed/quality sweet
  spot), then show them to the user and let them pick.
- **Expect 2 passes, not one.** Pass 1: get the image/composition right (often without text, since
  image models mangle long text). Pass 2: feed the chosen image back and add the headline cleanly,
  OR drop the headline in via the HTML cover-overlay variant in the template (more reliable for
  crisp, correct text). Default to the HTML overlay when the headline is long or must be exact.
- Keep the brand: violet accent, near-black background, condensed heavy headline, optional
  gradient highlight on 1–2 key words.

### Step 2 — Body slides (the value, via HTML)

Use [assets/carousel-template.html](assets/carousel-template.html) — a single self-contained file
(brand CSS + slides + a live tweak panel, no build step). Copy it into the user's carousel folder
and edit the slide content.

1. **Copy the template** into a working folder, e.g.
   `<carousels-dir>/<slug>/carousel.html` (see "Folder & library" below).
2. **Fill the slides.** Each `<section class="slide ...">` is exactly 1080×1350. Variants provided:
   - `slide--cover` — title slide. Use it either as an HTML cover (headline over the AI image set
     as `--cover-img`) or delete it if the cover is a finished AI PNG.
   - `slide--value` — the workhorse: kicker + big number + headline + 1–2 lines + optional
     image/screenshot slot. **Economy of action** — treat it like a good keynote slide, not a
     paragraph. One idea per slide.
   - `slide--data` — glass card with mono metrics / a fake terminal, matching the site's dashboard
     motif. Great for proof, stats, before/after.
   - `slide--cta` — outro: the ask (book a call, follow, link in bio) on the brand gradient.
3. **Write the copy in brand voice** — short, declarative, outcome-first. See design-system.md →
   Voice. Pull real specifics (numbers, names) rather than vague claims.
4. **Add screenshots where they add proof.** The user can paste a screenshot (GitHub repo,
   dashboard, product) and you drop it into a slide's image slot — far more credible than a
   generated graphic. You may also fetch a relevant real image from the web.

### The tweak loop (the differentiator)

Open the saved `carousel.html` in a browser. A **tweak panel** is docked on the right. It lets the
user dial the design live without round-tripping through code:

- Sliders: display size, body size, dot-field opacity, card tilt, slide padding, accent hue.
- Per-slide selection so they can tune one slide at a time.
- **"Export tweaks"** → copies a small JSON of the current values.

The loop, exactly like the video: user nudges sliders → clicks **Export tweaks** → pastes the JSON
back to you → you write those values into the `:root` (or the slide's `style`) block in
`carousel.html` so they persist. Re-open to confirm. This gives the user real hands-on control
while you keep the source as the single point of truth.

To verify your own work, open the file with `mcp__playwright__browser_navigate` to
`file:///.../carousel.html?export=1` (the `?export=1` hides the tweak panel) and screenshot it.

### Step 3 — Export to PNGs (ready to post)

Run the bundled exporter to turn each slide into a crisp 1080×1350 PNG:

```bash
node scripts/export_slides.js "<path>/carousel.html" --out "<path>/slides" --scale 2
```

It loads the file with the panel hidden (`?export=1`), waits for the webfonts, finds every
`.slide`, and renders each at 2× for retina sharpness, named `slide-01.png`, `slide-02.png`, … in
swipe order. (It uses Node + Playwright, already installed on this machine. Fresh machine:
`npm i -D playwright && npx playwright install chromium`.) If the cover is a finished AI PNG, place it as `slide-01.png` and start the body
export at 02, or keep it as the HTML cover slide and let the script handle all of them.

## Folder & library (so this compounds)

Keep one carousels root and one subfolder per carousel — this is how the user builds a reusable
template library, which is where the real leverage is:

```
<carousels-dir>/
  <YYYY-MM-DD>-<slug>/
    carousel.html          # body (+ optional HTML cover)
    cover/                 # AI cover variants + the chosen one
    slides/               # exported PNGs ready to post
    notes.md              # topic, hook, reference used, what worked
```

After ~10–15 carousels the user has proven templates. Then "carousel v12 on <new topic>" is a copy
+ copy-swap, not a from-scratch build. Encourage saving winners.

## Definition of done

- A cover that would make *you* stop scrolling (on-brand: dark violet, condensed headline, glow).
- Body slides that are unmistakably AI Studio Today, one idea each, brand voice.
- Exported 1080×1350 PNGs in swipe order, in the carousel's `slides/` folder.
- The tweak panel works in-browser and exported tweaks round-trip into the source.

If you produced HTML but never rendered/exported it, you're not done — open it in the browser and
screenshot before claiming success.

## Reference files

- [references/design-system.md](references/design-system.md) — exact brand tokens, fonts, motifs,
  voice. Read before any markup or prompt.
- [references/cover-image-prompts.md](references/cover-image-prompts.md) — fill-in cover prompt
  recipes for Higgsfield / GPT Image / Nano Banana.
- [assets/carousel-template.html](assets/carousel-template.html) — the self-contained body-slide
  deck + tweak panel.
- [scripts/export_slides.js](scripts/export_slides.js) — HTML → 1080×1350 PNG exporter (Node + Playwright).
