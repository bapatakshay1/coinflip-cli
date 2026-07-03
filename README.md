# coinflip-cli

A tiny command-line tool that flips a virtual coin.

## Install

```bash
pip install -e .
```

This installs the `coinflip` executable locally.

## Usage

Flip a single coin:

```bash
$ coinflip
heads
```

Flip N times and print a summary tally:

```bash
$ coinflip --count 10
heads: 6
tails: 4
```

`-c` is a short alias for `--count`. Invalid values (non-numeric, zero, or
negative) are rejected with a stderr message and a non-zero exit code.

## Tests

```bash
pip install pytest
pytest
```
