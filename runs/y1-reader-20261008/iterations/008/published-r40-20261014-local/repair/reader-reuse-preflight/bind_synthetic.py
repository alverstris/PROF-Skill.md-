"""Build only the local synthetic fixture and pinned launcher. No real inputs."""
import hashlib
import json
import shutil
import struct
import sys
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def png():
    # Distinct colored quadrants identify completeness and orientation visually.
    width, height = 160, 120
    rows = []
    for y in range(height):
        row = bytearray([0])
        for x in range(width):
            color = ((230, 55, 70) if x < width // 2 else (30, 160, 90)) if y < height // 2 else ((35, 90, 220) if x < width // 2 else (245, 200, 35))
            row.extend(color)
        rows.append(bytes(row))
    def chunk(kind, data):
        return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", zlib.crc32(kind + data) & 0xFFFFFFFF)
    return b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0)) + chunk(b"IDAT", zlib.compress(b"".join(rows))) + chunk(b"IEND", b"")


def build():
    fixture = ROOT / "synthetic-fixtures"
    fixture.mkdir(exist_ok=True)
    bparts = [b"Baseline fixture block one: amber token.\n", b"Baseline fixture block two: violet token.\n"]
    tparts = [b"Teaching fixture opening: plain sample text.\n", b"Teaching fixture ending: final sample text.\n"]
    blobs = {"BFILE": b"".join(bparts), "TFILE": b"".join(tparts), "FIMAGE": png()}
    filenames = {"BFILE": "baseline-fixture.txt", "TFILE": "teaching-fixture.txt", "FIMAGE": "four-quadrants.png"}
    kinds = {"BFILE": "baseline", "TFILE": "teaching_text", "FIMAGE": "teaching_figure"}
    files = {}
    for file_id, data in blobs.items():
        path = fixture / filenames[file_id]
        path.write_bytes(data)
        files[file_id] = {"artifact_id": "synthetic-" + file_id, "revision": "fixture-r1", "kind": kinds[file_id],
                          "path": str(path), "size": len(data), "sha256": hashlib.sha256(data).hexdigest(),
                          "encoding": "binary-image" if file_id == "FIMAGE" else "utf-8"}
    def step(step_id, file_id, start, data):
        return {"id": step_id, "file_id": file_id, "start": start, "length": len(data), "sha256": hashlib.sha256(data).hexdigest(),
                "kind": "figure" if file_id == "FIMAGE" else "text"}
    config = {"schema": "sasis-fixed-route-v1", "route_id": "SYNTHETIC_R39", "revision": "non-subject-r1",
              "range_convention": "zero-based-byte-start-length", "files": files,
              "steps": [step("B001", "BFILE", 0, bparts[0]), step("B002", "BFILE", len(bparts[0]), bparts[1]),
                        step("T001", "TFILE", 0, tparts[0]), step("F001", "FIMAGE", 0, blobs["FIMAGE"]),
                        step("T002", "TFILE", len(tparts[0]), tparts[1])],
              "baseline_revisits": {"RB001": "B001", "RB002": "B002"}}
    route_path = ROOT / "synthetic-route.json"
    raw = (json.dumps(config, indent=2, ensure_ascii=False) + "\n").encode("utf-8")
    route_path.write_bytes(raw)
    route_hash = hashlib.sha256(raw).hexdigest()
    source = (ROOT / "launcher_template.py").read_text(encoding="utf-8")
    source = source.replace("__FIXED_CONFIG_PATH__", str(route_path).replace("\\", "/"))
    source = source.replace("__FIXED_CONFIG_SHA256__", route_hash)
    source = source.replace("__FIXED_RUNTIME_DIR__", str(ROOT / "synthetic-runtime").replace("\\", "/"))
    (ROOT / "fixed_launcher.py").write_text(source, encoding="utf-8", newline="\n")
    shutil.copyfile(ROOT / "receipt_template.py", ROOT / "record_receipt.py")
    adapter = (ROOT / "adapter_template.js").read_text(encoding="utf-8")
    for marker, value in {"__FIXED_PYTHON__": sys.executable, "__FIXED_LAUNCHER__": str(ROOT / "fixed_launcher.py"),
                          "__FIXED_RECEIPT__": str(ROOT / "record_receipt.py"), "__FIXED_CONFIG_SHA256__": route_hash}.items():
        adapter = adapter.replace(marker, value.replace("\\", "/"))
    (ROOT / "fixed_adapter.js").write_text(adapter, encoding="utf-8", newline="\n")
    (ROOT / "binding.json").write_text(json.dumps({"route_path": str(route_path), "route_sha256": route_hash,
                                                   "launcher_path": str(ROOT / "fixed_launcher.py"), "condition": "non-subject synthetic only"}, indent=2), encoding="utf-8")
    return config


if __name__ == "__main__":
    build()
    print("Synthetic fixture and fixed route-bound launcher written.")
