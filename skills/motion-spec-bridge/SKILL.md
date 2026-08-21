---
name: motion-spec-bridge
description: Use when the same product needs matching motion on web and on mobile — a landing page and its app, a Figma motion spec that has to become both GSAP and Reanimated code, or a design system whose animation tokens must mean the same thing in CSS and in React Native. Defines one platform-neutral motion vocabulary (duration, easing, spring, stagger, choreography) and gives the exact translation table into GSAP, CSS, Reanimated and Compose, plus the places the platforms genuinely cannot match and what to do instead. Reach for this before writing motion twice, or when web and app motion have drifted apart.
---

# Motion Spec Bridge

Teams write motion twice — once in GSAP for the site, once in Reanimated for the app — and the two drift until the brand feels like two brands. The fix is not a shared library. It is a **shared vocabulary** plus an explicit translation table, because the runtimes genuinely differ and pretending otherwise produces the worst of both.

**Companion skills.** Web implementation → `premium-motion-cookbook`, `gsap-scrolltrigger`. Mobile implementation → `reanimated`, `react-native-motion`. Android-specific pitfalls → `android-motion-system`. Performance gate → `motion-performance-budget`. Figma-origin specs → `figma-first-app-pipeline`.

## The one rule

**Specify motion in tokens, not in code.** A spec that says `duration: base, easing: standard-out, stagger: tight` survives translation to any runtime. A spec that says "0.4s cubic-bezier(0.2, 0, 0, 1)" is already a web artifact and will be mistranslated on mobile.

Write the token set once, in the design system. Both platforms consume it.

## The shared vocabulary

### Duration tokens

| Token | Value | Use for |
|---|---|---|
| `instant` | ~70 ms | Immediate feedback — button press, toggle |
| `quick` | ~130 ms | Small state changes, hover, icon morphs |
| `base` | ~220 ms | Default. Most component transitions |
| `slow` | ~350 ms | Screen and container transitions |
| `deliberate` | ~500 ms | Large hero movement, full-screen takeovers |
| `cinematic` | 800 ms+ | Scroll-scrubbed sequences only — never user-initiated UI |

Anything the user initiates should complete within `slow`. Beyond that the interface feels unresponsive regardless of how good the curve is.

### Easing tokens

| Token | Character | Use for |
|---|---|---|
| `standard` | Symmetric ease | Movement that starts and ends on screen |
| `standard-out` | Decelerate | Elements **entering** — fast start, gentle settle |
| `standard-in` | Accelerate | Elements **leaving** — gentle start, fast exit |
| `emphasized` | Strong decelerate | Hero moments, primary transitions |
| `linear` | None | Only for continuous loops and scroll scrubbing |

The rule that makes motion feel professional: **enter decelerating, exit accelerating.** Entering content should arrive and settle; leaving content should get out of the way. Using the same symmetric curve for both is the most common amateur signature.

### Spring tokens

Springs are described by feel, not by numbers, because the numeric parameters differ between runtimes:

| Token | Feel | Use for |
|---|---|---|
| `snappy` | Fast, minimal overshoot | Toggles, small controls |
| `smooth` | No overshoot, natural settle | Sheets, drawers, most gestures |
| `bouncy` | Visible overshoot | Playful moments, success states — use sparingly |
| `gentle` | Slow, heavily damped | Large surfaces, ambient movement |

**Use springs for anything the user directly manipulates** — drags, sheets, dismissals — because the motion should respond to gesture velocity. **Use durations for anything the system initiates**, because those need predictable timing.

### Stagger tokens

| Token | Gap | Use for |
|---|---|---|
| `tight` | ~25 ms | Long lists — keeps total time sane |
| `base` | ~50 ms | Default cascade |
| `loose` | ~90 ms | Short sets of 3–5 hero items |

Cap total stagger time. A 40-item list at `base` takes two seconds to finish — clamp the total rather than the per-item gap.

## Translation table

