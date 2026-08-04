#!/usr/bin/env python3
"""Download a targeted Mobbin JPEG manifest with validation."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any


USER_AGENT = "Codex-Mobbin-Research/1.0 (targeted internal reference export)"


def is_jpeg(path: Path) -> bool:
    try:
        with path.open("rb") as handle:
            return handle.read(3) == b"\xff\xd8\xff"
    except OSError:
        return False


def safe_destination(root: Path, relative_path: str) -> Path:
    root_path = os.path.abspath(root)
    destination_path = os.path.abspath(root / relative_path)
    root_key = os.path.normcase(root_path)
    destination_key = os.path.normcase(destination_path)
    try:
        inside_root = os.path.commonpath([root_key, destination_key]) == root_key
    except ValueError:
        inside_root = False
    if not inside_root:
        raise ValueError(f"Unsafe relative_path: {relative_path}")
    return Path(destination_path)


def download_asset(
    asset: dict[str, Any], root: Path, timeout: int, retries: int = 3
) -> dict[str, str]:
    relative_path = str(asset["relative_path"])
    destination = safe_destination(root, relative_path)
    destination.parent.mkdir(parents=True, exist_ok=True)

    if is_jpeg(destination):
        return {"path": relative_path, "status": "skipped"}

    part = destination.with_suffix(destination.suffix + ".part")
    request = urllib.request.Request(
        str(asset["image_url"]), headers={"User-Agent": USER_AGENT}
    )

    for attempt in range(retries):
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                with part.open("wb") as output:
                    shutil.copyfileobj(response, output)
            if not is_jpeg(part):
                raise ValueError("response is not a JPEG")
            os.replace(part, destination)
            return {"path": relative_path, "status": "downloaded"}
        except Exception as exc:
            part.unlink(missing_ok=True)
            if attempt + 1 == retries:
                return {
                    "path": relative_path,
                    "status": "failed",
                    "error": str(exc),
                }
            time.sleep(2**attempt)

    raise AssertionError("unreachable")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Download a targeted Mobbin JPEG manifest."
    )
    parser.add_argument("manifest", type=Path)
    parser.add_argument("destination", type=Path)
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--timeout", type=int, default=30)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not 1 <= args.workers <= 32:
        raise SystemExit("--workers must be between 1 and 32")
    if args.limit < 0:
        raise SystemExit("--limit must be zero or greater")
    if args.timeout < 1:
        raise SystemExit("--timeout must be positive")

    manifest = json.loads(args.manifest.read_text(encoding="utf-8-sig"))
    assets = list(manifest.get("assets", []))
    if args.limit:
        assets = assets[: args.limit]
    if not assets:
        raise SystemExit("Manifest has no assets")

    root = Path(os.path.abspath(args.destination))
    root.mkdir(parents=True, exist_ok=True)

    relative_paths = [str(asset["relative_path"]) for asset in assets]
    if len(relative_paths) != len(set(relative_paths)):
        raise SystemExit("Manifest contains duplicate relative_path values")
    for asset in assets:
        if not asset.get("image_url") or not asset.get("relative_path"):
            raise SystemExit("Every asset needs image_url and relative_path")
        safe_destination(root, str(asset["relative_path"]))

    def run(asset: dict[str, Any]) -> dict[str, str]:
        return download_asset(asset, root, args.timeout)

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        results = list(pool.map(run, assets))

    summary = {
        "destination": str(root),
        "requested": len(assets),
        "downloaded": sum(item["status"] == "downloaded" for item in results),
        "skipped": sum(item["status"] == "skipped" for item in results),
        "failed": sum(item["status"] == "failed" for item in results),
        "failures": [item for item in results if item["status"] == "failed"],
    }
    print(json.dumps(summary, indent=2))
    return 1 if summary["failed"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
