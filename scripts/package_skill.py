#!/usr/bin/env python3
"""Create a portable ZIP containing the canonical Artifact 3026 skill."""

from __future__ import annotations

import argparse
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / ".agents" / "skills" / "artifact-3026"


def build(output: Path) -> Path:
    output = output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(SOURCE.rglob("*")):
            if path.is_file():
                archive.write(path, Path(SOURCE.name) / path.relative_to(SOURCE))
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description="Package Artifact 3026 as a portable skill ZIP.")
    parser.add_argument("--output", type=Path, default=ROOT / "dist" / "artifact-3026.zip")
    args = parser.parse_args()
    print(build(args.output))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