| Concept | Web — GSAP | Web — CSS | Mobile — Reanimated | Android — Compose |
|---|---|---|---|---|
| Duration | `duration` in **seconds** | `transition-duration` in **ms** | `withTiming({duration})` in **ms** | `tween(durationMillis)` |
| Easing | `ease` string or `CustomEase` | `cubic-bezier()` | `Easing.bezier()` | `CubicBezierEasing` |
| Spring | `elastic` / physics plugins | Not natively expressible | `withSpring({damping, stiffness})` | `spring(dampingRatio, stiffness)` |
| Stagger | `stagger` on a tween | Manual per-element delay | `withDelay(index * gap)` | `delayMillis` |
| Sequence | `timeline()` | Chained delays | `withSequence()` | `AnimatedVisibility` / sequence |
| Repeat | `repeat`, `yoyo` | `animation-iteration-count` | `withRepeat(anim, n, reverse)` | `infiniteRepeatable` |
| Scroll-linked | `ScrollTrigger` with `scrub` | `animation-timeline` (limited) | `useAnimatedScrollHandler` | `nestedScroll` |
| Gesture-linked | Draggable / pointer events | Not expressible | `Gesture` + shared values | `pointerInput` |

**The unit trap: GSAP takes seconds, everything else takes milliseconds.** A token table stored in milliseconds must divide by 1000 on the GSAP side. This is the most frequent bug when porting a spec, and it fails silently by producing motion 1000× too slow.

## What does not translate

Be explicit about these rather than approximating badly.

| Web capability | Mobile reality |
|---|---|
| Scroll-linked page choreography | Mobile scroll is shorter and gesture-driven. Do not port a pinned scroll sequence to an app screen — redesign it as a gesture or a paged flow |
| CSS filters and blend modes | Expensive or unavailable in RN. Use a dedicated graphics layer for real blur |
| Hover states | No hover on touch. Every hover-revealed affordance needs a visible mobile equivalent, not a long-press |
| Arbitrary DOM animation | RN animates a view tree, not a document. There is no equivalent of animating text nodes directly |
| Cursor effects | No cursor. The mobile analogue is haptics and press states |

| Mobile capability | Web reality |
|---|---|
| Gesture velocity handoff into a spring | Possible but manual; no native equivalent |
| Haptic feedback | Very limited and inconsistent on web |
| Native screen transitions | Must be hand-built |
| Interruptible spring on drag | Requires deliberate implementation |

**Never force parity where the platform disagrees.** The goal is that both feel like the same brand, not that both run the same animation. A hover effect ported as a long-press is worse than a well-designed press state.

## Cross-platform pitfalls

- **Seconds versus milliseconds.** Stated twice because it causes most of the bugs.
- **Reduced motion must be honoured on both.** Web reads `prefers-reduced-motion`; mobile reads the OS accessibility setting. A spec is incomplete until it defines the reduced variant of each animation.
- **Android animator duration scale** can multiply or zero every duration. Do not fight it.
- **60 fps is not universal.** High-refresh displays exist on both. Drive by time, never by frame count.
- **Only `transform` and `opacity` are cheap on both.** This constraint is shared, which conveniently means a spec written to it ports cleanly.
- **Test the mobile side on a real mid-range Android.** A spec validated only on iOS will feel different in the place most users are.

## Spec template

Hand this to both implementers:

```
MOTION SPEC — <component or flow>

Trigger      : <what starts it>
Elements     : <what moves>
Properties   : <transform / opacity — flag any exception and why>
Duration     : <token>
Easing       : <token — enter and exit stated separately>
Spring       : <token, if gesture-driven>
Stagger      : <token, plus total cap>
Sequence     : <ordered steps, if a timeline>
Reduced      : <what happens under reduced motion — required>
Web note     : <anything GSAP-specific>
Mobile note  : <anything Reanimated-specific>
Not ported   : <what deliberately differs, and the replacement>
```

The `Reduced` and `Not ported` lines are the ones teams skip and the ones that cause rework. Neither is optional.

## Verification

Before reporting motion as matched across platforms, point to:

- the token table both implementations actually import, not two hardcoded copies
- side-by-side screen recordings of the same interaction on web and on a real Android device
- reduced-motion forced on and recorded on both platforms
- an explicit written list of what deliberately differs

Two implementations that merely look similar in a still frame have not been verified. If only one platform was checked, say which, and label the other unverified.
