# context/designs/ — one visual reference per screen

Drop an image here for every screen before the agent builds it. With a reference it matches;
without one it invents, and what it invents drifts from the last thing it invented.

## Naming

`<route-or-screen>.png` — the same name as the route in `01-project-overview.md`.

```
home.png
profile.png
job-detail.png
paywall.png
dashboard.png
```

Variants get a suffix: `paywall-annual.png`, `home-mobile.png`, `home-rtl.png`.

## Where a reference comes from

- Figma frame export (best — use the Figma MCP to read tokens directly rather than eyeballing)
- An approved screenshot from the deck in `DESIGN.md`
- A Mobbin reference, if the pattern is being adapted rather than invented — note the source in a sibling `.md`

## Rules

- A reference here is **the target**, not a suggestion. If the build diverges, the build is wrong.
- An approved screenshot becomes a LOCKED spec. Re-verify live against it after every deploy.
- References do not override `06-ui-tokens.md`. If a reference shows a color that is not a token,
  either add the token or fix the reference — never hard-code it.
- RTL screens need their own reference. A mirrored Latin screen is not an Arabic design.

Empty is fine at the start. Add each screen's reference before that screen's feature is built,
not all at once up front.
