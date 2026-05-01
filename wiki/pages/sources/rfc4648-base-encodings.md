# RFC 4648: Base16, Base32, and Base64 Data Encodings

## Summary
- RFC 4648 standardizes Base16, Base32, Base64, plus Base64 URL-safe and Base32 Extended Hex variants to reduce ambiguity and improve interoperability.
- It defines strict default decoder behavior: reject non-alphabet characters unless a referring specification explicitly relaxes this.
- It requires padding by default for Base64/Base32 unless the referring specification explicitly opts out; Base16 does not use padding.
- It defines canonical encoding constraints, including zeroing pad bits, to avoid multiple encodings decoding to the same data.

## Key details
- Status and scope: Standards Track RFC (October 2006), obsoleting RFC 3548, focused on common alphabet/encoding behavior for protocol consistency.
- Line wrapping: Encoders MUST NOT insert line feeds unless a higher-level spec explicitly requires fixed line lengths.
- Padding: Encoders MUST include proper trailing `=` padding for Base64/Base32 unless a higher-level spec states otherwise.
- Non-alphabet characters: Decoders MUST reject by default; MIME-like specs may allow ignoring such characters, but this is a conscious exception.
- Base64url naming: `base64url` is not identical in name/semantics to `base64`; the alphabet differs at positions 62 and 63 (`-` and `_` instead of `+` and `/`).
- Security notes: Base encoding does not provide confidentiality; permissive decoding/case handling/pad-bit mishandling can create covert channels and implementation risks.
- Includes test vectors for Base64, Base32, Base32-HEX, and Base16 (`""`, `"f"`, `"fo"`, `"foo"`, etc.).

## Connections
- Related concepts: [[base64]], [[base32]], [[base16]], [[canonical-base-n-encoding]]
- Related entities: [[simon-josefsson]]
- Supports stricter interoperability guidance compared with ad-hoc MIME-derived practices.

## Sources
- `wiki/raw/rfc4648.txt`
