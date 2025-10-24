#!/usr/bin/env python3
"""
Zip ship directories to zip files.

Scan the root directory for directories named 'ship' and
create a zip archive for each at the root, named after the
parent directory (e.g., tr1.zip for tr1/ship).

Usage:
    python zip_ship.py [--root DIR] [--pattern NAME]
"""

import argparse
import zipfile
from pathlib import Path


def zip_ship_directory(ship_dir: Path, output_path: Path) -> None:
    """Create a zip archive of all files under ship_dir at output_path."""
    with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for file_path in ship_dir.rglob("*"):
            if file_path.is_file():
                arcname = file_path.relative_to(ship_dir)
                zf.write(file_path, arcname)


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Zip ship directories to zip files named after their parent."
        )
    )
    parser.add_argument(
        "--root",
        "-r",
        default=".",
        help="Root directory to scan (default: current directory)",
    )
    parser.add_argument(
        "--pattern",
        "-p",
        default="ship",
        help="Name of ship directories to zip (default: 'ship')",
    )
    args = parser.parse_args()

    root_dir: Path = Path(args.root).expanduser().resolve()
    pattern: str = args.pattern
    created: list[Path] = []
    for ship_dir in root_dir.rglob(pattern):
        if not ship_dir.is_dir():
            continue
        # Skip nested pattern directories under another pattern directory
        skip = False
        for parent in ship_dir.parents:
            if parent == root_dir:
                break
            if parent.name == pattern:
                skip = True
                break
        if skip:
            continue
        parent_name = ship_dir.parent.name
        zip_name = f"{parent_name}.zip"
        output_path: Path = root_dir / zip_name
        zip_ship_directory(ship_dir, output_path)
        print(f"Created archive: {output_path}")
        created.append(output_path)
    if not created:
        print(f"No directories named '{pattern}' found under {root_dir}.")


if __name__ == "__main__":  # pragma: no cover
    main()
