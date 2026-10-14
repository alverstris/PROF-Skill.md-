"""Adapter-only recording helper, not an authorized reader command.

Receipts are adapter assertions checked for identity/order. This cannot certify
that an arbitrary caller actually invoked a tool. The functions.exec adapter
records only events it actually observes and preserves failed calls.
"""
import base64
import sys
from pathlib import Path

import fixed_launcher as runner


def record(payload):
    config = runner.load_config()
    with runner.exclusive():
        state = runner.load_state(config)
        runner.require(type(payload) is dict, "receipt must be object")
        stage = payload.get("stage")
        if stage == "text_output_delivered":
            runner.exact_keys(payload, ("stage", "route_sha256", "step_id", "sha256", "byte_length", "display_mechanism"), "text receipt")
            runner.require(payload["route_sha256"] == runner.EXPECTED_CONFIG_SHA256, "receipt route mismatch")
            by_id = {s["id"]: s for s in config["steps"]}
            target = config["baseline_revisits"].get(payload["step_id"], payload["step_id"])
            runner.require(target in by_id, "unknown text receipt step")
            step = by_id[target]
            runner.require(step["kind"] == "text" and step["sha256"] == payload["sha256"] and step["length"] == payload["byte_length"], "text receipt content mismatch")
            runner.require(config["steps"].index(step) < state["cursor"], "text receipt before successful retrieval")
            runner.require(payload["display_mechanism"] == "functions.text_then_yield_control", "invalid text display mechanism")
            runner.append_event(stage, **{k: v for k, v in payload.items() if k != "stage"})
            return {"ok": True, "stage": stage, "cursor": state["cursor"]}
        pending = state["pending_figure"]
        runner.require(pending is not None, "no pending figure")
        common = {"stage", "route_sha256", "step_id", "nonce", "input_path", "input_sha256", "tool_name"}
        extras = {"view_invocation": set(), "view_result": {"result_image_sha256", "result_image_bytes", "result_mime_type", "display_mime_type", "result_detail"},
                  "image_output_delivered": {"result_image_sha256", "display_mechanism", "semantic_inspection_claim"},
                  "view_failed": {"error"}}
        runner.require(stage in extras, "invalid receipt stage")
        runner.exact_keys(payload, common | extras[stage], "figure receipt")
        runner.require(payload["route_sha256"] == runner.EXPECTED_CONFIG_SHA256, "receipt route mismatch")
        runner.require(payload["step_id"] == pending["step_id"] and payload["nonce"] == pending["nonce"], "receipt step/nonce mismatch")
        runner.require(payload["input_path"] == pending["cache_path"] and payload["input_sha256"] == pending["sha256"], "receipt image input mismatch")
        runner.require(payload["tool_name"] == "functions.view_image", "receipt must name actual functions.view_image tool")
        stages = pending["stages"]
        if stage == "view_invocation":
            runner.require(stages == [], "view invocation out of order")
            # Check the complete cached image without accepting a caller path/range.
            with Path(pending["cache_path"]).open("rb") as handle:
                image_data = handle.read(pending["byte_length"] + 1)
            runner.require(len(image_data) == pending["byte_length"] and runner.sha(image_data) == pending["sha256"], "cached full-image mismatch")
            runner.append_event("bounded_cache_verified", step_id=pending["step_id"], byte_length=len(image_data), sha256=runner.sha(image_data))
            pending["stages"].append(stage)
        elif stage == "view_result":
            runner.require(stages == ["view_invocation"], "view result without invocation")
            runner.require(type(payload["result_image_sha256"]) is str and runner.HEX_RE.fullmatch(payload["result_image_sha256"]), "invalid actual result hash")
            runner.integer(payload["result_image_bytes"], 1, 64 * 1024 * 1024, "result image length")
            runner.require(payload["result_mime_type"] in ("image/png", "image/jpeg", "image/webp", "application/octet-stream") and
                           payload["display_mime_type"] == "image/png" and payload["result_detail"] == "original", "invalid view result")
            runner.require(payload["result_image_sha256"] == pending["sha256"] and payload["result_image_bytes"] == pending["byte_length"], "actual view result differs from complete identified figure")
            pending["result_image_sha256"] = payload["result_image_sha256"]
            pending["stages"].append(stage)
        elif stage == "image_output_delivered":
            runner.require(stages == ["view_invocation", "view_result"], "image display without actual invocation/result receipt")
            runner.require(payload["result_image_sha256"] == pending["result_image_sha256"], "displayed image result mismatch")
            runner.require(payload["display_mechanism"] == "functions.image_then_yield_control" and payload["semantic_inspection_claim"] is False, "invalid/overclaimed display receipt")
            state["cursor"] += 1
            state["pending_figure"] = None
        else:
            runner.require(stages == ["view_invocation"], "view failure out of order")
            runner.require(type(payload["error"]) is str and payload["error"], "missing actual view error")
            # Failure stays pending: it can never be mistaken for a view result.
        runner.append_event(stage, cursor_before=state["cursor"] - (1 if stage == "image_output_delivered" else 0),
                            cursor_after=state["cursor"], **{k: v for k, v in payload.items() if k != "stage"})
        runner.save_state(state)
        return {"ok": True, "stage": stage, "cursor": state["cursor"], "figure_pending": state["pending_figure"] is not None}


def main():
    try:
        runner.require(len(sys.argv) == 2, "adapter receipt requires exactly one encoded payload")
        runner.require(len(sys.argv[1]) <= 32000, "receipt too large")
        payload = runner.unique_json(base64.b64decode(sys.argv[1], validate=True))
        result = record(payload)
        sys.stdout.buffer.write(runner.canonical(result) + b"\n")
        return 0
    except Exception as exc:
        error = str(exc) if isinstance(exc, runner.Denied) else type(exc).__name__ + ": " + str(exc)
        try:
            runner.append_event("receipt_rejected", reason=error)
        except Exception:
            pass
        sys.stderr.buffer.write(runner.canonical({"ok": False, "error": error}) + b"\n")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
