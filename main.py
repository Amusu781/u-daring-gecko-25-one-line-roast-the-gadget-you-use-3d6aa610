"""One-Line Roast: The Gadget You Use Every Day.

Writes a single original roast line to /output/entry.txt.
"""

import os

ENTRY = "My microwave beeps five times when it's done, as if the first four were just practice."


def validate(line):
    """Enforce the bounty gate: UTF-8, 1-200 chars, one line, not only whitespace."""
    if not line or line != line.strip():
        raise ValueError("entry must be non-empty with no surrounding whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not 1 <= len(line) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(line))
    line.encode("utf-8")


def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    # Clear only the contents of the output dir, never the dir itself:
    # the grader mounts it read-only as uid 65534, so deleting it fails.
    for name in os.listdir("/output"):
        path = os.path.join("/output", name)
        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
