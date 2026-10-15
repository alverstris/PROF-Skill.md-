"""Apply the root's bounded revision/note review to this unpublished proposal only."""
import difflib
import hashlib
import importlib.util
import json
import shutil
from pathlib import Path

R = Path(__file__).resolve().parent
P = R / "proposed-package"
INSTALLED = Path("C:/Users/alver/.codex/skills/prof")
spec = importlib.util.spec_from_file_location("candidate_builder", R / "build_candidate.py")
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)

for name in ("validation.json", "proposed-file-identities.json", "manifest-validation.json"):
    source = R / name
    target = R / (source.stem + "-before-root-metadata-review.json")
    if source.exists() and not target.exists():
        shutil.copyfile(source, target)

carrier = P / "references/sasis.md"
text = carrier.read_text(encoding="utf-8")
assert text.count("Protocol revision: 2026-10-14-r40.") == 1
text = text.replace("Protocol revision: 2026-10-14-r40.", "Protocol revision: 2026-10-14-r41.", 1)
carrier.write_text(text, encoding="utf-8", newline="\n")

manifest = P / "references/sasis/profile-manifest.json"
profile = json.loads(manifest.read_text(encoding="utf-8"))
frozen = dict(profile["file_hashes"])
assert len(frozen) == 19
assert profile["protocol_revision"] == "2026-10-14-r40"
profile["protocol_revision"] = "2026-10-14-r41"
assert builder.R41_NOTE not in profile["protocol_update_notes"]
profile["protocol_update_notes"].append(builder.R41_NOTE)
for relative in profile["control_file_hashes"]:
    local = manifest.parent / relative
    if local.exists():
        profile["control_file_hashes"][relative] = hashlib.sha256(local.read_bytes()).hexdigest()
assert profile["file_hashes"] == frozen
manifest.write_text(json.dumps(profile, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")

diff = []
for file in sorted(p for p in P.rglob("*") if p.is_file()):
    name = file.relative_to(P).as_posix()
    old = (INSTALLED / name).read_text(encoding="utf-8")
    new = file.read_text(encoding="utf-8")
    diff.extend(difflib.unified_diff(old.splitlines(True), new.splitlines(True), fromfile="r40/" + name, tofile="r41/" + name))
(R / "proposed-controls.diff").write_text("".join(diff), encoding="utf-8", newline="\n")
print(json.dumps({"review_applied": True, "protocol_revision": profile["protocol_revision"], "frozen_baseline_provenance_hashes_unchanged": len(frozen), "control_checks": len(profile["control_file_hashes"]), "r41_note": builder.R41_NOTE}, indent=2))
