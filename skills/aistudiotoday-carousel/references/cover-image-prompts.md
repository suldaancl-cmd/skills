# Cover-image prompt recipes (AI Studio Today)

The cover earns the swipe, so it's the one slide worth an AI image model. These recipes are
pre-tuned to the brand (dark violet, purple glow, condensed display). Fill the `[BRACKETS]`,
generate **4 variants at 4:5**, show the user, iterate.

## How to run it

**Preferred — Higgsfield MCP (connected this session):**
Use the image tool `mcp__94e5225e-fb8d-478d-95a9-201307e1a653__generate_image` with:
- `prompt`: one filled recipe below
- model: `gpt-image` (great text/instruction following) or `nano-banana` (Nano Banana Pro —
  strong photoreal + editing). Try both; they miss differently.
- aspect ratio / size: 4:5 (≈1024×1280 or 2K equivalent), high quality.
- count: 4.

**Alt — Higgsfield CLI:** install from higgsfield.ai → "MCP and CLI" tab → `higgsfield login`,
then call via Bash. **Alt — any image MCP** the user has (fal, Replicate, Imagen, Venice): the
prompts are model-agnostic.

## Two-pass rule (important)

Image models mangle long/exact text. So:
- **Pass 1 — composition, usually no text.** Get the scene, subject, palette, mood right.
- **Pass 2 — text.** Either (a) feed the chosen image back and ask the model to add a short
  headline in the brand style, or (b) skip model text entirely and use the **HTML cover variant**
  in `assets/carousel-template.html` (set the image as `--cover-img` and lay the Anton headline
  over it). Default to (b) when the headline must be exact or is longer than ~5 words — it's
  pixel-crisp every time.

## Recipe A — Abstract brand hero (safest default)

> A premium, high-end abstract hero image for an AI marketing agency. Near-black background with a
> deep violet tint (#0B0712). Glowing violet and purple light (#8B5CF6, #A855F7) forming
> [A FOCAL SHAPE: e.g. a sweeping 3D ribbon / a glowing node-and-line network / a liquid chrome
> orb]. Soft particle dots scattered in the dark like the night sky. Subtle dotted grid receding
> into depth. Cinematic studio lighting, volumetric glow, deep shadows, 8k, photoreal render,
> shallow depth of field. Minimal, lots of negative space in the [upper / lower] area for a
> headline. No text. Vertical 4:5 composition.

Use when: the topic is conceptual (strategy, growth, "the funnel"), or you want a clean text
overlay zone.

## Recipe B — Statue / subject hero (the video's example)

> A dramatic [classical marble statue bust / a confident founder figure / a robot-human hybrid]
> centered on a near-black violet background (#0B0712). Glowing violet rim light and purple
> bloom (#8B5CF6 → #A855F7) wrapping the subject; [a thin band of rainbow-iridescent light across
> the eyes]. Floating minimalist 3D tech icons around it ([SWAP: GitHub / Anthropic / terminal /
> chart icons]) in matte dark glass with violet edge-glow. Scattered particle dots. Cinematic,
> high-contrast, premium product-launch aesthetic, 8k photoreal. Empty space at the top for a
> headline. No text. Vertical 4:5.

Use when: you want a striking "character" cover with personality. Swap the subject + the floating
icons to fit the topic. To iterate from a reference screenshot, attach it and say: *"Match this
composition and lighting, but change [X→Y] and keep everything else."*

## Recipe C — Product / screenshot hero

> A floating [dashboard / phone / app window] mockup with a dark glassmorphic UI, violet accent
> data and charts, set on a near-black violet background (#0B0712) with purple glow and scattered
> particle dots. Dramatic perspective tilt, soft reflections, volumetric violet light, premium
> 8k render. Negative space [left / top] for a headline. No text. Vertical 4:5.

Use when: the carousel is about a real product/result and you want the cover to feel like proof.

## Pass-2 "add the headline" prompt (if doing text in-model)

> Keep this image exactly the same. Add a short, bold, condensed UPPERCASE headline reading
> "[HEADLINE — ≤5 words]" in the [top / bottom] area, in an off-white heavy condensed grotesque
> (like Helvetica Neue Condensed Black / Anton). Make [1 key word] use a violet→purple gradient
> (#8B5CF6 → #A855F7). Clean kerning, crisp, no other text. Keep 4:5.

## Quality checklist for the chosen cover

- Reads instantly at thumbnail size (the scroll happens fast).
- On-brand: near-black violet canvas, violet/purple as the only accent, glow, particle texture.
- A clear empty zone where the headline sits (or headline already crisp).
- Doesn't look like a generic AI gradient card — it has a *subject* or real depth.
- If you wouldn't stop scrolling for it, regenerate or switch recipe/model.
