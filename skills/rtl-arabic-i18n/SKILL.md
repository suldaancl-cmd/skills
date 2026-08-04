---
name: rtl-arabic-i18n
description: Use when building or auditing websites for Arabic / Hebrew / Persian / Urdu audiences — RTL layout, bilingual switching, Arabic-aware typography, logical CSS properties, GSAP/Motion direction flipping, icon mirroring, and Next.js i18n routing. Triggers — "Arabic website", "RTL site", "بالعربي", "right-to-left layout", "rtl tailwind", "bilingual English Arabic", "i18n next.js", "next-intl", "i18next", "dir=rtl", "logical properties", "Arabic typography", "خط عربي".
---

# RTL + Arabic i18n — bilingual web that doesn't break

Most "Arabic version" web builds break in 5 predictable places: text alignment, icon direction, GSAP transforms, gradient angles, and `margin-left` everywhere. This skill teaches the cure: **logical CSS properties + dir-aware layout + Arabic-tuned typography**.

Karim works Arabic-first; this skill exists so a Tailwind/Next stack doesn't fight him on every project.

## When to reach for this

- Building any UI that targets Arabic / Hebrew / Persian / Urdu audiences (RTL languages)
- Bilingual landing pages (Arabic + English with a language switcher)
- Adding Arabic to an existing English-only site without rebuilding
- Debugging a GSAP scroll-scrub that "scrolls backwards" in RTL
- Picking Arabic fonts (most "Arabic fallback" font stacks ship broken)

**Do NOT use** for purely English sites — RTL retrofitting on a finished English-only design costs more than building bilingual from day one.

## The two layout strategies

### Strategy A — Logical properties (Tailwind v4 / modern CSS)

Replace direction-specific properties with **logical** ones. They flip automatically based on `dir`.

| Don't use (physical) | Use (logical) |
|---|---|
| `margin-left`, `ml-4` | `margin-inline-start`, `ms-4` |
| `margin-right`, `mr-4` | `margin-inline-end`, `me-4` |
| `padding-left`, `pl-2` | `padding-inline-start`, `ps-2` |
| `left-0`, `right-0` | `inset-inline-start-0`, `inset-inline-end-0` |
| `text-left`, `text-right` | `text-start`, `text-end` |
| `border-l`, `border-r` | `border-s`, `border-e` |
| `rounded-tl-md` | `rounded-ss-md` (start-start) |
| `float: left/right` | `float: inline-start/end` |

**Tailwind v4** ships these by default (`ms-*`, `me-*`, `ps-*`, `pe-*`, `text-start`, `border-s`, `rounded-ss-md`, …). For Tailwind v3, add the `@tailwindcss/logical` plugin or rely on `rtl:` variants.

```jsx
// Works in BOTH directions, no rtl: variant needed
<div className="ms-4 ps-2 border-s text-start rounded-ss-md">…</div>
```

### Strategy B — `rtl:` variant (Tailwind v3, legacy)

```bash
npm install tailwindcss-rtl
```

```js
// tailwind.config.js
module.exports = { plugins: [require('tailwindcss-rtl')] };
```

```jsx
<div className="ml-4 rtl:ml-0 rtl:mr-4">…</div>
```

Verbose. Use Strategy A when possible.

## Setting direction at the root

Vanilla:
```html
<html lang="ar" dir="rtl">
```

Bilingual app with switcher (React):
```jsx
function RootLayout({ children, locale }) {
  return (
    <html lang={locale} dir={locale === 'ar' ? 'rtl' : 'ltr'}>
      <body>{children}</body>
    </html>
  );
}
```

Per-section direction (mix RTL and LTR on one page):
```html
<section dir="rtl">
  <p>هذا النص بالعربية. Then <span dir="ltr">latin tokens</span> are framed correctly.</p>
</section>
```

Per Karim's rule (`feedback_arabic_english_format`): never mix LTR/RTL mid-sentence; wrap technical tokens with `<code>` or `<span dir="ltr">`.

