# Agent instruction template

Include only repository-specific facts that change agent behavior.

```markdown
# Repository purpose

<One paragraph: users, product outcome, and non-goals.>

## Architecture boundaries

- Client:
- Trusted backend:
- Source of truth:
- Background workers:
- External providers:

## Commands

- Install:
- Run:
- Typecheck:
- Lint:
- Test targeted:
- Test full:
- Build:

## Implementation rules

- <Directory ownership or patterns that are not obvious from code.>
- <Generated files or migrations that must not be edited directly.>

## Security and data invariants

- <Secret boundary.>
- <Authorization/RLS rule.>
- <Money, deletion, or irreversible-action rule.>

## UI quality

- <Design source, RTL, accessibility, supported form factors.>

## Definition of done

- <Observable checks and evidence.>
```

Prefer nested instructions when a monorepo package genuinely has different commands or rules. Avoid repeating root instructions in every nested file.
