# Wiki Log

## [2026-05-01] setup | Initialize wiki scaffolding

- Created wiki structure (`raw/`, `pages/`, `index.md`, `log.md`, `AGENTS.md`).
- Added project skills for ingest/query/lint workflows under `.cursor/skills/`.

## [2026-05-01] ingest | RFC 4648 Base-N encodings

- Ingested `wiki/raw/rfc4648.txt` into [[rfc4648-base-encodings]].
- Added entity page: [[simon-josefsson]].
- Added concept pages: [[base64]], [[base32]], [[base16]], [[canonical-base-n-encoding]].
- Updated `wiki/index.md` source/entity/concept entries to include new pages.

## [2026-05-01] query | Base64 URL-safe coverage check

- Question: "have we documented base 64 url?"
- Answered from [[base64]] and [[rfc4648-base-encodings]]; both explicitly document `base64url` as distinct from `base64`.
- Touched pages: `wiki/index.md`, [[base64]], [[rfc4648-base-encodings]].
