# Layout Reference

> Auto-extracted from live DOM. Use this to understand how the site is structured spatially.

## Spacing System

**Base grid:** 4px

**Scale:** `2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30` px

| Spacing | Semantic Use |
|---------|-------------|
| 4px | Tight — within a component |
| 8px | Medium — between sibling items |
| 16px | Wide — between sections |
| 32px | Vast — major section breaks |

## Flex Layouts

| Element | Direction | Justify | Align | Gap | Children |
|---------|-----------|---------|-------|-----|----------|
| `nav#navigation-menu.hds-navigation-menu.navigation-menu` | row | — | center | 16px | 4 |
| `div.rc-bg__buttons.rc-bg__buttons--row1` | row | — | — | — | 2 |
| `div.rc-bg__buttons.rc-bg__buttons--row1` | row | — | — | — | 2 |
| `div.rc-bg__buttons.rc-bg__buttons--row3` | row | — | — | — | 2 |
| `div.rc-bg__buttons.rc-bg__buttons--row4` | row | — | — | — | 2 |
| `div.hero-cta-group` | row | center | center | 20px | 1 |
| `div.rc-bg__buttons__container` | row | — | center | — | 8 |
| `div.rc-bg__buttons__container` | row | — | center | — | 8 |
| `div.rc-bg__buttons__container` | row | — | center | — | 11 |
| `div.rc-bg__buttons__container` | row | — | center | — | 8 |
| `div.rc-bg__buttons__container` | row | — | center | — | 8 |
| `div.rc-bg__buttons__container` | row | — | center | — | 8 |
| `div.rc-bg__buttons__container` | row | — | center | — | 10 |
| `div.rc-bg__buttons__container` | row | — | center | — | 6 |

## Grid Layouts

| Element | Template Columns | Gap | Children |
|---------|-----------------|-----|----------|
| `div.rc-grid.rc-gap-5` | `1440px` | 0px | 2 |
| `div.rc-bg__buttons__wrapper` | `1440px` | — | 4 |
| `div.za-wrapper__body` | `320px 908px` | normal 60px | 2 |
| `div.rc-grid.rc-relative` | `1440px` | — | 3 |
| `div.rc-trusted__container` | `33.0781px 33.0781px 33.0781px 33.0781px 33.0781px ` | 10px | 4 |

## Structural Containers

### `<header>` (`header.cb-header`)

```
display:          block
children:         1
```

### `<footer>` (`footer.deferred-section.rc-bg-contain`)

```
display:          block
children:         2
```

### `<nav>` (`nav#navigation-menu.hds-navigation-menu.navigation-menu`)

```
display:          flex
flex-direction:   row
justify-content:  —
align-items:      center
gap:              16px
children:         4
```

## Layout Rules

- **Container max-width:** `1440px` — always center with `margin: auto`
- Primary layout system: **Flexbox**
- Secondary layout system: **CSS Grid** (used for card grids and multi-column layouts)
- Every spacing value must be a multiple of **4px**
- Never use arbitrary margin/padding values outside the spacing scale

