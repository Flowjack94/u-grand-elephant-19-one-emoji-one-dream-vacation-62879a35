#!/usr/bin/env python3
"""One Emoji, One Dream Vacation — make.fun entry.

The entry is a single emoji, nothing else: the aurora borealis,
the dream trip of standing under the northern lights in Iceland
or Norway. It writes exactly that one emoji to /output/entry.txt.
"""

import os

# U+1F30C MILKY WAY — the aurora borealis, a bucket-list dream trip.
EMOJI = "\U0001F30C"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
