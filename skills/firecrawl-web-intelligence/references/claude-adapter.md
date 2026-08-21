# Claude Code Adapter — Firecrawl Web Intelligence

Use the repository-level `SKILL.md` as the canonical policy.

## Invocation behavior

When web context is required:
1. classify the task with the Firecrawl routing ladder
2. invoke the smallest suitable Firecrawl capability
3. collect source URLs + timestamps
4. return evidence to the main coding task
5. do not paste large irrelevant webpage bodies into context

For implementation/debugging questions prefer:
`developer_search -> scrape official docs/source if needed`

For docs migration/audit:
`map -> crawl selected paths`

For current package/API behavior:
use live/current sources, not model memory.

Never put FIRECRAWL_API_KEY or other secrets in client/mobile code.
Secrets belong in server-side environment variables or secret stores.
