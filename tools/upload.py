#!/usr/bin/env python3
import os
from pathlib import Path
from subprocess import run

REMOTE_HOST = "lostartefacts"
REMOTE_BASE = "srv/website/aux"


def upload(source: Path, target: str) -> None:
    """
    Upload a file to the remote lostartefacts server under /srv/aux/{target}.
    """
    if not source.exists():
        raise FileNotFoundError(source)
    remote_path = f"{REMOTE_BASE}/{target}"
    remote_dir = os.path.dirname(remote_path)

    print(f"Creating remote directory: lostartefacts:{remote_dir}")
    run(["ssh", REMOTE_HOST, "mkdir", "-p", remote_dir], check=True)

    print(f"Uploading {source} to lostartefacts:{remote_path}")
    run(["scp", str(source), f"lostartefacts:{remote_path}"], check=True)


def main() -> None:
    src_dir = Path(__file__).parent.parent.resolve()
    upload(src_dir / "tr1.zip", "tr1x/main.zip")
    upload(src_dir / "tr2.zip", "tr2x/main.zip")
    upload(src_dir / "tr2gm.zip", "tr2x/trgm.zip")


if __name__ == "__main__":
    main()
