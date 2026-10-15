// Exact saved failed call, exercised only with synthetic proof/tool stubs.
const ROOT="C:/Users/alver/.codex/.chatgpt-projects/g-p-6aa4088af61c8191a4b578a4310457ae/.prof-sasis/20261014-d008-r41/procedure-candidate";
const r=await tools.exec_command({cmd:"[Console]::Out.Write([IO.File]::ReadAllText('"+ROOT+"/failure-evidence/exact-failed-call.js'))",max_output_tokens:6000});
if(r.exit_code!==0)throw Error(r.output);
const failed=r.output;
const marker='p.schema !== "prof-reader-reuse-store-v1"';
if(failed.split(marker).length!==2)throw Error("Exact observed proof guard occurrence mismatch");
const cached={schema:"prof-reader-reuse-store-v1",binding_sha256:"bdfd374e597b3dd936c9f6b6915eec97c1168e816453a12d7a88b303cc7d8184",adapter_source:'throw new Error("synthetic adapter reached after correct proof guard");'};
const loader=()=>cached;
const records=[];
for(const [label,code] of [["exact_original_failed_guard",failed],["only_proof_schema_corrected_diagnostic",failed.replace(marker,'p.schema !== "prof-reader-reuse-proof-v1"')]]){
 let metadataStubCalls=0,viewCalls=0,error=null;
 const stub={exec_command:async()=>{metadataStubCalls++;return{exit_code:0,output:JSON.stringify({schema:"prof-reader-reuse-proof-v1",mode:"step",step_id:"B0024",seal:cached})};},view_image:async()=>{viewCalls++;throw Error("unpermitted synthetic view");}};
 try{await eval("(async function(tools,load){\n"+code+"\n})(stub,loader)");}catch(e){error=String(e);}
 records.push({label,error,metadata_stub_calls:metadataStubCalls,actual_launcher_calls:0,view_calls:viewCalls,subject_opens:0,adapter_reached:error?.includes("synthetic adapter reached")===true});
}
const passed=records[0].error?.includes("cached adapter/binding identity mismatch")&&records[0].adapter_reached===false&&records[1].adapter_reached===true&&records.every(x=>x.metadata_stub_calls===1&&x.view_calls===0);
const result={passed,records,scope:"Independent synthetic reproduction of the exact saved r40 failed call. No production verifier, launcher, subject or runtime used; the corrected variant is diagnostic only, never a retry."};
await tools.apply_patch("*** Begin Patch\n*** Add File: "+ROOT+"/failure-evidence/schema-copy-synthetic-reproduction.json\n+"+JSON.stringify(result,null,2).replace(/\n/g,"\n+")+"\n*** End Patch");
if(!passed)throw Error("Observed schema-copy reproduction failed");
text(result);
