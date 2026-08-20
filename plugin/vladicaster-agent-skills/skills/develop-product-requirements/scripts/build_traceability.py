#!/usr/bin/env python3
"""Build a Markdown PRD-to-GitHub traceability report from YAML."""

from __future__ import annotations

import argparse
from pathlib import Path

import yaml


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("traceability", type=Path)
    parser.add_argument("--strict", action="store_true", help="Fail when a requirement has no issue mapping")
    args = parser.parse_args()
    data = yaml.safe_load(args.traceability.read_text(encoding="utf-8")) or {}
    prd_id = data.get("prd_id")
    requirements = data.get("requirements") or {}
    if not prd_id or not isinstance(requirements, dict):
        parser.error("traceability file requires prd_id and requirements mapping")
    uncovered = []
    print(f"# Traceability: {prd_id}\n")
    print("| Requirement | Acceptance | GitHub issues | PRs | Tests | Status |")
    print("| --- | --- | --- | --- | --- | --- |")
    for req_id, item in requirements.items():
        acceptance = ", ".join(item.get("acceptance") or []) or "—"
        issues = item.get("issues") or []
        issue_text = ", ".join(
            f"{issue.get('repository')}#{issue.get('number')} ({issue.get('role', 'delivery')})"
            for issue in issues
        ) or "—"
        prs = ", ".join(
            f"{pr.get('repository')}#{pr.get('number')}" if isinstance(pr, dict) else str(pr)
            for pr in (item.get("pull_requests") or [])
        ) or "—"
        tests = ", ".join(map(str, item.get("tests") or [])) or "—"
        statuses = {str(issue.get("status", "planned")) for issue in issues}
        status = ", ".join(sorted(statuses)) if statuses else "unmapped"
        if not issues:
            uncovered.append(req_id)
        print(f"| {req_id} | {acceptance} | {issue_text} | {prs} | {tests} | {status} |")
    print(f"\nCoverage: {len(requirements) - len(uncovered)}/{len(requirements)} requirements mapped to issues.")
    if uncovered:
        print("Unmapped: " + ", ".join(uncovered))
    return 1 if args.strict and uncovered else 0


if __name__ == "__main__":
    raise SystemExit(main())
