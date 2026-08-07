# Animation Reference

> Cinematic motion design extracted from live DOM. Follow these specs exactly to recreate the experience.

## Motion Technology Stack

| Library | Type | Notes |
|---------|------|-------|
| **Web Animations API (12 active)** | animation |  |

## Scroll Journey

The page is **10,042px** tall. Each frame below shows what the user sees at that scroll depth.

> **Use these screenshots to understand WHAT animates, WHEN it animates, and HOW it moves.**

### 0% — Top / Hero
Scroll position: 0px

![Scroll 0%](../screens/scroll/scroll-000.png)

### 17% — Opening Section
Scroll position: 1,554px

![Scroll 17%](../screens/scroll/scroll-017.png)

### 33% — First Feature Section
Scroll position: 3,017px

![Scroll 33%](../screens/scroll/scroll-033.png)

### 50% — Mid-Page
Scroll position: 4,571px

![Scroll 50%](../screens/scroll/scroll-050.png)

### 67% — Lower Content
Scroll position: 6,125px

![Scroll 67%](../screens/scroll/scroll-067.png)

### 83% — Near Footer
Scroll position: 7,588px

![Scroll 83%](../screens/scroll/scroll-083.png)

### 100% — Bottom / Footer
Scroll position: 9,142px

![Scroll 100%](../screens/scroll/scroll-100.png)

## Video Elements

| # | Role | Autoplay | Loop | Muted | Size | First Frame |
|---|------|----------|------|-------|------|-------------|
| 1 | content | — | ✓ | ✓ | 593×228 | — |
| 2 | content | — | ✓ | ✓ | 421×458 | — |
| 3 | content | — | ✓ | ✓ | 335×220 | — |
| 4 | content | — | ✓ | ✓ | — | — |
| 5 | content | — | ✓ | ✓ | — | — |
| 6 | content | — | ✓ | ✓ | — | — |

- **Source:** `https://webstatic.chargebee.com/assets/web/20260804043214/images/home_v2/oct-2025/gartner-video.mp4`
- **Poster:** `https://webstatic.chargebee.com/assets/web/20260804043214/images/home_v2/oct-2025/gartner-video.webp`
- **Source:** `https://webstatic.chargebee.com/assets/web/20260804043214/images/home_v2/oct-2025/gartner-video.mp4`
- **Poster:** `https://webstatic.chargebee.com/assets/web/20260804043214/images/home_v2/oct-2025/gartner-video.webp`
- **Source:** `https://webstatic.chargebee.com/assets/web/20260804043214/images/home_v2/oct-2025/beelieve-video.mp4`
- **Poster:** `https://webstatic.chargebee.com/assets/web/20260804043214/images/home_v2/oct-2025/beelieve-video.webp`
- **Source:** `https://webstatic.chargebee.com/assets/web/20260804043214/images/home_v2/videos/video-5.mp4`
- **Poster:** `https://webstatic.chargebee.com/assets/web/20260804043214/images/home_v2/videos/video-5.webp`
- **Source:** `https://webstatic.chargebee.com/assets/web/20260804043214/images/home_v2/videos/video-7.mp4`
- **Poster:** `https://webstatic.chargebee.com/assets/web/20260804043214/images/home_v2/videos/video-7.webp`
- **Source:** `https://webstatic.chargebee.com/assets/web/20260804043214/images/home_v2/videos/video-6.mp4`
- **Poster:** `https://webstatic.chargebee.com/assets/web/20260804043214/images/home_v2/videos/video-6.webp`

## Scroll Animation Patterns

| Pattern | Library | Element Count | Duration | Delay | Easing |
|---------|---------|---------------|----------|-------|--------|
| parallax / sticky scroll | CSS | 3 | — | — | — |

### CSS Implementation

## CSS Keyframes (38 extracted)

### `@keyframes slides`

Duration: `20s` · Easing: `linear` · Delay: `0s` · Iteration: `infinite` · Fill: `none`

Used by: `.rc-animate-\[20s_slides_infinite_linear\]`, `.index .rc-bg__buttons__container`

```css
@keyframes slides {
  0% {
    transform: translate(0px);
  }
  100% {
    transform: translate(-50%);
  }
}
```

> Transform/motion animation

### `@keyframes skeletonShimmer`

Duration: `1.5s` · Easing: `ease` · Delay: `0s` · Iteration: `infinite` · Fill: `none`

