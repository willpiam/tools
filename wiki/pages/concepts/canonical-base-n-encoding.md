# Canonical Base-N Encoding

## Summary
- RFC 4648 defines canonical encoding constraints to ensure one stable encoded representation per binary input.
- For Base64/Base32, pad bits must be zeroed by conforming encoders.
- Non-canonical inputs may decode correctly but still be rejected by stricter decoders.

## Key details
- Canonicality risk: if pad bits are not zero, multiple strings may decode to the same binary output.
- RFC 4648 states pad bits MUST be set to zero in conforming encoders.
- Decoders MAY reject encodings with non-zero pad bits in environments that require strict canonical behavior.
- Canonical encoding guidance complements rules on padding inclusion and treatment of non-alphabet characters.

## Connections
- Parent source: [[rfc4648-base-encodings]]
- Related: [[base64]], [[base32]], [[base16]]
- Security-adjacent behavior: covert channels and comparison bypass risks are discussed in [[rfc4648-base-encodings]].

## Sources
- [[rfc4648-base-encodings]]
- `wiki/raw/rfc4648.txt`
