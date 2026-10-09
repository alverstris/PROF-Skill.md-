from pathlib import Path
import json,hashlib,subprocess,sys,shutil
from datetime import datetime,timezone
p=Path(__file__).resolve().parent;root=p.parents[1];s=p/'.prof-state';helper=Path('/workspace/scratch/6a5c7131498d/prof-r19/scripts/prof_state.py')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def ev(rel):
 q=root/rel;return {'path':rel,'sha256':sha(q),'locator':{'kind':'lines','start':1,'end':len(q.read_text().splitlines())}}
m=json.loads((s/'manifest.json').read_text());t=json.loads((s/'topics/mvt.json').read_text())
for src in m['sources']:assert sha(src['path'])==src['sha256'],src['id']
for o in m['outputs']:assert sha(root/o['path'])==o['sha256'],o['id']
for x in [m['skill'],m['request']]:assert sha(x['path'])==x['sha256']
new=[('destination-review','destination-v2/review.md','Complete final review and all limitations read.'),('destination-audit','destination-v2/final-audit.json','Complete exact destination/AST/native preview audit read.'),('destination-visual','destination-v2/visual-inspection.json','Complete six-figure and all13final-page findings read; destination reviewer owns actual visual inspection.'),('root-destination','root-destination-v2-disposition.md','Complete independent final destination disposition read.'),('root-pdf','root-final-pdf-independent.json','Complete independent canonical PDF/page/link check read.'),('issue-register','issue-register.md','Entire register including every original issue, correction, unknown cause and final limit read.'),('content-acceptance','final-acceptance.md','Complete independent root content acceptance read; publication and queue closure remain separate.'),('raster-correspondence','destination-v2/preview-final4/exact-PDF-raster-correspondence.json','All13 canonical-to-saved RGB comparisons read.'),('preview-failure-1','destination-v2/preview-integrity-failure.json','Complete failed integrity record read; rejected damaged PDF not accepted.'),('preview-failure-2','destination-v2/preview-integrity-second-check.json','Complete both damaged/canonical integrity observations read; cause unknown.'),('destination-archive','destination-v2-archive.json','Header read and all171entries independently byte/hash/zip verified; not a new full subject read of every archive member.'),('final-integrity','final-state/v2-final/final-integrity-check.json','Actual author all-entry archive and canonical structure/hash verification.'),('final-reconstruction','final-state/v2-final/final-reconstruction-disposition.md','Current full-route reconstruction bridge, final finding dispositions and honest gate scope.'),('canonical-preview','destination-v2/preview-final4/verified-build.pdf','Actual entire binary bytes hashed and opened for13page/EOF check. Full-page visual inspection is separately evidenced by destination reviewer/root records; no new author visual-read claim.')]
for ident,rel,reason in new:
 assert ident not in [x['id'] for x in m['sources']]
 q=root/rel;m['sources'].append({'id':ident,'path':str(q),'sha256':sha(q),'portions':[{'id':'full','locator':'whole file within stated review scope','disposition':'required','reason':reason,'evidence':[]}]})
 m['required_topics'][0]['source_portions'].append({'source_id':ident,'portion_id':'full'})
 t['source_reads'].append({'source_id':ident,'portion_id':'full','status':'read','reviewed_sha256':sha(q),'note':reason})
bridge='final-state/v2-final/final-reconstruction-disposition.md'
for i in range(1,11):
 c=t['requirements'][f'T{i}'];c['reason']+=' Final current gate disposition supersedes historical pending references in original witnesses: complete final evidence has now been reviewed as recorded in final-reconstruction-disposition.md.';c['evidence'].append(ev(bridge))
