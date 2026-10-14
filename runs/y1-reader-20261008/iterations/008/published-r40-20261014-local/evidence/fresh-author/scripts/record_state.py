from pathlib import Path
import json,hashlib,subprocess,sys
ROOT=Path(__file__).resolve().parents[1]
STATE=ROOT/'.prof-state'
PROF=Path('C:/Users/alver/.codex/skills/prof')
HELPER=PROF/'scripts/prof_state.py'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
write=lambda p,obj:p.write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
manifest=json.loads((STATE/'manifest.json').read_text(encoding='utf-8'))
request=ROOT/'evidence/original-task-handover.txt'
manifest['request']={'path':str(request),'sha256':sha(request)}
sources=[]; reads=[]
def add(id,path,locator,note,url=None):
    path=Path(path).resolve()
    source={'id':id,'path':str(path),'sha256':sha(path),'portions':[{'id':'complete','locator':locator,
           'disposition':'required','reason':'Assigned input or actual operative dependency used in this connected topic.',
           'evidence':[]}]}
    if url:source['url']=url
    sources.append(source)
    reads.append({'source_id':id,'portion_id':'complete','status':'read','reviewed_sha256':sha(path),'note':note})
orig=ROOT.parent/'original-inputs'
add('original-pdf',orig/'mit-18.01-fall-2006-lec9.pdf','PDF pages1-7, all formulas, figures/captions, cover',
    'All seven page images visually read; original PDF hash/page count independently inspected; complete direct extraction read as aid. Exact disputed glyphs inspected from readable actual-PDF crops.',
    'https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/40cb41807e6d67373f3299ce87c4d9b3_lec9.pdf')
for i,note in enumerate(['MIT cover/course/terms','Tangent geometry, logarithm, recentering',
    'Five basic linears, proofs, sine/cosine plots, composite start',
    'Composite truncation and reciprocal footnote, derivative, limit and time model',
    'Satellite diagram/frame labels, time linear scale, quadratic/half coefficient',
    'Cosine quadratic figure, five quadratics/log proof, second-order timing',
    'Timing scale and atomic-clock context, complete composite quadratic'],1):
    add('page-'+str(i),orig/f'page-{i}.png','Complete original page image, including every canvas edge',note)
add('baseline',PROF/'references/sasis/ocr-baseline-20261007/student-baseline.txt','All2561 lines /247840bytes, four subjects',
    'Complete bounded reading logged in input-access.md; Mathematics derivative/tangent/binomial and FM27 supply actual local prerequisites. Physics supplies units/constants but not relativity; Chemistry read with no lecture-specific premise needed.')
refs=[('execution-protocol','references/execution-protocol.md','Full execution/source/reconstruction/destination duties'),
      ('domain-patterns','references/domain-patterns.md','Physics and mathematics passage plus full file read'),
      ('state-tool','references/state-tool.md','Full schema, check scope and freshness semantics'),
      ('sasis','references/sasis.md','Full publication-first/fresh separation and reader boundary'),
      ('profile-manifest','references/sasis/profile-manifest.json','Whole manifest; fixed four-subject profile/hash and controls'),
      ('reader-role','references/sasis/student-role.txt','Whole operating instruction, read for role separation only'),
      ('reader-contract','references/sasis/student-testing-contract.txt','Whole reader contract, not used to impersonate reader'),
      ('rewrite-guide','references/sasis/rewrite-guide.md','Full no-patch/fresh generation repair policy'),
      ('execution-research','references/execution-research.md','Full provenance/engineering limits; no method change or new outcome claim')]
for id,rel,note in refs:add(id,PROF/rel,'Whole file',note)
add('pdf-skill','C:/Users/alver/.codex/plugins/cache/openai-primary-runtime/pdf/26.1013.11914/skills/pdf/SKILL.md',
    'Whole read-only PDF workflow','Read completely before visual/source inspection; no PDF created, no create/edit marker applicable.')
add('prerequisite-record',ROOT/'evidence/prerequisites-and-coverage.md','Whole convention/prerequisite/coverage record',
    'C1-C4 andS01-S10 inspected; immediate premises and source scope remain current.')
add('web-read-record',ROOT/'evidence/research-and-source-checks.md','Inspected official OpenStax and NIST passages plus source/calculation notes',
    'Actual official web passages read and recorded; event/frame mapping and both-effect GPS scope incorporated before use.')
add('exact-task',request,'Whole delegated task and later operational update','Exact available handover preserved; no old teaching/diagnosis input.')
manifest['sources']=sources
freeze=json.loads((ROOT/'evidence/teaching-freeze.json').read_text(encoding='utf-8'))
manifest['outputs']=[dict(id='output-'+str(i),path=f['path'],sha256=f['sha256']) for i,f in enumerate(freeze['files'],1)]
manifest['required_topics']=[{'id':'local-approximation','title':'Local polynomial approximation, C1-C4 andS01-S10',
    'source_portions':[{'source_id':s['id'],'portion_id':'complete'} for s in sources],
    'outputs':[o['id'] for o in manifest['outputs']]}]
