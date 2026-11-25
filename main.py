"""One line: the funniest commit message for the worst fix ever.

Writes a single line (69 chars, cap 100) to /output/entry.txt.
"""

from pathlib import Path

LINE = "fix(tests): silence flaky test by deleting the only check that ran it"

OUT = Path("/output/entry.txt")


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
