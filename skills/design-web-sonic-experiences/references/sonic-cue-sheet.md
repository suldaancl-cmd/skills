# Web sonic cue sheet

| Scene/state | User action | Visual event | Sound layer | Trigger/input | Mapping | Attack/release | Gain ceiling | Stop condition | Muted fallback |
|---|---|---|---|---|---|---|---|---|---|
|  |  |  | ambience/event/motion/signature |  |  |  |  |  |  |

## Bus graph

```text
ambience ─┐
events ───┼─> master gain ─> destination
media ────┤
voice ────┘
```

Define ducking rules:

- lower ambience when voice or core video plays
- prevent stacked reveal hits
- cap master output conservatively
- fade all buses before suspending or changing routes

## Consent state machine

```text
unknown → offered → enabled ↔ muted
                    ↓
                 suspended (hidden/inactive)
```

## Acceptance tests

- Fresh visit remains silent until a clear user gesture.
- Audio resumes only when the user previously enabled it.
- Mute is visible and keyboard operable at all times.
- Hidden tab and route changes stop or suspend processing.
- Video playback ducks or pauses the ambient mix.
- Muted mode preserves all information and visual feedback.
- Failed audio loads do not block navigation or render.
