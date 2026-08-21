# Hermes / LangGraph Adapter — Firecrawl Web Intelligence

Canonical policy: `../SKILL.md`

## Suggested LangGraph nodes

- `classify_web_task`
- `search_web`
- `scrape_page`
- `map_site`
- `crawl_site`
- `developer_research`
- `scientific_research`
- `validate_evidence`
- `persist_knowledge`
- `request_action_authorization`
- `interact_web`
- `monitor_manager`
- `finalize_research`

## State contract

```ts
type WebIntelState = {
  objective: string;
  route?: "search"|"scrape"|"map"|"crawl"|"developer"|"research"|"interact"|"monitor";
  urls: string[];
  evidence: Evidence[];
  contradictions: string[];
  freshnessRequired: boolean;
  sideEffectRisk: "none"|"low"|"high";
  userAuthorizedSideEffect: boolean;
  costBudget?: {
    maxSearches?: number;
    maxPages?: number;
    maxInteractions?: number;
  };
};
```

## Routing edges

- known single URL -> scrape
- unknown URL/current topic -> search
- technical/API/error -> developer
- site known, page unknown -> map
- multi-page site evidence -> map then crawl
- dynamic authenticated/browser workflow -> authorization then interact
- recurring change condition -> monitor
- scientific question -> research

## Production recommendation

Queue long crawl/ingestion jobs through Trigger.dev/queue workers.
Write status/progress to Supabase.
Persist normalized evidence to Neon/Supabase.
Use Realtime only for client progress/events, not as the job queue itself.

Never send agent-provider API keys to Expo/React Native clients.
Mobile app -> authenticated backend/edge endpoint -> agent worker -> Firecrawl.
