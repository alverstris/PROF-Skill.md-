"""Final message/identity readback; metadata and operational code only."""
import hashlib,json,re,shutil
from pathlib import Path
P=Path(__file__).resolve().parent
R=P.parent/"reader-inputs"
def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,x):p.write_text(json.dumps(x,indent=2)+"\n",encoding="utf-8")
route=json.loads((R/"frozen-route.json").read_text())
core=json.loads((R/"seal-core.json").read_text())
summary=json.loads((P/"production-binding-summary.json").read_text())
report=str(P.parent/"reader-report-original.md").replace("\\","/")
message=(P/"dispatch_authorization_template.md").read_text()
values={"FROZEN_BASELINE_ID_AND_REVISION":"OCR-A-4-subjects-r1 / frozen-operational-20261007","FROZEN_TEACHING_ID_AND_REVISION":"D008-r40-fresh-author-1 / "+route["revision"],"BOUND_BOOTSTRAP_SHA256":h(R/"bootstrap.js"),"EXACT_BOUND_BOOTSTRAP_BODY":(R/"bootstrap.js").read_text(),"BOUND_SHORT_CALL_SHA256":h(R/"short_call.js"),"EXACT_BOUND_SHORT_CALL_BODY":(R/"short_call.js").read_text(),"SUBJECT_FREE_ROUTE_DELIVERY_OR_IMMUTABLE_LOCATOR":"Complete route metadata is inline below; do not issue a separate metadata-read command.\n\n```json\n"+(R/"frozen-route.json").read_text()+"```","READER_REPORT_DESTINATION":report}
for k,v in values.items():message=message.replace("{{"+k+"}}",v)
assert "{{" not in message
blocks=re.findall(r'^```(?:javascript|json)\n(.*?)^```\s*$',message,re.M|re.S)
assert len(blocks)==3
assert blocks[0].rstrip("\n")== (R/"bootstrap.js").read_text().rstrip("\n")
assert blocks[1].rstrip("\n")== (R/"short_call.js").read_text().rstrip("\n")
assert json.loads(blocks[2])==route
backup=R/"reader-launch-message-before-route-format-readback.txt"
assert not backup.exists()
shutil.copyfile(R/"reader-launch-message.txt",backup)
(R/"reader-launch-message.txt").write_text(message,encoding="utf-8",newline="\n")
summary.update(launch_message_sha256=h(R/"reader-launch-message.txt"),launch_message_bytes=(R/"reader-launch-message.txt").stat().st_size,launch_message_exact_code_blocks_and_complete_route_readback=True)
save(P/"production-binding-summary.json",summary)
state=json.loads((P/"binding-state.json").read_text())
state.update(fixed_launcher_identity=h(R/"fixed_launcher.py"),fixed_receipt_identity=h(R/"record_receipt.py"),operational_adapter_identity=h(R/"operational_adapter.js"),bound_verifier_identity=h(R/"verify_reuse.py"),reader_report_destination=report,launch_message_identity=summary["launch_message_sha256"])
state["frozen_teaching_identity"]["files"]={k:v for k,v in route["files"].items() if k!="BASELINE"}
save(P/"binding-state.json",state)
save(P/"launch-message-readback.json",{"passed":True,"exact_bootstrap_code_body":True,"exact_short_call_code_body":True,"inline_route_json_matches_complete_frozen_route":True,"separate_arbitrary_metadata_read_required":False,"launch_message_sha256":summary["launch_message_sha256"],"production_runtime_exists":(R/"runtime").exists(),"subject_bytes_read_by_this_check":False,"reader_dispatched":False})
for folder,name in ((R,"binding-inventory.json"),(P,"INVENTORY.json")):
 save(folder/name,{"files":{str(p.relative_to(folder)).replace("\\","/"):{"bytes":p.stat().st_size,"sha256":h(p)} for p in folder.rglob("*") if p.is_file() and "__pycache__" not in p.parts and p.name!=name},"scope":"Production bindings and separate synthetic evidence, pending root review and actual reader admission"})
print(json.dumps({"launch_message_sha256":summary["launch_message_sha256"],"bytes":summary["launch_message_bytes"],"exact_three_blocks_verified":True,"production_runtime_exists":(R/"runtime").exists()}))
