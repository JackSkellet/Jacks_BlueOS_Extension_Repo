#!/usr/bin/env python3
"""Validate the small static part of a BlueOS extension catalog."""

from __future__ import annotations

import json
import sys
from pathlib import Path

REQUIRED_FIELDS = {"name", "website", "docker", "description"}


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else "repos")
    errors: list[str] = []

    for metadata_path in sorted(root.glob("*/*/metadata.json")):
        try:
            metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as error:
            errors.append(f"{metadata_path}: invalid JSON: {error}")
            continue

        missing = sorted(REQUIRED_FIELDS - metadata.keys())
        if missing:
            errors.append(f"{metadata_path}: missing fields: {', '.join(missing)}")

        docker = metadata.get("docker")
        if not isinstance(docker, str) or docker.count("/") != 1:
            errors.append(f"{metadata_path}: docker must be namespace/repository")

        extension_dir = metadata_path.parent
        company_dir = extension_dir.parent
        if not (extension_dir / "extension_logo.png").is_file():
            errors.append(f"{metadata_path}: extension_logo.png is missing")
        if not (company_dir / "company_logo.png").is_file():
            errors.append(f"{metadata_path}: company_logo.png is missing")

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1

    count = len(list(root.glob("*/*/metadata.json")))
    print(f"Validated {count} extension metadata file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
