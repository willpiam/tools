# Base64

## Summary
- Base64 encodes 24-bit input groups into 4 printable characters, using a 64-character alphabet plus `=` for padding.
- RFC 4648 distinguishes standard `base64` from URL-safe `base64url` and recommends precise naming.
- Padding is required by default unless a referring specification explicitly opts out.

## Key details
- Alphabet mapping: values 0-63 map to `A-Z`, `a-z`, `0-9`, `+`, `/`; `=` is the pad character.
- Final quantum behavior:
  - 24 bits -> 4 chars, no padding
  - 8 bits -> 2 chars + `==`
  - 16 bits -> 3 chars + `=`
- Encoders MUST NOT insert line feeds unless explicitly directed by the higher-level specification.
- For URL/file-safe use, RFC 4648 defines `base64url`, replacing `+` and `/` with `-` and `_`.

## Connections
- Parent source: [[rfc4648-base-encodings]]
- Related: [[base32]], [[base16]], [[canonical-base-n-encoding]]
- Adjacent variant: `base64url` (defined within [[rfc4648-base-encodings]])

## Sources
- [[rfc4648-base-encodings]]
- `wiki/raw/rfc4648.txt`
