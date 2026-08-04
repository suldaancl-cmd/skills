# Scroll cue sheet

Complete one row per beat before implementation.

| Beat | Purpose | Content | Entry | Progress behavior | Exit | Scroll length | DOM state | Canvas/media state | Sound | Mobile | Reduced motion | Focus/anchor |
|---|---|---|---|---|---|---:|---|---|---|---|---|---|
| 01 |  |  |  | trigger/scrub/pin/native |  | vh |  |  |  |  |  |  |

## Motion tokens

| Token | Value | Use |
|---|---|---|
| `--motion-fast` | 160–220ms | direct feedback |
| `--motion-base` | 300–500ms | component transitions |
| `--motion-scene` | progress-driven | large narrative change |
| enter easing | strong ease-out | arrivals |
| exit easing | ease-in | departures |
| scrub smoothing | smallest useful value | prevent lag from detaching input and response |

## Curve sketch

Mark intensity from 0–5. Avoid a constant 5.

```text
beat       01 02 03 04 05 06 07
intensity   2  1  4  2  5  1  3
reading     y  y  n  y  n  y  y
```

## Acceptance tests

- Back-scroll returns every scene to the correct prior state.
- Refresh at the middle of the page restores a coherent state.
- Resize and font load do not misalign triggers.
- Keyboard focus never lands inside hidden or off-screen content.
- Mobile content order remains logical without pinning.
- Reduced-motion users receive the same information and actions.
