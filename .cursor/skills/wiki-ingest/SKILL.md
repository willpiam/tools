---
name: wiki-ingest
description: Ingest a new source into the project wiki by reading raw material, updating source/entity/concept pages, refreshing index.md, and appending log.md. Use when the user asks to ingest, process, file, or integrate a source document.
disable-model-invocation: true
---
# Wiki Ingest

## Goal

Integrate one source from `wiki/raw/` into the persistent wiki in `wiki/pages/`.

## Workflow

1. Read `wiki/AGENTS.md`, `wiki/index.md`, and the requested source file in `wiki/raw/`.
2. Extract high-signal claims, entities, concepts, and contradictions.
3. Create or update:
   - `wiki/pages/sources/<source-name>.md`
   - related `wiki/pages/entities/*.md`
   - related `wiki/pages/concepts/*.md`
4. Add or improve cross-links using `[[page-name]]`.
5. Update `wiki/index.md` entries that changed.
6. Append an ingest entry to `wiki/log.md` with touched pages.

## Output contract

- Cite where claims came from (source page or raw file).
- Preserve previous claims when uncertain; mark as unresolved.
- Keep raw files immutable.
