# Wiki Workspace

This directory is the persistent knowledge base managed by an LLM agent.

## Structure

- `raw/`: immutable source material (articles, papers, notes, assets).
- `pages/`: generated wiki pages that synthesize the raw sources.
- `index.md`: catalog of wiki pages and short descriptions.
- `log.md`: append-only operations log for ingest, query, and lint runs.
- `AGENTS.md`: schema and operating rules for the agent.

## First steps

1. Add one source file to `raw/`.
2. Run your `wiki-ingest` workflow on that source.
3. Ask a question with `wiki-query`.
4. Periodically run `wiki-lint` to keep links and claims healthy.
