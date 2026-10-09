from pathlib import Path
import hashlib,json,re,difflib,datetime
p=Path(__file__).resolve().parent
sha=lambda b:hashlib.sha256(b).hexdigest()
original=(p/'learner-v1.md').read_bytes();assert sha(original)=='4af6ed4369de2cc322f2d1022fdc05071a5355d05f4cf8df52d3fc343baf7364'
s=original.decode('utf-8')
math_re=re.compile(r'\$\$(.*?)\$\$|(?<!\$)\$(?!\$)([^\n$]*)\$(?!\$)',re.S)
nodes=list(math_re.finditer(s));assert len(nodes)==214
changes=[];nraw=0

def replacement(m):
 global nraw
 if m.group(1) is not None:return m.group(0)
 before=m.group(2)
 after=before.replace('<',r'\lt ').replace('>',r'\gt ')
 if before!=after:
  assert r'\lt ' not in before and r'\gt ' not in before
  changes.append({'math_ordinal_1based':next(i+1 for i,z in enumerate(nodes) if z.start()==m.start()),'source_line':s.count('\n',0,m.start())+1,'before':before,'after':after,'comparison_count':before.count('<')+before.count('>')})
  nraw+=before.count('<')+before.count('>')
 return '$'+after+'$'
changed=math_re.sub(replacement,s)
assert len(changes)==48 and nraw==58
prose_changes=[
 ('it is the limit of nearby secant slopes as their two inputs approach one another.','it is the limit of secant slopes with one input fixed at c while the other approaches c.'),
 ('the black points are their outputs on the curve.','the black points pair each input with its output on the curve.'),
 ('The tangent equation is','The equation matching the tangent slope to the secant slope is')
]
for before,after in prose_changes:
 assert changed.count(before)==1
 changed=changed.replace(before,after)
result=changed.encode('utf-8')
newnodes=list(math_re.finditer(changed));assert len(newnodes)==214
assert sum(n.group(1) is not None for n in newnodes)==24
assert sum(n.group(2) is not None for n in newnodes)==190
for old,new in zip(nodes,newnodes):
 if old.group(1) is not None:assert old.group(0)==new.group(0)
 else:
  expected=old.group(2).replace('<',r'\lt ').replace('>',r'\gt ')
  assert new.group(2)==expected
  assert '<' not in new.group(2) and '>' not in new.group(2)
  assert r'\\lt' not in new.group(2) and r'\\gt' not in new.group(2)
# Invert only the authorized operator encodings and three exact phrase changes.
def invert(m):
 if m.group(1) is not None:return m.group(0)
 return '$'+m.group(2).replace(r'\lt ','<').replace(r'\gt ','>')+'$'
inverse=math_re.sub(invert,changed)
for before,after in reversed(prose_changes):
 assert inverse.count(after)==1
 inverse=inverse.replace(after,before)
assert inverse.encode('utf-8')==original
prompts=(p/'prompts-only-v1.md').read_text()
for i in range(1,7):
 q=prompts.split(f'Task P{i}\n\n',1)[1]
 if i<6:q=q.split(f'\n\nTask P{i+1}',1)[0]
 assert f'Task P{i}\n\n'+q.rstrip() in changed
oldpacket=json.loads((p/'packet-manifest-v1.json').read_text())
for z in oldpacket['constituents']:
 f=p/z['path'];assert len(f.read_bytes())==z['bytes'] and sha(f.read_bytes())==z['sha256']
old_inventory=json.loads((p/'author-manifest-v1.json').read_text())
for z in old_inventory['files']:
 f=p/z['path'];assert len(f.read_bytes())==z['bytes'] and sha(f.read_bytes())==z['sha256']
anchors=re.findall(r'<a id="([^"]+)"></a>',changed);links=re.findall(r'\]\(#([^\)]+)\)',changed)
assert len(anchors)==27 and len(links)==37 and len(set(anchors))==27 and set(links)<=set(anchors)
assert anchors==re.findall(r'<a id="([^"]+)"></a>',s) and links==re.findall(r'\]\(#([^\)]+)\)',s)
assert changed.count('\n')==s.count('\n')==326
assert not re.search(r'(?m)^#{1,6}\s|\*\*|__|(?<!\*)\*(?!\*)',changed)
# This script is one-shot and refuses to overwrite a frozen v2.
for fn in ['learner-v2.md','packet-manifest-v2.json','v2-local-check-results.json','v1-to-v2.diff']:
 assert not (p/fn).exists(),f'{fn} already exists; no frozen overwrite permitted'
(p/'learner-v2.md').write_bytes(result)
(p/'v1-to-v2.diff').write_text(''.join(difflib.unified_diff(s.splitlines(True),changed.splitlines(True),fromfile='learner-v1.md',tofile='learner-v2.md')))
packet={'revision':'D013-current-r19-learner-v2','frozen_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'root_markdown':'learner-v2.md','instruction':'Frozen consolidated local repair. All v1 originals and all six figure bytes preserved. Fresh SASIS and actual destination checks pending.','incoming_skill':{'version':'2026-10-09-r19','sha256':'9a40f31312855aed26f5ad78227e509a3401600e351bf4690c5d7c9f9cf5fa23'},'constituents':[{'path':'learner-v2.md','bytes':len(result),'sha256':sha(result),'role':'core and all tasks/help'}]+oldpacket['constituents'][1:]}
(p/'packet-manifest-v2.json').write_text(json.dumps(packet,indent=2)+'\n')
report={'v1_sha256':sha(original),'v2_sha256':sha(result),'v2_bytes':len(result),'inline_nodes':190,'display_nodes':24,'all_math_nodes':214,'changed_inline_nodes':len(changes),'changed_comparison_characters':nraw,'unchanged_inline_nodes':142,'unchanged_display_nodes':24,'prose_changes':[{'before':a,'after':b} for a,b in prose_changes],'math_changes':changes,'inverse_reconstruction_exact_bytes':True,'inverse_reconstruction_sha256':sha(inverse.encode()),'six_prompts_exact':True,'all_v1_inventory_files_unchanged':True,'all_six_figures_unchanged':True,'source_anchor_count':27,'source_link_count':37,'source_navigation_unchanged':True,'new_helper_state_created':False,'original_pending_helper_unchanged':True,'limits':'These are local exact-change, inverse-equivalence and structural checks. No actual destination/parser/render/navigation acceptance or fresh SASIS acceptance is claimed. Live browser clicks remain unobserved.'}
(p/'v2-local-check-results.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k not in ['math_changes','prose_changes']},indent=2))
