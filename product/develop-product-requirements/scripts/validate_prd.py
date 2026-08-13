#!/usr/bin/env python3
"""Validate required PRD sections and stable requirement identifiers."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

REQUIRED = {
    "problem and evidence",
    "users and stakeholders",
    "objectives and success measures",
    "scope and priorities",
    "functional requirements",
    "nonfunctional requirements",
    "acceptance and validation",
    "out of scope",
    "open questions and decisions",
    "traceability",
}
ID_PATTERN = re.compile(r"\bPRD-[A-Z0-9-]+-(?:FR|NFR|AC|METRIC)-\d{3,}\b")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("prd", type=Path)
    args = parser.parse_args()
    text = args.prd.read_text(encoding="utf-8")
    headings = {
        match.group(1).strip().lower()
        for match in re.finditer(r"^#{2,3}\s+(.+?)\s*$", text, re.MULTILINE)
    }
    missing = sorted(REQUIRED - headings)
    ids = ID_PATTERN.findall(text)
    duplicates = sorted({item for item in ids if ids.count(item) > 1})
    errors = []
    if missing:
        errors.append("missing sections: " + ", ".join(missing))
    if not any("-FR-" in item for item in ids):
        errors.append("no stable functional requirement IDs found")
    if not any("-AC-" in item for item in ids):
        errors.append("no stable acceptance criterion IDs found")
    if duplicates:
        errors.append("duplicate identifiers: " + ", ".join(duplicates))
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"PASS: {args.prd} contains required sections and {len(ids)} unique traceable identifiers")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
