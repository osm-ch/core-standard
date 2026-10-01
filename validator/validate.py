# SPDX-License-Identifier: CC0-1.0
from __future__ import annotations

import argparse
import json
from pathlib import Path

from core import PROFILE_FILES, resolve_pair, validate


def load(path: str) -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser(description="Offline OSM-CH core validator")
    parser.add_argument("--profile", choices=sorted(PROFILE_FILES))
    parser.add_argument("--validate")
    parser.add_argument("--type")
    parser.add_argument("--instance")
    parser.add_argument("--resolved-out")
    args = parser.parse_args()

    if args.type or args.instance:
        if not (args.type and args.instance):
            parser.error("--type and --instance must be used together")
        resolved = resolve_pair(load(args.type), load(args.instance))
        if args.resolved_out:
            Path(args.resolved_out).write_text(
                json.dumps(resolved, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )
        print("PASS: type + instance resolve to a valid ResolvedProcedure")
        return 0

    if not (args.profile and args.validate):
        parser.error("use --profile PROFILE --validate FILE or --type FILE --instance FILE")

    errors = validate(args.profile, load(args.validate))
    if errors:
        print(json.dumps(errors, ensure_ascii=False, indent=2))
        return 1
    print(f"PASS: {args.validate} validates as {args.profile}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
