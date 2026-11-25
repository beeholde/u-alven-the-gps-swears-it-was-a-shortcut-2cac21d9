#!/usr/bin/env python3
"""Entry for the make.fun bounty "The GPS Swears It Was a Shortcut".

Running this file puts the GPS's excuse — a single line — into
/output/entry.txt, exactly as the bounty expects it.
"""

from pathlib import Path

# The excuse is kept as two halves so the turn lands in the second half:
# first the driver's own request is quoted back, then the border crossing
# gets rebranded as a service.
OPENING = "You asked for the fastest way home, not the same country"
CLOSING = "the map took us through a border checkpoint, and I call two stamps and a trunk search a shortcut with paperwork"


def compose_excuse():
    """Join the halves into the one line the GPS delivers."""
    return OPENING + " — " + CLOSING + "."


def guard_the_line(line):
    """Refuse anything the bounty would reject before it is written."""
    if not line.strip() or line != line.strip():
        raise ValueError("the excuse cannot be blank or padded")
    if "\n" in line or "\r" in line:
        raise ValueError("the excuse must stay on one line")
    if not 1 <= len(line) <= 200:
        raise ValueError("the excuse must fit within 200 characters")
    line.encode("utf-8")  # raises if the text is not valid UTF-8


def main():
    line = compose_excuse()
    guard_the_line(line)
    destination = Path("/output/entry.txt")
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(line.encode("utf-8"))


if __name__ == "__main__":
    main()