## Arabic typography — fonts that don't suck

Most "Arabic fallback" advice is wrong. The top tier (free, web-ready):

| Font | Style | Use |
|---|---|---|
| **IBM Plex Sans Arabic** | Modern sans, IBM Plex pair | Default body — pairs with English IBM Plex Sans seamlessly |
| **Tajawal** | Geometric sans, Google Fonts | Friendly, marketing |
| **Cairo** | Modern sans, Google Fonts | Default for Karim's existing sites |
| **Noto Sans Arabic** | System-safe, Google Fonts | Fallback / data tables |
| **Rubik (Arabic)** | Rounded geometric | Playful brands |
| **Amiri** | Naskh-style serif | Editorial / Quran-adjacent content |
| **Reem Kufi** | Display Kufi | Logos / large headings |

**Pairing strategy:**
```css
/* English display */
font-family: 'Plus Jakarta Sans', 'IBM Plex Sans Arabic', sans-serif;
/* Arabic display */
font-family: 'IBM Plex Sans Arabic', 'Plus Jakarta Sans', sans-serif;
```

Loading via `@fontsource`:
```bash
npm install @fontsource-variable/ibm-plex-sans-arabic @fontsource-variable/plus-jakarta-sans
```

```js
import '@fontsource-variable/ibm-plex-sans-arabic';
import '@fontsource-variable/plus-jakarta-sans';
```

**Critical:** Arabic font sizes feel ~10-15% smaller than Latin at same px. Bump up:
```css
:lang(ar) { font-size: 1.075em; line-height: 1.7; }
```

Arabic `line-height` should be looser than English (1.6-1.8 vs 1.4-1.5) because diacritics and tall letters need vertical room.

## Icon mirroring — what flips, what doesn't

Direction matters per icon's **meaning**:

| Icon | Action |
|---|---|
| Chevron / arrow indicating "next page" | **Flip** — points opposite in RTL |
| Back-arrow | **Flip** |
| Send / forward arrow | **Flip** |
| Quote mark | Often flip |
| Search 🔍 (magnifying glass) | **Don't flip** — universal symbol |
| Email envelope, phone, share | **Don't flip** |
| Logos | **Never flip** |
| Time-flow (timeline progress) | **Flip** — past on right in RTL |
| Numbers in price/data | **Don't flip** — digits remain LTR |

```jsx
<ChevronRight className="rtl:rotate-180" />     // flips for RTL
<MagnifyingGlass />                              // unchanged
<Logo />                                         // unchanged
```

Or with logical CSS:
```css
[dir="rtl"] .icon-directional { transform: scaleX(-1); }
```

## GSAP / Motion direction-flip gotchas

The biggest landmine. In RTL, `x: 100` moves **right** but visually looks like "advancing forward" reverses.

```js
// WRONG: this slides "forward" in LTR but "backward" in RTL
gsap.from('.card', { x: -50, opacity: 0 });

// RIGHT: read the dir, flip the sign
const isRTL = document.documentElement.dir === 'rtl';
gsap.from('.card', { x: isRTL ? 50 : -50, opacity: 0 });
```

Helper:
```js
const dirX = (v) => document.documentElement.dir === 'rtl' ? -v : v;
gsap.from('.card', { x: dirX(-50), opacity: 0 });
```

For Motion / Framer Motion:
```jsx
const isRTL = useIsRTL();
<motion.div initial={{ x: isRTL ? 50 : -50 }} animate={{ x: 0 }} />
```

ScrollTrigger horizontal pin: in RTL, the page scrolls **right-to-left**. Your `start: 'left top'` becomes `start: 'right top'`. Use `gsap.utils.normalizeScroll()` or test both directions before shipping.

## Gradient angles & shadows

CSS `linear-gradient(to right, ...)` becomes "to the right" regardless of `dir`. To mirror with direction:
```css
background: linear-gradient(to right, #000, #fff);          /* same in RTL */
background: linear-gradient(to inline-end, #000, #fff);     /* flips in RTL */
```

