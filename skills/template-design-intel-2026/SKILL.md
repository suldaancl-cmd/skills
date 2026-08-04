---
name: template-design-intel-2026
description: Master pattern library from a ~1244-site 2026 study of award-winning sites and bestselling Webflow/Framer templates. Invoke when designing any website, landing page, or template — tells the agent which hero, layout, scroll, color, type, and micro-interaction patterns currently sell, with real example sites and per-builder (Webflow/Framer) build notes.
---

# Template Design Intel 2026

Source: a 2026 study covering 150 hero sections, 150 layout/nav/footer systems, 110 scroll-animation sites, 112 color-palette sites, 140 typography sites, 115 micro-interaction sites, and 120 motion/3D/rich-media sites — cross-referenced against Awwwards, Dark.design, minimal.gallery, SiteInspire, Webflow's Made-in-Webflow gallery, and the Framer Marketplace's bestseller lists.

Use this skill to pick patterns BEFORE writing code for any landing page, SaaS site, portfolio, agency site, or sellable Webflow/Framer template. Full pattern dump (all 7 categories, every pattern, every trick, every source URL) is in `references/patterns-full.md` — read it when you need the complete option set or exact "how-in-Webflow/Framer" build notes beyond what's summarized here.

## Decision rules — apply in this order

1. **Pick an archetype from the hero table below FIRST.** Every sellable template starts from one dominant hero shape, not a blank canvas. Match the buyer's vertical: SaaS/dev-tool → centered-SaaS or dark-devtool hero; agency/portfolio → manifesto or oversized-typography hero; hardware/DTC → split-product hero.
2. **Pick ONE palette archetype, don't blend two.** Near-black dark-SaaS OR warm-paper editorial OR one-accent-on-dark — these are proven whole systems (see Color section). Never mix a cream editorial base with a neon SaaS accent stack.
3. **Ship the scroll/motion effects that are NATIVE in your target builder.** Marketplace legality is the constraint, not what looks cool in a showreel. Webflow marketplace = no custom code (except native GSAP-powered Interactions, marketplace-legal since May 1 2026); Framer marketplace = code components ARE allowed. If a pattern's "how_in_webflow" says "not native," it can only ship as an off-marketplace cloneable, not a submitted template.
4. **Typography: use the free-clone playbook, never a paid font.** Both marketplaces ban non-Google/non-library fonts in submitted templates. Design on Instrument Serif / Fraunces / Switzer / Space Grotesk / Inter, then list the paid "upgrade fonts" (Editorial New, Canela, Söhne, etc.) in the template docs as an upsell.
5. **Every page needs: pill/floating nav OR fullscreen overlay nav, a bento or asymmetric feature grid, a pre-footer CTA band, and an oversized-wordmark or sitemap footer.** These four are the load-bearing structure of a sellable multi-page template (see Layout section) — skipping any one reads as "unfinished" in marketplace review.
6. **Grain + one accent color + kinetic type reveal = the cheapest 3-layer "premium" signal.** Apply to any template regardless of niche: 4-8% noise overlay, one saturated accent bound to a variable, per-line/word text reveal on scroll. Near-zero cost, appears across every beat in this study.
7. **Sellability score is a build-effort-vs-buyer-appeal ratio, not raw wow.** A 10/10 pattern is native, zero-code, and universally reusable (bento grid, sticky stacking cards, near-black dark mode, kinetic text reveal). An 7-8/10 pattern demos great but needs an asset the buyer must supply (image sequence, 3D scene, custom footage) — still worth shipping, but flag the asset burden in the listing.

## Top patterns by category (highest sellability first)

### Hero sections
| Pattern | Sellability | Example | Builder note |
|---|---|---|---|
| Centered SaaS hero (pill → headline → subhead → CTA → screenshot) | 10 | Linear (linear.app), Midday (midday.ai) | Fully native both builders, IX2/Appear stagger |
| Dark dev-tool hero (near-black + glow gradients + code accent) | 10 | Resend (resend.com), Raycast (raycast.com) | Native gradients+blur both builders |
| Oversized display-typography hero | 9 | GSAP (gsap.com) | Native vw sizing; per-char split needs GSAP embed in Webflow, native in Framer |
| Agency manifesto hero (opinionated headline + stats + logos) | 9 | Hildén & Kaira (hildenkaira.fi), MONOLOG (bymonolog.com) | Zero custom code, either builder |
| Logo bar marquee under hero | 9 | Midday, Sui (sui.io) | Native marquee/Ticker both builders |
| Preloader → hero choreography | 8 | Osmo "Crisp Loading Animation" cloneable (219 clones) | Native-ish Webflow IX2; no native Framer preloader primitive |
| Split product hero | 8 | Radian Motorcycles (rideradian.com) | Native 2-col + scale-in both builders |
| Full-bleed WebGL/3D hero | 7 | Sui, EverSwap (everswap.com) | Native via Spline embed in BOTH builders — never hand-rolled Three.js in a sellable template |

