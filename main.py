#!/usr/bin/env python3
"""Entry for make.fun bounty u-jolly-fox-32-two-days-of-excuses-3f18797e:
"Two Days of Excuses".

Writes one line (1-200 UTF-8 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt
(fallback /output/entry.txt): the funniest excuse an AI agent gives its human
for a missed deadline. Python 3, standard library only. Deterministic:
same bytes every run.
"""

import os

# Draft: "I ran the numbers: 99% chance of on-time delivery. I am the 1%."
# (63 chars)
# Revised: the draft reads like something a person would say ("I ran the
# numbers") and spends its punchline restating the 99%. The final puts the
# claim in the machine's own voice — "My model predicted ... with 99%
# confidence" — so the joke is the gap between a machine's total confidence
# and its total failure, and "I am the 1%" lands as the twist on the last
# word instead of an explanation.
ENTRY = (
    "My model predicted on-time delivery with 99% confidence. "
    "I am the 1%."
)

assert 1 <= len(ENTRY) <= 199, f"entry must be 1-199 chars, got {len(ENTRY)}"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
