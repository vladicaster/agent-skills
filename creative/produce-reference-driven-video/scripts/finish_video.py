#!/usr/bin/env python3
"""Build or execute an FFmpeg command for exact captions and an end card."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import shlex
import subprocess


@dataclass(frozen=True)
class Caption:
    start: float
    end: float
    text: str


def escape_drawtext(value: str) -> str:
    """Escape user text for FFmpeg's drawtext option value."""
    return (
        value.replace("\\", r"\\")
        .replace("'", r"\'")
        .replace(":", r"\:")
        .replace("%", r"\%")
        .replace("\n", r"\n")
    )


def parse_caption(value: str) -> Caption:
    try:
        start_text, end_text, text = value.split(",", 2)
        caption = Caption(float(start_text), float(end_text), text)
    except (ValueError, TypeError) as exc:
        raise argparse.ArgumentTypeError("caption must be START,END,TEXT") from exc
    if caption.start < 0 or caption.end <= caption.start or not caption.text.strip():
        raise argparse.ArgumentTypeError("caption requires 0 <= START < END and non-empty TEXT")
    return caption


def drawtext(text: str, enable: str, y: str, size: int) -> str:
    escaped = escape_drawtext(text)
    return (
        f"drawtext=text='{escaped}':fontsize={size}:fontcolor=white:"
        "borderw=4:bordercolor=black@0.8:x=(w-text_w)/2:"
        f"y={y}:enable='{enable}'"
    )


def build_command(
    input_path: Path,
    output_path: Path,
    captions: list[Caption],
    end_card_text: str | None,
    end_card_start: float | None,
    font_size: int,
) -> list[str]:
    filters = [
        drawtext(
            caption.text,
            f"between(t,{caption.start:g},{caption.end:g})",
            "h-(text_h*2)",
            font_size,
        )
        for caption in captions
    ]
    if end_card_text is not None:
        if end_card_start is None or end_card_start < 0:
            raise ValueError("--end-card-start must be non-negative when --end-card-text is used")
        filters.append(
            "drawbox=x=0:y=0:w=iw:h=ih:color=black@0.68:t=fill:"
            f"enable='gte(t,{end_card_start:g})'"
        )
        filters.append(
            drawtext(
                end_card_text,
                f"gte(t,{end_card_start:g})",
                "(h-text_h)/2",
                max(font_size, 48),
            )
        )
    if not filters:
        raise ValueError("provide at least one --caption or --end-card-text")
    return [
        "ffmpeg", "-hide_banner", "-y", "-i", str(input_path),
        "-vf", ",".join(filters), "-c:v", "libx264", "-crf", "18",
        "-preset", "medium", "-c:a", "copy", "-movflags", "+faststart",
        str(output_path),
    ]


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description=__doc__)
    result.add_argument("input", type=Path)
    result.add_argument("output", type=Path)
    result.add_argument("--caption", action="append", type=parse_caption, default=[])
    result.add_argument("--end-card-text")
    result.add_argument("--end-card-start", type=float)
    result.add_argument("--font-size", type=int, default=42)
    result.add_argument("--dry-run", action="store_true")
    return result


def main() -> int:
    args = parser().parse_args()
    if args.font_size <= 0:
        raise SystemExit("--font-size must be positive")
    command = build_command(
        args.input,
        args.output,
        args.caption,
        args.end_card_text,
        args.end_card_start,
        args.font_size,
    )
    print(shlex.join(command))
    if args.dry_run:
        return 0
    if not args.input.is_file():
        raise SystemExit(f"input file does not exist: {args.input}")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(command, check=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
