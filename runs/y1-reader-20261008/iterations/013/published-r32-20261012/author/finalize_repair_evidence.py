from pathlib import Path
import json,hashlib,shutil,subprocess,zipfile
w=Path('/workspace/scratch/f9c0b7fc7e76/d013-clean-r32-20261012'); root=w.parent/'root-review-d013-r32'; e=w/'evidence'; rr=e/'root-final'; rr.mkdir(exist_ok=True)
for n in ['destination/navigation-causal-review.md','root-final-disposition.json','candidate-r33-review/package-identity-verification.json','candidate-r33-review/behavioral-repair.diff','destination/visual-review/visual-review.md','destination/visual-review/supplemental-visibility/supplemental-visibility.md','destination/math-preservation.md','destination/earlier-affected-cases/earlier-r33-navigation-observations.json']:
 dst=rr/n;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(root/n,dst)
a=w.parent/'source-audit-archives/d013-r32-root-complete-review-20261012.zip'
assert hashlib.sha256(a.read_bytes()).hexdigest()=='ede9ea58ff595865294fc52bfe1bc04b6692f1313f007a1bb0988375e413ba91'
with zipfile.ZipFile(a) as z:
 assert z.testzip() is None
 assert len(z.infolist())==87
shutil.copyfile(a,e/'root-complete-original.zip')
shutil.copyfile(a.with_name(a.stem+'-manifest.json'),e/'root-complete-archive-manifest.json')
assert hashlib.sha256((e/'root-complete-archive-manifest.json').read_bytes()).hexdigest()=='ab8e93b045aab78c07bb32450ebeaa5d123ca75184b82cbe166891a2b76c96b8'
d={
 'material':'D013','incoming_prof':'2026-10-12-r32','outgoing_prof':'2026-10-12-r33','status':'NOT_READY; immutable teaching unaccepted; verified material destination failure',
 'whole_audits_complete':True,'frozen_constituents_edited':False,
 'source_coverage':{'pages':5,'qualifications':7,'disposition':'All seven independently inspected source qualifications resolved by complete fresh teaching before freeze; evidence/source-audit-dispositions.json preserves exact mapping.'},
 'technical':{'demands':42,'disposition':'Independent prompt-first solutions and all-source/figure/teaching/help audit found no material subject defect; full original technical archive preserved.'},
 'sasis':{'disposition':'No demonstrated material instructional failure. Full original report retained; 55 actual-delivery records cover all four text inputs and three figures with contiguous verified slice hashes. Reader reconstructed access log after accumulator error; raw55 platform IDs unavailable. Qualified reader-attested actual access/order, not independently available transcript. Separate supplement retained unchanged.', 'R01':'P3 phrase about finite width and different slopes is scoped to explicit x squared numerical example; no established universal false implication.', 'R02':'Reconstructed recording qualification is implementation evidence limitation; no demonstrated skipped content/order or new instructional failure. No invented repair.'},
 'destination':{'math':314,'prose_characters':30124,'text_links':44,'named_anchors':18,'image_alts':3,'preservation':'pass all ordered actual expressions/prose/link/anchor/alt structures','visual':'Complete full-resolution visual review plus separate two-region supplement resolves toolbar/cursor capture artifacts. No figure/prose layout defect established.', 'navigation':'fail: D013 first hints P6 return target2234.453125 outside936viewport despite final233math and3complete images; repeat407.453125 visible does not erase miss. Auxiliary P2 miss is qualified contemporaneous tool witness, not independent saved raw DOM.'},
 'controlled_diagnosis':{'fixture_commit':'c8767dcde9ca83823051f822bef8fe658b717118','fixed':'Same neutral text,81math expressions, targets after normalized names and identical PNGbytes; only three image embeds vary. Separate immutable image URLs and help-first first visits; no prior main/image visit, scrolling or full-page capture before observation.', 'A':'Unloaded images zero boxes; settled target2564.140625 outside936viewport.', 'B':'Intrinsic1600x1080 markup reserves unloaded proportional627.0625px boxes; settled target737.140625 visible.', 'controls':'Same final article5485.140625 and81math; targetdifference1827 matches initial layoutdifference1827.1875 within rounding; later cachedP2 both125.046875 visible.', 'causal_scope':'Demonstrated image-reservation cause in tested condition, not universal guarantee across caches or browser states.'},
 'earlier_dependencies':{'census':'All15 prior accepted cases and50 exact accepted/current constituents inspected; markup exposure alone is not failure.', 'D007':'Retain accepted: bounded first-use P6 visible721.75/936,200math,1completeimage. Immediate observation still hints; no unloaded-state claim.', 'D008':'Reopen: earlier actual settled P6 miss2410.734375/936 with4unsizedimages preceding; preserve originally unrecorded loading uncertainty, append current causal-class assessment.', 'D016':'Reopen: first-use P5 immediate3incompletezero imageboxes/196math; settled target1811.84375/936 with3completeimages/196math; ordinary proof shows earlier P3/PartF.'},
 'repair':{'changed':['SKILL.md','references/execution-protocol.md','references/sasis/profile-manifest.json'],'unchanged':33,'internal_declarations':34,'trigger':'Images preceding fragment destinations in linked teaching/help.','action':'Reserve exported aspect geometry with host-supported markup, inspect unloaded/loaded geometry, check first-use help-to-late-main before warming images and ordinary repeat forward/return routes, preserve first misses and honest cache limits.','observable_check':'Actual settled target visible and faithful image aspect; controlled same-content fixture for diagnosis; reopen only actual failed dependencies.','limits':'Engineering inference from actual destination observations; no learner-performance research claim. Metadata-only candidate remains preserved but unused.'},
 'progress_after_checkpoint':{'all_ids':147,'eligible':76,'excluded':71,'accepted':13,'remaining':63,'active':'D013','next_pending_after_active':'D008','reopened':['D008','D016']},
 'next':'Publish and read back entire cumulative repaired package/evidence, then canonical progress preserving all prior evidence, then fresh fork:none same-D013 coordinator with only operational/original inputs. No frozen teaching patch.'}
