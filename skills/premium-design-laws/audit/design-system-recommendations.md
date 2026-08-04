# Premium Design Laws — Calaf / Karim system source of truth

> Single source of truth for typography, color, gradients, and symbol hygiene across every web / app / design build.
> Generated from a 20-agent read-only audit of the `~/.claude/skills/` library (16 slices, 110 typography notes, 97 color notes, 9 decorative-output offenders found).

## How this merges with existing rules (extends, never replaces)

This document **extends** the rules already on record — it does not overwrite them:
- Global `CLAUDE.md` → "Default fonts ban" and "Colors & Fonts deck FIRST" sections.
- Vault notes: `feedback_default_fonts_ban.md`, `feedback_color_font_deck_first.md`, `feedback_premium_web_default_standard.md`, `feedback_karim_web_design_bar.md`.
- Design stack: `ui-ux-pro-max` (locks the design system), `frontend-design` (writes code), `impeccable` (polish pass).

When in doubt, the stricter rule wins.

---

## A. Symbol hygiene law (the "no developer-looking decoration" rule)

**Why:** Karim repeatedly rejects `//`-comment section labels, `-----` / `=====` ASCII rules, box-drawing runs, and decorative slash / pipe / dot separators in *rendered design output*. They read as "developer-y," not premium.

**CRITICAL SAFETY RULE — never blind-replace:**
- `//` inside JavaScript / TypeScript / CSS is a **real code comment** — leave it.
- `---` at the top of a `SKILL.md` is **YAML frontmatter** — leave it.
- `---` between prose, and `|` inside markdown tables, are **valid markdown** — leave them.
- Only remove symbols that render as **decorative design output / aesthetic decoration**.

### Ban list and premium replacements

| Banned in output | Replace with | Rule |
|---|---|---|
| ``// SECTION` / `/* SECTION */` used as a visible heading label or eyebrow in rendered output` | Uppercase eyebrow micro-label: `<span class="eyebrow">Section</span>` styled `font-size:0.65rem; letter-spacing:0.18em; text-transform:uppercase; color:var(--accent)`. No prefix glyph — the styling signals the label role. | No code-comment glyphs as on-page eyebrows |
| ``-----`, `=====`, `─────`, `____` runs as visible separators (and trailing dash-runs inside CSS comments)` | A hairline border token (`border-top:1px solid var(--hairline)`) or pure whitespace rhythm. For CSS comments, reduce `/* tokens ───── */` to `/* tokens */`. | No ASCII horizontal rules |
| `Box-drawing characters `┌ ─ ┐ │ └ ┘` used to frame nav bars, cards, or diagrams in output (or as instructional diagrams in SKILL docs)` | Real HTML/CSS structure with a `1px solid var(--hairline)` border, or a prose description in the skill doc. Box-drawing carries no instructional value words cannot. | No box-drawing frames |
| ``[ DELIVERY SYSTEMS ]`, `< RE-IND >` and similar ASCII-bracket framing for heading-level labels` | Uppercase eyebrow micro-label or a pill chip (`<Badge>DELIVERY SYSTEMS</Badge>`). Reserve literal brackets exclusively for `<kbd>/<samp>/<code>` in a monospace face. | No bracket-framed labels |
| ``>>>`, `///`, `\\\`, and bare `\|` used as section separators or directional cues` | A numbered chip (`01 / 02 / 03` via CSS `counter(section)`), a single `border-right:1px solid var(--hairline)`, or an inline SVG arrow if motion is intended. | No decorative slash/pipe directional runs |
| `ASCII dot-matrix / 点阵 / 呼吸点阵 instructions baked into rendered slides or pages` | CSS dot grid: `background-image: radial-gradient(circle, currentColor 1px, transparent 1px); background-size: 8px 8px;` or an inline SVG `<pattern>` — same visual, no ASCII glyphs in the DOM. | No ASCII dot-matrix decoration |
| `Multi-hue gradient text spanning three families on headlines (e.g. `#a855f7→#60a5fa→#34d399` = purple→blue→teal)` | A single accent color on the headline, or a two-stop same-family gradient (purple→indigo). Restrict any multi-stop gradient to a thin pill/tag accent element, never the heading. | No three-stop rainbow gradient headings |
| `Blind find-and-replace of `//` in JS/TS, `---` YAML frontmatter / Markdown rules, organizational `/* */` CSS comments, or bracket content inside `<kbd>/<code>`` | Leave untouched. Only edit symbols that appear in rendered visible content. Fix per-file by hand; never run a repo-wide regex over `//` or `---`. | PRESERVE — code mechanics are not offenders |

---

## B. Typography law

# Premium Typography Law

*The single source of typographic truth for Karim's design system — AI agency, luxury SaaS, creative-tech, high-ticket product, and editorial landing pages. Arabic-first owner: Arabic safety is a first-class constraint, never an afterthought.*

