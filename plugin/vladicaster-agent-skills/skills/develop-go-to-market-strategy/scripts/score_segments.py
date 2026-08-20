#!/usr/bin/env python3
"""Rank GTM segments from a CSV scorecard using transparent weighted criteria."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

CRITERIA = {
    "problem_intensity": 0.20,
    "urgency": 0.15,
    "willingness_to_pay": 0.15,
    "reachability": 0.15,
    "product_fit": 0.15,
    "proof": 0.08,
    "expansion": 0.07,
    "cost_to_serve": 0.05,
}


def score(value: str, field: str, row_number: int) -> float:
    try:
        number = float(value)
    except ValueError as exc:
        raise ValueError(f"row {row_number}: {field} must be numeric") from exc
    if not 1 <= number <= 5:
        raise ValueError(f"row {row_number}: {field} must be between 1 and 5")
    return 6 - number if field == "cost_to_serve" else number


def rank(path: Path) -> list[dict[str, object]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        required = {"segment", *CRITERIA}
        missing = required - set(reader.fieldnames or [])
        if missing:
            raise ValueError("missing columns: " + ", ".join(sorted(missing)))
        rows = []
        for number, row in enumerate(reader, start=2):
            segment = (row.get("segment") or "").strip()
            if not segment:
                raise ValueError(f"row {number}: segment is required")
            total = sum(score(row[field], field, number) * weight for field, weight in CRITERIA.items())
            rows.append({"segment": segment, "score": round(total, 2), "notes": row.get("notes", "")})
    return sorted(rows, key=lambda item: (-float(item["score"]), str(item["segment"]).lower()))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("scorecard", type=Path)
    parser.add_argument("--format", choices=("markdown", "csv"), default="markdown")
    args = parser.parse_args()
    try:
        rows = rank(args.scorecard)
    except (OSError, ValueError) as exc:
        parser.error(str(exc))
    if args.format == "csv":
        writer = csv.DictWriter(__import__("sys").stdout, fieldnames=["rank", "segment", "score", "notes"])
        writer.writeheader()
        for index, row in enumerate(rows, start=1):
            writer.writerow({"rank": index, **row})
    else:
        print("| Rank | Segment | Score / 5 | Notes |")
        print("| ---: | --- | ---: | --- |")
        for index, row in enumerate(rows, start=1):
            notes = str(row["notes"]).replace("|", "\\|")
            print(f"| {index} | {row['segment']} | {row['score']:.2f} | {notes} |")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
