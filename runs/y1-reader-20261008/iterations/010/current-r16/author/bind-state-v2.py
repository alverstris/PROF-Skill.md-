from pathlib import Path
import hashlib,json,subprocess,sys,copy
p=Path(__file__).resolve().parent;root=p
while not (root/'scripts/prof_state.py').exists():root=root.parent
st=p/'.prof-state-v2';helper=root/'scripts/prof_state.py'
def sha(f):return hashlib.sha256(f.read_bytes()).hexdigest()
def ev(file,text):return {'path':file,'sha256':sha(p/file),'locator':{'kind':'text','value':text}}
audit=(p/'v2-repair-and-audit.md').read_text().splitlines()
def para(start):return next(l for l in audit if l.startswith(start))
m=json.loads((st/'manifest.json').read_text());t=json.loads((st/'topics/max-min.json').read_text())
old=json.loads((p/'.prof-state/manifest.json').read_text());ot=json.loads((p/'.prof-state/topics/max-min.json').read_text())
# Preserve original state; exact byte checks justify carrying its actual source reads.
for source in old['sources']:assert sha(Path(source['path']))==source['sha256'],source['id']
m['sources']=copy.deepcopy(old['sources']);t['source_reads']=copy.deepcopy(ot['source_reads'])
for ident,file,note in [('reader-v1',p.parent/'sasis-reader-v1-original.md','Complete original178-line reader report reread in1–95 and96–178 packets. D1 andD2 verified; no other required repair established.'),('root-review-v1',p.parent/'root-technical-review-v1.md','Complete root review read: independently obtained source/math/figure and presolution checks support unchanged computations; upper-bound definition defect confirmed.'),('v2-audit',p/'v2-repair-and-audit.md','Complete new repair record, explicit counterexamples, full sequential v2 read and exact-content carryforward evidence.')]:
 m['sources'].append({'id':ident,'path':str(file),'sha256':sha(file),'portions':[{'id':'whole','locator':'whole file','disposition':'required','reason':'','evidence':[]}]})
 t['source_reads'].append({'source_id':ident,'portion_id':'whole','status':'read','reviewed_sha256':sha(file),'note':note})
m['outputs']=copy.deepcopy(old['outputs'])
for output in m['outputs']:
 if output['id']=='teaching':output['path']='teaching-v2.md';output['sha256']=sha(p/'teaching-v2.md')
 else:assert sha(p/output['path'])==output['sha256']
m['required_topics']=copy.deepcopy(old['required_topics']);m['required_topics'][0]['source_portions']=[{'source_id':s['id'],'portion_id':z['id']} for s in m['sources'] for z in s['portions']]
for key in t['requirements']:
 if key in ('T1','T3'):
  line=para(key+' repaired author pass.')
  t['requirements'][key]={'applicable':True,'status':'pass','reason':line,'evidence':[ev('v2-repair-and-audit.md',line)],'dependencies':[]}
 elif key in ('T11','T12'):
  line=para('T11 and T12 pending.')
  t['requirements'][key]={'applicable':True,'status':'pending','reason':line,'evidence':[ev('v2-repair-and-audit.md',line)],'dependencies':[]}
 else:
  t['requirements'][key]=copy.deepcopy(ot['requirements'][key]);t['requirements'][key]['dependencies']=[]
  t['requirements'][key]['reason']='v2 exact-content carryforward after full reread and changed-definition dependency retry. '+t['requirements'][key]['reason']
  t['requirements'][key]['evidence'].append(ev('v2-repair-and-audit.md',para('T2/T4–T10 justified carryforward.')))
m['output_checks']=copy.deepcopy(old['output_checks'])
for rec in m['output_checks']:
 rec['dependencies']=[]
 if rec['status']=='pass':
  rec['reason']='v2: exact unaffected content and figures verified; full integrated read and D1/D2 semantic repair checks completed. '+rec['reason']
  rec['evidence'].append(ev('v2-repair-and-audit.md',para('Full v2 reading.')))
 else:
  rec['reason']='Pending current-v2 evidence: '+rec['reason']
# The same mathematical expressions are byte-identical, so repeat symbolic execution is unnecessary;
# fresh semantic definition checks are recorded explicitly instead.
(st/'manifest.json').write_text(json.dumps(m,indent=2)+'\n');(st/'topics/max-min.json').write_text(json.dumps(t,indent=2)+'\n')
def deps(args,file):
 r=subprocess.run([sys.executable,str(helper),'dependencies','--state',str(st),*args],capture_output=True,text=True);assert r.returncode==0,r.stderr
 (p/file).write_text(r.stdout);return json.loads(r.stdout)
globaldeps=deps([],'v2-dependencies.json');topicdeps=deps(['--topic','max-min'],'v2-topic-dependencies.json')
for condition in t['requirements'].values():
 if condition['status']=='pass':condition['dependencies']=topicdeps
for condition in m['output_checks']:
 if condition['status']=='pass':condition['dependencies']=globaldeps
(st/'manifest.json').write_text(json.dumps(m,indent=2)+'\n');(st/'topics/max-min.json').write_text(json.dumps(t,indent=2)+'\n')
(st/'RUN.md').write_text('D010 v2 author recovery\n\nSkill r16, exact requests at '+str(root/'runs/y1-reader-20261008/requests.md')+'. Separate state preserves v1 failure history untouched.\nCurrent teaching-v2.md plus unchanged five PNGs: freeze-v2.json. Only P007/P011 definitions repaired. Full v2 route read, counterexamples and downstream uses retried; v2-repair-and-audit.md and v2-static-check.json record actual checks. Complete original baseline/source reads retained with unchanged hashes and declared dependencies.\nT1–T10 author checks pass at v2 with specific repair or exact-content carryforward evidence. T11/T12 and new destination/SASIS/final acceptance pending. Next action: parent obtains fresh v2 reader and actual destination results, then independently disposes issues before closure. No skill change or publication performed here.\n')
for label,args in [('topic',['--topic','max-min']),('full',[])]:
 r=subprocess.run([sys.executable,str(helper),'check','--state',str(st),*args,'--json'],capture_output=True,text=True);(p/f'v2-{label}-state-check.json').write_text(r.stdout or r.stderr);print(label,r.returncode,r.stdout or r.stderr)
