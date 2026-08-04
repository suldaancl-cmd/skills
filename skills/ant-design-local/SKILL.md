---
name: ant-design-local
description: Use this for Ant Design React implementation, component APIs, theme tokens, migration, local source inspection, and design-system-aligned UI work using the cloned ant-design repository.
---

# Ant Design Local

Original clone: `C:\tmp\ant-design`
Component index: `references/component-index.md`

Use this skill for Ant Design React work: choosing components, checking props, implementing forms/tables/modals/layouts, customizing v5 tokens, migration questions, and inspecting local source.

Workflow:

1. For component API details, prefer the native `antd-component-lookup` skill or read `components/<component>/index.en-US.md` in the clone.
2. For theme work, prefer `antd-theme-customization`; use v5 Design Tokens and `ConfigProvider`.
3. For migration work, prefer `antd-migration` and inspect local changelog/docs when needed.
4. For implementation, import from `antd`, keep TypeScript props accurate, and match the host app's existing patterns.
5. Avoid older Less-variable customization unless the project is explicitly on Ant Design v4.

When the user names a specific component, prefer the matching `antd-component-*` wrapper skill if it exists.
