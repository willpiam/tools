---
name: Mermaid Diagram Renderer
overview: Add a standalone Mermaid diagram renderer page matching the existing dark-theme HTML tools, and register it in the tools hub so users can paste Mermaid source and see a live rendered diagram.
todos:
  - id: create-mermaid-page
    content: Create mermaidRenderer.html with editor/preview, live render, error handling, SVG download/copy, Mermaid CDN
    status: completed
  - id: register-tool
    content: Add Mermaid Diagram Renderer entry to data.js
    status: completed
isProject: false
---

# Mermaid Diagram Renderer

## Approach

Add a self-contained page [`mermaidRenderer.html`](mermaidRenderer.html) and register it in [`data.js`](data.js), following the same pattern as [`htmlRenderer.html`](htmlRenderer.html) (split editor/preview) and other recent dark-theme tools.

Load Mermaid from a CDN (same approach as [`qrcodeMaker.html`](qrcodeMaker.html) / [`kiss_my_AES.html`](kiss_my_AES.html)). Pin a specific version via jsDelivr, e.g. `https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js`.

## UX

Layout mirrors HTML Renderer:

1. **Controls:** Render button, Live preview checkbox (on by default), Download SVG, Copy SVG, short status/error text.
2. **Left panel:** monospace textarea for Mermaid source, with a sensible sample flowchart as the initial value / placeholder.
3. **Right panel:** scrollable preview container where Mermaid injects the SVG.
4. **Responsive:** stacked on narrow viewports; two columns from ~900px up (same breakpoint as HTML Renderer).

Behavior:

- Debounced live re-render on input (when live preview is on); always re-render on Render click.
- On parse/render failure, show the Mermaid error message and keep the last successful diagram (or clear preview if first render fails).
- Initialize Mermaid with `startOnLoad: false` and `theme: 'dark'` so diagrams match the page chrome (`#1a1a1a` / `#60a5fa` / `#2d2d2d`).
- Download SVG downloads the current rendered SVG; Copy SVG puts SVG markup on the clipboard.

## Files

- **Create** [`mermaidRenderer.html`](mermaidRenderer.html) — dark-theme UI + Mermaid CDN + render/error/export logic.
- **Update** [`data.js`](data.js) — append:

```js
{
    title: "Mermaid Diagram Renderer",
    description: "Paste Mermaid syntax and view the rendered diagram; download or copy the SVG",
    path: "mermaidRenderer.html"
}
```

## Implementation notes

- Use `mermaid.render(id, source)` (or the current Mermaid 11 async API) into a dedicated preview element; unique ids per render to avoid collisions.
- Strip wrapping ` ```mermaid ` fences if the user pastes a fenced code block, so copy-paste from Markdown works.
- No URL persistence or theme picker in v1 — keep scope to paste → render → export, consistent with HTML Renderer simplicity.
- Style the page like [`htmlRenderer.html`](htmlRenderer.html) / [`textFileSha256.html`](textFileSha256.html): Segoe UI, dark panels, blue primary buttons.