Box-shadow offsets:
```css
/* Physical (doesn't flip) */
box-shadow: 4px 0 10px rgba(0,0,0,.1);

/* Logical equivalent — manual swap or use CSS variables */
[dir="rtl"] .card { box-shadow: -4px 0 10px rgba(0,0,0,.1); }
```

## i18n routing — Next.js 14+ (App Router)

The canonical pick: **next-intl** (lighter, App-Router-native). Alternative: **next-i18next** (legacy Pages Router).

```bash
npm install next-intl
```

```ts
// middleware.ts
import createMiddleware from 'next-intl/middleware';
export default createMiddleware({
  locales: ['en', 'ar'],
  defaultLocale: 'en',
  localePrefix: 'always',  // /en/about, /ar/about
});
export const config = { matcher: ['/((?!api|_next|.*\\..*).*)'] };
```

```jsx
// app/[locale]/layout.tsx
import { NextIntlClientProvider } from 'next-intl';
import { getMessages } from 'next-intl/server';

export default async function LocaleLayout({ children, params: { locale } }) {
  const messages = await getMessages();
  return (
    <html lang={locale} dir={locale === 'ar' ? 'rtl' : 'ltr'}>
      <body>
        <NextIntlClientProvider messages={messages}>{children}</NextIntlClientProvider>
      </body>
    </html>
  );
}
```

```jsx
// app/[locale]/page.tsx
import { useTranslations } from 'next-intl';

export default function Home() {
  const t = useTranslations('Home');
  return <h1>{t('title')}</h1>;
}
```

```json
// messages/en.json
{ "Home": { "title": "Welcome" } }
// messages/ar.json
{ "Home": { "title": "أهلاً وسهلاً" } }
```

## i18n strategies — full coverage of patterns

| Approach | Where it lives | When |
|---|---|---|
| `next-intl` | App Router | Default for new Next.js |
| `next-i18next` | Pages Router | Legacy projects |
| `react-i18next` | Any React | Non-Next React apps |
| `vue-i18n` | Vue | Vue apps |
| `formatjs` + ICU | Any | Complex pluralization (Arabic has 6 plural forms vs 2 in English) |
| Manual `dir` toggle + dictionary | Static sites | Single landing page, no framework |

## Arabic pluralization — the 6-form trap

English plural: `1 file` / `0+ files`. Arabic plural: 6 forms based on count.

```js
// Wrong: English-style 2-form check
const label = count === 1 ? 'ملف' : 'ملفات';

// Right: explicit Arabic 6-form mapping with Intl.PluralRules
const pr = new Intl.PluralRules('ar');
const forms = {
  zero:  'لا ملفات',       // 0
  one:   'ملف واحد',       // 1
  two:   'ملفان',          // 2
  few:   `${count} ملفات`,  // 3-10
  many:  `${count} ملفاً`,  // 11-99
  other: `${count} ملف`,    // 100, 200, 1000+ (and fractions)
};
const label = forms[pr.select(count)];
```

**Strongly prefer ICU via `next-intl` / `formatjs`** — it handles all 6 forms declaratively:
```json
{ "files": "{count, plural, zero {لا ملفات} one {ملف واحد} two {ملفان} few {# ملفات} many {# ملفاً} other {# ملف}}" }
```
```jsx
const t = useTranslations();
t('files', { count: 5 });
```
Don't roll your own — the JS object above is correct but easy to fork wrong across hundreds of strings.

## Numbers, dates, currency

- **Numbers**: Arabic-Indic (٠١٢٣٤٥٦٧٨٩) vs Latin (0123456789). Most Arab UIs in 2026 use Latin digits. Use `Intl.NumberFormat('ar-EG')` if you want Arabic-Indic
- **Dates**: `Intl.DateTimeFormat('ar', { calendar: 'gregory' })` for Gregorian; `'islamic'` for Hijri
- **Currency**: `new Intl.NumberFormat('ar-SA', { style: 'currency', currency: 'SAR' })` produces `١٬٢٣٤٫٥٦ ر.س.`

