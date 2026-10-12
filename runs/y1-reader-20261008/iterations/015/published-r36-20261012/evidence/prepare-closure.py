from pathlib import Path
import json,hashlib,copy,subprocess,shutil
B=Path(__file__).resolve().parents[1];old=B/'work/canonical';out=B/'closure';out.mkdir(exist_ok=True)
receipt=json.loads((B/'work/release-readback.json').read_text());archives=json.loads((B/'work/published-archive-readback.json').read_text());assert receipt['all_actual_bytes_match'] and archives['all_pass'] and receipt['pin']==archives['pin']
pin=receipt['pin'];repo=B.parent/'prof-iteration';prefix='runs/y1-reader-20261008/';iteration='iterations/015/published-r36-20261012/'
for n in ['queue.json','RUN.md','CHANGELOG.md']:
 b=subprocess.check_output(['git','show',pin+':'+prefix+n],cwd=repo);assert b==(old/n).read_bytes(),('canonical source changed',n)
q0=json.loads((old/'queue.json').read_text());q=copy.deepcopy(q0);s=next(s for s in q['sessions'] if s['material_id']=='D015');previous=copy.deepcopy(s)
s.setdefault('iteration_history',[]).append({'archived_at':'2026-10-12','reason':'Preserve exact prior D015 object before fresh r36 acceptance closure.','previous_record':previous})
s.update(status='closed',source_access='All five original PDF pages/texts and figures read before fresh authoring; complete independent source, technical, admitted chronological fresh SASIS and actual GitHub destination audits accepted. Frozen teaching unchanged.',incoming_prof='2026-10-12-r36',outgoing_prof='2026-10-12-r37',published_commit=pin)
s['evidence']+= [iteration+'evidence/'+n for n in ['final-adjudication.md','sasis-report.md','technical-report.txt','independent-mechanics-report.md','root-original/final-disposition.md','root-original/destination-review.md','closure.md','release-readback.json','published-archive-readback.json']]
s['current_review_status']={'destination':'pass: actual complete rendered content and all47 routes','iteration_closure':'accepted after all whole audits and actual complete package/evidence readback','required_next':'Continue fresh D016 under independently admitted published r37; do not reuse prior semantic findings.'}
s['current_iteration']={'state':'accepted_closed','incoming_prof':'2026-10-12-r36','verified_incoming_package_commit':'cb5f12cb9762839fade6841c161cdc8c670894cf','teaching_commit':'97e10125d66e612e3f0446ab1f8460c6fd4064a5','outgoing_prof':'2026-10-12-r37','verified_package_commit':pin,'behavioral_change':False,'evidence':iteration+'evidence/final-adjudication.md','next_action':'Fresh D016 original-only generation after exact current package admission; then all whole audits. Entire76-eligible corpus continues.'}
q['active_material_id']='D016';q['active_readability_scope']['closed']=16;q['active_readability_scope']['remaining']=60
assert len(q['sessions'])==147
assert [(x['id'],x['material_id'],x['order']) for x in q['sessions']]==[(x['id'],x['material_id'],x['order']) for x in q0['sessions']]
assert all(a==b for a,b in zip(q['sessions'],q0['sessions']) if a['material_id']!='D015')
eligible=set(q['active_readability_scope']['active_session_ids']);assert len(eligible)==76
assert sum(x['status']=='closed' for x in q['sessions'] if x['id'] in eligible)==16
assert sum(x['status']!='closed' for x in q['sessions'] if x['id'] in eligible)==60
assert len([x for x in q['sessions'] if x['id'] not in eligible])==71
assert next(x['material_id'] for x in q['sessions'] if x['id'] in eligible and x['status']!='closed')=='D016'
after=False;next_after=None
for x in q['sessions']:
 if x['material_id']=='D016':after=True;continue
 if after and x['id'] in eligible and x['status']!='closed':next_after=x['material_id'];break
assert next_after=='D018'
(out/'queue.json').write_text(json.dumps(q,indent=2,ensure_ascii=False)+'\n')
note=f'''D015 accepted; metadata-only PROF r37 closure — 2026-10-12

The complete fresh D015 under published PROF 2026-10-12-r36 is accepted after all original-source, whole technical, admitted chronological fresh SASIS, independent access and actual GitHub destination audits. All six teaching/help/figure files remain frozen at 97e10125d66e612e3f0446ab1f8460c6fd4064a5. All 213 equations, complete prose and figures, and 47 navigation edges pass. The original nonblocking uniqueness-overreading concern, unexplained preflight ledger anomaly, operational errors and authentication/source-scope limits remain preserved. No material failure or human learning outcome is claimed.

The complete 36-file, 907146-byte PROF 2026-10-12-r37 package and evidence release {pin} has exact actual-Git-byte readback of {receipt['count']} paths and {receipt['bytes']} bytes. Four files contain five metadata/hash-line changes; 32 files and every instructional body remain unchanged. All 34 internal declarations are verified. All current evidence archives have actual published member-byte verification; future archives remain opaque exact copies. No behavioral repair is invented. Original teaching, reports and previous canonical history remain intact.

Canonical totals are 16 accepted and 60 remaining of 76 eligible; 71 excluded; all 147 stable IDs and their order remain unchanged. Only D015's session object changes, preserving its entire previous object in iteration_history; all 146 others are identical. Active D016; the next pending material after D016 is D018. Continue the full corpus through fresh original-only author/reader contexts after verified publication. Root remains the sole browser operator, and publisher ownership transfers only by explicit root coordination.

Current evidence: {iteration}evidence/final-adjudication.md and closure.md. The closure commit itself requires a subsequent actual readback; this entry does not impersonate that later receipt.

'''
for n in ['RUN.md','CHANGELOG.md']:(out/n).write_bytes(note.encode()+(old/n).read_bytes())
(out/'closure.md').write_text(note)
inv={'release_pin':pin,'original_records':147,'eligible':76,'excluded':71,'accepted':16,'remaining':60,'only_changed_session':'D015','unchanged_other_sessions':146,'stable_ids_and_order_unchanged':True,'eligibility_unchanged':True,'all_prior_d015_fields_preserved_in_previous_record':True,'active_material_id':'D016','next_pending_after_active':'D018','run_and_changelog_original_bytes_preserved_as_suffix':True}
(out/'canonical-invariants.json').write_text(json.dumps(inv,indent=2)+'\n')
for src,dst in [('work/release-readback.json','release-readback.json'),('work/published-archive-readback.json','published-archive-readback.json'),('author/verify-published-archives.py','verify-published-archives.py'),('author/prepare-closure.py','prepare-closure.py')]:shutil.copyfile(B/src,out/dst)
def entry(p,remote):
 b=p.read_bytes();return {'local':str(p),'remote':remote,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest(),'upload':True}
files=copy.deepcopy(json.loads((B/'work/release-plan.json').read_text())['files'])
for f in files:f['upload']=False
for p in sorted(out.glob('*')):files.append(entry(p,prefix+p.name if p.name in ['queue.json','RUN.md','CHANGELOG.md'] else prefix+iteration+'evidence/'+p.name))
assert len({f['remote'] for f in files})==len(files)
(B/'work/closure-plan.json').write_text(json.dumps({'parent':pin,'base_tree':receipt['tree'],'files':files},indent=2)+'\n')
print(json.dumps({'files':len(files),'new_files':sum(f['upload'] for f in files),'bytes':sum(f['bytes'] for f in files),'invariants':inv},indent=2))
