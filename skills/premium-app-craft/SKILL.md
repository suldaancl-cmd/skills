---
name: premium-app-craft
description: The craft layer that separates a premium app from an AI-generated one — the ~20 stacked micro-details (press states, spring physics, haptics, keyboard behaviour, loading/empty states), the interaction patterns worth stealing (morphing pill tab bar, scroll-linked header, snap feed, slide-to-act, dock+FAB), and the verification discipline that proves it works. Use whenever building or reviewing a mobile app, an app screen, a nav bar, or any interaction — and before claiming any interaction is done. Companion to paywall-psychology, paywall-design-patterns, paywall-strategy-planner, paywall-compliance-guardrails, paywall-teardowns.
---

# Premium App Craft

Why most AI-built apps feel cheap, and the specific moves that fix it. Sourced from teardowns of shipped apps (Sol, Savee, Sabbath, Flighty, Revolut, a React-Native calendar) plus published A/B evidence. Working demos: `~/.claude/_projects/paywall-studio/designs/23-motion-lab.html`.

## The core law

> **Premium is not one thing. It is ~20 tiny details stacked.** Users never name a single one — they just say the app "feels different". Ship 3 of them and it still feels generated.

## The five details that matter most

1. **Press states with spring physics.** Every tappable element scales down on press (~0.93–0.97) and *cancels* if the finger slides off before release. Absence of press feedback is the number-one "AI built this" tell. Use `cubic-bezier(.34,1.4,.5,1)`, ~150ms.
2. **Animation that reports events, never decorates.** Fade in on first load; cross-fade a toggle; native zoom between screens. **Over-animating reads as cheap** — one teardown literally captions it "too much → low quality". If an animation does not communicate a state change, delete it.
3. **Haptics.** The closest software gets to earning physical trust. Success pattern on submit, a tick on toggle, continuous feedback while dragging. **`navigator.vibrate` is Android-only — iOS Safari ignores it.** Real haptics require the native layer; do not promise them on web.
4. **Keyboard behaviour.** The single biggest human-vs-generated separator. Button rides up with the keyboard, input auto-focuses, swipe-down blurs, the field grows then scrolls. A static input pinned under a keyboard is the lazy tell.
5. **Loading and empty states.** Never a blank screen or a raw spinner. Empty = icon + one line of what happens next. Loading = branded shimmer naming what is happening. Onboard every OS permission *before* the system prompt.

## Interaction patterns worth stealing

All five are implemented and tappable in `23-motion-lab.html`.

| Pattern | What it is | Use when |
|---|---|---|
| **Morphing pill tab bar** | The bar is three elements: a fixed utility icon, ONE morphing pill carrying the active context (icon + label), and a plus. Inactive tabs are not rendered anywhere; in a detail view the whole bar swaps for a contextual toolbar | You want a narrow, premium dock (Sol) |
| **Scroll-linked header** | Scroll position drives header *state* (selected date, week number), not just size | Lists with temporal or sectioned structure |
| **Compact-on-scroll dock** | Dock collapses to icons in one direction, expands in the other, always full at top | Long scrolling content under a persistent dock |
| **Full-bleed snap feed** | Edge-to-edge cards, `scroll-snap-type: y mandatory`, zero chrome while browsing | The media *is* the product (Savee) |
| **Slide-to-act** | Drag-to-confirm with a travelling light hint | Committing or destructive actions — ceremony beats a tap |
| **Dock + separate FAB** | Tabs switch context; a FAB creates. Never merge them | Any app with both navigation and a primary create action |
| **Glass over a real scene** | Frosted glass only reads premium over a *lit* scene (photo/3D), never a flat fill; one dark card anchors, one warm accent carries all emphasis | Premium/luxury surfaces (travel, concierge, booking) |
| **Ambient particles over the UI** | Weather/state particles fall across the *whole* screen, not inside a widget; die under `prefers-reduced-motion` | The condition IS the content (weather, celebration) |
| **Onboarding that proves it** | Every claim is demonstrated by the object on its own screen — the prompt types itself, the flow runs, the graph draws. Show the proof, then ask | Any onboarding before a paywall |
| **Data as atmosphere** | The reading *is* the background — a thermal gradient driven by the value, with a hardware-style tick wheel | Single-value dashboards (temp, mood, score) |
| **Nested submenu** | The child menu opens *beside* its parent row, never covering it; checkmarks carry state in both layers | Dense pickers (model + effort, filter + sort) |

**Rules that fall out of these:**
- Bind scroll-driven state to the **topmost visible section**, not raw offset — survives a fling.
- Use a **movement threshold (~6px)** before flipping any scroll-reactive state, or a thumb wobble makes it strobe.
- Decorative loops (shimmer, travelling orb) must die under `prefers-reduced-motion`. Informational motion may stay.
- Never destroy DOM to change state. Animate `max-width`/`opacity` so the change is reversible and smooth. (A real bug: a dock that `.remove()`d its label left a blank pill forever after the first tap.)
- A scroll-linked selection must be able to reach the **last** section. Add an end inset (`clientHeight − lastSectionHeight`, like a native contentInset) or the final items can never top-align and never get selected. (A real bug: days 21–23 were mathematically unreachable — max scroll 585px, last section at 967px.)

## Native vs web — the honest line

A screen-for-screen rebuild of Flighty in Expo proves **visual** parity is reachable. Still frames cannot prove animation feel, gesture response, haptics, or scroll performance — which is exactly what separates native from web. Claim visual parity; do not claim feel.

## Verification discipline (non-negotiable)

An interaction is not done because it renders. Prove it:

1. **Render it and look.** Headless Chrome to PNG, then actually read the image. Bugs found this way that "looked fine" in code: a `$2 . 49` price (monospace gives the decimal a full cell), a badge colliding with a close button, a dead void where content did not reach the bottom.
2. **Probe the behaviour, not the paint.** Drive the DOM programmatically and assert on the resulting state.
3. **Beware the harness.** `requestAnimationFrame` under headless virtual-time gives contradictory results, and embedded/offscreen browser panes suspend the rendering pipeline entirely — scroll events and rAF simply never fire (verified: a trivial sanity scroller registered 0 events). A probe that scrolls and sees no state change proves nothing about the page. If a browser probe is flaky, extract the decision into a **pure function and unit-test it**, and check reachability with raw geometry (offsets vs max scroll).
4. **Test the shipped artefact.** Pull the function out of the built HTML by regex so the test cannot drift from what ships.
5. **Red-green or it does not count.** Inject a fault, confirm the test fails, restore, confirm it passes. A test that has never failed proves nothing.
6. **Contrast is a gate.** Footer legal links (Terms/Privacy/Restore) must clear **4.5:1** — the element store review inspects. One build shipped at 2.94:1.

## Quick audit — run before calling an interaction done

- [ ] Every tappable has a press state that cancels on slide-off
- [ ] No animation that fails to report a state change
- [ ] Scroll-reactive state uses a threshold and survives a fling
- [ ] Nothing removes DOM to change visual state
- [ ] `prefers-reduced-motion` kills decorative loops only
- [ ] Empty and loading states exist and say what happens next
- [ ] Keyboard moves the primary action, does not cover it
- [ ] Rendered to PNG and visually inspected
- [ ] Behaviour probed or unit-tested, with a red-green check
- [ ] Text contrast ≥ 4.5:1, verified numerically
- [ ] Haptics claimed only where the platform supports them
