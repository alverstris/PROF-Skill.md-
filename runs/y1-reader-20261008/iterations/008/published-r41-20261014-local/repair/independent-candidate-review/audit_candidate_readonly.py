"""Read-only sealed-candidate identity, template, metadata and runtime audit."""
import collections
import hashlib
import importlib.util
import json
import os
import pathlib
import re
import subprocess
import sys

OUT=pathlib.Path(__file__).resolve().parent
RUN=OUT.parent
C=RUN/'procedure-candidate'
S=C/'synthetic-preflight'
EXPECTED='7679387d9640b65221c959ec314fdd145da419b72389393662933ddd167e65dc'
def sha(b):return hashlib.sha256(b).hexdigest()
def ident(p):
 p=pathlib.Path(p);b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':sha(b)}
def save(name,obj):(OUT/name).write_bytes((json.dumps(obj,ensure_ascii=False,indent=2)+'\n').encode('utf-8'))
assert ident(C/'REVIEW-SEAL.json')['sha256']==EXPECTED
seal=json.loads((C/'REVIEW-SEAL.json').read_bytes())
for name,spec in seal['files'].items():
 actual=ident(C/name);assert actual['bytes']==spec['bytes'] and actual['sha256']==spec['sha256'],name
inventory=json.loads((C/'INVENTORY.json').read_bytes())
actual_paths={x.relative_to(C).as_posix() for x in C.rglob('*') if x.is_file()}
assert actual_paths=={x['path'] for x in inventory['files']}|set(inventory['excluded_self_referential_records'])
before={str(x):ident(x) for x in C.rglob('*') if x.is_file()}
for spec in inventory['files']:
 actual=ident(C/spec['path']);assert actual['bytes']==spec['bytes'] and actual['sha256']==spec['sha256'],spec['path']
assert len(inventory['files'])==inventory['file_count'] and sum(x['bytes'] for x in inventory['files'])==inventory['total_bytes']
carrier=(C/'proposed-package/references/sasis.md').read_bytes().decode('utf-8')
templates=[]
bindings={'__FIXED_ROUTE_FILENAME__':'frozen-route.json','__FIXED_RUNTIME_DIRNAME__':'runtime','__FIXED_SCOPE__':'synthetic r41 retained invoker','__FIXED_ROUTE_ID__':'SYNTHETIC_R41'}
for name in ['invoker_template.js','bootstrap_template.js','short_call_template.js','verify_reuse_template.py']:
 pattern=r'<!-- PROF-READER-TEMPLATE-BEGIN: '+re.escape(name)+r' -->\n```(?:javascript|python)\n(.*?)```\n<!-- PROF-READER-TEMPLATE-END: '+re.escape(name)+r' -->'
 found=re.findall(pattern,carrier,re.S);assert len(found)==1
 raw=found[0].encode('utf-8');assert raw==(C/'templates'/name).read_bytes()==(C/'verified-extracted-templates'/name).read_bytes()
 if name=='verify_reuse_template.py':
  bound=raw.decode('utf-8')
  for k,v in bindings.items():bound=bound.replace(k,v)
  assert bound.encode('utf-8')==(S/'verify_reuse.py').read_bytes()
 else:assert raw==(S/name).read_bytes()
 templates.append({'name':name,'bytes':len(raw),'sha256':sha(raw),'exact_carrier_extraction':True,'exact_tested_template_or_enumerated_binding':True})
old=RUN.parent/'20261014-d008-r40/reader-inputs'
logic=[]
for name,pattern in [('fixed_launcher.py',r'^(CONFIG_PATH|EXPECTED_CONFIG_SHA256|RUNTIME_DIR) = .+$'),('operational_adapter.js',r'^const (PYTHON|LAUNCHER|RECEIPT|ROUTE_SHA256) = .+$'),('record_receipt.py',None),('audit_bound_run.py',None)]:
 a=(old/name).read_text('utf-8');b=(S/name).read_text('utf-8')
 if pattern:a=re.sub(pattern,'<BOUND>',a,flags=re.M);b=re.sub(pattern,'<BOUND>',b,flags=re.M)
 assert a==b,name
 logic.append({'file':name,'same_r40_program_except_enumerated_bindings':True})
core=json.loads((S/'seal-core.json').read_bytes());core_hash=sha((S/'seal-core.json').read_bytes())
assert len(core['files'])==9
for name,spec in core['files'].items():
 x=ident(S/name);assert x['bytes']==spec['bytes'] and x['sha256']==spec['sha256'],name
sys.dont_write_bytecode=True
spec=importlib.util.spec_from_file_location('r41_review_metadata_only',S/'verify_reuse.py')
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
route=json.loads((S/'frozen-route.json').read_bytes())
forbidden={os.path.normcase(os.path.abspath(f['path'])) for f in route['files'].values()}
blocked=[];opens=[];metadata_phase=True
def hook(event,args):
 if event!='open' or not isinstance(args[0],(str,bytes,os.PathLike)):return
 p=os.path.normcase(os.path.abspath(os.fsdecode(args[0])));mode=str(args[1]);flags=args[2] or 0
 if any(c in mode for c in 'wax+') or flags & (os.O_WRONLY|os.O_RDWR|os.O_CREAT|os.O_TRUNC|os.O_APPEND):
  # Review artifacts are the sole permitted write destination.
  if not p.startswith(os.path.normcase(str(OUT))+os.sep):raise RuntimeError('Write denied in candidate metadata review: '+p)
 if metadata_phase:
  if p in forbidden:blocked.append(p);raise RuntimeError('Synthetic subject open denied in metadata proof: '+p)
  opens.append({'path':p,'mode':mode})
