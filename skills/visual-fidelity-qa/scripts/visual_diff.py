#!/usr/bin/env python3
"""Create deterministic visual-difference evidence for two same-size images.

Requires Pillow. This tool intentionally does not assign a universal pass/fail
grade; visual metrics must be interpreted with semantic and functional QA.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

try:
    from PIL import Image, ImageChops, ImageEnhance, ImageStat
except ImportError:
    print(
        "Pillow is required. Install it in an isolated environment with "
        "`python -m pip install Pillow`.",
        file=sys.stderr,
    )
    raise SystemExit(2)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Compare a reference image with an actual capture."
    )
    parser.add_argument("reference", type=Path)
    parser.add_argument("actual", type=Path)
    parser.add_argument("--out-dir", type=Path, default=Path("visual-diff-output"))
    parser.add_argument(
        "--threshold",
        type=int,
        default=24,
        help="Per-channel absolute difference threshold from 0 to 255 (default: 24).",
    )
    parser.add_argument(
        "--resize-actual",
        action="store_true",
        help="Resize actual to reference dimensions. The report records this normalization.",
    )
    return parser.parse_args()


def validate(args: argparse.Namespace) -> None:
    if not 0 <= args.threshold <= 255:
        raise ValueError("--threshold must be between 0 and 255")
    if not args.reference.is_file():
        raise FileNotFoundError(f"Reference image not found: {args.reference}")
    if not args.actual.is_file():
        raise FileNotFoundError(f"Actual image not found: {args.actual}")


def main() -> int:
    args = parse_args()
    try:
        validate(args)
    except (ValueError, FileNotFoundError) as exc:
        print(str(exc), file=sys.stderr)
        return 2

    reference = Image.open(args.reference).convert("RGBA")
    actual = Image.open(args.actual).convert("RGBA")
    original_actual_size = actual.size
    resized = False

    if reference.size != actual.size:
        if not args.resize_actual:
            print(
                "Image dimensions differ: "
                f"reference={reference.size}, actual={actual.size}. "
                "Capture at matching dimensions or pass --resize-actual and disclose normalization.",
                file=sys.stderr,
            )
            return 3
        actual = actual.resize(reference.size, Image.Resampling.LANCZOS)
        resized = True

    args.out_dir.mkdir(parents=True, exist_ok=True)

    reference_rgb = reference.convert("RGB")
    actual_rgb = actual.convert("RGB")
    diff = ImageChops.difference(reference_rgb, actual_rgb)
    stat = ImageStat.Stat(diff)

    mean_by_channel = [float(value) for value in stat.mean]
    rms_by_channel = [float(value) for value in stat.rms]
    mae_percent = sum(mean_by_channel) / (3 * 255) * 100
    rmse_percent = math.sqrt(sum(value * value for value in rms_by_channel) / 3) / 255 * 100

    if hasattr(diff, "get_flattened_data"):
        pixels = list(diff.get_flattened_data())
    else:
        pixels = list(diff.getdata())
    changed_pixels = sum(
        1 for red, green, blue in pixels if max(red, green, blue) > args.threshold
    )
    changed_percent = changed_pixels / max(1, len(pixels)) * 100

    overlay = Image.blend(reference, actual, 0.5)
    heatmap = ImageEnhance.Contrast(diff).enhance(2.5)

    overlay_path = args.out_dir / "overlay-50.png"
    heatmap_path = args.out_dir / "difference-heatmap.png"
    normalized_actual_path = args.out_dir / "actual-normalized.png"
    metrics_path = args.out_dir / "metrics.json"

    overlay.save(overlay_path)
    heatmap.save(heatmap_path)
    if resized:
        actual.save(normalized_actual_path)

    report = {
        "schema_version": 1,
        "reference": str(args.reference.resolve()),
        "actual": str(args.actual.resolve()),
        "reference_size": list(reference.size),
        "actual_original_size": list(original_actual_size),
        "actual_resized": resized,
        "threshold_0_to_255": args.threshold,
        "mean_absolute_error_by_channel_0_to_255": mean_by_channel,
        "root_mean_square_error_by_channel_0_to_255": rms_by_channel,
        "mean_absolute_rgb_error_percent": round(mae_percent, 6),
        "root_mean_square_rgb_error_percent": round(rmse_percent, 6),
        "pixels_above_threshold_percent": round(changed_percent, 6),
        "exact_match": diff.getbbox() is None,
        "evidence": {
            "overlay_50": str(overlay_path.resolve()),
            "difference_heatmap": str(heatmap_path.resolve()),
            "actual_normalized": str(normalized_actual_path.resolve()) if resized else None,
        },
        "interpretation_warning": (
            "Metrics are sensitive to font rasterization, antialiasing, compression, "
            "capture state, and color profiles. They do not test semantics or behavior."
        ),
    }

    metrics_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