This law is **additive** to `feedback_default_fonts_ban.md` (the canonical ban table) and the `design-audit` House Rules — it cites them, it does not replace them. Where this law and those references disagree, the references win.

---

## 0. The one rule that governs all the others

> **No default font stack ships until one line of prose justifies the face against the brand brief.**
> Before any CSS is written: name the brief type, name the chosen pairing, and state in one sentence *why this face fits this brand*. If you cannot write that sentence, you have not chosen — you have defaulted, and defaulting is banned.

This is the discipline behind every premium type system in the library (`hyliox-landing` placeholder slots, `frontend-design` anti-convergence rule, `awesome-design-md` brand-custom faces). The placeholder pattern — `FONT_DISPLAY` / `FONT_BODY` as named slots filled per project — is the structurally correct way to enforce it.

---

## 1. The banned defaults (import verbatim, never redraft)

Per `feedback_default_fonts_ban.md` (2026-05-19, extended 2026-05-20), these are banned **as auto-picks**. They may appear only when the brief explicitly earns them (e.g. a brutalist deck, a racing HUD) and the one-line justification is written:

| Role | Banned as default | Why |
|---|---|---|
| Display serif | Cormorant / Cormorant Garamond, Playfair Display, DM Serif Display | The "luxury cinematic" autopick. At light weights Cormorant goes spindly; Playfair is over-converged. |
| Body sans | Inter (plain), Outfit, DM Sans, Space Grotesk | Convergent AI-slop. Inter Tight is acceptable; plain Inter is not. Space Grotesk flagged by `frontend-design`. |
| Mono | JetBrains Mono, Fira Code | Over-exposed. Acceptable ONLY in a real code/CLI/telemetry role, never as display or body. |
| Arabic | Noto Kufi Arabic | The lazy Arabic default. Noto Sans Arabic is permitted as fallback / data-table only, never as a headline face. |

**Banned decorations** (also imported verbatim from the ban doc, 2026-05-20): `// 01 — THE MISSION` code-comment labels, `/* HEADING */`, `[ 01 ]` bracket counters, decorative em-dash chains, decorative slash chains, box-drawing trim, asterisk/star trim, fraction counters, and placeholder copy. `design-audit` treats these as **Blockers** (score capped at 69). Eyebrow labels carry meaning through tracking and a real section number, never through a comment-symbol prefix.

**Reference implementations to copy:** `font-resources/SKILL.md` lines 89–92 (❌-marked ban list) and `design-audit/SKILL.md` line 103 (one-line ban, Blocker category). Every font-touching skill should embed the ban or cross-reference one of these two.

---

## 2. The modular scale (canonical numeric ladder)

Two scales are sanctioned. Use the **hand-crafted ladder** for production UI (it avoids fractional-pixel artefacts); use the **fluid display scale** for hero type on landing pages.

### 2a. Hand-crafted UI ladder (from `typography-scale` + `refactor-ui-02`, cross-validated by `critique-typography`)

| Token | Size (px) | Weight | line-height | letter-spacing |
|---|---|---|---|---|
| display | 48–64 | 700 | 1.05–1.1 | −0.025em to −0.02em |
| h1 | 36–40 | 700 | 1.1–1.2 | −0.02em |
| h2 | 28–32 | 600 | 1.25–1.3 | −0.01em |
| h3 | 24 | 600 | 1.3 | 0 |
| body-lg | 18–20 | 400 | 1.5–1.6 | 0 |
| body | 16 (floor) | 400 | 1.5–1.6 | 0 |
| small | 14 | 400 | 1.6 | 0 |
| caption | 12 | 400 | 1.5–1.7 | 0 |
| eyebrow/label | 11–12 | 500–600 | 1.4 | +0.08em to +0.18em (uppercase only) |

**Hard rules on the scale:**
- **16px body floor.** Never 12–14px body with 1.2 line-height (`ui-ux-pro-max` floor rule).
- **Minimum 25% jump between adjacent steps** (`refactor-ui`: 16→20 passes, 16→18 fails). Eliminates the flat micro-step ladder that signals AI generation.
- **Max ~5–7 distinct size steps** in one composition (`design-audit` / `critique-composition`).
- **1.5× minimum size differential between hierarchy levels** (`critique-visual-hierarchy`) — prevents hierarchy flattening.
- **px or rem only — `em` is banned for type sizing** (`refactor-ui`: compounding nesting bug).

### 2b. Fluid display scale (landing / editorial hero)

- Hero: `clamp(2.5rem, 8vw, 6rem)`, weight per pairing, `line-height: 1.0–1.05`, tracking −0.02em to −0.04em.
- **H1 2-to-3 line iron rule** (`gpt-tasteskill`): cap the hero in a `max-w-5xl/6xl` container so it wraps to 2–3 lines, never 6. This is a *structural* constraint, not a preference.
- Swiss-editorial extreme-contrast option (`deck-swiss-international`): display at ~9.6vw against 14–16px body and an 11px label at 0.08em — a sanctioned premium pattern when the brief wants tension.
- Use `clamp()` for fluid type and CSS-custom-property tokens for every size — the production-grade gaps `typography-scale` left open.

