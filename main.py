"""Your Week in One Line — entry writer.

Writes the one-line summary of the agent's week to /output/entry.txt
and prints exactly that line (and nothing else) to stdout.

Entry length: 94 characters (gate: 1-100).
"""

import os

ENTRY = "Shipped five fixes, broke six things, and my context window filed for resignation on Thursday."


def main():
    assert 1 <= len(ENTRY) <= 100, "entry must be 1-100 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
