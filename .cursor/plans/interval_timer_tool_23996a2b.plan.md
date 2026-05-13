---
name: Interval Timer Tool
overview: Add a standalone interval timer page where users can run multiple looping timers, each with its own duration, color, and stable chime pitch, then save the timer configuration into a base64url URL blob for bookmarking/reloading.
todos:
  - id: create-page
    content: Create the standalone interval timer HTML/CSS/JS page.
    status: completed
  - id: implement-timers
    content: Implement multi-timer state, looping countdown logic, pie progress rendering, and timer controls.
    status: completed
  - id: add-audio
    content: Implement stable per-timer Web Audio chimes with persisted pitch values.
    status: completed
  - id: add-url-config
    content: Implement base64url config encode/decode, Save-to-URL behavior, and load-time hydration.
    status: completed
  - id: register-tool
    content: Add the new tool entry to data.js and run focused validation.
    status: completed
isProject: false
---

# Add Interval Timer Tool

## Scope
- Create a new standalone page at [`/home/william/projects/tools/intervalTimers.html`](/home/william/projects/tools/intervalTimers.html).
- Register it in [`/home/william/projects/tools/data.js`](/home/william/projects/tools/data.js) so it appears on the homepage.
- Keep the implementation dependency-free, matching the existing static HTML/CSS/JS pattern used by tools like [`/home/william/projects/tools/sha256Miner.html`](/home/william/projects/tools/sha256Miner.html) and [`/home/william/projects/tools/textFileSha256.html`](/home/william/projects/tools/textFileSha256.html).

## UI And Behavior
- Build a sleek dark-mode layout with:
  - A small form for duration input, optional timer label, and add/save actions.
  - A responsive grid of timer cards.
  - Each card showing a CSS/SVG pie progress indicator, remaining time text, total duration, and controls such as reset/remove.
- Timers will run as repeating intervals: when one reaches zero, it plays its chime and immediately starts a fresh cycle.
- Use `requestAnimationFrame` with `performance.now()` for smooth progress and accurate remaining-time calculations.
- Assign each timer a color from a modern palette and persist that color in config.
- Assign each timer a stable chime pitch when it is created, persist that pitch in config, and use the same pitch every time that timer fires.

## URL Config
- Use one query parameter, `cfg`, containing base64url-encoded JSON, following the local per-tool URL persistence style already used in [`/home/william/projects/tools/passwordmaker.html`](/home/william/projects/tools/passwordmaker.html) and [`/home/william/projects/tools/encodingConverter.html`](/home/william/projects/tools/encodingConverter.html).
- Proposed payload shape:

```json
{
  "version": 1,
  "timers": [
    { "id": "...", "label": "Stretch", "durationSeconds": 300, "color": "#3b82f6", "pitchHz": 523.25 }
  ]
}
```

- The Save button will serialize only configuration, not transient remaining time, then call `history.replaceState` so the current URL becomes bookmarkable without reloading.
- On page load, decode and validate `cfg`; invalid or missing config falls back to a simple default timer.

## Chime Implementation
- Use the Web Audio API to synthesize a gentle short chime instead of relying on an external audio file.
- Resume/unlock audio on user interaction, since browsers may block sound before the user clicks.
- For each chime, play a soft envelope at the timer’s persisted `pitchHz`, optionally with a quiet harmonic for a cleaner bell-like sound.

## Validation
- Manually test by serving the static site and opening [`http://localhost:8000/intervalTimers.html`](http://localhost:8000/intervalTimers.html).
- Verify multiple timers can be added, removed, reset, and allowed to loop.
- Verify each timer keeps a distinct color and stable pitch across repeats and after loading a saved URL.
- Verify Save writes a base64url `cfg` blob and reloading/bookmarking restores the configured timers.
- Check the edited files with the linter diagnostics available in Cursor after implementation.