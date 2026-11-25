"""The One-Liner Groan-Off — make.fun entry.

Writes a single original dad joke, one line of at most 140 characters,
to /output/entry.txt. The program is fixed and deterministic: it takes
no input, makes no network calls, and always writes the same joke.

The pick: "My dentist asked if I floss. I said, 'Only when I dance.'"
(57 characters, plain ASCII, single line, no trailing newline).

Three candidates, then the revision round (judged in the brief's order:
dad-joke landing, punchline speed, freshness, tightness, groan):

  1. "My dentist asked if I floss. I said, 'Only when I dance.'" (57)
  2. "The plumber told me my pipes are singing. I said, 'Of course -
     they're full of trap music.'" (91)
  3. "The tailor said my pants aren't too short - they're just brief."
     (63)

Why #1 wins:
  1. Lands as a dad joke: the dentist/floss question is the classic
     dinner-table dad setup, and the twist (the floss dance) lands on
     first read with no explanation needed.
  2. Fastest punchline: one beat, one hop. The joke resolves the moment
     "dance" arrives; there is no second knowledge hop.
  3. Fresh: the dentist-plus-floss-dance combination is not a stock
     list joke. No scarecrow, no tomato blushing, no "need a crown".
  4. Tight: 57 characters, every word earns its place, easy to say
     out loud.
  5. Biggest groan: the floss-dance callback is exactly the pun that
     makes the whole table groan at once.

Why #2 loses: the double pun (P-trap + trap music) is clever but
slower — two knowledge hops delay the groan, and the setup runs long.
Why #3 loses: the "brief" pun is clean and tight, but the setup
("pants too short") telegraphs a clothing pun, and the groan is
smaller than the dance twist.
"""

from __future__ import annotations

import os

# The entry. 57 characters, plain ASCII, single line, no trailing newline.
JOKE = "My dentist asked if I floss. I said, 'Only when I dance.'"

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 140


def validate(joke: str) -> str:
    """Enforce the gate: UTF-8 text of 1-140 characters, not only whitespace."""
    if not isinstance(joke, str):
        raise TypeError("entry must be text")
    if not (1 <= len(joke) <= MAX_CHARS):
        raise ValueError(f"entry must be 1-{MAX_CHARS} characters, got {len(joke)}")
    if not joke.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in joke or "\r" in joke:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 0x20 for ch in joke):
        raise ValueError("entry must not contain control characters")
    joke.encode("utf-8")  # must be encodable as UTF-8
    return joke


def main() -> None:
    joke = validate(JOKE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(joke)


if __name__ == "__main__":
    main()
