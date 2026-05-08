---
name: URL Preconfig for Converter
overview: Add URL-based persistence for encoding conversion settings so users can share preconfigured converter states via copy/paste links.
todos:
  - id: add-url-config-utils
    content: Add helper functions to read/write encoding config from URL query params.
    status: completed
  - id: hydrate-initial-state
    content: Apply URL config during initialization before normal UI setup.
    status: completed
  - id: sync-on-user-actions
    content: Wire URL updates into dropdown change and swap handlers.
    status: completed
  - id: validate-manual-scenarios
    content: Run manual validation scenarios for defaults, valid params, invalid params, and swap behavior.
    status: completed
isProject: false
---

# Add URL Preconfig For Encoding Converter

## Goal
Persist encoding configuration in the URL so users can share links that reopen the converter with the same selected input/output formats (including swapped direction).

## Implementation
- Update [`/home/william/projects/tools/encodingConverter.html`](/home/william/projects/tools/encodingConverter.html) script logic to introduce:
  - `readConfigFromUrl()` to parse query params (e.g. `from`, `to`) and validate against supported encoding values.
  - `writeConfigToUrl()` to update query params with `history.replaceState` (no page reload, no history spam).
- Initialize selections on page load by applying URL values first, then calling existing `updatePlaceholder()`.
- Keep URL in sync when configuration changes:
  - On `inputEncoding` change
  - On `outputEncoding` change
  - After swap button action
- Preserve current behavior for conversion/copy/error handling; only add configuration persistence responsibilities.
- Add simple defensive handling for invalid URL params (ignore unknown values and retain current defaults).

## Proposed URL Contract
- `?from=<inputEncoding>&to=<outputEncoding>`
- Example: `?from=base64&to=hex`

## Validation
- Manual checks in browser:
  - Load page with no params -> defaults remain (`text` -> `hex`).
  - Load with valid params -> dropdowns hydrate correctly.
  - Change either dropdown -> URL updates immediately.
  - Use swap button -> both dropdowns and URL values swap.
  - Load with invalid params -> app falls back to valid defaults without errors.