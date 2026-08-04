# Design System, Components & CMS Architecture

Source beat: Webflow-side craft research (140 sites covered) — Client-First, Relume, Webflow
Variables, CMS submission rules.

## One class-naming system, no exceptions

Webflow's allowed formats: default Title Case ("Hero Container Element"), snake_case, Pascal,
camel, kebab, BEM, or a recognized framework (Finsweet's Client-First, Mast, Knockout). Pick one
and use it for the entire project — mixing systems is a QA flag. Max 3-4 stacked combo classes,
descriptive purpose-based names, purge unused styles.

**Client-First** is the de facto community standard: `fs-` prefixes, a
`padding-global`/`container-large` structure-utility pattern, and it's what Relume's 1,000+
component library is built on — so buyers who already know Client-First can edit any
Client-First template instantly, which lowers support burden.

Reference: Finsweet Client-First — https://finsweet.com/client-first · Relume Library —
https://www.relume.io/ · Webflow Submission Guidelines (Design Systems section) —
https://webflow.com/templates/submission-guidelines

## Variables and Variable Modes

Colors, type scale, and spacing live in the Webflow Variables panel as **groups**: Colors
(primary/secondary/background) with light-to-dark ramps, Typography (families/sizes/weights),
Spacing. **Variable Modes** carry responsive overrides per breakpoint (tablet, mobile-landscape,
mobile-portrait). Apply baseline styles to HTML tag selectors (All H1s, All Links, etc. — this
is what the Style Guide page demonstrates), then override with single-purpose classes. Primary
font goes on Body; secondary fonts on specific tags.

This is both a submission requirement and the #1 customizability signal buyers check: swap 3
color variables and 2 font variables and the whole template rebrands.

## Components: Navbar / Footer / CTA are mandatory, everything else should be too

Navbar, Footer, and CTA **must** be Webflow Components on every page — this is an explicit
submission requirement. Beyond the mandatory three, build every repeatable section
(Header 1-N, Feature 1-N, CTA 1-N in the Relume naming convention) as a Component exposing
props/slots/style variants instead of duplicating structure. Rules: concise Title Case
component/variant names, no nested same-type components (no slider inside a slider).

Why: components are what make a template editable by a non-designer buyer — change the nav
once, it updates everywhere. Relume normalized this assembly model across the whole Webflow
economy, so buyers now expect swappable, modular sections (BRIX's "block-based, modular
layouts" pitch converts directly on this expectation).

Reference: Relume Library — https://www.relume.io/ · BRIX Templates —
https://brixtemplates.com/ · Webflow Submission Guidelines (Components section) —
https://webflow.com/templates/submission-guidelines

## CMS collection architecture

Anything repeatable (blog, projects, team, services, testimonials) is a **Collection page**,
never a stack of static sections copy-pasted per item.

Per-collection rules:
- Title Case collection names that read naturally in "This is a Collection of {plural}".
- Singular slugs (`/article/...`).
- Sentence-case field names with help text.
- Reference/multi-reference fields for relationships between collections.
- Conditional visibility where relevant (e.g. show a social icon only if the URL field is
  filled).
- Required flags on essential fields.
- **Field types cannot be changed after creation** — plan them up front.
- Use option fields for fixed value sets; paginate long lists.
- Compress CMS media to AVIF/WebP under 4MB using Webflow's native compression.
- Wire `{Name}` and `{Meta description}` collection fields into each collection template's SEO
  settings for dynamic per-item SEO.
- **Exactly 3-7 realistic dummy items per collection** — no lorem ipsum, no filler. Realistic
  content is also what makes the marketplace preview convert.

CMS presence is what moves a template from the $24 tier to the $34+ tier (see the price ladder
in `submission-and-economics.md`), and it's the single biggest perceived-value signal for
buyers — it makes the template read as a "system," not a static page.

Reference: Atlantic by Azwedo (official Multi Layout / CMS reference) —
https://webflow.com/templates/grading-rubric · BRIX Templates ("Webflow CMS collections
built-in" as core pitch) — https://brixtemplates.com/ · Webflow Submission Guidelines (CMS and
Ecommerce section) — https://webflow.com/templates/submission-guidelines

## Framer equivalents (if building the same template for both marketplaces)

Framer has no user-facing CSS classes — the equivalent discipline is rigorous Color Styles +
Text Styles + component variants (defined once in the assets panel), with per-breakpoint
overrides set directly on each frame instead of Variable Modes. Framer CMS covers the same
ground (collections, references, dynamic SEO title/description per item) with a lower ceiling
on relational complexity — same "3-7 realistic demo items" discipline applies. Framer is
inherently component-first, so the Navbar/Footer/CTA-as-component rule is closer to the
platform's native model than an added discipline.