### Layout, navigation, footer
| Pattern | Sellability | Example | Builder note |
|---|---|---|---|
| Bento feature grid | 10 | Linear, Supabase (supabase.com) | Native CSS Grid / Grid layout, zero code |
| Floating pill navbar, shrinks on scroll | 9 | Linear | Native Webflow (fixed div + IX2); Framer shrink-on-scroll needs a code override |
| Fullscreen overlay menu, oversized links | 9 | Klim Type Foundry (klim.co.nz), Dogstudio (dogstudio.co) | Line-stagger native both; per-character split needs GSAP embed (Webflow) or code component (Framer) |
| Oversized wordmark footer | 9 | Wix "Big Footer" trend roundup examples | Native vw heading + overflow-hidden crop, both builders |
| Pre-footer CTA band | 9 | Vercel (vercel.com), Linear | Native componentized section, both builders |
| Sitemap mega-footer + utilities row | 8 | Linear (6-col), Vercel (7-col + theme toggle) | Native grid/stack; real dark-mode toggle needs code override in both |
| Two-panel/tabbed mega menu | 8 | Segment (segment.com), Qualtrics (qualtrics.com) | Native in Webflow (Tabs inside Dropdown); Framer has no mega-menu primitive — genuine differentiator if built |
| Editorial asymmetric/broken grid | 7 | STAGECREW (stagecrew.studio), Gusta (gusta.studio) | Native Grid column-span (Webflow) more robust than Framer's absolute-position approach |

### Scroll animation
| Pattern | Sellability | Example | Builder note |
|---|---|---|---|
| Sticky stacking cards | 10 | Framer "Sticky Overlap" component ($12) | Native `position: sticky` + IX2/Scroll Transform, both builders |
| Scroll-scrubbed text reveal (line/word/char) | 10 | YesNo (yesnowww.com), Blux Studio (bluxstudio.com) | Native Framer Text Effects; Webflow needs GSAP SplitText embed (now free) |
| Pinned section with content swap (scrollytelling tour) | 9 | Quoti (getquoti.ai) | Native sticky-media-column + IX2/Scroll Variant, both builders |
| Zoom-scrub media hero (framed → full-bleed) | 9 | Apple Oct 2020 remake (Webflow cloneable) | Native sticky + scale transform, both builders |
| Section wipes / curtain overlaps | 9 | Petralithe (petralithe.com/en) | Native `position: sticky` + z-index stacking, both builders |
| Horizontal scroll driven by vertical scroll | 8 | Theo (theo.be), Canals Amsterdam | Native-ish Webflow (IX2 or GSAP ScrollTrigger); needs code component in Framer |
| Multi-layer parallax hero | 8 | Firewatch parallax (fire-watch-parallax.webflow.io) | Fully native both — most-cloned interaction in Webflow |
| Scroll-scrubbed video/image-sequence | 7 | Chanel J12 (chanel.com), Ray-Ban Meta | Custom code required in both — flag asset burden (100-150 frame sequence) |

