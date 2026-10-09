from pathlib import Path
from hashlib import sha256
import json, re, subprocess, datetime
from PIL import Image
import fitz

base = Path('/workspace/scratch/ac36b9c5ff31')
repo = base / 'PROF-repo'
rel = 'runs/y1-reader-20261008/iterations/008/author-work-r14'
p = repo / rel
out = Path(__file__).resolve().parent
h = lambda b: sha256(b).hexdigest()
manifest = json.loads((p/'artifact-sha256.json').read_bytes())
incoming = 'e35a59a64ed1b01f7ae43e4ef46042f23cc7e2d6'
freeze = 'e0f87210f8085487a1fb6e29bb4ca821cadca5e5'
r = {'audited_at': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'incoming_commit': incoming, 'diagnostic_freeze': freeze}
r['manifest'] = {'sha256':h((p/'artifact-sha256.json').read_bytes()), 'expected_sha256':'9a4bb087d84259f0262a3d5e2e59bd7bfa9fdc2b29bcfd548266519e6590da09', 'entries':[]}
for f in manifest['files']:
    b=(p/f['path']).read_bytes()
    r['manifest']['entries'].append({'path':f['path'],'hash_match':h(b)==f['sha256'],'bytes_match':len(b)==f['bytes']})
listed={x['path'] for x in manifest['files']}|{'artifact-sha256.json'}
actual={str(f.relative_to(p)) for f in p.rglob('*') if f.is_file()}
r['manifest']['missing']=sorted(listed-actual)
r['manifest']['unlisted']=sorted(actual-listed)
r['manifest']['expected_match']=r['manifest']['sha256']==r['manifest']['expected_sha256']
r['control_copies']=[]
for f in sorted((p/'inputs').rglob('*')):
    if not f.is_file() or 'original-source' in f.parts: continue
    path=str(f.relative_to(p/'inputs'))
    b=subprocess.run(['git','show',incoming+':'+path],cwd=repo,check=True,capture_output=True).stdout
    r['control_copies'].append({'path':path,'bytes':len(b),'raw_chars':len(b.decode()),'sha256':h(b),'actual_git_object_match':b==f.read_bytes()})
r['teaching_bindings']=[]
for n in ['teaching.md','teaching-original.md']:
    b=(p/n).read_bytes()
    q=subprocess.run(['git','show',freeze+':'+rel+'/'+n],cwd=repo,capture_output=True)
    r['teaching_bindings'].append({'path':n,'bytes':len(b),'raw_chars':len(b.decode()),'sha256':h(b),'diagnostic_git_show_exit':q.returncode,'diagnostic_git_show_stderr':q.stderr.decode(),'exact_diagnostic_match':q.returncode==0 and q.stdout==b})
r['source_bindings']=[]
cache=base/'prof-readability/audit-1801-notes/L09'
for f in sorted((p/'inputs/original-source').iterdir()):
    b=f.read_bytes(); row={'path':str(f.relative_to(p)),'sha256':h(b),'bytes':len(b),'original_cache_exact_match':(cache/f.name).read_bytes()==b}
    if f.suffix=='.txt': row['full_raw_character_extent']=[0,len(b.decode())]
    if f.suffix=='.png':
        im=Image.open(f); im.load(); row.update({'decodes_completely':True,'dimensions':[im.width,im.height]})
    if f.suffix=='.pdf':
        doc=fitz.open(f); row['page_count']=doc.page_count
    r['source_bindings'].append(row)
b=(p/'inputs/references/sasis/ocr-baseline-20261007/student-baseline.txt').read_bytes();s=b.decode()
access=(p/'author/access-record.md').read_text()
part=access.split('Actual zero-based half-open character ranges read in order: ',1)[1].split('. One thousand',1)[0]
ranges=[[int(a),int(b)] for a,b in re.findall(r'\[(\d+),(\d+)\)',part)]
cursor=0; gaps=[]
for a,z in ranges:
    if a>cursor:gaps.append([cursor,a])
    cursor=max(cursor,z)
r['baseline']={'bytes':len(b),'raw_utf8_characters':len(s),'LF':s.count('\n'),'sha256':h(b),'declared_full_read_ranges':ranges,'gaps':gaps,'ends_at_actual_end':cursor==len(s),'preserves_CRCRLF': '\r\r\n' in s,'declared_unclipped': 'All responses were unclipped.' in access, 'auditor_full_baseline_read':False,'auditor_focused_reads':[[20248,26731],[63872,64638]]}
r['author_read_extents']={'skill_recovery_ranges':[[16000,28000],[0,16000],[28000,37389]],'execution_protocol_ranges':[[0,14000],[14000,26404]],'teaching_ranges':[[0,13930],[13300,26970]],'source_text_pages_declared':list(range(1,8)),'source_full_image_pages_declared':list(range(1,8)),'basis':'Author access attestation checked against exact artifact lengths and unique source-coverage content; not independently replayed historical tool output.'}
state=json.loads((p/'.prof-state/manifest.json').read_bytes())
topic=json.loads((p/'.prof-state/topics/local-approximations.json').read_bytes())
deps={kind:json.loads((p/f'author/dependencies-{kind}.json').read_bytes()) for kind in ['topic','full']}
r['state_sources']=[{'id':x['id'],'hash_match':h(Path(x['path']).read_bytes())==x['sha256'],'portion_count':len(x['portions']),'all_required':all(y['disposition']=='required' for y in x['portions'])} for x in state['sources']]
srcmap={x['id']:x for x in state['sources']}
r['source_read_bindings']=[{'source_id':x['source_id'],'portion_id':x['portion_id'],'recorded_status':x['status'],'hash_match':x['reviewed_sha256']==srcmap[x['source_id']]['sha256']}for x in topic['source_reads']]
reqtext=(p/'author/requirements.md').read_text()
r['requirements']=[{'id':k,'status':v['status'],'reason_found_in_ledger':v['reason'] in reqtext,'dependency_count':len(v['dependencies']),'dependencies_current':v['dependencies']==deps['topic']}for k,v in topic['requirements'].items()]
r['output_checks']=[{'id':x['id'],'status':x['status'],'dependency_count':len(x['dependencies']),'dependencies_current':x['dependencies']==deps['full']}for x in state['output_checks']]
r['evidence_bindings']=[]
def evidence(v):
    if isinstance(v,dict):
        if {'path','sha256','locator'}<=set(v):
            f=Path(v['path']);f=f if f.is_absolute() else p/f;b=f.read_bytes();lo=v['locator'];lines=b.decode().splitlines()
            found=(1<=lo['start']<=lo['end']<=len(lines)) if lo['kind']=='lines' else (lo['value'] in b.decode())
            r['evidence_bindings'].append({'path':v['path'],'sha256':h(b),'hash_match':h(b)==v['sha256'],'locator':lo,'locator_exists':found})
        for x in v.values():evidence(x)
    elif isinstance(v,list):
        for x in v:evidence(x)