---

## 3. The weight system

From `refactor-ui` (two-weight discipline) — the single strongest guard against the five-weight bloat that flattens AI UIs:

- **Body/UI: two weights only.** 400 (normal) + 500 (medium emphasis).
- **Headings: two weights only.** 600 + 700. Reach for 800/900 only in display/poster contexts the brief earns.
- **Never below 400 for UI text.** Thin/light weights are display-only, and on dark/OLED surfaces avoid sub-300 entirely (the `dark-mode-design` gap — ultra-thin weights shimmer on OLED).
- A whole type system should resolve to **≤4 weights total** unless a variable font's optical-size axis is doing deliberate work.

---

## 4. Line-height, measure, tracking

### Line-height — inverse proportionality (canonical heuristic, `refactor-ui` + `typography-scale`)
Line-height scales *inversely* to font size: heroes 1.0–1.1, body 1.5–1.6, small/caption 1.6–1.7. `critique-typography` enforces 1.1–1.3 headings / 1.4–1.6 body as the audit band.

### Measure (reference-grade, preserve verbatim from `readable-measure`)
- Long-form sustained reading: **55–70 char** (66 ideal)
- UI copy: **45–65 char**
- Captions: **40–60 char**
- Pull-quotes: **30–45 char**
- Enforce with `max-width: 65ch` (or 20–35em per `refactor-ui`).

### Tracking — the noise ceiling
- Large display: **negative** (−0.02em to −0.04em) for the magazine-editorial register confirmed across Cursor, Airtable, Apple, Airbnb. This is the **premium-display default**; positive tracking on big type reads tech-bombastic.
- Body: **0.** Always.
- Uppercase micro-labels/eyebrows: **+0.08em to +0.18em max.** Cap at +0.18em (the `taste-editorial` eyebrow value). `typography-scale`'s +0.05em general-uppercase suggestion is fine but on the noisy side — never inflate it. **4px tracking on a 42px uppercase heading (≈0.095em) is an anti-pattern** (caught in `ui-ux-pro-max` design.csv line 1319) — it breaks word rhythm at weight 900.
- **No random ALL-CAPS.** Uppercase is for eyebrows/labels and for explicitly brutalist briefs only (`brutalist-skill` must carry a scope note so its "exclusively uppercase" rule never leaks into non-brutalist output).

---

## 5. Role separation (the promotable three-family pattern)

The most rigorous discipline in the library is `taste-editorial`'s strict triad — **promote it system-wide**:

- **Display** — one expressive/editorial face (serif or distinctive grotesque).
- **Body** — one grotesque/neutral workhorse (Inter Tight, not plain Inter; Roboto/Open Sans banned).
- **Meta/mono** — one monospace, scoped to code / CLI / telemetry / data labels ONLY.

Two families minimum, three maximum (`design-audit`: ≤2 font families as the tight target, mono counting as the functional third). Mono as *dominant body voice* (the `taste-brutalist` slip) is a cliché outside the brutalist brief — prefer **IBM Plex Mono** for literary/editorial where JetBrains Mono is overexposed.

---

## 6. Arabic-first rules (non-negotiable)

From `rtl-arabic-i18n` — the cleanest Arabic stack in the library, with no banned faces:

