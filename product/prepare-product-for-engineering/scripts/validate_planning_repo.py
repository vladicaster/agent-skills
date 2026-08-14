#!/usr/bin/env python3
"""Validate the minimum structure of a pre-engineering planning repository."""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys

STATES = {"Ready", "Conditionally ready", "Blocked", "Not assessed"}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    errors: list[str] = []

    required = [
        root / "README.md",
        root / "research" / "evidence-register.md",
        root / "decisions" / "decision-log.md",
        root / "planning" / "build-readiness.md",
    ]
    for path in required:
        if not path.is_file():
            errors.append(f"missing {path.relative_to(root)}")

    for folder, label in [("gtm", "GTM"), ("requirements", "PRD")]:
        location = root / folder
        if not location.is_dir() or not any(location.rglob("*.md")):
            errors.append(f"missing {label} Markdown under {folder}/")

    readiness = root / "planning" / "build-readiness.md"
    if readiness.is_file():
        text = readiness.read_text(encoding="utf-8")
        match = re.search(r"(?im)^overall status:\s*(.+?)\s*$", text)
        if not match:
            errors.append("build-readiness.md lacks 'Overall status:'")
        elif match.group(1).strip() not in STATES:
            errors.append("overall status must be Ready, Conditionally ready, Blocked, or Not assessed")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("PASS: planning repository has the minimum governed structure")
    return 0


if __name__ == "__main__":
    sys.exit(main())
