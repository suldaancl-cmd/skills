# Accessibility — WCAG, keyboard, screen readers, motion

Accessible design is not a post-hoc audit; it's a structural choice. Building accessibly also builds better for everyone (low-vision, motor-impaired, cognitive load, slow connections, old devices). This is a craft standard, not a compliance checkbox.

## The WCAG 2.1 / 2.2 AA bar (minimum)

### Color contrast
- **Normal text** (< 18pt or < 14pt bold): **≥ 4.5:1** against background
- **Large text** (≥ 18pt or ≥ 14pt bold): **≥ 3:1**
- **UI components & graphics**: **≥ 3:1**
- **Focus indicators**: **≥ 3:1** against adjacent colors

Check with tools (Stark, Contrast, axe DevTools). Never eyeball.

Common violations:
- Light gray body text (`#999` on `#FFF` = 2.85:1 → fails)
- Placeholder text used as label (placeholder is typically < 4.5:1)
- Brand color buttons (`#0066FF` on `#FFF` = 4.53:1 → borderline, often fails at smaller sizes)

### Text alternatives
- Every `<img>` has `alt`. Decorative images: `alt=""`.
- Icons with meaning: `aria-label` or adjacent visible text.
- Complex images / charts: `aria-describedby` pointing to a longer text description.
- Video: captions (and transcripts, ideally).

### Keyboard accessibility
- All interactive elements reachable by Tab.
- Logical tab order (usually DOM order; override only with care).
- Visible focus indicator on every focusable element.
- `Escape` closes modals/dropdowns. `Enter`/`Space` activates buttons. `Arrow keys` in menus/radio-groups.
- Skip link at page start: `<a href="#main" class="skip-link">Skip to main content</a>`.

### Focus
Default browser outline is ugly but functional. Custom focus styles:
```css
:focus-visible {
  outline: 2px solid var(--color-accent);
  outline-offset: 2px;
  border-radius: inherit;
}
/* Remove the dotted outline only if you replace it */
:focus:not(:focus-visible) { outline: none; }
```

Never `outline: 0` without replacement. Never `outline: 0` on global `*`.

### Semantic HTML

This is 80% of accessibility:
```html
<button>Click me</button>       <!-- NOT <div onclick> -->
<a href="/page">Link</a>         <!-- NOT <span onclick> -->
<input type="checkbox">          <!-- NOT styled div -->
<nav>, <main>, <header>, <footer>, <aside>, <article>, <section>
<h1>...<h6>                      <!-- proper hierarchy, one <h1> per page -->
<label for="email">              <!-- associated with input -->
```

Custom components (Radix UI, Ark UI, React Aria Components) give you accessibility-correct primitives. Use them; don't hand-roll a Select from divs.

### Forms
- Every input has a `<label>`. Placeholder is NOT a label.
- Required fields marked both visually (`*`) and semantically (`aria-required`).
- Error messages associated via `aria-describedby` and announced via `aria-live`.
- Group related inputs with `<fieldset>` + `<legend>`.
- Inline validation: don't validate on keypress (too aggressive); validate on blur.
- `autocomplete` attributes on common fields: `autocomplete="email"`, `autocomplete="current-password"`.

### Headings
- One `<h1>` per page — the page's topic.
- `<h2>`–`<h6>` nest logically. Don't skip levels for styling.
- Screen reader users navigate by heading; bad hierarchy = lost.

### Links vs. buttons
- **Link**: navigates to somewhere. `<a href>`. Opens in new tab? `target="_blank" rel="noopener noreferrer"`.
- **Button**: performs an action. `<button>`.
- Never style a link as a button (or vice-versa) and confuse their semantics.

### Color as communication
- Error states can't rely on color alone (red border) — add an icon or text.
- Charts need patterns or labels in addition to color.
- Links in body text need more than just color (underline them, or make the color contrast ≥ 3:1 against body text).

### Motion & animation
- Respect `prefers-reduced-motion`:
```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```
- No flashing > 3Hz (seizure risk).
- Auto-playing video: must be pauseable, no audio (or muted by default with unmute control).
- Parallax and scroll-jacking: provide an opt-out.

