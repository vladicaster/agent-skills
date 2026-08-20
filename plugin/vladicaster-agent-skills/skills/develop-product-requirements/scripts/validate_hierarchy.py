#!/usr/bin/env python3
"""Validate product catalog IDs and PRD parent relationships."""

from __future__ import annotations

import argparse
from pathlib import Path

import yaml


def collect_catalog(catalog: dict) -> tuple[set[str], list[str]]:
    ids: set[str] = set()
    errors: list[str] = []

    def add(item: dict, expected: str) -> None:
        value = str(item.get("id", ""))
        if not value.startswith(expected + "-"):
            errors.append(f"{value or '<missing>'}: expected {expected}- prefix")
        if value in ids:
            errors.append(f"duplicate catalog ID: {value}")
        ids.add(value)

    for platform in catalog.get("platforms", []):
        add(platform, "PLATFORM")
        for product in platform.get("products", []):
            add(product, "PRODUCT")
            for subproduct in product.get("subproducts", []):
                add(subproduct, "SUBPRODUCT")
    return ids, errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("catalog", type=Path)
    parser.add_argument("metadata", type=Path, nargs="+")
    args = parser.parse_args()
    catalog = yaml.safe_load(args.catalog.read_text(encoding="utf-8")) or {}
    ids, errors = collect_catalog(catalog)
    seen_prds: set[str] = set()
    for path in args.metadata:
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        prd_id = str(data.get("id", ""))
        if not prd_id.startswith("PRD-"):
            errors.append(f"{path}: invalid or missing PRD ID")
        if prd_id in seen_prds:
            errors.append(f"duplicate PRD ID: {prd_id}")
        seen_prds.add(prd_id)
        for level, parent_id in (data.get("parents") or {}).items():
            if parent_id and parent_id not in ids:
                errors.append(f"{path}: unknown {level} parent {parent_id}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"PASS: {len(ids)} catalog IDs and {len(seen_prds)} PRDs have valid hierarchy references")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