## Bidirectional text — embedding LTR inside RTL

When Arabic content contains English/code/URLs:
```html
<p>اذهب إلى <span dir="ltr">github.com/karim</span> للمزيد</p>
```

Or Unicode bidi controls:
- `&lrm;` (LRM, U+200E) — left-to-right mark
- `&rlm;` (RLM, U+200F) — right-to-left mark
- `&#x202A;` ... `&#x202C;` — LRE … PDF (embedding)

For inline code in markdown/MDX, the Tailwind `font-mono` class + `dir="ltr"` on the `<code>` element solves 99% of cases.

## Common patterns

### Language switcher
```jsx
'use client';
import { useRouter, usePathname } from 'next/navigation';

export function LangSwitcher({ locale }) {
  const router = useRouter();
  const pathname = usePathname();
  const newLocale = locale === 'en' ? 'ar' : 'en';
  const newPath = pathname.replace(`/${locale}`, `/${newLocale}`);
  return (
    <button onClick={() => router.push(newPath)} lang={newLocale}>
      {newLocale === 'ar' ? 'العربية' : 'English'}
    </button>
  );
}
```

### Detect direction in a component
```jsx
import { useEffect, useState } from 'react';

export function useIsRTL() {
  const [isRTL, setIsRTL] = useState(false);
  useEffect(() => {
    setIsRTL(document.documentElement.dir === 'rtl');
  }, []);
  return isRTL;
}
```

### Bilingual layout block (one direction per block per Karim's rule)
```jsx
<>
  <section dir="ltr" lang="en"><EnglishContent /></section>
  <section dir="rtl" lang="ar"><ArabicContent /></section>
</>
```

Never mix mid-sentence — wrap whole blocks.

## Audit checklist for "Arabic-ize an existing English site"

1. Add `dir="rtl"` to `<html>` when locale is ar — verify everything flips visually
2. Find every `ml-`, `mr-`, `pl-`, `pr-`, `text-left/right`, `border-l/r` → swap to logical (`ms-`, `me-`, `text-start/end`, `border-s/e`)
3. Audit icons: `Chevron`, `Arrow`, back/forward — add `rtl:rotate-180` or directional variants
4. GSAP/Motion: every `x:` value with `-` → use `dirX()` helper
5. Gradients with `to right` / `to left` → switch to `to inline-end` / `to inline-start`
6. Box-shadows with `+x` offsets → add `[dir=rtl]` override
7. Test scroll-linked hero in both directions — pinned + scrubbed sections break first
8. Numbers in cards/tables → confirm Latin digits render in RTL (they should — bidi handles it)
9. URL slugs: keep English (`/about`) or transliterate (`/من-نحن`)? Decide before launch
10. Fonts: confirm Arabic glyphs render — open in Chrome dev tools, check `font-family` resolved value on Arabic text

## Quick decision guide

| Need | Reach for |
|---|---|
| Greenfield bilingual app | Tailwind v4 + logical props + next-intl |
| Add Arabic to existing English site | `tailwindcss-rtl` + audit checklist above |
| Static page with toggle | Manual `dir` + 2 JSON dictionaries |
| Complex pluralization (countdown timers, item counts) | `Intl.PluralRules` or `formatjs` |
| GSAP scroll-scrub that breaks in RTL | `dirX()` helper + test both directions |
| Arabic-only site | Single `dir="rtl"`, skip switcher overhead |

## Related

`tailwind` (Tailwind v4 logical props), `frontend-design`, `senior-frontend` (Next.js routing + i18n architecture), `gsap` (transform-direction handling), `feedback_arabic_english_format` (Karim's bilingual layout rule — never mix mid-sentence), `feedback_arabic_first` (content-side language preferences).
