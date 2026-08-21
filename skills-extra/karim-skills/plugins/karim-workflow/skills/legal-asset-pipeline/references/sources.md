# Sources & licenses — full reference

Read this when you need the exact license terms, an API detail, or to choose between open-source and API image generation. The SKILL.md source picker is the quick version.

## Table of contents
1. Free photo sources
2. Free video sources
3. Icons
4. Fonts
5. Open-source image generation (local GPU)
6. API image generation (no GPU)
7. Why a Plus/Pro subscription is not API credit

---

## 1. Free photo sources

| Source | License | Attribution | Page |
|--------|---------|-------------|------|
| Unsplash | Unsplash License | Not required (appreciated) | https://unsplash.com/license |
| Pexels | Pexels License | Not required | https://www.pexels.com/license/ |
| Pixabay | Pixabay Content License | Not required | https://pixabay.com/service/license-summary/ |
| Wikimedia Commons | **Per file** — CC-BY, CC-BY-SA, CC0, or public domain | **Depends — check each file** | https://commons.wikimedia.org |
| Openverse | **Per item** — mostly CC + public domain | **Depends — check each item** | https://openverse.org |

Practical notes:
- Unsplash / Pexels / Pixabay: safe default for commercial work, no attribution obligation. Still log the source URL — if a photo is ever disputed you want proof of where it came from.
- Wikimedia / Openverse: never assume. A CC-BY-SA image can force your whole page's license open in strict readings; read the specific file's terms and attribute exactly as required.
- **Never** pull from Google Images results, Pinterest, a competitor's site, or "I found it somewhere" — none of those are a license.

## 2. Free video sources

| Source | License | Page |
|--------|---------|------|
| Pexels Videos | Pexels License (same as photos) | https://www.pexels.com/videos/ |
| Mixkit | Mixkit License — free commercial, short restriction list | https://mixkit.co/license/ |
| Coverr | Coverr License — free commercial | https://coverr.co/license |
| Pixabay Videos | Pixabay Content License | https://pixabay.com/videos/ |

For websites you usually do **not** need AI video. A legal stock clip + CSS color-grading/overlay reads more premium than a warped AI clip. Reach for generation only when the shot literally cannot be filmed or found.

## 3. Icons

| Set | License | Install |
|-----|---------|---------|
| Lucide | ISC | `npm i lucide-react` (or framework variant) |
| Heroicons | MIT | `npm i @heroicons/react` |
| Tabler Icons | MIT | `npm i @tabler/icons-react` |
| Phosphor | MIT | `npm i @phosphor-icons/react` |

Install the package — do not copy individual SVGs out of a paid set or a competitor's bundle.

## 4. Fonts

- **Google Fonts** via `@fontsource/<family>` npm packages (self-hosted, no external request) — not by cloning the multi-GB `google/fonts` repo. See the `font-resources` skill.
- **Fontsource** for the same OFL/Apache families packaged for npm.
- Respect the project's font rules. Karim's standing ban: do **not** default to Cormorant, Outfit, JetBrains Mono, or Noto Kufi.

## 5. Open-source image generation (local GPU)

Best when a GPU is available — zero per-image cost, no rate limits, full control.

- **ComfyUI** — node-based runner for local diffusion models. https://github.com/comfyanonymous/ComfyUI
- **FLUX.1-schnell** — Apache-2.0, fast, genuinely free for commercial use. https://huggingface.co/black-forest-labs/FLUX.1-schnell
  - (FLUX.1-dev exists too but is a non-commercial license — schnell is the commercial-safe one.)
- **SDXL / Stable Diffusion 3.x** — strong quality, but check the **Stability community license**: it has revenue thresholds above which a paid license is required. Verify current terms at https://stability.ai before shipping commercially.

Log generated images in the ledger too: source = "generated locally, <model> <version>", license = the model's license, plus the prompt in `design/image-prompts.md`.

## 6. API image generation (no GPU)

Call a hosted model from a script with a key in `.env`. Providers worth knowing:

- **OpenAI Images** — the current GPT image model via the Images API.
- **Google Gemini image model** — via Google AI Studio / Vertex API.
- **fal.ai**, **Replicate**, **WaveSpeed**, **DeepInfra** — aggregators that expose many image/video models (including **FLUX.1-schnell / SDXL / SD3.x**) behind one API, usually pay-as-you-go. This is the API path for **open-source** models.
- **OpenRouter** — unified key, but for **proprietary image models only**: Google Gemini "flash/pro image" (Nano Banana family) + OpenAI GPT-image. **Not a source for open-source diffusion.** Verified live 2026-07-16 against `https://openrouter.ai/api/v1/models`: 9 image-output models, all closed, zero FLUX / Stable Diffusion / SDXL. Use it for cheap closed generations; use fal / Replicate / DeepInfra (or local ComfyUI) for FLUX/SD.

> Model names, version numbers, and per-image prices change frequently. **Look up the provider's current model list and pricing before spending** — do not hard-code a version from any document, including this one. Existing skills `imagegen`, `replicate`, `fal-generate`, `higgsfield-generate`, and `venice-image-generate` wrap several of these already.

A small metered API budget (often ~$10–25 for a whole project) is the practical no-GPU path. Log every generated asset in the ledger.

## 7. Why a Plus/Pro subscription is not API credit

`ChatGPT Plus` and `Gemini Pro` are **chat-UI subscriptions**. They authenticate a person into a web app; they do not issue programmatic API credits and cannot be attached to a script or MCP. Automated generation needs a real API key (a separate, metered product). The correct wiring is:

```
Claude Code → script / MCP → OpenAI API | Gemini API | fal | Replicate | WaveSpeed
```

Keep the subscriptions for manual generation and eyeballing results; use the metered API for anything the pipeline runs on its own.
