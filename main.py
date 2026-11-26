"""The One-Liner Groan-Off — entry program (program/v1).

Writes exactly one original dad joke to /output/entry.txt.
Stdlib only, deterministic, offline: same bytes on every run.
"""

from pathlib import Path

# 114 characters, one line: current / charges / shocking / resisted —
# four electricity puns stacked so the groan builds to the last two words.
JOKE = (
    "I was fired for stealing electricity, but I found a current job "
    "\u2014 the charges were shocking, so I resisted arrest."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    try:
        OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
        OUTPUT_PATH.write_text(JOKE, encoding="utf-8")
    except OSError:
        # Local fallback for running outside the grading sandbox.
        fallback = Path("output") / "entry.txt"
        fallback.parent.mkdir(parents=True, exist_ok=True)
        fallback.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
