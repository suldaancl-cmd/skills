# Motion Architecture

## State model first

Define the product states before keyframes. Example recording state machine:

- `idle`
- `requesting_permission`
- `recording`
- `paused`
- `processing`
- `success`
- `error`

Motion visualizes state transitions; it must not become the only state store.

## Motion tokens

Use project tokens when they exist. Otherwise start with provisional values and validate:

- `duration.instant`: 80 ms
- `duration.quick`: 120 ms
- `duration.standard`: 220 ms
- `duration.emphasis`: 360 ms
- `duration.route`: 480 ms

Define easing tokens by purpose, not by arbitrary curve names. Springs need mass, stiffness, damping, overshoot policy, and completion threshold.

## Continuous input

For sensor, audio, gesture, or scroll:

- Normalize the input range.
- Clamp extreme values.
- Smooth noise.
- Define stale and unavailable states.
- Keep the mapping deterministic.
- Avoid updating React state every frame.
- Provide a noncontinuous reduced-motion alternative.

## Interruption

Specify what happens when:

- The user taps repeatedly.
- Navigation leaves halfway through.
- A gesture reverses.
- New data arrives.
- The app backgrounds.
- Permission is denied.
- The component unmounts.

Animations should cancel or retarget cleanly rather than queueing stale transitions.

## Reduced motion

Reduced motion is not simply “duration = 0.” Choose a meaningful fallback:

- Replace spatial travel with crossfade.
- Remove parallax and continuous tilt.
- Keep essential state feedback.
- Avoid flashing and excessive scale.
- Preserve data legibility and focus order.

## Performance

- Prefer transform and opacity for frequent animation.
- Limit simultaneously blurred translucent layers.
- Optimize and predecode large assets.
- Avoid large bitmap frame sequences.
- Test the real screen, not an isolated component only.
- Measure on target-class hardware.

