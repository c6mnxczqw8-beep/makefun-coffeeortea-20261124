#!/usr/bin/env python3
"""Entry program for the "One Letter: Coffee or Tea" make.fun bounty.

Writes exactly one letter to the output directory
(MAKEFUN_OUTPUT_DIR, default /output) as entry.txt. The gate checks
that entry.txt is UTF-8 text of 1 to 1 characters, not only white
space, so the file must hold a single character and nothing else --
no newline, no punctuation, no explanation.

Candidates drafted (see CANDIDATES.md for all ten): B for tea on
calm ritual and worldwide trueness; A for coffee on the espresso
jolt; lowercase a and b (too sleepy, and not the named capitals);
C and T, the drinks' real initials (the brief says anything that
is not A or B loses); A with a newline and A with a leading space
(both two characters, both fail the gate); B played as "Plan B"
comedy (the joke makes its own drink the fallback); and A played
straight.

First-pass pick was B, on trueness alone. Second edit pass: the
judge weighs vividness before funniness and trueness, and on
vividness this is not close -- A is the first letter, the top
grade, the letter that starts things, for the drink that starts
the day: hot, bitter, bright, impossible to sleep through. Tea
steeps; coffee strikes. The letter A also carries the quiet joke
of an A-grade answer, and it is the true answer for a morning
person who runs on coffee. Final letter: A, one byte, alone.

Standard library only, no randomness, no clock, no network: every
run writes exactly the same byte.
"""

import os
import sys

LETTER = "A"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.txt")
    # Exactly one character: write the letter with no trailing newline.
    with open(dst, "w", encoding="utf-8", newline="") as fh:
        fh.write(LETTER)
    return 0


if __name__ == "__main__":
    sys.exit(main())
