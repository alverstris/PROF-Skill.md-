from pathlib import Path
import json,hashlib
w=Path(__file__).resolve().parents[1];out=w/'publication';prefix='runs/y1-reader-20261008/iterations/008/published-r35-20261012/';H=lambda b:hashlib.sha256(b).hexdigest()
def ident(p,path):
 b=p.read_bytes();return {'local':str(p),'path':path,'bytes':len(b),'sha256':H(b),'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()}
def write(p,d):p.write_text(json.dumps(d,indent=2)+'\n')
a=json.loads((out/'phase-a-mutations.json').read_text());r=json.loads((w/'evidence/release-publication-readback.json').read_text());assert r['all_bytes_match'];q=json.loads((w/'closure/queue.json').read_text());assert sum(s['status']=='closed' for s in q['sessions'])==15
p=w/'.prof-state/RUN.md';p.write_text(p.read_text()+'''\nFinal closure checkpoint: root full gates complete, all original root/reader/technical/preflight evidence archived byte-identically. No verified material teaching failure. Complete r36 metadata-only release c1e31e7528d6d9582ba07aa6b1324e99e4585be9/tree160c39b828ae54399b0eefd819c158146e7bcfff actual81path31,821,947B readback passed;36package907146B/all34declarations and three whole reconstructed archives verified. T1–T12 and all six global helper gates now pass; actual topic/full helper checks MECHANICALLY_READY, not human-learning evidence. Candidate canonical checkpoint closes onlyD008,15accepted61remaining,all147identity/order/readability and146otherrows unchanged. PhaseB publication/readback then cleanD015 handoff throughroot remain. No Git writes after explicit successor transfer.\n''')
fm=[x for x in a if '/future-preparation/' in x['path']];write(w/'evidence/future-preparation-publication-map.json',{'note':'Original future preparation manifests retain their original source-audit-archives locators unchanged. This map supplies actual repository destinations. Semantics remain held for future authors until whole freeze. Reassemble part001 then part002 as raw bytes.','files':[{k:x[k] for k in ['path','bytes','sha256','git_blob']} for x in fm]})
files=[]
for name in ['queue.json','RUN.md','CHANGELOG.md']:files.append(ident(w/'closure'/name,'runs/y1-reader-20261008/'+name))
files.append(ident(w/'closure/closure.md',prefix+'closure.md'))
paths=['evidence/release-publication-readback.json','evidence/helper-topic-final-check.json','evidence/helper-full-final-check.json','evidence/closure-invariants.json','evidence/future-preparation-publication-map.json','.prof-state/manifest.json','.prof-state/topics/approximations.json','.prof-state/RUN.md','author/readback-publication.py','author/build-publication-b.py','publication/phase-a-mutations.json','publication/phase-a-readback-paths.json','publication/phase-a-new-blob-receipts.json','publication/phase-a-publication-receipts.json']
for p in paths:files.append(ident(w/p,prefix+p))
write(out/'phase-b-mutations.json',files)
# The published manifest lists all mutation entries except its own nonrecursive identity.
files.append(ident(out/'phase-b-mutations.json',prefix+'publication/phase-b-mutations.json'))
write(out/'phase-b-all-mutations.json',files)
allpaths={x['path']:x for x in json.loads((out/'phase-a-readback-paths.json').read_text())}
allpaths.update({x['path']:x for x in files});write(out/'phase-b-readback-paths.json',list(allpaths.values()))
print(json.dumps({'mutations':len(files),'full_readback_paths':len(allpaths),'mutation_bytes':sum(x['bytes'] for x in files),'queue_sha256':H((w/'closure/queue.json').read_bytes())}))
