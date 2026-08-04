# Patterns full dump — 2026 template design intel

Full data behind `SKILL.md`. 7 beats, ~1244 sites studied. Each pattern keeps: what it is, why it works, real example sites (name + URL), and exact build notes for Webflow and Framer. Sellability is 1-10 (build-effort-vs-buyer-appeal).

## 1. Hero sections (150 sites studied)

### Centered SaaS hero — sellability 10
Badge pill -> headline (5-8 words) -> subhead -> CTA with reassurance microcopy -> full-width product screenshot, top-down load stagger (~80-120ms delays per element).
- Linear — https://linear.app/homepage
- Midday — https://midday.ai/en
- Stripe — https://stripe.com
Webflow: flex column, max-width container, pill = link block radius 999px, IX2 page-load stagger (opacity+translateY), screenshot in a div with 3D perspective + rotateX. Framer: Stack layout, per-element Appear (Fade Up) with incremental delays, screenshot tilt via Transform + Scroll Transform, pill as a reusable component with New/Beta/Announcement variants.

### Oversized display-typography hero — sellability 9
Viewport-filling headline/wordmark at 10-20vw, tiny supporting UI. Entrance = per-character/per-line mask reveal.
- GSAP — https://gsap.com/
- Palazzo Monti / DEMO Festival (via Qode roundup) — https://qodeinteractive.com/magazine/innovative-typography-hero-trends/
Webflow: heading in vw units native; char/line mask reveal needs GSAP SplitText embed, wrap lines in overflow-hidden divs, translateY 100%->0 with stagger. Framer: native per-character/word stagger via text Appear effects, no code; cursor-reactive distortion needs a code component.

### Dark dev-tool hero — sellability 10
Near-black bg, 1-2 blurred radial glows, grain overlay, white headline with gradient-tinted keyword, monospace accent, product screenshot in thin bordered frame.
- Resend — https://resend.com/
- Raycast — https://www.raycast.com/
- Warp — https://www.warp.dev/
- Fey — https://www.feyapp.com/
Webflow: body #0A0A0A, absolutely-positioned divs with radial-gradient + blur filter, PNG noise overlay low opacity, IX2 slow glow drift. Framer: gradient+blur on shapes, built-in Noise texture fill, loop Appear effects; ship dark+light as theme variants via color styles.

### Split product hero — sellability 8
Hero-scale product photo/render one side, short headline + dual CTA (explore/convert) the other.
- Radian Motorcycles — https://www.rideradian.com/
- Icebug — https://icebug.com
- Longbow Motors — https://longbowmotors.com
Webflow: 2-col grid or layered absolute image, scale-in 1.08->1.0 via IX2, works with Ecommerce CMS. Framer: grid/stack layout, image Appear with scale, Scroll Transform parallax.

### Full-bleed WebGL/3D interactive hero — sellability 7
Entire above-fold is a live 3D scene/shader reacting to cursor/scroll; headline/CTA float over canvas.
- Sui — https://www.sui.io/
- EverSwap (Lusion) — https://everswap.com/
- Vectr (Utsubo) — https://vectrfl.com/
Webflow: not native — custom code embed (Three.js) or, easier, Spline viewer / Unicorn Studio embed pasted into an Embed element; keep text as real DOM for SEO. Framer: native Spline component (paste scene URL) or Unicorn Studio code component — established ecosystem tools, buyers swap the scene link.

### Agency manifesto hero — sellability 9
Editorial, left-aligned/stacked; opinionated-claim headline, guarantee line, stats + founder photo + client logos, CTAs "Our approach"/"Work with us".
- Hildén & Kaira — https://www.hildenkaira.fi/
- MONOLOG — https://bymonolog.com/
Webflow: large rich-text heading, stats row, logo grid, line-by-line IX2 stagger — zero custom code. Framer: text stack with word-stagger Appear, logo row component, number counters via simple override or community counter component.

### Social-proof logo bar docked under hero — sellability 9
5-8 grayscale client/integration logos immediately below CTA, usually an infinite marquee loop.
- Midday — https://midday.ai/en
- Sui — https://www.sui.io/
- Shopify (via roundup) — https://www.perfectafternoon.com/2025/hero-section-design/
Webflow: two duplicated logo rows in overflow-hidden flex wrapper, IX2 loop translateX 0 to -50%, or 3-line CSS embed for smoothness. Framer: native Ticker component — drop logos, set speed/direction.

### Preloader -> hero load choreography — sellability 8
Branded preloader (numeric counter/wordmark/wipe) handing off into the hero's staggered reveal.
- Palazzo Monti (via Qode roundup) — https://qodeinteractive.com/magazine/innovative-typography-hero-trends/
- Osmo "Crisp Loading Animation" cloneable (219 clones, 1.1k likes) — https://webflow.com/made-in-webflow/popular
- Osmo — https://www.osmo.supply/
Webflow: fixed full-screen div, IX2 page-load timeline (counter needs small JS embed or lottie), height/clip wipe continuing the same timeline. Framer: no native preloader primitive — top-layer frame with Appear/Exit animations on load, or community code component; offset hero Appear delays ~1.2s after the wipe.

### Standout tricks — hero
- GSAP.com: animated "worm" weaves through the oversized headline letterforms — mascot-in-typography (gsap.com)
- DEMO Festival: hero letters deform asymmetrically on hover via variable-font axis play, cheap with font-variation-settings (Qode roundup)
- Ekipa Agency reloads with a different background color every visit (Qode roundup)
- Redo Bureau: draggable/rotatable liquid-metal logo, hero-as-toy (Qode roundup)
- Midday/Linear: announcement pill as a living news channel above the headline — ship as a CMS-bound component
- Osmo's "Crisp Loading Animation" cloneable proves preloaders are the most-cloned hero-adjacent asset on Made in Webflow
- Radian: static product hero + embedded 2:56 release film directly below — poster-image-first, video-second is the performance-safe 2026 pattern
- Schauspielhaus Zürich fills outline hero numerals with color on scroll (Qode roundup)
- Linear's verified headline length across top SaaS heroes: 5-8 words, never more
- Framer's native Spline component + Unicorn Studio embeds are how template authors ship "3D hero wow" swappable via one scene URL — never hand-rolled Three.js in a sellable template

