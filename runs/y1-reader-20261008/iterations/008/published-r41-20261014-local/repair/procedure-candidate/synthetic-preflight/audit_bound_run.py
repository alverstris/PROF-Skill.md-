"""Compare a complete runtime ledger to its fixed route; no content-file read.

Checks operational access/display records, not semantic inspection or confinement.
Rejection events remain visible for the orchestrator to classify separately.
"""
import json
import sys
import fixed_launcher as runner


def audit():
    config = runner.load_config()
    state = runner.load_state(config)
    ledger_path = runner.RUNTIME_DIR / "access.jsonl"
    events = [runner.unique_json(line) for line in ledger_path.read_bytes().splitlines()]
    steps = config["steps"]
    by_id = {s["id"]: s for s in steps}
    cursor = 0
    baseline_read = set()
    pending_text = None
    pending_figure = None
    accesses = []
    displays = []
    rejections = []
    for index, event in enumerate(events):
        runner.require(event.get("route_sha256") == runner.EXPECTED_CONFIG_SHA256, "ledger route identity mismatch")
        kind = event["event"]
        if kind in ("launcher_rejected", "receipt_rejected", "view_failed"):
            rejections.append({"ledger_index": index, **event})
        if kind == "verified_access_receipt":
            runner.require(pending_text is None and pending_figure is None, "new content before preceding text/image output receipt")
            step_id = event["requested_step"]
            revisit = step_id in config["baseline_revisits"]
            target_id = config["baseline_revisits"].get(step_id, step_id)
            runner.require(target_id in by_id, "unknown access receipt step")
            step = by_id[target_id]
            runner.require(event["target_step"] == target_id and event["baseline_revisit"] is revisit, "access target/revisit mismatch")
            if revisit:
                runner.require(target_id in baseline_read, "unread baseline revisit in ledger")
            else:
                runner.require(cursor < len(steps) and step_id == steps[cursor]["id"], "ledger access out of route order")
            runner.require(event["file_id"] == step["file_id"] and event["start"] == step["start"] and event["byte_length"] == step["length"] and event["sha256"] == step["sha256"], "ledger exact range/hash mismatch")
            runner.require(event["cursor_before"] == cursor, "ledger cursor-before mismatch")
            if step["kind"] == "figure":
                runner.require(event["cursor_after"] == cursor and event["figure_pending"] is True, "figure access advanced without display")
                pending_figure = {"step_id": step_id, "stages": [], "result_hash": None, "nonce": None}
            else:
                if not revisit:
                    cursor += 1
                    if config["files"][step["file_id"]]["kind"] == "baseline":
                        baseline_read.add(step_id)
                runner.require(event["cursor_after"] == cursor and event["figure_pending"] is False, "text/revisit cursor mismatch")
                pending_text = {"step_id": step_id, "sha256": step["sha256"], "byte_length": step["length"]}
            accesses.append({"ledger_index": index, "step_id": step_id, "target_step": target_id, "sha256": step["sha256"], "byte_length": step["length"]})
        elif kind == "text_output_delivered":
            runner.require(pending_text is not None and event["step_id"] == pending_text["step_id"] and event["sha256"] == pending_text["sha256"] and event["byte_length"] == pending_text["byte_length"], "text output receipt mismatch")
            displays.append({"ledger_index": index, "step_id": event["step_id"], "kind": "text"})
            pending_text = None
        elif kind in ("view_invocation", "view_result", "image_output_delivered"):
            runner.require(pending_figure is not None and event["step_id"] == pending_figure["step_id"] and event["tool_name"] == "functions.view_image", "view receipt outside scheduled figure")
            expected_stage = ("view_invocation", "view_result", "image_output_delivered")[len(pending_figure["stages"])]
            runner.require(kind == expected_stage, "figure receipt order mismatch")
            step = by_id[pending_figure["step_id"]]
            runner.require(event["input_sha256"] == step["sha256"], "view input image mismatch")
            if kind == "view_invocation":
                pending_figure["nonce"] = event["nonce"]
            else:
                runner.require(event["nonce"] == pending_figure["nonce"], "view receipt nonce mismatch")
            pending_figure["stages"].append(kind)
            if kind == "view_result":
                runner.require(event["result_image_sha256"] == step["sha256"] and event["result_image_bytes"] == step["length"] and event["result_detail"] == "original", "view result is not the exact complete identified image")
                pending_figure["result_hash"] = event["result_image_sha256"]
            if kind == "image_output_delivered":
                runner.require(event["result_image_sha256"] == pending_figure["result_hash"] and event["semantic_inspection_claim"] is False, "display result mismatch/semantic overclaim")
                runner.require(event["cursor_before"] == cursor and event["cursor_after"] == cursor + 1, "display cursor advancement mismatch")
                cursor += 1
                displays.append({"ledger_index": index, "step_id": event["step_id"], "kind": "figure"})
                pending_figure = None
    runner.require(cursor == len(steps) and state["cursor"] == cursor and pending_text is None and pending_figure is None and state["pending_figure"] is None, "route/display evidence incomplete")
    raw_opens = [e for e in events if e["event"] == "python_subject_open_audit"]
    bounded_reads = [e for e in events if e["event"] == "bounded_bytes_read"]
    runner.require(len(raw_opens) == len(accesses) == len(bounded_reads), "unverified/extra content open or read")
    for access, read in zip(accesses, bounded_reads):
        runner.require(read["requested_step"] == access["step_id"] and read["sha256"] == access["sha256"] and read["actual_length"] == access["byte_length"] and read["requested_length"] == access["byte_length"], "bounded read/access mismatch")
    return {"route_id": config["route_id"], "route_sha256": runner.EXPECTED_CONFIG_SHA256, "operational_route_audit_passed": True,
            "scheduled_steps": len(steps), "verified_accesses": accesses, "display_receipts": displays,
            "subject_open_audit_count": len(raw_opens), "rejected_or_failed_calls_for_separate_review": rejections,
            "complete_text_byte_coverage_from_exact_route": True, "complete_figure_delivery_receipts_present": True,
            "semantic_inspection_proven": False, "technical_confinement_proven": False, "reader_admission_automatic": False}


if __name__ == "__main__":
    if len(sys.argv) != 1:
        raise SystemExit("no arguments accepted")
    try:
        print(json.dumps(audit(), indent=2))
    except Exception as exc:
        print(json.dumps({"operational_route_audit_passed": False, "error": str(exc)}), file=sys.stderr)
        raise SystemExit(2)
