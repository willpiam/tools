---
name: Mermaid Saved Diagrams
overview: Add named diagram persistence to mermaidRenderer.html using localStorage, with a library toolbar for select/save/clone/rename/delete plus a Markdown (.md) download that wraps source in mermaid fences.
todos:
  - id: storage-layer
    content: Add localStorage load/save helpers, schema, unique-name checks in mermaidRenderer.html
    status: completed
  - id: library-ui
    content: Add diagram select, name field, Save/Clone/Delete/Download Markdown controls and wire dirty/load/save/clone/delete flows
    status: completed
  - id: markdown-download
    content: Implement fenced ```mermaid Markdown file download with sanitized filename
    status: completed
isProject: false
---

# Mermaid Saved Diagrams

## Scope

Extend only [`mermaidRenderer.html`](mermaidRenderer.html). Keep render/export behavior as-is; add a local library of named diagrams and a Markdown download.

## Storage

Use `localStorage` (browser-local, no server) under key `mermaidRenderer.diagrams`.

```js
{
  version: 1,
  activeId: "…"|null,
  diagrams: [
    { id: "…", name: "My flow", source: "flowchart TD\n…", updatedAt: 0 }
  ]
}
```

- IDs: `crypto.randomUUID()` (fallback: `Date.now()` + random).
- Names must be unique (case-insensitive trim). Reject empty names.
- Persist `activeId` so a refresh restores the last open diagram; if missing/corrupt, fall back to the current sample flowchart as an unsaved draft (`activeId = null`).

## UI

Add a second controls row under the existing Render / SVG row, matching the same dark button styles:

- **Diagram** `<select>` — “Untitled” option when `activeId` is null, then one option per saved diagram (sorted by name).
- **Name** text input — shows the current diagram’s name; empty when untitled.
- **Save** — if named: overwrite that entry’s `source`/`updatedAt`. If untitled/empty name: `prompt('Diagram name')`, then create. Status confirms save.
- **Clone** — prompt for a new name (default `"{name} (copy)"` or `"Untitled (copy)"`), create a new entry with the current textarea source, select it.
- **Delete** — disabled when untitled; otherwise `confirm`, remove from store, clear to untitled sample or next remaining diagram, refresh select.
- **Download Markdown** — download `{sanitizedName}.md` (or `diagram.md` if untitled) with:

```md
```mermaid
<source>
```
```

Rename flow: editing the Name field and clicking **Save** (or pressing Enter in the name field) renames the active entry if `activeId` is set; if the name collides with another diagram, show an error and do not save.

Selecting from the dropdown loads that diagram’s source into the textarea and re-renders (respect live preview). Warn with `confirm` before switching away if the textarea differs from the last saved source for the active diagram (dirty check). Untitled drafts: switching away without saving discards after confirm.

## Wiring notes

- Reuse existing `stripFences` for what gets stored/saved (store the cleaned Mermaid source, not markdown fences).
- Dirty flag: compare `inputEl.value` to `lastLoadedSource` (updated on load/save/clone).
- Keep SVG Download / Copy independent of the library.
- No changes to [`data.js`](data.js) (tool already registered).

## Concrete behavior summary

| Action | Result |
|--------|--------|
| Save (named) | Update current entry |
| Save (untitled) | Prompt for name, create + select |
| Clone | Prompt, duplicate source as new entry |
| Name edit + Save | Rename active entry |
| Delete | Confirm, remove |
| Select | Load source, render |
| Download Markdown | Fence-wrapped `.md` file |