Sources: awwwards.com/websites, minimal.gallery, dark.design, siteinspire.com, qodeinteractive.com/magazine/innovative-typography-hero-trends, perfectafternoon.com/2025/hero-section-design, lexingtonthemes.com/blog/stunning-hero-sections-2026, webflow.com/made-in-webflow/popular, pentaclay.com/blog/top-50-latest-framer-templates-for-the-upcoming-2026, frameplate.co/categories/best-sellers, linear.app/homepage, midday.ai/en, resend.com, rideradian.com, bymonolog.com

---

## 2. Layout, navigation, footer (150 sites studied)

### Bento feature grid — sellability 10
3-4 column grid of rounded cards, mixed spans (1x1/2x1/2x2), one feature per card, shared radius/border tokens, 1-2 hero cells span double width.
- Linear — https://linear.app
- Supabase — https://supabase.com
- Framer homepage — https://www.framer.com
- One Page Love bento collection — https://onepagelove.com/tag/bento
Webflow: Display:Grid wrapper (e.g. 4 col, auto rows), per-card column/row span, card as Component with label/copy/image props, hover lift via IX2. Framer: Grid layout or nested stacks, per-cell spans, card component with hover variant, Appear stagger on scroll — zero code.

### Floating pill/glass navbar, shrinks on scroll — sellability 9
Detached rounded-full nav floating 12-24px below top, backdrop blur, logo/links/CTA; compresses on scroll, some hide-on-scroll-down.
- Linear — https://linear.app
- shadcn Floating Pill Navbar block — https://www.shadcn.io/blocks/navbar-floating-pill
- Tegan Digital trend writeup — https://tegan.io/trends-pill-shaped-navigation/
Webflow: fixed-position wrapper (top 16px, max-width ~720px, radius 999px), native Backdrop Filters, IX2 "page scrolled" shrink + scroll-direction hide. Framer: fixed frame, native background blur; shrink/hide needs a code override (useScroll from framer-motion) — common marketplace approach.

### Fullscreen overlay menu, oversized links — sellability 9
Hamburger opens 100vh overlay, 4-7 links at 6-12vw, stagger-in, hover reveals image/video preview.
- Klim Type Foundry — https://klim.co.nz
- Dogstudio — https://www.dogstudio.co
- Bruno Simon — https://bruno-simon.com
- 34 examples roundup — https://qodeinteractive.com/magazine/examples-of-fullscreen-navigation-menus/
Webflow: fixed 100vh div (display:none default), IX2 click trigger fades/slides overlay then staggers links; hover image preview via absolutely-positioned image + IX2 hover. Per-character stagger needs GSAP SplitText embed — line-level is fully native. Framer: component with Closed/Open variants (auto-animated transition = the wipe), Appear stagger for links, hover-variant image layers; character-level splits need a code component.

### Two-panel/tabbed mega menu — sellability 8
Desktop dropdown expands full-width: category tabs left, icon+heading+description rows right, featured card, persistent CTA.
- Segment — https://segment.com
- Plaid — https://plaid.com
- Qualtrics — https://www.qualtrics.com
- Monday.com / Asana / Nike
Webflow: Navbar Dropdown set to position:absolute width:100vw, Tabs element inside (tab menu left, panes right), open-on-hover setting — no code, classic Webflow differentiator. Framer: not native — no mega-menu primitive; build hover-variant panel per item or a code component for ARIA/keyboard support — genuinely harder in Framer, so a working one is a selling point.

### Oversized wordmark footer — sellability 9
Footer's final row is the brand wordmark at 10-20vw or full-width SVG, often cropped off the bottom edge.
- Mitra / Diana's Seafood (via Wix roundup) — https://www.wix.com/blog/website-footer-examples
- Big-footer trend analysis — https://www.wix.com/studio/blog/big-website-footers
Webflow: heading font-size in vw (e.g. 13vw), line-height 0.8, overflow hidden on footer to crop baseline, or embedded SVG wordmark width:100%; scroll-into-view IX2 slide-up. Make the footer a Component. Framer: fluid/viewport-relative text sizing, clipping frame to crop, Appear slide-up on enter — inside the shared footer component.

### Sitemap mega-footer + utilities row — sellability 8
5-7 grouped link columns + bottom bar (logo, copyright, status, socials, theme toggle).
- Linear (6-col + brand statement) — https://linear.app
- Vercel (7+ col, status link, theme toggle) — https://vercel.com
Webflow: grid/flex columns inside a footer Component (marketplace requires footer as Component); theme toggle needs custom-code embed + Webflow Variables modes. Framer: horizontal stack of link-list stacks; real dark-mode toggle needs code override with localStorage — most templates ship separate light/dark styles instead.

### Pre-footer CTA band — sellability 9
Full-width section between last content and footer: headline, 1-2 buttons, optional email input, inverted background, shipped as a reusable component on every page.
- Vercel — https://vercel.com
- Linear — https://linear.app
- Category analysis — https://www.flowsamurai.com/post/top-selling-webflow-template-categories
Webflow: one Section as a Component with text/button props, insert on every page — Webflow guidelines explicitly want CTAs componentized. Framer: section component with text variables, trivial to retext.

### Editorial asymmetric/broken grid — sellability 7
12-col grid with deliberately offset image/text spans, varied heights, occasional overlaps via negative margin/z-index.
- STAGECREW — https://stagecrew.studio
- Gusta — https://gusta.studio
- The Print Loft — https://theprintloft.art
- SiteInspire gallery — https://www.siteinspire.com/
Webflow: Display:Grid 12 columns, explicit column start/end per child, overlaps via negative top margin + z-index, keep offsets in combo classes so buyers can retheme without breaking the grid. Framer: grids exist but overlaps usually mean absolute-positioned layers per breakpoint — more fragile; limit to 1-2 signature moments.

### Standout tricks — layout
- TRIONN "hold to blast" hero — press-and-hold gamified interaction (trionn.com)
- Linear numbers homepage feature sections 1.0-5.0 like a spec document
- Vercel puts a system/light/dark theme selector in the footer bottom-right
- Qualtrics mega menu has a use-case switcher refiltering the whole menu
- Segment color-codes mega-menu iconography by product area
- Ashley & Co's fullscreen menu is two-layered (page -> subsections in place, imagery changes per category)
- Barkli Gallery: menu shrinks the current page into a live thumbnail while sitemap takes the left
- Mathieu Lévesque's menu shows photo counts + hover previews per link
- Everyday Needs morphs its logo into the hamburger icon on scroll
- Cusp's overlay menu is an infinite-scroll loop of Roman numerals

