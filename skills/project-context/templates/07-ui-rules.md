# 07 — UI Rules

> `06` holds the values. This file holds the behaviour. Together they are the design system.
> Fill after the deck is approved, alongside `06`.

## The feel, in one sentence

<e.g. "Immersive modern-classic: full-bleed imagery, floating glass layers, one serif display
over one grotesk UI face." If you cannot write this sentence, the direction is not locked.>

## Layout

- Page max width: <> · gutters: <mobile / desktop>
- Grid: <columns, gap>
- Vertical rhythm: sections separated by `--s-16`, blocks by `--s-8`
- Sticky/fixed elements: <which, and their z-index>

## Typography in use

- Display face is for <headlines only / hero only>. Never body copy.
- Body copy measure: 60–75 characters. Never full-bleed text.
- Sentence case for headings and buttons. No ALL CAPS except <the one exception, if any>.
- Numbers: Latin numerals everywhere, including in Arabic blocks.

## Cards

<Surface, border, radius, padding, shadow, hover state, whether they are clickable as a whole.
Say whether cards are even the right pattern here — a flat generic card grid is the default
AI output and is banned as a first reach.>

## Buttons

| Variant | Use for | Fill | Border | Ink | Hover | Press |
|---|---|---|---|---|---|---|
| Primary | the one action on the screen | | | | | |
| Secondary | | | | | | |
| Ghost | | | | | | |
| Destructive | | | | | | |

One primary per screen. Height `<>`. Icon-only buttons need an `aria-label`.

## Forms

- Label above the field, always visible. No placeholder-as-label.
- Error text sits under the field, in `--danger`, and says what to do — not "invalid input".
- Disabled submit until valid, or submit-then-show-errors — <pick one and be consistent>.
- Every input has a focus ring that survives on `--bg` and `--surface`.

## Badges and status

<Shape, size, when a color carries meaning vs decoration.>

## Empty, loading, error states

Every list, every fetch, every screen. Three states, all designed, none default:

- **Empty:** an illustration or icon, one line of what goes here, one action to fill it.
- **Loading:** skeleton matching the real layout. Never a centered spinner on a full page.
- **Error:** what failed, what to try, a retry control.

## Imagery

<Treatment, aspect ratios, whether people appear, how AI-generated assets are handled,
where the real assets live. "Real assets, not stock placeholders" if that is the bar.>

## Iconography

<Set, weight, size steps. One set only.>

## RTL (if bilingual)

- Direction flips layout, padding, and icon direction — not the logo, not numbers, not charts.
- One direction per block. Never mix AR and EN inside a sentence.
- Test at the same optical size, not the same px.

## Accessibility floor

Contrast ≥ 4.5:1 body / 3:1 large. Keyboard reachable everything. Focus visible.
Touch targets ≥ 44px. `prefers-reduced-motion` respected. Headings in order, no skipped levels.

## Never

- Hard-coded hex, px, or font family.
- Decorative ASCII dividers, `// ---- section ----` banners, box-drawing characters in output.
- A flat generic card grid as the first answer to "how do I lay this out".
- Destroying DOM to change state — animate it, so it is reversible.
- Default fonts from the ban list.
