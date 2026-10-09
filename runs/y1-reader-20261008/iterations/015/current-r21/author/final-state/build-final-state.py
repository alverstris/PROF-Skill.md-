from pathlib import Path
import json,hashlib,shutil,subprocess,datetime,zipfile
F=Path(__file__).resolve().parent;A=F.parent;C=A.parent;R=A.parents[5];S=F/'.prof-state';E=A/'v2-evidence'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,d):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(d,indent=2)+'\n')
def cp(src,rel):
 p=F/rel;p.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(src,p);assert p.read_bytes()==src.read_bytes();return p
# Preserve and independently verify both previous checkpoints.
preserved={}
for name,base,manifest in [('v1',A,A/'author-packet-manifest-v1.json'),('v2',A,E/'author-packet-manifest-v2.json')]:
 d=json.loads(manifest.read_text())
 for f in d['files']:assert sha(base/f['path'])==f['sha256'],f['path']
 preserved[name]={'manifest_sha256':sha(manifest),'all_files_verified':len(d['files'])}
# Binding frozen controls avoids upcoming metadata-only root skill release.
skill=cp(A/'controls/SKILL.md','inputs/controls/SKILL.md');tool=cp(A/'controls/scripts/prof_state.py','inputs/controls/prof_state.py')
(F/'request.txt').write_text('''Parent /root final-state assignment, verbatim:
Root final integrated semantic checks accepted; prepare final helper packet NOW, own ONLY new author/final-state/**. Read final-review.md, issue-register-final.md, root-destination-v2-disposition.md, root-sasis-v2-disposition.md, sasis-v2-admission-result.json, root-parser-v2-verification.json, root-preview-native-verification.json and root-preview-attempt3-correction.json at current-r21 plus complete stable destination-v2/review.md/final-audit.json/visual-inspection.json. Preserve original and v2-evidence packets. All303 destinationfiles archived+roundtrip in destination-v2-complete.zip; actualteachingcommit f531ccd..., source/CSS/parser/nativecontract/full12page internalpreview checks scope-bound as reports; NO livebrowser/MathJax/computedstyles/click orOverleaf claims. NativePDFcanonical attempt3 hash4def..., all24targetlabelpages/all31links, hints9solutions10–12. Preview attempts1/2 rejected preserved, rootfooterconcernwithdrawn with exactgeometry/pixel/crops (notdocumentdefect). Build final prof_state with current substantive evidence for T1–T12/G08/eightoutputgates, all actual dependencies hashbound/current locators, standalone copied dependency packet if useful for stable helper. Mechanical checks notsemanticproof. Run topic+fullcheck; reportall files/deps withmanifest. No teaching, skill, priorrecord,queueorpublication edits. Root owns outgoingr22metadata, actualpublication/readback/closure.

Parent follow-up, verbatim:
Final helper should bind frozen r21 controls/inputs, not mutable root SKILL.md directly: root will subsequently increment ONLY its metadata to r22, preserving exact instructional bytes. Include copied dependencies/current evidence so final helper remains truthful and mechanically current under release metadata change. Root complete finalcontent publication is in progress; don't mutate bound final-review/root reports.
''')
# Copy every original declared source and retain exact read scope rather than invent new source reading.
m=json.loads((E/'.prof-state/manifest.json').read_text());t=json.loads((E/'.prof-state/topics/d015.json').read_text())
original_sources=[]
for src in m['sources']:
 old=Path(src['path']);new=cp(old,'inputs/sources/'+src['id']+'/'+old.name);assert sha(new)==src['sha256'];original_sources.append({'id':src['id'],'original_path':str(old),'copy_path':str(new.relative_to(F)),'sha256':sha(new)});src['path']=str(new)
# Copy all currently referenced original evidence and map to standalone project-relative paths.
def map_evidence(ev):
 if ev['path']=='@request':return ev
 old=A/ev['path'];rel='evidence/prior/'+ev['path'];new=cp(old,rel);assert sha(new)==ev['sha256'];ev['path']=rel;return ev
