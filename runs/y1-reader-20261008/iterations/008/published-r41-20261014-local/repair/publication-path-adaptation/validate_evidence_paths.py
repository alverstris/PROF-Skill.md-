"""Reusable bounded path-shape checks for GitHub evidence tree entries.

Checks known rejected Git metadata components and unambiguous portable relative
paths. This is local validation, not a guarantee of every GitHub API condition.
"""
import json
import sys


def validate_path(path):
    if type(path) is not str or not path:
        raise ValueError("Nonempty string path required")
    if path.startswith("/") or path.endswith("/") or "\\" in path:
        raise ValueError("Canonical repository-relative slash path required")
    if any(ord(c) < 32 or ord(c) == 127 for c in path):
        raise ValueError("Control character in path")
    parts = path.split("/")
    if any(p in ("", ".", "..") for p in parts):
        raise ValueError("Empty/dot/traversal path component")
    if any(p.casefold() == ".git" for p in parts):
        raise ValueError("Git metadata path component is not publishable evidence")
    path.encode("utf-8", errors="strict")
    return parts


def validate_target_set(paths):
    if len(set(paths)) != len(paths):
        raise ValueError("Duplicate target path")
    folded = {}
    files = set(paths)
    for path in paths:
        parts = validate_path(path)
        folded_path = path.casefold()
        if folded_path in folded:
            raise ValueError("Case-folded target collision: " + path)
        folded[folded_path] = path
        for i in range(1, len(parts)):
            if "/".join(parts[:i]) in files:
                raise ValueError("File/ancestor target collision: " + path)
    return {"paths_checked": len(paths), "exact_duplicates": 0, "case_folded_collisions": 0, "file_ancestor_collisions": 0, "invalid_components": 0}


def main():
    if len(sys.argv) != 2:
        raise ValueError("Exactly one metadata index argument required")
    with open(sys.argv[1], "rb") as handle:
        record = json.load(handle)
    entries = record["items"] if isinstance(record, dict) else record
    print(json.dumps({"passed": True, **validate_target_set([e["path"] if isinstance(e, dict) else e for e in entries])}))


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(json.dumps({"passed": False, "error": str(exc)}), file=sys.stderr)
        raise SystemExit(2)
