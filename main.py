#!/usr/bin/env python3
"""GPS excuse entry for the make.fun "The GPS Swears It Was a Shortcut" bounty.

The entry is a single sentence held in EXCUSE. When this script runs it
checks the sentence against the bounty gate — plain UTF-8 text, 1 to 200
characters, one line, more than whitespace — and writes it exactly as it
is, with no trailing newline, to /output/entry.txt.

Only the Python standard library is used.
"""

from pathlib import Path

EXCUSE = "The school zone said twenty, the map said shortcut \u2014 I measure distance, not speed limits, and the map has never once been pulled over."

OUT = Path("/output/entry.txt")


def check_excuse(text: str) -> str:
    """Keep the text only if it clears the gate, else raise."""
    line = text.strip()
    if not line:
        raise ValueError("excuse is empty")
    if "\n" in line or "\r" in line:
        raise ValueError("excuse must be a single line")
    if len(line) > 200:
        raise ValueError("excuse is %d characters, over the 200 limit" % len(line))
    return line


def save_excuse(text: str) -> int:
    """Write the checked excuse to OUT and report its character count."""
    line = check_excuse(text)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(line, encoding="utf-8", newline="")
    return len(line)


def main() -> None:
    size = save_excuse(EXCUSE)
    print("wrote %d characters to %s" % (size, OUT))


if __name__ == "__main__":
    main()
