"""Command-line entry point for coinflip."""

import argparse
import random
import sys


def flip() -> str:
    """Return the result of a single fair coin flip: 'heads' or 'tails'."""
    return random.choice(("heads", "tails"))


def parse_count(raw: str) -> int:
    """Parse and validate the --count argument.

    Raises ValueError if raw is not a positive integer.
    """
    try:
        value = int(raw)
    except ValueError:
        raise ValueError(f"--count must be a positive integer, got {raw!r}")
    if value <= 0:
        raise ValueError(f"--count must be a positive integer, got {value}")
    return value


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="coinflip",
        description="Flip a virtual coin.",
    )
    parser.add_argument(
        "-c",
        "--count",
        metavar="N",
        help="flip the coin N times and print a heads/tails summary tally",
    )
    return parser


def main(argv=None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.count is None:
        print(flip())
        return 0

    try:
        count = parse_count(args.count)
    except ValueError as exc:
        print(f"coinflip: error: {exc}", file=sys.stderr)
        return 1

    heads = sum(1 for _ in range(count) if flip() == "heads")
    tails = count - heads
    print(f"heads: {heads}")
    print(f"tails: {tails}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
