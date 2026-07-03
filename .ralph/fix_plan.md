# Ralph Fix Plan

## High Priority
- [ ] Set up basic project structure (choose language/runtime, entry point in src/)
- [ ] Implement default `coinflip` behavior: single flip, print "heads" or "tails"
- [ ] Implement `--count N` flag: N flips, print summary tally (`heads: X` / `tails: Y`)
- [ ] Validate `--count` argument (reject non-numeric/zero/negative with stderr message + non-zero exit)
- [ ] Write basic tests for single flip, tally summation, and invalid input handling

## Medium Priority
- [ ] Make tool locally installable/runnable (e.g. npm link, pip install -e ., go build)
- [ ] Add usage/help text (`coinflip --help`)
- [ ] Update README.md with install and usage instructions

## Low Priority
- [ ] Polish CLI output formatting
- [ ] Add `-c` short flag alias for `--count`

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