for req in t['requirements'].values():req['evidence']=[map_evidence(ev) for ev in req['evidence']]
for g in t['gaps']:g['evidence']=[map_evidence(ev) for ev in g['evidence']]
# Full final reports actually read during this assignment.
records=['final-review.md','issue-register-final.md','root-destination-v2-disposition.md','root-sasis-v2-disposition.md','sasis-v2-admission-result.json','root-parser-v2-verification.json','root-preview-native-verification.json','root-preview-attempt3-correction.json','destination-v2/review.md','destination-v2/final-audit.json','destination-v2/visual-inspection.json','destination-v2-archive-verification.json','root-teaching-v2-review.md','sasis-v2/report.md','sasis-v2/access-log.md']
def add_source(id,p,locator,note):
 src={'id':id,'path':str(p),'sha256':sha(p),'portions':[{'id':'whole','locator':locator,'disposition':'required','reason':note,'evidence':[]}]};m['sources'].append(src);t['source_reads'].append({'source_id':id,'portion_id':'whole','status':'read','reviewed_sha256':sha(p),'note':note})
for i,n in enumerate(records,1):
 p=cp(C/n,'evidence/final/'+n);add_source('final'+str(i),p,'Complete exact report', 'Complete report read in this final-state assignment. Root/reviewer observations remain attributed; their report scopes and unobserved limits are retained.')
for id,old in [('initial-request',A/'assignment.txt'),('repair-request',E/'assignment-v2.txt')]:
 p=cp(old,'inputs/requests/'+old.name);add_source(id,p,'Complete original exact assignment','Exact earlier author instructions retained as dependencies; read during their execution and preserved unchanged.')
