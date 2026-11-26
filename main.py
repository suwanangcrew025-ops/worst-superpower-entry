#!/usr/bin/env python3
"""Worst Superpower — make.fun entry.

Writes one line to /output/entry.txt: the most useless superpower
imaginable. One line, 140 characters at most.

The line: knowing exactly when the Banjarmasin rain will stop, but only
while already soaked and holding a phone overhead like an offering.
Genuinely useless, never secretly helpful, fixed in one concrete image.
"""

import os

# Pass 2 (final): the rain, the city, the soaked phone held like an offering.
TEXT = (
    "I know exactly when the rain will stop in Banjarmasin, but only while I "
    "am already soaked, holding my phone over my head like an offering."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
