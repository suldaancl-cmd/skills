# React and Next.js Web Playbook

## Architecture

- Respect the existing router, server/client component boundaries, data fetching, styling, and design system.
- Do not convert every Figma node into a component. Extract components by reuse, state, and ownership.
- Keep content and data semantic for search, accessibility, selection, and localization.

## Responsive layout

- Define container behavior and breakpoints from product needs, not only the reference screenshot.
- Use normal flow, grid, and flex for UI.
- Reserve absolute positioning for deliberate art composition and overlays.
- Use `object-fit`/position policies for background art.
- Test zoom, reflow, long strings, keyboard navigation, and high-contrast modes where applicable.

## Effects and motion

- Prefer CSS for simple state transitions.
- Use the existing motion library for component/layout choreography.
- Use GSAP only for timeline/scroll complexity that justifies it.
- Use Three.js/R3F only when true 3D interaction is product-essential.
- Provide reduced-motion styles and avoid scroll hijacking.

## Images and performance

- Serve responsive images in modern formats with correct dimensions.
- Avoid shipping a mobile screenshot as the entire page.
- Limit large translucent blurs, compositing layers, and shader work.
- Measure layout shift, input responsiveness, and loading behavior in the actual page.

## Accessibility and localization

- Use semantic HTML and native controls unless a custom control is necessary.
- Preserve focus visibility and predictable keyboard order.
- Set document direction by locale and test mixed-direction content.
- Keep text and labels outside images and animation files.

