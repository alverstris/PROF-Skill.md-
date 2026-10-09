from pathlib import Path
import json,hashlib,datetime
P=Path(__file__).resolve().parents[1]; OLD=P.parent/'author';L=P/'learner'
def sha(d):return hashlib.sha256(d).hexdigest()
def dump(f,o):
 with f.open('x') as out:out.write(json.dumps(o,indent=2,ensure_ascii=False)+'\n')
original=json.loads((OLD/'learner-manifest-v1.json').read_text());failure=json.loads((OLD/'evidence/destination-failure-map-v1.json').read_text());assert len(failure)==14
expected={'notes.md':[146,177,209,227,252,260,264,284],'solutions.md':[87,128,136,143,161,169]}
changes=[];constituents=[]
for f in original['constituents']:
 rel=Path(f['relative_path']);src=OLD/rel;raw=src.read_bytes();assert sha(raw)==f['sha256'];assert len(raw)==f['bytes'];dest=P/rel;dest.parent.mkdir(parents=True,exist_ok=True)
 entries=[x for x in failure if x['file']==src.name]
 if entries:
  assert sorted(x['source_line'] for x in entries)==expected[src.name]
  lines=raw.splitlines(keepends=True);inverse=lines.copy();boundaries=[]
  for e in sorted(entries,key=lambda x:x['source_line']):
   start=e['source_line']-1;assert lines[start]==b'$$\n';end=start+1
   while lines[end]!=b'$$\n':end+=1
   interior=b''.join(lines[start+1:end]);old_payload=b'\n'+interior;assert old_payload.decode()==e['source']
   lines[start]=b'```math\n';lines[end]=b'```\n';boundaries.append((start,end))
   new_payload=lines[start][len(b'```math'):]+b''.join(lines[start+1:end]);assert new_payload==old_payload
   changes.append({'file':src.name,'opening_line':start+1,'closing_line':end+1,'old_delimiters':['$$','$$'],'new_delimiters':['```math','```'],'payload_bytes_between_delimiter_tokens':len(old_payload),'payload_sha256':sha(old_payload),'verbatim_payload_equal':True,'boundary_rule':'The LF after the opening token and LF before closing token remain exactly as in v1; they are syntax boundaries for a fenced block, not inserted/deleted TeX content. The source comparison includes the leading LF; a parser may exclude that fence-boundary LF, so destination comparison must normalize only this documented syntactic boundary.','interior_bytes_sha256':sha(interior),'v1_source_line_map_agrees':True})
  new=b''.join(lines);back=lines.copy()
  for start,end in boundaries:back[start]=b'$$\n';back[end]=b'$$\n'
  assert b''.join(back)==raw
  assert sum(a!=b for a,b in zip(inverse,lines))==2*len(entries)
  assert len(inverse)==len(lines)
 else:new=raw
 with dest.open('xb') as out:out.write(new)
 constituents.append({'path':str(dest),'relative_path':str(rel),'bytes':len(new),'sha256':sha(new),'lines':len(new.splitlines()) if dest.suffix=='.md' else None,'v1_sha256':sha(raw),'changed':new!=raw})
assert len(changes)==14
assert sum(c['changed'] for c in constituents)==2
proof={'repair_type':'local representation repair, not fresh generation','skill_unchanged':'r23-candidate1','exact_change_count':14,'changed_delimiter_lines':28,'all_tex_payloads_unchanged':True,'all_other_learner_bytes_unchanged':True,'inverse':'For every recorded block replace opening ```math line with $$ and closing ``` line with $$. Reconstructed full files are byte-identical to all six original learner constituents. Assertions executed on raw bytes.','changes':changes}
dump(P/'evidence/exact-repair-proof.json',proof)
man={'revision':'d016-r23-c1-learner-v2-local-repair','frozen_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'immutable':True,'constituents':constituents,'read_order':original['read_order'],'figure_insertions':original['figure_insertions'],'change_scope':'Exactly 14 affected $$ displays converted to fenced math blocks; all TeX payloads and all other learner bytes preserved. Delimiter line lengths change, line count does not.','provenance':'Local repair after original fresh candidate generation and complete v1 review, under unchanged r23-candidate1. Not another fresh generation.','v1_manifest':{'path':str(OLD/'learner-manifest-v1.json'),'sha256':sha((OLD/'learner-manifest-v1.json').read_bytes())},'repair_proof':'evidence/exact-repair-proof.json','pending_gates':['full author current-route re-audit','actual repaired GitHub destination full math and native styling/navigation checks','fresh v2 two-input SASIS','root final acceptance/publication'],'isolation':'Instruction-only subject boundaries; current v1 audits explicitly authorized for local repair.'}
dump(P/'learner-manifest-v2.json',man)
print(json.dumps({'manifest':str(P/'learner-manifest-v2.json'),'bytes':(P/'learner-manifest-v2.json').stat().st_size,'sha256':sha((P/'learner-manifest-v2.json').read_bytes()),'constituents':constituents},indent=2))
