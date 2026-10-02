---
name: Index tool search
overview: Add a live search box to the tools index that filters the existing list by title and description as you type, styled to match the current dark theme.
todos:
  - id: search-ui
    content: Add search input + matching dark-theme CSS + empty state in index.html
    status: completed
  - id: filter-logic
    content: Refactor render into renderTools() and wire live title/description filtering
    status: completed
isProject: false
---

# Add search to the tools index

## Approach

Keep everything in [`index.html`](index.html). Tools already come from [`data.js`](data.js); refactor the render loop so it can re-run against a filtered subset on each keystroke. No new dependencies — ~20 tools makes a simple case-insensitive substring match on title + description enough.

## UI

- Place a search input at the top of `.tools-container`, above `#tools-list`.
- Use `<input type="search">` with placeholder like `Search tools…`, autofocus, and `autocomplete="off"`.
- Style the input to match the dark theme (`#363636` background, `#e0e0e0` text, blue focus ring consistent with existing `#60a5fa` accents).
- When the query matches nothing, show a short empty-state message (e.g. “No tools match”) instead of an empty list.

## Logic (inline script in `index.html`)

1. Extract the current `tools.forEach(...)` into a `renderTools(list)` helper that clears `#tools-list` and rebuilds `<li>` items (reuse existing `resolveToolHref`).
2. On `input` (and `search` for the clear button), normalize the query (`trim` + lowercase) and filter:

```js
const q = input.value.trim().toLowerCase();
const filtered = !q
  ? tools
  : tools.filter(t =>
      t.title.toLowerCase().includes(q) ||
      t.description.toLowerCase().includes(q)
    );
renderTools(filtered);
```

3. Initial page load calls `renderTools(tools)` once.

## Out of scope

- No fuzzy ranking, URL query params, or keyboard navigation beyond the native search input.
- No changes to [`data.js`](data.js) or individual tool pages.