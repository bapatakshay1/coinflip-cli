# Technical Specifications: coinflip-cli

## Overview
`coinflip` is a minimal command-line tool that simulates flipping a coin.

## System Architecture
- Single, self-contained CLI executable/script named `coinflip`.
- No external services, databases, or network calls required.
- No persistent state between invocations.

## CLI Interface

### Default invocation
```
$ coinflip
heads
```
or
```
$ coinflip
tails
```
- With no arguments, the tool performs exactly one coin flip.
- Output is a single line: either `heads` or `tails` (lowercase).
- Each outcome should have ~50% probability, using a random source suitable for simulating a fair coin.

### `--count N` flag
```
$ coinflip --count 10
heads: 6
tails: 4
```
- Accepts an integer `N` (positive, non-zero).
- Performs `N` independent coin flips.
- Prints a summary tally, not each individual flip result.
- Output format: two lines, `heads: <count>` and `tails: <count>`, where the two counts sum to `N`.

### Argument validation
- If `N` is not a valid positive integer (e.g., `0`, negative, non-numeric), print a clear error message to stderr and exit with a non-zero status code.
- `--count 1` is valid and behaves like the summary format (`heads: 1` / `tails: 0` or similar), not the single bare-word output.

## Data Model
- No persistent data model needed.
- Internal representation: a simple enum/boolean/string for a flip result (heads/tails), and an integer tally for counts when `--count` is used.

## Performance Requirements
- Trivial computational cost; N flips should complete instantly for any reasonable N (e.g., up to 1,000,000) without noticeable delay.

## Security Considerations
- No sensitive data, no network I/O, no file I/O beyond standard output/error.
- Randomness does not need to be cryptographically secure — a standard PRNG is sufficient since this is a novelty/utility tool, not a security-critical application.

## Installation / Runnability
- Must be runnable locally as an MVP (e.g., via a shebang script, a package.json bin entry, a Python entry point, or equivalent for the chosen language/runtime).
- Should be installable such that `coinflip` (or `coinflip --count N`) can be invoked directly from a shell after a simple local install step (e.g., `npm link`, `pip install -e .`, `go build`, etc.), depending on implementation language chosen.

## Testing Requirements
- Basic unit tests covering:
  - Single flip returns one of `heads`/`tails`.
  - `--count N` returns counts summing to N.
  - Invalid `--count` values are rejected with a non-zero exit code.
- Tests should be lightweight — this is an MVP-scope project, not a project requiring exhaustive coverage.

## Out of Scope
- Configurable probability/weighted coins.
- Persistent history/logging of flips.
- Interactive/REPL mode.
- GUI or web interface.
