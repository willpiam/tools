---
name: Pixel Zoom Viewer
overview: "Add a standalone image zoom tool: upload an image, view it full-viewport, and zoom with crisp (non-blurred) nearest-neighbor scaling. Register it in the tools hub."
todos:
  - id: create-pixel-zoom
    content: "Create pixelZoom.html with upload, full-viewport viewer, wheel/pinch zoom, pan, and image-rendering: pixelated"
    status: completed
  - id: register-tool
    content: Add Pixel Zoom entry to data.js
    status: completed
isProject: false
---

# Pixel Zoom Image Viewer

## Approach

Add a self-contained page [`pixelZoom.html`](pixelZoom.html) and register it in [`data.js`](data.js), matching the existing flat-tool pattern (inline CSS/JS, dark theme like [`textFileSha256.html`](textFileSha256.html) / [`index.html`](index.html)).

**Crisp zoom:** render via an `<img>` transformed with CSS `scale`, and force nearest-neighbor interpolation:

```css
.viewer img {
  image-rendering: pixelated;
  image-rendering: crisp-edges;
}
```

That keeps pixels blocky/sharp when magnified instead of bilinear blur.

## UX

1. **Landing:** dark upload screen — file picker (`accept="image/*"`), drag-and-drop, short hint (wheel to zoom, drag to pan).
2. **Viewer:** after load, switch to a full-viewport black stage (image centered, fit-to-screen initially).
3. **Zoom:** mouse wheel / trackpad; `+` / `-` buttons; pinch on touch. Clamp roughly 0.1x–64x relative to fit.
4. **Pan:** click-drag (and touch-drag) when zoomed; zoom toward cursor/pinch center.
5. **Chrome:** minimal floating bar — zoom %, reset view, “New image”, optional browser Fullscreen toggle. `Esc` exits browser fullscreen if active, otherwise returns to upload / resets as appropriate.

No external libraries.

## Files

- **Create** [`pixelZoom.html`](pixelZoom.html) — upload UI + fullscreen viewer + transform/zoom logic + crisp `image-rendering`.
- **Update** [`data.js`](data.js) — append:

```js
{
  title: "Pixel Zoom",
  description: "Upload an image and zoom in with sharp, unblurred pixels",
  path: "pixelZoom.html"
}
```

## Implementation notes

- Revoke object URLs on replace/unload to avoid leaks.
- Use `transform: translate(...) scale(...)` on the image (or a wrapper) so layout stays simple; keep `transform-origin: 0 0` and compute offsets so zoom anchors under the pointer.
- Do not use CSS `image-rendering: auto` / smoothed canvas draws — that is what blurs pixels.