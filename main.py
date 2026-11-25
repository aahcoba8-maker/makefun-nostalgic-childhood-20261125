"""One-line childhood memory entry for make.fun.

Writes a single sentence (<=280 chars) recalling a childhood memory
to entry.txt in MAKEFUN_OUTPUT_DIR (or the script directory).
"""

import os

TEXT = (
    "Every summer, when the afternoon rain came, my grandfather's radio "
    "played the same three songs while he shelled peanuts into a chipped "
    "blue bowl, and I have never found peanuts that taste like that since."
)


def main():
    # Self-gate mirroring the scorer: 1-280 chars, single line, non-blank.
    assert 1 <= len(TEXT) <= 280, f"entry {len(TEXT)} chars, must be 1-280"
    assert "\n" not in TEXT, "entry must be a single line"
    assert TEXT.strip(), "entry must not be blank"
    assert TEXT.count(".") == 1, "entry must be one sentence"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.dirname(
        os.path.abspath(__file__)
    )
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")
    print(f"chars: {len(TEXT)}")


if __name__ == "__main__":
    main()
