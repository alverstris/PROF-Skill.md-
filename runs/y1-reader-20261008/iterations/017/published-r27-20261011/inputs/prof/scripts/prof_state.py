#!/usr/bin/env python3
"""PROF state bookkeeping. A clean result is mechanical readiness, not teaching certification.

Only init and begin-topic write state. No command stored in JSON is ever executed;
source, request, skill, evidence and output files are only read. See state-tool.md.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import sys
import tempfile
import os

VERSION = 1
IDS = re.compile(r"[a-z][a-z0-9_-]{0,63}\Z")
HASH = re.compile(r"[0-9a-f]{64}\Z")
REQUIREMENTS = tuple("T%d" % n for n in range(1, 13))
STATUSES = {"pending", "pass", "fail", "unverified", "not_applicable", "waived_by_user"}
LIMIT = ("This checks declared records, file/locator existence and revision freshness only. "
         "Source reads, web reads, applicability, waivers and semantic reviews are self-reported. "
         "It does not certify teaching quality, learner mastery, authorization, or skill invocation/application.")


def digest(path):
    value = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            value.update(chunk)
    return value.hexdigest()


def read_json(path):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError("duplicate JSON key: " + key)
            result[key] = value
        return result
    return json.loads(Path(path).read_text(encoding="utf-8"), object_pairs_hook=unique)


def save_json(path, value):
    path = Path(path)
    # Replace only this state file; an interrupted write leaves the previous JSON intact.
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent,
                                         prefix=path.name + ".", suffix=".tmp", delete=False) as handle:
            temporary = Path(handle.name)
            handle.write(json.dumps(value, indent=2, ensure_ascii=False) + "\n")
            handle.flush()
            os.fsync(handle.fileno())
        temporary.replace(path)
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()


def canonical_hash(value):
    """SHA-256 of UTF-8 compact JSON with sorted keys and ensure_ascii=False."""
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
                                     ensure_ascii=False).encode("utf-8")).hexdigest()


def pending():
    return {"applicable": True, "status": "pending", "reason": "",
            "evidence": [], "dependencies": []}


class Audit:
    def __init__(self, state):
        self.state = Path(state).resolve()
        self.errors = []
        self.notes = []
        self.topic_counts = {}
        self.refs = {}
        self.sources = {}
        self.portions = {}
        self.topics = {}
        self.outputs = {}

    def bad(self, where, message):
        self.errors.append(where + ": " + message)

    def shape(self, obj, required, optional, where):
        if not isinstance(obj, dict):
            self.bad(where, "expected an object")
            return False
        missing = set(required) - set(obj)
        extra = set(obj) - set(required) - set(optional)
        if missing or extra:
            self.bad(where, "schema fields missing=%s unknown=%s" % (sorted(missing), sorted(extra)))
            return False
        return True

    def array(self, value, where):
        if not isinstance(value, list):
            self.bad(where, "expected an array")
            return []
        return value

    def string(self, value, where, allow_empty=False):
        if not isinstance(value, str) or (not allow_empty and not value.strip()):
            self.bad(where, "expected a nonempty string")
            return False
        return True

    def identifier(self, value, where):
        if not isinstance(value, str) or not IDS.fullmatch(value):
            self.bad(where, "invalid ID; use a lowercase letter then letters, digits, _ or - (max 64)")
            return False
        return True

    def path(self, value, where, absolute=False, request_alias=False):
        if request_alias and value == "@request":
            return self.refs.get(("request", ""), (None, None))[0]
        if not self.string(value, where):
            return None
        if "\x00" in value or re.match(r"^[a-zA-Z]+://", value):
            self.bad(where, "expected a filesystem path, not a URL or NUL")
            return None
        p = Path(value)
        if absolute:
            if not p.is_absolute():
                self.bad(where, "path must be absolute")
                return None
            return p.resolve()
        if p.is_absolute() or ".." in p.parts or re.match(r"^[A-Za-z]:", value):
            self.bad(where, "path must be relative to project_root without '..'")
            return None
        p = (self.root / p).resolve()
        if not p.is_relative_to(self.root):
            self.bad(where, "path escapes project_root (including a link)")
            return None
        return p

    def file_hash(self, path, expected, where):
        if not isinstance(expected, str) or not HASH.fullmatch(expected):
            self.bad(where, "missing or malformed SHA-256")
            return False
        if path is None:
            return False
        try:
            actual = digest(path)
        except OSError as exc:
            self.bad(where, "cannot read file: " + str(exc))
            return False
        if actual != expected:
            self.bad(where, "stale hash; current bytes differ (checks were not refreshed)")
            return False
        return True

    def ref(self, kind, obj, where, absolute=False):
        if not self.shape(obj, {"path", "sha256"}, set(), where):
            return
        path = self.path(obj["path"], where + ".path", absolute)
        self.file_hash(path, obj["sha256"], where)
        self.refs[(kind, "")] = (path, obj["sha256"])

    def evidence(self, items, where, waiver=False):
        items = self.array(items, where)
        if not items:
            self.bad(where, "completed pass/waiver needs actual evidence")
        instruction = False
        for n, item in enumerate(items):
            label = "%s[%d]" % (where, n)
            if not self.shape(item, {"path", "sha256", "locator"}, set(), label):
                continue
            path = self.path(item["path"], label + ".path", request_alias=True)
            self.file_hash(path, item["sha256"], label)
            loc = item["locator"]
            if not isinstance(loc, dict) or loc.get("kind") not in {"lines", "text"}:
                self.bad(label, "evidence locator must be lines or exact text")
                continue
            try:
                content = path.read_text(encoding="utf-8") if path else ""
            except (OSError, UnicodeError) as exc:
                self.bad(label, "evidence must be a readable UTF-8 witness file: " + str(exc))
                continue
            if loc["kind"] == "lines":
                if not self.shape(loc, {"kind", "start", "end"}, set(), label + ".locator"):
                    continue
                start, end = loc["start"], loc["end"]
                if (type(start) is not int or type(end) is not int or
                        not 1 <= start <= end <= len(content.splitlines())):
                    self.bad(label, "nonexistent or invalid line range")
            else:
                if not self.shape(loc, {"kind", "value"}, set(), label + ".locator"):
                    continue
                if not self.string(loc["value"], label + ".locator.value"):
                    continue
                if loc["value"] not in content:
                    self.bad(label, "exact text locator does not occur in witness file")
                elif item["path"] == "@request":
                    instruction = True
        if waiver and not instruction:
            self.bad(where, "waiver/exclusion needs exact user-instruction text in @request")

    def dependencies(self, items, expected, where):
        seen = set()
        for n, item in enumerate(self.array(items, where)):
            label = "%s[%d]" % (where, n)
            if not self.shape(item, {"kind", "id", "sha256"}, set(), label):
                continue
            key = (item["kind"], item["id"])
            if not isinstance(key[0], str) or not isinstance(key[1], str):
                self.bad(label, "dependency kind/id must be strings")
                continue
            if key in seen:
                self.bad(label, "duplicate dependency")
            seen.add(key)
            if key not in self.refs:
                self.bad(label, "unknown dependency " + str(key))
            elif item["sha256"] != self.refs[key][1]:
                self.bad(label, "stale dependency hash for " + str(key))
        for key in sorted(expected - seen):
            self.bad(where, "missing dependency binding " + str(key))

    def condition(self, obj, expected, where, universal=False):
        if not self.shape(obj, {"applicable", "status", "reason", "evidence", "dependencies"}, set(), where):
            return
        applicable, status = obj["applicable"], obj["status"]
        if type(applicable) is not bool or not isinstance(status, str) or status not in STATUSES:
            self.bad(where, "invalid applicability/status")
            return
        self.string(obj["reason"], where + ".reason", status in {"pending", "fail", "unverified"})
        self.array(obj["evidence"], where + ".evidence")
        self.array(obj["dependencies"], where + ".dependencies")
        if universal and (not applicable or status in {"not_applicable", "waived_by_user"}):
            self.bad(where, "universal truthful acceptance/coverage cannot be waived or inapplicable")
        if (not applicable) != (status == "not_applicable"):
            self.bad(where, "false trigger requires not_applicable; applicable duty cannot use it")
        if status in {"pending", "fail", "unverified"}:
            self.bad(where, "not ready: " + status)
        else:
            self.dependencies(obj["dependencies"], expected, where + ".dependencies")
            if status in {"pass", "waived_by_user"}:
                self.evidence(obj["evidence"], where + ".evidence", status == "waived_by_user")
            elif obj["evidence"]:
                self.evidence(obj["evidence"], where + ".evidence")

    def load_manifest(self, selected_topic=None):
        try:
            m = read_json(self.state / "manifest.json")
        except (OSError, UnicodeError, ValueError) as exc:
            self.bad("manifest", "cannot load JSON: " + str(exc))
            return False
        if not self.shape(m, {"schema_version", "project_root", "skill", "request", "required_topics",
                              "sources", "outputs", "output_checks"}, set(), "manifest"):
            return False
        if type(m["schema_version"]) is not int or m["schema_version"] != VERSION:
            self.bad("manifest", "unsupported schema_version")
            return False
        self.root = self.path(m["project_root"], "project_root", absolute=True)
        if self.root is None or not self.root.is_dir():
            self.bad("project_root", "must be an existing directory")
            return False
        self.ref("skill", m["skill"], "skill", absolute=True)
        self.ref("request", m["request"], "request", absolute=True)
        self.manifest = m
        self.refs[("inventory", "")] = (None, canonical_hash({k: v for k, v in m.items() if k != "output_checks"}))
        selected = next((t for t in m["required_topics"] if isinstance(t, dict) and
                         t.get("id") == selected_topic), {}) if isinstance(m["required_topics"], list) else {}
        selected_sources = {p.get("source_id") for p in selected.get("source_portions", [])
                            if isinstance(p, dict) and isinstance(p.get("source_id"), str)} \
                           if isinstance(selected.get("source_portions", []), list) else set()
        selected_outputs = {p for p in selected.get("outputs", []) if isinstance(p, str)} \
                           if isinstance(selected.get("outputs", []), list) else set()
        for source in self.array(m["sources"], "sources"):
            if not self.shape(source, {"id", "path", "sha256", "portions"}, {"url"}, "source"):
                continue
            sid = source["id"]
            if not self.identifier(sid, "source.id"):
                continue
            if sid in self.sources:
                self.bad(sid, "duplicate source ID")
            self.sources[sid] = source
            self.refs[("source_scope", sid)] = (None, canonical_hash(source))
            if "url" in source and not self.string(source["url"], sid + ".url"):
                continue
            path = self.path(source["path"], sid + ".path", absolute=True)
            if selected_topic is None or sid in selected_sources:
                self.file_hash(path, source["sha256"], sid)
            self.refs[("source", sid)] = (path, source["sha256"])
            portions = self.array(source["portions"], sid + ".portions")
            if not portions:
                self.bad(sid, "declare supplied/researched source portions; whole-file is a valid portion")
            for portion in portions:
                if not self.shape(portion, {"id", "locator", "disposition", "reason", "evidence"}, set(), sid + ".portion"):
                    continue
                pid = portion["id"]
                if not self.identifier(pid, sid + ".portion.id"):
                    continue
                key = (sid, pid)
                if key in self.portions:
                    self.bad(sid, "duplicate portion ID " + pid)
                self.portions[key] = portion
                self.string(portion["locator"], sid + "." + pid + ".locator")
                if portion["disposition"] not in {"required", "excluded_by_user", "inaccessible"}:
                    self.bad(sid + "." + pid, "unknown portion disposition")
                if portion["disposition"] != "required":
                    self.string(portion["reason"], sid + "." + pid + ".reason")
                self.array(portion["evidence"], sid + "." + pid + ".evidence")
                if portion["disposition"] == "excluded_by_user" and (selected_topic is None or sid in selected_sources):
                    self.evidence(portion["evidence"], sid + "." + pid + ".evidence", waiver=True)
        for output in self.array(m["outputs"], "outputs"):
            if not self.shape(output, {"id", "path", "sha256"}, set(), "output"):
                continue
            oid = output["id"]
            if not self.identifier(oid, "output.id"):
                continue
            if oid in self.outputs:
                self.bad(oid, "duplicate output ID")
            self.outputs[oid] = output
            path = self.path(output["path"], oid + ".path")
            if selected_topic is None or oid in selected_outputs:
                self.file_hash(path, output["sha256"], oid)
            self.refs[("output", oid)] = (path, output["sha256"])
        for topic in self.array(m["required_topics"], "required_topics"):
            if not self.shape(topic, {"id", "title", "source_portions", "outputs"}, set(), "topic declaration"):
                continue
            tid = topic["id"]
            if not self.identifier(tid, "topic.id"):
                continue
            if tid in self.topics:
                self.bad(tid, "duplicate required topic ID")
            self.topics[tid] = topic
            self.refs[("topic", tid)] = (None, canonical_hash(topic))
            self.string(topic["title"], tid + ".title")
        if not self.topics:
            self.bad("required_topics", "must explicitly declare at least one topic")
        if not self.outputs:
            self.bad("outputs", "must explicitly declare at least one actual output")
        if not (self.state / "RUN.md").is_file():
            self.bad("RUN.md", "missing recovery record")
        return True

    def topic_bindings(self, declaration):
        tid = declaration["id"]
        expected = {("request", ""), ("skill", ""), ("topic", tid)}
        assigned = set()
        for item in self.array(declaration["source_portions"], tid + ".source_portions"):
            if not self.shape(item, {"source_id", "portion_id"}, set(), tid + ".source_portions"):
                continue
            if not self.identifier(item["source_id"], tid + ".source_id") or not self.identifier(item["portion_id"], tid + ".portion_id"):
                continue
            key = (item["source_id"], item["portion_id"])
            if key in assigned:
                self.bad(tid, "duplicate source portion assignment")
            assigned.add(key)
            if key not in self.portions:
                self.bad(tid, "unknown source portion " + str(key))
            elif self.portions[key]["disposition"] != "required":
                self.bad(tid, "assigned portion is excluded or inaccessible " + str(key))
            expected.add(("source", item["source_id"]))
            expected.add(("source_scope", item["source_id"]))
        output_ids = self.array(declaration["outputs"], tid + ".outputs")
        if not output_ids:
            self.bad(tid, "topic needs a declared output location")
        for oid in output_ids:
            if not self.identifier(oid, tid + ".output_id"):
                continue
            if oid not in self.outputs:
                self.bad(tid, "unknown output " + oid)
            expected.add(("output", oid))
        return expected, assigned

    def check_topic(self, tid):
        expected, assigned = self.topic_bindings(self.topics[tid])
        try:
            t = read_json(self.state / "topics" / (tid + ".json"))
        except (OSError, UnicodeError, ValueError) as exc:
            self.bad(tid, "missing/unreadable topic record: " + str(exc))
            return assigned
        if not self.shape(t, {"id", "activation", "source_reads", "gaps", "requirements"}, set(), tid):
            return assigned
        if t["id"] != tid:
            self.bad(tid, "topic record ID differs from manifest")
        a = t["activation"]
        if self.shape(a, {"skill_path", "skill_sha256", "activated_at"}, set(), tid + ".activation"):
            skill_path, skill_hash = self.refs.get(("skill", ""), (None, None))
            if a["skill_path"] != str(skill_path) or a["skill_sha256"] != skill_hash:
                self.bad(tid, "missing/stale per-topic skill activation; use begin-topic after rereading")
            try:
                stamp = datetime.fromisoformat(a["activated_at"])
                if stamp.tzinfo is None:
                    raise ValueError("timezone missing")
            except (TypeError, ValueError):
                self.bad(tid, "missing/malformed activation timestamp")
        seen = set()
        for read in self.array(t["source_reads"], tid + ".source_reads"):
            if not self.shape(read, {"source_id", "portion_id", "status", "reviewed_sha256", "note"}, set(), tid + ".source_read"):
                continue
            if not self.identifier(read["source_id"], tid + ".source_id") or not self.identifier(read["portion_id"], tid + ".portion_id"):
                continue
            key = (read["source_id"], read["portion_id"])
            if key in seen or key not in assigned:
                self.bad(tid, "duplicate/unassigned source read " + str(key))
            seen.add(key)
            if read["status"] != "read":
                self.bad(tid, "required source portion unread: " + str(key))
            self.string(read["note"], tid + ".source_read.note")
            ref = self.refs.get(("source", read["source_id"]))
            if ref is None or read["reviewed_sha256"] != ref[1]:
                self.bad(tid, "stale/missing source-reading hash: " + str(key))
        for key in sorted(assigned - seen):
            self.bad(tid, "required source portion has no read record: " + str(key))
        gap_ids = set()
        for gap in self.array(t["gaps"], tid + ".gaps"):
            if not self.shape(gap, {"id", "question", "consequential", "status", "reason", "next_action", "evidence", "dependencies"}, set(), tid + ".gap"):
                continue
            if not self.identifier(gap["id"], tid + ".gap.id"):
                continue
            if gap["id"] in gap_ids:
                self.bad(tid, "duplicate gap ID")
            gap_ids.add(gap["id"])
            label = tid + ".gap." + gap["id"]
            self.string(gap["question"], label + ".question")
            if type(gap["consequential"]) is not bool or gap["status"] not in {"open", "unverified", "resolved", "waived_by_user"}:
                self.bad(label, "invalid consequence/status")
            if gap["status"] in {"open", "unverified"}:
                self.string(gap["next_action"], label + ".next_action")
                if gap["consequential"]:
                    self.bad(label, "unresolved consequential gap")
                else:
                    self.notes.append(label + ": nonconsequential gap remains " + str(gap["status"]))
            else:
                self.string(gap["reason"], label + ".reason")
                self.evidence(gap["evidence"], label + ".evidence", gap["status"] == "waived_by_user")
                self.dependencies(gap["dependencies"], expected, label + ".dependencies")
        r = t["requirements"]
        if self.shape(r, set(REQUIREMENTS), set(), tid + ".requirements"):
            self.topic_counts[tid] = {s: sum(isinstance(x, dict) and x.get("status") == s for x in r.values()) for s in sorted(STATUSES)}
            for rid in REQUIREMENTS:
                self.condition(r[rid], expected, tid + "." + rid, universal=rid == "T12")
        return assigned

    def run(self, topic=None):
        if not self.load_manifest(topic):
            return self
        if topic is not None and topic not in self.topics:
            self.bad("topic", "not a required topic: " + topic)
            return self
        assigned = set()
        for tid in ([topic] if topic else self.topics):
            assigned.update(self.check_topic(tid))
        if topic is None:
            for key, portion in self.portions.items():
                if portion["disposition"] == "required" and key not in assigned:
                    self.bad("sources", "required portion not assigned to any topic: " + str(key))
                elif portion["disposition"] == "inaccessible":
                    self.bad("sources", "inaccessible portion keeps full completion unverified: " + str(key))
            checks = self.array(self.manifest["output_checks"], "output_checks")
            seen = set()
            expected = set(self.refs)
            for check in checks:
                if not self.shape(check, {"id", "description", "applicable", "status", "reason", "evidence", "dependencies"}, set(), "output_check"):
                    continue
                cid = check["id"]
                if not self.identifier(cid, "output_check.id"):
                    continue
                if cid in seen:
                    self.bad(cid, "duplicate output check")
                seen.add(cid)
                self.string(check["description"], cid + ".description")
                self.condition({k: v for k, v in check.items() if k not in {"id", "description"}}, expected,
                               "output_check." + cid, universal=cid in {"coverage", "final_review"})
            for cid in {"coverage", "final_review"} - seen:
                self.bad("output_checks", "missing mandatory declared check: " + cid)
        return self

    def report(self, topic=None):
        return {"result": "NOT_READY" if self.errors else "MECHANICALLY_READY",
                "scope": "topic:" + topic if topic else "full declared project",
                "limits": LIMIT, "requirements": self.topic_counts, "defects": self.errors,
                "notes": self.notes,
                "next_action": "Address the listed readiness items: repair actual defects or await required student information. Recheck affected teaching and dependencies before updating recorded hashes; do not invent resolution to obtain a clean status."
                if self.errors else "Author remains responsible for substantive acceptance and honest delivery."}


def initialize(args):
    state = Path(args.state).resolve()
    if state.exists() and any(state.iterdir()):
        raise ValueError("state directory must be absent or empty; refusing to overwrite records")
    skill = Path(args.skill).resolve()
    request = Path(args.request).resolve()
    skill.read_text(encoding="utf-8")
    request.read_text(encoding="utf-8")
    root = Path(args.project_root).resolve() if args.project_root else state.parent
    if not root.is_dir():
        raise ValueError("project_root must be an existing directory")
    if len(set(args.topic)) != len(args.topic) or any(not IDS.fullmatch(t) for t in args.topic):
        raise ValueError("topic IDs must be unique lowercase safe identifiers")
    (state / "topics").mkdir(parents=True, exist_ok=True)
    manifest = {"schema_version": VERSION, "project_root": str(root),
                "skill": {"path": str(skill), "sha256": digest(skill)},
                "request": {"path": str(request), "sha256": digest(request)},
                "required_topics": [{"id": t, "title": t, "source_portions": [], "outputs": []} for t in args.topic],
                "sources": [], "outputs": [],
                "output_checks": [{"id": cid, "description": description, **pending()} for cid, description in
                                  [("coverage", "Compare all requested topics and source portions with final locations."),
                                   ("final_review", "Read and audit the actual complete final route, help and material limits.")]]}
    save_json(state / "manifest.json", manifest)
    for tid in args.topic:
        save_json(state / "topics" / (tid + ".json"), {"id": tid,
                  "activation": {"skill_path": "", "skill_sha256": "", "activated_at": ""},
                  "source_reads": [], "gaps": [], "requirements": {rid: pending() for rid in REQUIREMENTS}})
    (state / "RUN.md").write_text("# PROF recovery\n\nExact request: " + str(request) +
                                 "\n\nExact skill: " + str(skill) +
                                 "\n\nCurrent topic: choose the next manifest topic.\n\n" +
                                 "Decisions/conventions and learner evidence: record exact locators, dates and uncertainty here.\n\n" +
                                 "Next action: read the skill and exact request; declare source portions and outputs; begin one topic.\n\n" +
                                 "After a reset: reread this record, the skill, request and the next topic's artifacts/sources.\n",
                                 encoding="utf-8")
    print("Initialized pending state at " + str(state))
    print(LIMIT)


def begin(args):
    state = Path(args.state).resolve()
    manifest = read_json(state / "manifest.json")
    if manifest.get("schema_version") != VERSION:
        raise ValueError("unsupported schema_version")
    if not IDS.fullmatch(args.topic) or args.topic not in {t["id"] for t in manifest["required_topics"]}:
        raise ValueError("topic must be a safe, declared required topic ID")
    skill = Path(manifest["skill"]["path"])
    if not skill.is_absolute():
        raise ValueError("skill path must be absolute")
    skill = skill.resolve()
    raw = skill.read_bytes()  # A real complete read, not a caller's asserted hash.
    content = raw.decode("utf-8")
    topic_root = (state / "topics").resolve()
    path = (topic_root / (args.topic + ".json")).resolve()
    if not topic_root.is_relative_to(state) or not path.is_relative_to(topic_root):
        raise ValueError("resolved topic path escapes state/topics; refusing to write")
    protected = [manifest["skill"]["path"], manifest["request"]["path"]]
    protected += [s["path"] for s in manifest["sources"]]
    protected += [str(Path(manifest["project_root"]) / o["path"]) for o in manifest["outputs"]]
    if any(Path(p).resolve() == path for p in protected):
        raise ValueError("topic record aliases declared source/request/skill/output; refusing to write")
    record = read_json(path)
    if record.get("id") != args.topic:
        raise ValueError("record ID mismatch")
    record["activation"] = {"skill_path": str(skill), "skill_sha256": hashlib.sha256(raw).hexdigest(),
                            "activated_at": datetime.now(timezone.utc).isoformat()}
    save_json(path, record)
    print("Read %d bytes from %s\nTopic %s activation hash: %s" %
          (len(raw), skill, args.topic, record["activation"]["skill_sha256"]))
    print("The author must read and apply the skill. No requirement status or evidence hash was changed.")
    if args.show_skill:
        print(content)


def main(argv=None):
    # Keep redirected CLI output predictable across Windows parent/child locales,
    # including full Unicode skill text. StringIO used by tests has no reconfigure.
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="backslashreplace")
    parser = argparse.ArgumentParser(description=__doc__)
    subs = parser.add_subparsers(dest="command", required=True)
    init = subs.add_parser("init", help="create intentionally pending state and RUN.md")
    init.add_argument("--state", required=True)
    init.add_argument("--skill", required=True)
    init.add_argument("--request", required=True, help="UTF-8 exact user task/constraints file")
    init.add_argument("--project-root")
    init.add_argument("--topic", required=True, action="append")
    start = subs.add_parser("begin-topic", help="read current skill bytes and bind this topic activation")
    start.add_argument("--state", required=True)
    start.add_argument("--topic", required=True)
    start.add_argument("--show-skill", action="store_true")
    for name in ("check", "status"):
        check = subs.add_parser(name, help="read-only mechanical readiness summary; nonzero on defects")
        check.add_argument("--state", required=True)
        check.add_argument("--topic", help="only this topic; never certifies full project readiness")
        check.add_argument("--json", action="store_true")
    snapshots = subs.add_parser("dependencies", help="print current declared dependency snapshots; does not complete checks")
    snapshots.add_argument("--state", required=True)
    snapshots.add_argument("--topic", help="topic bindings; omission prints bindings for full output checks")
    args = parser.parse_args(argv)
    try:
        if args.command == "init":
            initialize(args)
        elif args.command == "begin-topic":
            begin(args)
        elif args.command == "dependencies":
            audit = Audit(args.state)
            if audit.load_manifest(args.topic):
                if args.topic is None:
                    expected = set(audit.refs)
                elif args.topic not in audit.topics:
                    raise ValueError("unknown required topic")
                else:
                    expected, _ = audit.topic_bindings(audit.topics[args.topic])
                if not audit.errors:
                    print(json.dumps([{"kind": kind, "id": ident, "sha256": audit.refs[(kind, ident)][1]}
                                      for kind, ident in sorted(expected)], indent=2))
                    return 0
            print(json.dumps({"result": "NOT_READY", "defects": audit.errors, "limits": LIMIT}, indent=2))
            return 1
        else:
            report = Audit(args.state).run(args.topic).report(args.topic)
            if args.json:
                print(json.dumps(report, indent=2))
            else:
                print(report["result"] + " — " + report["scope"])
                print(report["limits"])
                for tid, counts in report["requirements"].items():
                    print(tid + ": " + ", ".join("%s=%d" % (s, n) for s, n in counts.items() if n))
                for defect in report["defects"]:
                    print("READINESS ITEM " + defect)
                for note in report["notes"]:
                    print("NOTE " + note)
                print(report["next_action"])
            return 1 if report["defects"] else 0
        return 0
    except (OSError, UnicodeError, ValueError, KeyError, TypeError, AttributeError) as exc:
        print("NOT_READY — malformed/unreadable state: " + str(exc), file=sys.stderr)
        print(LIMIT, file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
