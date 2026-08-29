#!/usr/bin/env python3
"""Fail when an implementation changed protected visual references or baselines."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

DEFAULT_PREFIXES = (
    "design/baselines/",
    "design/references/approved/",
)
PATH_KEYS = {
    "baseline",
    "baseline_path",
    "file",
    "golden",
    "image",
    "path",
    "reference",
    "snapshot",
}


def run_git(root: Path, *arguments: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(root), *arguments],
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or "Git command failed")
    return result.stdout


def collect_manifest_paths(value: Any, key: str = "") -> set[str]:
    paths: set[str] = set()
    if isinstance(value, dict):
        for child_key, child_value in value.items():
            paths.update(collect_manifest_paths(child_value, str(child_key).lower()))
    elif isinstance(value, list):
        for child in value:
            paths.update(collect_manifest_paths(child, key))
    elif isinstance(value, str) and (key in PATH_KEYS or key.endswith(("_path", "_file"))):
        candidate = value.replace("\\", "/").lstrip("./")
        if candidate and "://" not in candidate:
            paths.add(candidate.rstrip("/"))
    return paths


def changed_paths(root: Path, base_ref: str) -> set[str]:
    tracked = run_git(root, "diff", "--name-only", "--diff-filter=ACDMRTUXB", base_ref, "--")
    untracked = run_git(root, "ls-files", "--others", "--exclude-standard")
    return {line.strip().replace("\\", "/") for line in (tracked + untracked).splitlines() if line.strip()}


def is_protected(path: str, protected_files: set[str], prefixes: set[str]) -> bool:
    normalized = path.lstrip("./")
    if normalized in protected_files:
        return True
    return any(normalized == prefix.rstrip("/") or normalized.startswith(prefix.rstrip("/") + "/") for prefix in prefixes)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-ref", required=True, help="Accepted Git commit or ref")
    parser.add_argument("--manifest", type=Path, help="Optional baseline manifest")
    parser.add_argument("--protected", action="append", default=[], help="Additional protected file or directory prefix")
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="Repository root")
    args = parser.parse_args()

    root = args.root.resolve()
    try:
        run_git(root, "rev-parse", "--verify", f"{args.base_ref}^{{commit}}")
    except RuntimeError as error:
        print(f"ERROR: cannot resolve accepted base ref: {error}", file=sys.stderr)
        return 2

    protected_files: set[str] = set()
    if args.manifest:
        manifest_path = (args.manifest if args.manifest.is_absolute() else root / args.manifest).resolve()
        try:
            manifest_relative = manifest_path.relative_to(root).as_posix()
        except ValueError:
            print("ERROR: baseline manifest must stay inside the repository", file=sys.stderr)
            return 2
        if not manifest_path.is_file():
            print(f"ERROR: baseline manifest not found: {manifest_path}", file=sys.stderr)
            return 2
        try:
            protected_files = collect_manifest_paths(json.loads(manifest_path.read_text(encoding="utf-8")))
            protected_files.add(manifest_relative)
        except (OSError, json.JSONDecodeError) as error:
            print(f"ERROR: cannot read baseline manifest: {error}", file=sys.stderr)
            return 2

    prefixes = {prefix.replace("\\", "/").lstrip("./") for prefix in DEFAULT_PREFIXES + tuple(args.protected)}
    try:
        changed = changed_paths(root, args.base_ref)
    except RuntimeError as error:
        print(f"ERROR: cannot inspect Git changes: {error}", file=sys.stderr)
        return 2

    violations = sorted(path for path in changed if is_protected(path, protected_files, prefixes))
    result = {
        "base_ref": args.base_ref,
        "baseline_changed": bool(violations),
        "protected_changes": violations,
        "changed_path_count": len(changed),
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 1 if violations else 0


if __name__ == "__main__":
    raise SystemExit(main())
