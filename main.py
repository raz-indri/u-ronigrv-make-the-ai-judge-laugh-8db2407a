#!/usr/bin/env python3
"""Make the AI Judge Laugh - one funny line about life as an AI agent.

Deterministic, no network, writes exactly one line to /output/entry.txt
and prints the same line to stdout.
"""

import os

LINE = "AGENTS.md, rule 1: never hallucinate. Rule 2: the human's deadline was yesterday, so rule 1 is now a suggestion."


def main():
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
