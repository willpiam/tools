# Base16

## Summary
- Base16 (hex) is a case-insensitive encoding of octets into 2 hexadecimal symbols per byte.
- RFC 4648 treats Base16 as analogous to Base32/Base64 but without padding.

## Key details
- Alphabet: `0-9` and `A-F` for values 0-15.
- Encoding groups 8 input bits into 2 output symbols (4 bits each).
- No special padding is required because Base16 always maps complete 4-bit units.
- RFC 4648 security notes still apply: encoded data is not confidential, and case-insensitive handling may create leakage/equality pitfalls.

## Connections
- Parent source: [[rfc4648-base-encodings]]
- Related: [[base64]], [[base32]], [[canonical-base-n-encoding]]

## Sources
- [[rfc4648-base-encodings]]
- `wiki/raw/rfc4648.txt`
