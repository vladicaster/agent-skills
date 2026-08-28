#!/usr/bin/env python3
"""Build or execute a source-preserving FFmpeg background-music mix."""

from __future__ import annotations

import argparse
from pathlib import Path
import shlex
import subprocess


def validate_settings(
    video_path: Path,
    music_path: Path,
    output_path: Path,
    duration: float,
    music_gain: float,
    fade_in: float,
    fade_out: float,
    duck_threshold: float,
    duck_ratio: float,
) -> None:
    if output_path in (video_path, music_path):
        raise ValueError("output must differ from the source video and music paths")
    if duration <= 0:
        raise ValueError("--duration must be positive")
    if not 0 <= music_gain <= 4:
        raise ValueError("--music-gain must be between 0 and 4")
    if fade_in < 0 or fade_out < 0 or fade_in > duration or fade_out > duration:
        raise ValueError("fades must be non-negative and no longer than the duration")
    if not 0 < duck_threshold <= 1:
        raise ValueError("--duck-threshold must be greater than 0 and at most 1")
    if not 1 <= duck_ratio <= 20:
        raise ValueError("--duck-ratio must be between 1 and 20")


def build_command(
    video_path: Path,
    music_path: Path,
    output_path: Path,
    duration: float,
    music_gain: float,
    fade_in: float,
    fade_out: float,
    duck_threshold: float,
    duck_ratio: float,
) -> list[str]:
    validate_settings(
        video_path, music_path, output_path, duration, music_gain,
        fade_in, fade_out, duck_threshold, duck_ratio,
    )
    fade_out_start = duration - fade_out
    music_filters = [f"atrim=0:{duration:g}", "asetpts=PTS-STARTPTS"]
    if fade_in:
        music_filters.append(f"afade=t=in:st=0:d={fade_in:g}")
    if fade_out:
        music_filters.append(f"afade=t=out:st={fade_out_start:g}:d={fade_out:g}")
    music_filters.append(f"volume={music_gain:g}")
    graph = (
        f"[1:a]{','.join(music_filters)}[music];"
        f"[music][0:a]sidechaincompress=threshold={duck_threshold:g}:"
        f"ratio={duck_ratio:g}:attack=20:release=450[ducked];"
        "[0:a][ducked]amix=inputs=2:duration=first:dropout_transition=0:"
        "normalize=0,alimiter=limit=0.95[aout]"
    )
    return [
        "ffmpeg", "-hide_banner", "-y", "-i", str(video_path),
        "-i", str(music_path), "-filter_complex", graph,
        "-map", "0:v:0", "-map", "[aout]", "-c:v", "copy",
        "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
        "-movflags", "+faststart", str(output_path),
    ]


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description=__doc__)
    result.add_argument("video", type=Path, help="approved narrated source master")
    result.add_argument("music", type=Path, help="approved duration-matched music cue")
    result.add_argument("output", type=Path, help="new candidate mix path")
    result.add_argument("--duration", required=True, type=float,
                        help="measured source-master duration in seconds")
    result.add_argument("--music-gain", required=True, type=float,
                        help="cue-specific linear gain; not a universal prominence label")
    result.add_argument("--fade-in", type=float, default=1.0)
    result.add_argument("--fade-out", type=float, default=1.5)
    result.add_argument("--duck-threshold", type=float, default=0.012)
    result.add_argument("--duck-ratio", type=float, default=6.0)
    result.add_argument("--dry-run", action="store_true")
    return result


def main() -> int:
    args = parser().parse_args()
    try:
        command = build_command(
            args.video, args.music, args.output, args.duration,
            args.music_gain, args.fade_in, args.fade_out,
            args.duck_threshold, args.duck_ratio,
        )
    except ValueError as exc:
        raise SystemExit(str(exc)) from exc
    print(shlex.join(command))
    if args.dry_run:
        return 0
    if not args.video.is_file():
        raise SystemExit(f"source video does not exist: {args.video}")
    if not args.music.is_file():
        raise SystemExit(f"music cue does not exist: {args.music}")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(command, check=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
