"""One Star for Monday — make.fun entry.

Writes a single one-star review of Monday, written as though Monday were
a restaurant, to /output/entry.txt. The line must be at most 25 words of
plain text, sound like a real diner's complaint, and land the joke on
Monday itself — the table Monday lost, the bill that arrives too soon.

Why this line: it keeps all four restaurant props the judge wants
(reservation, table, bill, food) in one complaint, and the joke only
works on Monday — it is the one day whose table the next day can take.
"""

from pathlib import Path

REVIEW = "One star. Monday took my reservation, gave my table to Tuesday, and served the bill before the food."


def main() -> None:
    # Gate: 1-180 characters, at most 25 words, plain text, not blank.
    words = REVIEW.split()
    assert 1 <= len(REVIEW) <= 180, f"review is {len(REVIEW)} chars"
    assert 1 <= len(words) <= 25, f"review is {len(words)} words"
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(REVIEW + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
