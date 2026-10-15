"""Read-only bounded JSON transport of independently indexed raw bytes; no publication."""
import base64
import hashlib
import json
import sys
from pathlib import Path

R = Path(__file__).resolve().parent
INDEX = R / "publication-inputs.json"
SECTIONS = {"items", "package", "unique_blobs"}

def require(ok, reason):
    if not ok: raise ValueError(reason)

def raw(entry):
    data = Path(entry["source"]).read_bytes()
    require(len(data) == entry["bytes"] and hashlib.sha256(data).hexdigest() == entry["sha256"], "Source changed since indexed")
    blob = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
    require(blob == entry["git_blob_sha"], "Raw Git blob mismatch")
    return data

def integer(value, lower, upper):
    require(value.isascii() and value.isdigit(), "Nonnegative integer required")
    n = int(value); require(lower <= n <= upper, "Bound exceeded"); return n

def main():
    require(len(sys.argv) >= 2, "Operation required")
    record = json.loads(INDEX.read_bytes())
    op = sys.argv[1]
    if op == "summary":
        require(len(sys.argv) == 2, "summary takes no arguments")
        out = {k: record[k] for k in ("status", "base_commit", "version", "summary", "preserve_all_other_tracked_files", "pending")}
    elif op == "metadata":
        require(len(sys.argv) == 5 and sys.argv[2] in SECTIONS, "metadata SECTION START COUNT")
        section = sys.argv[2]; start = integer(sys.argv[3], 0, len(record[section])); count = integer(sys.argv[4], 1, 10)
        out = {"section": section, "total": len(record[section]), "start": start, "entries": record[section][start:start + count]}
    elif op == "tree-metadata":
        require(len(sys.argv) == 4, "tree-metadata START COUNT")
        start = integer(sys.argv[2], 0, len(record["items"])); count = integer(sys.argv[3], 1, 50)
        out = {"total": len(record["items"]), "start": start, "base_tree": record["base_tree"], "entries": [{"path": e["path"], "mode": "100644", "type": "blob", "sha": e["git_blob_sha"]} for e in record["items"][start:start + count]]}
    elif op == "blob-metadata":
        require(len(sys.argv) == 4, "blob-metadata START COUNT")
        start = integer(sys.argv[2], 0, len(record["unique_blobs"])); count = integer(sys.argv[3], 1, 50)
        keys = ("bytes", "sha256", "git_blob_sha", "encoding", "text_chars", "encoded_chars", "utf16_length")
        out = {"total": len(record["unique_blobs"]), "start": start, "entries": [{"index": i, **{k: e[k] for k in keys}} for i, e in enumerate(record["unique_blobs"][start:start + count], start)]}
    elif op in {"chunk", "base64-chunk"}:
        require(len(sys.argv) == 6 and sys.argv[2] in SECTIONS, "chunk SECTION INDEX START LENGTH")
        section = sys.argv[2]; idx = integer(sys.argv[3], 0, len(record[section]) - 1); entry = record[section][idx]
        data = raw(entry)
        if op == "chunk":
            require(entry["encoding"] == "utf-8", "Text chunk requires exact UTF-8 data")
            text = data.decode("utf-8"); start = integer(sys.argv[4], 0, len(text)); length = integer(sys.argv[5], 1, 18000)
            # JSON escaping preserves BOM/newlines/non-ASCII; no text normalization occurs.
            out = text[start:start + length]
        else:
            start = integer(sys.argv[4], 0, len(data)); length = integer(sys.argv[5], 1, 18432); part = data[start:start + length]
            out = {"encoding": "base64", "byte_start": start, "byte_length": len(part), "total_bytes": len(data), "data": base64.b64encode(part).decode("ascii"), "file_sha256": entry["sha256"], "git_blob_sha": entry["git_blob_sha"]}
    else: raise ValueError("Unknown transport operation")
    print(json.dumps(out, ensure_ascii=True, separators=(",", ":")))

if __name__ == "__main__":
    try: main()
    except Exception as exc:
        print(json.dumps({"ok": False, "error": str(exc)}), file=sys.stderr)
        raise SystemExit(2)
