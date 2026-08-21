# Gate procedures

One section per gate. Each ends with the artifact that lets you claim the gate passed. If you cannot
point at that artifact, the gate did not pass — say so and stop rather than moving on.

---

## G0 SYSTEM — lock the tokens

Load `premium-design-laws` first; it governs every type and color decision that follows.

1. Produce a **colors + fonts deck** — 2–3 complete options, each showing the full palette in use,
   the type pairing at real sizes, and one sample screen. Not swatch chips.
2. **Stop. Karim picks one.** No screen work happens before that.
3. Turn the chosen option into Figma **variables**: color roles (not raw hexes), type styles,
   spacing scale, radius scale, elevation levels.
4. Default fonts stay banned. Use the curated sets in `premium-design-laws/audit/`.

**Artifact:** a Figma variables collection, plus the deck option Karim named.

**Existing project?** If the design system is already locked (ATHAR's Night Glass, for instance),
G0 is *read the tokens file and use it* — not redesign it. Never re-open a locked system without
being asked.

---

## G1 DESIGN — every screen as a frame

Flow order comes from `onboarding-design` and the vault's onboarding playbooks. Decide the screen
list before drawing any of them, and get it agreed.

Two entry paths:

- **From words** — `figma-generate-design` or `figma-use` to lay out frames from the brief.
- **From an image** — `reference-image-to-figma`. The screenshot is a spec: name every element you
  can see before rebuilding it. Never import the image as the design.

Name frames for the flow position, e.g. `01-welcome`, `02-preferences`, `03-destination`.

**Artifact:** named frames, one per screen, count matching the agreed flow. Include empty, filled,
error and loading states for any screen that has them — they are screens too.

---

## G2 IMPLEMENT — make it real

The difference between a picture of an app and a design that can become one.

- Live text layers. No text baked into images.
- Auto layout everywhere a real layout would flex.
- Components with **variants** for every state — `default` / `selected` / `disabled`.
- Bound variables, not pasted hex values.
- **Real images placed**, at real resolution. WebP fills come in blank in the Figma MCP — convert
  to PNG before `upload_assets`.
- Anything that repeats becomes one component used many times.

`figma-component-craft` covers the component work; `figma-use` does the authoring calls.

**Artifact:** open any frame, select any element — it should be a component instance bound to
variables, not a rectangle with a hardcoded fill.

---

## G3 MOTION — author it in Figma

The gate that is skipped most and matters most. Its output is a **spec**, in this shape:

| element | property | from | to | duration | easing | trigger | stagger |
|---|---|---|---|---|---|---|---|
| content group | opacity | 0 | 1 | 280ms | ease-out | screen enter | — |
| content group | translateY | 12 | 0 | 280ms | ease-out | screen enter | — |
| chip | opacity | 0 | 1 | 200ms | ease-out | screen enter | 40ms |
| CTA fill | opacity | 0.4 | 1 | 160ms | ease-in-out | selection valid | — |

Preferred tool: `figma-use-motion` (requires the `metronome_plugin_api` flag). Without it, use the
fallback ladder in `SKILL.md` — hand-authored table, or Smart Animate prototype read off for timings.

Also decide, and write down:
- What is **shared** across screens and must live outside the navigator
- What the **reduced-motion** variant is for every entry above
- Whether any motion is **state-driven** rather than time-driven — those become derived values in
  code, never timers

**Artifact:** the filled table, one per screen, plus the shared-layer list.

---

## G4 EXTRACT — Figma to running code

`figma-motion-pipeline` decides the route: web target → `figma-implement-motion`; Expo / React
Native → `react-native-motion` and `figma-motion-to-runtime`.

Then:
- `figma-to-production-code` for structure and tokens
- `figma-motion-to-runtime` to turn the G3 table into Reanimated/Moti code
- `rn-screen-transitions` for screen-to-screen

Non-negotiables:
- Components consume the G0 tokens. A raw hex in a screen file is a G4 failure.
- Animate on the UI thread — worklets and shared values, never `setState` per frame.
- `react-native-reanimated/plugin` LAST in `babel.config.js`; `npx expo start --clear` after any
  babel change; wrap the app in `GestureHandlerRootView`.
- Honor `useReducedMotion()` using the variants decided at G3.
- Shared layers stay mounted across the flow.

**Artifact:** the flow running on a device or simulator, with a screenshot or recording.

---

## G5 VERIFY — prove the match

`visual-fidelity-qa` owns this. It ships `visual_diff.py` (Pillow), which produces a 50% overlay,
a difference heatmap, and MAE/RMSE numbers as JSON.

Check all of:

- [ ] Pixel diff per screen against its Figma frame — overlay, heatmap, MAE recorded
- [ ] Every state rendered: empty, filled, error, loading
- [ ] RTL mirrored correctly — layout, icons, and chip/flow direction
- [ ] Dark mode, if the system has one
- [ ] Reduced motion honored
- [ ] Real mid-range Android tested — the iOS simulator hides jank
- [ ] No shared layer flashing on transition

A green build is not evidence. Metrics are sensitive to font rasterization, antialiasing and color
profile, so read them alongside the overlay rather than chasing a number.

**Artifact:** the diff output per screen, plus the checklist above with real results.