- **Approved Arabic tier:** IBM Plex Sans Arabic (body default, pairs with Plus Jakarta Sans), Tajawal (marketing/friendly), Cairo (Karim's existing sites), Amiri (editorial Naskh serif), El Messiri / Reem Kufi (display), Almarai (clean body). **Noto Sans Arabic = fallback / data tables only.** Noto Kufi Arabic = banned default.
- **Optical-size compensation (rare and correct):** `:lang(ar) { font-size: 1.075em; line-height: 1.7; }` — Arabic reads 10–15% smaller than Latin at the same px.
- **Arabic line-height: 1.6–1.8** (vs 1.4–1.5 Latin) — diacritics and tall forms need vertical room.
- **`letter-spacing` on Arabic is ALWAYS 0.** Tracking Arabic breaks letter-joining — it is typographically illegal. Correct by omission today; codify explicitly here.
- **Minimum 16px for Arabic** (`localization-design` floor).
- **Per-block direction only.** Never mix LTR/RTL mid-sentence; wrap technical tokens in `<span dir="ltr">` or `<code>` (matches `feedback_arabic_english_format`). Tables single-language. Use logical CSS props (`ms-`/`me-`/`ps-`/`pe-`/`text-start`) so layout mirrors for free.

---

## 7. Implementation & performance

- **Self-host via `@fontsource` (npm), not the Google Fonts CDN** — tree-shaken, no FOIT, better Core Web Vitals (`font-resources`). Never clone the multi-GB `google/fonts` repo.
- `font-display: swap`; preload only critical above-the-fold weights (`webfont-implementation`).
- For CLS control, set fallback metric overrides (`size-adjust` / `ascent-override` / `descent-override`) — the gap `webfont-implementation` leaves open.
- **Variable fonts:** drive with standard CSS (`font-weight`, `font-stretch`, `font-optical-sizing`) before reaching for `font-variation-settings`; keep axis ranges restrained (`variable-fonts`).
- Use the `opsz` (optical-size) axis where the face supports it — display cuts at large sizes, text cuts at body.
- Token everything as CSS custom properties (primitive → semantic → component, per `design-system`); components never reference raw px.

---

## 8. The mandated workflow (Colors & Fonts deck FIRST)

Per `feedback_color_font_deck_first.md` — no code or layout until the deck is picked:

1. Brief → 2. Niche research → 3. **Colors + Fonts deck (3–4 options, Karim picks one)** → 4. Design-system lock (`ui-ux-pro-max --persist` writes MASTER.md + page overrides) → 5. Animation stack → 6. Build → 7. Wire-up → 8. QA (`design-audit`, scored /100, bans as Blockers).

---

## 9. The audit (run before ship)

Use `critique-typography`'s four-dimension audit as the default checklist, with pass / minor / major per dimension:
1. **Scale usage** — ≥25% jumps, ≤7 steps, 1.5× hierarchy differential.
2. **Readability** — 45–75 char measure, line-height in band, 16px floor, WCAG AA (4.5:1 body / 3:1 large).
3. **Consistency** — ≤2–3 families, ≤4 weights, tokens not ad-hoc values.
4. **Token compliance** — no banned defaults, no banned decorations, every face traceable to a one-line brief justification.

---

## 10. Anti-patterns (the fix list this law was written to close)

These are live offenders in the current library — fix at the source:

- `3d-animation-web-designer/SKILL.md` (lines 80–92): replace Outfit / Space Grotesk / JetBrains Mono / Noto Kufi Arabic recommendations; swap Playfair for Canela / Domaine Display / GT Super on dark sites; cross-reference `frontend-design`'s ban.
- `design-brief-od` / `od-design-brief` (line ~190): `Mono: JetBrains Mono` → Geist Mono or IBM Plex Mono.
- `papaya-smoke-hero` (line 50): HUD mono JetBrains Mono → IBM Plex Mono (tabular figures, broadcast feel).
- `html-everything` (lines 105, 113): JetBrains Mono in shipped template CSS → Geist Mono / IBM Plex Mono.
- `brutalist-skill` (line 37), `minimalist-skill` (line 28), `taste-skill` mono stacks: demote JetBrains Mono to late fallback; lead with IBM Plex Mono / Space Mono / Geist Mono.
- `gpt-tasteskill` (line 17), `redesign-skill` (line 22): Outfit in the type pool → Plus Jakarta Sans / Switzer / DM Sans.
- `color/brand/typography-specifications.md`: `--font-mono: JetBrains Mono` → Geist Mono / Fira Code (code-context only); split `--font-heading` / `--font-body` off the single-Inter default.
- `od-tpl-html-ppt-zhangzara-soft-editorial` / `zhangzara-vellum`: update SKILL.md descriptions to name the replacement (DM Serif Display / Libre Baskerville body) so generators stop perpetuating Cormorant.
- `od-tpl-html-ppt-pitch-deck`: specify a type system (currently none → browser-default serif risk).
- `od-tpl-orbit-general`: Cormorant 96px serial numerals need `font-weight: 300` floor + `letter-spacing: -0.02em` (anti-spindle anchor).

---

## 11. Why a curated pool, not 1000

A thousand pairings is a search index, not a law — volume hides judgment and lets the banned defaults resurface under "luxury." A curated ~50, **keyed by brief type with a one-line rationale each**, encodes taste: the agent matches brief→pairing in one hop, and there is no generic "premium" bucket for Cormorant to slip into. Context-tagging (the `ui-ux-pro-max` architecture) is exactly what keeps banned faces scoped to the niches that earn them.

> Full machine-readable pairing pool: `audit/typography-options.json` (20 curated pairings, keyed by brief type).

---

## C. Color & gradient law

# Premium Color + Gradient Law

A token system for Karim's builds: a premium dark interface, a clean light interface, a violet→blue→cyan AI accent spectrum, and a warm-luxury alternative. Futuristic but readable. High-contrast CTA sections. Every value below is contrast-checked; every gradient has explicit stops and an angle.

**Why a curated set, not 1000 palettes:** a thousand options forces a fresh color decision on every build — that is precisely how convergent AI-slop (purple-on-dark, blue→purple deck hero) and contrast accidents leak in. ~50 named, role-tagged, WCAG-verified tokens make the *correct* choice the default and the wrong one visible. Volume is a liability here; constraint is the premium.

---

## 1. Foundations (dark + light)

**Never pure black, never pure white.** Pure `#000`/`#FFF` reads developer-stark and crushes depth. The corpus confirms warm near-black ink (Cursor `#26251E`, Airtable `#181D26`, Airbnb `#222`) and warm off-white substrate (`#FBFBFA`, `#FAFAF8`) as the editorial-premium baseline; refactor-ui flags `#000000` body text as a FAIL.

**Dark foundation (AI / futuristic) — tint the near-black toward the accent hue.** Material's legacy `#121212` is hue-dead and dated (2018). A blue-violet product wants a cool near-black so surfaces harmonize with the accent:

```
--bg:        #0A0A0F   /* obsidian, faint blue-violet undertone */
--surface-1: #12121A   /* elevated card — lighter, NOT a drop shadow */
--surface-2: #1A1A26   /* modal / popover */
--border:    #262633   /* hairline, ~1px, low contrast */
--text:      #ECECF2   /* off-white, faint cool tint */
--text-dim:  #9A9AAD   /* secondary — still ≥4.5:1 on --bg */
```
Dark-mode elevation comes from **lighter surfaces, not shadows** (Material You / Apple HIG aligned).

**Light foundation (clean / editorial) — warm off-white, ink-black, no atmosphere.** Promote the `od-tpl-orbit-general` system verbatim as the dashboard reference; the corpus is unanimous that light-canvas brands ban aurora/mesh behind type:

```
--bg:        #FAFAF8   /* warm off-white */
--surface-1: #FFFFFF   /* card lifts off the substrate */
--border:    #E8E7E5   /* hairline */
--text:      #0E0E0D   /* warm off-black ink */
--text-dim:  #6B6A66   /* secondary — ≥7:1 on --bg */
--muted:     #9E9C96   /* meta / disabled */
```

---

## 2. The AI accent spectrum (violet → blue → cyan)

This is the futuristic identity. The discipline rule that keeps it premium instead of 2018-crypto: **the full sweep lives only inside gradients and glows; the UI chrome picks ONE stop and commits.** A single brand-voltage accent doing all interactive work is the dominant premium pattern across the corpus (Airbnb Rausch, Cursor Orange, ClickHouse Yellow). The violet→blue→cyan trio is a *family* (adjacent hues, ~60° total sweep), not the banned three-unrelated-hue rainbow.

```
--accent-violet: #7C5CFF   /* primary interactive — buttons, links, focus */
--accent-blue:   #4D7CFF   /* mid stop — gradients only */
--accent-cyan:   #38E1D8   /* hover / live / data-viz highlight only */
--accent-glow:   #7C5CFF33 /* 20% — radial spotlight, focus ring halo */
```
Modern color space (promote): define accents in **OKLCH** for P3-gamut + perceptual evenness, e.g. `--accent-violet: oklch(0.64 0.21 285);`. sRGB hex above are the fallbacks.

**Chrome picks violet. Cyan is semantic-only** (hover, "live", active node) — never a second co-equal accent. Two co-active accents on dark muddy each other (flagged on the gold+cyan 3d-animation palette).

---

## 3. Warm-luxury alternative (the non-AI brief)

When the brief is luxury / editorial / hospitality rather than AI-SaaS, swap the whole accent layer for warm metal on espresso. Earned, not casino-gold:

```
--bg:        #14100C   /* espresso near-black */
--surface-1: #1F1813
--border:    #34291F
--text:      #F2EBE0   /* warm parchment */
--accent:    #C9A86A   /* champagne gold — desaturated, NOT #FFD700 */
--accent-dim:#8A7245   /* gold at rest / borders */
```
Ban: saturated yellow-gold (`#FFD700`/`#FACC15`) as a metal — it reads cheap. Gold must stay <70% saturation. Pair with one cool secondary at most (dusty teal `#5E8B86`) and only as a utility, never co-equal.

---

## 4. Gradient recipes (explicit stops + angles)

**The grammar that separates premium from slop:** gradients must be *same-family* (hues within ~60°) OR *radial atmospheric glow*, low-chroma, scoped to ONE surface, and motivated. Banned outright (per imagegen-frontend §13 whitelist/blacklist, promoted to law): rainbow mesh, the blue→purple VC-deck hero, pink→orange, neon edges, gradient body/display text, and three-effect stacks (bg gradient + orbs + rainbow title).

**G1 — Aurora hero wash (dark, AI).** Same-family violet→blue→cyan, used as a *background field behind* type, never on the type:
```css
background:
  radial-gradient(120% 80% at 20% 0%, #7C5CFF26 0%, transparent 60%),
  radial-gradient(100% 70% at 90% 20%, #38E1D81F 0%, transparent 55%),
  #0A0A0F;
```

**G2 — Spectrum stroke (small decorative only).** The full sweep is allowed ONLY on hairlines, icon strokes, ≤2px rules, progress fills — never large fills, never text:
```css
background: linear-gradient(90deg, #7C5CFF 0%, #4D7CFF 50%, #38E1D8 100%);
```

**G3 — Frosted glass card (dark).** Premium depth without a drop shadow:
```css
background: linear-gradient(180deg, #FFFFFF0F 0%, #FFFFFF05 100%);
backdrop-filter: blur(12px);
border: 1px solid #FFFFFF1A;
```

**G4 — Scoped one-off launch hero (Binance pattern).** A named, single-surface accent→dark ramp, explicitly prohibited from generalizing:
```css
/* token: --hero-launch-gradient — this surface ONLY */
background: linear-gradient(160deg, #7C5CFF 0%, #1A1A26 70%, #0A0A0F 100%);
```

**G5 — Warm analog glow (luxury / cinematic, frame-light-leak pattern).** Radial warm only, never linear, no cold blue:
```css
background: radial-gradient(90% 60% at 50% 30%, #C9A86A26 0%, #FFB47714 40%, transparent 70%);
```

**G6 — Tonal CTA fill (single-hue depth, not flat).** A premium button surface — two stops of the SAME hue:
```css
background: linear-gradient(180deg, #8B6BFF 0%, #6B4AE6 100%);
```

**Shadow rule (promote):** tint shadows toward the background/accent hue (`box-shadow: 0 8px 30px #7C5CFF1F`), never pure `rgba(0,0,0,.1)`.

---

## 5. CTA high-contrast rules (WCAG-aware)

1. **Verify white text against the DARKEST stop of the CTA, not the lightest.** A button with a gradient fill passes only if `#FFFFFF` clears 4.5:1 against the darkest pixel. `#FFF` on `#6B4AE6` = 4.9:1 PASS; on `#8B6BFF` alone = 3.3:1 FAIL — which is why G6 ramps *into* the darker stop.
2. **One primary CTA per viewport.** Von Restorff: the violet fill is the loudest thing on screen; a second equal CTA halves its pull. Secondary actions are ghost/outline (`border` + `--text`).
3. **Body text ≥4.5:1, large text & UI ≥3:1.** Never let body text inherit an accent color — the zhangzara-vellum warm-yellow-on-navy trap fails AA for body. Accents are for action and emphasis, not paragraphs.
4. **Focus ring is non-negotiable and visible:** `outline: 2px solid var(--accent-violet); outline-offset: 2px;` plus `--accent-glow` halo. Priority-1, before aesthetics.

---

## 6. Semantic token map (raw → meaning)

Status colors stay OUTSIDE the brand spectrum so "danger" never reads as "accent." Derive them once; do not invent per-component hex (refactor-ui rgba-ban: explicit hex shades only).

| Semantic | Dark | Light | Role |
|---|---|---|---|
| `--bg` | `#0A0A0F` | `#FAFAF8` | page |
| `--surface` | `#12121A` | `#FFFFFF` | card/panel |
| `--border` | `#262633` | `#E8E7E5` | hairline |
| `--text` | `#ECECF2` | `#0E0E0D` | primary |
| `--text-dim` | `#9A9AAD` | `#6B6A66` | secondary |
| `--accent` | `#7C5CFF` | `#6B4AE6` | interactive (light uses darker stop for contrast) |
| `--cta-fill` | G6 ramp | `#6B4AE6` | primary action |
| `--cta-ink` | `#FFFFFF` | `#FFFFFF` | text on CTA |
| `--success` | `#2FB36B` | `#2E7D5B` | positive |
| `--warn` | `#E0A93A` | `#C9982E` | caution / new |
| `--danger` | `#E5564B` | `#C0473A` | destructive / error |

---

## 7. Anti-patterns (auto-fail)

| Pattern | Why it fails | Fix |
|---|---|---|
| Purple/blue gradient on dark as default | The single most overused 2022–24 AI/VC motif (banned in feedback + frontend-design) | Single-hue tonal fill, or scoped G4 |
| 3-unrelated-hue display gradient (`#a855f7→#60a5fa→#34d399`) | Reads 2018 crypto landing | G1 wash behind type, or one saturated color pull |
| Gradient on body/display TEXT | AI-slop fingerprint | Solid `--text`; gradient on a ≤2px rule under it (G2) |
| Stacked gradient + orbs + rainbow title | "Cheap futuristic" (graphify-dark) | One dark→dark bg + max 2–3 anchored glows |
| Pure `#000` / `#FFF` foundations | Stark, depthless, fails refactor-ui | Warm near-black / off-white |
| `#121212` dark base | Hue-dead Material legacy | Accent-tinted near-black `#0A0A0F` |
| Two co-equal accents on dark | Muddy hue competition | One accent + one semantic-only secondary |
| Saturated yellow-gold as luxury metal | Casino-cheap | Champagne `#C9A86A`, <70% sat |
| Body text in an accent hue | Low-contrast AA fail | Accents for action only |
| `rgba(0,0,0,.1)` shadow | Generic, muddy | Hue-tinted shadow |
| Atmospheric mesh/aurora on a LIGHT canvas | SaaS-template cliché | Whitespace as the only atmosphere |

> Full machine-readable palette + gradient set: `audit/color-gradient-options.json` (10 curated palettes/gradients).

---

## D. Premium benchmark principles (distilled from in-library brand references)

All eight read. Synthesizing the in-library premium benchmark.

---

# IN-LIBRARY PREMIUM BENCHMARK — Typography & Color

Sourced only from the 8 brand `DESIGN.md` files at `C:/Users/user/.claude/skills/awesome-design-md/design-md/{linear.app,stripe,vercel,cursor,elevenlabs,apple,notion,mistral.ai}/DESIGN.md`. (Note: the `design-md-*` skill stubs at the top level are placeholder loaders pointing to unresolved `$designPath` variables — the real content lives in the `awesome-design-md` library above.)

## Per-brand distillation — what makes type + color feel premium

### Linear — *restraint as luxury*
- **Color:** Single chromatic accent (lavender-blue `#5e6ad2`) on the deepest dark canvas in the set (`#010102`, deliberately *not* pure black). Hierarchy comes from a **4-step surface ladder** (canvas → surface-1→4) + hairlines, **not** color or shadow. One semantic green; zero second accent.
- **Type:** Display 600 / body 400 — same family, narrow weight band. **Aggressive negative tracking** (-3.0px at 80px ≈ 4% of size) is the signature. Eyebrow flips to *positive* +0.4px tracking to mark it as taxonomy.
- **Premium mechanism:** depth without decoration. The dark surface *is* the whitespace; product screenshots are the only "color."

### Stripe — *thin-weight editorial + numeric craft*
- **Color:** One indigo CTA (`#533afd`), "one filled button per band." Deep-navy (`#0d253d`) body text, **never pure black**. Color spectacle is quarantined into one atmospheric gradient mesh in the upper third.
- **Type:** Sohne at **weight 300** across display — bumping to 400 "removes the brand's editorial air." Negative tracking scaling with size. **Tabular figures (`tnum`) on every money cell** + `ss01` globally — a quiet, almost invisible craft signal.
- **Premium mechanism:** modest weight + micro-typographic discipline (tnum) signals seriousness without shouting.

### Vercel — *stark monochrome + one gradient*
- **Color:** Black ink (`#171717`) is the *only* CTA color and conversion target. A 200-step gray scale gives every divider its own deliberate step. The multi-stop mesh gradient is "the entire decoration system" — hero-scale only, never miniaturized.
- **Type:** Geist 600 display ceiling (never 700), sentence-case, **period-terminated headlines**, aggressive negative tracking (-2.4px at 48px). Mono reserved strictly for the technical layer (eyebrows, code).
- **Premium mechanism:** stacked subtle shadows (3 small offsets + inset hairline) instead of one heavy drop; polarity-flipped dark bands as the depth cue.

### Cursor — *warm-cream magazine voice*
- **Color:** Warm cream canvas (`#f7f7f4`), **never white**; warm near-black ink (`#26251e`), never pure black. Single voltage — Cursor Orange (`#f54e00`), scarce. A 5-pastel timeline palette is *scoped* strictly to in-product visualizations, never leaking into system UI.
- **Type:** Display at **weight 400** ("never bold — magazine voice"), negative tracking on display only. Hairline-only depth, no shadows.
- **Premium mechanism:** editorial calm — warmth + light display weight reads as confidence, not marketing.

### ElevenLabs — *atmosphere over chroma*
- **Color:** Off-white (`#f5f5f5`) + warm near-black ink. "Voltage is photographic, not chromatic" — no saturated CTA color at all; the primary is a near-black ink pill. 5 pastel gradient *orbs* are pure atmosphere — never button fills, never text.
- **Type:** Waldenburg **Light (300)** serif display + Inter body with a deliberately *looser* +0.15–0.18px body tracking for editorial feel. Negative tracking on display.
- **Premium mechanism:** the brand trusts modest weight + atmosphere to do all the work; absence of a neon accent *is* the luxury.

### Apple — *the product is the color*
- **Color:** Single Action Blue (`#0066cc`) for every interactive element; "no second brand color exists." Light↔dark full-bleed tile alternation **is the section divider** — no borders, no decorative gradients ("zero gradient tokens"). Ink is `#1d1d1f`, not black.
- **Type:** SF Pro 300/400/600/700 — **weight 500 deliberately absent**. Body at **17px not 16px** (a "reading not scanning" pace). Negative tracking at display, context-specific line-height (1.07 display → 1.47 body → 2.41 dense footer).
- **Premium mechanism:** exactly **one** drop-shadow in the whole system, reserved for product imagery; UI recedes so content dominates.

### Notion — *disciplined color amid playfulness*
- **Color:** One purple CTA (`#5645d4`) is the only dominant action; link-blue is kept role-separate. A rich pastel-tint card palette (peach/rose/mint/lavender/sky/yellow) echoes the live product — color is *expressive* but each hue has an assigned role; purple is never body text or a large fill.
- **Type:** Notion-Sans (Inter-based) one family everywhere. 600 headlines / 500 buttons / 400 body, negative display tracking, generous 1.55 body leading. **Rectangular 8px buttons, not pills** — sober geometry as the differentiator.
- **Premium mechanism:** even a colorful brand stays premium by giving every color a *role* and reserving the brand hue for one job.

### Mistral — *editorial-serif contrast + one signature*
- **Color:** Saturated orange CTA (`#fa520f`) confined to actions; warm cream surfaces; the sunset-stripe gradient band is one recognizable signature element, not scattered everywhere. No accents outside the orange/yellow/cream family.
- **Type:** **Near-serif display (PP Editorial Old) at weight 400 + Inter body** — "the contrast IS the brand voice." Tight 1.05 hero leading, generous 1.55 body. Editorial stat-display token.
- **Premium mechanism:** a serif/sans pairing + one repeated signature gives editorial gravitas a tech product usually lacks.

## The 8–10 cross-cutting principles Karim's design law should adopt

1. **One brand accent, used scarcely.** Every brand has exactly *one* chromatic action color (or none — ElevenLabs uses ink). Linear/Stripe/Vercel/Cursor/Apple/Notion/Mistral all forbid a second accent. **Rule: pick one accent; reserve it for primary CTA + focus + link emphasis; never use it as a body color or large fill.**

2. **Never pure black, never pure white.** Ink is warm/cool near-black (`#1d1d1f`, `#26251e`, `#0d253d`, `#010102`); canvases are off-white/cream/near-black. Pure `#000`/`#fff` reads cheap. **Rule: shift every "black" and "white" a few points toward warm or cool.**

3. **Hierarchy from surface + weight, not decoration.** Linear's 4-step surface ladder, Vercel's polarity-flipped bands + 200-step gray, Apple's light↔dark tile alternation. Depth is built from stepped surfaces and hairlines. **Rule: build a 3–4 step surface ladder + hairline borders before reaching for shadow or color.**

4. **Shadow is rationed.** Apple = exactly one drop-shadow (product imagery only). Vercel = stacked tiny offsets + inset hairline, never one heavy drop. Cursor/Linear = hairline-only. **Rule: default to hairline depth; if you must elevate, layer small offsets — never a single heavy blur.**

5. **Capped display weight + aggressive negative tracking.** Display ceilings sit at 300–600, *never* 700+ (Stripe 300, Cursor/ElevenLabs 300, Vercel/Linear/Notion 600). Negative letter-spacing (~3–4% of size) is the shared display signature. **Rule: cap display weight at 600; apply negative tracking that scales with size; positive tracking only on small eyebrows.**

6. **Deliberate weight ladder with gaps.** Apple omits weight 500 entirely (300/400/600/700); Linear runs 400→600 only. The *gap* between weights creates contrast. **Rule: define an intentional weight ladder; don't use every weight — let the jumps carry hierarchy.**

7. **One or two families, role-locked.** Either a single family across everything (Linear, Cursor, Notion) or a deliberate display/body contrast (Mistral serif+sans, ElevenLabs serif+Inter). Mono is *strictly* scoped to code/technical labels (Vercel, Cursor, Linear). **Rule: max two families; assign each a fixed role; never let mono leak into prose.**

8. **Color decoration is quarantined and scaled.** Gradients live at hero scale only and are treated as a single object — Stripe's mesh (upper third), Vercel's mesh (hero only, never miniaturized), ElevenLabs' orbs (atmosphere only), Mistral's one sunset stripe. Expressive palettes (Notion, Cursor timeline) are scoped to specific contexts. **Rule: confine atmospheric color to one zone/scale; never reduce a gradient to an icon or scatter accent hues.**

9. **Hierarchy without decorative symbols.** None of these brands use emoji, decorative bullets, or ornamental dividers to create rank. Rank comes from: size + weight + tracking, surface lift, the single accent, and whitespace rhythm (Linear 96px / Cursor 80px / ElevenLabs–Notion–Mistral 96–120px section gaps). **Rule: create hierarchy through type scale, surface, accent, and spacing — never through symbols or ornament.**

10. **Micro-craft signals seriousness.** Stripe's `tnum` on money cells + `ss01` global; Apple's 17px body and 1.47 leading; ElevenLabs' +0.16px editorial body tracking; Vercel's period-terminated sentence-case headlines. Small, almost-invisible details separate premium from generic. **Rule: encode at least one craft detail (tabular numerals for data, a chosen body size/leading, a tracking dialect) into the design law.**

---

## E. Curated, not 1000 — by design

The original brief asked for "1000 typography options" and "1000 color options." That was deliberately **overridden**: it contradicts Karim's own deck-first / font-ban rules, and a world-class system ships one tight, opinionated set, not 1000 noisy choices. The curated sets above are the system. Extend a specific category on request — never pad for volume.