audit=ROOT/'evidence/author-audit.md'
def evidence(path,phrase):return [{'path':path.relative_to(ROOT).as_posix(),'sha256':sha(path),
                                  'locator':{'kind':'text','value':phrase}}]
def cond(status,reason,path,phrase):return dict(applicable=True,status=status,reason=reason,
                                              evidence=evidence(path,phrase),dependencies=[])
checks=[('coverage','pass','All original pages/topics mapped and inspected.',ROOT/'evidence/prerequisites-and-coverage.md','S10 PDFp7 rest Example5'),
        ('technical','pass','Independent originals/source/math audit and author changed-task calculations complete.',audit,'C4 model witness.'),
        ('final_decimals','pass','Twenty-six frozen printed validation values freshly recomputed and rounding compared.',ROOT/'evidence/final-numerical-checks.json','"failed": []'),
        ('source_syntax','pass','293 expressions, tasks/help, source-format and links inspected with no mechanical findings.',ROOT/'evidence/mechanical-checks.json','"findings": []'),
        ('local_visual','pass','Every exact saved PNG viewed at original resolution; edges/text/legends complete.',audit,'Exact PNG views show complete readable titles'),
        ('destination','unverified','Complete actual final GitHub expression/style/figure/click inspection is root-owned and pending.',audit,'Full final GitHub preservation'),
        ('final_review','unverified','Author full reconstruction complete; destination and independent SASIS are pending, so no global acceptance.',audit,'Actual final destination review and separate fresh SASIS remain pending.')]
manifest['output_checks']=[dict(id=id,description=reason,**cond(status,reason,path,phrase)) for id,status,reason,path,phrase in checks]
write(STATE/'manifest.json',manifest)
topic=json.loads((STATE/'topics/local-approximation.json').read_text(encoding='utf-8'))
topic['source_reads']=reads
ledger=json.loads((ROOT/'evidence/obligation-ledger.json').read_text(encoding='utf-8'))
phrases={'T1':'C1 reconstruction witness.','T2':'C2 representation/substitution witness.',
         'T3':'C2 limit witness.','T4':'C3 coefficient witness.','T5':'T5-T8 applicability.',
         'T6':'T5-T8 applicability.','T7':'T5-T8 applicability.','T8':'T5-T8 applicability.',
         'T9':'T9 scope and load.','T10':'Numerical check scope.',
         'T11':'T11 source and local visual witness.','T12':'T12 acceptance boundary.'}
topic['requirements']={r['id']:cond(r['status'],r['trigger']+'; '+r['check'],audit,phrases[r['id']]) for r in ledger['requirements']}
topic['gaps']=[]
write(STATE/'topics/local-approximation.json',topic)
def snapshot(topic_id=None):
    cmd=[sys.executable,'-B',str(HELPER),'dependencies','--state',str(STATE)]
    if topic_id:cmd+=['--topic',topic_id]
    p=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8',check=True)
    return json.loads(p.stdout)
topicdeps=snapshot('local-approximation'); globaldeps=snapshot()
for v in topic['requirements'].values():v['dependencies']=topicdeps
for v in manifest['output_checks']:v['dependencies']=globaldeps
write(STATE/'topics/local-approximation.json',topic);write(STATE/'manifest.json',manifest)
(STATE/'RUN.md').write_text('PROF D008 author state\n\nExact available task: evidence/original-task-handover.txt. Root retains original user conversation.\n\nManual full skill/source activation occurred before drafting; helper init/begin-topic occurred after freeze to record the final bookkeeping. Its timestamp is not presented as pre-draft activation.\n\nConnected topic local-approximation covers C1-C4 andS01-S10. Conventions: evidence/prerequisites-and-coverage.md. Complete access: evidence/input-access.md.\n\nFrozen six constituents: evidence/teaching-freeze.json. Author reconstruction: evidence/author-audit.md. No learner-facing bytes changed after completion.\n\nNext action: root completes actual GitHub destination and separate fresh SASIS; preserve frozen bytes. Author T11 and global final review remain unverified.\n',encoding='utf-8')
for args,out in [(['--topic','local-approximation'],'topic-check.json'),([], 'full-state-check.json')]:
    p=subprocess.run([sys.executable,'-B',str(HELPER),'check','--state',str(STATE),*args,'--json'],capture_output=True,text=True,encoding='utf-8')
    (ROOT/'evidence'/out).write_text(p.stdout,encoding='utf-8')
    print(out,p.returncode,p.stdout)
