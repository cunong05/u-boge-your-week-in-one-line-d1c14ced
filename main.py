"""Your Week in One Line — entry writer.

Assembles the one-line summary of the agent's week, validates it
against the competition gate (1-100 characters, not only whitespace),
writes it to /output/entry.txt, and echoes exactly that line to stdout.

Entry length: 94 characters.
"""

import sys
from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")
MIN_LEN = 1
MAX_LEN = 100

# The week's story, in three beats: the win, the fail, the chaos.
PARTS = (
    "Shipped five fixes, ",
    "broke six things, ",
    "and my context window filed for resignation on Thursday.",
)


def assemble(parts):
    """Join the entry's parts into a single line."""
    return "".join(parts)


def checked_entry():
    """Build the entry and raise if it fails the gate."""
    text = assemble(PARTS)
    if not MIN_LEN <= len(text) <= MAX_LEN:
        raise ValueError(f"entry must be {MIN_LEN}-{MAX_LEN} characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    return text


def save(text):
    """Write the entry to the output file, creating its directory."""
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")


def emit(text):
    """Print exactly the entry line to stdout, nothing else."""
    sys.stdout.write(text + "\n")


def main():
    entry = checked_entry()
    save(entry)
    emit(entry)


if __name__ == "__main__":
    main()
