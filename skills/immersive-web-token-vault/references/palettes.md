# Palettes — extracted from award-winning sites

Source: `skillui` static analysis (no AI, no guessing) on the live sites, 2026-07-13. Every hex below was pulled from the site's shipped CSS. Re-verify before quoting as current — live sites change.

## How to read this

Each site lists its **functional** roles (background, surface, text, accent, semantic) plus any **extended** swatches skillui found but could not role-classify. The role labels (`danger`, `info`, etc.) are skillui's guesses from the color's position/usage — trust the **hex**, treat the role as a hint.

The recurring architecture across all 15 sites: **one background + one primary text + one saturated accent**, everything else near-neutral. This restraint is the pattern, not an accident.

---

## Dark-theme sites

### Clear Street — `clearstreet.io` (17 colors, 1 font)
- background `#01001f` · surface `#000000` · text `#ffffff` · text-muted `#656578` · border `#222222`
- accent `#9bbcfd` (soft periwinkle) · info `#2e21de` · success `#34a36c` · danger `#e85030`
- extended: `#c7dcfe` `#161631` `#020250` `#f2f4fd` `#573ebb` `#3488a3` `#0d111d` `#1f2c41`
- Note: near-black navy base, a single soft-blue accent, muted supporting blues. 4px grid.

### Hatom — `hatom.com` (15 colors, 1 font, expressive motion)
- background `#000000` · surface `#007e2b` (deep green) · text `#ffffff`
- accent `#ffff00` (pure yellow) · lime `#c1ff12` · success `#90ee90` · warning `#ffe60a`
- extended: `#00ff57` `#a304ff` `#ae5dff` `#23f7dd` `#00aa96` `#9d8e06` `#9f1010`
- Note: black + electric green/yellow/violet — a high-energy "crypto-native" neon set on black.

### Igloo Inc — `igloo.inc` (2 colors, 1 font) — Awwwards Site of the Year 2024
- background `#000000` · text-muted `#a0a5b1`
- Note: near-zero palette. The entire experience is carried by 3D/WebGL, not color. The lesson: an SOTY winner shipped a **two-color** DOM. Restraint at the extreme.

### X-Shack — `xshack.app` (15 colors, 2 fonts)
- background `#1c2928` (dark teal) · surface `#000000` · text `#f3f0ed` · text-muted `#485958` · border `#27211e`
- accent `#3d78f6` (blue) · danger `#df6f45` (terracotta) · warm-white `#ffeae2`
- extended: `#7c726d` `#73807f` `#7a606a` `#a3a3a3`
- Note: muted teal-green base + a single clean blue accent + earthy terracotta. "Elevated cannabis."

### Scout Motors — `scoutmotors.com` (20 colors, 3 fonts, expressive motion)
- background `#010101` · surface `#1c1c1a` · text `#e5e7eb` · text-muted `#585856` · border `#31312c`
- accent `#007aff` (system blue) · danger/brand `#ff5432` (orange) · deep-navy `#11232f` / `#0c0e1c` / `#162c3b`
- extended greys: `#f0f0f0` `#849eae` `#808080` `#626262` `#dbdbdb` `#747473`
- Note: automotive dark, a rugged orange brand accent (`#ff5432` / `#c73201`) over near-black + navies.

### Zajno — `zajno.com` (2 colors, 1 font)
- background `#1a1a1a` · text `#ebebeb`
- Note: again near-monochrome DOM; the studio's craft lives in motion/WebGL, not swatches.

---

## Light-theme sites

### Exo Ape — `exoape.com` (5 colors, 2 fonts)
- background `#ffffff` · surface `#e4e0db` (warm stone) · text `#0d0e13` · warm-beige `#e0ccbb` · near-black `#070707`
- Note: warm off-white system, zero saturated accent — the "quiet luxury" studio look. 10px grid.

### Unseen Studio — `unseen.co` (8 colors, 2 fonts) — Awwwards SOTM May 2024
- background `#ffffff` · surface `#faf6f4` (warm white) · text `#212121` · text-muted `#424242` · warm `#efded9`
- extended: `#000000` `#d6d6d6` `#e7e7e7`
- Note: editorial warm-neutral, no color accent — the type does the work (Saol Display).

### Lusion — `lusion.co` (7 colors, 2 fonts) — award-winning 3D studio
- background `#ffffff` · surface `#f0f1fa` · text `#000000` · border `#2b2e3a`
- accent `#0016ec` (electric ultramarine) · info `#1a2ffb`
- Note: white + black + one **electric blue**. The cleanest "neutral + one loud accent" example in the set.

### Serious Business — `serious.business` (8 colors, 2 fonts)
- background `#ffffff` · surface `#fbc1d4` (pink) · text `#1e1e1e`
- accent `#ff7ec4` (hot pink) · success `#48b469` · warning `#fed35b` · info `#c3abff` (lavender)
- Note: playful candy palette — pink lead, pastel supporting set. B2B without being grey.

### Studiogusto — `studiogusto.com` (9 colors, 1 font)
- background `#ffffff` · surface `#ebd9dc` · text `#0f0f0f` · text-muted `#bfaaa1`
- accent `#ff4e4d` (coral-red) · info `#0000ee` (link blue) · warm `#f2b67b` / `#d8d7b2`
- Note: warm-neutral + a single hot coral-red accent + a classic `#0000ee` link blue.

### Umault — `umault.com` (11 colors, 2 fonts)
- background `#ffffff` · surface `#f2f2f2` · text `#000000` · text-muted `#747474`
- accent-blue `#3055ff` · success `#24ce49` · warning `#ffb701`
- Note: clean agency white + one strong blue + bright semantic set.

### funkhaus — `funkhaus.io` (9 colors, 3 fonts, expressive motion)
- background `#ffffff` · surface `#96ffd9` (mint) · text `#0a0a12` · text-muted `#9ca3af` · border `#181820`
- accent `#f3996e` (coral) · secondary `#eb6273` (rose) · violet `#8981ee`
- Note: the most *chromatic* of the set — mint + coral + rose + violet. Expressive by design.

### Design Embraced — `designembraced.com` (5 colors, 2 fonts)
- background `#eeeeee` · surface `#e1ddd9` · text `#151417` · grey `#d3d3d3` · black `#000000`
- Note: pure greyscale editorial. No accent at all. Type + layout carry it.

### Dorst & Lesser — `dorstlesser.com` (0 colors, 0 fonts)
- Nothing extractable — the site renders through JS/canvas with no shipped CSS tokens skillui could read. Honest zero; treat as canvas-driven.

---

## The award palette recipe (synthesized from the above)

1. **Pick a base:** one near-black (`#000`–`#1c2928`) OR one off-white (`#fff`–`#eee`, often *warmed*: `#faf6f4`, `#e4e0db`). Warm neutrals read more premium than pure `#f5f5f5`.
2. **One text color**, high-contrast against the base. That's usually it for 60% of the page.
3. **One saturated accent, used sparingly** — electric blue (`#0016ec`), coral-red (`#ff4e4d`), hot pink (`#ff7ec4`), or acid green (`#c1ff12`). One. Not three.
4. **Semantic colors are functional, not decorative** — keep success/warning/danger out of the hero.
5. **Extended swatches are for depth** (surfaces, borders, muted text), always low-chroma neighbors of the base.

If you want the value in code, the vault ships nothing you have to trust blindly — every hex traces to a named site above.
