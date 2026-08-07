# Interaction Reference

> Micro-interactions extracted from live DOM. Recreate these exactly for authentic feel.

## Coverage

| Component Type | Count | States Captured |
|----------------|-------|----------------|
| Button | 3 | default, hover, focus |
| Role Button | 3 | default, hover, focus |
| Link | 3 | default, focus, hover |

## Transition System

These transition declarations were extracted from interactive elements:

```css
transition: color 0.2s, background 0.2s;
transition: opacity 0.2s, background-color 0.2s;
transition: color 0.24s cubic-bezier(0.45, 0.05, 0.55, 0.95), background-color 0.24s cubic-bezier(0.45, 0.05, 0.55, 0.95), border-color 0.24s cubic-bezier(0.45, 0.05, 0.55, 0.95);
transition: all;
transition: opacity 0.24s cubic-bezier(0.45, 0.05, 0.55, 0.95);
```

Apply these to all interactive elements. Never invent new durations or easings.

## Button Interactions

### Button 1 — `Open view mode toggle`

**States:**

- Default: `../screens/states/button-1-default.png`
- Hover: `../screens/states/button-1-hover.png`
- Focus: `../screens/states/button-1-focus.png`

**On hover:**

```css
/* color: rgba(255, 255, 255, 0.85) → */ color: rgb(255, 255, 255);
/* border-color: rgba(255, 255, 255, 0.85) → */ border-color: rgb(255, 255, 255);
/* outline: rgba(255, 255, 255, 0.85) none 3px → */ outline: rgb(255, 255, 255) none 3px;
/* outline-color: rgba(255, 255, 255, 0.85) → */ outline-color: rgb(255, 255, 255);
```

**Transition:** `color 0.2s, background 0.2s`

### Button 2 — `Dismiss banner`

**States:**

- Default: `../screens/states/button-2-default.png`
- Hover: `../screens/states/button-2-hover.png`
- Focus: `../screens/states/button-2-focus.png`

**On hover:**

```css
/* background-color: rgba(0, 0, 0, 0) → */ background-color: rgba(1, 42, 56, 0.06);
/* opacity: 0.75 → */ opacity: 1;
```

**Transition:** `opacity 0.2s, background-color 0.2s`

### Button 3 — `Products`

**States:**

- Default: `../screens/states/button-3-default.png`
- Hover: `../screens/states/button-3-hover.png`
- Focus: `../screens/states/button-3-focus.png`

**On focus:**

```css
/* outline: rgb(1, 42, 56) none 3px → */ outline: rgb(255, 51, 0) solid 2px;
/* outline-color: rgb(1, 42, 56) → */ outline-color: rgb(255, 51, 0);
```

**Transition:** `color 0.24s cubic-bezier(0.45, 0.05, 0.55, 0.95), background-color 0.24s cubic-bezier(0.45, 0.05, 0.55, 0.95), border-color 0.24s cubic-bezier(0.45, 0.05, 0.55, 0.95)`

## Role Button Interactions

### Role Button 1 — `Go to slide 1`

**States:**

- Default: `../screens/states/role-button-1-default.png`
- Hover: `../screens/states/role-button-1-hover.png`
- Focus: `../screens/states/role-button-1-focus.png`

**On focus:**

```css
/* outline: rgb(1, 42, 56) none 3px → */ outline: rgb(0, 187, 255) solid 3px;
/* outline-color: rgb(1, 42, 56) → */ outline-color: rgb(0, 187, 255);
```

**Transition:** `all`

### Role Button 2 — `AI`

**States:**

- Default: `../screens/states/role-button-2-default.png`
- Hover: `../screens/states/role-button-2-hover.png`
- Focus: `../screens/states/role-button-2-focus.png`

**On focus:**

```css
/* outline: rgb(1, 42, 56) none 3px → */ outline: rgb(0, 187, 255) solid 3px;
/* outline-color: rgb(1, 42, 56) → */ outline-color: rgb(0, 187, 255);
```

**Transition:** `all`

### Role Button 3 — `Media`

**States:**

- Default: `../screens/states/role-button-3-default.png`
- Hover: `../screens/states/role-button-3-hover.png`
- Focus: `../screens/states/role-button-3-focus.png`

**On focus:**

```css
/* outline: rgb(1, 42, 56) none 3px → */ outline: rgb(0, 187, 255) solid 3px;
/* outline-color: rgb(1, 42, 56) → */ outline-color: rgb(0, 187, 255);
```

**Transition:** `all`

## Link Interactions

### Link 1 — `Accessibility Screen-Reader Guide, Feedb`

**States:**

- Default: `../screens/states/link-1-default.png`
- Focus: `../screens/states/link-1-focus.png`

**Transition:** `all`

_No visible style changes detected for this element._

### Link 2 — `Learn more`

**States:**

- Default: `../screens/states/link-2-default.png`
- Hover: `../screens/states/link-2-hover.png`
- Focus: `../screens/states/link-2-focus.png`

**On focus:**

```css
/* outline: rgb(255, 51, 0) none 3px → */ outline: rgb(1, 42, 56) solid 2px;
/* outline-color: rgb(255, 51, 0) → */ outline-color: rgb(1, 42, 56);
```

**Transition:** `all`

### Link 3 — `Chargebee homepage`

**States:**

- Default: `../screens/states/link-3-default.png`
- Hover: `../screens/states/link-3-hover.png`
- Focus: `../screens/states/link-3-focus.png`

**On hover:**

```css
/* opacity: 1 → */ opacity: 0.7;
```

**On focus:**

```css
/* outline: rgb(1, 42, 56) none 3px → */ outline: rgb(255, 51, 0) solid 2px;
/* outline-color: rgb(1, 42, 56) → */ outline-color: rgb(255, 51, 0);
```

**Transition:** `opacity 0.24s cubic-bezier(0.45, 0.05, 0.55, 0.95)`

## Interaction Rules

- Accent color `#ff5722` is used for focus rings, active states, and hover highlights
- Hover effects use **opacity** changes, not color shifts
- Hover effects include **color transitions** — use the extracted values, not approximations
- Focus states use **outline** (not box-shadow) — always match the extracted focus ring
- Transition durations in use: `0.2s`, `0.24s`
- Always respect `prefers-reduced-motion` — set all transitions to `0s` when enabled

