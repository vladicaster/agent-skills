#!/usr/bin/env python3
"""Create deterministic release notes from a built update manifest."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    added = manifest.get("addedSkills", [])
    lines = [
        f"# Vladicaster Agent Skills {manifest['version']}",
        "",
        "## Added skills",
        "",
    ]
    lines.extend(f"- `{name}`" for name in added)
    if not added:
        lines.append("- No newly bundled skills in this release.")
    lines.extend(
        [
            "",
            "## Package",
            "",
            f"- Content hash: `{manifest['contentHash']}`",
            f"- Source commit: `{manifest['sourceCommit']}`",
            "- Includes both OpenAI and Claude plugin manifests.",
            "",
            "See the repository README for host-specific update and reload instructions.",
        ]
    )
    args.output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
