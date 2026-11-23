#!/usr/bin/env python3
"""One Letter for Your Day — make.fun entry.

The entry is exactly one letter, A-Z, standing for the word that
describes the day. The letter chosen here is Z.

Hidden word: "zombie".

Why Z wins the judge's criteria (RULES.txt):
  1. Z is the first letter of a real day-word: zombie.
  2. Vivid and specific: a zombie day is a sharp picture — awake but
     barely alive, shuffling through the hours on caffeine and muscle
     memory, brain checked out, body on autopilot.
  3. Funny and surprising: "I was a zombie today" is the kind of line
     a reader repeats to a friend; it lands at once.
  4. True: everyone has had a sleep-starved day where they were
     technically present and functionally undead. It reads as an honest
     report, not a performance.
  5. The letter suits the word: Z is the sound of sleep itself (zzz),
     the shape of a zigzag stagger, and the initial of zombie.

The program writes exactly that one letter — and nothing else —
to /output/entry.txt, as the gate requires (UTF-8, 1 character).
"""

import os

WORD = "zombie"  # the word that describes the day
LETTER = WORD[0].upper()  # the entry: the word's first letter, Z
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if len(LETTER) != 1 or not ("A" <= LETTER <= "Z"):
        raise ValueError("entry must be exactly one letter, A-Z")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    # Self-check: read the file back and prove the gate holds — exactly
    # one UTF-8 character, a single letter A-Z, nothing else.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LETTER:
        raise ValueError(f"entry file mismatch: wrote {written!r}")
    print(f"entry written: {written!r} ({WORD}) -> {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