Sources: minimal.gallery, dark.design, awwwards.com/websites, siteinspire.com, awwwards.com/awwwards/collections/menu, onepagelove.com/tag/bento, onepagelove.com/inspiration, qodeinteractive.com/magazine/examples-of-fullscreen-navigation-menus, webstacks.com/blog/mega-menu-examples, sitebuilderreport.com/inspiration/website-footer-designs, wix.com/studio/blog/big-website-footers, flowsamurai.com/post/top-selling-webflow-template-categories, wcopilot.com/blog/top-framer-templates, framer.com/marketplace/templates/portal, linear.app

---

## 3. Scroll animation and scrollytelling (110 sites studied)

### Sticky stacking cards — sellability 10
Column of full-width cards, each pins (position:sticky), next card slides over; pinned card scales ~0.92/dims. 3-6 cards sweet spot.
- Sticky Overlap (Framer component, $12) — https://www.framer.com/marketplace/components/sticky-overlap/
- Parallax Image Stack (Framer, $12) — https://www.framer.com/marketplace/components/parallax-image-stack/
- Adidas Annual Report 2024 — https://report.adidas-group.com/2024/en/
Webflow: sticky top offset per card (2/4/6rem), parent position:relative, IX2 "while scrolling in view" scales to 0.92 + drops opacity. GSAP ScrollTrigger pin+scrub is the smoother upgrade. Framer: Sticky position per card with pin offset, Scroll Transform (scale 1->0.92, opacity), or a paid code component using Framer Motion useScroll.

