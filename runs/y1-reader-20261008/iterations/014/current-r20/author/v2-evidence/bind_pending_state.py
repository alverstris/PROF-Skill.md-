from pathlib import Path
import json,hashlib,subprocess
root=Path.cwd(); a=root/'runs/y1-reader-20261008/iterations/014/current-r20/author'; e=a/'v2-evidence'; st=e/'.prof-state'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text())
def save(p,d):p.write_text(json.dumps(d,indent=2)+'\n')
def ev(p,start,end):return {'path':str(p.relative_to(a)),'sha256':sha(p),'locator':{'kind':'lines','start':start,'end':end}}
old=load(a/'.prof-state/manifest.json'); ot=load(a/'.prof-state/topics/d014.json'); m=load(st/'manifest.json');t=load(st/'topics/d014.json')
m['required_topics']=old['required_topics']; m['sources']=old['sources']
m['outputs']=[{'id':'teaching','path':'teaching-v2.md','sha256':sha(a/'teaching-v2.md')}]
t['source_reads']=ot['source_reads']
extras=[('original-author-audit',a/'author-audit.md','Full original author reconstruction and requirement witnesses; unchanged teaching route rechecked in current reconstruction.'),('root-source-review',a.parent/'root-source-review.md','Entire 38-line source review read; independently validates original source conditions and corrections.'),('root-presolutions',a.parent/'root-independent-presolutions-v1.md','All seven independent presolutions read after original author solutions were frozen; unchanged answers agree.'),('original-reader',a.parent/'sasis-v1/reader-original.md','All 188 lines read in two packets; historical full baseline and v1 reading reports no mathematical prerequisite gap, not a fresh v2 pass.'),('original-destination',a.parent/'destination-v1/final-audit.json','Complete actual destination report read; established NAV-1 and MATH-1.'),('original-navigation',a.parent/'destination-v1/positive-navigation-audit.json','Complete positive navigation report read; all seven triples lacked supported links.'),('original-math-failure',a.parent/'root-destination-math-failure-verification.json','Complete twelve-row root failure verification read; thirteen thin-space commands accounted for.'),('current-reconstruction',e/'reconstruction.md','Complete current route reconstruction; read after full ordered teaching read, corrected L6 count before evidence freeze.')]
for ident,p,note in extras:
 m['sources'].append({'id':ident,'path':str(p),'sha256':sha(p),'portions':[{'id':'whole','locator':'entire file','disposition':'required','reason':note,'evidence':[]}]})
 m['required_topics'][0]['source_portions'].append({'source_id':ident,'portion_id':'whole'})
 t['source_reads'].append({'source_id':ident,'portion_id':'whole','status':'read','reviewed_sha256':sha(p),'note':note})
for k,v in ot['requirements'].items():
 t['requirements'][k]={'applicable':True,'status':'pass' if int(k[1:])<=10 else 'pending','reason':v['reason'] if int(k[1:])<=10 else 'Current local repair checks pass; fresh v2 reader, actual destination and root final acceptance remain pending. No browser clicks or live pixels claimed.','evidence':([*v['evidence'],ev(e/'reconstruction.md',13,43)] if int(k[1:])<=10 else []),'dependencies':[]}
 for c in ['T1','T2','T3','T4','T5','T6','T7','T8','T9','T10']:
  if k==c:t['requirements'][k]['reason']+=' Rechecked at v2 by complete ordered route reconstruction and exact change closure; v1 status alone is not carried as proof.'
t['gaps']=[{'id':i,'question':q,'consequential':True,'status':'unverified','reason':'Local source repair and complete exact-difference checks pass; actual v2 destination check is not yet admitted.','next_action':'Root inspect actual published v2 destination and supply the complete evidence report.','evidence':[ev(e/'reconstruction.md',31,43)],'dependencies':[]} for i,q in [('nav-1','Do all repaired named anchors and links preserve the seven task/help/answer relationships at the actual GitHub destination?'),('math-1','Does the actual destination now preserve all 346 mathematical expressions after thirteen whitespace-command repairs?')]]
checks=[('coverage','pass','Full five-page source coverage and current integrated route reconstructed.',[ev(a/'author-audit.md',9,41),ev(e/'reconstruction.md',13,29)]),('technical','pass','All 26 calculations rerun plus three numerical cube-root comparisons; all mathematical token content retained.',[ev(e/'reconstruction.md',31,41)]),('repair_integrity','pass','Exact inverse reconstructs original bytes; all 23 original files preserved; all 310 inline and 24 unaffected display payloads unchanged.',[ev(e/'reconstruction.md',9,9),ev(e/'reconstruction.md',31,37)]),('final_review','pending','Root complete independent v2 acceptance pending.',[]),('sasis','pending','Fresh full v2 SASIS report and admission pending; historical original report does not establish this gate.',[]),('destination','pending','Actual GitHub v2 typography, full mathematics, and positive navigation report pending.',[])]
m['output_checks']=[{'id':i,'description':r,'applicable':True,'status':s,'reason':r,'evidence':evs,'dependencies':[]} for i,s,r,evs in checks]
save(st/'manifest.json',m);save(st/'topics/d014.json',t)
for name,args in [('topic',['--topic','d014']),('global',[])]:
 p=subprocess.run(['python','scripts/prof_state.py','dependencies','--state',str(st),*args],capture_output=True,text=True,check=True)
 (e/f'{name}-dependencies.json').write_text(p.stdout)
 deps=json.loads(p.stdout)
 if name=='topic':
  for v in t['requirements'].values():
   if v['status']=='pass':v['dependencies']=deps
 else:
  for v in m['output_checks']:
   if v['status']=='pass':v['dependencies']=deps
save(st/'manifest.json',m);save(st/'topics/d014.json',t)
(st/'RUN.md').write_text('''D014 v2 recovery index

Current immutable learner output: author/teaching-v2.md, SHA256 caf74a9a150f61d2531e8b2768abb1448fb7d5304818a9e1fcc73d02bead826b. One file, no companions or figures.

Exact instructions: ../request.txt. Incoming r20 skill: ../frozen-inputs/SKILL-r20.md; frozen bytes bind this topic even when root publishes metadata-only r21. Original author/.prof-state and all 23 original evidence files remain untouched.

Source/prerequisite/notation record: author/source-and-scope.md, full baseline read records and actual source/lec15.pdf; manifest binds exact portions. Actual v2 author reconstruction: ../reconstruction.md. Exact edits, inverse, all-math equality, and positive source navigation: ../repair-checks.json and ../math-token-preservation.json. Source/report historical inputs are declared dependencies, not fresh v2 acceptance.

Current local checks: T1–T10 author pass; 26 calculation checks pass; full ordered v2 read and seven prompt/hint/solution relations rechecked. NAV-1 and MATH-1 locally repaired but externally unverified. T11/T12 and fresh SASIS, destination, final review pending. No observed student mastery, browser clicks or live pixels claimed.

Next action: root supplies complete fresh v2 reader, actual destination and independent final-gate records; read them fully, bind exact dependencies, and update only this separate v2 state after the evidence is admitted. Until then NOT_READY is expected.
''')
for name,args in [('topic',['--topic','d014']),('full',[])]:
 p=subprocess.run(['python','scripts/prof_state.py','check','--state',str(st),*args],capture_output=True,text=True)
 (e/f'helper-{name}-check.txt').write_text(p.stdout+p.stderr+f'\nexit_code={p.returncode}\n')
 print(name,p.stdout,p.returncode)
