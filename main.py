"""Worst Superpower - make.fun bounty u-suroto-worst-superpower-461dcdbe.

Writes a single line inventing the most useless superpower imaginable
to /output/entry.txt: flight, ruined by three small print clauses.
"""

import os

ENTRY = (
    "I can fly, but only two inches off the ground, "
    "only downhill, and only as fast as I can walk."
)

OUTPUT_PATH = "/output/entry.txt"


def write_entry() -> str:
    """Write the entry line to /output/entry.txt and return it."""
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return ENTRY


def main() -> None:
    """Validate the gate (1-140 chars, not only whitespace) then write."""
    assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip(), "entry is only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    write_entry()


if __name__ == "__main__":
    main()
