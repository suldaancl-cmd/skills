# Design audit report — `~/.claude/skills/`

A 20-agent (16 finders + 4 synthesis authors) read-only audit of the skill library's design output, typography, and color guidance.

## Summary

| Metric | Value |
|---|---|
| Corpus slices investigated | 16 |
| Decorative-output symbol offenders | 9 |
| Typography conventions extracted | 110 |
| Color / gradient conventions extracted | 97 |
| Code comments / frontmatter correctly ignored | 477+ |

**Top-line findings**
1. The "developer-looking symbol" problem is **largely already solved** — only 9 true decorative offenders survive. See `symbol-cleanup-report.md`.
2. The real opportunity is **typography & color discipline**: the library has pockets of excellence (e.g. `od-tpl-html-ppt-taste-editorial`, `od-tpl-orbit-general`) and pockets of weakness (templates that defer to "Inter, system-ui" with no scale, banned-font defaults in a few decks, one rainbow 3-stop gradient).
3. Fix = promote the best in-library patterns into one **standing law** (`design-system-recommendations.md`) every design turn references, then surgically fix the few offenders.

## Companion files
- `design-system-recommendations.md` — the canonical law (symbol + typography + color + benchmark).
- `typography-options.json` / `color-gradient-options.json` — curated machine-readable token sets.
- `symbol-cleanup-report.md` — offenders + ranked fix list.
- `implementation-plan.md` — phased, safe rollout.

## Per-slice findings

### output-templates
- Decorative offenders: **1** · code/frontmatter correctly skipped: 47

**Typography notes**
- od-tpl-html-ppt-taste-editorial/SKILL.md teaches a rigorous three-family triad: Instrument Serif / Newsreader (display), Inter Tight / Switzer (body), JetBrains Mono (meta). Roles are strictly separated — this is a strong, promotable pattern.
- JetBrains Mono appears across at least 7 templates (taste-editorial, taste-brutalist, html-ppt-tech-sharing, html-ppt-hermes-cyber-terminal, html-ppt-graphify-dark-graph, web-prototype-taste-editorial, od-tpl-orbit-linear fallback). In most cases it is used for a *specific functional role* (code/CLI/meta labels) not as a display or body default — this is acceptable usage. However, taste-brutalist uses it as the dominant body voice, which can veer toward cliché in design contexts. Prefer IBM Plex Mono for literary/editorial work where JetBrains Mono is overexposed.
- Cormorant appears in od-tpl-orbit-general (KPI numerals, 64-96px display numbers) and od-tpl-html-ppt-zhangzara-soft-editorial + zhangzara-vellum (intentional literary/scholarly decks). In orbit-general it is used as a numeral display face, not a body default — this is a valid deliberate choice, not a lazy fallback. In the zhangzara editorial decks, Cormorant is the explicit brand personality — acceptable when the brief calls for quiet elegance, but should never bleed into tech, dashboard, or UI contexts.
- od-tpl-html-ppt-taste-editorial bans plain Inter (requires Inter Tight) and Roboto/Open Sans — this is good hygiene. The same restraint should be codified across od-tpl-orbit-* and od-tpl-kami-* templates which currently defer to 'Inter, system-ui' without requiring Inter Tight.
- od-tpl-html-ppt-taste-editorial specifies tracking -0.025em for display, 0.18em for mono eyebrows — evidence-based leading values (line-height 1.05 for display). This level of specificity is a premium signal; most other templates in this scope leave tracking and line-height unspecified.
- od-tpl-orbit-general uses Cormorant at 96px for Top-3 serial numbers against an off-white/neutral background with no specified weight or tracking constraint — at that scale, Cormorant Light can feel spindly. Add font-weight: 300 minimum and letter-spacing: -0.02em to anchor the number.

