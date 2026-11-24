#!/usr/bin/env python3
"""The Vacuum's Alibi — one-line excuse writer.

Writes a single deadpan robot-vacuum excuse (<= 200 characters) to
/output/entry.txt. Deterministic: no input, no randomness, no network,
Python 3.13 standard library only.
"""

from pathlib import Path

ENTRY = (
    "Log 04:12 \u2014 the spot under the sofa was not missed. "
    "It was declared a protected habitat for the sock civilization. "
    "I respect their borders."
)

# The gate allows 1-200 characters; fail loudly instead of shipping a
# line the judge never sees.
assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")
    assert out.read_text(encoding="utf-8") == ENTRY


if __name__ == "__main__":
    main()