Used by: `.rc-form__fields .rc-form__skeleton-input, .rc-form__fields .rc-form__skeleton-l`, `.rc-form__fields .rc-form__skeleton-button`

```css
@keyframes skeletonShimmer {
  0% {
    background-position-x: 200%;
    background-position-y: 0px;
  }
  100% {
    background-position-x: -200%;
    background-position-y: 0px;
  }
}
```

> Background color/gradient shift · Background position (shimmer/scroll)

### `@keyframes skeletonShimmer`

Duration: `1.5s` · Easing: `ease` · Delay: `0s` · Iteration: `infinite` · Fill: `none`

Used by: `.rc-form__fields .rc-form__skeleton-input, .rc-form__fields .rc-form__skeleton-l`, `.rc-form__fields .rc-form__skeleton-button`

```css
@keyframes skeletonShimmer {
  0% {
    background-position-x: 200%;
    background-position-y: 0px;
  }
  100% {
    background-position-x: -200%;
    background-position-y: 0px;
  }
}
```

> Background color/gradient shift · Background position (shimmer/scroll)

### `@keyframes slides`

Duration: `20s` · Easing: `linear` · Delay: `0s` · Iteration: `infinite` · Fill: `none`

Used by: `.rc-animate-\[20s_slides_infinite_linear\]`, `.index .rc-bg__buttons__container`

```css
@keyframes slides {
  0% {
    transform: translate(0px);
  }
  100% {
    transform: translate(-50%);
  }
}
```

> Transform/motion animation

### `@keyframes rc-bounce`

Duration: `1s` · Easing: `ease` · Delay: `0s` · Iteration: `infinite` · Fill: `none`

Used by: `.rc-animate-bounce`

```css
@keyframes rc-bounce {
  0%, 100% {
    transform: translateY(-25%);
    animation-timing-function: cubic-bezier(0.8, 0, 1, 1);
  }
  50% {
    transform: none;
    animation-timing-function: cubic-bezier(0, 0, 0.2, 1);
  }
}
```

> Transform/motion animation

### `@keyframes rc-ping`

Duration: `1s` · Easing: `cubic-bezier(0, 0, 0.2, 1)` · Delay: `0s` · Iteration: `infinite` · Fill: `none`

Used by: `.rc-animate-ping`

```css
@keyframes rc-ping {
  75%, 100% {
    transform: scale(2);
    opacity: 0;
  }
}
```

> Fade + motion enter animation

### `@keyframes rc-tv-toaster-shimmer`

Duration: `1.3s` · Easing: `linear` · Delay: `0s` · Iteration: `infinite` · Fill: `none`

Used by: `.rc-tv-toaster__skeleton`

```css
@keyframes rc-tv-toaster-shimmer {
  0% {
    background-position-x: 150%, 0px;
    background-position-y: 0px, 0px;
  }
  100% {
    background-position-x: -150%, 0px;
    background-position-y: 0px, 0px;
  }
}
```

> Background color/gradient shift · Background position (shimmer/scroll)

### `@keyframes rc-tv-toaster-chevron`

Duration: `1.8s` · Easing: `ease-in-out` · Delay: `0s` · Iteration: `infinite` · Fill: `none`

Used by: `.rc-tv-toaster__restore-logo path`

```css
@keyframes rc-tv-toaster-chevron {
  0%, 100% {
    opacity: 0.45;
    transform: translateY(1px);
  }
  50% {
    opacity: 1;
    transform: translateY(-1.5px);
  }
}
```

> Fade + motion enter animation

### `@keyframes rc-tv-toaster-spin`

Duration: `6s` · Easing: `linear` · Delay: `0s` · Iteration: `infinite` · Fill: `none`

Used by: `.rc-tv-toaster__restore-mark svg`

```css
@keyframes rc-tv-toaster-spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(1turn);
  }
}
```

> Transform/motion animation

### `@keyframes ripple`

Duration: `1s` · Easing: `linear` · Delay: `0s` · Iteration: `1` · Fill: `none`

Used by: `.index .rc-hero--ripple:hover .rc-ripple`

```css
@keyframes ripple {
  0% {
    opacity: 1;
    transform: rotate(60deg) translate(200px, 300px);
  }
  100% {
    opacity: 1;
    transform: rotate(60deg) translate(200px);
  }
}
```

> Fade + motion enter animation

### `@keyframes scroll-left`

Duration: `18s` · Easing: `linear` · Delay: `0s` · Iteration: `infinite` · Fill: `none`

