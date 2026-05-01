---
name: wiki-lint
description: Perform a wiki health pass by finding orphan pages, stale claims, weak cross-links, and contradictions, then applying safe fixes and logging the results. Use when the user asks to lint, health-check, reconcile, or maintain the wiki.
disable-model-invocation: true
---
# Wiki Lint

## Goal

Keep the wiki coherent, current, and navigable as it grows.

## Workflow

1. Read `wiki/index.md`, `wiki/log.md`, and a representative set of pages.
2. Detect:
   - orphan pages with no inbound references
   - stale claims superseded by newer sources
   - missing high-value concept/entity pages
   - unresolved contradictions
3. Apply safe markdown fixes:
   - add cross-links
   - annotate stale claims
   - improve section structure
   - add missing index entries
4. Do not delete raw evidence; preserve traceability.
5. Append a lint entry to `wiki/log.md` with findings and actions.

## Output contract

- Report findings by severity: critical contradictions, then structure gaps.
- Include touched files and next recommended ingest/query actions.
