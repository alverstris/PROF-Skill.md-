// Orchestrator-only synthetic transport failure. Preserve both success and failed runtimes.
const ROOT="C:/Users/alver/.codex/.chatgpt-projects/g-p-6aa4088af61c8191a4b578a4310457ae/.prof-sasis/20261014-d008-r40/reader-preparation/synthetic-preflight-r40";
const PY="C:/Users/alver/AppData/Local/Programs/Python/Python314/python.exe";
const actual=tools;
async function support(mode,name){
 const r=await actual.exec_command({cmd:"& '"+PY+"' '"+ROOT+"/preflight_support.py' '"+mode+"'"+(name?" '"+name+"'":""),max_output_tokens:12000});
 if(r.exit_code!==0||r.session_id)throw Error(r.output);
 return JSON.parse(r.output.trim());
}
await support("archive-runtime","successful-runtime");
const wrapped={exec_command:async args=>{const r=await actual.exec_command(args);return args.cmd.includes("/fixed_launcher.py'")?{...r,output:r.output.slice(0,120)}:r;},view_image:actual.view_image};
let error=null;
try {await eval("(async function(tools){\n"+load("reuse.short-source")+"\n})(wrapped)");}catch(err){error=String(err);}
const failed=await support("snapshot");
const passed=error?.includes("launcher output missing/truncated")&&failed.state.cursor===1&&failed.subject_open_audit_count===1&&failed.verified_access_count===1&&!failed.events.some(x=>x.event==="text_output_delivered");
const record={name:"actual_launcher_output_truncation",passed,error,state:failed.state,subject_open_audit_count:failed.subject_open_audit_count,verified_access_count:failed.verified_access_count,text_output_delivered:false,failure_runtime_preserved:"launcher-truncation-runtime",reader_recovery_allowed:false,synthetic_orchestrator_cleanup_only:true};
await support("archive-runtime","launcher-truncation-runtime");
await support("restore-success-runtime");
await actual.apply_patch("*** Begin Patch\n*** Add File: "+ROOT+"/launcher-truncation-evidence.json\n+"+JSON.stringify(record,null,2).replace(/\n/g,"\n+")+"\n*** End Patch");
if(!passed)throw Error("Launcher truncation preflight failed");
text(record);
