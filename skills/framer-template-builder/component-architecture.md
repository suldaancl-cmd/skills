# Component, variant, CMS and breakpoint architecture

This is the structural layer a marketplace template is graded on before anyone looks at motion. Get this wrong and no amount of animation saves the submission.

## Shared styles are the #1 structural requirement

Framer's own template requirements explicitly check for "shared text and color styles ... used throughout" (framer.com/template-requirements). Build the style system before building any section:

- Define every heading level, body size, and label as a Text Style. Never set one-off font-size/weight/color on individual layers.
- Define every brand color, neutral, and state color (hover, disabled, error) as a Color Style.
- Reason this is graded: buyers restyle the whole template by editing 8-12 style definitions instead of hunting through hundreds of layers. This is the single biggest support-ticket reducer.

## Component variant architecture

Variants are Framer's core reuse mechanism and the reason several patterns in `patterns.md` need zero code:

- **Card components**: base variant + hover variant (image scale, caption slide-up) is the highest-sellability pattern in the research (10/10) precisely because it's pure variant-swap, no code.
- **Pricing components**: build the pricing card as one component with Monthly/Yearly variants; the toggle switches which variant renders. This is how Vectura's "exceptional pricing page" and the toggle+highlighted-tier pattern gets built without a line of code.
- **Nav/link components**: underline-on-hover as a variant (idle vs hover, scaleX 0 to 1). Note the limitation: a variant pair is a single transition per property, so the "exit to the right" origin-swap detail (transform-origin flips on leave, not just reverses) is NOT expressible in variants — that specific micro-detail needs a CSS override or code component. Ship the simple hover-variant version by default.
- **Navbar theme-swap**: Scroll Variant switching per section (light-section variant vs dark-section variant) drives the scroll-linked color-morph pattern.
- **Code components with property controls**: this is Framer's structural moat over Webflow. A code component (React) can expose color/speed/density as visual sliders in the properties panel — this is literally how Jet ($149) sells a "customizable hero animation" without buyers touching code. Any code component you bundle should expose its tunable parameters this way, not hardcode them.

## CMS collection architecture

Framer's requirements grade CMS usage directly: "repeatable content is managed through the CMS where appropriate ... collections and fields use clear naming ... empty entries removed."

Rules that follow from that:
- Anything repeatable — case studies, team members, testimonials, FAQ, blog posts, pricing tiers if they vary per plan — goes in a CMS collection, never hand-duplicated frames.
- Field names must be human-readable (`Client Name`, not `field_3` or `title2`). This is an explicit checklist item, not a style preference.
- Bind CMS fields into component variants so cards restyle automatically per category/tag (e.g., a "Featured" boolean field swaps the card into a highlighted variant).
- Delete placeholder/empty CMS entries before submission — a populated-looking collection with 3 real items and 7 empty ones is a documented rejection driver.
- CMS-driven detail pages (collection list -> item page) is what "advanced CMS" means in bestseller listings like Mugen ($129) and Nord-Å ($99) — build at least list + detail, not just a flat list.

## Breakpoints

Framer ships with responsive breakpoints (desktop / tablet / phone) that each accept layout and variant overrides per size. Practical rules, not specific pixel values (none are in the research data, so none are asserted here):

- Set the desktop layout first, fully styled with Text/Color Styles and component variants in place, then adjust tablet and phone breakpoints — don't design three times from scratch.
- Motion-heavy patterns (horizontal-scroll sections, 3D scroll transforms, cursor-follow effects) commonly get disabled or simplified below tablet, since touch has no hover/cursor and scroll-jacking reads poorly on small screens. Several patterns in `patterns.md` note "disabled below ~992px" for exactly this reason (custom cursor).
- Test every Scroll Section and Sticky-positioned element at the phone breakpoint specifically — sticky/pin behavior is the most common thing that silently breaks on resize.

## Native effects vs. code overrides vs. code components — decision order

Work down this list; stop at the first rung that delivers the effect, because native-only submissions are the safest and fastest through self-audit:

1. **Framer native Effects panel** (Appear, Scroll Transform, Scroll Speed, Scroll Variant, Text Effects, Ticker component, Cursors, Lottie/Spline/video components) — covers the large majority of patterns in `patterns.md` at 8-10/10 sellability with zero code.
2. **A small code override on an existing layer** — for behavior variants (drag physics, magnetic pull, velocity-reactive ticker) that native controls don't expose a slider for.
3. **A bundled code component with property controls** — for a signature/bespoke effect (WebGL hero, Rive state machine) that buyers tune visually without reading code.
4. **Baked media substitute** — when the real effect is too heavy or too custom to hand to buyers (a live shader), record it once as an MP4 loop or Lottie file and ship that instead. It reads the same in a preview and never breaks per-buyer.

Framer's marketplace does no manual review and explicitly permits clean code components — this is the concrete reason several rich-media patterns (Unicorn Studio WebGL, Rive) are shippable in Framer templates but are blocked outright in Webflow marketplace templates (which ban custom code in templates entirely).
