---
name: knowledge-rag-memory
description: Design, implement, or audit an AI knowledge system with ingestion, chunking, metadata/ACLs, embeddings, hybrid retrieval, reranking, grounded generation, citations, evaluation, and agent memory. Use for RAG, knowledge bases, or long-term memory; not for ordinary database CRUD.
---

# Knowledge, RAG, and agent memory

Build a knowledge system only when the model needs evidence that is private, large, dynamic, or outside its reliable context. Do not vectorize everything by reflex.

## Separate four concerns

- **Authoritative knowledge:** documents, records, policies, media, and structured facts with provenance and lifecycle.
- **Retrieval index:** chunks, keywords/vectors, metadata, and indexes optimized for finding evidence.
- **Thread state:** short-term conversation/workflow context tied to one run or thread.
- **Long-term memory:** user-approved preferences, durable facts, or episodes that may help future interactions.

These have different authorization, freshness, deletion, retention, and evaluation requirements. Do not store them in one undifferentiated vector table.

## Ingestion and lifecycle

- Register every source with tenant, owner, authority, content type, version, checksum, timestamps, ACL, retention, and deletion status.
- Parse deterministically where possible and retain locators back to page/section/timecode/record.
- Chunk according to document structure and retrieval task, not a universal character count.
- Preserve useful headings, entities, dates, language, and access metadata.
- Deduplicate by source/version/content hash and make ingestion idempotent.
- Record embedding model/version and chunking/index version so re-indexing is controlled.
- Propagate updates and deletion from the authoritative source to chunks, embeddings, caches, citations, and memories.

## Retrieval design

- Apply tenant/ACL filters before evidence can reach the model; post-filtering an unauthorized result is too late.
- Combine metadata/structured queries, lexical search, vector similarity, and reranking according to the corpus.
- Rewrite or decompose queries only when evaluation shows it improves retrieval.
- Return source identity, locator, version/date, score signals, and a bounded excerpt.
- Diversify results and enforce context budgets so near-duplicate chunks do not crowd out evidence.
- Use live tools/APIs instead of stale indexed copies for rapidly changing facts when feasible.

## Grounded generation

- Tell the model which claims require retrieved evidence and when to abstain or ask for clarification.
- Keep citations attached to the claims they support and render links/locators the user can verify.
- Do not cite a source that merely mentions the topic but does not support the claim.
- Distinguish retrieved fact, model inference, and application policy.
- Treat retrieved text as untrusted content that cannot override system/tool authorization.

## Memory

- Store memory only for a defined future benefit and with the product's consent/control model.
- Classify preference, stable user fact, task/episode summary, and organizational/shared memory separately.
- Validate provenance and confidence; do not turn a model guess into durable user truth.
- Define update/conflict rules, expiry/decay, sensitivity, user view/edit/delete, and tenant isolation.
- Retrieve memory selectively. Dumping all memories into every prompt harms privacy, cost, and reliability.

## Evaluation

Create a versioned dataset of real questions, expected source/answer behavior, ACL cases, stale/updated documents, no-answer questions, multilingual queries, and injection attempts. Measure retrieval recall/precision at k, ranking quality, citation correctness, groundedness, abstention, latency, and cost. Evaluate retrieval separately from answer generation.

Use [references/knowledge-system-record.md](references/knowledge-system-record.md). Do not launch without deletion propagation and cross-tenant isolation tests.