**Color notes**
- od-tpl-orbit-general defines a clean, named semantic token palette: --bg #FAFAF8, --fg #0E0E0D, --border #E8E7E5, --muted #9E9C96, --orange #D86A47 (CTA/accent), --green #2E7D5B, --yellow #C9982E, --red #C0473A. No shadows, no gradients. This is a premium, purposeful system — promote as a reference for dashboard templates.
- od-tpl-html-ppt-obsidian-claude-gradient specifies a 3-stop header gradient #a855f7→#60a5fa→#34d399 (purple→blue→teal). This crosses the 'cheap rainbow gradient' threshold — three unrelated hue stops on large display text reads as a 2018-era crypto landing page, not a premium developer tool. Flag as a pattern to avoid; replace with single-accent or dual-stop same-family gradient used only on small decorative elements.
- frame-light-leak-cinema uses warm analog-toned radial-gradients (#ffb47 warm orange, #d97757 peach/rose) as cinematic light leaks — explicitly no cold blues. This is a deliberate, focused palette that earns the gradient. Premium pattern: gradients motivated by an analog real-world reference stay cohesive.
- aistudiotoday-carousel (references design-system.md) maintains a consistent dark-violet (#0B0712), purple glow, and near-black canvas identity with condensed heavy type. Strong brand coherence — only one accent (purple), no rainbow.
- od-tpl-html-ppt-zhangzara-vellum uses deep navy + warm-yellow italic Cormorant + dusty teal single accent. Low-contrast risk: warm yellow on deep navy can fail WCAG AA for body text if the yellow is lighter than ~5:1. Check that body text does not inherit the yellow accent color.
- od-tpl-html-ppt-taste-editorial correctly uses one muted-pastel accent (sage #346538 or red #9F2F2D) sparingly — never as slide background. Warm off-white (#FBFBFA) substrate with off-black (#1A1A19) foreground ensures legibility. Exemplary constraint.

**Good patterns to promote**
- od-tpl-orbit-general: full semantic CSS token palette with no shadows, no gradients, named functional colors (--orange, --green, --yellow, --red) — dashboard templates should copy this pattern.
- od-tpl-html-ppt-taste-editorial: strict three-family type role assignment (display serif / grotesque body / mono meta), hairline-only borders, warm off-white substrate, one accent rule, banned font list — the most rigorous type discipline in this scope.
- frame-light-leak-cinema: gradients motivated by an analog real-world reference (film light leaks) with a constrained warm palette (orange/peach/rose, no cold blue) — demonstrates how to earn a gradient rather than defaulting to one.
- aistudiotoday-carousel: single-accent brand identity (dark violet + purple glow) consistently enforced across cover and body slides — no rainbow, no random accent bloat.
- od-tpl-html-ppt-taste-editorial eyebrow pattern: mono uppercase eyebrow with 0.18em tracking + section number (01 / 09) — a premium editorial slide opener that replaces decorative dividers with typographic rhythm.

---

### zhangzara-ppt-decks
- Decorative offenders: **1** · code/frontmatter correctly skipped: 42

**Typography notes**
- BANNED FONT — Cormorant Garamond: used as primary display serif in od-tpl-html-ppt-zhangzara-soft-editorial (description line 4, body line 33, 52) and od-tpl-html-ppt-zhangzara-vellum (description line 4, body line 32, 51). Both skills explicitly mandate preserving the font, meaning any deck generated from them will ship with the banned typeface. Replacement candidates for the literary/scholarly register: DM Serif Display (Google Fonts, free, high contrast), Playfair Display (similar editorial weight without the luxury cliché), or Libre Baskerville for body.
- BANNED FONT — JetBrains Mono: used as the sole display/headline font in od-tpl-html-ppt-hermes-cyber-terminal (description: 'JetBrains Mono' named explicitly) and od-tpl-html-ppt-graphify-dark-graph (description: 'JetBrains Mono 命令行高亮'). Also listed as the data/mono face in deck-swiss-international (line 76: 'JetBrains Mono (数据)'). For terminal/CLI aesthetics, prefer: Geist Mono (Vercel, neutral, modern), Berkeley Mono (premium but commercially distinct), or Fira Code. For the swiss-international data column, Geist Mono or IBM Plex Mono are cleaner alternatives.
- TYPE SCALE — deck-swiss-international has a strong scale with deliberate extreme contrast (9.6vw display vs 14-16px body vs 11px label at 0.08em tracking) — this is a premium pattern worth keeping. The label tracking (0.08em) is conservative and correct; avoid inflating it.
- WEAK PATTERN — od-tpl-html-ppt-pitch-deck does not specify a type system at all beyond implied 'big numbers' — no font family, no scale. Any generated deck will default to the browser's default serif or whatever the upstream html-ppt master skill ships, which risks inconsistency.
- The 20+ zhangzara-* skills appropriately omit inline CSS font specs in their SKILL.md (font identity lives in the vendored example.html), which is architecturally correct — but the two Cormorant-bearing templates need their SKILL.md descriptions updated to name the replacement font so generators don't perpetuate the banned face.

**Color notes**
- CHEAP/OUTDATED — od-tpl-html-ppt-pitch-deck describes a 'white + blue→purple gradient hero' (description line 3 and example_prompt line 23). The blue-to-purple linear gradient is the most overused VC/SaaS deck motif of 2022-2024 and reads as generic AI-startup filler. Replace with a strong single-hue backdrop with a precise tonal accent, or a monochrome hero with one saturated typographic color pull.
- BORDERLINE — od-tpl-html-ppt-zhangzara-biennale-yellow specifies 'atmospheric sun-glow gradients' (description line 4, body blockquote line 34). This is intentional for the art-biennale context and the gradient is radial/atmospheric rather than a stock linear ramp — acceptable as a deliberate aesthetic choice, but should be documented as 'warm radial glow only, never linear' to prevent drift.
- STRONG PATTERN — deck-swiss-international's four locked accent colors (IKB #002FA7 / Lemon #FFD500 / Neon Green #C5E803 / Safety Orange #FF6B35) on neutral cream paper with strict no-shadow, no-gradient, no-blur rules is a premium, disciplined palette system. The explicit ink contrast rules (black text on Lemon/Neon, white+bold on Orange) show WCAG awareness. Worth promoting as a model for other deck skills.
- STRONG PATTERN — od-tpl-html-ppt-zhangzara-vellum's deep navy + warm-yellow italic serif + single dusty teal accent is a tightly controlled two-tone-plus-one system with clear hierarchy. No muddy secondary colors. Premium.
- STRONG PATTERN — od-tpl-html-ppt-zhangzara-cobalt-grid's electric cobalt italic serif on graph-paper canvas with stair-stepped pixel-glitch decoration is a single-accent system with strong restraint. Fits the 'one saturated accent only' discipline.
- od-tpl-html-ppt-hermes-cyber-terminal's mint-green #7ed3a4 on #0a0c10 black is a high-contrast, CRT-inspired pairing that works well for the terminal aesthetic. The amber/green/red three-tier tag system adds intentional semantic color without decorative noise — this is a premium pattern.
- od-tpl-html-ppt-graphify-dark-graph's '#06060c→#0e1020 深夜渐变 + 漂浮 blur orbs + 彩虹渐变标题' stacks three gradient effects simultaneously (background gradient + floating orbs + rainbow title). This is the 'too-many-accent / cheap futuristic' anti-pattern. Recommend: drop the rainbow headline gradient (use a single accent color for display type), keep the dark-to-slightly-lighter background and limit blur orbs to two or three positioned anchors.

**Good patterns to promote**
- deck-swiss-international's locked four-theme system (Klein Blue / Lemon / Neon Green / Safety Orange) with a single-accent-only discipline, no shadows/gradients/blur, and explicit WCAG-informed text-color rules per accent is a model palette architecture for any deck skill family.
- od-tpl-html-ppt-zhangzara-vellum and cobalt-grid demonstrate strict two-tone-plus-one systems: dominant dark/neutral canvas + one precise typographic accent + a single secondary utility color, nothing else.
- deck-swiss-international's type scale using extreme contrast (9.6vw display vs 14-16px body vs 11px uppercase label at 0.08em tracking) is a premium Swiss-editorial convention that should be normalized across more templates in this family.
- od-tpl-html-ppt-hermes-cyber-terminal's semantic three-tier tag color system (amber/green/red) gives functional color meaning without decorative excess — a pattern worth reusing in any data/dashboard deck template.
- The entire zhangzara-* family correctly keeps its type and color spec locked inside example.html rather than duplicating it in SKILL.md, which prevents drift between skill instructions and actual template behavior — this is architecturally sound.

---

### design-md-brands-A-L
- Decorative offenders: **0** · code/frontmatter correctly skipped: 54

**Typography notes**
- All 27 design-md-* skill files in scope (design-md-airbnb through design-md-lovable) are 18-line stub wrappers. They contain only YAML frontmatter (name + description) and a 4-step workflow referencing $designPath and $readmePath variables. No typography tokens, font families, type scales, weights, or tracking values are embedded anywhere in these files.
- The $designPath variable is expected to resolve at runtime to an external DESIGN.md not bundled in the skill folder. No DESIGN.md files were found inside any of the 27 scoped skill folders — they are absent, meaning no embedded type or color data to audit.

**Color notes**
- No color palettes, hex values, gradients, or CSS custom properties exist in any of the 27 scoped design-md-* SKILL.md files. All design content is deferred to external $designPath references that are not present in the skill folders.

**Good patterns to promote**
- The stub-wrapper pattern (SKILL.md points to $designPath) is a clean separation of concerns — the reference material is not duplicated into the skill itself. This avoids stale copy-paste of brand tokens inside Claude's skill corpus.

---

### design-md-brands-M-Z
- Decorative offenders: **0** · code/frontmatter correctly skipped: 34

**Typography notes**
- All 34 brand SKILL.md files in this slice (design-md-mastercard through design-md-zapier, plus design-md root) are pure thin wrappers: YAML frontmatter + a $designPath/$readmePath pointer + a 4-step prose workflow. Zero inline font families, type scales, weights, letter-spacing, or line-height values are present. Typography guidance lives in the external DESIGN.md files referenced at runtime via $designPath, which are not stored inside the skill folders.
- No banned defaults (Cormorant, Outfit, JetBrains Mono, Noto Kufi Arabic) appear anywhere in this slice — there is no font declaration of any kind to flag.
- Weak pattern to note: the workflow step 2 instructs the agent to 'Convert the style guide into concrete UI decisions: typography, colors, spacing, surfaces, layout, imagery, and motion' without providing a fallback type scale. This means if $designPath resolves to a missing or sparse file, the agent has no guardrails and may default to AI-slop font choices. Recommend adding a minimum fallback type scale (e.g. system-ui or Inter at 16/24/32/48px with weight 400/600) to the skill body.

**Color notes**
- No inline color values, palette definitions, gradient declarations, or dark/light mode tokens appear in any of the 34 SKILL.md files examined. Color specs live entirely in the external $designPath files.
- The instruction 'Apply the style to the user's product context without copying proprietary content verbatim' is the only color-adjacent guidance. This leaves a gap: if the runtime DESIGN.md is absent, the agent has no fallback palette and may produce random-gradient or low-contrast output. Recommend a fallback one-accent neutral palette note (e.g. white/near-black + one brand accent).
- No muddy, cheap, or low-contrast patterns are present in the skill files themselves — there is simply nothing to evaluate at this layer.

**Good patterns to promote**
- Consistent minimal wrapper pattern across all 34 brand skills: identical 4-step workflow, no hardcoded tokens that would go stale when a brand updates. This is architecturally correct — the skill is a pointer, not a copy.
- The $designPath/$readmePath variable pattern defers all brand-specific content to the external DESIGN.md, avoiding duplication and keeping the skill body brand-agnostic and update-proof.
- Step 4 ('keep the implementation aligned with the host app's framework and existing components') is a good surgical-change guardrail that prevents the skill from overwriting existing code conventions with brand tokens.

---

### awesome-design-md-local + awesome-design-md + design-md-airbnb + design-md-airtable
- Decorative offenders: **0** · code/frontmatter correctly skipped: 34

**Typography notes**
- The corpus teaches well-specified, brand-faithful type systems. Every DESIGN.md defines a named token scale (display-xl → caption → micro-label) with explicit px, weight, lineHeight, and letterSpacing values — this is a strong pattern worth promoting.
- Dominant brand-custom font strategy: Airbnb Cereal VF, CursorGothic, Haas Grotesk, BinanceNova, CoinbaseDisplay, IBM Plex Sans (Sanity/together.ai), Universal Sans (x.ai) — all contextually appropriate and non-generic.
- JetBrains Mono appears across many DESIGN.md files (Cursor, Composio, Claude, cal.com, Coinbase, Binance, Bugatti, together.ai) — but exclusively as the designated code-block / monospace face for brands whose product involves code or technical output. This is contextually correct usage, not the banned 'lazy default' pattern. No violation.
- Cormorant Garamond appears in two places (claude/DESIGN.md line 394, bugatti/DESIGN.md line 290) only as a documented fallback substitute for licensed proprietary serif faces (Copernicus and Bugatti Text Regular respectively). It is never specified as a primary design voice. No violation.
- Outfit is absent from the entire corpus. No violation.
- Noto Kufi Arabic is absent from the entire corpus. No violation.
- Weak pattern flagged: Airbnb 'uppercase-tag' at 8px / 700 / 0.32px tracking is borderline — 8px rendered uppercase text risks illegibility at standard screen densities. The corpus documents it accurately but implementers should treat it as a brand-quirk exception, not a reusable pattern.
- BMW and Lamborghini UPPERCASE-as-default-display is correctly flagged in their respective files as brand-specific (Lamborghini 'ALL-CAPS is the default voice'). This is descriptive accuracy, not a prescriptive recommendation to adopt wholesale.
- The Verge DESIGN.md documents 1.5–1.9px letter-spacing on ALL-CAPS mono labels — a valid editorial-news voice but noisy if cargo-culted. The corpus correctly isolates it to The Verge's signed-off token set.
- Strong pattern: negative letter-spacing on large display (Cursor -2.16px at 72px, Airtable display-xl 48px at 0 letterSpacing, Apple SF Pro with negative tracking) — magazine-editorial register, not tech-bombastic. Worth promoting as the premium-display default.

**Color notes**
- Single-accent-voltage pattern is the dominant premium convention across the corpus: Airbnb Rausch (#ff385c), Cursor Orange (#f54e00), ClickHouse Yellow (#facc15-adjacent), Coinbase Blue, Hashicorp Violet-per-product. One brand color does all interactive work; UI chrome is monochrome. This is the correct premium pattern.
- Dark-canvas brands (Bugatti #0d0d0d, BMW-M pure black, SpaceX black) all prohibit gradient backdrops explicitly — depth from photography only. This is premium; the corpus documents it correctly and should be reinforced in any derived skill output.
- Light-canvas brands (Airtable white, Airbnb white, Apple white, Intercom cream) also prohibit atmospheric gradients ('no gradient, no aurora, no mesh behind the type' — Airtable DESIGN.md line 503). The corpus consistently warns against the SaaS-template mesh/aurora cliché.
- Binance documents a legitimate situational gradient (yellow→dark for the Futures Arena launch hero, DESIGN.md line 465/565) while explicitly prohibiting atmospheric gradients elsewhere. This is a good pattern: named one-off gradient token scoped to a single surface, not generalized.
- Composio documents a radial spotlight glow (`{colors.primary-glow}`) for hero backdrops — a moderate-risk pattern. Acceptable when isolated to hero only, but corpus correctly warns against generalizing.
- Expo uses a sky-blue gradient wash (`#cfe7ff → #a8c8e8`) limited to the homepage hero device-mockup backdrop only — correctly scoped, low risk.
- Cursor's pastel AI-timeline palette (peach/mint/blue/lavender/gold) is correctly scoped to in-product timeline visualizations only, not generalized UI accents. This is exemplary token isolation.
- No muddy, random-gradient, or too-many-accent patterns found in the documented token sets. The corpus is notably disciplined about accent count — only one or two accent hues per brand.
- Clay's cream canvas (#fffaf0) with 3D claymation illustrations is a distinctive outlier from the otherwise monochrome-or-white baseline. Correctly documented as brand-specific; not a generalizable default.
- Premium pattern worth promoting: near-black warm ink (Cursor #26251e, Airtable #181d26, Airbnb #222222) rather than pure #000000 black — softer contrast with warm undertone reads as editorial rather than developer-stark.

**Good patterns to promote**
- Single named brand-voltage accent + monochrome UI chrome: every premium brand in the corpus follows this (Airbnb Rausch, Cursor Orange, ClickHouse Yellow, Coinbase Blue). Promotes as the default pattern for any new brand system.
- Negative letter-spacing at large display sizes (-2.16px at 72px, -0.44px at 22px) for magazine-editorial voice instead of neutral or positive tracking — confirmed across Cursor, Airtable, Apple, Airbnb.
- Token-isolated gradient: one named gradient token scoped to a single hero surface (Binance arena-hero-gradient), explicitly prohibited elsewhere. Better than either 'no gradients ever' or 'gradients everywhere'.
- Warm near-black ink (#181d26–#26251e) instead of pure black — softer, more editorial, less developer-stark. Consistent across Airtable, Cursor, Airbnb.
- JetBrains Mono correctly scoped to code/terminal surfaces only within technical-product brands — not used as a decorative display or body font. Correct contextual monospace use.
- Whitespace as the primary atmospheric tool on light-canvas brands (Airtable 96px section padding, Apple tile-per-viewport density, Airbnb generous padding) — documented explicitly as the anti-template differentiator.
- Brand-custom variable font (Airbnb Cereal VF) with a full named fallback stack including system-ui — correct progressive-enhancement typography.
- Full token scale with explicit px/weight/lineHeight/letterSpacing per role (not vague 'large/medium/small') — the DESIGN.md schema is a premium specification pattern.

---

### karim-web-build-skills
- Decorative offenders: **1** · code/frontmatter correctly skipped: 14

**Typography notes**
- 3d-animation-web-designer/SKILL.md lines 85-87: Typography table recommends `Outfit` (banned default) and `Space Grotesk` (explicitly flagged as 'convergent common choice' in frontend-design/SKILL.md) for body copy, and `JetBrains Mono` (banned) for mono/technical labels. `Noto Kufi Arabic` is recommended for Arabic text — also banned as a lazy default. Replace body recommendations with a rotation pool: `Editorial New`, `PP Neue Montreal`, `Aktiv Grotesk`, `Syne`, `Lausanne`; replace JetBrains Mono with `IBM Plex Mono` or `Fira Code`; replace Noto Kufi Arabic with `IBM Plex Arabic`, `Almarai`, or `Tajawal`.
- papaya-smoke-hero/SKILL.md line 50: Recommends `JetBrains Mono` for HUD/telemetry mono labels (banned default). `IBM Plex Mono` is the correct substitute — it has tabular figures and a technical-broadcast feel without the banned default stigma.
- frontend-design/SKILL.md line 36: Correctly calls out Inter, Roboto, Arial, Space Grotesk as banned convergent defaults — good anti-slop rule, should be cross-referenced in 3d-animation-web-designer's typography table.
- hyliox-landing/SKILL.md: Placeholder-driven font system (FONT_DISPLAY / FONT_BODY) is excellent — forces per-project choice rather than baking in a default. Premium pattern worth replicating.
- papaya-smoke-hero/SKILL.md line 48: `Druk Wide Bold` as display with `Arial Black` fallback is appropriate for the racing aesthetic; not a lazy default — context-specific and intentional. Good pattern.
- 3d-animation-web-designer/SKILL.md line 80-87: Typography table bakes in `Playfair Display`, `Anton`, `Bebas Neue`, `Oswald` as the display pool — this is reasonable variety but Playfair Display edges toward the Cormorant luxury-default territory for dark sites. Recommend swapping Playfair for `Canela`, `Domaine Display`, or `GT Super`.

**Color notes**
- landing-page-generator/SKILL.md line 65: The 'Dark SaaS' design style hardcodes `violet-500/400` accent on `bg-gray-950` — this is exactly the cliched 'purple gradient on dark background' pattern called out as banned in frontend-design/SKILL.md. The landing-page-generator skill is teaching the pattern it should prohibit. Replace with a single-hue, high-contrast alternative (electric cyan `#00D2FF`, warm amber `#F59E0B`, or cobalt `#2563EB`) or make the accent a placeholder the user fills.
- 3d-animation-web-designer/SKILL.md lines 37-76: Three named palettes (Gold & Midnight, Lime & Obsidian, Teal & Navy) are well-structured — each has a clear role (bg, card, accent, dim) and dark-luxury application. Gold `#D4A853` + Obsidian `#050508` is a premium combination. No muddy choices; gradients are minimal (single-direction linear used only for progress bars). Good pattern.
- 3d-animation-web-designer/SKILL.md: Palette A includes both `--gold` and `--cyan` (`#4ECDC4`) as accent colors — two warm/cool accents active simultaneously can create muddy competition on dark backgrounds. Prefer a primary accent + a single semantic-only secondary (e.g., only use cyan for hover or interactive states).
- papaya-smoke-hero/SKILL.md lines 36-44: Papaya `#FF8000` + Lando cyan `#47C7FC` two-accent system is intentional and context-specific (F1 livery), not random. Clean ink/carbon/graphite base means the accents pop without fighting. Premium contextual pattern.
- landing-page-generator/SKILL.md: 'Bold Startup' and 'Clean Minimal' both use white/gray-50 backgrounds without any depth tokens (no subtle texture, no layered surface). For award-tier builds this reads flat. Recommend noting that these are conversion-rate-first templates, not premium cinematic — or adding optional surface depth layer.

**Good patterns to promote**
- hyliox-landing/SKILL.md: Placeholder-driven palette and font system (HSL triplets + Google Fonts family names as named slots) forces per-project decision rather than baking defaults. Prevents convergent aesthetic drift.
- frontend-design/SKILL.md: Explicit ban on Inter, Roboto, Arial, Space Grotesk convergence, with 'vary between light and dark themes, different fonts, different aesthetics' as a runtime rule. Anti-slop guardrail at invocation time.
- papaya-smoke-hero/SKILL.md: Context-specific typography — Druk Wide Bold + JetBrains Mono is justified by the F1/racing brief. The skill correctly scopes the mono choice to HUD microcopy (telemetry counters, sector labels) not general body text.
- 3d-animation-web-designer/SKILL.md: Palette-per-project selection rule ('Choose ONE palette per project') and named battle-tested palettes prevent the too-many-accents anti-pattern at the design system level.
- 3d-animation-web-designer/SKILL.md: CSS custom-property token system for all color roles (--bg, --bg-card, --gold, --text, --glass, --glass-border) is correct single-source-of-truth architecture. Means palette swaps require one block change.
- awwwards-winner-playbook/SKILL.md: Explicitly names the 'motion is only 20%' rule and routes Design (40%) + Usability (30%) to non-motion specialist skills. Prevents the common trap of over-investing in GSAP/WebGL at the cost of typography and IA craft.
- premium-motion-cookbook/SKILL.md: All `//` occurrences are real JavaScript inline code comments inside code fences — correctly structured, no decorative symbol use.

---

### color-skills
- Decorative offenders: **0** · code/frontmatter correctly skipped: 33

**Typography notes**
- brand/references/typography-specifications.md hardcodes JetBrains Mono as the monospace default (both --font-mono CSS variable and Tailwind config). This is a banned default per Karim's rules. Replace with a less opinionated choice such as 'Fira Code', 'Cascadia Code', 'Geist Mono', or context-appropriate system-ui monospace fallback.
- brand/references/typography-specifications.md sets both --font-heading and --font-body to Inter — a single-font-for-everything approach that produces flat hierarchy in practice. The 'Common Font Pairings' section lists alternatives (Playfair+Source Sans, Poppins+Open Sans, Merriweather+Lato) but the default CSS variables override them. The default should be more opinionated or the pairings should be elevated to primary recommendations rather than footnotes.
- brand/references/typography-specifications.md All-caps letter-spacing is prescribed at 0.05em, small-caps at 0.1em — these are reasonable. However body tracking is 0 with no mention of negative tracking on large display text beyond Display's -0.02em. Missing guidance on fluid type / clamp() for responsive scale.
- dark-mode-design/SKILL.md and theming-system/SKILL.md contain no font guidance at all — color-only skills by design, which is acceptable, but means a consumer of these skills gets zero type-in-dark-mode direction (e.g., switching to lighter weights in dark mode, or avoiding ultra-thin weights on OLED).
- brandkit/SKILL.md uses 'very sparse typography' and 'minimal text' as the standard — appropriate for image generation prompts, not a typography spec. No font families named. This is intentional (image generation context) but should not be read as a typography system.

**Color notes**
- brand/references/color-palette-management.md default CSS variables use #2563EB (primary blue) paired with #8B5CF6 (secondary purple) — this blue+purple combination is the single most overused SaaS color pairing in 2024-2026 and should be flagged as a lazy/generic default. The 'Tech/SaaS' example palette in that file doubles down on exactly this combo. A premium system should start from brand-specific hue decisions, not Tailwind's blue-600+violet-500.
- brand/references/color-palette-management.md semantic palette uses hardcoded hex values (#22C55E success, #F59E0B warning, #EF4444 error, #3B82F6 info) rather than semantic token references. These are directly Tailwind's default colors and will cause a generic feel. Preferred approach: derive semantic colors from the brand's own hue, or at minimum reference them as token aliases not raw hex.
- dark-mode-design/SKILL.md recommends #121212 as the base dark background — this is Material Design's legacy value from 2018. Preferred 2025 standard is OKLCH-based dark surfaces (e.g., oklch(12% 0 0)) for perceptual consistency, or at minimum a cooler near-black that harmonizes with the brand hue (e.g., #0D0D10 for blue-tinted products). The file gives no guidance on hue in dark surfaces.
- dark-mode-design/SKILL.md suggests off-white #E0E0E0 for text — neutral gray-white is fine but the file gives no guidance on whether to tint the off-white toward the brand hue for warmth/coolness. Missing: hue-tinted white strategy.
- brandkit/SKILL.md COLOR DISCIPLINE section is genuinely strong: single dominant palette, accent repeating across panels, explicit ban on random rainbow and generic purple-blue AI glow. Named palette examples (black+cyan+muted coral, forest green+lime+fog gray, etc.) are intentional and non-generic. Worth promoting into the color law.
- brandkit/SKILL.md explicitly calls out 'no generic purple-blue AI glow unless appropriate' — this is a premium rule worth adopting globally. Surfaces the exact problem that color-palette-management.md causes by defaulting to blue+purple.
- color-system/SKILL.md teaches correct layered palette structure (brand + neutral + semantic + extended) and mandates tonal scales rather than single swatches. This is architecturally sound. However it gives no guidance on color space — OKLCH/OKLAB vs HSL vs hex. Given that color-expert references OKLCH/OKLAB extensively, color-system should align to OKLCH-first generation.
- theming-system/SKILL.md three-layer token model (global → semantic → component) is textbook correct and worth keeping. No color-specific palette values named, which is appropriate for an architecture skill.
- critique-brand-consistency/SKILL.md is purely procedural (compare screen against tokens.md, mood.md, voice.md) — no palette values. Architecturally sound; no color anti-patterns.

**Good patterns to promote**
- brandkit/SKILL.md COLOR DISCIPLINE: enforces one dominant palette + repeating accent across panels + explicit ban on random rainbow and generic purple-blue AI glow. Concrete named palette examples (black+cyan+muted coral, forest green+lime+fog gray, navy+white+steel, ivory+deep blue+red+gold) show restraint over decoration.
- color-system/SKILL.md: mandates full tonal scales (50–950) rather than single swatches, requires testing every foreground/background pair for contrast, and specifies dark mode mappings from the start — not as an afterthought.
- theming-system/SKILL.md three-layer token architecture (global raw palette → semantic aliases → component tokens) is sound and promotes predictable theme overrides without hardcoding.
- critique-brand-consistency/SKILL.md pattern of comparing against mood.md + voice.md + tokens.md as three separate reference files is a strong audit framework — flags hardcoded drift from tokens as a 'common failure pattern' explicitly.
- brandkit/SKILL.md board composition rhythm (quiet → functional → emotional → technical → atmospheric → detailed) as a sequencing principle for brand presentations is a premium structural insight transferable to any multi-panel design output.
- dark-mode-design/SKILL.md elevation through lighter surfaces (not shadows) for dark mode is the correct 2024+ approach (aligns with Material You and Apple HIG dark mode). Worth codifying as a hard rule.

---

### typography-skills
- Decorative offenders: **0** · code/frontmatter correctly skipped: 14

**Typography notes**
- typography-scale/SKILL.md defines a clean modular scale (12/14/16/20/24/32/40/48-64px) with correct line-height tiers: tight 1.2 for headings, normal 1.5 for body, relaxed 1.75 for long-form. This matches best practice and should be treated as the canonical numeric ladder.
- Letter-spacing guidance in typography-scale is correct directionally (−0.02em large headings, 0 body, +0.05em uppercase labels) but the +0.05em value for uppercase labels/captions is on the noisy side — premium practice caps tracked uppercase at +0.04em max. Flag as a minor weak pattern.
- critique-typography/SKILL.md enforces ≥1.25× ratio between scale steps, WCAG AA contrast (4.5:1 body / 3:1 large), line-height 1.1–1.3 headings / 1.4–1.6 body, and 45–75 char measure — all correct and worth encoding in any type law.
- readable-measure/SKILL.md correctly specifies 45–75 char optimal measure (66 ideal), recommends max-width: 65ch, and differentiates sustained reading (55–70) from UI copy (45–65). No weaknesses — this is reference-grade.
- font-resources/SKILL.md explicitly bans Cormorant, Outfit, JetBrains Mono, and Noto Kufi Arabic as lazy defaults, and links to the variation pool rule. This is the only skill in the set that enforces the ban — typography-scale, font-pairing-local, font-selection-local, google-fonts-local, and variable-fonts-local are SILENT on the ban, creating a gap where those skills could recommend banned faces.
- font-selection-local and font-pairing-local delegate font knowledge to local reference files (awesome-fonts.md, google-fonts-family-index.md) rather than embedding opinionated pairings — efficient but produces no teachable convention. Neither skill names a single concrete typeface recommendation or pairing example, making them pure routers with no design judgment of their own.
- google-fonts-family-lookup and google-fonts-local are metadata/path lookup tools only — they contain no pairing guidance, no banned-defaults enforcement, and no discussion of rendering quality or print-screen suitability. Useful for slug resolution; not a typography authority.
- variable-fonts-local correctly recommends using standard CSS properties (font-weight, font-stretch, font-optical-sizing) before dropping to font-variation-settings, and warns to keep axis ranges restrained. This is good practice. No weaknesses.
- webfont-implementation-local recommends font-display: swap and preloading only critical above-the-fold files — both correct. The skill does not mention size-adjust / ascent-override / descent-override for fallback metric matching, which is an emerging best practice gap when precise CLS control matters.
- No skill in the set covers optical sizing (opsz axis), fluid type with clamp(), or CSS custom property–driven type tokens beyond a brief mention in critique-typography. These are gaps for a production-grade type law.

**Color notes**
- The typography-skill cluster contains no color palette definitions and no gradient specifications — all color guidance in this slice is confined to critique-typography's single WCAG AA contrast check (4.5:1 body, 3:1 large). No offenders and no premium patterns to flag here; color is intentionally out of scope for this skill set.
- critique-typography correctly flags contrast ratio as a readability dimension rather than an aesthetic one — this is the right framing. The skill does not prescribe a palette, which avoids introducing muddy or cheap defaults.

**Good patterns to promote**
- critique-typography's four-dimension audit structure (Scale Usage / Readability / Consistency / Token Compliance) with pass/minor/major ratings is a premium, reusable framework — promote this pattern into the type law as the default audit checklist.
- font-resources is the only skill that encodes the banned-defaults rule with an explicit list (Cormorant / Outfit / JetBrains Mono / Noto Kufi Arabic). This ban-check-before-writing-CSS discipline should be injected into every other font-related skill as a cross-reference or embedded rule.
- typography-scale's clear separation of size, weight, line-height, and letter-spacing into distinct subsections with numeric values is the right scaffolding for a token-based type system — other skills should reference this as the source of numeric tokens rather than inventing their own.
- readable-measure's context-differentiated measure table (long-form 55–70 / UI copy 45–65 / captions 40–60 / pull-quotes 30–45) is a concrete, actionable reference that most competitors omit. Worth preserving verbatim in any type law.
- font-resources correctly recommends @fontsource npm over Google Fonts CDN for performance (self-hosted, tree-shaken, no FOIT, better Core Web Vitals) and explicitly forbids cloning the multi-GB google/fonts repo. This is a net-positive DX/performance pattern to promote as the default.

---

### refactor-ui-pack
- Decorative offenders: **0** · code/frontmatter correctly skipped: 47

**Typography notes**
- Scale defined in refactor-ui-02: Hero 48-60px/700/lh1.1, H1 36-40px/700/lh1.2, H2 28-32px/600/lh1.3, Body 16-18px/400/lh1.6, Small 14px/400/lh1.6, Caption 12px/400/lh1.5 — solid, production-safe range.
- No specific font families are prescribed or recommended anywhere in the pack. This is a deliberate abstraction (brand-agnostic principles), which is appropriate for a principles library but means the pack cannot enforce the banned-fonts rule (Cormorant/Outfit/JetBrains Mono/Noto Kufi Arabic) — a consumer could still pick them without any guard here.
- Two-weight rule enforced: 400/500 for normal, 600/700 for bold. Weights below 400 explicitly banned ('Never < 400 for UI'). Strong pattern.
- Line-height is treated as inversely proportional to font size: small text (12-14px) gets 1.6-1.7, body 1.5-1.6, large headlines 1.0-1.2. This is correct and premium.
- em units explicitly banned in favour of px or rem — good guard against compounding nesting bugs.
- Minimum 25% jump between scale steps enforced. Example given: 16px→20px pass, 16px→18px fail. Strong.
- Line length constrained to 45-75 characters / 20-35em max-width for paragraphs — correct readability target.
- The scale is described as 'hand-crafted, not mathematical' to avoid fractional-pixel artefacts from modular ratios (1.25×, 1.333×). This is a premium pattern — matches Refactoring UI book exactly.
- No ALL-CAPS tracking / letter-spacing rules defined. The pack is silent on decorative tracking and eyebrow labels — a gap that leaves a consumer free to add noisy uppercase-tracking headings without any push-back from these skills.
- No variable-font or optical-size guidance. Minor omission for a principles pack but worth noting.

**Color notes**
- Color structure in refactor-ui-03: 8-10 greys + 5-10 primary shades + 5-10 accent shades each (red/yellow-amber/green/teal-pink-purple). This is a rigorous, well-structured multi-step palette approach — premium pattern.
- Example grey ramp (10 steps) uses Tailwind-adjacent hex values: #F9FAFB through #111827. These are warm-neutral greys, not cool blue-greys, which avoids the cheap blue-grey UI cliché.
- Explicit rule against rgba() opacity shortcuts — all shades must be defined as explicit hex. This prevents the common AI-slop pattern of generating 20 colour variants from 5 tokens via alpha stacking.
- True black (#000000) flagged as FAIL; #111827 or #1F2937 recommended as near-black for body text — eliminates the harsh contrast artefact.
- Accent palette organises meaning: red=destructive/error, yellow-amber=new-feature/caution, green=success/positive, teal/pink/purple=categorisation. Semantic colour assignment is precise.
- HSL-based shade generation method documented (lightness 10-98% across 5-10 stops per hue). Prevents perceptually uneven ramps that HSB-based tools produce.
- No gradient guidance at all. The pack is gradient-silent, which is appropriate — gradients are treated as decoration (see refactor-ui-06 which explicitly flags 'decorative gradients without purpose' as FAIL). Premium restraint.
- No dark-mode palette covered. This is a gap: the grey ramp given is light-mode only. A consumer building a dark UI has no guidance from these skills and could produce an inverted grey ramp that breaks contrast hierarchy.
- refactor-ui-09 provides a contrast reference table: #000000=21:1, #333333=12.6:1, #999999 flagged as too light for body text, #666 given as minimum for secondary. All WCAG AA aligned.
- No oklch or P3 wide-gamut guidance. Minor omission; the pack predates widespread oklch adoption so not a defect, but worth noting for upgrade path.

**Good patterns to promote**
- Inverse line-height proportionality rule (lh1.1 for heroes, lh1.6 for body, lh1.5 for captions) — cite this in the law as the canonical line-height heuristic.
- Two-weight-only discipline (400/500 body, 600/700 bold) prevents the five-weight bloat pattern common in AI-generated UIs.
- rgba()-ban / explicit hex shades rule — strong guard against AI-slop colour drift; promote to a global colour law.
- Semantic colour mapping (red=destructive, amber=caution/new-feature, green=success) with explicit 5-10-shade depth per accent — solid foundation for any token system.
- Minimum 25% type-scale jump rule — directly eliminates the 'micro-step' anti-pattern (16/18/20px) that makes AI-generated type look flat.
- Shadow elevation semantics: refactor-ui-08 defines none/subtle/medium/large/xl shadow tiers keyed to functional elevation (card vs modal vs sticky header), not to aesthetics. This is the right mental model for a shadow token system.
- Whitespace-over-borders principle (refactor-ui-06): prefer margin/padding to create visual groups; only add a border if whitespace alone is insufficient. Eliminates 'border-itis' and 'boxy UI' at the principle level.
- Grey dominance rule: 'the majority of your UI is grey' — teaches consumers to reach for grey-scale tokens first and reserve brand colour for intentional emphasis.

---

### taste-packs
- Decorative offenders: **2** · code/frontmatter correctly skipped: 12

**Typography notes**
- brutalist-skill/SKILL.md line 37: JetBrains Mono listed as the first micro-typography recommendation (before IBM Plex Mono, Space Mono). JetBrains Mono is on Karim's banned-default list. Swap first-listed pick to IBM Plex Mono or Space Mono; keep JetBrains Mono as a late fallback only.
- gpt-tasteskill/SKILL.md line 17: Outfit appears in the random typography pool alongside Satoshi, Cabinet Grotesk, Geist. Outfit is banned. Replace with Plus Jakarta Sans or Switzer in that slot — both have comparable geometric friendliness without the banned-font stigma.
- minimalist-skill/SKILL.md line 28: JetBrains Mono listed first in the monospace stack ('Geist Mono', 'SF Mono', 'JetBrains Mono'). Flip order: Geist Mono already leads, but the explicit call-out of JetBrains Mono as a named option is the risk. Swap to Berkeley Mono or Commit Mono as the third fallback.
- redesign-skill/SKILL.md line 22: Outfit recommended as a direct Inter replacement ('Replace with a font that has character. Good options: Geist, Outfit, Cabinet Grotesk, Satoshi'). Outfit is banned. Replace the mention with Switzer or DM Sans.
- soft-skill/SKILL.md (high-end-visual-design): Font bans are correctly stated (Inter, Roboto, Arial, Open Sans, Helvetica). Premium alternatives named (Geist, Clash Display, PP Editorial New, Plus Jakarta Sans) are all strong and unbanned — good pattern to promote.
- gpt-tasteskill: 'NEVER Inter' rule is correctly enforced. The 2-to-3 line H1 cap with clamp(3rem, 5vw, 5.5rem) is a strong mechanical constraint worth promoting.
- minimalist-skill: Lyon Text and Instrument Serif for editorial headings, tight -0.02em to -0.04em tracking, 1.1 line-height — these are premium editorial conventions worth promoting system-wide.
- imagegen-frontend-web: Compressed statement typography (Monument-like) and editorial serif + sans pairing listed as named options. Neither is banned and both are sound choices for premium web direction.
- image-to-code-skill: No explicit font names prescribed — good hygiene. The combinatorial engine uses 'clean grotesk / refined grotesk / expressive display / compressed statement / editorial serif + sans / Swiss rational' — all style categories, not named fonts, which avoids the banned-font risk entirely.
- ALL skills: Uppercase tracking abuse risk. brutalist-skill mandates ALL-CAPS for both macro and micro-type ('Exclusively uppercase'). This is intentional for the aesthetic but should be scoped — the pattern leaks into non-brutalist outputs if this skill is invoked without a project guard. Add an explicit scope note: uppercase-only applies to the brutalist/tactical telemetry aesthetic only.

**Color notes**
- soft-skill/SKILL.md (high-end-visual-design) Archetype 1 'Ethereal Glass': prescribes 'subtle glowing purple/emerald orbs' on OLED black. Purple/AI-glow is the most common AI fingerprint — its own sibling (redesign-skill) explicitly bans the 'purple/blue AI gradient aesthetic'. The Ethereal Glass archetype should replace 'purple/emerald orbs' with 'ink-to-graphite radial depth' or 'cool zinc vignette' to avoid the pattern.
- brutalist-skill: single-accent-only constraint is a premium pattern. One red (#E61919 / #FF2A2A) with zero tolerance for a second accent is editorial discipline. Promote this 'one accent maximum' rule to all taste-pack skill outputs.
- minimalist-skill: muted pastel semantic system (Pale Red #FDEBEC / Pale Blue #E1F3FE / Pale Green #EDF3EC / Pale Yellow #FBF3DB) with explicit paired foreground values is the best color system in this family. The desaturated pastel-on-white pair ratios imply safe WCAG AA contrast. Promote as a reference implementation.
- imagegen-frontend-web §13: Gradient Discipline section is premium. Distinguishes 'allowed tonal gradients' (palette-matched, low chroma, single-hue atmospheric) from 'banned AI slop gradients' (rainbow mesh, purple-to-blue, pink-to-orange, neon edges, gradient text). This explicit whitelist/blacklist model should be adopted by all taste-pack skills that currently have vague anti-gradient rules.
- gpt-tasteskill: No explicit color system defined — relies on 'creative backgrounds: deep radial blurs, grainy mesh gradients, shifting dark overlays'. This is vague and risks defaulting to purple/blue AI-glow. Needs a Palette Discipline block matching imagegen-frontend-web §13.
- imagegen-frontend-mobile §23: Color Palette Rule correctly bans 'default purple-blue AI palettes', 'random bright rainbow color use', 'accidental or chaotic combinations'. Palette logic options (restrained monochrome + one accent; warm neutral + sharp dark; cool mineral + highlight accent) are all premium and non-generic. Good reference.
- redesign-skill: Correctly bans oversaturated accents (below 80% saturation), mixing warm and cool grays, and the purple/blue AI gradient. The 'tint shadows to match background hue' rule is a premium pattern not present in other skills — worth promoting.

**Good patterns to promote**
- brutalist-skill: 'Choose ONE substrate palette per project and commit. NEVER mix light and dark substrates within the same interface.' — this single-mode rule eliminates the random dark-section-in-light-page anti-pattern caught by redesign-skill.
- minimalist-skill: Muted semantic pastel system with explicit paired foreground hex values. Each pastel background has a corresponding muted text color (e.g. #FDEBEC bg / #9F2F2D text) — a ready-made accessible color chip set.
- soft-skill (high-end-visual-design): Double-Bezel / Doppelrand nested architecture (outer shell + inner core with concentric border-radius math: rounded-[calc(2rem-0.375rem)]) is a premium haptic component pattern not present in any other skill.
- soft-skill: 'Button-in-Button trailing icon' architecture — nested icon in its own w-8 h-8 rounded-full container flush with the button — gives internal kinetic tension on hover. Highly specific and premium.
- imagegen-frontend-web §2: Combinatorial Variation Engine with Python-RNG simulation to force layout diversity. Prevents repeated left-text/right-image hero defaults by requiring a different Composition Anchor each section.
- imagegen-frontend-web §13: Gradient whitelist/blacklist. Explicit allowed list (low-chroma palette-matched tonal gradients, single-hue atmospheric grades, soft radial vignettes, noise-textured gradients, editorial color washes) alongside an explicit banned list (rainbow mesh, purple-to-blue, pink-to-orange, neon halos, gradient text).
- redesign-skill: 'Tint shadows to match background hue rather than using pure black at low opacity.' Specific, actionable, and produces more premium depth than generic rgba(0,0,0,0.1) shadows.
- gpt-tasteskill: '2-to-3 line H1 iron rule' enforced via max-width container class (max-w-5xl or max-w-6xl) and clamp() type sizing. Structural constraint rather than a stylistic preference — prevents the 6-line-wrap heading AI slop pattern mechanically.
- minimalist-skill: scroll-entry animation spec: translateY(12px) + opacity:0 over 600ms with cubic-bezier(0.16,1,0.3,1) via IntersectionObserver — not window.addEventListener('scroll'). Correct GPU-safe, mobile-performant animation pattern.
- image-to-code-skill §12: Combinatorial Variation Engine defined as style-category picks (not named fonts), eliminating banned-font risk while still enforcing taste variance.

---

### core-design-system-skills
- Decorative offenders: **0** · code/frontmatter correctly skipped: 47

**Typography notes**
- ui-ux-pro-max/data/typography.csv (row 4): Cormorant Garamond + Libre Baskerville listed as pairing #4 'Editorial Classic'. This is the banned-default serif duo. It appears contextually labeled as 'publishing/blogs' only — acceptable as a named niche option in a searchable palette, but the label must never become the lazy auto-pick for any 'luxury' or 'premium' brief.
- ui-ux-pro-max/data/design.csv line 32: Outfit used as the font family for a Bauhaus-style brutalist template. Outfit is on the banned-default list (feedback_default_fonts_ban). This is an embedded example in the CSV data corpus — when this record is served as a design recommendation, it will push Outfit into production. Flag for replacement with a more distinctive geometric alternative (e.g. DM Sans, Barlow Condensed, or ABC Favorit).
- ui-ux-pro-max/data/design.csv lines 196, 347, 524, 560, 576, 1318, 1320: JetBrains Mono appears in 7 distinct design templates as the go-to monospace for labels, stats, tags, and 'MENU' text. JetBrains Mono is banned as a lazy default. Some uses are contextually appropriate (developer tools, cyberpunk wallet) but it appears in generic contexts (Coinbase-style fintech line 576, sports/event line 560) where it signals 'AI picked the obvious mono' rather than a deliberate choice. Recommended alternatives: Space Mono (more character), Geist Mono (clean, modern), Berkeley Mono (premium, distinctive), Fira Code for code-specific contexts.
- ui-ux-pro-max/data/design.csv lines 1194-1203: Cormorant Garamond used as heading font for a 'Philosophical/Academia' themed template, paired with Crimson Pro body and Cinzel labels. Cormorant Garamond is on the banned-default list. The academic context might justify a high-contrast serif, but Cormorant in particular is overused as the 'luxury serif autopick'. Alternatives: Freight Display, Canela, Domaine Display, or EB Garamond.
- ui-ux-pro-max/data/design.csv line 1319: letterSpacing: 4 on H1 (font-size 42, weight 900, uppercase) in the cyberpunk/tech template. At 4px tracking on a 42px uppercase heading, this is extremely wide — approaching decorative-only territory. Max recommended tracking for display all-caps is 0.08em (~3.3px at 42px); 4px is 0.095em, which starts to break word rhythm. Flag as a noisy-tracking anti-pattern for weight 900 fonts.
- ui-ux-pro-max/data/design.csv line 1122 and line 1421: letterSpacing 1.5 on uppercase labels (Inter-Bold and accent-colored text) appears in two separate templates. At small sizes (12pt) 1.5px letter-spacing on uppercase is within acceptable range (~0.1em); at body size it becomes noisy. The pattern itself is acceptable IF applied only to uppercase micro-labels — the risk is it bleeds into general body text via copy-paste.
- ui-ux-pro-max/SKILL.md rule table line 59: Typography rule states 'Base 16px, Line-height 1.5' — this is correct and well-specified. Positive pattern worth keeping.
- ui-ux-pro-max/data/typography.csv: 57 pairings with clear mood/use-case tagging, Google Fonts URLs, Tailwind config snippets, and notes. Strong pattern: pairings are contextually labeled (e.g. 'Pixel Retro', 'Korean Modern', 'Developer Mono') which prevents the banned fonts from becoming defaults — they only appear under explicit context matches. This is the right architecture.
- ui-design-system/SKILL.md: Does not specify fonts. It instructs the AI to generate font tokens from a brand color + style preference input, which is the correct token-first approach. No font default risk here.
- design-token/SKILL.md: No font families specified. Correct — purely structural token taxonomy.

**Color notes**
- ui-ux-pro-max/data/design.csv lines 1309-1317 (cyberpunk/Web3 template): triple neon accent palette — Matrix Green #00ff88, Neon Magenta #ff00ff, Cyber Cyan #00d4ff on near-black #0a0a0f. Three distinct saturated accent colors with no clear hierarchy. This is a too-many-accents pattern. The design itself is genre-correct (cyberpunk) but when served as a recommendation it can bleed into products that don't need the full neon triad. The record is correctly labeled 'cyberpunk/gaming/web3' — acceptable as a niche entry, but the generator should not surface it for generic 'dark mode' queries.
- ui-ux-pro-max/data/design.csv lines 1087-1095 (street/urban fashion template): near-black #0A0A0A background with Vermillion #FF3D00 accent. High contrast, single accent — this is a premium minimalist dark palette. Worth promoting as a pattern: dark base + one warm accent with strong saturation contrast beats dark base + multiple cool glows.
- ui-ux-pro-max/data/design.csv lines 1400-1407 (crypto/Bitcoin template): three accent colors — bitcoinOrange #F7931A, burntOrange #EA580C, digitalGold #FFD600. Two warm-orange variants plus yellow-gold is an over-accent problem: burntorange vs bitcoin-orange is too close in hue (Δhue ~8°) to read as distinct semantic roles. One of the two oranges should be dropped; the gold can serve as the differentiated secondary.
- ui-ux-pro-max/data/colors.csv: 161 palettes stored with primary, secondary, accent, surface, and dark/light variants per row. The palette database itself is well-structured (each row is a coherent palette). Premium pattern: explicit surface + foreground pairing per palette ensures contrast is always checked at the data level.
- ui-ux-pro-max/data/design.csv lines 1190 (academic/philosophical template): Brass gradient ['#D4B872', '#C9A962', '#B8953F'] used for buttons — a three-stop warm gold gradient on dark background. This is a legitimate premium metallic treatment, not a cheap gradient. Positive pattern: named gradient with purpose-labeled stops rather than generic 'purple-to-blue'.
- ui-ux-pro-max SKILL.md rule table line 59: states 'Semantic color tokens' and 'avoid Raw hex in components' — this is the correct constraint. Positive architecture: the skill enforces token-first color usage at the rule level.
- ui-design-system/SKILL.md Workflow 1: generates primary, secondary, neutral, semantic, and surface color categories from a brand hex input. Correct three-layer (global → alias → component) architecture documented in design-system/SKILL.md. No color anti-patterns in the structural layer.
- design-token/SKILL.md: Color token taxonomy (global → alias → component) is clean. No hardcoded hex values in the skill itself. Correct.

**Good patterns to promote**
- ui-ux-pro-max MASTER.md generator with --persist flag: writes a hierarchical MASTER.md + per-page override files. This is the correct architecture for cross-session design consistency — a single source of truth with scoped deviations, not a flat config per page.
- ui-ux-pro-max/data/typography.csv: 57 font pairings tagged by mood, use case, and context with Google Fonts URLs and Tailwind config snippets. Context-tagged font pairings prevent lazy defaults — the banned fonts (Cormorant, JetBrains Mono, Outfit) only surface under explicit genre matches, not as generic recommendations.
- ui-ux-pro-max SKILL.md Priority-10 rule table: ordered accessibility (contrast 4.5:1, focus rings, ARIA) as Priority 1 before any aesthetic decision. This is the correct hierarchy — beauty is downstream of usability.
- ui-ux-pro-max base-16px + line-height-1.5 as the typography floor rule: explicit minimum body font size and line-height prevents the common AI anti-pattern of 12-14px body text with tight 1.2 line-height.
- design-system/SKILL.md three-layer token architecture (primitive → semantic → component) with CSS custom property examples: this is the correct pattern for maintainable, themeable design systems. The explicit 'never reference raw values in components' rule in design-token/SKILL.md reinforces it.
- ui-ux-pro-max/data/colors.csv: 161 palettes each carrying explicit surface + foreground pairs, not just accent colors. This ensures contrast is architecturally guaranteed rather than checked ad-hoc.
- ui-ux-pro-max SKILL.md 'SVG icons (no emoji)' listed as a must-have under Style Selection: prevents the common AI output anti-pattern of emoji as UI icons.

---

### animation-motion
- Decorative offenders: **0** · code/frontmatter correctly skipped: 38

**Typography notes**
- No font-family declarations appear in rendered design output across any of the 17 animation skills audited. All skills are library-reference documents (GSAP, Anime.js, PixiJS, Three.js, Babylon.js, R3F, Barba, Lenis, Rive, Lottie, Theatre.js, Motion Dev, etc.) — they teach API syntax, not produce visual HTML.
- pixijs-2d/SKILL.md line 198 uses fontFamily: 'Arial' inside a PixiJS TextStyle code example. Arial here is a PixiJS canvas font default, not a design recommendation — no issue.
- motion-system/SKILL.md defines a clean duration/easing token vocabulary (duration-instant through duration-deliberate, 6 tokens) with no font prescriptions — good separation of concerns.
- animation-principles/SKILL.md and motion-system/SKILL.md teach purposeful motion with duration values (50–700ms range) and named easing curves — neither imposes typography. Premium pattern: token-based duration scale is the right level of abstraction for a motion system skill.
- No banned fonts (Cormorant, Outfit, JetBrains Mono, Noto Kufi Arabic) appear anywhere in this slice. Zero typography offenders detected.

**Color notes**
- All color values in this slice appear exclusively inside fenced JS/TS code blocks illustrating API usage (e.g., pixijs-2d 'red', '#ffffff', 0x00ff00; animejs '#FF0000', '#FFF'; barba-js 'blue', 'red'; react-three-fiber 'orange'; theatre-js rgba struct). None render as design output — all are API parameter demonstrations.
- web-animation-effects/SKILL.md references gradient effects as an advanced animation type and links to federicopian.com as a real-world example — no color palette prescribed, which is correct for a catalog skill.
- No muddy, low-contrast, random-gradient, too-many-accent, or cheap gradient patterns found. No design palette is imposed by any animation skill — they correctly defer color decisions to design-system skills (ui-ux-pro-max, color-expert, etc.).
- Premium pattern worth keeping: no animation skill hardcodes a color palette. They stay library-neutral, which is exactly correct — animation skills should drive motion tokens, not color decisions.

**Good patterns to promote**
- motion-system/SKILL.md: clean 6-token duration scale (50ms–600ms) with semantic names and explicit reduced-motion override strategy at :root level — a textbook token architecture worth promoting as a standard.
- animation-principles/SKILL.md: tight prose-only reference (42 lines) with zero decorative filler, covers easing/duration/stagger/a11y concisely — exemplary lean skill format.
- web-animation-effects/SKILL.md: project-archetype recommender table (8 rows) maps project type → effect set → budget tier — a high-leverage routing table that prevents over-engineering.
- pixijs-2d/SKILL.md: // DON'T / // DO comment pairs inside code blocks are effective performance contrast patterns — legitimate instructional use of inline code comments, not decorative.
- gsap-scrolltrigger/SKILL.md and gsap-utils/SKILL.md: inline // return-value comments (e.g., gsap.utils.clamp(0, 100, 150); // 100) follow REPL-style documentation convention — clear, scannable, no ambiguity with decorative labels.
- All 17 skills cleanly separate animation logic from visual design — no font or color opinions leak into library reference skills. This is the correct boundary for a motion skill layer.

---

### critique-audit-skills
- Decorative offenders: **0** · code/frontmatter correctly skipped: 8

**Typography notes**
- The audit skills (design-audit, critique-visual-hierarchy, critique-composition, design-qa-checklist, design-audit/references/measures.md) collectively teach a coherent typography law: modular scale ratio 1.2–1.333, max ~5–7 distinct size steps, body line-height 1.4–1.6, heading line-height 1.05–1.25, line length 45–75ch (~66 target), ≤2 font families, small intentional weight set (e.g. 400/500/700). These are evidence-based and align with readable-measure and typography-scale companion skills.
- No font families are prescribed or recommended inside any of these 13 skills — typography checks are purely relational (scale, ratio, weight count, measure) not opinionated about specific typefaces. This is the correct approach: the law should enforce *structure*, not pick the fonts.
- The banned-font list (Cormorant, Outfit, JetBrains Mono, Noto Kufi Arabic as lazy defaults) is explicitly codified in design-audit/SKILL.md Step 3 (House Rules, line 103). This is the strongest enforcement point in the library — flagged as a Blocker category. Good: it is cited by name with the feedback doc reference.
- design-qa-checklist/SKILL.md checks 'Typography matches specified styles' and 'Icons are correct size and color' but does not enumerate what the style should be — it defers to the spec. This is appropriate for a QA skill but means it will not independently catch a banned-font choice if the spec itself uses one.
- critique-visual-hierarchy teaches 1.5× minimum size differential between hierarchy levels and warns against 'hierarchy flattening' — weight set too uniform. This is a valuable, concrete, enforceable threshold that should be promoted to the design law.

**Color notes**
- design-audit/references/measures.md (line 22–23) codifies the palette discipline rule: 'neutrals carry the UI; 1 (maybe 2) accent(s) reserved for primary action and key emphasis. Many competing saturated colors = a smell.' This is the correct premium principle and should be cited as the law.
- WCAG AA contrast minimums are consistently cited across design-audit (Step 3, line 65), design-qa-checklist ('Color contrast meets WCAG AA'), design-review-process ('WCAG AA'), and measures.md (body ≥4.5:1, large text/UI ≥3:1, non-text UI ≥3:1). Enforcement is thorough and traceable.
- No color palette examples or actual hex values appear in any of the 13 skill files. The skills are framework-only — they check structure and ratios, not specific palettes. This is appropriate for audit skills but means no premium or anti-patterns can be flagged from within this skill slice.
- None of the audit skills explicitly flag muddy gradient abuse, random multi-stop gradients, or cheap neon/glassy effects as patterns to catch — a gap worth adding to the critique-composition or design-audit House Rules checklist.
- critique-composition catches 'Competing horizontal rules and dividers that multiply without adding structure' as a common failure pattern — this is the closest any skill gets to flagging decorative visual noise, and it is a good hook for extending the law to gradient/color noise.

**Good patterns to promote**
- design-audit/SKILL.md is the strongest skill in the slice: it is a genuine meta-runner that aggregates all 13 sub-dimensions into a single scored /100 report with a blocker cap at 69. The House Rules section (lines 102–112) explicitly encodes Karim's bans (fonts, comment-label decoration, RTL/Arabic correctness, premium-web motion standard). This pattern — a master runner with hard house rules as blockers — is worth promoting as the law template.
- measures.md is an exemplary reference companion: pure numeric thresholds with skill citations, no fluff, immediately usable by any audit runner. The 'cite the rule each issue comes from' discipline it enforces turns subjective 'I feel like' feedback into attributable standards.
- critique-visual-hierarchy's 1.5× minimum size differential between hierarchy levels is a concrete, verifiable threshold that other skills should adopt explicitly.
- critique-composition's gestalt-based four-dimension structure (Balance / Whitespace / Rhythm / Gestalt) with a pass/minor/major tri-state per dimension is a clean, actionable output format that scales well for both fast desk-crits and formal audits.
- design-debt-audit's Severity × Frequency / Effort prioritization formula for debt triage is a quantitative approach worth reusing in any checklist that needs to rank findings.
- The banned-decoration rule in design-audit line 106 — flagging '// 01 — THE MISSION' comment-label motifs as a Blocker — is the most precise anti-pattern definition in the entire library. It is both specific (names the exact pattern) and enforceable (Blocker category caps the score).

---

### tailwind-component-libs
- Decorative offenders: **0** · code/frontmatter correctly skipped: 1

**Typography notes**
- tailwind/SKILL.md: Example design output uses `uppercase tracking-[0.18em]` on a <p> eyebrow label — 0.18em tracking is within acceptable range for an all-caps micro-label, but the skill does not constrain it with a reusable token, so individual compositions may over-track inconsistently.
- tailwind/SKILL.md: `text-7xl font-black leading-none` on an h1 — `leading-none` (line-height: 1) is aggressive and risky for multi-line headings; the skill should recommend `leading-[0.95]` or `leading-tight` as a safer lower bound.
- tailwind/SKILL.md: `text-xl font-medium` for eyebrow — font-medium (500) is fine, but the skill teaches no systematic type scale or scale rationale; compositions using it will DIY their own sizes.
- tailwind/SKILL.md: Font family is set via `@theme { --font-display: 'Inter', sans-serif; }` — Inter is an acceptable neutral choice, not a banned font. However the skill does not prohibit Cormorant/Outfit/JetBrains Mono at the token level, so a composition author could freely slip banned defaults in.
- antd-component-typography/SKILL.md: Instructs to 'prefer token-based customization' and use 'Ant Design v5 imports from ntd' — sound guidance. No explicit font family, scale, or weight conventions taught; entirely defers to the local antd component docs at C:\tmp\ant-design (path may not exist on non-dev machines).
- antd-theme-customization/SKILL.md: Exposes `fontFamily` and `fontSize` as key design tokens but gives no guidance on what values to avoid or prefer. `colorPrimary` default of `#1677ff` is documented but not critiqued. No type-scale rationale provided.
- design-resource-carousel/SKILL.md: Teaches 'big, phone-legible type' and recommends specimen display for font carousels — good, practical guidance. No banned-font check or variation pool is enforced; practitioners can freely default to Cormorant for a 'luxury' carousel look.
- icon-system/SKILL.md: No typography conventions. Stroke-weight and sizing tiers (12–48px) are well-specified.

**Color notes**
- tailwind/SKILL.md: Uses `text-cyan-300` and `bg-zinc-950` in the example composition — this is a reasonable dark-surface + accent pairing with acceptable contrast for large text, but the skill teaches no contrast-check step or minimum ratio requirement.
- tailwind/SKILL.md: Defines `--color-brand: oklch(0.68 0.2 252)` in the @theme example — use of oklch is a premium modern choice (P3-gamut aware, perceptually uniform). Good pattern worth promoting.
- tailwind/SKILL.md: Teaches `border-white/20` as an explicit safe default over bare `border` — smart, avoids the Tailwind v4 border-color regression. Premium defensive token practice.
- antd-theme-customization/SKILL.md: `colorPrimary` default `#1677ff` is Ant Design v5's built-in blue — not muddy, but flat sRGB with no P3 or oklch guidance. The skill does not teach how to build a multi-stop palette from a primary (e.g. tints/shades via the antd algorithm).
- antd-theme-customization/SKILL.md: Dark mode via `theme.darkAlgorithm` is documented — good. No guidance on semantic color tokens (danger, warning, success) or surface layering in dark mode.
- design-resource-carousel/SKILL.md: Recommends 'Carbon #171717 + Lime' and 'Onyx + Candy Blue' as example combos — these are strong high-contrast pairs (dark anchor + vivid accent). The cinematic-photo-behind-glass-card treatment avoids flat swatches. Premium aesthetic direction.
- design-resource-carousel/SKILL.md: 'Subtle gradients beat plain white' — correct directional guidance, but no gradient grammar (stop count, hue rotation, angle constraints) is provided; practitioners may use muddy multi-stop gradients.
- shadcn-ui/SKILL.md: Is a stub/catalogue entry only — no color or token conventions taught. Defers entirely to upstream (google-labs-code/skills) which is not installed.

**Good patterns to promote**
- tailwind/SKILL.md: CSS-first @theme token system (oklch color space, @utility named tokens) — teaches a principled, future-proof token layer rather than ad-hoc utility classes. Directly promotes the P3-gamut oklch(0.68 0.2 252) pattern.
- tailwind/SKILL.md: Separates layout/style concerns (Tailwind) from animation timing (GSAP/seekable adapter) explicitly — clean single-responsibility architecture for design tokens vs motion.
- tailwind/SKILL.md: `border border-white/20` defensive default against Tailwind v4 border regression — a small but premium-grade guardrail that prevents invisible-border bugs in rendered output.
- antd-theme-customization/SKILL.md: Teaches CSS variable mode (`cssVar: true`) and static token extraction (`theme.getDesignToken()`) — promotes design-token parity between code and tooling.
- design-resource-carousel/SKILL.md: Frosted-glass card over tone-matched cinematic photo as the premium swatch presentation — a concrete, reproducible alternative to flat color swatches that reads premium at thumbnail scale.
- icon-system/SKILL.md: Defines a systematic naming convention (icon-[category]-[name]-[variant]) and size tier grid (XS–XL) — provides a complete, unambiguous token language for icon assets.

---

### arabic-rtl-bilingual
- Decorative offenders: **0** · code/frontmatter correctly skipped: 5

**Typography notes**
- rtl-arabic-i18n/SKILL.md recommends a curated Arabic font tier: IBM Plex Sans Arabic (body default, pairs with Plus Jakarta Sans), Tajawal (marketing/friendly), Cairo (Karim's existing sites), Noto Sans Arabic (fallback/data tables only — not as a headline default), Rubik Arabic (playful brands), Amiri (editorial/Naskh serif), Reem Kufi (display Kufi for logos/headings). This is a clean, intentional stack.
- Banned fonts (Cormorant, Outfit, JetBrains Mono, Noto Kufi Arabic as lazy default) are absent from both skills — no violations found.
- rtl-arabic-i18n/SKILL.md specifies that Arabic font sizes feel 10-15% smaller than Latin at the same px and prescribes a compensating rule: `:lang(ar) { font-size: 1.075em; line-height: 1.7; }`. This is a strong, evidence-based practice.
- Arabic line-height guidance is explicit and correct: 1.6–1.8 for Arabic vs 1.4–1.5 for English, justified by diacritics and tall letter forms needing vertical room.
- localization-design/SKILL.md states minimum font size 16px+ for Arabic and Hebrew cursive scripts — valid floor, though it does not prescribe a full scale. No type scale, weight progression, or letter-spacing guidance is given in localization-design; the skill defers to the implementing team.
- Neither skill prescribes `letter-spacing` values. Arabic script tracking should always be 0 (tracking Arabic is illegal typographically — it breaks letter joining). This is unspoken but correct behavior by omission.
- Pairing strategy in rtl-arabic-i18n uses Plus Jakarta Sans as the English display face alongside IBM Plex Sans Arabic — a premium, non-default pairing that avoids the banned Outfit/Cormorant trap. Good pattern worth promoting.

**Color notes**
- Neither rtl-arabic-i18n nor localization-design prescribes any color palette, accent, or gradient for designs. Color guidance in localization-design is limited to cultural meaning tables (red, white, green across cultures) — purely informational, not a design prescription.
- The only color values present in rtl-arabic-i18n/SKILL.md are #000 and #fff in a didactic gradient-direction demo (lines 187-188). These are illustrative contrast extremes, not palette recommendations. No concern.
- localization-design/SKILL.md explicitly warns against relying on color alone for semantic meaning and notes that color associations vary by culture — this is a premium, WCAG-aligned pattern.
- No muddy, low-contrast, random-gradient, or cheap-gradient choices were found in either skill. No color anti-patterns to flag.

**Good patterns to promote**
- IBM Plex Sans Arabic + Plus Jakarta Sans as the default bilingual font pairing — monospace sibling (IBM Plex Mono) is already in the family but not forced, avoiding the JetBrains Mono ban.
- Arabic font-size compensation rule `:lang(ar) { font-size: 1.075em; line-height: 1.7; }` codifies the 10-15% optical-size gap between Arabic and Latin glyphs at the same px — rare and correct.
- Logical CSS property table (ms-/me-/ps-/pe-/text-start/border-s) as the primary layout strategy — zero directional override debt, direction-agnostic by construction.
- Per-block direction rule (never mix LTR/RTL mid-sentence; wrap technical tokens in `<span dir='ltr'>` or `<code>`) matches Karim's feedback_arabic_english_format rule exactly — good alignment between skill and user preference.
- GSAP dirX() helper pattern for flipping x-offset sign based on document dir — simple, composable, avoids per-animation RTL conditionals.
- `linear-gradient(to inline-end, ...)` over `to right` for direction-aware gradients — logical gradient shorthand that auto-mirrors in RTL.
- Noto Sans Arabic listed only as 'Fallback / data tables' — correctly demoted from headline role, consistent with Karim's ban on Noto Kufi Arabic as a lazy default.

---

### existing-rules-and-feedback
- Decorative offenders: **4** · code/frontmatter correctly skipped: 47

**Typography notes**
- BANNED DEFAULTS ON RECORD (per feedback_default_fonts_ban.md, 2026-05-19): Cormorant Garamond, Playfair Display, DM Serif Display (display); Inter, Outfit, DM Sans, Space Grotesk (body); JetBrains Mono, Fira Code (mono); Noto Kufi Arabic (Arabic). These are banned as AUTO-PICKS — they may appear in explicitly themed templates (e.g. brutalist-skill, frame-glitch-title) where the choice is justified by the brief, but must never be the default reach.
- OFFENDING FILE — 3d-animation-web-designer/SKILL.md lines 84-87: Lists Playfair Display, Outfit, DM Sans, Space Grotesk as 'recommended' body fonts and JetBrains Mono + Noto Kufi Arabic as mono/Arabic defaults. This directly contradicts the ban. The 'Recommended Fonts' table must be updated to the variation pool from feedback_default_fonts_ban.md.
- OFFENDING FILE — design-brief-od/SKILL.md line 190 and od-design-brief/SKILL.md line 192: Both list `Mono: JetBrains Mono, 400, 0.875rem` as part of the default type scale. This is a banned default. Replace with `Geist Mono` or `IBM Plex Mono` as the safe alternatives.
- Approved variation pool per brief type (from feedback_default_fonts_ban.md): Luxury/editorial → Fraunces (variable SOFT/WONK), Instrument Serif, Reckless, PP Editorial New; SaaS/tech → Bricolage Grotesque, Geist Mono AS display, Authentic Sans; Brutalist/cultural → Authentic Sans, Migra; Beauty/fashion → PP Editorial New, Tan Pearl, Marcellus; Arabic-first/MENA → Amiri Display or El Messiri (display), Cairo or Tajawal (body).
- Premium type scale conventions (from feedback_premium_web_default_standard.md): no default font stacks unless the brief earns them; typography decision must be justified in one line linking face choice to the brand brief before any CSS is written.
- Tracking/leading quality signals to enforce: hero text at clamp(2.5rem, 8vw, 6rem); section eyebrow labels at 0.65–0.75rem uppercase with letter-spacing ~0.2em in accent color (no `//` prefix); body at 0.85–0.95rem with line-height 1.7 and weight 300–400. These are from 3d-animation-web-designer/SKILL.md and are sound except for the `// ` prefix rule.
- gpt-tasteskill/SKILL.md recommends Outfit as one of four type picks while banning Inter — this partially contradicts the ban (Outfit is on the banned list). Needs alignment.
- html-everything/SKILL.md lines 105 and 113 use JetBrains Mono in template CSS defaults — a direct banned-default inclusion in a shipped template. Should be replaced with Geist Mono or IBM Plex Mono.

**Color notes**
- BANNED per feedback_premium_web_default_standard.md: generic purple/blue gradients as the default color story. No evidence of a specific palette being globally mandated, but the anti-slop rule bans reaching for purple/blue gradient without brief justification.
- CONFIRMED PREMIUM PALETTE on record (feedback_karim_web_design_bar.md): Karim's personal brand → navy #04091A + electric blue #4A80FF. This is a project-specific palette, not a universal default.
- AI Studio Today brand palette (from playbook_aistudiotoday_carousel.md): violet #0B0712 / #8B5CF6. This is a product-specific palette.
- feedback_color_font_deck_first.md mandates 3-4 palette options per web build BEFORE any code, each with a brief-matched rationale. The deck format uses `▌ HEX #XXXXXX CMYK …` swatches — the ▌ character here is used as a swatch indicator in a document template, not rendered design output. It appears in a code block in the skill memory note and is a documentation convention, not a deployed offender.
- Color deck format references `───────────────────────────────` as a divider in the Colors & Fonts deck slide template (feedback_color_font_deck_first.md line 39) — this is a slide mock-up in a plain-text doc, not rendered output. Mark as documentation convention, not an offender.
- No evidence of muddy or low-contrast color choices being systematically taught. The skills audited (3d-animation-web-designer, minimalist-skill, brutalist-skill) use high-contrast dark/light systems: near-black backgrounds with electric or accent color pops.
- Good pattern: 3d-animation-web-designer/SKILL.md prescribes `backdrop-filter: blur(12px)` frosted-glass nav with dark-on-scroll — a cinematic but functional treatment. Worth preserving.
- Risk: `Space Grotesk` appearing in multiple skills as a body font default while simultaneously being on the banned list creates an inconsistency that could cause a skill to contradict the law.

**Good patterns to promote**
- feedback_default_fonts_ban.md: variation-pool table keyed to brief type — this is the canonical reference; extend the law by citing this table, not replacing it.
- feedback_default_fonts_ban.md: the 'banned decorations' section (added 2026-05-20) is comprehensive — covers `// 01 — THE MISSION`, `/* HEADING */`, `[ 01 ]`, decorative em-dash chains, decorative slash chains, box-drawing trim, asterisk/star trim, fraction counters, and placeholder copy. The new law should import this list verbatim rather than redrafting it.
- feedback_color_font_deck_first.md: 8-step build workflow (brief → niche research → colors+fonts deck → design-system lock → animation stack → build → wire-up → testing) is a solid process skeleton. The law should mandate this workflow rather than describe it from scratch.
- design-audit/SKILL.md line 103: already has a one-line ban on Cormorant/Outfit/JetBrains Mono/Noto Kufi Arabic — this skill is already aligned. Use it as the reference implementation.
- font-resources/SKILL.md lines 89-92: cleanly lists the four banned fonts with ❌ markers. This is the desired pattern for how any skill should document the ban.
- minimalist-skill/SKILL.md: recommends Lyon Text/Newsreader/Instrument Serif for editorial serif with tight tracking (-0.02em to -0.04em) and tight line-height (1.1) — a premium editorial type spec worth codifying as a positive example in the law.
- ayzz-web-design-method/references/typography-and-color.md: explicitly references the `// 01 — THE MISSION` ban in context — this skill has already internalized the rule and can serve as a model for how domain skills should document compliance.
- 3d-animation-web-designer/SKILL.md body type spec (line 92): `0.85-0.95rem, line-height: 1.7, font-weight: 300` — solid readable body spec. Worth including as a positive benchmark (minus the `// ` prefix on labels).
- feedback_premium_web_default_standard.md Anti-Slop Guardrails section: 'Do not use visible code-comment labels, slash/bracket decorations, generic counters, or placeholder copy' — this is already law language; extend, don't replace.

