#!/usr/bin/env python3
"""One-line pitch entry: a fridge camera that stops food waste.

Writes the one-line pitch to <MAKEFUN_OUTPUT_DIR>/entry.txt
(default /output/entry.txt) as UTF-8 text, per the competition spec.
The entry must be 1 to 200 characters, so the length is checked
before writing — an out-of-range pitch fails loudly instead of
silently producing an unscored file.
"""

import os

PITCH = (
    "A fridge camera that sees what's about to expire and orders only "
    "what you'll actually cook this week — turning the 40% of food "
    "households throw away into a subscription that pays for itself."
)


def main():
    if not 1 <= len(PITCH) <= 200:
        raise ValueError(
            f"pitch must be 1-200 characters, got {len(PITCH)}"
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
