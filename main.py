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


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