### Zoom & text resize
- Design works at 200% browser zoom without horizontal scroll (except known 2D surfaces like maps).
- Text reflows; doesn't overlap.
- Use `rem` / `em` for font sizes, not `px`, so users' browser font-size settings apply.

### Touch targets
- **Minimum 44×44px** hit area (WCAG 2.5.5 AAA, but treat as baseline).
- Spacing between adjacent targets: ≥ 8px to prevent misclicks.
- Icon buttons: don't make the button the icon's size; pad around it.

## Screen reader patterns

### Hidden-but-spoken text
```css
.sr-only {
  position: absolute;
  width: 1px; height: 1px;
  padding: 0; margin: -1px; overflow: hidden;
  clip: rect(0, 0, 0, 0); white-space: nowrap; border: 0;
}
```

Use for: icon button labels, skip links, context that's visual-only ("loading complete").

### Live regions
```html
<div aria-live="polite" aria-atomic="true">
  <!-- announcements go here, e.g., "Form saved" -->
</div>
```
- `polite`: announced when screen reader is idle (most updates)
- `assertive`: announced immediately (errors only — don't abuse)

### ARIA — the rule
First rule of ARIA: don't use ARIA. If a native element exists (`<button>`, `<details>`), use it. ARIA is a patch for custom components.

When you do need it:
- `aria-label`: short label for unlabeled elements (icon buttons).
- `aria-labelledby`: references visible text that labels this element.
- `aria-describedby`: references additional description (error message).
- `aria-expanded`: on disclosure triggers (menus, accordions).
- `aria-current="page"`: on active nav link.
- `aria-hidden="true"`: hide from SR (decorative elements only — don't hide interactive content).

## Complex patterns

### Modal / dialog
- Focus trap: Tab cycles within the modal, doesn't escape.
- First focusable element receives focus on open.
- `Escape` closes, returns focus to the trigger.
- `aria-modal="true"` + `role="dialog"` + `aria-labelledby` pointing to title.
- Body scroll locked while open.
- Use Radix Dialog, HeadlessUI Dialog, or react-aria — they handle all of this.

### Dropdown menu
- Opens on click (not hover) for accessibility (`hover` is hard for motor impairments).
- Arrow keys navigate items; `Enter` activates; `Escape` closes.
- Focus returns to trigger on close.

### Tabs
- Arrow keys navigate tabs; `Enter`/`Space` activates.
- `role="tablist"`, `role="tab"`, `role="tabpanel"`.
- Tab panel receives focus (or is focusable via `tabindex="0"`).

### Carousel / slider
- Auto-play: pauseable, pause on focus/hover.
- Previous/next buttons have clear labels.
- Announce current slide position (`Slide 2 of 5`).
- Most carousels should not exist; reconsider the design.

## Testing — the minimum before ship

1. **Keyboard-only**: navigate the entire page with Tab/Shift+Tab, Enter, Space, Escape, Arrow keys. Can you reach and use everything?
2. **Screen reader**: test with VoiceOver (Mac: Cmd+F5) or NVDA (Windows, free). Walk through hero → CTA → form submit.
3. **Automated scan**: axe DevTools, Lighthouse accessibility audit. Catches ~30% of issues — not a substitute for manual testing.
4. **Contrast scan**: Stark or axe highlights low-contrast text.
5. **Zoom to 200%**: does the layout still work?
6. **Reduced motion**: enable the OS setting (Mac: System Settings → Accessibility → Display → Reduce Motion). Do animations still look acceptable?

## Writing accessibly

- Plain language. Grade 8 reading level for consumer content; grade 12 for technical.
- Meaningful link text. Not "click here" or "learn more" — "See our pricing" or "Read the docs".
- Avoid jargon without definition.
- Avoid ALL CAPS for emphasis (SRs sometimes read letter-by-letter).
- Avoid symbol-heavy text (✓✗→) in copy — ambiguous to SRs.

## Progressive enhancement

Build the page so it works:
1. With HTML only (no CSS) — content is readable.
2. With HTML + CSS (no JS) — layout works, critical actions still possible.
3. With everything — full experience.

Modern CSS + HTML can handle many interactions previously requiring JS (`<details>`, form validation, `:has()`, view transitions).

## The test

Ask a screen reader user to complete the primary task. If they can do it in reasonable time without getting stuck, you shipped accessible. If they can't, no amount of axe score matters.