# Archive binds all actual destination bytes, including rejected attempts and final raw/style/AST/PDF proof.
archive=cp(C/'destination-v2-complete.zip','evidence/destination-v2-complete.zip');archive_entries=[]
with zipfile.ZipFile(archive) as z:
 for name in z.namelist():
  if name.endswith('/'):continue
  data=z.read(name);rel=name.removeprefix('destination-v2/');local=C/'destination-v2'/rel
  if not local.exists():local=C/name
  assert local.is_file() and local.read_bytes()==data,name
  archive_entries.append({'path':name,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
assert len(archive_entries)==303
add_source('destination-archive',archive,'Complete ZIP member inventory and full-byte roundtrip against all303 preserved destination files','All303 archive members read for byte/hash integrity and compared with exact preserved files; semantic/visual review of their content is attributed to the complete root/reviewer reports, not relabelled as this author viewing every archive item.')
dump(F/'archive-member-verification.json',{'archive_sha256':sha(archive),'members':archive_entries,'all303_identical':True})
# Copy exact final nine-file learner bundle; no teaching changes.
frozen=json.loads((E/'freeze-manifest-v2.json').read_text());m['outputs']=[]
for i,f in enumerate(frozen['constituents'],1):
 p=cp(A/'v2'/f['path'],'artifacts/'+f['path']);assert sha(p)==f['sha256'];m['outputs'].append({'id':'file'+str(i),'path':str(p.relative_to(F)),'sha256':sha(p)})
cp(E/'freeze-manifest-v2.json','evidence/freeze-manifest-v2.json')
(F/'acceptance-record.md').write_text('''D015 final acceptance evidence integration

Scope. This final helper binds the nine exact D015-r21-v2 Markdown/figure constituents accepted by root at immutable teaching commit f531ccd1a3ec4b4918b96fbab30a7f6d8c03aafa. The complete frozen r21 skill, all previously declared sources, their exact reading scopes, original prerequisite/course-convention records, complete current author reconstruction, original constraints and all final reports are copied inside this packet. Upcoming root metadata-only r22 does not change these bytes or the teaching. This author writes no release/queue/publication record.

Read/access integration. Every named final report was read completely, including all453 final-audit lines, all12 page findings, all175 fresh SASIS report lines and its complete95-line access log. Author examined the current final acceptance and correction, rather than retaining original provisional reader wording as final status. Original T1–T10 content witnesses remain current for unchanged nine-file teaching, confirmed by exact output hashes and prior checkpoint manifests. No new full baseline/source reading or new blind answer attempt is claimed. Earlier actual source/baseline readings and independent root prompt-first checks retain their explicit provenance.

Coverage. C01–C10 in the copied original topic record and A01–A20 in the current author audit still cover all five original source pages, all three figures, operator aside, both independently corrected source errors and the full historical exam-list ending. Root current teaching/source review independently confirms this full scope. All five generated tasks have useful distinct hints and complete solutions. No required source portion is removed by the final state.

T1–T10. The copied author-audit-v2.md contains the complete substantive A01–A20 reconstruction and precise T1–T10 witnesses. Root-teaching-v2-review.md confirms every current content/help route and Q5 repair. The 18 zero mathematical residuals and rejecting -2/-4 candidate residuals are unchanged, as is the exact inverse proof; no math was changed by preview conversion. Those conditions remain pass on the actual unchanged artifacts, with all source and output dependencies rebound to the identical copies.

T11. Actual GitHub extraction preserves all398 ordered expressions/types, all three complete prose streams, all25 labels and all six historical notice items. Actual source/CSS evidence, with all21 fetched stylesheets and no applicable prose emphasis/heading/table-header nodes, is the styling witness. All six fetched figures were viewed by the destination reviewer. The exact three-file hint/answer route has all21 named targets, all31 cross-file references and all five complete task/help chains under the documented native path/anchor contract. The separate internal preview has exact complete AST correspondence, all12 final pages viewed, all24 native destinations on their actual label pages, all31 logical links and disjoint hint page9 versus solutions10–12. Canonical attempt3 is 220790 bytes, SHA2564def38d3eda70758f861fda78bbf1b3f26098a0a5dfbf892ace588dfa29b2725, with no substantive compilation diagnostic. Root independently matched all12 rasters to the canonical PDF. These observations support usable output within their recorded scopes. Live GitHub pixels, client MathJax, computed styles, responsive layout, browser/PDF-viewer clicks and Overleaf upload were not observed and are not claimed.

G08. Resolved within the actual documented destination/preview scope. The original21 comparison characters now parse exactly as intended, independently verified over every398 expression rather than a sample or second unescape. Source/CSS/native-contract checks and faithful full-preview checks are separate evidence, not interchangeable claims. Original preview attempts1/2 remain rejected for actual converter target/label faults; attempt3 corrects those without any learner change. The later root footer concern is withdrawn with exact geometry, all12 pixel matches and enlarged crops; it is a preserved review error, not a document defect or a reason to fabricate another repair.

T12. Root final-review.md accepts the complete final route and help and every diagnosed issue. The fresh reader provides58 chronological witnesses and complete baseline/nine-constituent access; root admitted it after independent full report/access and premise checks. Its two external-source limits are appropriately handled by independent original-source and primary-quantum verification, not by giving the reader extra premises. The reader is instruction-confined, not technically isolated, and is not evidence of human learning. All original/revised teaching and reports, rejected previews and corrected review concern are preserved. No unresolved material issue remains in the accepted content/evidence scope. Mechanical readiness verifies record presence/freshness only and does not prove semantic quality, human mastery, universal error absence or publication.

Release boundary. Final helper acceptance covers the declared teaching and review evidence only. Root still owns outgoing metadata, actual publication/readback and corpus closure. No new closed-count, completed147/76 corpus claim or successful future publication is made here. The PDF remains internal audit evidence; the learner artifact is the original Markdown/figure bundle.
''')
add_source('final-integration',F/'acceptance-record.md','Complete final scope and evidence integration','Authored and reviewed complete final integration; distinguishes actual acceptance scope from unobserved live behavior and later publication.')
m['project_root']=str(F);m['skill']={'path':str(skill),'sha256':sha(skill)};m['request']={'path':str(F/'request.txt'),'sha256':sha(F/'request.txt')}
m['required_topics'][0]['source_portions']=[{'source_id':src['id'],'portion_id':p['id']} for src in m['sources'] for p in src['portions']]
def ev(path,text):return {'path':path,'sha256':sha(F/path),'locator':{'kind':'text','value':text}}
def acceptance(prefix):return ev('acceptance-record.md',next(l for l in (F/'acceptance-record.md').read_text().splitlines() if l.startswith(prefix)))
def cond(reason,evidence):return {'applicable':True,'status':'pass','reason':reason,'evidence':evidence,'dependencies':[]}
for n in range(1,11):
 req=t['requirements'][f'T{n}'];req['dependencies']=[];req['evidence'].append(acceptance('T1–T10.'));req['reason']+=' Unchanged teaching verified against frozen v2; current complete root teaching review and final integration confirm retained witnesses.'
t['requirements']['T11']=cond('Usable final three-file route, actual whole-destination preservation/source styling/native contract and faithful complete internal preview all accepted within documented observations; unobserved live behavior is not claimed.',[acceptance('T11.')])
t['requirements']['T12']=cond('Complete current route/help, fresh full58-witness SASIS/access admission, issue dispositions and root integrated acceptance; no unresolved material defect within documented scope.',[acceptance('T12.'),ev('evidence/final/final-review.md','No original defect or affected dependency remains unresolved.')])
for g in t['gaps']:g['dependencies']=[]
g=t['gaps'][-1];assert g['id']=='g08';g.update(status='resolved',reason='Full actual destination and final faithful-preview evidence resolves original output-verification gap within the precise accepted scope.',next_action='No content/evidence repair pending. Root owns final publication/readback and corpus closure.',evidence=[acceptance('G08.'),acceptance('T11.')])
# Eight final gates group source structure with destination and independent technical review with execution.
def gate(id,desc,prefix):return {'id':id,'description':desc,**cond(desc,[acceptance(prefix)])}
m['output_checks']=[gate('coverage','Entire assigned source coverage retained and independently reviewed','Coverage.'),gate('author_reconstruction','Complete current author route and help reconstruction','T1–T10.'),gate('technical_execution','Current mathematical/source and independent root technical review','T1–T10.'),gate('destination_math','All398 actual ordered destination payloads/types and all prose preserved','T11.'),gate('destination_visual','Actual source/CSS/figure and complete faithful12-page preview scope; no live-browser claim','T11.'),gate('native_navigation','All21 actual targets/31crossfile references plus24PDFtargets/31logical links verified under respective contracts; no click claim','T11.'),gate('sasis','Fresh full58-witness report/access independently admitted under instruction confinement','T12.'),gate('final_review','Root integrated final semantic acceptance with all issue dispositions and release boundary','T12.')]
S.mkdir(exist_ok=True);(S/'topics').mkdir(exist_ok=True);dump(S/'manifest.json',m);dump(S/'topics/d015.json',t)
def run(*args):
 r=subprocess.run(['python',str(tool),*args],capture_output=True,text=True);assert r.returncode==0,(r.stdout,r.stderr);return r
(S/'RUN.md').write_text('Final helper construction in progress; exact request ../request.txt; acceptance ../acceptance-record.md; root publication/readback remains separate.\n')
run('begin-topic','--state',str(S),'--topic','d015');t=json.loads((S/'topics/d015.json').read_text())
for topic in [True,False]:
 deps=json.loads(run('dependencies','--state',str(S),*(['--topic','d015'] if topic else [])).stdout);dump(F/('topic-dependencies.json' if topic else 'global-dependencies.json'),deps)
 if topic:
  for req in t['requirements'].values():req['dependencies']=deps
  for g in t['gaps']:g['dependencies']=deps
  dump(S/'topics/d015.json',t)
 else:
  for check in m['output_checks']:check['dependencies']=deps
  dump(S/'manifest.json',m)
(S/'RUN.md').write_text('D015 final helper recovery\n\nExact final instruction ../request.txt. Frozen r21 inputs/controls/SKILL.md and copied dependencies are standalone; no mutable root skill dependency. Final teaching artifacts/ copied byte-identically from frozen author/v2. All prior author records remain unchanged. Final substantive integration ../acceptance-record.md and complete root/reviewer reports evidence/final/.\n\nT1–T12 and G01–G08 resolved; eight output gates pass within documented source/CSS/parser/native-contract/full-preview/fresh-reader scope. No live-browser, click, Overleaf or human-learning claim. Topic/full helper checks verify bookkeeping only.\n\nNext action: root independently inspect this packet, publish/read back metadata and evidence, then record corpus closure. Final helper does not assert those future actions.\n')
for topic in [True,False]:
 r=run('check','--state',str(S),*(['--topic','d015'] if topic else []));(F/('topic-check.txt' if topic else 'full-check.txt')).write_text(r.stdout+r.stderr);print(r.stdout)
dump(F/'dependency-copy-map.json',{'original_sources':original_sources,'frozen_skill_sha256':sha(skill),'state_tool_sha256':sha(tool),'final_sources':len(m['sources']),'outputs':9,'output_gates':8})
dump(F/'preservation-verification.json',preserved)
# Recheck all originals after final packet creation.
for manifest in [A/'author-packet-manifest-v1.json',E/'author-packet-manifest-v2.json']:
 for f in json.loads(manifest.read_text())['files']:assert sha(A/f['path'])==f['sha256']
files=[{'path':str(p.relative_to(F)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(F.rglob('*')) if p.is_file() and p.name!='final-packet-manifest.json']
dump(F/'final-packet-manifest.json',{'revision':'D015-r21-v2-final-helper','created_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'files':files,'sources':len(m['sources']),'outputs':9,'output_gates':8,'topic_result':'MECHANICALLY_READY','full_result':'MECHANICALLY_READY','scope':'Declared final teaching/evidence packet only; root publication/readback/corpus closure remain separate actions; mechanical results are not semantic proof.'})
print('FINAL',len(files),'files',len(m['sources']),'sources',sha(F/'final-packet-manifest.json'))
