// Run inside functions.exec with tools, load, store and text globals.
// Requires publish_key, publish_workdir, publish_expected, publish_message,
// and <key>_plan [{path,bytes,blob}] computed from exact local bytes.
const key=load('publish_key'),repo='alverstris/PROF-Skill.md-',workdir=load('publish_workdir');
const unwrap=r=>{if(r.isError)throw Error(JSON.stringify(r));let s=r.structuredContent;if(s?.content && typeof s.content==='string')return JSON.parse(s.content);if(s)return s;let t=r.content?.find(x=>x.type==='text')?.text;return JSON.parse(t);};
const branch=unwrap(await tools.mcp__codex_apps__github_fetch({url:'https://api.github.com/repos/'+repo+'/branches/main'}));
if(branch.commit.sha!==load('publish_expected'))throw Error('Unexpected head '+branch.commit.sha);
const tree=unwrap(await tools.mcp__codex_apps__github_fetch({url:'https://api.github.com/repos/'+repo+'/git/trees/'+branch.commit.commit.tree.sha+'?recursive=1'}));
if(tree.truncated)throw Error('Truncated canonical tree');
const existing=new Set(tree.tree.filter(x=>x.type==='blob').map(x=>x.sha));const entries=[];
for(const p of load(key+'_plan')){
 if(tree.tree.find(x=>x.path===p.path)?.sha===p.blob)continue;
 if(!existing.has(p.blob)){
  let b64='';const size=45000;
  for(let offset=0;offset<p.bytes;offset+=size){
   const n=Math.min(size,p.bytes-offset);
   const code="from pathlib import Path\nimport base64\np=Path("+JSON.stringify(p.path)+")\nwith p.open('rb') as f:\n f.seek("+offset+");v=f.read("+n+")\nprint(base64.b64encode(v).decode())\n";
   const result=await tools.exec_command({cmd:"python - <<'PY'\n"+code+'PY',workdir,max_output_tokens:65000});
   if(result.exit_code!==0||result.output.length!==4*Math.ceil(n/3)+1||!/^[-A-Za-z0-9+/=]+\n$/.test(result.output))throw Error('Base64 transfer incomplete '+p.path+' offset '+offset);
   b64+=result.output.trim();
  }
  if(b64.length!==4*Math.ceil(p.bytes/3))throw Error('Base64 total length mismatch');
  const made=unwrap(await tools.mcp__codex_apps__github_create_blob({repository_full_name:repo,content:b64,encoding:'base64'}));
  if(made.sha!==p.blob)throw Error('Created blob mismatch '+p.path+' '+JSON.stringify(made));existing.add(p.blob);
 }
 entries.push({path:p.path,mode:'100644',type:'blob',sha:p.blob});
}
if(!entries.length)throw Error('No changed publication entries');
const madeTree=unwrap(await tools.mcp__codex_apps__github_create_tree({repository_full_name:repo,base_tree_sha:branch.commit.commit.tree.sha,tree_elements:entries}));
const madeCommit=unwrap(await tools.mcp__codex_apps__github_create_commit({repository_full_name:repo,parent_sha:branch.commit.sha,tree_sha:madeTree.sha,message:load('publish_message')}));
store(key+'_tree',madeTree.sha);store(key+'_commit',madeCommit.sha);store(key+'_entries',entries);
text(await tools.mcp__codex_apps__github_update_ref({repository_full_name:repo,branch_name:'main',expected_sha:branch.commit.sha,force:false,sha:madeCommit.sha}));
text({changed:entries.length,commit:madeCommit.sha,tree:madeTree.sha});
