# Wiki Agent Schema

You are the maintainer of this wiki. Treat this directory as a persistent, compounding knowledge base.

## Core principles

1. `raw/` is immutable source-of-truth input. Never edit files in `raw/`.
2. `pages/` is LLM-owned output. Create and update markdown pages as needed.
3. Keep `index.md` current after any page creation or major edit.
4. Append a new entry to `log.md` for every ingest, query, and lint operation.
5. Prefer cross-linked markdown using `[[page-name]]` style links.
6. If claims conflict, keep both with source citations and an explicit contradiction note.

## Directory conventions

- Store source summaries in `pages/sources/`.
- Store entity pages in `pages/entities/`.
- Store concept/topic pages in `pages/concepts/`.
- Store analysis pages (comparisons, Q&A outputs) in `pages/analysis/`.

## Page template

Use this structure for most pages:

```markdown
# Title

## Summary
2-5 bullet synthesis.

## Key details
Important claims and evidence.

## Connections
- Related: [[other-page]]
- Contradiction or support notes.

## Sources
- [[source-page]] (or raw file path)
```

## Operation: ingest

When asked to ingest a source:

1. Read the source from `raw/`.
2. Create/update a source summary in `pages/sources/`.
3. Update relevant entity/concept pages.
4. Add any new pages needed for missing concepts.
5. Update `index.md`.
6. Append an `ingest` entry to `log.md`.

## Operation: query

When asked a question:

1. Read `index.md` first, then relevant pages.
2. Answer with citations to wiki pages and/or raw files.
3. If the answer is durable, save it as a page in `pages/analysis/`.
4. Update `index.md` and append a `query` log entry.

## Operation: lint

When asked to lint:

1. Detect orphan pages, stale claims, weak cross-links, and contradictions.
2. Propose and apply safe improvements directly in markdown.
3. Add missing pages for high-value uncovered concepts.
4. Append a `lint` entry to `log.md` with findings and changes.
