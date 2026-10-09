const key=load('verify_key'),repo='alverstris/PROF-Skill.md-',commit=load(key+'_commit');
const b=JSON.parse((await tools.mcp__codex_apps__github_fetch({url:'https://api.github.com/repos/'+repo+'/branches/main'})).structuredContent.content);
if(b.commit.sha!==commit)throw Error('Canonical head changed: '+b.commit.sha);
const t=JSON.parse((await tools.mcp__codex_apps__github_fetch({url:'https://api.github.com/repos/'+repo+'/git/trees/'+b.commit.commit.tree.sha+'?recursive=1'})).structuredContent.content);
if(t.truncated||!load(key+'_plan').every(p=>t.tree.find(x=>x.path===p.path)?.sha===p.blob))throw Error('Published tree mismatch');
store('latest_verified_tree',t);text({commit,tree:b.commit.commit.tree.sha,local_blob_matches:load(key+'_plan').length});
const result=await tools.exec_command({cmd:'git fetch origin main',workdir:load('publish_workdir'),max_output_tokens:1000});
if(result.exit_code!==0)throw Error('Fetch failed');text(result);
// Caller must additionally compare git show COMMIT:path bytes to every plan file.
