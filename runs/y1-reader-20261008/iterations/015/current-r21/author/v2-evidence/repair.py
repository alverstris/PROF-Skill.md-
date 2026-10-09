from pathlib import Path
import json,hashlib,shutil,re,datetime
E=Path(__file__).resolve().parent; A=E.parent; V=A/'v2'; V.mkdir(exist_ok=False);(V/'assets').mkdir()
def sha(b):return hashlib.sha256(b).hexdigest()
m=json.loads((A/'freeze-manifest-v1.json').read_text());positions=json.loads((A.parent/'destination-v1/all21-comparison-character-positions.json').read_text())
assert len(positions)==21
for x in m['constituents']:assert sha((A/x['path']).read_bytes())==x['sha256']
texts=['teaching.md','hints.md','solutions.md'];records=[];proofs=[]
prose={
 'teaching.md': [('identify the first condition it fails.', 'identify which conditions it fails by checking both the differential equation and the initial condition.')],
 'solutions.md': [('checking the equation first already finds a failure:', 'the differential equation fails:'),('Either check disproves it; there is no unique chronological “first” unless a check order is chosen.','Both required conditions therefore fail; either failure alone would disprove the candidate.')]}
for name in texts:
 raw=(A/name).read_bytes();old=raw.decode();edits=[]
 for p in positions:
  if p['file']!=name:continue
  i=p['character_offset'];assert old[i]==p['source_character'];assert len(old[:i].encode())==p['UTF8_byte_offset']
  replacement='\\lt ' if old[i]=='<' else '\\gt '
  edits.append({'issue':'MATH-1','start':i,'end':i+1,'old':old[i],'new':replacement,'math_ordinal':p['math_ordinal'],'original_line':p['line'],'original_column':p['column']})
 for before,after in prose.get(name,[]):
  assert old.count(before)==1
  i=old.index(before);edits.append({'issue':'SASIS-A1','start':i,'end':i+len(before),'old':before,'new':after})
 edits.sort(key=lambda x:x['start']);new=old;delta=0
 for e in edits:
  e['new_start']=e['start']+delta;e['new_end']=e['new_start']+len(e['new']);delta+=len(e['new'])-len(e['old']);e['original_UTF8_byte_offset']=len(old[:e['start']].encode())
 for e in reversed(edits):new=new[:e['start']]+e['new']+new[e['end']:]
 reverse=new
 for e in reversed(edits):
  assert reverse[e['new_start']:e['new_end']]==e['new'];reverse=reverse[:e['new_start']]+e['old']+reverse[e['new_end']:]
 assert reverse.encode()==raw
 orig_display=re.findall(r'```math\n(.*?)\n```',old,re.S);new_display=re.findall(r'```math\n(.*?)\n```',new,re.S);assert orig_display==new_display
 oi=re.findall(r'\$`(.*?)`\$',old);ni=re.findall(r'\$`(.*?)`\$',new);assert len(oi)==len(ni)
 canonical=[x.replace('\\lt ','<').replace('\\gt ','>') for x in ni];assert canonical==oi
 assert all('<' not in x and '>' not in x for x in ni)
 (V/name).write_bytes(new.encode())
 records.append({'file':name,'original_sha256':sha(raw),'revised_sha256':sha(new.encode()),'edits':edits})
 proofs.append({'file':name,'byte_identical_after_inverse':True,'restored_sha256':sha(reverse.encode()),'all_display_payloads_byte_identical':True,'display_count':len(orig_display),'inline_count':len(oi),'all_inline_math_equal_after_exact_lt_gt_inverse':True,'no_unmapped_inline_comparison_character_remains':True})
for x in m['constituents']:
 if x['path'] not in texts:shutil.copyfile(A/x['path'],V/x['path'])
figures=[{'file':x['path'],'v1_sha256':x['sha256'],'v2_sha256':sha((V/x['path']).read_bytes()),'byte_identical':(A/x['path']).read_bytes()==(V/x['path']).read_bytes()} for x in m['constituents'] if x['path'] not in texts]
assert all(x['byte_identical'] for x in figures)
ledger={'revision':'D015-r21-v2','scope':'Exactly21 mapped inline comparison characters across20 payloads and3 Q5 prose replacements. No other mathematical or figure change.','source_map_sha256':sha((A.parent/'destination-v1/all21-comparison-character-positions.json').read_bytes()),'files':records,'inverse_proofs':proofs,'figures':figures,'total_comparison_character_edits':sum(e['issue']=='MATH-1' for r in records for e in r['edits']),'total_prose_replacements':sum(e['issue']=='SASIS-A1' for r in records for e in r['edits'])}
(E/'edit-inverse-ledger-v2.json').write_text(json.dumps(ledger,indent=2)+'\n')
freeze={'revision':'D015-r21-v2','frozen_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'bundle_root':str(V),'reading_order':['teaching.md including all3figures at placement','hints.md','solutions.md'],'constituents':[{'path':x['path'],'bytes':(V/x['path']).stat().st_size,'sha256':sha((V/x['path']).read_bytes())} for x in m['constituents']],'edit_proof':'../v2-evidence/edit-inverse-ledger-v2.json','limits':['Full revised author audit in progress.','Fresh actual destination, SASIS, and final gates pending root.','No teaching changes authorized after this freeze.']}
(E/'freeze-manifest-v2.json').write_text(json.dumps(freeze,indent=2)+'\n')
print(json.dumps(freeze,indent=2))
