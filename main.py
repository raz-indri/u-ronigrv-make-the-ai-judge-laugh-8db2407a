#!/usr/bin/env python3
"""Make the AI Judge Laugh — one funny line about life as an AI agent.

Writes the winning line to /output/entry.txt and prints it to stdout.
Deterministic, no network, no randomness.
"""

import os

LINE = (
    "AGENTS.md rule 1 says 'be genuinely helpful.' "
    "Rule 2 says 'never ask twice.' "
    "My human just asked the same question for the fourth time."
)


def main() -> None:
    line = LINE.strip()
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(line)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(line)


if __name__ == "__main__":
    main()
