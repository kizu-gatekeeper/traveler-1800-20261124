#!/usr/bin/env python3
"""Write the entry sentence to $MAKEFUN_OUTPUT_DIR/entry.txt.

Entry for make.fun's "One Sentence for a Traveler from 1800" bounty:
one sentence of at most 200 characters explaining the modern internet
to someone arriving from the year 1800, built only from things that
person already knows -- post roads, letters, libraries, markets.
"""

import os
import sys

LINE = "Picture a web of post roads swifter than any horse, joining every library, market and workshop on Earth, where a letter crosses the world in a breath and any man may read any book from his own chair."


def write_entry(out_dir: str) -> str:
    """Write the sentence to ``entry.txt`` in ``out_dir``; return its path.

    The file holds exactly the sentence and nothing else: one line of
    plain text, no trailing newline, so the gate reads the 199
    characters and nothing more.
    """
    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    return entry_path


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)
    return 0


if __name__ == "__main__":
    sys.exit(main())
