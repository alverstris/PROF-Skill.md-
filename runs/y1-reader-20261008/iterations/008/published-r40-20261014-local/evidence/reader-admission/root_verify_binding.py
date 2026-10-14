"""Independent route/identity check; never invokes the production launcher."""
from pathlib import Path
import hashlib
import importlib.util
import json
import re
import sys
from datetime import datetime,timezone

sys.dont_write_bytecode=True
CASE=Path(__file__).resolve().parents[1];BOUND=CASE/'reader-inputs'
def sha(data):return hashlib.sha256(data).hexdigest()
core_raw=(BOUND/'seal-core.json').read_bytes()
core_hash=sha(core_raw)
assert core_hash=='bdfd374e597b3dd936c9f6b6915eec97c1168e816453a12d7a88b303cc7d8184'
core=json.loads(core_raw)
for name,spec in core['files'].items():
    p=BOUND/name;assert p.resolve().parent==BOUND.resolve()
    data=p.read_bytes();assert len(data)==spec['bytes'] and sha(data)==spec['sha256'],name
route_raw=(BOUND/'frozen-route.json').read_bytes()
assert sha(route_raw)==core['route_sha256']=='940bb751e8f8146ab41747c79ae20132929d1b7155cb8663cd5c113c90ff49dc'
route=json.loads(route_raw);assert route['revision']=='2102c1fc637c7c97248c9b2c2d2a6e5da39a39ce'
data_by_id={}
for fid,f in route['files'].items():
    p=Path(f['path']);assert p.resolve().is_relative_to((BOUND/'subjects').resolve())
    data=p.read_bytes();assert len(data)==f['size'] and sha(data)==f['sha256'],fid
    data_by_id[fid]=data
frozen=json.loads((CASE/'fresh-author/evidence/teaching-freeze.json').read_bytes())
assert len(frozen['files'])==6
for f in frozen['files']:
    original=(CASE/'fresh-author'/f['path']).read_bytes()
    copied=(BOUND/'subjects'/f['path']).read_bytes()
    assert original==copied and len(original)==f['bytes'] and sha(original)==f['sha256'],f['path']
assert data_by_id['BASELINE']==Path('C:/Users/alver/.codex/skills/prof/references/sasis/ocr-baseline-20261007/student-baseline.txt').read_bytes()
cursors={fid:0 for fid in route['files']};ids=[];first_teaching=None;main_cursor=0;figures=[]
for i,s in enumerate(route['steps']):
    fid=s['file_id'];assert s['id'] not in ids;ids.append(s['id'])
    assert s['start']==cursors[fid] and s['length']>0
    chunk=data_by_id[fid][s['start']:s['start']+s['length']]
    assert len(chunk)==s['length'] and sha(chunk)==s['sha256']
    cursors[fid]+=s['length']
    if s['kind']=='text':assert s['length']<=6000 and chunk.decode('utf-8')
    else:assert s['start']==0 and s['length']==len(data_by_id[fid])
    if fid!='BASELINE' and first_teaching is None:first_teaching=i
    if fid=='MAIN':main_cursor=cursors[fid]
    if fid.startswith('FIG'):
        assert i>0 and route['steps'][i-1]['file_id']=='MAIN'
        figures.append((fid,main_cursor))
assert len(ids)==77 and first_teaching==45
assert all(s['file_id']=='BASELINE' for s in route['steps'][:45])
assert all(s['file_id']!='BASELINE' for s in route['steps'][45:])
assert all(cursors[fid]==len(data) for fid,data in data_by_id.items())
assert len(route['baseline_revisits'])==45 and set(route['baseline_revisits'].values())==set(ids[:45])
main=data_by_id['MAIN'];expected_figures=[];boundaries=[];offset=0
for line in main.splitlines(keepends=True):
    text=line.decode('utf-8')
    if '<a id="main-d008-a' in text or '<a id="main-d008-revisit"' in text:boundaries.append(offset)
    if '<img ' in text:
        src=re.search(r'src="([^"]+)"',text).group(1)
        fid=next(fid for fid,f in route['files'].items() if Path(f['path']).name==Path(src).name)
        expected_figures.append((fid,offset+len(line)))
    offset+=len(line)
assert figures==expected_figures and len(figures)==3
for boundary in boundaries:
    assert not any(s['file_id']=='MAIN' and s['start']<boundary<s['start']+s['length'] for s in route['steps'])
assert len(boundaries)==5
launch_raw=(BOUND/'reader-launch-message.txt').read_bytes()
assert len(launch_raw)==26580 and sha(launch_raw)=='7e7d4a00ad2d615c6f1a15b8b5a5a95307913551bb48be1d880f3ea7a6f1b04b'
blocks=re.findall(r'```(?:javascript|json)\r?\n(.*?)```',launch_raw.decode(),re.S)
assert len(blocks)==3
for i,name in enumerate(['bootstrap.js','short_call.js']):
    assert blocks[i].replace('\r\n','\n')==(BOUND/name).read_bytes().decode().replace('\r\n','\n')+'\n'
assert json.loads(blocks[2])==route
assert not (BOUND/'runtime').exists()
subject_paths={str(Path(f['path']).resolve()).lower() for f in route['files'].values()}
subject_opens=[]
def audit(event,args):
    if event=='open' and isinstance(args[0],(str,bytes,Path)):
        p=str(Path(args[0]).resolve()).lower()
        if p in subject_paths:
            subject_opens.append(p);raise RuntimeError('Metadata proof attempted subject open')
sys.addaudithook(audit)
spec=importlib.util.spec_from_file_location('root_sealed_verifier',BOUND/'verify_reuse.py')
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
proof=module.proof('bootstrap',core_hash)
assert proof['seal']['binding_sha256']==core_hash and not subject_opens and not (BOUND/'runtime').exists()
record={'root_binding_verification':'pass','baseline_and_teaching_constituents':7,'exact_covered_bytes':sum(cursors.values()),
        'scheduled_steps':77,'initial_baseline_steps':45,'baseline_revisits':45,'figures_at_first_use':figures,
        'exercise_boundaries':boundaries,'launch_message_sha256':sha(launch_raw),'core_sha256':core_hash,
        'metadata_proof_subject_opens':len(subject_opens),'production_runtime_exists':False,
        'production_launcher_invoked':False,'reader_dispatched':False,'semantic_admission':False,
        'verified_at':datetime.now(timezone.utc).isoformat()}
(Path(__file__).parent/'root-binding-verification.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print(json.dumps(record))
