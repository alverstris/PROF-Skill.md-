from pathlib import Path
from collections import defaultdict
from datetime import datetime, timezone
import hashlib, json, subprocess, shutil

ROOT = Path('/workspace/scratch/ac36b9c5ff31/PROF-repo')
AUTHOR = ROOT/'runs/y1-reader-20261008/iterations/008/author-work-r15'
OUT = Path('/workspace/scratch/ac36b9c5ff31/prof-readability/d008-r15-author-audit')
CANDIDATE = '7ea4148ed1eda90436c0f6f23fde479de3452079'
FREEZE = '2d144338ec647166e6fd2a6527fbc96b766e7d5e'
TEACHING_SHA = '86b6338315866e711ddfcefd52e4a84b2bb99093c321ff6b7a8124c66c739718'
def sha(b): return hashlib.sha256(b).hexdigest()
def readj(p): return json.loads(p.read_bytes())
def save(n, v): (OUT/n).write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n')
def git(commit,path): return subprocess.check_output(['git','show',f'{commit}:{path}'],cwd=ROOT)
def file_record(p):
    b=p.read_bytes()
    return {'path':str(p),'bytes':len(b),'sha256':sha(b)}

manifest=readj(AUTHOR/'artifact-manifest.json')
entries=manifest['files']
actual={str(p.relative_to(AUTHOR)) for p in AUTHOR.rglob('*') if p.is_file() and p.name!='artifact-manifest.json'}
declared={e['path'] for e in entries}
assert actual==declared, {'missing':list(declared-actual),'undeclared':list(actual-declared)}
assert len(entries)==len(declared)
for e in entries:
    p=AUTHOR/e['path']; assert not p.is_symlink()
    b=p.read_bytes(); assert len(b)==e['bytes'] and sha(b)==e['sha256'],e['path']
save('artifact-verification.json',{'manifest':file_record(AUTHOR/'artifact-manifest.json'),'count':len(entries),'bytes':sum(e['bytes'] for e in entries),'all_entries_verified':True,'exact_file_set':True,'entries':entries})

controls=readj(AUTHOR/'control-manifest.json')
checks=[]
for e in controls:
    p=AUTHOR/'controls'/e['path']; b=p.read_bytes()
    assert len(b)==e['bytes'] and len(b.decode('utf-8'))==e['raw_chars'] and sha(b)==e['sha256']
    assert git(CANDIDATE,e['path'])==b
    checks.append({**e,'candidate_byte_identical':True})
for e in readj(AUTHOR/'control-supplement-manifest.json'):
    b=(AUTHOR/e['path']).read_bytes()
    assert len(b)==e['bytes'] and len(b.decode('utf-8'))==e['raw_chars'] and sha(b)==e['sha256']
    if e['path'].endswith('student-role.txt'): ref=git(CANDIDATE,e['path'].removeprefix('controls/')); provenance='candidate git object'
    else: ref=Path('/root/.codex/skills/builtins/pdf/SKILL.md').read_bytes(); provenance='installed cloud PDF skill'
    assert ref==b
    checks.append({**e,'verified_against':provenance})
for n in ['teaching.md','teaching-original.md']:
    p=AUTHOR/n;b=p.read_bytes();assert sha(b)==TEACHING_SHA
    assert git(FREEZE,str(p.relative_to(ROOT)))==b
save('pinned-controls-and-teaching.json',{'candidate':CANDIDATE,'teaching_freeze':FREEZE,'teaching_sha256':TEACHING_SHA,'control_count':len(checks),'controls':checks,'both_teaching_copies_identical_to_freeze':True})

src=readj(AUTHOR/'source-manifest.json');cache=ROOT.parent/'prof-readability/audit-1801-notes/L09'
for e in src:
    b=(AUTHOR/'source'/e['file']).read_bytes(); assert len(b)==e['bytes'] and sha(b)==e['sha256']
    assert b==(cache/e['file']).read_bytes()
save('original-source-preservation.json',{'count':len(src),'exact_set':['lec9.pdf']+[f'lec9-p{i:02d}.{ext}' for ext in ['txt','png'] for i in range(1,8)],'all_copies_byte_identical_to_original_cache':True,'entries':src,'limitation':'This checks author access records and preserved original bytes; it does not recreate the author image-viewing events.'})

packets=readj(AUTHOR/'read-packets.json');success=readj(AUTHOR/'read-success.json');access=readj(AUTHOR/'full-input-access.json')
assert len(packets)==len(success)==len(access['packets'])==35
by_input=defaultdict(list)
for i,(p,s,a) in enumerate(zip(packets,success,access['packets'])):
    assert s['index']==i and s['exit_code']==0 and s['status']=='read_full_success_no_truncation'
    assert all(a[k]==v for k,v in p.items()) and all(a[k]==v for k,v in s.items())
    assert 0<p['end']-p['start']<=15000
    by_input[p['input']].append(p)
