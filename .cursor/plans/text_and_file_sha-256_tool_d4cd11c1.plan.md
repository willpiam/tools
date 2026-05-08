---
name: Text and file SHA-256 tool
overview: Replace the file-only [fileSha256.html](fileSha256.html) with a dual-mode (text + file) SHA-256 hasher that reuses the existing crypto/fallback logic, adds a text-area input with an optional salt prefix written into the field as `salt::message`, and updates the tool listing in [data.js](data.js).
todos:
  - id: implement-page
    content: "Rebuild fileSha256.html: mode toggle, text panel (textarea + salt checkbox + UTF-8 hash path), file panel (reuse existing logic), shared output/copy/status."
    status: completed
  - id: update-data-js
    content: Adjust tools[] title/description in data.js for the expanded behavior; keep path fileSha256.html.
    status: completed
isProject: false
---

# Text + file SHA-256 hasher (replace fileSha256)

## Current state

- [fileSha256.html](fileSha256.html) is a self-contained dark-themed page: file picker, **Compute SHA-256**, **Copy Hash**, Web Crypto with a full JS SHA-256 fallback ([`sha256Bytes`](fileSha256.html), [`sha256FallbackBytes`](fileSha256.html)), and status messaging.
- The index lists it via [data.js](data.js) (title **File SHA-256 Hasher**, path `fileSha256.html`).

## Target behavior

1. **Mode switch** (e.g. radio buttons or a simple toggle): **Text** vs **File**. Only one mode’s inputs are active at a time; **hash output** and **Copy** are shared (same as today for file).
2. **Text mode**
   - Multiline `<textarea>` for the message.
   - **Compute**: encode the textarea contents as **UTF-8** (`TextEncoder`), run the same [`sha256Bytes`](fileSha256.html) pipeline, show lowercase hex like today.
   - **Checkbox** (shown only in text mode), e.g. *“Insert random salt (salt::message) before hashing”*:
     - When **checked** at compute time: if the current input **does not** already contain `::`, generate a cryptographically random salt (recommend **`crypto.getRandomValues`** → **32 hex chars** = 16 bytes, no `::` in the salt), set the textarea value to **`{salt}::{previous entire textarea}`**, then hash **that full string** (UTF-8). If `::` is already present, **skip mutation** and hash as-is while showing a short status note (avoids accidental `salt1::salt2::…` chaining and ambiguity when the payload contains `::`).
   - Empty input: mirror file mode’s validation (friendly error, no hash).
3. **File mode**
   - Keep the existing flow: [`file.arrayBuffer`](fileSha256.html) → `Uint8Array` → `sha256Bytes` → hex. No salt checkbox (user scope: text mode only).

## UI/layout

- Reuse the **same visual language** as the current page (panels, mono hash block, `.ok` / `.warn` / `.err` statuses, button styling).
- Structure: heading → mode control → conditional **Text** panel (textarea + checkbox + row of buttons) vs **File** panel (existing file controls) → optional compact “selected file info” panel only in file mode → shared **SHA-256** output panel.
- **Copy** continues to copy the last computed hex; disable until a successful compute.

## Code organization

- Keep a **single HTML file** with inline script (consistent with sibling tools): lift `bytesToHex`, `rightRotate`, `sha256FallbackBytes`, `sha256Bytes`, `copyTextToClipboard`, and status helpers with minimal renaming.
- Add small helpers: UTF-8 buffer from string; optional `insertSaltPrefix(textarea)` invoked from the compute path when checkbox + text mode + no `::` in raw string.

## Registry

- Update the entry in [data.js](data.js) (~lines 63–65): title/description to reflect **text or file**, and optional salted `salt::message` workflow. **Keep path `fileSha256.html`** so existing bookmarks and links stay valid unless you prefer a rename later.

## Out of scope (unless you ask)

- Multiple hash algorithms, HMAC, or salting **file** mode.
- Parsing `salt::payload` beyond “contains `::` → do not auto-insert another salt.”
