# Aesthetic archetypes

Pick ONE. Commit fully. Never blend two of these in the same surface — that's where AI design fails.

Each archetype below is a full system: the typography, color, spacing, motion, and details that belong together. Cheat sheets, not recipes — adapt thoughtfully.

---

## 1. Editorial Luxury (Real estate, agencies, fashion, lifestyle, wine/spirits)

**Feel:** A Condé Nast travel spread. Expensive paper. Warm daylight.

- **Typography:** Variable serif display (Fraunces, PP Editorial New, Instrument Serif, Lyon) at massive sizes, tight tracking (`-0.02em` to `-0.04em`), compressed line-height (`0.95` to `1.05`). Body in a refined grotesk (Switzer, Geist, Sohne). Occasional italic pull-quotes.
- **Palette:** Warm creams (`#FDFBF7`, `#F5F0E8`), muted sage, terracotta, deep espresso, parchment. Near-black text (`#1A1815`) not pure black.
- **Texture:** Subtle CSS noise/film grain overlay at ~3% opacity. Hair-thin rules (`1px solid rgba(0,0,0,0.08)`).
- **Layout:** Asymmetric two-column with massive margins. Editorial pull-quotes, caption type, numbered sections. Generous white space; let headings breathe.
- **Motion:** Slow, heavy fades with blur dissolve. `cubic-bezier(0.4, 0.0, 0.2, 1)` over 800–1200ms. Minimal micro-interactions; the composition carries it.
- **Don'ts:** Gradients, neon, glassmorphism, tight 3-column grids, sans-serif display.

## 2. Ethereal Glass / Dark Luxury (SaaS, AI, fintech, agencies, night-themed)

**Feel:** Linear × Apple × a commodity trader's cinematic trailer. Deep space, glowing accents.

- **Typography:** Wide geometric grotesk display (Clash Display, Monument Extended, Geist) in medium weight, generous tracking. Body in Geist or Inter Display (Inter only in body).
- **Palette:** OLED black (`#050508`), off-black surfaces (`#0A0A0F`), one signature glow color (gold `#D4A853`, cyan `#4ECDC4`, emerald `#10B981`, violet `#8B5CF6`). Muted warm text (`#E8E4DD`).
- **Texture:** Radial mesh gradients with subtle glowing orbs in the background at low opacity. `backdrop-blur-2xl` glass cards with `1px` white/5 hairline borders and inset `0 1px 0 rgba(255,255,255,0.1)` highlights.
- **Layout:** Bento grid of varying card sizes. Floating glass nav pill detached from top. Technical framing: corner brackets, tiny eyebrow tags, measurement markers.
- **Motion:** Custom bezier (`0.32, 0.72, 0, 1`) over 600–900ms. Magnetic button hover (scale + translate of inner icon). Gentle scroll parallax. Hamburger morphs to X.
- **Don'ts:** Light backgrounds, serif display, heavy shadows, bright primaries.

## 3. Cinematic 3D / Immersive (Product launches, real estate, luxury tech)

**Feel:** An Apple product page. Each scroll is a scene transition.

