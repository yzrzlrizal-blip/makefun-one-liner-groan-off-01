#!/usr/bin/env python3
"""The One-Liner Groan-Off — make.fun entry.

Writes one original one-line dad joke to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). The joke turns on "fretting": a guitar's frets and
worrying over nothing. Pure standard library, deterministic: the same
line on every run.
"""

import os
import sys

LINE = "I told my guitar it was out of tune. It said, 'I'm just fretting over nothing.'"


def check(line: str) -> None:
    # The sealed gate: UTF-8 text, 1 to 140 characters, not only white space.
    if not line or not line.strip():
        sys.exit("entry must not be empty or only white space")
    if len(line) > 140:
        sys.exit("entry must be at most 140 characters, got %d" % len(line))
    if "\n" in line or "\r" in line:
        sys.exit("entry must be a single line")


def main() -> None:
    check(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open(path, encoding="utf-8") as f:
        if f.read() != LINE:
            sys.exit("entry.txt does not match the entry")


if __name__ == "__main__":
    main()
