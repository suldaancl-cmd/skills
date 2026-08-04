---
name: hyliox-landing
description: Build a one-shot cinematic landing page in the hyliox / "Claude Design" style — Vite + React 18 + TypeScript + Tailwind v4 + shadcn/ui (button, accordion) + Framer Motion (motion/react) + lucide-react + @fontsource. Signature interaction is an Apple AirPods Pro-style scroll-scrub canvas hero (240 JPG/WebP frames swapped on scroll, NOT a <video> tag). Default warm luxury palette (ochre/cream/ink/terra) on a dark theme. Nine sections: Navbar pill / Hero (250vh sticky) / ServicesBento / Pourquoi (why-us) / Process / Stats band / Testimonials marquee / FAQ accordion / CTA + Footer cinématique. Use this skill whenever the user asks for a "hyliox" landing page, mentions @hyliox / hyliox.co reels, asks for a "Claude Design" template build, or describes wanting a cinematic / editorial / AirPods-style / liquid-glass / scroll-scrub / warm-luxury landing page. Also trigger on prompts like "ABP-style site", "moving company landing page", "Vite Tailwind v4 shadcn cinematic site", "scroll-scrubbed video hero", "ScrubSequence component", or any French Swiss luxury moving / fashion / SaaS site that should feel editorial and premium. Walk the user through filling 32 placeholders, the ffmpeg frame pipeline, project bootstrap, and section-by-section build.
---

# Hyliox Landing — Cinematic One-Shot Template

This skill wraps the full hyliox "Claude Design" mega-prompt — the same template the user receives when DM'ing "WORK" to **@hyliox** on Instagram. The mega-prompt produces a Vite + React + Tailwind v4 + shadcn site with a scroll-scrubbed canvas hero in the spirit of Apple's AirPods Pro page.

The full 1,106-line source is in **`references/mega-prompt.md`**. Do NOT paste it inline — it's massive. Read it section-by-section as you build, and keep the user's filled placeholders + brand brief in working memory.

## When to Build vs. Decline

Build with this skill when:
- User asks for a hyliox-style or "Claude Design" landing page explicitly
- User describes a cinematic / editorial / liquid-glass / scroll-scrub site for a luxury, real-estate, moving, fashion, SaaS, or agency brand
- User shows a hyliox/reel screenshot and asks for "the same thing"

Decline (and route to a different skill) when:
- User wants a generic dashboard, admin panel, or data-heavy app — the template is editorial-marketing, not utility
- User wants a Next.js site — the template is Vite-only and §24 explicitly forbids substituting Next.js
- User wants 3D / Spline / Three.js as the hero (use `3d-animation-web-designer` instead — many hyliox reels use that pattern, but the *template* the user receives via DM is scroll-scrub canvas, not 3D)

## Workflow

The build has four phases. Move through them in order and don't skip placeholder collection — the mega-prompt's anti-slop guardrails (§22) will misfire if placeholders are unfilled.

### Phase 1 — Brief + placeholders

Read `references/placeholders.md` and walk the user through the 32 placeholders. Don't ask all 32 at once — that's overwhelming. Instead, ask in batches grouped by purpose:

1. **Brand identity** (5 q): `BRAND_NAME`, `BRAND_TAGLINE`, `LANG` (BCP-47), `LOGO_PATH`, `COPYRIGHT`
2. **Palette + fonts** (6 q): `COLOR_INK`, `COLOR_CREAM`, `COLOR_OCHRE`, `COLOR_TERRA` (HSL triplets, no `hsl()` wrapper), `FONT_DISPLAY`, `FONT_BODY` (Google Fonts family names)
3. **Hero** (5 q): `HERO_HEADLINE` (2-5 words, will be uppercased), `HERO_SUB`, `HERO_CTA_PRIMARY`, `HERO_CTA_SECONDARY`, `PARTNERS` (5-6 trust-logo strings)
4. **Sections content** — the heavy lift. Get from the user:
   - `SERVICES` — array of 6 `{icon, title, body}` (icon names from lucide-react)
   - `REASONS` — array of 4 `{icon, title, body}` (why-us pillars)
   - `PROCESS_STEPS` — array of 3-4 `{n, title, body}`
   - `STATS` — array of exactly 4 `{value, label}`
   - `TESTIMONIALS` — array of ≥6 `{quote, name, role}`
   - `FAQ_ITEMS` — array of 5-8 `{q, a}`
5. **Closing** (4 q): `CTA_HEADLINE`, `CTA_SUB`, `CTA_LABEL`, `FOOTER_LINKS`
6. **Frame pipeline** (3 q): `FRAMES_PATH` (default `/frames`), `FRAME_COUNT` (set after extraction), `FRAME_EXT` (jpg or webp), `FPS` (default 30)
7. **Video assets**: `STATS_BG_VIDEO` (HLS or MP4 URL for the stats band) and `CTA_BG_VIDEO` (same for the closing CTA)

Why batched: it keeps the user engaged and gives them concrete decisions rather than a wall of fields. After each batch, restate what you have so far so they can correct mid-stream.

If the user has a strong brand brief (e.g. "ABP, French Swiss luxury moving company"), default the placeholder values to plausible French copy from §1 of the source. Don't invent stats or testimonials — flag them as `[TODO]` if the user can't provide real ones. §22 anti-slop rule #5 is non-negotiable.

### Phase 2 — Source video + frame pipeline

The hero is a scroll-scrubbed canvas, NOT a `<video>` tag. The user supplies one short video (5-15s ideal); ffmpeg extracts it into 240-ish JPG/WebP frames that the canvas swaps per scroll position.

