# Anti-patterns — what generic AI design does that great design doesn't

If any of these appear in your output without a deliberate reason, the design reads as AI-generated. Treat this as a pre-ship checklist.

## Typography anti-patterns

- **Inter / Roboto / Open Sans / Arial as display type.** Fine as body in moderation; as a hero font, instantly reads as default.
- **System UI stack everywhere.** No voice, no craft.
- **Single font family, single weight.** No hierarchy, no contrast.
- **Same exact font pairing as every other AI page** (Space Grotesk + Inter is the current cliché).
- **All-caps in body copy.** Reads as shouting, hurts scanability.
- **Line length > 90 characters.** Fatigues readers.
- **Line height 1.0 on body text.** Breathable body needs 1.5–1.7.
- **Tracking 0 on massive display type.** Large type needs negative tracking.

## Color anti-patterns

- **Purple-to-pink gradient on white background.** The single most overused AI hero aesthetic.
- **Neon green / acid yellow on black** applied without a brand reason.
- **Every section a different background color.** Confetti, not design.
- **Accent color used for every button AND every heading AND every icon.** Loses all meaning.
- **Pure black `#000` on pure white `#FFF` for body.** Feels sterile; use off-black on near-white.
- **Low-contrast gray-on-gray** that fails WCAG AA.
- **7 competing brand colors.** Pick 2–3.

## Layout anti-patterns

- **Centered-everything.** Every heading, every paragraph, every CTA. Asymmetry creates visual interest.
- **Identical 3-column card grid** for every section.
- **"Follow these 3 steps" / "Why choose us" / "Our features" generic sections** with the same structure everywhere.
- **Edge-to-edge sticky nav glued to viewport top** with no personality.
- **Full-viewport hero with just a headline + button + photo in the corner.** Default. Do something.
- **No whitespace.** Premium feels spacious; `py-8` sections read as cheap. Use `py-24`+.
- **Aspect-ratio-ignored images** that distort on resize.

## Component anti-patterns

- **Pill-shaped primary buttons on luxury/editorial sites.** Wrong register.
- **Harsh drop shadows** (`shadow-lg`, `shadow-xl`) with high opacity on cards.
- **1px solid gray borders** as the default container outline. Use hairline `rgba(0,0,0,0.06)` or no border with differentiated background.
- **Cards with flat backgrounds, flat borders, flat shadows, and no internal hierarchy.** Nothing about them feels considered.
- **Icons pasted into buttons without containers.** See "Double-bezel" in `aesthetics.md` → Ethereal Glass.
- **Form inputs with no focus style.** Or with the default browser ring.
- **Disabled states that look active.** Opacity 0.5 with same colors = confusing.
- **Loading spinners** when a skeleton or progress bar would be clearer.

## Motion anti-patterns

- **`transition: all ease-in-out`.** The AI default. Specify properties; use custom beziers.
- **Every element has a scroll-reveal.** Loses meaning; use 2–3 hero moments.
- **Scroll-linked everything.** Cluttered, nauseating.
- **Parallax on the entire page.** Subtle parallax on one element; obvious parallax on the whole site.
- **Fade-in from `opacity: 0` alone** with no translate. Feels ghostly.
- **Animation-duration 200ms on a big hero reveal.** Too fast.
- **Animation-duration 1500ms on a button hover.** Too slow; hover should feel instant.
- **No `prefers-reduced-motion` honored.** Accessibility failure.
- **Motion on `width` / `height` / `top` / `left`.** Layout thrash.

## Copy anti-patterns

- **"Transform your X."** What business isn't claiming to transform?
- **"Seamless", "unlock", "unleash", "supercharge", "revolutionize", "elevate", "next-gen", "cutting-edge", "game-changer", "delve".** Banned.
- **"We believe..." / "Our mission..."** No one came to your site to learn what you believe.
- **Passive voice everywhere.** "Our platform is used by..." → "Teams at X and Y use [product]."
- **Stacked adjectives.** "Powerful, intuitive, seamless" = powerful, intuitive, seamless nothing.
- **Buzzwords as proof.** "AI-powered" in 2026 is baseline, not a differentiator.
- **Lorem ipsum / Acme Corp / John Doe.** Write real content or ask for it.
- **"Learn more" as CTA.** Learn WHAT? Be specific.
- **"Click here" as link text.** Tell me where.
- **Emoji bullets in headings.** Low-register for premium product.

## Content anti-patterns

- **Feature list as hero.** Users aren't shopping features; they're shopping outcomes.
- **Abstract value propositions** without examples.
- **Testimonials with no photo, no company, no specificity.** "Great product!" — Anonymous. Means nothing.
- **Pricing hidden behind "Contact us".** Fine for enterprise tier; not for primary plan.
- **Stats without source.** "40% faster" — than what, measured how?
- **Fake urgency.** "Only 3 spots left!" on a SaaS product.
- **Cookie banner blocking the fold.** Bad.

## Accessibility anti-patterns

- **Low-contrast body text** (gray on gray, < 4.5:1).
- **Placeholder as label.** Disappears on type, no SR announcement.
- **Links with no underline** and contrast ratio < 3:1 against body text.
- **Focus indicator removed globally** (`outline: 0`).
- **Modal without focus trap.**
- **Click-only interactions** that don't work on keyboard.
- **Icon buttons with no `aria-label`.**
- **Auto-playing video with sound.**
- **Parallax without a reduce-motion fallback.**
- **Images with no `alt`, or decorative images with meaningful alt.**

## Performance anti-patterns

- **50MB of images on a landing page.** Compress, use modern formats (AVIF/WebP).
- **Google Fonts via `<link>` with no preconnect.** Slows LCP.
- **Render-blocking JS in `<head>`.** Move below or defer.
- **Huge React bundles for marketing pages.** Use Astro or SSG; ship HTML.
- **100+ ScrollTrigger instances** on a long page. Batch.
- **Video on mobile with autoplay + sound.** Drain + annoyance.

## Structural anti-patterns

- **8+ items in primary nav.** IA failure.
- **Footer with every link in alphabetical order** rather than grouped.
- **Homepage tries to serve 5 audiences.** Pick the primary; others get their own page.
- **CTA button says 3 different things** on the same page.
- **Multiple competing CTAs in the hero.** Pick one primary, one secondary max.
- **"Trusted by" logo row with only 2 logos** or fake/illegible ones.

## The pre-ship checklist

Before calling a design "done", scan for:

1. Typography — distinctive display + refined body? Not Inter/Roboto?
2. Color — palette committed to? Accent used scarcely?
3. Layout — at least one asymmetric / bento / distinctive composition?
4. Components — tokens applied? Shadows soft? Radii consistent?
5. Motion — custom beziers? 2–3 hero moments, not 20?
6. Copy — specific? Active voice? No banned buzzwords?
7. Content — real, contextual? No lorem ipsum?
8. Accessibility — contrast, keyboard, focus, reduced motion?
9. Performance — assets compressed? Fonts preloaded? JS deferred?
10. Mobile — tested at 375px? Touch targets ≥ 44px?

If any answer is "no" without a deliberate reason, fix it before shipping.

## The meta test

Screenshot your design. Put it in a grid with 20 AI-generated landing pages from Midjourney / Claude / GPT. Could a designer friend spot yours as different? If no, you're converging on the mean. Commit harder to your aesthetic direction.
