---
name: mine-award-site-patterns
description: Mine recent award-winning and benchmark websites into evidence-backed, transferable design patterns without copying their assets or layouts. Use when a user provides reference URLs, screenshots, browser tabs, Awwwards/FWA/CSSDA winners, studio portfolios, or asks to research what makes a site immersive, identify reusable interaction ideas, compare prize-winning work, reverse-engineer visual and motion systems, or turn inspiration into an original design brief.
---

# Mine Award Site Patterns

Convert references into an original design brief. Observe first, infer carefully, and cite every external claim.

## Route the work

- Use browser or web research to verify award status, publication date, credits, and first-party case studies.
- Use `website-stack-teardown` only for passive technical fingerprinting.
- Use `awwwards-winner-playbook` to map findings to Design, Usability, Creativity, and Content.
- Read `references/verified-reference-set.md` when the request mentions recent winners or resembles Karim's saved references.

## Workflow

1. **Define the research question.** Record the audience, business goal, desired emotion, and what must remain usable.
2. **Choose a reference set.** Use two anchor references plus one contrasting reference. Prefer official award pages, studio case studies, and the live site.
3. **Verify provenance.** Record URL, publisher, award/category, date, studio, and whether the claim is observed, documented, or inferred.
4. **Capture states.** Inspect desktop and mobile at hero, first transition, mid-story, conversion moment, footer, menu, hover, loading, and reduced-motion states when available.
5. **Decompose each site** across eight layers:
   - central concept and emotional arc
   - information architecture and conversion path
   - composition, grid, spacing, and density
   - typography roles and kinetic behavior
   - palette, light, texture, and depth
   - scroll, pointer, transition, and feedback choreography
   - media, 3D, WebGL, audio, and fallback strategy
   - implementation, performance, accessibility, and CMS clues
6. **Extract mechanisms, not surfaces.** Translate “large orange orb” into “one persistent object changes role across scenes.” Do not copy layouts, assets, typefaces, shaders, copy, or signature interactions.
7. **Synthesize patterns.** Promote a rule only when it appears in at least two references or is explained by a first-party case study. Label one-off observations as experiments.
8. **Define the novelty boundary.** State what may be borrowed as a principle, what must be redesigned, and the new brand-specific idea that makes the result original.

## Evidence rules

- Cite the exact page supporting each award, technology, or process claim.
- Separate `Observed`, `Documented`, and `Inferred` findings.
- Never infer a library from visual resemblance alone.
- Record the research date because live sites change.
- Treat inaccessible or broken experiences as incomplete evidence.
- Do not download proprietary code or assets unless the license explicitly permits it.

## Required output

```markdown
# Reference Intelligence — <project> — <date>

## Reference matrix
| Site | Verified status | Concept | Type | Color/light | Motion | Tech evidence | Transferable principle |

## Cross-reference patterns
1. <pattern + evidence from at least two sites>

## Originality boundary
- Borrow as principle:
- Redesign completely:
- Brand-specific leap:

## Recommended direction
- Concept sentence:
- Hero mechanism:
- Scroll grammar:
- Type behavior:
- Palette/light arc:
- Mobile/reduced-motion translation:

## Risks and unknowns
- <claim still inferred or unverified>
```

## Quality gate

- Include at least three references and one counterexample.
- Tie every effect to meaning, navigation, or content.
- Reject “effect soup”: one hero mechanism, two supporting motion motifs, and quiet sections between peaks.
- Preserve readable DOM content, native navigation, keyboard access, and a useful mobile experience.
- End with a direction another designer or developer can execute without reopening the references.
