# Type motion specification

## Route

| Role | Family | License/source | Axes | Size/leading | Measure | Static reason | Motion role |
|---|---|---|---|---|---|---|---|
| Display |  |  |  |  |  |  |  |
| Body |  |  |  |  |  |  |  |
| Utility |  |  |  |  |  |  |  |
| Arabic display |  |  |  |  |  |  |  |
| Arabic body |  |  |  |  |  |  |  |

## Motif

```text
name:
meaning:
split unit:
start state:
end state:
trigger:
duration or progress range:
easing:
interrupt behavior:
mobile translation:
reduced-motion translation:
```

## Component choreography

| Component | Trigger | Unit | Properties | Stagger | Final readable state | AR/RTL rule | Fallback |
|---|---|---|---|---|---|---|---|
| Hero |  |  |  |  |  |  |  |
| Section heading |  |  |  |  |  |  |  |
| Navigation |  |  |  |  |  |  |  |
| CTA |  |  |  |  |  |  |  |

## Acceptance tests

- Content remains readable before web fonts load.
- No layout overflow at 320px or 200% zoom.
- Arabic shaping and DOM order remain intact.
- Screen readers announce each phrase once.
- Reduced motion displays the final state immediately.
- Off-screen motion pauses and no essential body copy continuously animates.