sys.addaudithook(hook)
proof=module.proof('bootstrap',core_hash)
metadata_phase=False
assert not blocked and proof['schema']=='prof-reader-reuse-proof-v1' and proof['seal']['schema']=='prof-reader-invoker-store-v1'
assert proof['seal']['invoker_source']==(S/'invoker.js').read_bytes().decode('utf-8')
assert proof['seal']['invoker_sha256']==ident(S/'invoker.js')['sha256']
call=(S/'short_call.js').read_bytes().decode('utf-8')
assert len(call.splitlines())==2 and not any(x in call for x in ['schema','proof','JSON','receipt','exec_command'])
env=os.environ.copy();env['PYTHONDONTWRITEBYTECODE']='1'
p=subprocess.run([core['python'],'-B',str(S/'audit_bound_run.py')],cwd=OUT,env=env,capture_output=True)
assert p.returncode==0 and not p.stderr
audit=json.loads(p.stdout);saved=json.loads((S/'whole-route-audit.json').read_bytes());assert audit==saved
(OUT/'synthetic-whole-route-audit-readback.json').write_bytes(p.stdout)
events=[json.loads(x) for x in (S/'runtime/access.jsonl').read_bytes().splitlines()]
assert len([e for e in events if e['event']=='python_subject_open_audit'])==7
assert [e['requested_step'] for e in events if e['event']=='verified_access_receipt']==['B001','B002','RB001','T001','F001','RB002','T002']
view=[e for e in events if e['event'] in ['view_invocation','view_result','image_output_delivered']]
assert [e['event'] for e in view]==['view_invocation','view_result','image_output_delivered']
figure=next(f for f in route['files'].values() if f['kind']=='teaching_figure')
assert view[1]['result_image_sha256']==figure['sha256'] and view[1]['result_image_bytes']==figure['size'] and view[1]['result_detail']=='original'
assert view[-1]['cursor_before']==3 and view[-1]['cursor_after']==4 and view[-1]['semantic_inspection_claim'] is False
fail=[json.loads(x) for x in (S/'launcher-truncation-runtime/access.jsonl').read_bytes().splitlines()]
assert len([e for e in fail if e['event']=='python_subject_open_audit'])==1 and not any(e['event']=='text_output_delivered' for e in fail)
neg=json.loads((S/'negative-preflight-evidence.json').read_bytes())['negative_checks'];assert len(neg)==32
for e in neg:
 assert e['passed'] and e.get('subject_opens_added',e.get('subject_opens'))==0,e['name']
 assert e.get('view_calls',0)==0,e['name']
 if 'cursor_before' in e:assert e['cursor_before']==e['cursor_after']==3
fig=json.loads((S/'figure-preflight-evidence.json').read_bytes())
assert [x['stage'] for x in fig['figure_checks']]==['full_bytes_staged_before_invocation','invocation_before_actual_result','actual_result_before_image_output','delivered_image_releases_cursor']
assert all(x['passed'] for x in fig['figure_checks'])
after={str(x):ident(x) for x in C.rglob('*') if x.is_file()};assert before==after
save('candidate-procedure-evidence.json',{'review_seal':ident(C/'REVIEW-SEAL.json'),'all_113_candidate_files_match_seal_inventory':True,'inventory_files':inventory['file_count'],'candidate_total_files':len(before),'candidate_source_bytes':sum(x['bytes'] for x in before.values()),'templates':templates,'unchanged_runtime_logic':logic,'metadata_proof_independently_replayed_read_only':True,'metadata_subject_opens':blocked,'metadata_operational_opens':opens,'canonical_proof_and_seal_schemas_distinguished':True,'minimal_call_identity':ident(S/'short_call.js'),'minimal_call_lines':2,'synthetic_route_audit_replayed_matches_sealed_result':True,'actual_runtime_event_counts':dict(collections.Counter(x['event'] for x in events)),'positive_access_sequence':[e['requested_step'] for e in events if e['event']=='verified_access_receipt'],'actual_figure_receipts':view,'negative_cases':neg,'failed_truncation_runtime_has_access_but_no_delivery':True,'candidate_bytes_unchanged_by_review':True,'same_surface_unread_baseline_revisit':'Candidate itself contains only a direct-launcher fresh-runtime negative; parent has required a separate exact two-line fixture before publication. Supplemental review pending.','limits':'No production binding or reader dispatch. Actual original functions.exec call history is represented by sealed harness/evidence plus instrumented runtime; no independent host transcript. This review replays read-only metadata and runtime auditing only, never subject launcher calls.'})
print(json.dumps({'candidate_files':len(before),'template_payloads':len(templates),'core_files':len(core['files']),'metadata_subject_opens':len(blocked),'positive_accesses':len(audit['verified_accesses']),'negative_cases':len(neg),'readonly_route_audit_matches':True,'candidate_unchanged':True},indent=2))