Used by: `.index .rc-marquee__track`

```css
@keyframes scroll-left {
  0% {
    transform: translate(0px);
  }
  100% {
    transform: translate(-50%);
  }
}
```

> Transform/motion animation

### `@keyframes animatedgradient`

Duration: `3s` · Easing: `ease` · Delay: `0s` · Iteration: `infinite` · Fill: `none`

Used by: `.index .rc-marquee:hover::after`

```css
@keyframes animatedgradient {
  0% {
    background-position-x: 0px;
    background-position-y: 50%;
  }
  50% {
    background-position-x: 100%;
    background-position-y: 50%;
  }
  100% {
    background-position-x: 0px;
    background-position-y: 50%;
  }
}
```

> Background color/gradient shift · Background position (shimmer/scroll)

### `@keyframes fadeInRight`

Used by: `.index .fadeInRight`

```css
@keyframes fadeInRight {
  0% {
    opacity: 0;
    transform: translate3d(10%, 0px, 0px);
  }
  100% {
    opacity: 1;
    transform: none;
  }
}
```

> Fade + motion enter animation

### `@keyframes fadeInLeft`

Used by: `.index .fadeInLeft`

```css
@keyframes fadeInLeft {
  0% {
    opacity: 0.1;
    transform: translate3d(-10%, 0px, 0px);
  }
  100% {
    opacity: 1;
    transform: none;
  }
}
```

> Fade + motion enter animation

### `@keyframes fadeInUp`

Used by: `.index .fadeInUp`

```css
@keyframes fadeInUp {
  0% {
    opacity: 0.7;
    transform: translate3d(0px, 15%, 0px);
  }
  100% {
    opacity: 1;
    transform: none;
  }
}
```

> Fade + motion enter animation

### `@keyframes za-cta-heart-blink`

Duration: `0.65s` · Easing: `ease-in-out` · Delay: `0s` · Iteration: `infinite` · Fill: `none`

Used by: `.index .za-grid__col:hover .za-cta--heart`

```css
@keyframes za-cta-heart-blink {
  0%, 100% {
    opacity: 1;
    scale: 1;
  }
  50% {
    opacity: 0.2;
    scale: 0.8;
  }
}
```

> Opacity fade

### `@keyframes showLogo`

Duration: `0.4s` · Easing: `ease-in-out` · Delay: `0s` · Iteration: `1` · Fill: `forwards`

Used by: `.index .rc-slider__body .slick-slide.slick-current [class^="cb-storybook-img"]`

```css
@keyframes showLogo {
  100% {
    opacity: 1;
    transform: translate(0px);
  }
}
```

> Fade + motion enter animation

### `@keyframes showAuthorInfo`

Duration: `0.25s` · Easing: `ease-in-out` · Delay: `0.5s` · Iteration: `1` · Fill: `forwards`

Used by: `.index .rc-slider--casestudy .card.active .rc-casestudy__body`

```css
@keyframes showAuthorInfo {
  100% {
    opacity: 1;
    transform: translateY(0px);
  }
}
```

> Fade + motion enter animation

### `@keyframes anime`

Duration: `8s` · Easing: `linear` · Delay: `0s` · Iteration: `infinite` · Fill: `none`

Used by: `#rcFooter footer .rc-footer-cta`

```css
@keyframes anime {
  0% {
    background-position-x: 0px;
    background-position-y: 50%;
  }
  50% {
    background-position-x: 100%;
    background-position-y: 50%;
  }
  100% {
    background-position-x: 0px;
    background-position-y: 50%;
  }
}
```

> Background color/gradient shift · Background position (shimmer/scroll)

### `@keyframes anime`

Duration: `8s` · Easing: `linear` · Delay: `0s` · Iteration: `infinite` · Fill: `none`

Used by: `#rcFooter footer .rc-footer-cta`

```css
@keyframes anime {
  0% {
    background-position-x: 0px;
    background-position-y: 50%;
  }
  50% {
    background-position-x: 100%;
    background-position-y: 50%;
  }
  100% {
    background-position-x: 0px;
    background-position-y: 50%;
  }
}
```

> Background color/gradient shift · Background position (shimmer/scroll)

### `@keyframes splide-loading`

Duration: `1s` · Easing: `linear` · Delay: `0s` · Iteration: `infinite` · Fill: `none`

Used by: `.splide__spinner`

```css
@keyframes splide-loading {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(1turn);
  }
}
```

> Transform/motion animation

