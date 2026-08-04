# SplitText

SplitText breaks text into lines, words, and characters so you can animate each piece independently. Since GSAP 3.13 it's free.

## Registration
```js
import { SplitText } from "gsap/SplitText";
gsap.registerPlugin(SplitText);
```

## Basic usage

```js
const split = new SplitText(".headline", {
  type: "chars,words,lines",   // what to split into
  linesClass: "line",
  wordsClass: "word",
  charsClass: "char",
  mask: "lines",               // wrap lines in overflow:hidden for reveal effects
});

gsap.from(split.chars, {
  y: 100,
  opacity: 0,
  duration: 0.8,
  ease: "power3.out",
  stagger: 0.02,
});

// Clean up when done (restores original DOM):
split.revert();
```

## Common patterns

**Line-by-line reveal (masked):**
```js
const split = new SplitText(".paragraph", { type: "lines", mask: "lines" });
gsap.from(split.lines, { yPercent: 100, duration: 0.8, stagger: 0.1, ease: "power3.out" });
```

**Character typewriter:**
```js
const split = new SplitText(".heading", { type: "chars" });
gsap.from(split.chars, { opacity: 0, duration: 0.02, stagger: 0.05, ease: "none" });
```

**Word-by-word fade:**
```js
const split = new SplitText(".quote", { type: "words" });
gsap.from(split.words, { opacity: 0, filter: "blur(10px)", duration: 0.6, stagger: 0.08 });
```

## Responsive — the critical part

Lines recompute when the container width changes. Always re-split on resize or use `autoSplit: true` (GSAP 3.13+).

```js
let split;
function createSplit() {
  split?.revert();
  split = new SplitText(".headline", { type: "lines", mask: "lines" });
  gsap.from(split.lines, { yPercent: 100, stagger: 0.1 });
}

// Option A: manual
window.addEventListener("resize", createSplit);

// Option B (preferred, 3.13+): autoSplit
const split = SplitText.create(".headline", {
  type: "lines",
  autoSplit: true,               // auto re-splits on font load + resize
  onSplit: (self) => {
    return gsap.from(self.lines, { yPercent: 100, stagger: 0.1 });
  },
});
```

## Font loading gotcha

If you split before fonts load, lines break at the wrong characters. Always wait:

```js
document.fonts.ready.then(() => {
  const split = new SplitText(".headline", { type: "lines" });
  // ... animate
});
```

## Accessibility

SplitText wraps characters in `<div>`s which can break screen readers. Add `aria-label` with the original text on the parent and `aria-hidden="true"` on the split pieces, or use `deepSlice: false` and test with VoiceOver.

```html
<h1 class="headline" aria-label="Welcome home">Welcome home</h1>
```
