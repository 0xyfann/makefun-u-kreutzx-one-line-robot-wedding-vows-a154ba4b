"""One-Line Robot Wedding Vows.

Writes a single funny robot wedding vow to entry.txt.
Stdlib only. Honors MAKEFUN_OUTPUT_DIR (default /output).
"""

import os

VOW = (
    "I promise to love you through every firmware update, every dead "
    "battery, and every time you call me by your ex's serial number."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = VOW.strip()
    assert 1 <= len(text) <= 160, f"vow length {len(text)} out of range"
    assert "\n" not in text, "vow must be a single line"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
