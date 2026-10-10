"""Bind performed reviews and retain the unresolved destination gate."""
import hashlib,json,subprocess,shutil
from pathlib import Path

root=Path(__file__).resolve().parents[1]
state=root/'.prof-state'
tool=root/'inputs/prof/scripts/prof_state.py'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
dst=root/'review/root-independent'
records=[]
for p in sorted((root.parent/'root-review-d016-r26').iterdir()):
    if p.is_file():
        t=dst/p.name
        if t.exists():assert t.read_bytes()==p.read_bytes()
        else:shutil.copyfile(p,t);t.chmod(0o444)
        records.append({'source':str(p),'copy':str(t.relative_to(root)),'sha256':sha(t),'bytes':t.stat().st_size})
(root/'review/root-evidence-identities.json').write_text(json.dumps(records,indent=2)+'\n')
def deps(topic=False):
    args=['python',str(tool),'dependencies','--state',str(state)]
    if topic:args+=['--topic','definite-integrals']
    return json.loads(subprocess.check_output(args,text=True))
def witness(path,phrase):
    p=root/path
    line=next(l for l in p.read_text().splitlines() if phrase in l)
    return {'path':path,'sha256':sha(p),'locator':{'kind':'text','value':line}}
td=deps(True);gd=deps()
topic=json.loads((state/'topics/definite-integrals.json').read_text());manifest=json.loads((state/'manifest.json').read_text())
coord='review/coordinator-disposition.md';source='review/source-prof-original.md';live='review/root-independent/live-destination-attempt.json'
for i in range(1,11):
    evidence=[witness(source,f'| T{i} ')]
    if i==10:evidence+=[witness(coord,'I reconstructed the complete saved lesson'),witness('review/root-independent/frozen-mathematics-disposition.md','All five solution results')]
    topic['requirements']['T'+str(i)].update(status='pass',reason='Applicable teaching duty was checked across the actual complete route and help; concrete current passage witnesses and their independent reconciliation are preserved.',evidence=evidence,dependencies=td)
for rid in ['T11','T12']:
    topic['requirements'][rid].update(status='unverified',reason='Native/source checks and complete content audits are performed, but actual GitHub destination-dependent preservation/readability/navigation and therefore final acceptance remain unverified after two observed error pages.',evidence=[witness(coord,'Actual GitHub expression preservation')],dependencies=[])
topic['gaps']=[{'id':'destination-access','question':'Does the actual GitHub destination preserve all frozen expressions, prose style, embedded figure readability and help navigation?','consequential':True,'status':'unverified','reason':'Two actual attempts returned the GitHub Unicorn page, with no lesson content. No document/PROF cause is established.','next_action':'Resume the unchanged immutable destination audit when it is available; do not regenerate, invent a PROF defect or advance D016 meanwhile.','evidence':[witness(coord,'The browser record preserves both actual error-page observations')],'dependencies':[]}]
check_witnesses={
'coverage':[(source,'No substantive source page')],
'source_integrity':[(coord,'The operative source of PROF was'),(coord,'The frozen generation was published')],
'technical':[('review/root-independent/frozen-mathematics-disposition.md','All five solution results'),(coord,'I reconstructed the complete saved lesson')],
'reader':[('review/sasis-original.md','Input admission is complete.'),(coord,'I read both complete original reports')],
'native_figures':[(source,'rectangles.png, 1700'),(source,'pyramids.png, 1768'),(source,'triangle-and-tag.png, 1700'),(coord,'Triangle/tag annotations:')],
'source_structure':[(coord,'The reproducible source-structure check finds')],
'published_bytes':[(coord,'The frozen generation was published')],
'earlier_cases':[('review/earlier/coordinator-disposition.md','I fetched the seven'),('review/earlier/coordinator-disposition.md','Disposition: these exact earlier artifacts')]
}
for c in manifest['output_checks']:
    if c['id'] in ['destination','final_review']:
        c.update(status='unverified',reason='Actual destination checks remain unavailable; the full generation is not accepted.',evidence=[witness(coord,'Actual GitHub expression preservation')],dependencies=[])
    else:c.update(status='pass',reason='Performed scoped check with the actual current files; witness limits retained.',evidence=[witness(*pair) for pair in check_witnesses[c['id']]],dependencies=gd)
(state/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
(state/'topics/definite-integrals.json').write_text(json.dumps(topic,indent=2)+'\n')
(state/'RUN.md').write_text('D016 r26b recovery\n\nExact request: ../original-task.txt. Operative PROF: ../inputs/prof/SKILL.md, version2026-10-10-r26, package publicationa5e86eac9e9805921473419c48b329bde7bd46ec; actual36-file readback in ../package-verification.json.\n\nCurrent topic: definite-integrals. Complete original source/full baseline author admission precedes generation; see ../author/input-admission.json and coverage-and-research.md. Frozen six-file teaching is published at51a78beccef858072b1da8d057ef3dff09878409; no teaching edits permitted.\n\nFull fresh SASIS, independent source/PROF and mathematical originals, coordinator/parent dispositions and affected-earlier checks are in ../review/. No material content failure is established. Source/local checks do not replace destination evidence. T11/T12 and destination/final review remain unverified after two GitHub Unicorn error pages; next action is inspect the same immutable published destination when available, including every expression, all3 embedded figures and all help navigation.\n\nD016 pending;15 accepted/61remaining,76eligible/71excluded,all147IDs unchanged. D017 follows D016, thenD018. No PROF revision or fresh generation is justified by an external access failure alone. No installed-skill, user-computer or automation change. Reopen exact skill, execution protocol, request, current topic and relevant original evidence on recovery.\n')
for name,args in [('topic-check',['--topic','definite-integrals']),('full-check',[])]:
    result=subprocess.run(['python',str(tool),'check','--state',str(state),*args],text=True,capture_output=True)
    (root/'review'/f'{name}.txt').write_text(result.stdout+result.stderr)
    print(name,'exit',result.returncode,result.stdout)
