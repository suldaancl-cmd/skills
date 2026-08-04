---
name: design-web-sonic-experiences
description: Design optional, consent-based sound systems for immersive websites using Web Audio, media elements, spatial cues, scroll or pointer reactivity, ambience, UI feedback, and audio-reactive visuals. Use when a site should feel cinematic, musical, tactile, spatial, game-like, or emotionally responsive; when users mention web sound, headphones, audio-reactive shaders, scroll-velocity sound, sonic branding, ambient worlds, or interaction audio; or when a video-focused sound workflow must be translated into accessible live browser behavior.
---

# Design Web Sonic Experiences

Use sound only when it adds meaning. Silence and user control are part of the design.

## Decide whether sound belongs

Choose one:

- **none:** the concept gains nothing from sound
- **optional ambience:** atmosphere after explicit opt-in
- **interaction cues:** short confirmation, material, or spatial feedback
- **narrative score:** scene-based layers supporting a story
- **audio-reactive world:** visuals respond to analyzed audio or microphone input

Reject sound when it masks weak visual hierarchy, repeats information, competes with core media, or lacks a visible control.

## Consent and control are mandatory

- Start or resume `AudioContext` only from a user gesture.
- Never surprise the user with audible autoplay.
- Provide persistent mute/unmute and volume controls using semantic buttons/inputs.
- Remember preference locally without making sound unavoidable on return.
- Pause or attenuate when the document is hidden, a video starts, a call/voice interaction begins, or the experience loses focus.
- Respect assistive technology and keyboard input; do not make audio the only feedback channel.

## Build a sonic concept

Derive four layers from the same central metaphor:

1. **bed:** low-information ambience establishing material and space
2. **events:** short cues for meaningful state changes
3. **motion:** continuous or granular response to scroll velocity, cursor, drag, proximity, or physics
4. **signature:** one memorable sonic event reserved for the main reveal

Keep the palette small. Reuse timbre and spatial rules so the site sounds like one instrument.

## Map sound to interaction

Use `references/sonic-cue-sheet.md`.

- Position drives location in the narrative.
- Smoothed velocity may drive intensity, filtering, playback rate, or step frequency.
- Direction may drive stereo position or rising/falling motifs.
- Proximity may drive gain or brightness.
- State changes trigger discrete cues.

Smooth all continuous inputs. Clamp ranges. Add hysteresis/dead zones so tiny scroll noise does not chatter.

## Architecture

- Use `<audio>` for straightforward music or narration and Web Audio for routing, analysis, spatialization, synthesis, and precise mixing.
- Create one audio manager and one `AudioContext`; do not let components create competing contexts.
- Route layers through gain buses: `master`, `ambience`, `events`, `media`, and optional `voice`.
- Decode or stream after consent; lazy-load nonessential layers.
- Fade on scene changes and disposal; never hard-cut looping ambience unless conceptually intended.
- Dispose nodes, event listeners, media sources, and animation loops on route changes.

## Audio-reactive visuals

- Extract a small number of stable features such as smoothed low-frequency energy, overall RMS, or selected frequency bands.
- Map features to restrained parameters such as emission, particle tension, displacement, or light—not every visual property.
- Apply attack/release smoothing so visuals feel organic rather than mechanically noisy.
- Provide a non-audio animation path when sound is muted or unavailable.

## Performance and delivery

- Use compressed web formats with a tested fallback.
- Keep initial page paint independent from audio downloads.
- Avoid many simultaneous decoded long files on mobile.
- Suspend processing while hidden or muted when possible.
- Test Bluetooth latency, mobile Safari, background tabs, failed autoplay, slow networks, and route changes.

## Required deliverable

1. sound/no-sound decision and rationale
2. sonic palette and signature event
3. completed cue sheet
4. consent and control UX
5. bus graph and asset/loading plan
6. audio-reactive mappings with smoothing ranges
7. mute, hidden-tab, video-conflict, mobile, and no-audio fallbacks
8. acceptance tests

## Quality gate

- The experience is complete and understandable while muted.
- The first audible sound follows deliberate user consent.
- There is always a visible, keyboard-operable stop/mute control.
- Sound responds to meaning and action, not every pixel of movement.
- No cue repeats frequently enough to become irritating.
- The mix leaves room for speech and embedded video.

## Evidence base

- MDN autoplay guide: https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Autoplay
- MDN Web Audio best practices: https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API/Best_practices
- MDN Using Web Audio: https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API/Using_Web_Audio_API
- The Spark: https://tympanus.net/codrops/2026/01/09/the-spark-engineering-an-immersive-story-first-web-experience/
- Aether 1: https://tympanus.net/codrops/2025/08/06/building-aether-1-sound-without-boundaries/
- Frequency Breathwork: https://tympanus.net/codrops/2025/12/29/frequency-breathwork-translating-the-invisible-rhythm-of-breath-into-digital-form/
- Arts Corporation: https://tympanus.net/codrops/2025/04/22/designing-for-flow-not-frustration-the-transformation-of-arts-corporation/
