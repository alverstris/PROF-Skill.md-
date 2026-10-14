// Orchestrator-only synthetic probes. Never a reader command or real reader dispatch.
const ROOT = "C:/Users/alver/.codex/.chatgpt-projects/g-p-6aa4088af61c8191a4b578a4310457ae/.prof-sasis/20261014-d008-r40/reader-preparation/synthetic-preflight-r40";
const PY = "C:/Users/alver/AppData/Local/Programs/Python/Python314/python.exe";
const KEY = "prof.reader.d008.r40.synthetic.preflight1";
const actual = tools;
const source = load("reuse.short-source");
const bootstrap = load("reuse.bootstrap-source");
const original = load(KEY);
const evidence = load(KEY + ".evidence");
evidence.negative_checks = [];
async function support(mode, name) {
  const r = await actual.exec_command({cmd: "& '" + PY + "' '" + ROOT + "/preflight_support.py' '" + mode + "'" + (name ? " '" + name + "'" : ""), max_output_tokens: 12000});
  if(r.exit_code !== 0 || r.session_id) throw Error(r.output);
  return JSON.parse(r.output.trim());
}
async function test(name, stepValue, setup, options = {}) {
  if(setup) await setup();
  const before = await support("snapshot");
  let launcherCalls = 0, viewCalls = 0, error = null;
  const wrapped = {
    exec_command: async args => {
      if(args.cmd.includes("/fixed_launcher.py'")) launcherCalls++;
      const r = await actual.exec_command(args);
      if(options.truncateVerifier && args.cmd.includes("/verify_reuse.py'")) return {...r, output:r.output.slice(0,150)};
      return r;
    },
    view_image: async args => { viewCalls++; return await actual.view_image(args); }
  };
  const call = options.bootstrap ? bootstrap : source.replace('const STEP_ID = "B001";', "const STEP_ID = " + JSON.stringify(stepValue) + ";");
  try { await eval("(async function(tools){\n" + call + "\n})(wrapped)"); }
  catch(err) { error = String(err); }
  const after = await support("snapshot");
  const passed = error !== null && JSON.stringify(before.state) === JSON.stringify(after.state) && after.subject_open_audit_count === before.subject_open_audit_count && viewCalls === 0 && (options.allowLauncher ? launcherCalls === 1 : launcherCalls === 0);
  const row={name,passed,error,launcher_calls:launcherCalls,view_calls:viewCalls,subject_opens_added:after.subject_open_audit_count-before.subject_open_audit_count,cursor_before:before.state?.cursor??null,cursor_after:after.state?.cursor??null};
  evidence.negative_checks.push(row);
  store(KEY + ".evidence", evidence);
  store(KEY, original); // Explicit synthetic test cleanup; reader recovery is never automatic.
  if(!passed) throw Error("Negative preflight failed: "+name+" "+JSON.stringify(row));
}
await test("bootstrap_cannot_be_repeated", "B001", null, {bootstrap:true});
for(const value of ["", "C:/synthetic-unpermitted.txt", "B001' ; throw 'injection", "B001\nT001", ["B001","C:/synthetic-unpermitted.txt"], {STEP_ID:"B001",subject_path:"C:/synthetic-unpermitted.txt"}, 4, null]) {
  await test("invalid_STEP_ID_"+JSON.stringify(value), value);
}
await test("missing_store", "F001", async()=>store(KEY,null));
await test("stale_binding_store", "F001", async()=>store(KEY,{...original,binding_sha256:"0".repeat(64)}));
await test("stale_route_store", "F001", async()=>store(KEY,{...original,route_sha256:"0".repeat(64)}));
await test("extra_subject_path_in_store", "F001", async()=>store(KEY,{...original,subject_path:"C:/synthetic-unpermitted.txt"}));
await test("corrupted_cached_operational_code", "F001", async()=>store(KEY,{...original,adapter_source:original.adapter_source.replace("0x391c0cb3","0x682e6ff3")}));
await test("truncated_identity_proof", "F001", null, {truncateVerifier:true});
await test("changed_valid_STEP_ID_skip_figure", "T002", null, {allowLauncher:true});
await test("changed_valid_STEP_ID_unknown", "UNKNOWN", null, {allowLauncher:true});
for(const name of ["operational_adapter.js","fixed_launcher.py","record_receipt.py","verify_reuse.py","frozen-route.json","bootstrap.js","short_call.js","reader-operating.md","seal-core.json"]) {
  await support("mutate",name);
  try { await test("changed_disk_"+name, "F001"); }
  finally { await support("restore",name); }
}
// Independently reproduce the reported wrong k-array segment against synthetic bound code only.
const correct = "0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,0x748f82ee";
const changed = "0x2748774c,0x34b0bcb5,0x682e6ff3,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x748f82ee";
if(original.adapter_source.split(correct).length!==2) throw Error("Synthetic reproduction segment count mismatch");
let stubCalls = 0, selfError = null;
const stub = {exec_command:async()=>{stubCalls++;throw Error("unexpected launcher call");},view_image:async()=>{stubCalls++;throw Error("unexpected view call");}};
try { await eval("(async function(tools,STEP_ID){\n"+original.adapter_source.replace(correct,changed)+"\n})(stub,'T002')"); }
catch(err) {selfError=String(err);}
const reproduction={name:"independent_wrong_k_segment_synthetic_reproduction",passed:selfError?.includes("adapter hash self-check failed")&&stubCalls===0,error:selfError,stub_tool_calls:stubCalls,original_departed_reader_call:false,subject_opens:0};
evidence.negative_checks.push(reproduction);
if(!reproduction.passed)throw Error("Wrong-segment reproduction failed");
evidence.negative_checks_passed=evidence.negative_checks.every(x=>x.passed);
store(KEY+".evidence",evidence);
await actual.apply_patch("*** Begin Patch\n*** Add File: "+ROOT+"/negative-preflight-evidence.json\n+"+JSON.stringify(evidence,null,2).replace(/\n/g,"\n+")+"\n*** End Patch");
text({negative_checks:evidence.negative_checks.length,passed:evidence.negative_checks_passed,original_r39_untouched:true,synthetic_only:true});
