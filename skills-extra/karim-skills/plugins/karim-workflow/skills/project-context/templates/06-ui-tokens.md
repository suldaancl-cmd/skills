# 06 — UI Tokens

> **Do not fill this before Karim picks a deck option in `DESIGN.md`.** This file is the
> chosen option made machine-readable. Filling it early means the agent builds against a
> direction that was never approved.
>
> `premium-design-laws` overrides anything here. The default-fonts ban applies:
> no Cormorant, Outfit, JetBrains Mono, or Noto Kufi as a default pick.

Approved deck option: **<A / B / C — name>** · approved on `<date>`

## Color

```css
:root {
  /* surfaces */
  --bg:            #;
  --surface:       #;
  --surface-raised:#;
  --border:        #;

  /* ink */
  --ink:           #;   /* primary text */
  --ink-muted:     #;   /* secondary text — must hit 4.5:1 on --bg */
  --ink-inverse:   #;

  /* brand */
  --accent:        #;
  --accent-hover:  #;
  --accent-ink:    #;   /* text that sits on --accent */

  /* signal */
  --success:       #;
  --warning:       #;
  --danger:        #;
}
```

Dark mode: <same tokens re-declared under `[data-theme="dark"]` / `prefers-color-scheme`, or
"single theme, no dark mode" — say which.>

**Contrast checked:** `--ink-muted` on `--bg` = <ratio> · legal and paywall text ≥ 4.5:1.

## Type

| Token | Family | Size | Line height | Weight | Tracking |
|---|---|---|---|---|---|
| `--t-display` | | | | | |
| `--t-h1` | | | | | |
| `--t-h2` | | | | | |
| `--t-body` | | | | | |
| `--t-small` | | | | | |
| `--t-mono` | | | | | |

Families loaded: `<display face>` + `<UI face>`. Weights shipped: <only the ones used — every
extra weight is bytes>. Arabic face (if bilingual): `<face>`, and it must be tested at the same
optical size as the Latin face, not the same px.

## Spacing

4px base. `--s-1: 4px` · `--s-2: 8px` · `--s-3: 12px` · `--s-4: 16px` · `--s-6: 24px` ·
`--s-8: 32px` · `--s-12: 48px` · `--s-16: 64px`

Nothing between these steps. A one-off `13px` is a bug.

## Radius

`--r-sm:` · `--r-md:` · `--r-lg:` · `--r-full: 9999px`

## Elevation

| Token | Shadow | Used on |
|---|---|---|
| `--e-1` | | |
| `--e-2` | | |

## Motion

| Token | Duration | Easing | Used for |
|---|---|---|---|
| `--m-fast` | 150ms | | hover, press |
| `--m-base` | 250ms | | reveals, sheets |
| `--m-slow` | 400ms | | page/route |

`prefers-reduced-motion` collapses all of these to 0ms except opacity.

## Breakpoints

`sm:` · `md:` · `lg:` · `xl:`

---

**The rule:** no hard-coded hex, px, or font family anywhere in the codebase. If a value is
needed and not here, add it here first, then use it.