### `@keyframes agent-shimmer-962d5e26`

Duration: `1.4s` · Easing: `ease` · Delay: `0s` · Iteration: `infinite` · Fill: `none`

Used by: `.agent-loading__bar[data-v-962d5e26]`

```css
@keyframes agent-shimmer-962d5e26 {
  0% {
    background-position-x: 200%;
    background-position-y: 0px;
  }
  100% {
    background-position-x: -200%;
    background-position-y: 0px;
  }
}
```

> Background color/gradient shift · Background position (shimmer/scroll)

### `@keyframes rc-tv-toaster-shimmer`

Duration: `1.3s` · Easing: `linear` · Delay: `0s` · Iteration: `infinite` · Fill: `none`

Used by: `.rc-tv-toaster__skeleton`

```css
@keyframes rc-tv-toaster-shimmer {
  0% {
    background-position-x: 150%, 0px;
    background-position-y: 0px, 0px;
  }
  100% {
    background-position-x: -150%, 0px;
    background-position-y: 0px, 0px;
  }
}
```

> Background color/gradient shift · Background position (shimmer/scroll)

### `@keyframes rc-tv-toaster-chevron`

Duration: `1.8s` · Easing: `ease-in-out` · Delay: `0s` · Iteration: `infinite` · Fill: `none`

Used by: `.rc-tv-toaster__restore-logo path`

```css
@keyframes rc-tv-toaster-chevron {
  0%, 100% {
    opacity: 0.45;
    transform: translateY(1px);
  }
  50% {
    opacity: 1;
    transform: translateY(-1.5px);
  }
}
```

> Fade + motion enter animation

### `@keyframes rc-tv-toaster-spin`

Duration: `6s` · Easing: `linear` · Delay: `0s` · Iteration: `infinite` · Fill: `none`

Used by: `.rc-tv-toaster__restore-mark svg`

```css
@keyframes rc-tv-toaster-spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(1turn);
  }
}
```

> Transform/motion animation

### `@keyframes ripple`

Duration: `1s` · Easing: `linear` · Delay: `0s` · Iteration: `1` · Fill: `none`

Used by: `.index .rc-hero--ripple:hover .rc-ripple`

```css
@keyframes ripple {
  0% {
    opacity: 1;
    transform: rotate(60deg) translate(200px, 300px);
  }
  100% {
    opacity: 1;
    transform: rotate(60deg) translate(200px);
  }
}
```

> Fade + motion enter animation

### `@keyframes scroll-left`

Duration: `18s` · Easing: `linear` · Delay: `0s` · Iteration: `infinite` · Fill: `none`

Used by: `.index .rc-marquee__track`

```css
@keyframes scroll-left {
  0% {
    transform: translate(0px);
  }
  100% {
    transform: translate(-50%);
  }
}
```

> Transform/motion animation

### `@keyframes animatedgradient`

Duration: `3s` · Easing: `ease` · Delay: `0s` · Iteration: `infinite` · Fill: `none`

Used by: `.index .rc-marquee:hover::after`

```css
@keyframes animatedgradient {
  0% {
    background-position-x: 0px;
    background-position-y: 50%;
  }
  50% {
    background-position-x: 100%;
    background-position-y: 50%;
  }
  100% {
    background-position-x: 0px;
    background-position-y: 50%;
  }
}
```

> Background color/gradient shift · Background position (shimmer/scroll)

### `@keyframes fadeInRight`

Used by: `.index .fadeInRight`

```css
@keyframes fadeInRight {
  0% {
    opacity: 0;
    transform: translate3d(10%, 0px, 0px);
  }
  100% {
    opacity: 1;
    transform: none;
  }
}
```

> Fade + motion enter animation

### `@keyframes fadeInLeft`

Used by: `.index .fadeInLeft`

```css
@keyframes fadeInLeft {
  0% {
    opacity: 0.1;
    transform: translate3d(-10%, 0px, 0px);
  }
  100% {
    opacity: 1;
    transform: none;
  }
}
```

> Fade + motion enter animation

### `@keyframes fadeInUp`

Used by: `.index .fadeInUp`

```css
@keyframes fadeInUp {
  0% {
    opacity: 0.7;
    transform: translate3d(0px, 15%, 0px);
  }
  100% {
    opacity: 1;
    transform: none;
  }
}
```

> Fade + motion enter animation

### `@keyframes za-cta-heart-blink`

