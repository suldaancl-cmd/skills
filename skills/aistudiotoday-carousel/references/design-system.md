# AI Studio Today — Design System (for carousels)

Extracted from the live site (aistudiotoday.com) on 2026-06-04. These are the real tokens — use
them verbatim so every carousel reads as the brand. The CSS variables here mirror what's already
wired into `assets/carousel-template.html`.

## The brand in one breath

Dark, premium, high-contrast **AI-agency** look: a near-black **violet** canvas, a heavy
**condensed display** headline in off-white, a single **purple** accent that glows, and quiet
**dotted-grid / particle** texture. Glassmorphic dark cards carry data in mono. It feels like a
high-end product launch, not a template.

## Colors

| Token | Hex / value | Use |
|---|---|---|
| `--bg-primary` | `#0B0712` | Page + slide background (near-black violet). The default canvas. |
| `--bg-elevated` | `#150E22` | Slightly raised panels / alternate slide bg. |
| `--bg-navy` | `#0E2138` | Capsule/pill backgrounds, nav-style chips (the site's nav capsule). |
| `--card-bg` | `rgba(10,10,12,0.72)` | Glassmorphic cards (with backdrop-blur). |
| `--border` | `rgba(255,255,255,0.10)` | Hairline 1px borders on cards/pills. |
| `--text-primary` | `#F0EBFA` | Headlines + primary text (off-white lavender). |
| `--text-secondary` | `#C2B9D4` | Body copy, supporting lines. |
| `--text-muted` | `#A99FC2` | Captions, fine print, de-emphasized. |
| `--text-on-navy` | `#B8C3DC` | Text inside navy capsules. |
| `--accent` | `#8B5CF6` | **Primary** violet accent. Default for highlights, rules, glows. |
| `--accent-bright` | `#A855F7` | Brighter purple — gradient end, hover, emphasis. |
| `--accent-deep` | `#6D28D9` | Deep purple — gradient start, shadows. |
| `--gradient-brand` | `linear-gradient(120deg,#6D28D9,#8B5CF6 50%,#A855F7)` | Hero CTA, gradient text highlight, CTA slide bg. |
| `--glow-accent` | `0 0 28px rgba(139,92,246,0.28)` | Violet glow halo around accent elements. |
| `--glow-magenta` | `0 0 24px rgba(168,85,247,0.22)` | Secondary magenta glow. |

**Contrast rule:** off-white text on the near-black canvas, violet as the *single* accent. Don't
introduce other hues — restraint is what makes it premium. Highlight at most 1–2 words per headline
with `--gradient-brand` as clipped text.

## Typography

The site's signature is a **heavy, condensed, tight** display face (live stack:
`"Arial Black","Helvetica Neue Condensed Black","SF Pro Display"`). For crisp, cross-platform
carousels we load close free matches; all are swappable via CSS variables.

| Role | Font (loaded) | Fallback stack | Notes |
|---|---|---|---|
| Display / headlines | **Anton** | `"Arial Black","Helvetica Neue",sans-serif` | Condensed black poster grotesque — matches "Stop losing customers." Tight `line-height: 0.95`, `letter-spacing: -0.01em`. UPPERCASE or sentence case both work. |
| Body / UI | **Inter** | `-apple-system,"Segoe UI",sans-serif` | Matches the site's system/Inter body. Weights 400–600. |
| Mono / data | **IBM Plex Mono** | `ui-monospace,"SF Mono",monospace` | Metrics, terminal mockups, kickers/labels (uppercase + `letter-spacing: 0.08em`, in `--accent`). |

Do **not** substitute Cormorant, Outfit, JetBrains Mono, or Noto Kufi Arabic (user-banned
defaults). Anton / Inter / IBM Plex Mono are the locked picks.

**Anton quirk:** Anton's period is a solid square glyph, so a *trailing* period on a huge headline
reads as a stray block. On the biggest display lines either omit the terminal period (poster
convention) or tuck it **inside** the colored/gradient `<span>` so it reads as part of the word
(e.g. `<span class="grad">We fix that.</span>`). At ≤64px periods render fine either way.

Type scale (at 1080×1350, before the tweak-panel `--display-scale`):
- Cover headline: ~120–160px, line-height 0.92
- Body-slide headline: ~72–92px, line-height 0.95
- Supporting line: ~30–36px, line-height 1.3, `--text-secondary`
- Kicker / label (mono): ~22px, uppercase, `--accent`
- Slide index number: ~200px ghost number at low opacity behind content

## Motifs (the texture that sells "AI Studio Today")

Use 1–2 per slide, never all at once — restraint.

1. **Dot field** — scattered faint violet dots over the background (the hero's particle look).
   In the template it's a CSS radial-gradient layer with adjustable `--dot-opacity`.
2. **Dotted grid** — evenly spaced dots, used on content sections. Subtle, behind cards.
3. **Glass cards** — `--card-bg` + `backdrop-filter: blur(12px)` + `--border` + 16–24px radius +
   `--glow-accent`. House data, screenshots, quotes.
4. **Capsule / pill** — `--bg-navy` rounded-full chip with mono label. Use for "PLUGIN #1",
   "STEP 02", category tags.
5. **Gradient highlight** — `--gradient-brand` clipped onto 1–2 key words in a headline.
6. **Glow accent** — purple glow behind the focal element (number, icon, CTA).
7. **Mono data / fake terminal** — IBM Plex Mono rows of metrics or a terminal block; mirrors the
   site's live-dashboard panels. Strong for proof slides.

## Voice (copy)

Direct, punchy, **outcome-first**. Short declarative sentences. Real numbers and specifics over
adjectives. Confident, not hype-y.

On-brand examples (from the site): "Stop losing customers." · "The traffic you already have is
leaking." · "…booked customers — in 30 days, and you own all of it."

Carousel application:
- **Cover headline**: a sharp hook or a number-led promise. ("5 Claude Code plugins that actually
  ship." / "Your funnel is leaking. Here's where.")
- **Body headlines**: one idea, ≤6 words ideally.
- **Body line**: 1–2 lines of concrete value, not filler.
- **CTA**: one clear ask ("Book a free AI audit →", "Follow for the build", "Link in bio").

## Layout defaults

- Frame: 1080×1350 (4:5). Safe padding ~96px (`--slide-pad`).
- One focal element per slide; generous negative space (dark canvas is the design).
- Left-aligned headlines read strongest with this display face; center only the cover/CTA.
- Consistent footer micro-brand on body slides: small `@aistudiotoday` + dot in `--text-muted`.
