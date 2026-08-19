---
name: premium-mobile-experience
description: Audit or implement premium mobile interaction quality through purposeful motion, haptics, illustrations, feedback, latency handling, and platform craft. Use when an app works but feels generic, static, inconsistent, or unpolished; not for initial product scoping.
---

# Premium mobile experience

Improve perceived quality without turning every screen into a showreel.

## Audit the experience in layers

1. **Correctness:** actions work, state persists, and errors recover.
2. **Responsiveness:** every interaction acknowledges input immediately.
3. **Continuity:** navigation and state changes preserve spatial and causal relationships.
4. **Character:** brand-specific illustration, sound, motion, and copy appear at meaningful moments.
5. **Invisible craft:** keyboard, camera, permissions, loading, gestures, and interruption feel deliberate.

Fix lower layers before adding decorative motion.

## Assign motion a job

Every animation should provide at least one of:

- Orientation.
- Cause and effect.
- State feedback.
- Attention hierarchy.
- Brand expression.

Remove motion that delays the primary task, competes for attention, or hides latency. Use a small motion vocabulary and consistent physical behavior.

## Implementation decisions

- Use native transitions for platform navigation and controls when suitable.
- Use a UI-thread animation runtime for gesture-driven or interruptible interaction.
- Use a canvas runtime for shader, particle, or custom rendering work that truly requires it.
- Use Lottie/Rive for controlled authored assets, not for dynamic layout choreography.
- Respect reduced motion, font scaling, contrast, screen readers, and touch-target size.
- Keep expensive blur, shadows, masks, and offscreen rendering within a measured performance budget.
- Add haptics only to confirm a meaningful state change; do not fire on passive motion.

## Design premium states

Cover press, focus, selection, drag, refresh, optimistic update, pending, partial result, empty, offline, permission denied, failure, success, and destructive confirmation. Prefer skeletons or stable placeholders that preserve layout over blocking spinners.

## Validate

- Test on real iOS and Android hardware, including a slower device when available.
- Record representative interactions and inspect dropped frames, layout jumps, keyboard collisions, delayed feedback, and accidental double actions.
- Verify interruption: backgrounding, navigation back, rapid repeat taps, network loss, and reduced-motion mode.
- Compare the experience with product-specific references; do not copy unrelated visual flourishes.

Use [references/premium-experience-checklist.md](references/premium-experience-checklist.md) for a formal audit. Report improvements by user impact and implementation cost.
