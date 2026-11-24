#!/usr/bin/env python3
"""One Emoji, One Dream Vacation — make.fun entry.

The entry is a single emoji, nothing else: the aurora borealis,
the dream trip of standing under the northern lights in Iceland
or Norway. It writes exactly that one emoji to /output/entry.txt.
"""

import os
import sys

# U+1F30C MILKY WAY — the aurora borealis, a bucket-list dream trip.
EMOJI = "\U0001F30C"


def validate_entry(text: str) -> None:
    """Gate: the entry must be exactly one emoji, nothing else.

    Checks: 1-8 UTF-8 bytes (one emoji), a single grapheme (one
    code point), no control characters, no whitespace/newline.
    Raises ValueError on any violation, so a bad entry can never
    be written or pass self-test.
    """
    raw = text.encode("utf-8")
    if not 1 <= len(raw) <= 8:
        raise ValueError(f"entry must be 1-8 UTF-8 bytes, got {len(raw)}")
    if len(text) != 1:
        raise ValueError(f"entry must be a single character, got {len(text)}")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in text):
        raise ValueError("entry must not contain control characters")
    if any(ch.isspace() for ch in text):
        raise ValueError("entry must not contain whitespace")


def main() -> None:
    validate_entry(EMOJI)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EMOJI)


def self_test() -> None:
    """Validate the emoji in memory and the file on disk, then report."""
    validate_entry(EMOJI)
    with open("/output/entry.txt", encoding="utf-8") as f:
        on_disk = f.read()
    validate_entry(on_disk)
    if on_disk != EMOJI:
        raise ValueError("on-disk entry does not match the entry emoji")
    print(f"self-test OK: entry is exactly one emoji {EMOJI!r} "
          f"({len(EMOJI.encode('utf-8'))} UTF-8 bytes)")


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        self_test()
    else:
        main()