Duration: `0.65s` · Easing: `ease-in-out` · Delay: `0s` · Iteration: `infinite` · Fill: `none`

Used by: `.index .za-grid__col:hover .za-cta--heart`

```css
@keyframes za-cta-heart-blink {
  0%, 100% {
    opacity: 1;
    scale: 1;
  }
  50% {
    opacity: 0.2;
    scale: 0.8;
  }
}
```

> Opacity fade

### `@keyframes showLogo`

Duration: `0.4s` · Easing: `ease-in-out` · Delay: `0s` · Iteration: `1` · Fill: `forwards`

Used by: `.index .rc-slider__body .slick-slide.slick-current [class^="cb-storybook-img"]`

```css
@keyframes showLogo {
  100% {
    opacity: 1;
    transform: translate(0px);
  }
}
```

> Fade + motion enter animation

### `@keyframes showAuthorInfo`

Duration: `0.25s` · Easing: `ease-in-out` · Delay: `0.5s` · Iteration: `1` · Fill: `forwards`

Used by: `.index .rc-slider--casestudy .card.active .rc-casestudy__body`

```css
@keyframes showAuthorInfo {
  100% {
    opacity: 1;
    transform: translateY(0px);
  }
}
```

> Fade + motion enter animation

### `@keyframes scrollRowOne`

```css
@keyframes scrollRowOne {
  0% {
    background-position-x: 0px;
    background-position-y: 0px;
  }
  100% {
    background-position-x: -860px;
    background-position-y: 0px;
  }
}
```

> Background color/gradient shift · Background position (shimmer/scroll)

### `@keyframes scrollRowTwo`

```css
@keyframes scrollRowTwo {
  0% {
    background-position-x: 0px;
    background-position-y: 0px;
  }
  100% {
    background-position-x: 690px;
    background-position-y: 0px;
  }
}
```

> Background color/gradient shift · Background position (shimmer/scroll)

### `@keyframes scrollRowOne`

```css
@keyframes scrollRowOne {
  0% {
    background-position-x: 0px;
    background-position-y: 0px;
  }
  100% {
    background-position-x: -860px;
    background-position-y: 0px;
  }
}
```

> Background color/gradient shift · Background position (shimmer/scroll)

### `@keyframes scrollRowTwo`

```css
@keyframes scrollRowTwo {
  0% {
    background-position-x: 0px;
    background-position-y: 0px;
  }
  100% {
    background-position-x: 690px;
    background-position-y: 0px;
  }
}
```

> Background color/gradient shift · Background position (shimmer/scroll)

## Global Transition Declarations

These `transition` values were extracted from CSS rules across the site:

```css
transition: transform 0.3s;
transition: 0.3s cubic-bezier(0.4, 0, 0.2, 1);
transition: opacity 0.35s;
transition: opacity 0.4s;
transition: background 0.2s;
transition: transform 0.2s;
transition: opacity 0.28s, max-height 0.28s;
transition: opacity 0.2s, background-color 0.2s;
transition: transform 0.4s, opacity 0.4s;
transition: opacity 0.25s ease-in-out;
transition: 0.25s ease-in-out;
transition: 0.3s ease-in-out;
```

## How to Recreate This Motion Design

### Step 1 — Install Dependencies

```bash
```

### Step 2 — Scroll-Reveal Pattern

Elements that animate into view follow this pattern:

```css
/* Initial hidden state */
.reveal {
  opacity: 0;
  transform: translateY(40px);
  transition: opacity 0.3s cubic-bezier(0.4, 0, 0.2, 1),
              transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}
.reveal.visible {
  opacity: 1;
  transform: translateY(0);
}
```

### Step 3 — Key Motion Principles

- **Duration scale:** `0.3s` · `0.35s` · `0.4s` · `0.2s` — use these values, never invent new durations
- **Always add** `@media (prefers-reduced-motion: reduce) { * { animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; } }`

### Step 4 — Scroll Journey Reference

Match what happens at each scroll position:

- **0%** (`0px`) → `screens/scroll/scroll-000.png`
- **17%** (`1554px`) → `screens/scroll/scroll-017.png`
- **33%** (`3017px`) → `screens/scroll/scroll-033.png`
- **50%** (`4571px`) → `screens/scroll/scroll-050.png`
- **67%** (`6125px`) → `screens/scroll/scroll-067.png`
- **83%** (`7588px`) → `screens/scroll/scroll-083.png`
- **100%** (`9142px`) → `screens/scroll/scroll-100.png`

