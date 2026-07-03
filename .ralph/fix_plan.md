# Ralph Fix Plan

## High Priority
- [x] Set up basic project structure (choose language/runtime, entry point in src/)
- [x] Implement default `coinflip` behavior: single flip, print "heads" or "tails"
- [x] Implement `--count N` flag: N flips, print summary tally (`heads: X` / `tails: Y`)
- [x] Validate `--count` argument (reject non-numeric/zero/negative with stderr message + non-zero exit)
- [x] Write basic tests for single flip, tally summation, and invalid input handling

## Medium Priority
- [x] Make tool locally installable/runnable (e.g. npm link, pip install -e ., go build)
- [x] Add usage/help text (`coinflip --help`)
- [x] Update README.md with install and usage instructions

## Low Priority
- [x] Polish CLI output formatting
- [x] Add `-c` short flag alias for `--count`

## Optional
<!-- Issue #239: unchecked items in this section (and "Future"/"Future Enhancements"/
     "Nice to Have") do NOT block Ralph's exit. Use it for genuinely optional/future work
     so Ralph can finish once the required sections above are complete. Configure the section
     names via OPTIONAL_SECTIONS in .ralphrc. -->
- [ ] Nice-to-have enhancements (non-blocking)

## Completed
- [x] Project initialization

## Notes
- Focus on MVP functionality first
- Ensure each feature is properly tested
- Update this file after each major milestone
