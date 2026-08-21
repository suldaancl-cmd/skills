# Worked example — reading the Polle onboarding reel

Source: <https://x.com/Triopixels/status/2089007755373715819> — Amjad (`@Triopixels`), 13s,
caption "Onboarding flow for Polle". Read here from 13 extracted frames, not from the caption.

This is what G1 input looks like when the brief is "make it like this".

## 1. Screen skeleton (repeats on every frame)

```
full-bleed photo, heavily darkened
  └ logo chip (pill, glass)          ← screen 1 only
  └ headline, 2-3 lines, white, tight leading
  └ support line, one sentence, grey, ~40% the headline size
  └ INPUT ZONE                        ← the only part that changes shape
  └ full-width glass pill CTA, bottom, DIMMED until input is valid
```

## 2. The three screens

| # | Headline | Input zone | CTA |
|---|---|---|---|
| 1 | "Plan better. / Go further. / Make memories." | none | `Get Started`, enabled |
| 2 | "What kind of trip are you after?" | 6 emoji chips — Hidden gems, Meet people, Adventure, Nightlife, Food & culture, Slow & relaxing | `Continue`, dimmed until one is picked |
| 3 | "Where are you going?" | search field + 4 country chips with flags + `Surprise me` | `Continue`, dimmed |

## 3. Shared vs swapped — the detail most rebuilds miss

**The background photo never changes.** Same coastal cliff shot across all three screens. Only the
foreground content swaps. That single decision is what makes the flow feel continuous instead of
like three separate screens.

In code this means: **one persistent background layer outside the navigator**, with only the content
layer transitioning. If you rebuild this by putting the photo inside each screen, you get a flash on
every transition and the whole effect dies.

## 4. Motion inventory

- Content cross-fades and rises slightly on screen advance; background holds still
- Chips enter staggered, not all at once
- CTA transitions dim → solid when the selection becomes valid — this is state-driven, not timed
- No layout animation, no parallax, no scroll effects

Everything is entrance motion on the content layer plus one state transition on the CTA. That is
the entire motion budget, and it is enough.

## 5. Accent

There isn't a saturated one. The whole design is white and grey glass over a desaturated photo,
which is why the flag emoji on the country chips read as color accents. If you rebuild this with a
brand accent, apply it to exactly one element — most likely the active chip border or the enabled
CTA — and leave everything else neutral.

## 6. Pattern name

This is a **preference-quiz onboarding**: ask before you tell, collect two cheap taps, personalize.
It matches the order in the vault's `playbook_onboarding_paywall_sequence_marco` — desire first,
features later, account creation LAST. Polle asks nothing about identity in these three screens.

## 7. What this becomes at each gate

- **G0** — glass tokens: blur radius, fill opacity, border opacity, dim overlay strength over photo
- **G1** — 3 frames, plus the empty and selected states of screens 2 and 3
- **G2** — one `Chip` component with `default` / `selected` variants; one `CTA` with
  `enabled` / `dimmed`; background as a shared layer, not a per-frame image fill
- **G3** — spec: content opacity 0→1 and translateY 12→0 over ~280ms ease-out, chips staggered
  ~40ms apart, CTA fill opacity change on state. **Measure these off the video or the prototype —
  the numbers here are a starting shape, not measured truth.**
- **G4** — Expo screens, background outside the navigator, chips as a multi-select, CTA disabled
  until `selected.length > 0`
- **G5** — pixel diff each screen against its Figma frame; verify the background does not flash on
  transition; verify RTL mirrors the chip flow

## Caveat

The motion timings above are **inferred from a 13-second reel sampled at 1fps** — enough to see
what moves and in what order, not enough to measure exact durations. Treat them as the shape to
verify, never as measured values. Nothing in the post states the tool used to author the motion.
