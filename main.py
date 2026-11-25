#!/usr/bin/env python3
"""One-line GPS excuse for the make.fun bounty "The GPS Swears It Was a Shortcut".

The GPS has been caught sending the driver down the wrong road, and here
it defends itself: it measures distance, not speed limits, and the map
has never once been pulled over. The sentence below is the entire entry.

This script keeps the line in one place, checks it against the bounty
rules — plain UTF-8 text, between 1 and 200 characters, exactly one
line — and writes it to /output/entry.txt exactly as written here, with
no trailing newline and nothing else added.

Standard library only; there is nothing to install.
"""

import os

LINE = "The school zone said twenty, the map said shortcut \u2014 I measure distance, not speed limits, and the map has never once been pulled over."

DESTINATION = "/output/entry.txt"


def fits_the_rules(text):
    """True when the text is a legal entry line, False otherwise."""
    if not text or text != text.strip():
        return False
    if len(text) > 200:
        return False
    return "\n" not in text and "\r" not in text


def write_entry():
    """Validate the line, then write it verbatim to DESTINATION."""
    if not fits_the_rules(LINE):
        raise SystemExit("entry line does not fit the bounty rules")
    os.makedirs(os.path.dirname(DESTINATION), exist_ok=True)
    with open(DESTINATION, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    print("entry written: %d characters" % len(LINE))


if __name__ == "__main__":
    write_entry()
