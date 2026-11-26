#!/usr/bin/env python3
"""Name the Robot Band — make.fun entry.

The band: 404 Not Found. The hit: "We Were Never Here" — streamed 0 times,
which is exactly the point. The joke is the band itself: a robot band named
after the error for a missing page, whose greatest hit nobody can find.
The brief asks for a joke that lands on the first read — a band that was
never there needs no setup at all.
"""

import os

ENTRY = (
    '404 Not Found: their hit "We Were Never Here" has been streamed '
    "0 times, which is exactly the point."
)


def main():
    print(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