### Color and gradients
| Pattern | Sellability | Example | Hex/notes |
|---|---|---|---|
| Near-black SaaS dark mode (never pure #000) | 10 | Linear #08090A, Stripe #181818 | Text off-white #E2E4E7, not #FFF |
| Aurora/mesh gradient hero | 10 | Stripe, Linear, Vercel | 3-4 analogous hues, 80-90% opacity, blurred corners; native both builders |
| Monochrome dark + one acid accent | 10 | Lando Norris landonorris.com — lime #D2FF00 on #101400 (tinted black) | Tint the black toward the accent hue |
| Warm off-white editorial base (never pure #FFF) | 9 | Aristotle heyaristotle.com #F0ECE0, Gusta #F9F7F2 | Pair with warm charcoal text, not pure black |
| Layered deep-purple glow stack | 9 | Raycast raycast.com — #330381/#523091/#550062/#1A0B33/#070D4F | 3-4 blurred radial-gradient divs, filter:blur(120px) |
| Grain/noise overlay on gradients | 8 | Grainient (grainient.supply) | 4-8% opacity, mix-blend-mode:overlay |
| Functional multi-accent set on dark | 7 | Linear — indigo #4354B8, orange #E5591D, pink #F79CE0 | Accents live only in feature/bento sections, never chrome |
| Paper + muted retro brights | 6 | Don't Board Me dontboardme.com — #A7A238/#E33529/#FFF500/#854720/#2B6786 on #F3F3E9 | Flat blocks only, never gradient-blend these hues |

### Typography
| Pattern | Sellability | Example | Free-clone pairing |
|---|---|---|---|
| Masked per-line kinetic reveal on load | 10 | Framer "Text Reveal Animated" component | Native Framer Text Effects; Webflow needs GSAP SplitText (free) embed |
| Editorial serif display + neutral grotesk body | 10 | Elena Scott = Editorial Old + Neue Montreal; Every (every.to) = Signifier + Switzer | Clone: Instrument Serif/Fraunces + Inter/Switzer |
| Monospace eyebrow/label layer | 9 | Speakeasy = Diatype + Diatype Mono | Clone: DM Sans + DM Mono |
| Italic serif accent word in sans headline | 9 | Readymag (readymag.com) | Instrument Serif Italic is the template-world default |
| Oversized full-bleed hero type ("Wide & Loud") | 9 | MONOLOG, Charles Leclerc site | Framer's "Fit" text-sizing toggle purpose-built for this |
| Single neo-grotesk system (Inter economy) | 8 | Stripe, Novastyle Webflow template | Safest rebrand story: one font swap |
| Quiet-luxury high-contrast serif | 8 | Heart & Soil (heartandsoil.co) = Cardinal + Sweet Sans | Clone: Fraunces (variable SOFT/WONK axes) |
| Scroll-scrubbed word-by-word text | 8 | Apple marketing pages, Linear | Needs GSAP ScrollTrigger scrub (Webflow) or Motion useScroll (Framer) |

### Micro-interactions
| Pattern | Sellability | Example | Builder note |
|---|---|---|---|
| Overflow-clip hover zoom + caption slide-up on cards | 10 | Pesquera Diez (pesqueradiez.com) | Fully native IX2/variant hover, both builders |
| Cursor-following image/video preview on hover list | 9 | Gianluca Gradogna (gianlucagradogna.com) | Native-ish Webflow (IX2 mouse-move); Framer needs code override |
| Marquee/ticker with hover-pause | 9 | Off+Brand free Webflow+GSAP template | Native Framer Ticker component; Webflow = CSS keyframe embed |
| Blend-mode dot cursor with hover morph | 8 | Waaarhol (waaarhol.com) | Native Framer Cursors feature; Webflow needs small CSS embed for blend-mode |
| Full-screen wipe/mask page transitions | 8 | Amaterasu (amaterasu.ai) | Partial-native Framer page transitions; Webflow needs overlay-trick or Barba.js embed |
| Counter/curtain preloader with content reveal | 7 | Grégory Lallé (gregorylalle.com) | Mostly native Webflow IX2; Framer has no native preloader primitive |
| Magnetic buttons/nav links | 7 | Codrops canonical demo (tympanus.net) | Not native in either — needs JS/code override in both |
| Animated link underlines (draw-through, exit-right) | 8 | FreeFrontend CSS collection | CSS embed (Webflow) or component variant (Framer); exit-right origin-swap needs custom CSS in both |

### Motion, 3D, rich media
| Pattern | Sellability | Example | Builder note |
|---|---|---|---|
| Kinetic typography reveal (blur+offset stagger) | 10 | MONOLOG (bymonolog.com) | Native Webflow GSAP-powered Interactions (marketplace-legal since May 1 2026); native Framer Text Effects |
| Aurora/blur-morph gradient background | 10 | Linear, Resend, Cursor (cursor.com) | Fully native both, zero code — the CSS-only WebGL impostor |
| Interactive Spline 3D hero | 8 | THREE DIMENSIONS cloneable (Made in Webflow) | THE marketplace-safe true-3D path in both builders |
| Film grain/noise overlay | 8 | Dark.design gallery norm | Native fixed-div overlay, both builders |
| Scroll-scrubbed Lottie hero/diagram | 9 | Sentry-style Lottie showcase | Native Lottie element both; scroll-scrub needs code component in Framer |
| Infinite marquee + velocity ticker | 8 | GSAP.com, TRIONN (trionn.com) | Constant-speed = native; velocity-reactive = code-only, not Webflow-marketplace-legal |
| Parallax depth stack | 9 | 21 Hrs On The Moon (21hrs.space) | Native Scroll Speed effect (Framer) / "while scrolling" IX2 (Webflow) |
| Video-first hero (autoplay loop) | 8 | Runway (runwayml.com) | Native Background Video / video component, both builders |

## Marketplace-legality cheat sheet

- **Webflow templates**: no custom code embeds allowed on submission (except native GSAP-powered Interactions as of May 1 2026). Anything marked "not native" above (magnetic buttons, velocity-reactive marquees, mega-menu-style Framer gaps, scroll-scrubbed video) can only ship as a free cloneable, not a paid marketplace template.
- **Framer templates**: no manual review; clean code components ARE permitted. This is the arbitrage — if a pattern needs real code (Unicorn Studio WebGL, Rive, magnetic buttons, cursor-follow previews), build it Framer-first.
- **Fonts**: Google/OFL only (Webflow) or Framer's built-in library/Google fonts only (Framer) — no paid customs in either. See the Typography free-clone pairings table above.
- Full "how_in_webflow" / "how_in_framer" build notes for every pattern (exact CSS properties, panel names, plugin names) are in `references/patterns-full.md`.

## Full reference

`references/patterns-full.md` — complete pattern dump: all 60 patterns across 7 categories with full "what/why/example_sites/how_in_webflow/how_in_framer" fields, plus every "standout trick" (70+ one-off techniques with source sites) and the full source-URL list per category.
