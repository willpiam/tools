# Base32

## Summary
- Base32 encodes 40-bit input groups into 8 printable characters with `=` padding.
- RFC 4648 defines both standard `base32` and `base32hex` (extended hex alphabet).
- `base32hex` preserves sort order under bit-wise comparison, unlike standard Base32/Base64 alphabets.

## Key details
- Standard Base32 alphabet uses uppercase letters `A-Z` and digits `2-7`, plus `=` for padding.
- Final quantum behavior supports five trailing cases (0, 8, 16, 24, 32 bits) with corresponding `=` padding lengths.
- Bit ordering is most-significant-bit first across the input stream.
- `base32hex` differs only in alphabet and is not interchangeable in naming with `base32`.

## Connections
- Parent source: [[rfc4648-base-encodings]]
- Related: [[base64]], [[base16]], [[canonical-base-n-encoding]]

## Sources
- [[rfc4648-base-encodings]]
- `wiki/raw/rfc4648.txt`
