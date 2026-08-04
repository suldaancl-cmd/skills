#!/usr/bin/env python3
"""Small self-check for download_manifest.py."""

import importlib.util
from pathlib import Path
from tempfile import TemporaryDirectory


SCRIPT = Path(__file__).with_name("download_manifest.py")
SPEC = importlib.util.spec_from_file_location("download_manifest", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


with TemporaryDirectory() as directory:
    root = Path(directory)
    image = MODULE.safe_destination(root, "ios/screen.jpg")
    image.parent.mkdir(parents=True)
    image.write_bytes(b"\xff\xd8\xfftest")
    assert MODULE.is_jpeg(image)

    try:
        MODULE.safe_destination(root, "../escape.jpg")
    except ValueError:
        pass
    else:
        raise AssertionError("path traversal was not rejected")

print("download_manifest self-check passed")

