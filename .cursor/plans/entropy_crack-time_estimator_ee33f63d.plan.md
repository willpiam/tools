---
name: Entropy Crack-Time Estimator
overview: Add a crack-time estimator based on entropy bits using an RTX 5090 offline fast-hash model, and present user-friendly time-to-crack text next to the entropy indicator.
todos:
  - id: add-cracktime-constants
    content: Add RTX 5090 guesses/sec model constant and document assumption in code.
    status: completed
  - id: add-pure-estimator-functions
    content: Implement pure functions to convert entropy bits to average crack time and human-readable durations.
    status: completed
  - id: wire-ui-estimator
    content: Add crack-time indicator and assumptions text to the existing entropy display section.
    status: completed
  - id: validate-estimates
    content: Verify sample bit values produce expected time scales and handle Invalid cfg gracefully.
    status: completed
isProject: false
---

# Add RTX 5090 Crack-Time Display

## Goal
Translate entropy bits into an understandable average crack time using a single RTX 5090 in an offline fast-hash scenario, while keeping assumptions explicit in UI text.

## Research Baseline (for constants)
- RTX 5090 hardware context (NVIDIA official page): 21,760 CUDA cores, 32GB GDDR7, Blackwell architecture.
- Fast-hash cracking benchmark references indicate roughly `~300-340 GH/s` for NTLM on a single RTX 5090:
  - Hashcat forum benchmark thread: [https://hashcat.net/forum/thread-13271-nextoldest.html](https://hashcat.net/forum/thread-13271-nextoldest.html)
  - Hashcat benchmark gist (Chick3nman): [https://gist.github.com/Chick3nman/09bac0775e6393468c2925c1e1363d5c](https://gist.github.com/Chick3nman/09bac0775e6393468c2925c1e1363d5c)
- Use a conservative default attack rate constant in code, e.g. `300e9 guesses/sec`, chosen from the lower end of those measured NTLM fast-hash results. Include a code comment that this is an offline fast-hash model assumption and varies by hash type.

## Implementation Plan
- Update [`/home/william/projects/tools/passwordmaker.html`](/home/william/projects/tools/passwordmaker.html) to add pure computation helpers:
  - `calculateAverageCrackSecondsFromEntropyBits(bits, guessesPerSecond)`
  - `formatDurationHuman(seconds)`
  - `estimateCrackTimeFromCfg(cfgBase32)` -> returns either `"Invalid cfg"` or structured estimate.
- Keep `calculateEntropyFromCfg(cfgBase32)` as the source of entropy bits, then derive average crack time via:
  - keyspace size `N = 2^bits`
  - average attempts `N / 2`
  - average seconds `N / (2 * guessesPerSecond)`
- Add UI text adjacent to current entropy indicator:
  - `Average crack time (RTX 5090, fast offline): ...`
  - On invalid cfg: show friendly invalid state message.
- Add tiny assumptions/help copy under the estimator:
  - “Model assumes offline fast-hash cracking (~300B guesses/sec on one RTX 5090). Real times vary by algorithm and defenses.”

## Correctness + UX Notes
- Use integer entropy bits already displayed; crack time should derive from that integer exactly as requested.
- Avoid false precision in long times; format into readable units (seconds/minutes/hours/days/years, and “centuries+” style if huge).
- Make sure this indicator updates whenever settings update (same place entropy indicator refreshes).

## Validation
- Check a few known values manually:
  - 40 bits -> sub-second to seconds range at 300 GH/s.
  - 60 bits -> around weeks.
  - 80 bits -> decades.
- Confirm no password material is written to URL or estimator output.
- Run lints on updated file after edits.