(e/'final-adjudication.json').write_text(json.dumps(d,indent=2)+'\n')
mp=w/'.prof-state/manifest.json';tp=w/'.prof-state/topics/mvt-inequalities.json';m=json.loads(mp.read_text());t=json.loads(tp.read_text())
def witness(p):
 b=(w/p).read_bytes();return {'path':p,'sha256':hashlib.sha256(b).hexdigest(),'locator':{'kind':'lines','start':1,'end':len(b.decode().splitlines())}}
base=['python',str(w/'verified-prof/scripts/prof_state.py')]
def deps(topic=False):
 r=subprocess.run(base+['dependencies','--state',str(w/'.prof-state')]+(['--topic','mvt-inequalities'] if topic else []),capture_output=True,text=True);assert r.returncode==0,r.stdout+r.stderr;return json.loads(r.stdout)
td=deps(True);gd=deps()
if isinstance(td,dict): td=td.get('dependencies',td)
if isinstance(gd,dict): gd=gd.get('dependencies',gd)
for k,c in t['requirements'].items():
 if int(k[1:])<=9:
  c['reason']=c['reason'].replace('Author audit only; independent whole review still pending.','Author reconstruction corroborated by whole technical and qualified fresh-reader review; this is not observed learner mastery.')
  c['evidence'] += [witness('evidence/root-content/whole-content-review.md')]
  c['dependencies']=td
for k,status,reason,ev in [
 ('T10','pass','All original pages/figures,42 independently solved prompt demands, complete source/teaching/help and official theorem foundation reviewed; no material mathematical defect established.','evidence/technical/full-technical-review.md'),
 ('T11','fail','Complete destination preservation and visual review pass, but actual first-use help return misses intended target. Controlled image geometry cause established; frozen teaching remains unaccepted.','evidence/root-final/destination/navigation-causal-review.md'),
 ('T12','pass','Whole audits completed and original reports preserved with exact limits. Honest nonacceptance records destination failure and access qualification; no mastery or global readiness claim.','evidence/final-adjudication.json')]:
  t['requirements'][k]={'applicable':True,'status':status,'reason':reason,'evidence':[witness(ev)],'dependencies':td}
checks={'coverage':('pass','All five source pages,seven source qualifications and complete teaching/help/figures mapped and inspected.','evidence/source-audit-dispositions.json'),'technical':('pass','All42 independent prompt demands and full source/teaching/figures checked; no demonstrated subject defect.','evidence/technical/full-technical-review.md'),'sasis':('pass','Original complete fresh-reader report admitted with reconstructed-access log qualification; no demonstrated missing read/order/content failure.','evidence/sasis-admission-and-dispositions.json'),'destination':('fail','Actual first-use target offscreen; successful repeats do not erase observed failure.','evidence/root-final/destination/navigation-causal-review.md'),'final_review':('fail','Whole review complete; integrated acceptance fails because the destination navigation fails. Full r33 repair and fresh same-case generation required.','evidence/final-adjudication.json')}
for c in m['output_checks']:
 status,reason,ev=checks[c['id']];c.update(status=status,reason=reason,evidence=[witness(ev)],dependencies=gd)
mp.write_text(json.dumps(m,indent=2)+'\n');tp.write_text(json.dumps(t,indent=2)+'\n')
for scope in ['topic','full']:
 args=base+['check','--state',str(w/'.prof-state')]+(['--topic','mvt-inequalities'] if scope=='topic' else [])
 r=subprocess.run(args,capture_output=True,text=True);(e/f'helper-{scope}-check.txt').write_text(r.stdout+r.stderr);assert r.returncode==1,(scope,r.returncode,r.stdout,r.stderr)
 r=subprocess.run(base+['status','--state',str(w/'.prof-state'),'--json']+(['--topic','mvt-inequalities'] if scope=='topic' else []),capture_output=True,text=True);(e/f'helper-{scope}-status.json').write_text(r.stdout);print(scope,r.returncode,r.stdout[:500])
(w/'.prof-state/RUN.md').write_text('D013 r32 immutable at36e3d042ba459f3048e1489fd12045029f61abbb. All whole audits complete; NOT_READY due actual first-use navigation failure. Full original technical/reader/root reports preserved. Controlled image geometry diagnosis supports cumulative r33 repair. Reopen only D008,D016; D007 bounded pass retained. Canonical checkpoint after publication will13accepted/63remaining/71excluded,147IDs/order. ActiveD013 fresh same-case retry; nextD008. Sole publisher current coordinator. Next: publish and read back complete36 repairedpackage plus preserved evidence, then canonical checkpoint; root independent verification before fresh transfer. Exact constraints inputs/operational-handover.json; final evidence evidence/final-adjudication.json. Frozen teaching never patched.\n')
print('final evidence and helper saved')
