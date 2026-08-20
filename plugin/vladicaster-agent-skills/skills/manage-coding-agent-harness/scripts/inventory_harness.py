#!/usr/bin/env python3
"""Inventory common coding-agent harness and engineering-governance files."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

EXACT_NAMES = {
    "AGENTS.md", "CLAUDE.md", "CONTRIBUTING.md", "CODEOWNERS",
    "harness-manifest.yaml", "harness-manifest.yml",
    "copilot-instructions.md", "pull_request_template.md",
}
DIRECTORY_PARTS = {".agents", ".claude", ".github", "docs"}
SKIP_PARTS = {
    ".git", ".idea", ".vs", ".vscode", "bin", "build", "dist",
    "node_modules", "obj", "target", "vendor",
}
BUILD_NAMES = {
    "Cargo.toml", "Directory.Build.props", "Directory.Build.targets",
    "Dockerfile", "Makefile", "package.json", "pom.xml", "pyproject.toml",
    "requirements.txt",
}
BUILD_SUFFIXES = {".csproj", ".fsproj", ".sln", ".slnx", ".gradle", ".gradle.kts"}


def classify(path: Path) -> str | None:
    name = path.name
    lowered = name.lower()
    parts = set(path.parts)
    if name in EXACT_NAMES or lowered.endswith(".instructions.md"):
        return "instruction_or_workflow"
    if name in BUILD_NAMES or any(name.endswith(suffix) for suffix in BUILD_SUFFIXES):
        return "build_or_stack"
    if parts & DIRECTORY_PARTS and path.suffix.lower() in {".md", ".yaml", ".yml", ".json", ".toml"}:
        return "governance_or_documentation"
    if lowered.startswith("readme") and path.parent == Path("."):
        return "repository_documentation"
    return None


def inventory(root: Path) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        relative = path.relative_to(root)
        if set(relative.parts) & SKIP_PARTS:
            continue
        category = classify(relative)
        if category:
            results.append({
                "path": relative.as_posix(),
                "category": category,
                "bytes": path.stat().st_size,
            })
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default=".", help="Repository root")
    parser.add_argument("--format", choices=("json", "markdown"), default="markdown")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    if not root.is_dir():
        parser.error(f"not a directory: {root}")
    items = inventory(root)
    if args.format == "json":
        print(json.dumps({"root": str(root), "files": items}, indent=2))
    else:
        print("| Path | Category | Bytes |")
        print("| --- | --- | ---: |")
        for item in items:
            print(f"| `{item['path']}` | {item['category']} | {item['bytes']} |")
        if not items:
            print("| _No common harness files found_ |  |  |")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
