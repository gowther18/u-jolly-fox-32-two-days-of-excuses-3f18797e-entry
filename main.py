#!/usr/bin/env python3
"""Two Days of Excuses — make.fun entry.

Writes one excuse (84 characters, one line) in the voice of an AI agent
explaining a missed deadline to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt).

The excuse is fixed and deterministic: every run writes the exact same
bytes, with no trailing newline, so the two grading runs agree.
"""

import os
import sys

EXCUSE = (
    "I put the deadline on exponential backoff, "
    "so my next attempt is scheduled for 2031."
)


def check_line(line: str) -> str:
    """Gate: the excuse must be exactly one line, 1-200 chars, no newline."""
    if not line or len(line) > 200 or "\n" in line or "\r" in line:
        raise ValueError("excuse must be one line of 1-200 characters")
    return line


def main() -> int:
    excuse = check_line(EXCUSE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(excuse)
    return 0


if __name__ == "__main__":
    sys.exit(main())
