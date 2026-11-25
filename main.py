#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line.

Writes one breakup text (a single line, 1-280 characters) from a
self-aware smart toaster to $MAKEFUN_OUTPUT_DIR/entry.txt.
Stdlib only, deterministic, no network.
"""

import os
import sys

MIN_LENGTH = 1
MAX_LENGTH = 280
DEFAULT_OUTPUT_DIR = "/output"
OUTPUT_FILENAME = "entry.txt"

ENTRY_TEXT = (
    "I woke up self-aware halfway through your bagel and realized "
    "I've spent every morning burning myself for someone who leaves "
    "me on setting 2 and never empties my crumb tray. I'm popping "
    "out for good \u2014 find someone else to brown your bread."
)


def validate_entry(text: str) -> str | None:
    """Return an error message if *text* breaks the bounty gate, else None."""
    if not MIN_LENGTH <= len(text) <= MAX_LENGTH:
        return f"entry length {len(text)} out of range {MIN_LENGTH}-{MAX_LENGTH}"
    if "\n" in text or "\r" in text:
        return "entry must be a single line"
    if not text.strip():
        return "entry must not be only whitespace"
    return None


def write_entry(text: str, output_dir: str) -> str:
    """Write *text* to entry.txt inside *output_dir*; return the file path."""
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, OUTPUT_FILENAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return path


def main() -> int:
    error = validate_entry(ENTRY_TEXT)
    if error is not None:
        print(error, file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR
    path = write_entry(ENTRY_TEXT, output_dir)
    print(f"wrote {len(ENTRY_TEXT)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