coverage=[]
for e in controls:
    seq=by_input[e['path']];end=0
    for p in seq: assert p['start']==end; end=p['end']
    assert end==e['raw_chars']
    coverage.append({'input':e['path'],'range':[0,end],'packets':len(seq),'continuous':True})
final=readj(AUTHOR/'final-access.json');end=0
for p in final['packets']:
    assert p['range'][0]==end;end=p['range'][1]
    assert p['status']=='read_full_success_no_truncation'
assert end==len((AUTHOR/'teaching-original.md').read_bytes().decode())==27792
save('access-record-verification.json',{'full_input_packets':35,'continuous_controls':coverage,'baseline_byte_and_extent_binding':True,'full_teaching_range':[0,end],'teaching_packets':final['packets'],'author_reported_full_seven_page_text_image_reading':access['additional_reads'][-2:],'limits':'Records establish declared scope, ranges, byte identity and output identifiers. The audit cannot replay private historical tool outputs or infer cognitive retention; it is not fresh-reader isolation.'})

state=AUTHOR/'.prof-state';helper=AUTHOR/'controls/scripts/prof_state.py'
reruns=[]
for n,args,expected_exit in [('topic-check.json',['check','--topic','approximations','--json'],1),('full-check.json',['check','--json'],1),('topic-dependencies.json',['dependencies','--topic','approximations'],0),('full-dependencies.json',['dependencies'],0)]:
    r=subprocess.run(['python3',str(helper),*args,'--state',str(state)],capture_output=True)
    assert r.returncode==expected_exit,(n,r.returncode,r.stderr.decode())
    value=json.loads(r.stdout);assert value==readj(AUTHOR/n),n
    save('rerun-'+n,value)
    reruns.append({'record':n,'exit_code':r.returncode,'json_equal':True,'stderr':r.stderr.decode()})
man=readj(state/'manifest.json');topic=readj(state/'topics/approximations.json')
for rec in [man['skill'],man['request']]+man['sources']+man['outputs']:
    p=Path(rec['path']);p=p if p.is_absolute() else AUTHOR/p
    assert p.is_relative_to(AUTHOR) and sha(p.read_bytes())==rec['sha256']
for collection in [topic['gaps'],list(topic['requirements'].values()),man['output_checks']]:
    for rec in collection:
        deps=rec['dependencies']
        if deps:
            expected='full-dependencies.json' if collection is man['output_checks'] else 'topic-dependencies.json'
            assert deps==readj(AUTHOR/expected)
        for e in rec['evidence']:
            p=Path(e['path']);p=p if p.is_absolute() else AUTHOR/p
            b=p.read_bytes(); assert sha(b)==e['sha256']
            if e['locator']['kind']=='text': assert e['locator']['value'] in b.decode()
assert topic['requirements']['T11']['status']=='unverified'
pending=[x['id'] for x in man['output_checks'] if x['status']=='pending']
assert set(pending)=={'destination_math','destination_typography','destination_navigation','independent_technical','fresh_sasis','final_review','publication'}
save('state-audit.json',{'reruns':reruns,'all_evidence_hashes_and_text_locators_verified':True,'all_declared_dependencies_equal_current_recomputed_snapshot':True,'sources':len(man['sources']),'source_portions':len(topic['source_reads']),'requirements':{k:v['status'] for k,v in topic['requirements'].items()},'output_checks':{v['id']:v['status'] for v in man['output_checks']},'false_parent_gate_pass':False})

repro=OUT/'verification-reproduction';repro.mkdir(exist_ok=True)
for n in ['verify.py','teaching.md','teaching-original.md']:shutil.copyfile(AUTHOR/n,repro/n)
r=subprocess.run(['python3','verify.py'],cwd=repro,capture_output=True)
assert r.returncode==0 and readj(repro/'verification-results.json')==readj(AUTHOR/'verification-results.json')
save('numeric-reproduction.json',{'exit_code':r.returncode,'stderr':r.stderr.decode(),'json_equal':True,'original_record':file_record(AUTHOR/'verification-results.json'),'reproduced_record':file_record(repro/'verification-results.json'),'scope':'Reproduces the authored rational/numeric/source checks; no independent semantic proof or rendering certification.'})
save('completion.json',{'at':datetime.now(timezone.utc).isoformat(),'audit_result':'No blocking package inconsistency or false independent-gate completion found.','artifact_files':len(entries),'skill_candidate':CANDIDATE,'teaching_freeze':FREEZE,'teaching_sha256':TEACHING_SHA,'originals_edited':False})
print(json.dumps(readj(OUT/'completion.json'),indent=2))
