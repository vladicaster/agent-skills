#!/usr/bin/env python3
"""Validate repository-wide Agent Skill structure and documentation propagation."""

from __future__ import annotations

import ast
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
IGNORED_PARTS = {".git", "__pycache__"}
REQUIRED_README_HEADINGS = ("## Updating this skill",)
PLUGIN_GUIDE = "docs/plugin-installation-and-updates.md"


def markdown_files() -> list[Path]:
    return sorted(
        path for path in ROOT.rglob("*.md")
        if not set(path.relative_to(ROOT).parts) & IGNORED_PARTS
    )


def skill_directories() -> list[Path]:
    return sorted(path.parent for path in ROOT.glob("*/*/SKILL.md"))


def parse_frontmatter(path: Path) -> tuple[dict[str, str], list[str]]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        return {}, ["frontmatter must start on the first line"]
    try:
        end = lines.index("---", 1)
    except ValueError:
        return {}, ["frontmatter closing delimiter is missing"]
    values: dict[str, str] = {}
    for line in lines[1:end]:
        if not line.strip():
            continue
        match = re.fullmatch(r"([a-z_]+):\s*(.+)", line)
        if not match:
            errors.append(f"unsupported frontmatter line: {line}")
            continue
        key, value = match.groups()
        values[key] = value.strip().strip('"').strip("'")
    unexpected = sorted(set(values) - {"name", "description"})
    if unexpected:
        errors.append(f"unsupported frontmatter keys: {', '.join(unexpected)}")
    for required in ("name", "description"):
        if not values.get(required):
            errors.append(f"missing {required} frontmatter")
    return values, errors


def validate_skill(directory: Path) -> list[str]:
    relative = directory.relative_to(ROOT)
    errors: list[str] = []
    required = ("README.md", "SKILL.md", "agents/openai.yaml")
    for name in required:
        if not (directory / name).is_file():
            errors.append(f"{relative}: missing {name}")

    skill_file = directory / "SKILL.md"
    if skill_file.is_file():
        frontmatter, frontmatter_errors = parse_frontmatter(skill_file)
        errors.extend(f"{relative}/SKILL.md: {error}" for error in frontmatter_errors)
        if frontmatter.get("name") and frontmatter["name"] != directory.name:
            errors.append(
                f"{relative}/SKILL.md: name '{frontmatter['name']}' does not match directory"
            )

    readme = directory / "README.md"
    if readme.is_file():
        text = readme.read_text(encoding="utf-8")
        if "## Installation" not in text and "## Install for " not in text:
            errors.append(f"{relative}/README.md: missing installation guidance")
        for heading in REQUIRED_README_HEADINGS:
            if heading not in text:
                errors.append(f"{relative}/README.md: missing heading '{heading}'")
        for required_text in (
            "codex plugin marketplace add vladicaster/agent-skills",
            "codex plugin marketplace upgrade vladicaster-tools",
            "claude plugin marketplace add vladicaster/agent-skills",
            "/plugin marketplace update vladicaster-tools",
        ):
            if required_text not in text:
                errors.append(
                    f"{relative}/README.md: missing explicit plugin instruction "
                    f"'{required_text}'"
                )

    root_readme = (ROOT / "README.md").read_text(encoding="utf-8")
    category_readme_path = directory.parent / "README.md"
    if f"({relative.as_posix()}/)" not in root_readme:
        errors.append(f"README.md: missing catalog link to {relative}/")
    if not category_readme_path.is_file():
        errors.append(f"{relative.parent}: missing category README.md")
    elif f"({directory.name}/)" not in category_readme_path.read_text(encoding="utf-8"):
        errors.append(f"{relative.parent}/README.md: missing catalog link to {directory.name}/")
    return errors


def validate_python() -> list[str]:
    errors: list[str] = []
    for path in sorted(ROOT.rglob("*.py")):
        if set(path.relative_to(ROOT).parts) & IGNORED_PARTS:
            continue
        try:
            ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        except (SyntaxError, UnicodeError) as exc:
            errors.append(f"{path.relative_to(ROOT)}: Python parse failed: {exc}")
    return errors


def validate_plugin_surfaces() -> list[str]:
    errors: list[str] = []
    required_files = (
        ".agents/plugins/marketplace.json",
        ".claude-plugin/marketplace.json",
        "release/version.json",
        PLUGIN_GUIDE,
    )
    for relative in required_files:
        if not (ROOT / relative).is_file():
            errors.append(f"missing {relative}")

    for relative in ("README.md", "engineering/README.md", "product/README.md"):
        path = ROOT / relative
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for required_text in (
            "codex plugin marketplace add vladicaster/agent-skills",
            "codex plugin marketplace upgrade vladicaster-tools",
            "claude plugin marketplace add vladicaster/agent-skills",
            "/plugin marketplace update vladicaster-tools",
        ):
            if required_text not in text:
                errors.append(f"{relative}: missing explicit plugin instruction '{required_text}'")
    return errors


def main() -> int:
    errors: list[str] = []
    skills = skill_directories()
    if not skills:
        errors.append("no skill directories found")
    for directory in skills:
        errors.extend(validate_skill(directory))

    for path in markdown_files():
        if "\\n" in path.read_text(encoding="utf-8"):
            errors.append(f"{path.relative_to(ROOT)}: contains visible escaped newline text")

    errors.extend(validate_python())
    errors.extend(validate_plugin_surfaces())
    if errors:
        print(f"FAILED: {len(errors)} repository validation error(s)")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"PASSED: validated {len(skills)} skills and {len(markdown_files())} Markdown files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