t['requirements']['T11']={'applicable':True,'status':'pass','reason':'Actual immutable server parser preserves all214math nodes/fullprose; actual CSS/article/assets checked. Complete faithful13page canonical preview inspected with exact AST and pixel correspondence. Navigation pass covers server anchors/relationships and native PDF destinations only. Live pixels, client MathJax, computed styles, responsive behavior and viewer clicks remain unobserved. Damaged PDFs rejected; stable canonical identity independently verified.','evidence':[ev(x)for x in ['destination-v2/review.md','destination-v2/final-audit.json','destination-v2/visual-inspection.json','root-destination-v2-disposition.md',bridge]],'dependencies':[]}
t['requirements']['T12']={'applicable':True,'status':'pass','reason':'Complete source/baseline-to-route reconstruction, all tasks/help/ending, author/root technical checks, fresh two-input SASIS and exact destination/native preview results reconciled. Every material issue has actual scoped disposition; failures and unknown causes preserved. Root content acceptance saved; no learner-outcome claim or publication/queue-closure claim.','evidence':[ev(x)for x in ['issue-register.md','final-acceptance.md',bridge]],'dependencies':[]}
reasons={
'destination_math':('All214 actual immutable server payloads exact after one HTML parse, including190inline/24display; fullprose/math stream preserved. Native faithful-preview AST matches. No client MathJax execution claim.',['destination-v2/final-audit.json','root-destination-v2-disposition.md']),
'destination_visual':('All actual seven constituent bytes, six full figure views, parsed prose/style structure and21CSS checked. All13 canonical native-preview pages inspected and reproduced pixel-exactly from stable verified-build.pdf. Pagination limits disclosed; no live browser pixels/computed-style or polished user PDF claim.',['destination-v2/visual-inspection.json','destination-v2/review.md','root-destination-v2-disposition.md','final-state/v2-final/final-integrity-check.json']),
'navigation_targets':('All27actual parsed anchors/37ordered links and P1–P6 task/hint/solution/return relationships correct. Canonical PDF all27native targets/37logical references resolve; hints page10 exclude full solutions pages11–12. Annotation/destination checks only; live browser/PDF-viewer clicks remain unobserved.',['destination-v2/final-audit.json','root-final-pdf-independent.json','root-destination-v2-disposition.md']),
'final_review':('Actual root final complete source/route/help/ending, independent math, full original SASIS and destination dispositions accepted current content. All material issues resolved within disclosed limits; original failures and unknown causes retained. Publication/readback and queue closure are subsequent root actions.',['final-acceptance.md','issue-register.md',bridge])}
for c in m['output_checks']:
 if c['id'] in reasons:
  reason,refs=reasons[c['id']];c.update(status='pass',reason=reason,evidence=[ev(x)for x in refs])
 else:c['evidence'].append(ev(bridge))
write(s/'manifest.json',m);write(s/'topics/mvt.json',t)
for label,args in [('topic',['--topic','mvt']),('global',[])]:
 r=subprocess.run([sys.executable,str(helper),'dependencies','--state',str(s),*args],capture_output=True,text=True);assert r.returncode==0,r.stdout+r.stderr
 (p/f'final-{label}-dependencies.json').write_text(r.stdout);deps=json.loads(r.stdout)
 for c in (t['requirements'].values()if label=='topic'else m['output_checks']):
  assert c['status']=='pass';c['dependencies']=deps
write(s/'manifest.json',m);write(s/'topics/mvt.json',t)
(s/'RUN.md').write_text('D013 frozen final v2 state\n\nIncomingr19 and exact control/request snapshots remain immutable application condition. Read final-reconstruction-disposition.md, exact frozen request and current topic on recovery. T1–T12 and all seven declared output checks pass in their explicit scopes; no live-browser/clientMathJax/computed-style/viewer-click claim. Only verified-build.pdf is accepted as native preview; damaged main.pdf files preserved/rejected with unknowncause. Original v1 state, prepared-pending-state and after-sasis-pending-state remain preserved.\n\nNext action: root independently reruns helper/inventory, publishes evidence and metadata-onlyr20, verifies canonical/fetched byte identities and closes queue. Author has not published/closed. Do not edit bound evidence; add later publication records separately. No learner-outcome claim.\n')
for label,args in [('topic',['check','--topic','mvt']),('global',['check']),('status',['status','--json'])]:
 r=subprocess.run([sys.executable,str(helper),args[0],'--state',str(s),*args[1:]],capture_output=True,text=True)
 (p/f'final-{label}-readiness.txt').write_text(r.stdout+r.stderr);print(label,r.returncode,r.stdout)
 assert r.returncode==0
shutil.copytree(s,p/'final-ready-state')
files=[]
for q in sorted(p.rglob('*')):
 if q.is_file()and q.name!='final-inventory.json':files.append({'path':str(q.relative_to(p)),'bytes':q.stat().st_size,'sha256':sha(q)})
write(p/'final-inventory.json',{'frozen_at_utc':datetime.now(timezone.utc).isoformat(),'status':'MECHANICALLY_READY within declared evidence scope; root publication/closure separate','incoming_skill_sha256':m['skill']['sha256'],'source_dependencies':len(m['sources']),'teaching_constituents':len(m['outputs']),'files':files})
print('Final file count',len(files),'sources',len(m['sources']),'outputs',len(m['outputs']))
