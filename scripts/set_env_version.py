#!/usr/bin/env python3
"""Update the environment version file with a new agent tag."""

from __future__ import annotations

import json
import pathlib
import sys


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: set_env_version.py <environment> <version>")
        return 1

    environment = sys.argv[1]
    version = sys.argv[2]

    path = pathlib.Path("environments") / f"{environment}.json"
    if not path.exists():
        print(f"Environment file not found: {path}")
        return 1

    data = json.loads(path.read_text())
    data["agentTag"] = version
    path.write_text(json.dumps(data, indent=2) + "\n")

    print(f"Updated {path} to {version}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
