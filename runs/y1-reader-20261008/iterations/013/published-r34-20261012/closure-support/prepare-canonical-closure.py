#!/usr/bin/env python3
"""Prepare local canonical closure only. No network, Git, publication or report edits.

Usage:
  python3 author/prepare-canonical-closure.py RELEASE_COMMIT RELEASE_TREE /absolute/release-readback.json

Writes a NEW canonical-after/RELEASE_COMMIT/ directory, only after the complete
actual release readback passes. Never overwrites canonical-before or any input.
The publisher must publish the copied release-readback.json at
runs/y1-reader-20261008/iterations/013/published-r34-20261012/closure-support/release-readback.json
and closure-invariants.json in that same closure-support directory, alongside the
three canonical files. This script does not assert that closure B is published.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import re

W = Path(__file__).resolve().parents[1]
RUN = "runs/y1-reader-20261008/"
REL = "iterations/013/published-r34-20261012/"
PREFIX = RUN + REL
INCOMING = "75d41178bb87e473d907e852f85f7047e0530a86"
TEACHING = "ce407f3f2a5276700e61f43d7d1c371b9f452121"
MAIN_SHA = "6262d74b9e4d146863de712473957c17d7c4ca31f52c924066407a9ed913811a"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def blob(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def json_bytes(value):
    return (json.dumps(value, indent=2, ensure_ascii=False) + "\n").encode("utf-8")


def load(path):
    def unique(pairs):
        answer = {}
        for key, value in pairs:
            require(key not in answer, "duplicate JSON key: " + key)
            answer[key] = value
        return answer
    return json.loads(path.read_bytes(), object_pairs_hook=unique)


def row_map(rows):
    require(type(rows) is list, "expected manifest rows")
    answer = {}
    for row in rows:
        require(type(row) is dict and type(row.get("path")) is str, "invalid manifest row")
        require(row["path"] not in answer, "duplicate path " + row["path"])
        require(type(row.get("bytes")) is int and row["bytes"] >= 0, "invalid file length")
        require(re.fullmatch(r"[0-9a-f]{64}", row.get("sha256", "")) is not None, "invalid SHA-256")
        require(re.fullmatch(r"[0-9a-f]{40}", row.get("git_blob", "")) is not None, "invalid Git blob")
        answer[row["path"]] = row
    return answer


def matching(actual, expected, path):
    require(path in actual, "readback missing " + path)
    for key in ("bytes", "sha256", "git_blob"):
        require(actual[path][key] == expected[key], "readback mismatch: " + path + ":" + key)


def append_unique(target, values):
    require(type(target) is list, "expected existing evidence array")
    for value in values:
        if value not in target:
            target.append(value)


def preserved_arrays(before, after, path="$", found=None):
    if found is None:
        found = []
    if type(before) is dict:
        require(type(after) is dict, "changed container at " + path)
        for key, value in before.items():
            require(key in after, "removed original field " + path + "." + key)
            # Operative objects replaced at closure are preserved verbatim in the
            # appended D013 history; their existing arrays are handled separately.
            if path == "$.sessions[12]" and key in ("current_iteration", "current_review_status"):
                continue
            preserved_arrays(value, after[key], path + "." + key, found)
    elif type(before) is list:
        require(type(after) is list and len(after) >= len(before), "array shortened at " + path)
        if path == "$.sessions":
            for index, row in enumerate(before):
                preserved_arrays(row, after[index], path + "[" + str(index) + "]", found)
        else:
            require(after[:len(before)] == before, "prior array prefix changed at " + path)
            found.append(path)
    return found


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("release_commit")
    parser.add_argument("release_tree")
    parser.add_argument("release_readback", type=Path)
    args = parser.parse_args()
    for name in ("release_commit", "release_tree"):
        require(re.fullmatch(r"[0-9a-f]{40}", getattr(args, name)) is not None, "full lowercase SHA required: " + name)
    require(args.release_readback.is_absolute(), "actual release readback path must be absolute")
    readback_raw = args.release_readback.read_bytes()
    readback = load(args.release_readback)
    require(readback.get("pin") == args.release_commit and readback.get("tree") == args.release_tree,
            "release readback commit/tree do not match CLI")
    for key in ("actual_full_byte_comparison", "teaching_unchanged", "canonical_unchanged_at_release"):
        require(readback.get(key) is True, "release readback gate not satisfied: " + key)
    for key, number in (("complete_package_files", 36), ("package_bytes", 907146), ("internal_hash_declarations", 34)):
        require(type(readback.get(key)) is int and readback[key] == number, "release count mismatch: " + key)

    actual = row_map(readback["files"])
    publication = load(W / "release/publication-inputs.json")
    published = row_map(publication)
    require(len(published) == 68, "unexpected release publication inventory")
    for path, row in published.items():
        matching(actual, row, path)
    package = load(W / "release-package-manifest.json")
    package_rows = row_map(package["files"])
    require(package["incoming_version"] == "2026-10-12-r34" and package["version"] == "2026-10-12-r35",
            "metadata release version mismatch")
    require(len(package_rows) == 36 and sum(r["bytes"] for r in package_rows.values()) == 907146,
            "complete package inventory mismatch")
    for path, row in package_rows.items():
        matching(actual, row, path)
    package_raw = (W / "release-package-manifest.json").read_bytes()
    matching(actual, {"bytes": len(package_raw), "sha256": sha(package_raw), "git_blob": blob(package_raw)},
             PREFIX + "closure-review/release-package-manifest.json")

    teaching_publication = load(W / "teaching-publication.json")
    require(teaching_publication["commit"] == TEACHING and teaching_publication["base"] == INCOMING,
            "frozen teaching/incoming package identity mismatch")
    frozen = load(W / "freeze-manifest.json")
    require(frozen["material"] == "D013" and frozen["immutable_after_freeze"] is True and len(frozen["files"]) == 6,
            "frozen teaching manifest mismatch")
    teaching_paths = set()
    for row in frozen["files"]:
        path = PREFIX + row["path"]
        matching(actual, row, path)
        teaching_paths.add(path)
    require(actual[PREFIX + "teaching/main.md"]["sha256"] == MAIN_SHA, "main teaching hash mismatch")

    before_bytes = {name: (W / "canonical-before" / name).read_bytes() for name in ("queue.json", "RUN.md", "CHANGELOG.md")}
    canonical_paths = set()
    for name, data in before_bytes.items():
        path = RUN + name
        matching(actual, {"bytes": len(data), "sha256": sha(data), "git_blob": blob(data)}, path)
        canonical_paths.add(path)
    require(set(actual) == set(published) | teaching_paths | canonical_paths,
            "readback must cover exactly release inventory, unchanged teaching and canonical inputs")
    require(readback["file_count"] == len(actual) == 77 and
            readback["actual_bytes"] == sum(r["bytes"] for r in actual.values()), "readback totals mismatch")

    archives = {entry["archive"]: entry for entry in readback["archives"]}
    require(len(archives) == len(readback["archives"]) == 4, "archive readback incomplete")
    for stem in ("author-and-inputs", "reader-complete", "technical-complete", "root-complete"):
        manifest = load(W / "release" / (stem + "-members.json"))
        remote = archives[manifest["archive"]]
        require(remote["bytes"] == manifest["archive_bytes"] and remote["sha256"] == manifest["archive_sha256"] and
                remote["members_verified"] == manifest["member_count"], "archive verification mismatch " + stem)
    require(sum(x["members_verified"] for x in archives.values()) == 482, "archive member total mismatch")
    opaque = readback.get("opaque_future_original_reassembly", {})
    require(opaque.get("byte_equal_local_original") is True and opaque.get("zip_crc") is True and
            opaque.get("members") == 277 and opaque.get("semantic_contents_read") is False,
            "opaque future preservation readback incomplete")

    before = json.loads(before_bytes["queue.json"])
    after = copy.deepcopy(before)
    require(before["run_id"] == "y1-reader-20261008" and "run" not in before, "unexpected canonical schema")
    sessions = before["sessions"]
    require(len(sessions) == 147 and len({s["id"] for s in sessions}) == 147 and
            [s["material_id"] for s in sessions] == ["D" + str(i).zfill(3) for i in range(1, 148)],
            "original complete queue identity/order mismatch")
    eligible = [s for s in sessions if s["readability"]["eligible"] is True]
    require(len(eligible) == 76 and sum(s["status"] == "closed" for s in eligible) == 13,
            "unexpected before acceptance/eligibility counts")
    scope = before["active_readability_scope"]
    require((scope["eligible"], scope["excluded"], scope["closed"], scope["remaining"]) == (76, 71, 13, 63),
            "unexpected canonical before totals")
    require(before["active_material_id"] == "D013", "unexpected active material")
    old = sessions[12]
    current = after["sessions"][12]
    require(old["material_id"] == "D013" and old["status"] == "pending", "D013 is not pending")

    operative = ["status", "source_access", "source_preparation", "incoming_prof", "outgoing_prof", "published_commit",
                 "current_review_status", "current_iteration", "incoming_revision", "incoming_commit", "activation",
                 "current_teaching", "current_frozen_commit", "document_commit", "document_revision", "final_document_sha256"]
    previous_fields = {key: copy.deepcopy(old[key]) for key in operative if key in old}
    current["iteration_history"].append({"superseded_by": "published-r34-20261012", "previous_current_fields": previous_fields})
    release_urls = ["https://github.com/alverstris/PROF-Skill.md-/blob/" + args.release_commit + "/" + row["path"]
                    for row in publication]
    local_evidence = [row["path"][len(RUN):] for row in publication if row["path"].startswith(PREFIX)]
    append_unique(current["evidence"], local_evidence + release_urls +
                  [REL + "freeze-manifest.json", REL + "teaching/main.md", REL + "teaching/hints.md",
                   REL + "teaching/solutions.md", REL + "closure-support/package-admission.json",
                   REL + "closure-support/release-readback.json", REL + "closure-support/closure-invariants.json"])
    current.update({
        "status": "closed",
        "source_access": "Complete original five-page source, full frozen baseline and all six unchanged teaching constituents reviewed. Whole source/technical, chronological reader and actual destination gates accepted; original qualifications and reports preserved. Complete metadata-only r35 release A actual-byte readback verified before this canonical closure preparation.",
        "incoming_prof": "2026-10-12-r34", "incoming_revision": "2026-10-12-r34", "incoming_commit": INCOMING,
        "outgoing_prof": "2026-10-12-r35", "published_commit": args.release_commit,
        "activation": REL + "closure-support/package-admission.json",
        "current_teaching": REL + "teaching/main.md", "current_frozen_commit": TEACHING,
        "document_commit": TEACHING, "document_revision": "published-r34-20261012", "final_document_sha256": MAIN_SHA,
        "current_review_status": {
            "technical_source": "complete original source and whole frozen teaching audit accepted; original findings/qualifications preserved",
            "fresh_reader": "whole chronological reader admitted with actual ordered retrieval and original figure-view results verified; original report unchanged",
            "destination": "whole actual destination review and consequential navigation gates accepted; original observation limits preserved",
            "iteration_closure": "closed after actual complete r35 metadata-only release A readback; canonical closure publication/readback remains separate"
        },
        "current_iteration": {
            "state": "closed", "incoming_prof": "2026-10-12-r34", "outgoing_prof": "2026-10-12-r35",
            "release_commit": args.release_commit, "release_tree": args.release_tree,
            "frozen_teaching_commit": TEACHING, "verified_package_commit": args.release_commit,
            "acceptance": REL + "closure-review/whole-disposition.md",
            "release_readback": REL + "closure-support/release-readback.json", "closure": REL + "closure-support/closure-invariants.json",
            "next_action": "Active D008 requires fresh whole generation under actual published r35; next pending after D008 is D015. Continue the full eligible corpus with original inputs, fresh contexts and sole publication ownership."
        }
    })
    current["source_preparation"]["state"] = "full_original_source_and_teaching_reviews_complete"
    current["source_preparation"]["next_document_authored"] = True
    append_unique(current["source_preparation"]["evidence"], [REL + "evidence/author-and-inputs.zip", REL + "closure-review/technical-review.md"])
    after["active_readability_scope"]["closed"] = 14
    after["active_readability_scope"]["remaining"] = 62
    after["active_material_id"] = "D008"

    require(set(after) == set(before), "top-level schema changed")
    require(all(a == b for i, (a, b) in enumerate(zip(sessions, after["sessions"])) if i != 12),
            "one of the other 146 session objects changed")
    require(all(a["readability"] == b["readability"] for a, b in zip(sessions, after["sessions"])), "eligibility changed")
    require(current["iteration_history"][-1]["previous_current_fields"] == previous_fields, "old operative fields not preserved")
    array_paths = preserved_arrays(before, after)
    pending = [s["material_id"] for s in after["sessions"] if s["readability"]["eligible"] and s["status"] != "closed"]
    require(len(pending) == 62 and pending[:2] == ["D008", "D015"], "remaining queue or next order mismatch")
    require(sum(s["status"] == "closed" for s in after["sessions"] if s["readability"]["eligible"]) == 14,
            "closed count mismatch")
    require(all(before[k] == after[k] for k in before if k not in ("sessions", "active_readability_scope", "active_material_id")),
            "unrelated top-level field changed")

    summary = (
        "D013 accepted; metadata-only PROF r35 closure — 2026-10-12\n\n"
        f"Fresh D013 under PROF 2026-10-12-r34 at {INCOMING} is accepted after the complete source/technical, "
        "chronological reader and actual destination gates. Frozen teaching remains exactly " + TEACHING +
        "; main SHA-256 " + MAIN_SHA + ". All original reports and qualifications are preserved.\n\n"
        f"Complete metadata-only PROF 2026-10-12-r35 release A {args.release_commit} (tree {args.release_tree}) "
        f"has actual full-byte readback: {readback['file_count']} paths, {readback['actual_bytes']} bytes, 36 package files/907146 bytes, "
        "all 34 internal declarations, all 482 archive members, unchanged teaching and canonical inputs. "
        "No behavioral PROF repair or teaching/report mutation is introduced at closure.\n\n"
        "Canonical totals: 14 accepted / 62 remaining of 76 eligible; 71 excluded; all 147 IDs, order and eligibility preserved. "
        "Only D013's session object changes. Active D008; next pending after D008 is D015. Continue the whole corpus with fresh "
        "author/reader contexts and original inputs after canonical publication/readback.\n\n"
        "Evidence: " + REL + "closure-review/whole-disposition.md; " + REL + "closure-support/release-readback.json; " + REL +
        "closure-support/closure-invariants.json. Canonical closure publication/readback is a separate publisher step, not asserted by this preparation.\n\n"
        "Earlier preserved record follows unchanged.\n\n"
    ).encode("utf-8")
    outputs = {"queue.json": json_bytes(after), "RUN.md": summary + before_bytes["RUN.md"],
               "CHANGELOG.md": summary + before_bytes["CHANGELOG.md"], "release-readback.json": readback_raw}
    invariants = {
        "state": "canonical_closure_prepared_after_actual_release_A_readback; pending_canonical_publication",
        "release_commit": args.release_commit, "release_tree": args.release_tree,
        "release_readback_sha256": sha(readback_raw), "incoming_prof": "2026-10-12-r34", "incoming_commit": INCOMING,
        "outgoing_prof": "2026-10-12-r35", "metadata_only": True, "frozen_teaching_commit": TEACHING, "main_sha256": MAIN_SHA,
        "total_ids": 147, "eligible": 76, "excluded": 71, "accepted": 14, "remaining": 62,
        "active_material_id": "D008", "next_pending_material_id": "D015", "only_changed_session": "D013",
        "all_146_other_sessions_equal": True, "all_ids_order_eligibility_preserved": True,
        "all_old_D013_operative_fields_preserved": True, "prior_arrays_preserved_as_prefixes": array_paths,
        "no_new_top_level_fields": True, "no_new_top_level_run": True,
        "original_RUN_and_CHANGELOG_exact_suffix_preserved": True,
        "all_current_release_evidence_locators": release_urls,
        "before": {name: {"bytes": len(data), "sha256": sha(data), "git_blob": blob(data)} for name, data in before_bytes.items()},
        "outputs": {name: {"bytes": len(data), "sha256": sha(data), "git_blob": blob(data)} for name, data in outputs.items()},
        "limits": "This local script trusts and checks the supplied actual publisher readback record; it does not perform network verification or publish. Original teaching, reports, package files, prior arrays and other sessions are never rewritten."
    }
    for name in ("RUN.md", "CHANGELOG.md"):
        require(outputs[name].endswith(before_bytes[name]), "original document suffix changed")
    # All checks finish before the first output-directory mutation.
    out = W / "canonical-after" / args.release_commit
    require(not out.exists(), "refusing to overwrite an existing closure output directory")
    out.mkdir(parents=True, exist_ok=False)
    for name, data in outputs.items():
        with (out / name).open("xb") as stream:
            stream.write(data)
    with (out / "closure-invariants.json").open("xb") as stream:
        stream.write(json_bytes(invariants))
    print(json.dumps({"output_directory": str(out), "files": list(outputs) + ["closure-invariants.json"],
                      "accepted": 14, "remaining": 62, "active": "D008", "next": "D015"}, indent=2))


if __name__ == "__main__":
    main()