- **Typography:** Massive display sizes (`clamp(4rem, 10vw, 14rem)`), negative tracking. Often serif but grotesk works. Text often over 3D or animated backgrounds.
- **Palette:** Either dark luxury (see above) or stark white-on-light with a single signature accent.
- **Core techniques:** Pinned scroll sections, scrubbed animations linked to scroll progress, horizontal scroll reveals, product objects that appear to float between sections via sticky positioning, clip-path reveals, text masks.
- **Stack:** GSAP + ScrollTrigger (see full `gsap` skill). Three.js / React Three Fiber for actual 3D objects. Spline for non-engineers. Lenis or ScrollSmoother for butter scroll (pick one; don't stack).
- **Motion choreography:** Hero sequence — 3–5 elements reveal in sequence over ~1.5s on first paint. Scroll sections feel like a film cut. `ease: "none"` for scrubbed tweens.
- **Don'ts:** Every scroll doesn't need a 3D effect. Choose 2–3 hero moments; the rest is disciplined typography and space.

## 4. Premium Utilitarian Minimalism (Notion-style, docs, productivity)

**Feel:** A document written by someone with impeccable taste.

- **Typography:** Clean geometric sans (SF Pro Display, Geist Sans, Switzer) for UI; refined serif (Lyon, Newsreader, Instrument Serif) for hero headings with tight tracking and tight line-height. Monospace (Geist Mono, JetBrains Mono) for meta and code.
- **Palette:** Pure white or warm off-white canvas (`#FFFFFF`, `#FBFBFA`). Off-black body (`#111`, `#2F3437`). Borders ultra-light (`#EAEAEA`). Accent colors are highly desaturated pastels (`#FDEBEC`, `#E1F3FE`, `#EDF3EC`) used only for semantic meaning.
- **Shadows:** Practically invisible. Max `shadow-[0_1px_2px_rgba(0,0,0,0.03)]`. No rounded-full on large containers.
- **Layout:** Flat bento grids. Content-first. Generous line-height (`1.6`). Small, precise icons.
- **Motion:** Restrained. Subtle hover lifts (`translate-y-0.5`), fades under 300ms. Motion should feel like documents being set down gently.
- **Don'ts:** Gradients, neon, glass, 3D, heavy shadows, primary-colored backgrounds, pill-shaped large cards.

## 5. Industrial Brutalist / Swiss Tactical (Data dashboards, portfolios, editorial)

**Feel:** A declassified blueprint × 1960s Swiss corporate identity × a mainframe terminal.

Two flavors — pick one, don't mix:

### 5a. Swiss Industrial Print
- **Typography:** Neue Haas Grotesk Black, Archivo Black, Monument Extended. Massive fluid scale (`clamp(4rem, 10vw, 15rem)`), negative tracking (`-0.03em` to `-0.06em`), tight leading (`0.9`). Uppercase structural headers.
- **Palette:** Newsprint off-white (`#F4F1EC`) substrate, charcoal text, primary red (`#D32F2F`) as alert/accent. Black for structural rules.
- **Layout:** Rigid modular grid with visible dividing lines. Asymmetric negative space. Viewport-bleeding oversized numerals. Everything aligned to a strict column grid.
- **Motion:** Minimal or none. Type is the subject.

### 5b. Tactical Telemetry / CRT Terminal
- **Typography:** JetBrains Mono, IBM Plex Mono, Space Mono, VT323 for CRT flavor. Generous tracking (`0.05em–0.1em`) to feel like typewriter matrices.
- **Palette:** Pure black background, phosphor green (`#33FF33`) or amber (`#FFB000`) text. One alert color (red).
- **Effects:** CSS scanlines (repeating linear gradient), text-shadow phosphor glow, occasional dithering/noise, ASCII bracket framing (`[ ]`, `> `), crosshair overlays.
- **Layout:** Dense tabular data. Everything in columns. Labels in uppercase with bracket prefixes.
- **Don'ts:** Rounded corners, soft shadows, fluid gradients. Sharp edges or nothing.

## 6. Soft Structuralism (Consumer, health, portfolios)

**Feel:** A product shot under a softbox. Clean but warm.

- **Typography:** Massive bold grotesk (Geist, Plus Jakarta Sans) for hero; refined sans or light serif for body.
- **Palette:** Silver-grey to white backgrounds. High contrast. A single warm or cool accent.
- **Shadows:** Unbelievably soft, highly diffused ambient shadows (`shadow-[0_40px_100px_-20px_rgba(0,0,0,0.12)]`). Multiple shadow layers to fake physical depth.
- **Layout:** Airy floating components. Lots of breathing room. Rounded corners but moderate (not pill).
- **Motion:** Soft spring physics (Motion library spring configs, or GSAP `back.out(1.4)`). Every element lands like a feather.

## 7. Epic Cinematic 2.5D (Awwwards, no WebGL)

**Feel:** An Apple product page built without Three.js. Depth via scroll parallax and layering.

- **Core techniques:** Sticky pinned sections. Parallax layers (background slowest, midground, foreground fastest). Horizontal scroll within vertical scroll. Clip-path reveals (`polygon(0 100%, 100% 100%, 100% 100%, 0 100%)` → `polygon(0 0, 100% 0, 100% 100%, 0 100%)`). Text that splits into lines/chars and flies in from edges. Product images that rise between sections via `position: sticky`. Curtain drops. Iris opens. Card stacks.
- **Stack:** GSAP + ScrollTrigger + SplitText + CSS `position: sticky`. No WebGL. No Three.js.
- **Typography:** Display sizes that bleed past viewport edges. Words that light up on scroll (animated `color` or `background-clip: text`).
- **Motion budget:** One big idea per section. Don't stack 5 effects; stack 2 that complement.
- **See the full `gsap` skill** for ScrollTrigger and SplitText details.

---

## How to pick

Ask what the site must *convince* the visitor of:

| Job-to-do | Archetypes that fit |
|---|---|
| Make trust & gravitas (law, finance, real estate, b2b) | Editorial Luxury, Swiss Industrial |
| Make excitement & futurism (AI, SaaS, crypto, agency) | Ethereal Glass, Cinematic 3D, Epic 2.5D |
| Make calm & intelligence (docs, productivity, dev tools) | Premium Minimalism, Soft Structuralism |
| Make raw technical credibility (data, security, ops) | Swiss Industrial, Tactical Telemetry |
| Make warmth & approachability (consumer, health, wellness) | Soft Structuralism, Editorial Luxury |

If you're genuinely stuck between two, the answer is almost always "the more restrained one" — restraint reads as confidence.
