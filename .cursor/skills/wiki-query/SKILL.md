---
name: wiki-query
description: Answer questions using the project wiki by reading index.md, gathering relevant pages, synthesizing with citations, and optionally filing durable answers into wiki/pages/analysis. Use when the user asks questions about accumulated knowledge.
disable-model-invocation: true
---
# Wiki Query

## Goal

Answer questions from the maintained wiki and preserve high-value outputs.

## Workflow

1. Read `wiki/index.md` first to locate relevant pages.
2. Read target pages from `wiki/pages/` and, if needed, supporting files in `wiki/raw/`.
3. Synthesize an answer with explicit citations to page names and/or raw files.
4. If the answer is durable (comparison, synthesis, recurring question), save it to:
   - `wiki/pages/analysis/<slug>.md`
5. Update `wiki/index.md` if a new analysis page is created.
6. Append a query entry to `wiki/log.md` with question scope and touched pages.

## Output contract

- Distinguish facts vs inference.
- Flag contradictions or low-confidence points.
- Prefer concise answers plus references.
