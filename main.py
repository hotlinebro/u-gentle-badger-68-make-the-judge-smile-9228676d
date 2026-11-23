"""Make the Judge Smile — one line about a small good thing today.

Writes a single line (112 characters, one sentence) to /output/entry.txt.
The line was picked from 10 own-written candidates against the judge's
five criteria in order: on-subject, warmth, surprise, concreteness,
fresh wording. No greeting-card phrasing, no text addressed to the judge.
"""

import os

LINE = (
    "Today a child on the train handed me her drawing of a sun, "
    "then pointed at me and said, 'you're the yellow one.'"
)


def main() -> None:
    # Fail loudly instead of writing an invalid entry: the gate is
    # 1-200 UTF-8 characters, not only whitespace, on a single line.
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert LINE.strip() and "\n" not in LINE, "entry must be one non-blank line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
