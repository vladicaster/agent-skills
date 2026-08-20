#!/usr/bin/env python3
"""Build and verify the cross-platform Vladicaster Agent Skills plugin."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import tempfile


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "plugin" / "vladicaster-agent-skills"
VERSION_FILE = ROOT / "release" / "version.json"
IGNORED_NAMES = {"__pycache__", ".DS_Store"}


def canonical_skills() -> list[Path]:
    skills = sorted(path.parent for path in ROOT.glob("*/*/SKILL.md"))
    if not skills:
        raise RuntimeError("no canonical skills found")
    names = [path.name for path in skills]
    duplicates = sorted({name for name in names if names.count(name) > 1})
    if duplicates:
        raise RuntimeError(f"duplicate canonical skill names: {', '.join(duplicates)}")
    for skill in skills:
        for required in ("README.md", "SKILL.md", "agents/openai.yaml"):
            if not (skill / required).is_file():
                raise RuntimeError(f"{skill.relative_to(ROOT)} is missing {required}")
    return skills


def included(path: Path) -> bool:
    return not any(part in IGNORED_NAMES for part in path.parts)


def content_hash(directory: Path) -> str:
    digest = hashlib.sha256()
    for path in sorted(p for p in directory.rglob("*") if p.is_file() and included(p)):
        if path.relative_to(directory).as_posix() == "release/update.json":
            continue
        relative = path.relative_to(directory)
        digest.update(relative.as_posix().encode("utf-8"))
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return f"sha256:{digest.hexdigest()}"


def parse_version(value: str) -> tuple[int, int, int]:
    parts = value.split(".")
    if len(parts) != 3 or any(not part.isdigit() for part in parts):
        raise RuntimeError(f"invalid semantic version: {value}")
    return tuple(int(part) for part in parts)


def git_commit() -> str:
    return os.environ.get("PLUGIN_SOURCE_COMMIT", "set-by-release-workflow")


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def build(output: Path) -> None:
    version_data = json.loads(VERSION_FILE.read_text(encoding="utf-8"))
    version = version_data["version"]
    current_version = parse_version(version)
    skills = canonical_skills()
    previous_skills: set[str] = set()
    previous_manifest = os.environ.get("PLUGIN_PREVIOUS_MANIFEST")
    if previous_manifest and Path(previous_manifest).is_file():
        previous = json.loads(Path(previous_manifest).read_text(encoding="utf-8"))
        previous_skills = set(previous.get("skills", []))
        previous_version = parse_version(str(previous["version"]))
        if current_version <= previous_version:
            raise RuntimeError(
                f"release version {version} must be newer than {previous['version']}"
            )
    added_skills = sorted(skill.name for skill in skills if skill.name not in previous_skills)
    if previous_skills and added_skills and current_version[:2] <= previous_version[:2]:
        raise RuntimeError(
            "adding a skill requires at least a minor-version increment; added: "
            + ", ".join(added_skills)
        )

    if output.exists():
        shutil.rmtree(output)
    (output / "skills").mkdir(parents=True)

    for skill in skills:
        shutil.copytree(
            skill,
            output / "skills" / skill.name,
            ignore=shutil.ignore_patterns(*IGNORED_NAMES),
        )

    plugin_description = (
        "Portable product and engineering delivery workflows for ChatGPT, "
        "Codex, and Claude Code."
    )
    write_json(
        output / ".codex-plugin" / "plugin.json",
        {
            "name": "vladicaster-agent-skills",
            "version": version,
            "description": plugin_description,
            "author": {
                "name": "Bill Elberg",
                "url": "https://github.com/vladicaster",
            },
            "repository": "https://github.com/vladicaster/agent-skills",
            "skills": "./skills/",
            "interface": {
                "displayName": "Vladicaster Agent Skills",
                "shortDescription": "Product and engineering delivery workflows",
                "developerName": "Bill Elberg",
                "category": "Developer Tools",
            },
        },
    )
    write_json(
        output / ".claude-plugin" / "plugin.json",
        {
            "name": "vladicaster-agent-skills",
            "version": version,
            "description": plugin_description,
            "author": {"name": "Bill Elberg"},
            "repository": "https://github.com/vladicaster/agent-skills",
        },
    )
    source_readme = ROOT / "docs" / "plugin-installation-and-updates.md"
    shutil.copy2(source_readme, output / "README.md")
    digest = content_hash(output)

    write_json(
        output / "release" / "update.json",
        {
            "name": "vladicaster-agent-skills",
            "version": version,
            "contentHash": digest,
            "sourceCommit": git_commit(),
            "releaseTimestamp": os.environ.get(
                "PLUGIN_RELEASE_TIMESTAMP", "set-by-release-workflow"
            ),
            "releaseNotesUrl": (
                "https://github.com/vladicaster/agent-skills/releases/tag/"
                f"v{version}"
            ),
            "latestManifestUrl": (
                "https://github.com/vladicaster/agent-skills/releases/latest/"
                "download/update.json"
            ),
            "skills": [skill.name for skill in skills],
            "addedSkills": added_skills,
            "updateInstructions": {
                "chatgptCodex": (
                    "Run `codex plugin marketplace upgrade vladicaster-tools`, "
                    "then refresh ChatGPT or start a new Codex session."
                ),
                "claudeCode": (
                    "Enable marketplace auto-update or run `/plugin marketplace "
                    "update vladicaster-tools`, then run `/reload-plugins` or start "
                    "a new session."
                ),
            },
        },
    )

def tree_snapshot(path: Path) -> dict[str, bytes]:
    return {
        item.relative_to(path).as_posix(): item.read_bytes()
        for item in sorted(path.rglob("*"))
        if item.is_file() and included(item)
    }


def check() -> None:
    with tempfile.TemporaryDirectory(prefix="agent-skills-plugin-") as temp:
        expected = Path(temp) / "vladicaster-agent-skills"
        build(expected)
        actual_files = tree_snapshot(DEFAULT_OUTPUT)
        expected_files = tree_snapshot(expected)
        if actual_files != expected_files:
            missing = sorted(set(expected_files) - set(actual_files))
            extra = sorted(set(actual_files) - set(expected_files))
            changed = sorted(
                path
                for path in set(actual_files) & set(expected_files)
                if actual_files[path] != expected_files[path]
            )
            details = []
            if missing:
                details.append(f"missing: {', '.join(missing)}")
            if extra:
                details.append(f"extra: {', '.join(extra)}")
            if changed:
                details.append(f"changed: {', '.join(changed)}")
            raise RuntimeError(
                "committed plugin bundle is stale; run "
                "`python scripts/build_plugin.py --sync` (" + "; ".join(details) + ")"
            )

    version = json.loads(VERSION_FILE.read_text(encoding="utf-8"))["version"]
    claude_marketplace = json.loads(
        (ROOT / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8")
    )
    listed_version = claude_marketplace["plugins"][0]["version"]
    if listed_version != version:
        raise RuntimeError(
            f"Claude marketplace version {listed_version} does not match {version}"
        )


def sync_marketplace_version() -> None:
    version = json.loads(VERSION_FILE.read_text(encoding="utf-8"))["version"]
    path = ROOT / ".claude-plugin" / "marketplace.json"
    marketplace = json.loads(path.read_text(encoding="utf-8"))
    marketplace["plugins"][0]["version"] = version
    write_json(path, marketplace)


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--sync", action="store_true", help="rebuild the committed bundle")
    mode.add_argument("--check", action="store_true", help="verify the committed bundle")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    try:
        if args.check:
            check()
            print("PASSED: committed plugin bundle matches canonical skills")
        else:
            build(args.output)
            if args.output.resolve() == DEFAULT_OUTPUT.resolve():
                sync_marketplace_version()
            print(f"BUILT: {args.output}")
    except (OSError, RuntimeError, KeyError, json.JSONDecodeError) as exc:
        print(f"FAILED: {exc}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
