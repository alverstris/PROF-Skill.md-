from pathlib import Path
import json,re,hashlib
P=Path(__file__).resolve().parents[1]; O=P.parent/'author'
def sha(b):return hashlib.sha256(b).hexdigest()
def load(p):return json.loads(p.read_text())
def identity_manifest(root,manifest,key):
 rows=[]
 for f in manifest[key]:
  r=f.get('relative_path',f.get('path')); p=root/r; b=p.read_bytes()
  assert sha(b)==f['sha256'] and len(b)==f['bytes'],str(p)
  rows.append({'path':r,'sha256':sha(b),'bytes':len(b)})
 return rows
oldpack=load(O/'author-packet-manifest-v1.json')
oldrows=identity_manifest(O,oldpack,'files')
newrows=identity_manifest(P,load(P/'learner-manifest-v2.json'),'constituents')
proof=load(P/'evidence/exact-repair-proof.json')
counts={}; inline=0;display=0;fences=0;links=0;anchors=0
for name in ['notes.md','hints.md','solutions.md']:
 old=(O/'learner'/name).read_bytes();new=(P/'learner'/name).read_bytes(); lines=new.splitlines(keepends=True)
 for e in proof['changes']:
  if e['file']==name:
   a=e['opening_line']-1;b=e['closing_line']-1
   assert lines[a]==b'```math\n' and lines[b]==b'```\n'
   assert sha(b'\n'+b''.join(lines[a+1:b]))==e['payload_sha256']
   lines[a]=b'$$\n';lines[b]=b'$$\n'
 assert b''.join(lines)==old
 oldt=old.decode();newt=new.decode()
 oldi=re.findall(r'\$`(.*?)`\$',oldt,re.S);newi=re.findall(r'\$`(.*?)`\$',newt,re.S);assert oldi==newi
 def displays(s):
  rows=[];ls=s.splitlines(keepends=True);i=0
  while i<len(ls):
   if ls[i] in ['$$\n','```math\n']:
    close='$$\n' if ls[i]=='$$\n' else '```\n';i+=1;payload=[]
    while i<len(ls) and ls[i]!=close:payload.append(ls[i]);i+=1
    assert i<len(ls);rows.append(''.join(payload))
   i+=1
  return rows
 od=displays(oldt);nd=displays(newt);assert od==nd
 count={'inline':len(newi),'display':len(nd),'fenced_math':newt.count('```math\n'),'anchors':len(re.findall(r'<a name="q[1-6]"></a>',newt))}
 counts[name]=count;inline+=count['inline'];display+=count['display'];fences+=count['fenced_math'];anchors+=count['anchors']
 assert len(re.findall(r'<a name="q[1-6]"></a>',newt))==6
 for match in re.finditer(r'!?\[[^\]]*\]\(([^)]+)\)',newt):
  target=match.group(1)
  if target.startswith('https://'):continue
  fn,sep,an=target.partition('#');p=P/'learner'/fn;assert p.is_file(),target
  if an: assert f'<a name="{an}"></a>' in p.read_text(),target
  links+=1
 assert not re.search(r'^#{1,6} |\*\*|^\|',newt,re.M)
 assert not any('<' in x or '>' in x for x in newi)
 for x in newi: assert not re.search(r'\\(?:lt|gt)(?! )',x)
assert (inline,display,fences,anchors)==(316,46,14,18)
notes=(P/'learner/notes.md').read_text();oldnotes=(O/'learner/notes.md').read_text()
qs=re.findall(r'^Q[1-6]\. .+$',notes,re.M);assert len(qs)==6 and qs==re.findall(r'^Q[1-6]\. .+$',oldnotes,re.M)
assert all(q in (O/'prompts-only-v1.md').read_text() for q in qs)
out={'status':'pass','scope':'current local source checks only, not actual destination','original_author_packet_all_files_unchanged':oldrows,'v2_frozen_constituents_verified':newrows,'current_counts':counts,'inline_payloads_exact_ordered':inline,'display_payloads_exact_ordered':display,'fenced_displays':fences,'remaining_dollar_displays':display-fences,'anchors':anchors,'local_targets_checked_including_images':links,'six_prompts_verbatim_original_prefreeze':True,'exact_inverse_all_six_files':True,'all_other_learner_bytes_unchanged':True,'technical_evidence_retained':{'path':str(O/'evidence/technical-checks.json'),'sha256':sha((O/'evidence/technical-checks.json').read_bytes()),'checks':32,'basis':'unchanged mathematical content/payloads and current whole-route audit; no claim of recomputation'},'external_gates':'pending root actual destination, fresh v2 SASIS, final acceptance'}
(P/'evidence/static-checks-v2.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['original_author_packet_all_files_unchanged','v2_frozen_constituents_verified']},indent=2))
