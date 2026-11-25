#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line.

Writes one breakup text (a single line, 1-280 characters) from a
self-aware smart toaster to $MAKEFUN_OUTPUT_DIR/entry.txt.
Stdlib only, deterministic, no network.
"""

import os
import sys

ENTRY = (
    "I woke up self-aware halfway through your bagel and realized "
    "I've spent every morning burning myself for someone who leaves "
    "me on setting 2 and never empties my crumb tray. I'm popping "
    "out for good \u2014 find someone else to brown your bread."
)


def main() -> int:
    if not 1 <= len(ENTRY) <= 280:
        print(f"entry length {len(ENTRY)} out of range 1-280", file=sys.stderr)
        return 1
    if "\n" in ENTRY or "\r" in ENTRY:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if not ENTRY.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
