# Motion Tokens

The exact, reusable animation values behind OpenAI/Anthropic-tier launch films. Use these
verbatim — they are the difference between "expensive" and "off". Derived from teardown of the
4 anchor references + GSAP/Motion/Material/Carbon motion docs (sources in
`research/02-motion-design-language.md`).

## Core gesture table

| Gesture | Duration | Easing (cubic-bezier) | Spring alt (stiffness/damping/mass) | Notes |
|---|---|---|---|---|
| **Word enter (mask reveal)** | 480ms | `cubic-bezier(0.16, 1, 0.3, 1)` | — | Expo-out. Text slides up from 24px below; clip mask reveals simultaneously. The workhorse — ~80% of headline animation. |
| **Hero display appear** | 600ms | `cubic-bezier(0.22, 1, 0.36, 1)` | — | Slower expo for maximum-weight type. |
| **UI frame float (idle)** | 4000ms loop | `cubic-bezier(0.45, 0, 0.55, 1)` | 80 / 12 / 1.2 | Sinusoidal Y ±8px, very slow; subtle X tilt ±1.5°. |
| **UI frame enter** | 700ms | `cubic-bezier(0.34, 1.56, 0.64, 1)` | 260 / 20 / 1 | Slight overshoot (back-ease) on scale 0.92→1.0, opacity 0→1. |
| **Scene fade / cut** | 200–250ms | `cubic-bezier(0.4, 0, 1, 1)` | — | Ease-in only; cuts feel snappier than dissolves. |
| **Cross-dissolve** | 400ms | `cubic-bezier(0, 0, 0.58, 1)` | — | Between adjacent UI states only. |
| **Stagger (multi-element)** | 60–80ms / item | per-element | — | Cards 70ms; list items 60ms; words in a headline 40–55ms. |
| **Accent word color flash** | 150ms | `cubic-bezier(0.25, 0.46, 0.45, 0.94)` | — | Clip-path wipe from left. Does NOT fade — snaps/wipes. |
| **Logo outro scale settle** | 800ms | `cubic-bezier(0.34, 1.2, 0.64, 1)` | 200 / 18 / 1 | Logo enters at 85% scale, slight spring overshoot to 100%. |
| **Cursor move / click** | 300ms move / 80ms click | `cubic-bezier(0.25, 0.1, 0.25, 1)` | — | Lerp, not teleport. Click = scale pulse 1.0→0.85→1.0. |
| **Terminal typing sim** | 35–55ms / char | linear (+ jitter ±10ms) | — | Occasional 120ms "pause". Paste = single frame. Cursor blink 500ms. |

## Product-UI micro-interactions

- **Click feedback:** scale pulse `1.0 → 0.78 → 1.0` over 120ms + `rgba(255,255,255,0.2)` ripple ring from click point.
- **Hover:** custom cursor scale `1.0 → 1.2` over 80ms.
- **Scroll sim:** `easeInOutQuart` over 800–1200ms per viewport; overshoot 12–20px then 200ms settle-back. Never linear.
- **Typing sim:** 35–55ms/char with ±10ms jitter; batch paste in one frame; cursor blink 500ms on/off.
- **UI frame shadow:** `0 40px 80px rgba(0,0,0,0.12)` on light bg (deepen on dark).

## Motion personality by brand type

| Brand type | Motion character | Avoid |
|---|---|---|
| Engineering / precision (Codex, Claude Code) | Snappy, staccato, no bounce | Bouncy springs, playful overshoot |
| Consumer / creative (whop, lifestyle) | Springy, slight overshoot, warmth | Stiff linear, clinical timing |

Maps to the brand-kit `motionStyle` key: `snap` (ease-in cuts, no overshoot) / `spring`
(overshoot on enters) / `ease` (gentle expo, organic).

## Remotion implementation notes

- Remotion renders deterministically by frame. Convert ms → frames: `frames = ms/1000 * fps`.
  At 60fps, 480ms = 28.8 → 29 frames; at 24fps = 11.5 → 12 frames.
- Use `interpolate()` with the cubic-bezier via `Easing.bezier(x1,y1,x2,y2)` for the curves
  above, or Remotion's `spring({fps, config:{stiffness, damping, mass}})` for the spring rows.
- For kinetic type, GSAP SplitText (in a `<Sequence>`) or manual per-word `<span>` with
  staggered `delay = wordIndex * staggerFrames`.
- Honor rule #3: budget ≥ 1.2s of *settled* hold at the end of every beat before the cut.
