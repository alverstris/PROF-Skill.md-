"""Independent read-only audit of a terminal reader prefix and preserved report."""
import collections
import datetime
import difflib
import hashlib
import json
import os
import pathlib
import re
import subprocess
import sys

OUT=pathlib.Path(__file__).resolve().parent
RUN=OUT.parent
INPUT=RUN/'reader-inputs'
sys.stdout.reconfigure(encoding='utf-8')
def sha(b): return hashlib.sha256(b).hexdigest()
def ident(p):
    p=pathlib.Path(p);b=p.read_bytes()
    return {'path':str(p),'bytes':len(b),'sha256':sha(b)}
def write(name,obj):
    (OUT/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def norm(p):return os.path.normcase(os.path.abspath(p))

report_path=RUN/'reader-report-original.md'
comparison_path=RUN/'reader-report-preservation/comparison.md'
report=report_path.read_text('utf-8')
comparison=comparison_path.read_text('utf-8')
route_path=INPUT/'frozen-route.json'
route=json.loads(route_path.read_text('utf-8'))
core=json.loads((INPUT/'seal-core.json').read_text('utf-8'))
inventory=json.loads((INPUT/'binding-inventory.json').read_text('utf-8'))
ledger_path=INPUT/'runtime/access.jsonl'
state_path=INPUT/'runtime/state.json'
events=[json.loads(x) for x in ledger_path.read_bytes().splitlines()]
state=json.loads(state_path.read_text('utf-8'))

checks=[]
def ck(name,a,b):
    ok=a==b
    checks.append({'check':name,'actual':a,'expected':b,'pass':ok})
    if not ok: raise AssertionError(name)
ck('saved report identity attested by preservation comparison',ident(report_path)['sha256'],'e3ebb4470b0d91e149e13ca3d4e564986ec1804be8e3690cf70df285431ba749')
ck('preservation text identifies actual saved report hash',ident(report_path)['sha256'] in comparison,True)
ck('decoded report character count',len(report),9701)
ck('route identity',ident(route_path)['sha256'],'940bb751e8f8146ab41747c79ae20132929d1b7155cb8663cd5c113c90ff49dc')
ck('sealed core identity',ident(INPUT/'seal-core.json')['sha256'],'bdfd374e597b3dd936c9f6b6915eec97c1168e816453a12d7a88b303cc7d8184')

immutable=[]
for name,want in inventory['files'].items():
    actual=ident(INPUT/name)
    ck('binding inventory '+name+' bytes',actual['bytes'],want['bytes'])
    ck('binding inventory '+name+' sha256',actual['sha256'],want['sha256'])
    immutable.append(actual)
for name,want in core['files'].items():
    actual=ident(INPUT/name)
    ck('core '+name+' bytes',actual['bytes'],want['bytes'])
    ck('core '+name+' sha256',actual['sha256'],want['sha256'])
subject_bytes={}
for file_id,spec in route['files'].items():
    data=pathlib.Path(spec['path']).read_bytes()
    ck('route input '+file_id+' bytes',len(data),spec['size'])
    ck('route input '+file_id+' SHA256',sha(data),spec['sha256'])
    subject_bytes[file_id]=data
for step in route['steps']:
    data=subject_bytes[step['file_id']][step['start']:step['start']+step['length']]
    ck('route slice '+step['id']+' exact extent',len(data),step['length'])
    ck('route slice '+step['id']+' exact hash',sha(data),step['sha256'])

expected_kinds=['subject_open_attempt','python_subject_open_audit','subject_open_succeeded','bounded_bytes_read','verified_access_receipt','launcher_output_prepared','text_output_delivered']
ck('runtime event count',len(events),23*len(expected_kinds))
ck('state cursor',state['cursor'],23)
ck('state route SHA256',state['route_sha256'],ident(route_path)['sha256'])
ck('state pending figure',state['pending_figure'],None)
ck('state baseline prefix',state['baseline_read'],[s['id'] for s in route['steps'][:23]])
prefix=[]
position=0
for i in range(23):
    s=route['steps'][i]
    group=events[i*7:(i+1)*7]
    ck(s['id']+' event sequence',[x['event'] for x in group],expected_kinds)
    ck(s['id']+' scheduled file',s['file_id'],'BASELINE')
    ck(s['id']+' contiguous start',s['start'],position)
    for x in group:
        ck(s['id']+' '+x['event']+' route hash',x['route_sha256'],ident(route_path)['sha256'])
    attempt,opened,succeeded,read,receipt,prepared,delivered=group
    for x in [attempt,succeeded,read,receipt,prepared]:ck(s['id']+' '+x['event']+' requested step',x['requested_step'],s['id'])
    for x in [attempt,succeeded,read,receipt]:ck(s['id']+' '+x['event']+' target step',x['target_step'],s['id'])
    ck(s['id']+' attempt cursor',attempt['cursor'],i)
    ck(s['id']+' actual audited open path',norm(opened['path']),norm(route['files']['BASELINE']['path']))
    ck(s['id']+' read file',read['file_id'],'BASELINE')
    for k,want in [('start',s['start']),('requested_length',s['length']),('actual_length',s['length']),('end',s['start']+s['length']),('sha256',s['sha256'])]:ck(s['id']+' bounded read '+k,read[k],want)
    for k,want in [('file_id','BASELINE'),('start',s['start']),('byte_length',s['length']),('sha256',s['sha256']),('baseline_revisit',False),('cursor_before',i),('cursor_after',i+1),('figure_pending',False)]:ck(s['id']+' access receipt '+k,receipt[k],want)
    for x in [prepared,delivered]:
        ck(s['id']+' '+x['event']+' byte count',x['byte_length'],s['length'])
        ck(s['id']+' '+x['event']+' SHA256',x['sha256'],s['sha256'])
    ck(s['id']+' displayed step',delivered['step_id'],s['id'])
    ck(s['id']+' display mechanism',delivered['display_mechanism'],'functions.text_then_yield_control')
    position += s['length']
    prefix.append({'step_id':s['id'],'start':s['start'],'length':s['length'],'end':position,'sha256':s['sha256'],'ledger_indices':list(range(i*7,(i+1)*7)),'audited_open':opened,'access_receipt':receipt,'display_receipt':delivered})
ck('baseline bytes prefix',position,124245)
ck('timestamp monotonicity',[x['time_utc'] for x in events],sorted(x['time_utc'] for x in events))
rows=re.findall(r'^\| (B\d{4}) \| (\d+) \| (\d+) \| `([a-f0-9]{64})` \| (\d+) \|$',report,re.M)
ck('reader report prefix table size',len(rows),23)
for row,p in zip(rows,prefix):
    ck(p['step_id']+' preserved report row',row[:4],(p['step_id'],str(p['start']),str(p['length']),p['sha256']))
ck('no logged teaching file reads',[x['file_id'] for x in events if x['event']=='bounded_bytes_read'],['BASELINE']*23)
ck('no logged figure events',[x for x in events if x['event'] in ['view_invocation','view_result','image_output_delivered','view_failed','bounded_cache_verified']],[])
ck('no logged revisit',[x for x in events if x.get('baseline_revisit') is True],[])
ck('no logged B0024 subject event',[x for x in events if x.get('requested_step')=='B0024' or x.get('step_id')=='B0024'],[])

authorized=(INPUT/'short_call.js').read_text('utf-8').replace('const STEP_ID = "B0001";','const STEP_ID = "B0024";',1)
reported=re.search(r'```javascript\n(.*?)\n```',report,re.S).group(1)+'\n'
diff=''.join(difflib.unified_diff(authorized.splitlines(keepends=True),reported.splitlines(keepends=True),fromfile='authorized short_call.js with STEP_ID=B0024',tofile='failed call as preserved in reader original report'))
(OUT/'failed-call.diff').write_bytes(diff.encode('utf-8'))
ck('one exact non-datum call change explains entire preserved failed body',authorized.replace('p.schema !== "prof-reader-reuse-proof-v1"','p.schema !== "prof-reader-reuse-store-v1"',1),reported)
(OUT/'authorized-B0024.js.txt').write_bytes(authorized.encode('utf-8'))
(OUT/'reported-failed-B0024.js.txt').write_bytes(reported.encode('utf-8'))

before={x['path']:ident(x['path']) for x in immutable}
before.update({str(p):ident(p) for p in [ledger_path,state_path,report_path,comparison_path,INPUT/'binding-inventory.json']})
env=os.environ.copy();env['PYTHONDONTWRITEBYTECODE']='1'
completed=subprocess.run([core['python'],'-B',str(INPUT/'audit_bound_run.py')],cwd=OUT,env=env,capture_output=True)
(OUT/'whole-route-audit.stdout.txt').write_bytes(completed.stdout)
(OUT/'whole-route-audit.stderr.txt').write_bytes(completed.stderr)
ck('existing whole-route audit expected incomplete exit code',completed.returncode,2)
audit_result=json.loads(completed.stderr.decode('utf-8'))
ck('existing whole-route audit incomplete result',audit_result,{'operational_route_audit_passed':False,'error':'route/display evidence incomplete'})
after={p:ident(p) for p in before}
ck('all operational/input/runtime/report bytes unchanged by audit',after,before)
write('whole-route-audit-execution.json',{'executable':core['python'],'arguments':['-B',str(INPUT/'audit_bound_run.py')],'cwd':str(OUT),'returncode':completed.returncode,'stdout':ident(OUT/'whole-route-audit.stdout.txt'),'stderr':ident(OUT/'whole-route-audit.stderr.txt'),'parsed_result':audit_result,'read_only_execution':True,'bytecode_writes_disabled':True,'preserved_runtime_unchanged':True})
write('independent-terminal-audit.json',{'checked_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'report_identity':ident(report_path),'preservation_comparison_identity':ident(comparison_path),'route_identity':ident(route_path),'core_identity':ident(INPUT/'seal-core.json'),'runtime_identities':[ident(ledger_path),ident(state_path)],'immutable_binding_inventory_matches':immutable,'checks':checks,'prefix':prefix,'coverage':{'scheduled_steps':len(route['steps']),'scheduled_baseline_steps':45,'delivered_baseline_steps':23,'baseline_range':[0,position],'baseline_size':len(subject_bytes['BASELINE']),'unread_baseline_range':[position,len(subject_bytes['BASELINE'])],'remaining_baseline_bytes':len(subject_bytes['BASELINE'])-position,'teaching_text_steps_delivered':0,'figure_steps_delivered':0,'logged_event_counts':dict(collections.Counter(x['event'] for x in events))},'failed_call_comparison':{'authorized_default':ident(INPUT/'short_call.js'),'authorized_B0024_identity':ident(OUT/'authorized-B0024.js.txt'),'reported_failed_call_identity':ident(OUT/'reported-failed-B0024.js.txt'),'all_non_datum_differences':[{'line':9,'authorized':'p.schema !== "prof-reader-reuse-proof-v1"','reported':'p.schema !== "prof-reader-reuse-store-v1"'}],'failed_call_source':'preserved original reader final response; no independent session call transcript was available to this reviewer'},'conclusion':{'material_procedure_failure_established_from_preserved_report_and_correlated_runtime':True,'teaching_verdict_admissible':False,'immutable_input_or_core_defect_established':False,'whole_route_complete':False,'no_outside_access_claim_supported':False,'limits':'The local ledger supplies instrumented open/read/output receipt evidence and is consistent with the report; it is not a comprehensive host/tool transcript, tamper-proof attestation, proof of semantic inspection, or technical confinement. The exact failed call/result and successful-call wait details remain preserved reader-return evidence. No claim is made that absent ledger events prove absence of unlogged outside access.'}})
print(json.dumps({'comparisons':len(checks),'prefix_steps':len(prefix),'prefix_bytes':position,'route_steps':len(route['steps']),'whole_route_exit':completed.returncode,'failed_non_datum_changes':1,'all_preserved_bytes_unchanged':True},indent=2))
