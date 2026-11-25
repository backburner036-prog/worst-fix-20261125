"""Commit-message entry for make.fun: one line, at most 100 chars.

The program writes LINE verbatim to /output/entry.txt (69 chars).
"""

from pathlib import Path

LINE = "fix(tests): silence flaky test by deleting the only check that ran it"
ENTRY_PATH = Path("/output/entry.txt")


def main() -> None:
    """Write the entry text, creating /output when needed."""
    ENTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
    ENTRY_PATH.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
