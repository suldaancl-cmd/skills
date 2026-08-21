---
name: legal-asset-pipeline
description: Set up and follow a legal, license-tracked asset pipeline when building any website, app, landing page, or deck — sourcing images, video, icons, and fonts from free legal sources (Pexels, Unsplash, Pixabay, Wikimedia, Openverse) or open-source generators instead of unknown/copyrighted files or paid Higgsfield credits. Use this whenever a project needs visuals or media, whenever the user mentions stock photos/video, royalty-free, "assets", "where do I get images", a Higgsfield/paid-credits alternative, or asks how to wire image/video generation into Claude Code. Enforces a mandatory license ledger (source URL + license + author + path for every asset) and clarifies that Claude Code connects to generation via API keys in `.env`, never via a ChatGPT Plus / Gemini Pro subscription.
version: 1.0.0
author: Karim
tags: [assets, images, video, licensing, stock, pipeline, claude-code]
---

# legal-asset-pipeline

A repeatable pipeline for putting **only legally-usable media** into a project, with a paper trail. The point is not bureaucracy — it's that an unknown image in a shipped site is a real liability, and a two-line ledger entry removes it. Every visual either comes from a source whose license you recorded, or it doesn't ship.

## The one non-negotiable rule

**Before any asset enters the repo, record it in `assets/licenses/assets.md`:**

1. Source URL (the page, not just the file)
2. License (name + link)
3. Author / attribution (if the license requires it)
4. Local path in the repo
5. What it's used for (optional but helps future-you)

No entry → the asset doesn't ship. Never use a file whose license you can't name. Never copy images, copy, icons, or SVGs from a competitor's site — "found it on their homepage" is not a license.

## Scaffold (create once per project)

```
/assets
  /images      /videos      /icons      /fonts
  /licenses/assets.md        <- the ledger, from assets/assets-ledger.template.md
/design
  DESIGN.md                  <- brand direction, from assets/DESIGN.template.md
  moodboard.md  image-prompts.md  copy-style.md
/scripts
  fetch-pexels.mjs  fetch-unsplash.mjs  fetch-pixabay.mjs  fetch-flux.mjs   <- copy from this skill's scripts/
```

Copy the fetch scripts and templates from this skill (`scripts/`, `assets/`) into the project so it's self-contained.

## Source picker (start here — all free for commercial use)

| Need | Reach for | License note |
|------|-----------|--------------|
| Photos | **Pexels**, **Unsplash**, **Pixabay** | No attribution required; still record source |
| Photos needing attribution / historical / logos | **Wikimedia Commons**, **Openverse** | Per-file — CC-BY / CC-BY-SA / public domain; **must check each file** and attribute |
| Stock video / backgrounds | **Pexels Videos**, **Mixkit**, **Coverr**, **Pixabay Videos** | Free commercial; Mixkit has a short restriction list — read it |
| Icons | **Lucide** (ISC), **Heroicons** / **Tabler** / **Phosphor** (MIT) | `npm install`, don't scrape icon SVGs |
| Fonts | **Google Fonts** (via `@fontsource` npm), **Fontsource** | OFL / Apache. Respect Karim's default-fonts ban — see below |

For the full table, per-source API notes, and the open-source vs API generation decision, read **`references/sources.md`**.

## Fetching with the scripts

The `scripts/*.mjs` files hit each provider's API, download into `assets/images/`, and **append a correct ledger entry automatically** — so following the rule is the path of least resistance. Three fetch stock photos (Pexels / Unsplash / Pixabay); `fetch-flux.mjs` *generates* images via fal.ai FLUX.1-schnell (Apache-2.0, metered API) and also logs the prompt to `design/image-prompts.md`. They need Node 18+ (built-in `fetch`) and a free API key in `.env`:

```
PEXELS_API_KEY=...          # pexels.com/api
UNSPLASH_ACCESS_KEY=...     # unsplash.com/developers
PIXABAY_API_KEY=...         # pixabay.com/api/docs
FAL_KEY=...                 # fal.ai/dashboard/keys (metered — verify pricing first)
```

```bash
node scripts/fetch-pexels.mjs "luxury gulf villa interior" 5
node scripts/fetch-unsplash.mjs "minimal saas dashboard" 3
node scripts/fetch-pixabay.mjs "arabic calligraphy texture" 4
node scripts/fetch-flux.mjs "cinematic gulf villa at dusk, warm rim light" 2
```

Each run writes files to `assets/images/` and rows to `assets/licenses/assets.md`. Review the images, delete the ones you don't use, and delete their ledger rows with them.

## When you need to *generate* an image (no legal stock fits)

Two honest paths — pick by whether a GPU is available. Details and current-model guidance in `references/sources.md`.

- **Have a GPU** → run **ComfyUI** locally with **FLUX.1-schnell** (Apache-2.0) or an SDXL / SD 3.x checkpoint. Free, no per-image cost. Check the SD model's community-license revenue terms before commercial use.
- **No GPU** → call a hosted image API (OpenAI Images, Google's Gemini image model, or a provider like **fal.ai** / **Replicate** / **WaveSpeed**) from a script, key in `.env`.

**Model names and per-image prices move fast — verify the provider's current model list and pricing before you spend, don't trust a hard-coded version number in any doc (including this one).**

## The subscription-vs-API fact people get wrong

Claude Code drives generation through **API keys in a script or MCP**, e.g.:

```
Claude Code  →  script / MCP  →  OpenAI API | Gemini API | fal | Replicate | WaveSpeed
```

A **ChatGPT Plus** or **Gemini Pro** subscription is *not* API credit and cannot be wired in this way — those log you into a chat UI, not a programmatic endpoint. Keep the subscriptions for manual generation and review; buy a small metered API (often $10–25 covers a project) for anything automated. Don't tell the user their subscription can be "connected" as credits — it can't.

## The ready prompt (paste into a fresh project)

When kicking off a build that needs its own pipeline, hand the agent this:

> Build this project with a legal asset pipeline.
> 1. Create `design/DESIGN.md` with brand direction, colors, typography, image style, UI style.
> 2. Source visuals ONLY from Pexels, Unsplash, Pixabay, Wikimedia Commons, or Openverse — or generate with open-source / API models. No competitor assets, no unknown-license files.
> 3. For every asset, record source URL + license + author + path in `assets/licenses/assets.md`.
> 4. Use `shadcn/ui` or Tailwind components but customize heavily so it doesn't look generic.
> 5. Save image prompts for missing visuals in `design/image-prompts.md`.
> 6. Fonts: Google Fonts / Fontsource only (respect the project's font rules).
> 7. Run the app, screenshot it, inspect spacing/typography/color, improve once, then finalize.
>
> Project: [details]

## Notes that pair with this skill

- **Fonts:** don't default to Cormorant / Outfit / JetBrains Mono / Noto Kufi — see `font-resources` and the project's font rules before choosing.
- **Design system first:** for premium web, lock the palette + type via `ui-ux-pro-max` before fetching a single asset, so what you fetch matches the system.
- **Generation skills already installed:** `imagegen`, `higgsfield-generate`, `replicate`, `fal-generate`, `venice-image-generate` — use them when you want a managed tool instead of a raw script.