### Scroll-scrubbed text reveal (line/word/char) — sellability 10
Headlines split into lines/words/chars animate tied to scroll; grey-fills-to-color word-by-word variant.
- YesNo — https://yesnowww.com/
- Blux Studio — https://bluxstudio.com/
- GSAP Text Animations (Timothy Ricks cloneable) — https://webflow.com/made-in-webflow/gsapscrolltrigger
- Sticky Text Reveal (Framer, $10) — https://www.framer.com/marketplace/components/sticky-text-reveal/
Webflow: IX2 alone only animates whole blocks; per-line/word/char needs GSAP SplitText + ScrollTrigger embed (GSAP + plugins free since Webflow's acquisition). Framer: native for appear-style reveals (Text effects animate per line/word/char on scroll-into-view); scrub-fill needs a code component (useScroll + useTransform).

### Pinned section with content swap — sellability 9
Section pins 2-4 viewport-heights while content swaps in steps (phone/dashboard mockup fixed, screenshots change).
- Quoti — https://getquoti.ai/
- BMW Group Report 2025 — https://www.bmwgroup.com/en/report/2025/index.html
- Switch Content on Scroll (Timothy Ricks cloneable) — https://webflow.com/made-in-webflow/gsapscrolltrigger
- Shopify Editions Winter '26 — https://www.shopify.com/editions/winter2026
Webflow: sticky media column beside scrolling text column, IX2 scroll-into-view cross-fades matching image; GSAP ScrollTrigger pin:true + timeline for the smoother pro version, CMS-editable. Framer: Sticky position on media frame, Scroll Variant triggers swap image variants as text passes — no code.

### Horizontal scroll driven by vertical scroll — sellability 8
300-500vh tall track pins a viewport container, translates panels on X as user scrolls Y.
- Theo — https://www.theo.be/
- Canals Amsterdam — https://canals-amsterdam.com/
- Nikola Radeski — https://nikolaradeski.com/
- Home Société — https://homesociete.ca/en/
Webflow: wrapper 300-500vh, inner sticky div 100vh overflow hidden, horizontal flex track, IX2 "while page scrolling" maps 0-100% to translateX; GSAP ScrollTrigger scrub+containerAnimation is the smoother, now-free option. Framer: not cleanly native — needs code component/override (useScroll + useTransform to '-75%' on a sticky container); marketplace components exist to include.

### Multi-layer parallax hero — sellability 8
3-6 stacked layers (bg/mid/fg/headline) at different scroll speeds; the Firewatch pattern; gradient fade blends hero into next section.
- Firewatch parallax (Webflow cloneable) — https://fire-watch-parallax.webflow.io/
- Cloudz — https://cloudz.webflow.io/
- Every Last Drop — http://everylastdrop.co.uk/
- OODOS — https://oodos.life/
Webflow: fully native IX2 "while page is scrolling" with different move-Y per layer (bg 0-10%, fg 30-50%), fixed gradient overlay fading opacity — most-cloned Webflow interaction. Framer: fully native Scroll Transform "Parallax"/speed effect per layer on canvas.

### Zoom-scrub media hero — sellability 9
Framed image/video scales to full-bleed (or inverse) scrubbed to scroll position. Apple-style.
- Sticky Zooming (Framer, $14) — https://www.framer.com/marketplace/components/sticky-zooming/
- Apple October 2020 remake (Webflow cloneable) — https://apple-october-2020.webflow.io/
- Chanel J12 Watch — https://www.chanel.com/us/watches/the-j12-watch/
Webflow: sticky inner container in 200-300vh wrapper, IX2 "while scrolling in view" maps progress to scale (0.6->1) + border-radius (24px->0). GSAP ScrollTrigger scrub for frame-perfect version. Framer: native Sticky + Scroll Transform scale/border-radius — one of the few "expensive" effects fully no-code in Framer.

### Scroll-scrubbed video/image-sequence — sellability 7
Pinned full-screen video/image-sequence whose playhead is bound to scroll — assemble/explode/rotate.
- Singula Team Chizzy — https://chizzy.singula.team/3/
- Ray-Ban Meta — https://www.ray-ban.com/usa/l/discover-meta-ray-ban-display
- Chanel J12 Watch, iCoMat — https://icomat.co.uk/
Webflow: custom code only — GSAP ScrollTrigger driving video.currentTime (unreliable iOS) or a canvas image-sequence (100-150 frames) drawn per scroll progress; ship script + documented frames folder. Framer: not native — code component using useScroll to drive canvas/video currentTime; flag the asset burden.

### Section wipes/curtain overlaps — sellability 9
Each full-height section pins as the next slides over (dark over light, footer revealed "under" the page).
- Petralithe — https://petralithe.com/en
- Unseen 2025 Annual Report — https://2025.unseen.co/
- GlobalLeathers (sticky-frame portal) — https://global-leathers-digitalbutlers.webflow.io/
Webflow: sections position:sticky top:0 ascending z-index, next section slides over naturally; reveal-footer variant via body margin-bottom = footer height + fixed footer. Framer: Sticky sections stacking z-index, Scroll Transform scale/opacity on outgoing section — no code.

### Standout tricks — scroll
- Webflow acquired GSAP (late 2024) — GSAP + all premium plugins (SplitText, ScrollSmoother, ScrollTrigger) now free in Webflow
- Framer marketplace proves single scroll effects sell standalone: Sticky Zooming $14, Parallax Video Pro $18, CMS Parallax Gallery $15, Sticky Text Reveal $10
- SBS "The Boat" uses a shaking/tilting scroll mechanic synced with audio
- HuffPost Highline "Poor Millennials" maps scroll to an 8-bit walking character with embedded charts
- UCL "Library of Lost Maps" — curated zoom across one giant map image, template-friendly single-asset scrollytelling
- Ray-Ban Meta / iCoMat use scroll-driven "exploded view" for hardware products
- OODOS's gradient-fade parallax exit solves the ugly hard-edge problem
- Timothy Ricks' cloneables dominate Made-in-Webflow's scroll category — mirroring his structure lowers support burden
- "Universe to You" switches typefaces as you zoom cosmic->human scale
- Webflow parallax template pricing: one-page $29-49, multi-layout $99-129 (Ertiox $59/4.93, Noire $99, Arisca $129)

Sources: scrollytelling.ai/examples, htmlburger.com/blog/best-scrolling-websites, memberstack.com/blog/14-of-the-best-parallax-scroll-examples-for-2025, visualhierarchy.co/best-parallax-websites, webflow.com/made-in-webflow/gsapscrolltrigger, webflow.com/templates/search/parallax, awwwards.com/websites/scrolling, framer.com/marketplace/components/tags/scroll, framer.com/marketplace/components/tags/parallax, framer.com/marketplace/components/tags/sticky

---

## 4. Color palettes and gradients (112 sites studied)

### Near-black SaaS dark mode — sellability 10
Base surface very dark desaturated near-black, never #000.
- Linear #08090A (314 CSS occurrences) — https://linear.app
- Stripe dark sections #181818 — https://stripe.com
- Halo Framer template #121212, stated 15.8:1 contrast
- Text off-white #E2E4E7/#E4E5E9, secondary #8A8F98
Webflow: Webflow Variables — bg #0A0A0B, surface #141416, border #2A2A2E, text #E4E5E9, text-muted #8A8F98, bind every class to variables, set on Body tag. Framer: native Color Styles as tokens (Background/Surface/Border/Text/Muted) referenced everywhere.

### Monochrome dark + one acid/electric accent — sellability 10
Grayscale-dark site, one high-chroma accent for CTAs/links/numbers.
- Lando Norris landonorris.com — acid lime #D2FF00 on green-tinted near-black #101400
- Sui sui.io — electric blue #298DFF (+ #5CA9FF) on gray #222529/#4B515B/#A1A7B2
- Vectr, TRIONN
Webflow: one "Accent" Variable bound to buttons/links/selection/highlights; also tint the background 2-3% toward the accent hue instead of neutral black; ::selection color needs a 2-line embed. Framer: single Accent Color Style + text-highlight component variant; ship 3-4 preset accent colorways as top-level variants.

### Aurora/mesh gradient hero — sellability 10
Soft multi-point blend or animated bands behind hero, over dark base. 3-4 analogous hues, 80-90% opacity, blobs pushed to corners + one near center.
- Stripe — https://stripe.com
- Linear — https://linear.app
- Vercel — https://vercel.com
- Wembi — https://www.wembi.ai/
- Recipe source: superdesign.dev/styles/aurora, designmd.app
Webflow: static mesh via 2-3 stacked radial gradients or exported SVG/PNG; animated aurora needs CSS keyframes embed or WebGL/GSAP embed, keep static Designer fallback. Framer: native gradient fills + Layer Blur + Loop effects cover static/simple animated; shader-quality needs a code component; expose 3 hues as props.

### Layered deep-purple/indigo glow stack — sellability 9
4-6 dark saturated purples/indigos stacked as overlapping blurred radial glows, "lit from within."
- Raycast raycast.com — #330381, #523091, #550062, #1A0B33, #070D4F, #043F96 + coral #FF6363 pop
- Rig (rig.ai), Ponder (ponder.ai)
Webflow: 3-4 absolutely-positioned divs, native radial-gradient fill, blur filter via 5-line CSS embed (filter: blur(120px) — no native blur UI), optional IX2/GSAP drift. Framer: native ellipse frames with radial gradient fill + Layer Blur 100-150px + loop transitions, zero code.

### Grain/noise overlay on gradients — sellability 8
Film-grain noise layer, low opacity, over gradients/whole page to kill banding and add texture.
- Grainient (dedicated supply site) — https://grainient.supply/
- MONOLOG — https://bymonolog.com/
- 108 — https://108.supply
Webflow: fixed full-viewport div with tiling noise PNG (128-256px tile), opacity 4-8%, mix-blend-mode overlay, pointer-events none (blend mode may need 1-line embed on some plans). Framer: native Texture/Noise effect on frames (or community components), set noise ~5% on a top-level overlay frame.

### Warm off-white editorial base — sellability 9
Light-mode counterpart: warm cream/paper background, never #FFF.
- Aristotle heyaristotle.com #F0ECE0/#E8E4D8
- Gusta gusta.studio #F9F7F2
- Don't Board Me dontboardme.com paper #FCFCF7/#F3F3E9
Webflow: bg variable #F7F4EE-range, text #1A1814 (warm black), borders 8-12% black; pair with a "dark editorial" inverse mode via Webflow Variables modes. Framer: native color tokens, light/dark appearance or duplicate color-style sets; warm-tint every gray in the ramp.

### Functional multi-accent set on dark (Linear trio) — sellability 7
Dark monochrome base carries 2-4 saturated accents reserved per product area, never mixed freely.
- Linear indigo #4354B8, orange #E5591D, pink #F79CE0 (each hundreds-to-dozens of CSS occurrences vs #08090A base)
- Raycast pairs purple stack with coral #FF6363
Webflow: define accent-1/2/3 variables, one "Feature card" component with combo classes per accent swapping icon color + radial glow (~12% alpha) + 1px tinted border. Framer: one card component with an Accent variant property (enum), each variant re-colors icon/glow/border — fully native.

### Paper base + muted retro brights — sellability 6
Cream/paper background with 3-4 desaturated-but-loud retro colors in flat blocks.
- Don't Board Me (Awwwards SOTY 2024) — olive-mustard #A7A238, tomato #E33529, yellow #FFF500, brown #854720, teal-blue #2B6786 on paper #F3F3E9
- Burrito Madre, Joy Rush, Mr Day
Webflow: 4-5 color variables + section-level bg swaps bound to a CMS color field. Discipline: hues never blend in gradients here, flat blocks only. Framer: color styles + per-page theme via component variants; CMS-driven color field on collection pages.

### Standout tricks — color
- Tint the black to the accent (landonorris.com): bg #101400 (green-tinted black) under acid lime #D2FF00 — formula: bg = accent hue at ~10% saturation, 4-8% lightness
- Linear's accent discipline: strictly 2-color base palette, 3 accents appear only in feature/bento contexts, never in chrome (nav/footer/buttons stay monochrome)
- Raycast stacks five adjacent deep hues as overlapping blurred glows rather than one purple — multi-hue stack is what makes the glow read as light, not fill
- Grain (4-8% opacity noise + mix-blend-mode:overlay) simultaneously kills gradient banding and de-generics the design — cheapest premium signal in both tools
- Aurora recipe: 3-4 ANALOGOUS hues only, 80-90% opacity, blobs at corners + one center, over near-black — complementary-hue meshes look amateur
- Awwwards 2024-25 winners split dark/high-tech vs warm-paper playful; the neutral-gray/default-blue middle never wins
- Marketplace economics: dark AI/SaaS templates dominate discovery (free NajmAI: 103,900+ Framer views) — meaning pastel-light health/fintech and warm-cream editorial are less-crowded sellable niches
- Never ship pure #FFF or #000 in a template — every verified premium site offsets both ends
- Ship the palette as swappable tokens (Webflow Variables with modes / Framer Color Styles) and advertise "customizable color system" as a purchase trigger

Sources: awwwards.com/websites, awwwards.com/websites/sites_of_the_year, awwwards.com/websites/colorful, dark.design, minimal.gallery, webflow.com/made-in-webflow/popular, victorflow.com/blog/dark-webflow-templates, gola.supply/blog/best-dark-saas-website-templates, oma-kase.com/blog/15-best-framer-saas-templates, veloxthemes.com/blog/best-framer-templates, framer.com/marketplace/templates/suprema, linear.app, sui.io, stripe.com, raycast.com

---

## 5. Typography (140 sites studied)

### Editorial serif display + neutral grotesk body — sellability 10
High-character serif at 60-120px headlines; quiet neutral grotesk 16-18px body.
- Elena Scott = Editorial Old + Neue Montreal (Typewolf SOTD Dec 9 2025) — https://typewolf.tumblr.com/
- Every = Signifier + Switzer — https://every.to/
- Azione = Editorial Old + Saans + Favorit Mono — https://azione.com/
- Pact = Manuka + Feature + Söhne; Gradient = New Spirit + Outfit; BioRepublic = Queens + Favorit
- Free marketplace-legal clone: Instrument Serif/Fraunces + Inter/Switzer
Webflow: Google Fonts in Site Settings > Fonts (Instrument Serif/Fraunces/Playfair Display + Inter); marketplace rule = Google/OFL only, document paid upgrade fonts in template instructions. Framer: built-in font library (Instrument Serif, Fraunces, Inter etc.) as Text Styles; Framer template submissions restricted to library/Google fonts (no custom uploads).

### Italic serif accent word inside a sans headline — sellability 9
One or two words swapped to an italic high-contrast serif inside a sans headline.
- Readymag — https://readymag.com/
- Frameblox font guide — https://www.frameblox.com/blog/30-best-fonts-for-framer-websites-and-templates
- Muse = DaVinci + Suisse Int'l (Typewolf SOTD Dec 11 2025)
Webflow: wrap accent word in a span, combo class font-family Instrument Serif, italic, ~1.05em to optically match x-height. Framer: select word inline, override font to Instrument Serif Italic — works inside Text Styles, zero code.

### Monospace eyebrow/label layer — sellability 9
Mono font 11-13px, uppercase, +5-10% tracking for eyebrows/section numbers/nav labels/footer meta.
- Speakeasy / London Short Film Festival = Diatype + Diatype Mono — https://typewolf.tumblr.com/
- Dirty Vine = Swear + DM Mono; Azione = Favorit Mono
- Free equivalents: DM Mono, Space Mono, IBM Plex Mono (DM Sans + DM Mono mirrors the paid system)
Webflow: "eyebrow" class (DM Mono, 12px, uppercase, letter-spacing 0.08em), reused everywhere, Google Fonts = legal. Framer: "Label/Mono" Text Style from built-in library, applied across components.

### Oversized full-bleed hero type ("Wide & Loud") — sellability 9
Hero headline/wordmark filling viewport width, 12-20vw, often uppercase, sometimes cropped/layered.
- MONOLOG — https://bymonolog.com/
- Studio OL — https://ol.studio/
- project://cult — https://cult.worldwidebased.space/
- Named trend "Wide & Loud" citing Charles Leclerc, Dropbox rebrand — https://www.nopanicdesign.com/blog/web-design-trends-2026-colors-fonts/
Webflow: font-size in vw (e.g. 13vw) or clamp() via head embed (Designer UI lacks native clamp). Framer: native "Fit" text sizing toggle auto-scales text to frame width — one click, purpose-built.

### Masked per-line kinetic reveal on load (SplitText pattern) — sellability 10
Headlines animate line/word-by-word from behind an overflow mask (translateY 100%->0, 0.05-0.08s stagger, expo ease) on load and scroll-into-view.
- Framer Marketplace Text Reveal Animated / Motion Text Reveal (free) — https://www.framer.com/marketplace/components/mask-text-reveal/ , https://www.framer.com/marketplace/components/motion-text-reveal/
- Navbar Digital, Made in May
Webflow: (a) native IX2 with manual line-splitting (brittle on reflow) or (b) GSAP SplitText + ScrollTrigger embed (free) — route (b) is what premium templates ship. Framer: fully native Text layer > Effects > Appear, per line/word/character with stagger + mask, no code — genuine Framer advantage.

### Scroll-scrubbed word-by-word text — sellability 8
Long statement paragraph pinned, words change opacity/color one-by-one tied to scroll (scrub, not trigger).
- Apple marketing pages — https://www.apple.com/
- Linear — https://linear.app/
- Framer Marketplace Text Scroll Effects — https://www.framer.com/marketplace/components/text-scroll-effects/
- Framer University Text Scroll Animator — https://framer.university/resources/text-scroll-animator-component-for-framer
Webflow: not native — IX2 can approximate whole-block opacity; real per-word scrub needs GSAP ScrollTrigger (scrub:true) + SplitText embed. Framer: not fully native — native Scroll Transforms animate whole layers; use free/premium code component (Motion Text Reveal is free) or Motion's useScroll override.

### Single neo-grotesk system (the Inter economy) — sellability 8
Entire site in one flexible sans, weights/size do hierarchy work.
- Premium tier: Neue Montreal, Söhne, Suisse Int'l, Aeonik, GT America (Aeonik used by Revolut/Eurosport)
- Template tier: Inter — Novastyle, Cutaway (Webflow templates), Stripe pairs Inter with refinements
Webflow: Inter (or Switzer OFL upload) as the single project font, whole scale in body/heading tag styles for one-change rebrand. Framer: one Text Style stack from built-in library (Inter, General Sans, Satoshi); global font swap is one click — a stated selling point.

### Quiet-luxury high-contrast serif — sellability 8
Soft, high-contrast/calligraphic serifs for hospitality/wellness/fashion.
- Heart & Soil = Cardinal + Sweet Sans + Baskerville — https://heartandsoil.co/
- Solab = Cardinal + Helvetica Now — https://www.solab.fr/
- Speakeasy = Tobias; BioRepublic = Queens; Dirty Vine = Swear
- Free stand-ins: Fraunces (closest to Canela/Alpina), Cormorant Garamond, Young Serif
Webflow: Fraunces + Cormorant Garamond on Google Fonts (legal); Fraunces' SOFT/WONK axes need @font-face CSS embed for full variable control (Designer UI exposes only weights). Framer: Fraunces/Cormorant available in library as display Text Style; variable axes beyond weight need a code override (style.fontVariationSettings).

### Standout tricks — typography
- The free-clone playbook IS the business: both marketplaces ban paid fonts, so bestsellers are designed on Instrument Serif/Fraunces/Switzer/Space Grotesk/Inter, then paid "upgrade fonts" are listed as an upsell hook
- Framer's "Fit" sizing + native per-line/word/character Appear effects make the two highest-selling type patterns zero-code in Framer but GSAP-embed-dependent in Webflow — build Framer first, port with a documented embed block
- Disable per-character splitting for Arabic kinetic type — it breaks the connected script; per-word/per-line reveals work fine (near-nobody knows this — defensible AR/EN template niche)
- Same-superfamily sans+mono (DM Sans + DM Mono mirroring Diatype/Diatype Mono) is the cheapest way to fake a bespoke type system
- Variable-font axis play (Fraunces SOFT/WONK/opsz, Aktiv Grotesk) for hover weight/width animation — needs font-variation-settings via custom code in BOTH tools, thin competition
- Typewolf's site-of-the-day archive (typewolf.tumblr.com) is a free, always-current pairing database — mine monthly instead of guessing trends
- Preview-thumbnail rule: templates whose hero IS type (oversized wordmark or serif/sans lockup) demo better than photo-led ones because buyers judge from one screenshot

Sources: awwwards.com/websites/typography, minimal.gallery, dark.design, siteinspire.com, typewolf.tumblr.com (+ /page/2, /page/3), typza.com/insights/top-10-best-typography-combinations-2026, creativeboom.com/resources/top-50-fonts-in-2026, frameblox.com/blog/30-best-fonts-for-framer-websites-and-templates, fontsinuse.com/in/6/formats/21/web

---

## 6. Micro-interactions (115 sites studied)

### Blend-mode dot cursor with hover morph — sellability 8
10-30px circle follows pointer with lag (lerp 0.1-0.2), morphs into a labeled disc on hover, mix-blend-mode:difference to invert. Disabled below ~992px.
- Waaarhol — https://waaarhol.com/
- Typography Principles by Obys — https://typographyprinciples.obys.agency/
- Lux Expression — https://luxexpression.com/
Webflow: fixed div (z-index 9999, pointer-events none), IX2 "Mouse move in viewport" with 50-90% smoothing for lag, hover-morph via "Mouse hover" scaling + text child reveal; mix-blend-mode/cursor:none need a 3-line CSS embed. Cloneables: "#37 Custom Cursor on Hover", "IX2 Custom Cursor" — https://webflow.com/made-in-webflow/custom-cursor. Framer: native Cursors feature (custom cursor per element with follow smoothing + hover swap), blend-mode invert needs a small code override.

### Overflow-clip hover zoom + caption slide-up on cards — sellability 10
Card image in overflow:hidden wrapper scales 1.05-1.1 over 0.6-0.9s on hover, caption slides up from clipped edge, card lifts 4-8px.
- Pesquera Diez / P10 by Mubien — https://pesqueradiez.com/en/about
- Duten (texture hover reveal) — https://duten.com/en/finish/brushed-stainless-steel/
- Made by Analogue — https://madebyanalogue.co.uk/studio/
Webflow: fully native IX2 hover trigger — scale action on child image, move action on absolutely-positioned caption, wrapper overflow hidden, custom cubic-bezier easing. Framer: fully native hover variant of card component (image scale, caption y-offset 0), spring or custom bezier transition.

### Cursor-following image/video preview on list hover — sellability 9
Text-only project/menu list; hovering a row floats an image/video near the cursor with lag, cross-fades between rows, non-hovered rows dim.
- Gianluca Gradogna — https://gianlucagradogna.com/through-this-lens
- Awwwards "List image hover" — https://www.awwwards.com/inspiration/list-image-hover
- Webflow cloneables (Smooth Effects for Mouse Cursor, Mouse Tooltip Next Project Teaser) — https://webflow.com/made-in-webflow/custom-cursor
Webflow: IX2 "Mouse move in viewport" drives a fixed image wrapper with smoothing, per-row hover toggles which image is visible + dims siblings; smoother version = 10-line GSAP embed using gsap.quickTo(). Framer: row-dimming/image-swap work with hover variants, but cursor-following float needs a code override (useMotionValue + useSpring on pointermove) or a marketplace cursor-follow component.

### Magnetic buttons and nav links — sellability 7
Buttons/nav items translate toward cursor within a proximity radius, spring back on leave.
- Codrops Magnetic Buttons demo — https://tympanus.net/Development/MagneticButtons/
- Webflow cloneable "Magnetic Call To Action" — https://webflow.com/made-in-webflow/magnetic
Webflow: not truly native — IX2 "mouse move over element" fakes a weak version; real spring-back needs a small custom-code embed (mousemove listener + GSAP elastic ease on mouseleave). Framer: not native — code component/override (onPointerMove sets motion value, useSpring returns to 0 on leave); reusable community overrides exist.

### Marquee/ticker bands with hover-pause — sellability 9
Infinite looping horizontal strips (display text, client logos, sponsor tickers); premium versions run two opposite-direction rows, pause on hover, or react to scroll velocity.
- Eight Pixel, FlowFest 2024, OnePageFlip, Off+Brand (free Webflow+GSAP template, marquee wraps the site) — https://onepagelove.com/marquees
- Webflow made-in-webflow marquee tag — https://webflow.com/made-in-webflow/marquee
Webflow: pure-CSS keyframe embed (duplicate content twice, translateX -50% loop, animation-play-state:paused on hover) or IX2 loop; scroll-velocity direction needs GSAP ScrollTrigger embed. Framer: fully native built-in Ticker component (speed, gap, direction, hover-pause); velocity-reactivity is the only part needing an override.

### Counter/curtain preloader with content reveal — sellability 7
Full-screen panel shows a counter or animating wordmark/logo, lifts away while hero elements stagger in, on the same timeline/easing as the reveal.
- Grégory Lallé — https://gregorylalle.com
- SPYLT by Tubik — https://spylt.com
- Henri Heymans — https://henriheymans.com/
Webflow: mostly native IX2 page-load trigger for curtain/wordmark versions; live 0-100 counter needs ~10-line JS embed. Standard practice — include a "delete this div to remove loader" note for buyers. Framer: no native preloader primitive — full-screen overlay frame with Appear + delayed exit, or a code component that hides after window load; keep to a 1-1.5s branded curtain since Framer sites render fast.

### Full-screen wipe/mask page transitions — sellability 8
Clicking a link plays a colored-panel wipe, mask/clip reveal, or pixelation dissolve, then the destination enters with the reverse move; persistent elements (logo, nav) stay fixed.
- Amaterasu (mask reveal) — https://amaterasu.ai
- TeleTech (pixelated transition) — https://teletech.events/archive
- Cyd Stumpel — https://cydstumpel.nl
- Saisei (Webflow-built page transition) — https://saisei-sbj.webflow.io
Webflow: not native across pages. (a) overlay trick — IX2 click animation plays the wipe, navigation delayed ~600ms, plus a page-load enter animation on every page (pure Webflow); (b) Barba.js/Swup custom-code embed for real cross-fade/persistent elements — more fragile, document it. Framer: partially native — link/page transition effects (fades, overlay-style) configurable without code, plus destination Appear effects complete the illusion; complex masks/pixel dissolves need a code component.

### Animated link underlines (draw-through, exit-right) — sellability 8
1-2px line scales in from the left on hover, exits to the right on mouse-leave (transform-origin swap) instead of reversing.
- FreeFrontend CSS link styles collection — https://freefrontend.com/css-link-styles/
- Alec Tear — https://alectear.com
Webflow: pure-CSS embed using ::after with transform-origin swap (right on base, left on :hover) applied to a global .link class — most robust for buyers; or IX2 hover scaling a 1px underline div (per-instance). Framer: native via component variants (underline layer scaleX 0 -> 1 on hover); the exit-to-right origin swap isn't expressible in variants — needs custom CSS in site settings or a code component.

### Standout tricks — micro-interactions
- Pixelated/dither page transition (TeleTech, teletech.events/archive) — mosaic-block dissolve, doable as a grid of divs toggled in random order
- Color-inverting cursor via mix-blend-mode:difference (Waaarhol) — one CSS line works over every background
- Draw-with-light cursor (Komnata Agency, komnata.agency) — canvas-based light-painting trail
- Interactive preloaders as engagement: Stained Glass Real Estate (color shapes while loading), Tolia (temperature-responsive ice-cream character)
- iPadOS-style sticky cursor snapping to/haloing hovered UI — Webflow cloneable "iPad Cursor Interactions" (Moritz Petersen)
- Marquee wrapped around the entire site frame (Off+Brand free template) — ticker as site architecture
- Loader-to-hero choreography (Grégory Lallé) — preloader exit and hero entrance share one timeline/easing
- Cursor morph as content preview: "Mouse Tooltip Next Project Teaser" (Jonas Arleth cloneable)
- WebGL point-cloud mouse displacement on hero imagery (Amaterasu) — top-tier wow, ship as optional embed only

Sources: awwwards.com/awwwards/collections/hovers-cursors-and-cute-interactions, awwwards.com/awwwards/collections/loading-page, awwwards.com/awwwards/collections/transitions, htmlburger.com/blog/website-preloaders, onepagelove.com/tag/custom-cursor, onepagelove.com/marquees, webflow.com/made-in-webflow/custom-cursor, awwwards.com (customize-your-mouse-cursor article), orpetron-team.medium.com (10 exceptional custom cursors)

---

## 7. Premium motion, 3D, rich media (120 sites studied)

### Kinetic typography reveal (per-char/word blur+offset stagger) — sellability 10
Headlines split into chars/words/lines, each starts ~20-40px lower, blurred 4-8px, 0 opacity, snaps to place over 0.6-1s ease-out; on load for hero, scroll-into-view for section headings; often paired with a clip-path mask.
- MONOLOG (Awwwards SOTD Jul 2026) — https://bymonolog.com
- Ten Years Away — Studio375 — https://ten.375.studio/en
- Obys Experiment Space — https://experiment.obys.agency
Webflow: fully native and marketplace-legal — Webflow Interactions are GSAP-powered and default for Marketplace templates from May 1 2026, support char/word/line splitting with stagger, blur, transform, no embed needed. Framer: native Text Effects (Scale, Blur, Offset per character/word/line, triggered on Appear/Layer In View/Section In View) — pure UI, no code.

### Aurora/blur-morph gradient background (CSS-only WebGL impostor) — sellability 10
3-5 large radial/conic blobs in brand hues over near-black, blurred 80-150px, slow 10-20s translate/scale loop.
- Linear — https://linear.app/homepage
- Resend — https://resend.com
- Cursor — https://cursor.com
- Raycast — https://raycast.com
Webflow: absolutely-positioned divs with radial-gradient bg + blur filter, looping Interactions timeline — ships clean through marketplace review, expose blob colors as swatches. Framer: gradient-filled frames with Blur layer effect, looped via Appear/loop or Scroll Transform — fully no-code.

### Interactive Spline 3D hero — sellability 8
Spline scene (product, glass blob, iridescent shape, device) as hero centerpiece; rotates on mouse move, scroll-scrubbed animation.
- THREE DIMENSIONS — Dirk Lach (cloneable) — https://webflow.com/made-in-webflow/spline
- FlowDrinks — Diego Toda de Oliveira
- Nike 360 product landing — Zoe Tang
Webflow: native Webflow<->Spline integration (scene URL pasted into Spline element, hover/scroll interactions drive scene states) — no code embed, passes the "no custom code" rule; include swap-the-scene instructions. Framer: native Spline component (paste scene link, wire mouse/scroll in Spline's own state machine) — zero code; ship 2-3 alternate scenes since buyers edit in Spline itself.

### Film grain/noise overlay — sellability 8
Full-viewport fixed overlay of tiled monochrome noise (PNG or SVG feTurbulence) at 3-8% opacity over gradients/video/imagery.
- Awwwards texture collection — https://www.awwwards.com/websites/texture/
- Everlovin' Press (Line25 roundup) — https://line25.com/articles/20-web-designs-with-subtle-grain-texture-backgrounds/
- Osmo — https://osmo.supply
Webflow: fixed pointer-events-none div, tiled noise PNG bg at low opacity, optional 8-step background-position loop via Interactions — no code, marketplace-safe. Framer: fixed frame with noise image fill above all sections; newer Framer versions have built-in Noise texture fill.

### Scroll-scrubbed Lottie hero/diagram animation — sellability 9
Lottie (After Effects export) with playhead bound to scroll progress — diagrams assembling, lines drawing; plus micro-Lotties on icons/cards hover.
- Sentry (Rive/Lottie showcase) — https://sentry.io
- Made in Webflow Lottie/Spline demos — https://webflow.com/made-in-webflow/spline
- LottieFiles Webflow plugin gallery — https://lottiefiles.com/plugins/webflow
Webflow: dedicated Lottie element (JSON/dotLottie), Interactions panel scrubs "while scrolling in view" or plays on hover/click/load — explicitly supported, marketplace-safe. Framer: native Lottie component (URL or upload), play on appear/hover/loop; scroll-scrub needs a small code component or free community Lottie-scroll component.

### Infinite marquee + scroll-velocity text ticker — sellability 8
Full-width looping strips (logos, oversized words, thumbnails) that drift; premium version accelerates/skews with scroll velocity.
- GSAP — https://gsap.com
- TRIONN — https://trionn.com
- Osmo — https://osmo.supply
Webflow: basic infinite marquee via native looping Interactions (classic no-code pattern); velocity-reactive skew needs GSAP ScrollTrigger custom code — NOT marketplace-legal, ship constant-speed version in templates. Framer: native Ticker component ships with Framer (speed, direction, hover-pause); velocity-reactive versions exist as legal marketplace code components.

### Parallax depth stack (multi-speed scroll layers) — sellability 9
2-4 layers scrolling at different rates (bg 40-80%, fg 110-140%), slight scale-up on entry — the "deep space" feel.
- 21 Hrs On The Moon — Studio 28K — https://21hrs.space
- Vero New-York — Rodéo studio — https://verostudio.com
- Julien Calot — https://juliencalot.com
Webflow: native "while page is scrolling" Interactions with different move distances per layer, image scale-on-scroll same panel — 100% marketplace-safe, backbone of bestselling templates. Framer: native Scroll Speed effect (set layers 40%/80%/120%/140%) + Scroll Transform for scale/opacity — Framer academy teaches this exact recipe.

### Video-first hero (full-bleed autoplay loop) — sellability 8
15-30s muted autoplay quick-cut background video filling hero viewport, text overlaid, optionally scroll-pinned.
- Runway — https://runwayml.com
- Cadigal Office Leasing — https://cadigal.com.au
- Awwwards video collection — https://www.awwwards.com/websites/video/
Webflow: native Background Video element (auto-loops, muted) — marketplace-safe, add poster image for mobile autoplay blocks. Section-pinning the video needs custom code — omit for marketplace. Framer: native video fill/component (autoplay+loop+muted), combine with Scroll Transform for fade/scale-away.

### Standout tricks — motion/3D
- Unicorn Studio: no-code WebGL editor (70+ effects, fluid sims, volumetric light, 36kb runtime), one-click Framer embeds — legal in Framer templates (code/embed allowed), blocked in Webflow marketplace templates (custom-code ban) where it can only ship as an off-marketplace cloneable
- Webflow Interactions becoming GSAP-powered and default for Marketplace templates on May 1 2026 — native text-splitting/staggers/timelines make kinetic typography marketplace-legal with zero embeds
- "Baked WebGL" substitution: record a shader/fluid effect once as a 15-30s MP4 loop (native both builders) — 80% of the wow, 0% of the code risk
- Spline is the only true-3D channel native (and marketplace-safe) in BOTH Webflow and Framer — every other route (Three.js, R3F, Unicorn, Rive) fails Webflow's no-custom-code rule
- Framer's marketplace does no manual review and explicitly permits clean code components — Rive runtimes, Three.js heroes, velocity-reactive tickers all shippable there but not on Webflow
- The premium dark-site formula across Dark.design (Resend, Cursor, Warp, Fey, Osmo): near-black base + aurora gradient blobs + 4% grain + kinetic type + one marquee — four CSS-only layers reproduce a $50k agency build with no code, either builder
- Rive's engagement claim (Notion doubled engagement; Shopify Winter '24 won 2 Webbys) is a strong sales-page stat for Framer templates bundling a Rive component — always ship a Lottie fallback since Lottie has native interaction-triggerable support in both builders

Sources: awwwards.com/websites/three-js, awwwards.com/websites/webgl, dark.design, minimal.gallery, webflow.com/made-in-webflow/spline, onepagelove.com/tag/rive, framer.com/template-requirements, framer.com/marketplace/templates, rive.app/use-cases/websites, unicorn.studio, webflow.com/templates/submission-guidelines, line25.com/articles/20-web-designs-with-subtle-grain-texture-backgrounds
