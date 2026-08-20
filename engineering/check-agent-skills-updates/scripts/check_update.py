#!/usr/bin/env python3
"""Compare an installed plugin version with the latest release manifest."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys
from urllib.error import HTTPError, URLError
from urllib.request import urlopen


DEFAULT_MANIFEST = (
    "https://github.com/vladicaster/agent-skills/releases/latest/download/update.json"
)


def parse_version(value: str) -> tuple[int, int, int]:
    match = re.fullmatch(r"v?(\d+)\.(\d+)\.(\d+)", value)
    if not match:
        raise ValueError(f"unsupported semantic version: {value}")
    return tuple(int(part) for part in match.groups())


def discover_installed_version(start: Path) -> str | None:
    for directory in (start, *start.parents):
        for relative in (
            Path(".codex-plugin/plugin.json"),
            Path(".claude-plugin/plugin.json"),
        ):
            manifest = directory / relative
            if manifest.is_file():
                return json.loads(manifest.read_text(encoding="utf-8"))["version"]
    return None


def fetch_json(url: str) -> dict[str, object]:
    with urlopen(url, timeout=10) as response:
        return json.loads(response.read().decode("utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--platform",
        choices=("chatgpt-codex", "claude-code"),
        required=True,
    )
    parser.add_argument("--installed-version")
    parser.add_argument("--manifest-url", default=DEFAULT_MANIFEST)
    args = parser.parse_args()

    installed = args.installed_version or discover_installed_version(Path(__file__).resolve())
    if not installed:
        print(json.dumps({"status": "unknown", "reason": "installed version unavailable"}))
        return 2

    try:
        latest = fetch_json(args.manifest_url)
        available = str(latest["version"])
        update_available = parse_version(available) > parse_version(installed)
        instruction_key = (
            "chatgptCodex" if args.platform == "chatgpt-codex" else "claudeCode"
        )
        result = {
            "status": "update-available" if update_available else "current",
            "installedVersion": installed,
            "availableVersion": available,
            "addedSkills": latest.get("addedSkills", []),
            "releaseNotesUrl": latest.get("releaseNotesUrl"),
            "updateInstruction": latest.get("updateInstructions", {}).get(instruction_key),
        }
        print(json.dumps(result, indent=2))
        return 0
    except (HTTPError, URLError, TimeoutError, ValueError, KeyError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "unavailable", "reason": str(exc)}))
        return 2


if __name__ == "__main__":
    sys.exit(main())