evidence(state);evidence(topic)
helper=p/'inputs/scripts/prof_state.py'
r['helper_reruns']=[]
for kind in ['topic','full']:
    suffix=['--topic','local-approximations'] if kind=='topic' else []
    args=['python',str(helper),'check','--state',str(p/'.prof-state')]+suffix
    q=subprocess.run(args,capture_output=True)
    (out/f'helper-{kind}-rerun.txt').write_bytes(q.stdout);(out/f'helper-{kind}-rerun.stderr.txt').write_bytes(q.stderr)
    original=(p/f'author/helper-check-{kind}.txt').read_text().split('\n',2)[2]
    j=subprocess.run(args+['--json'],capture_output=True)
    (out/f'helper-{kind}-rerun.json').write_bytes(j.stdout)
    d=subprocess.run(['python',str(helper),'dependencies','--state',str(p/'.prof-state')]+suffix,capture_output=True)
    r['helper_reruns'].append({'scope':kind,'exit':q.returncode,'stderr':q.stderr.decode(),'original_recorded_stdout_exact_match':q.stdout.decode()==original,'json_exit':j.returncode,'json_stderr':j.stderr.decode(),'report':json.loads(j.stdout),'dependency_rerun_exit':d.returncode,'dependencies_match_original':d.returncode==0 and json.loads(d.stdout)==deps[kind]})
t=(p/'teaching.md').read_bytes().decode();plain=re.sub(r'<!-- P\d+ -->\n','',t);pr=(p/'task-prompts-original.md').read_text()
r['prompt_bindings']={'sha256':h((p/'task-prompts-original.md').read_bytes()),'expected_sha256':'e29dbbaacd7ee2112c270762823bdc945f49ac822e6623d83cae07d0318e9d82','bodies_verbatim':[]}
for n in range(1,5):
    a=pr.index(f'A{n}.');z=pr.index(f'A{n+1}.') if n<4 else len(pr)
    r['prompt_bindings']['bodies_verbatim'].append({'id':f'A{n}','entire_label_and_prompt_in_teaching':pr[a:z].strip() in plain})
r['prompt_chronology']={'file_mtimes_utc':{n:datetime.datetime.fromtimestamp((p/n).stat().st_mtime,datetime.timezone.utc).isoformat()for n in ['task-prompts-original.md','author/pre-solution-checks.txt','teaching-original.md','teaching.md','author/reconstruction.md']},'root_acknowledgement_identifiers_in_author_record':['a25658795c1efdbf276bc164af32c499afd7ce952dcac2da1be047d6ad093b88','69fea3378178401c01922686ef858bbe0c340505ea799f384b43baad8ccbb07e'],'root_calculation_files_read_or_verified':False,'limit':'Explicitly not opened under the audit assignment. Author timing and parent acknowledgement claims are attestations; filesystem modification times are not tamper-proof execution history.'}
r['auditor_personal_teaching_read']={'ranges':[[0,14500],[14000,26970]],'full_current_teaching_core_help_ending':True,'untruncated':True,'is_SASIS':False}
r['original_author_files_still_match_manifest']=all(h((p/f['path']).read_bytes())==f['sha256']for f in manifest['files'])
r['limits']=['No parent first-draft review or root solution was read.','Source images were decoded and compared byte for byte, not visually re-reviewed by this auditor.','Only focused baseline passages were personally read during this binding audit.','External official pages were not reopened by this auditor; research reading scope remains author documentary evidence.','No live GitHub rendering, CSS, mathematical payload, navigation or fresh-reader verdict is claimed.','No author script that mutates original outputs/state was rerun.','No technical isolation, erased pretraining, learner outcome or corpus closure follows from this audit.']
(out/'verification.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'manifest_entries':len(manifest['files']),'manifest_sha_matches':r['manifest']['expected_match'],'manifest_failures':[x for x in r['manifest']['entries'] if not(x['hash_match']and x['bytes_match'])],'unlisted':r['manifest']['unlisted'],'missing':r['manifest']['missing'],'controls':len(r['control_copies']),'controls_failures':[x for x in r['control_copies']if not x['actual_git_object_match']],'source_files':len(r['source_bindings']),'source_failures':[x for x in r['source_bindings']if not x['original_cache_exact_match']],'teaching':r['teaching_bindings'],'baseline':r['baseline'],'helper_reruns':r['helper_reruns'],'evidence_count':len(r['evidence_bindings']),'evidence_failures':[x for x in r['evidence_bindings']if not(x['hash_match']and x['locator_exists'])],'unchanged':r['original_author_files_still_match_manifest']},ensure_ascii=False,indent=2))
