---
name: mobbin-motion-research
description: Analyze Mobbin iOS or web flow sequences and convert observed state changes into practical UI motion specifications. Use for animation inspiration, micro-interactions, transitions, onboarding choreography, gesture feedback, loading states, and reduced-motion guidance based on real product flows.
---

# Mobbin Motion Research

Use real flow sequences to derive motion intent while separating observation from recommendation.

## Workflow

1. Translate the request into one journey, such as onboarding progress, bottom-sheet interaction, swipe navigation, loading feedback, or success confirmation.
2. Search with `search_flows`, platform `ios` or `web`, maximum 10 flows per page.
3. Inspect adjacent screen images in order. Record only visible state changes.
4. Cite every referenced flow with its canonical `mobbin_url`.
5. Invoke `animation-principles` when converting observations into implementation guidance.

## Evidence rules

- Label visible differences as **Observed**.
- Label inferred transitions, timing, easing, and choreography as **Recommended**.
- Never claim an exact duration, easing curve, gesture velocity, or video behavior that still frames cannot prove.
- State that Mobbin MCP has no Android platform when Android is requested.
- State that the connector returns flow screenshots, not downloadable animation or video files.

## Motion specification

Return the smallest useful specification:

- Trigger
- Start, intermediate, and end states
- Animated properties
- Recommended duration and easing
- Interruption behavior
- Reduced-motion behavior
- Implementation note for transform/opacity/layout performance

Prefer responsive defaults: 150–250 ms for small transitions, 250–400 ms for larger state changes, ease-out for entrances, ease-in for exits, and 30–50 ms stagger only when hierarchy benefits.