Ask the user:
- Do you have a hero video? If not, suggest a 8-12s premium-feel clip (slow tracking shot, product close-up, atmospheric reel) and offer to source one via Seedance / stock.
- What's the path to the source file? They drop it at `<project>/input/source.mp4`.

Then run the pipeline (the exact commands are in `references/mega-prompt.md` §2). Key rules:
- Filenames MUST be zero-padded 4-digit: `frame_0001.jpg` ... `frame_0240.jpg`
- `/input` is gitignored, `/public/frames` ships
- After extraction, count files (`ls public/frames | wc -l`) and update `FRAME_COUNT` in `src/lib/constants.ts`
- If total frame size > 20 MB and target is Vercel Hobby, warn the user (25 MB function limit) and suggest WebP conversion at q=82 (~40% size drop, no visible quality loss)

### Phase 3 — Project bootstrap + build

Follow the source verbatim — do NOT improvise on stack choices. The exact bootstrap sequence, file structure, and component-by-component specs are in `references/mega-prompt.md` sections 3 through 9 (page sections) plus 20-21 (animation patterns + `App.tsx` composition).

Build order that works well:
1. `npm create vite` + install deps (§3)
2. `index.css` — fonts → tokens → liquid-glass utilities → Tailwind `@theme` (§4-6)
3. `ScrubSequence.tsx` + `BlurText.tsx` + `constants.ts` — verbatim from §8-10
4. `Navbar.tsx` (Section 1 of source)
5. `Hero.tsx` (Section 2) — wire `scrollRef` from `App.tsx`
6. Sections 3-9 in order — each is one component file
7. `App.tsx` composition (§21)

Read each section's spec from `references/mega-prompt.md` *before* writing the component. Don't try to remember the spec from training data — there are specific magic numbers (250vh hero, `clamp(56px,9vw,144px)` headline, 28s/32s marquee timings) that matter for the cinematic feel.

### Phase 4 — Verification

§23 of the source has the verification checklist. The high-value checks:
- `npm run dev` starts cleanly, `npm run build` completes with no TS error
- Hero first paint within 300ms (priority-preload `frame_0001` via `<link rel="preload">` in `index.html`)
- Scroll scrubs through ≥ FRAME_COUNT/2.5 distinct frames smoothly
- Marquee duplication is invisible (the array must be doubled so the loop point isn't visible)
- 375px (iPhone SE): no horizontal scroll, hero scrub still renders
- Lighthouse ≥85 desktop, LCP <2.5s

## Anti-Slop Discipline (§22 of source)

Re-read these before submitting. Every violation is a defect:

1. **No emoji anywhere** — not in copy, card headers, or buttons
2. **No default violet/purple gradients** — palette is warm; gradients use `--primary → transparent`
3. **No `shadow-2xl` on cards** — depth on liquid-glass comes from `::before` border + inset highlight + backdrop blur, never drop shadow
4. **Buttons rounded-full, cards rounded-2xl, pills rounded-full** — there is no rounded-xl mid-rhythm
5. **No lorem ipsum** — flag `[TODO: {{NAME}}]` if a placeholder is empty
6. **No `text-center` on body prose** — only hero + CTA section center their text
7. **Headings: `font-display uppercase tracking-tight` OR `font-display italic`** — never both, never plain serif
8. **Every section: badge + heading + sub** — except hero (its own world) and footer (bare)
9. **Icons: lucide-react only**
10. **NEVER `<video>` for the hero** — canvas only. Video appears only in Stats and CTA backgrounds
11. **Animations ≤ 0.9s** — slow fades feel bad
12. **No `console.log`, no commented-out code, no unused imports** in the delivered project
13. **Don't auto-translate placeholders** — if the user wrote French, leave French
14. **Responsive at 375px** — every section must render with no horizontal scroll
15. **Focus rings on every interactive** — `focus-visible:ring-2 ring-ring ring-offset-2 ring-offset-background`. Canvas gets `aria-hidden="true"` + an `sr-only` summary

## Customization vs. Substitution

The user may show a hyliox reel that looks different from this template (e.g. a 3D glassy "V" hero on a VOXR AI demo, dark + electric purple palette). Per the user's memory in `~/.claude/projects/C--Users-user/memory/hyliox_template.md`: hyliox heavily customizes per-demo. The template you receive via DM is the scroll-scrub scaffold; reel-quality polish requires palette swaps, hero swaps, and copy rewrites tailored per niche.

When the user wants a per-niche reel-style customization:
- **Palette swap** — replace ochre/cream/ink/terra with the reel's palette (HSL triplets in `--ink`/`--cream`/`--ochre`/`--terra` CSS vars). Everything downstream re-themes automatically.
- **Hero swap** — if the reel uses a 3D element instead of scroll-scrub, replace `<ScrubSequence>` with a Spline embed or Three.js scene. Keep the 250vh sticky shell. (Or hand off to `3d-animation-web-designer` for that part.)
- **Copy rewrite** — match the reel's tone (B2B SaaS vs. luxury moving vs. fashion). Same 9 sections; different voice.

## File Reference Map

- `references/placeholders.md` — the 32-placeholder table extracted from §1, plus suggested defaults per niche (luxury moving, B2B SaaS, fashion, agency)
- `references/mega-prompt.md` — the full 1,106-line source. §1 is placeholders, §2 is ffmpeg pipeline, §3-7 is bootstrap+tokens, §8-10 is core components, §13-19 is sections 1-9, §20-23 is patterns/composition/verification, §24 is the final note. Note: §5 appears twice in the source (lines 220 + 337) — that's a copy-paste artifact in the original template, the second instance has leaked §4 content. Read the first instance (line 220) and skip the duplicate.
