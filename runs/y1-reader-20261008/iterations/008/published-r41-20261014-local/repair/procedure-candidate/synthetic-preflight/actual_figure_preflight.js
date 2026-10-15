// Orchestrator-only real-tool synthetic figure test. The short-call source is unchanged except STEP_ID.
const ROOT="C:/Users/alver/.codex/.chatgpt-projects/g-p-6aa4088af61c8191a4b578a4310457ae/.prof-sasis/20261014-d008-r41/procedure-candidate/synthetic-preflight";
const PY="C:/Users/alver/AppData/Local/Programs/Python/Python314/python.exe";
const KEY="prof.reader.r41.synthetic.invoker1";
const actual=tools;
const evidence=load(KEY+".evidence");
evidence.figure_checks=[];
async function snapshot(){
  const r=await actual.exec_command({cmd:"& '"+PY+"' '"+ROOT+"/preflight_support.py' 'snapshot'",max_output_tokens:15000});
  if(r.exit_code!==0||r.session_id)throw Error(r.output);
  return JSON.parse(r.output.trim());
}
async function probe(stage){
  const before=await snapshot();
  const denied=await actual.exec_command({cmd:"& '"+PY+"' '"+ROOT+"/fixed_launcher.py' 'T002'",max_output_tokens:1500});
  const after=await snapshot();
  const passed=denied.exit_code!==0&&!denied.session_id&&before.state.cursor===3&&after.state.cursor===3&&JSON.stringify(before.state)===JSON.stringify(after.state)&&before.subject_open_audit_count===after.subject_open_audit_count;
  evidence.figure_checks.push({stage,passed,exit_code:denied.exit_code,error:denied.output.trim(),subject_opens_added:after.subject_open_audit_count-before.subject_open_audit_count,stages:after.state.pending_figure.stages,cursor:after.state.cursor});
  if(!passed)throw Error("Figure bypass test failed: "+stage);
}
const wrapped={
  exec_command:async args=>{
    const r=await actual.exec_command(args);
    if(args.cmd.includes("/fixed_launcher.py' 'F001'")&&r.exit_code===0)await probe("full_bytes_staged_before_invocation");
    if(args.cmd.includes("/record_receipt.py'")&&r.exit_code===0){
      const receipt=JSON.parse(r.output.trim());
      if(receipt.stage==="view_invocation")await probe("invocation_before_actual_result");
      if(receipt.stage==="view_result")await probe("actual_result_before_image_output");
      if(receipt.stage==="image_output_delivered"){
        const final=await snapshot();
        const passed=final.state.cursor===4&&final.state.pending_figure===null;
        evidence.figure_checks.push({stage:"delivered_image_releases_cursor",passed,cursor:final.state.cursor});
        if(!passed)throw Error("Actual image delivery did not release figure");
      }
    }
    return r;
  },
  view_image:async args=>{
    evidence.actual_tool_events.push({event:"functions.view_image_invoked",path:args.path,detail:args.detail,time:new Date().toISOString()});
    const r=await actual.view_image(args);
    evidence.actual_tool_events.push({event:"functions.view_image_returned",detail:r.detail,transport_mime:r.image_url?.slice(5,r.image_url.indexOf(";")),time:new Date().toISOString()});
    return r;
  }
};
const source=load("reuse.short-source").replace('const STEP_ID = "B001";', 'const STEP_ID = "F001";');
await eval("(async function(tools){\n"+source+"\n})(wrapped)");
evidence.figure_checks_passed=evidence.figure_checks.every(x=>x.passed);
store(KEY+".evidence",evidence);
await actual.apply_patch("*** Begin Patch\n*** Add File: "+ROOT+"/figure-preflight-evidence.json\n+"+JSON.stringify(evidence,null,2).replace(/\n/g,"\n+")+"\n*** End Patch");
text({figure_checks:evidence.figure_checks.length,passed:evidence.figure_checks_passed,actual_view_tool_events:evidence.actual_tool_events.length,semantic_inspection_claim:false});
