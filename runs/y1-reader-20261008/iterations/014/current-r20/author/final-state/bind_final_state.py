from pathlib import Path
import json,hashlib,subprocess,zipfile,datetime
root=Path.cwd();a=root/'runs/y1-reader-20261008/iterations/014/current-r20/author';p=a.parent;e=a/'final-state';st=e/'.prof-state';old=a/'v2-evidence/.prof-state'
def sha(f):return hashlib.sha256(f.read_bytes()).hexdigest()
def load(f):return json.loads(f.read_text())
def save(f,d):f.write_text(json.dumps(d,indent=2)+'\n')
def ev(f,start=1,end=None):return {'path':str(f.relative_to(a)),'sha256':sha(f),'locator':{'kind':'lines','start':start,'end':end or len(f.read_text().splitlines())}}
# Preserve both complete author evidence checkpoints.
preserved=[]
for mf in [a/'author-packet-manifest.json',a/'v2-evidence/author-packet-manifest-v2.json']:
 for r in load(mf)['files']:
  f=Path(r['path']);assert sha(f)==r['sha256'] and f.stat().st_size==r['bytes'];preserved.append(r)
# Independently compare all 125 archive members, local files and archive identity.
ar=load(p/'destination-v2-archive.json');az=p/ar['archive'];assert sha(az)==ar['sha256'] and az.stat().st_size==ar['bytes']
with zipfile.ZipFile(az) as z:
 assert len(z.namelist())==len(ar['files'])==125
 for r in ar['files']:
  b=z.read(r['path']);assert len(b)==r['bytes'] and hashlib.sha256(b).hexdigest()==r['sha256'];assert b==(p/r['path']).read_bytes()
save(e/'preservation-and-archive-check.json',{'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'both_author_checkpoints_unchanged':True,'compared_checkpoint_rows':len(preserved),'destination_archive_members':125,'all_archive_local_record_bytes_equal':True,'archive_sha256':sha(az),'teaching_sha256':sha(a/'teaching-v2.md')})
subprocess.run(['python','scripts/prof_state.py','init','--state',str(st),'--project-root',str(a),'--skill',str(a/'v2-evidence/frozen-inputs/SKILL-r20.md'),'--request',str(e/'request.txt'),'--topic','d014'],check=True,capture_output=True)
subprocess.run(['python','scripts/prof_state.py','begin-topic','--state',str(st),'--topic','d014'],check=True,capture_output=True)
m=load(st/'manifest.json');t=load(st/'topics/d014.json');om=load(old/'manifest.json');ot=load(old/'topics/d014.json')
for key in ['required_topics','sources','outputs']:m[key]=om[key]
t['source_reads']=ot['source_reads']
extras=[('reader-v2','sasis-v2/reader-original.md','Complete fresh original reader report actually read; all chronological reconstruction, help, precision consideration and limitations.'),('reader-access-v2','sasis-v2/access-log.md','Complete access log read; initial truncated packet fully reread and complete baseline before teaching.'),('reader-admission-v2','sasis-admission-v2-result.json','Complete admission result read; exact two input hashes/ranges, instruction-only boundary.'),('reader-disposition-v2','root-sasis-v2-disposition.md','Complete root disposition read; bounded precision consideration does not establish a defect.'),('destination-final-v2','destination-v2/final-audit.json','All 1887 lines read in three bounded packets; complete actual source/parser/CSS/navigation and internal preview limits.'),('destination-review-v2','destination-v2/review.md','Entire final review read, including identity, navigation contract, all-page preview and limits.'),('destination-navigation-v2','destination-v2/positive-navigation-audit.json','Complete JSON read; all seven positive P/H/S relationships and prefix correspondence.'),('navigation-contract','root-navigation-contract.md','Complete attributed root official documentation review read; no author fresh web fetch claimed.'),('navigation-scope','destination-v2/navigation-scope-supplement.json','Complete target-prefix and unobserved client boundary read.'),('visual-v2','destination-v2/visual-inspection.json','Entire eleven-page inspection report read; reviewer actual image observation, not author new image observation.'),('ast-v2','destination-v2/preview-final2/AST-content-check.json','Complete exact AST comparison and preview adaptation record read.'),('compile-v2','destination-v2/preview-final2/preview-check.json','Complete final PDF identity/count/diagnostic record read.'),('native-pdf-v2','destination-v2/preview-final2/navigation-fonts.json','Every native target/link/font entry read in lossless compact JSON; distinct hint/solution pages and no viewer click claim.'),('rasters-v2','destination-v2/preview-final2/exact-PDF-raster-correspondence.json','All eleven exact raster correspondence rows read.'),('root-read-v2','root-v2-full-readback.md','Complete root current full-read and inverse exact-change record read; historical pending conclusions superseded by final acceptance.'),('root-parser-v2','root-v2-parser-verification.json','Complete independent actual GitHub bytes/all346payload check read.'),('root-preview-v2','root-preview-v2-inspection.json','Complete additional root pages8–11 observation read.'),('root-acceptance','final-acceptance.md','Complete final content acceptance and remaining publication boundary read.'),('root-issues','issue-register.md','Entire supported issue disposition read; no unresolved material issue, all failures preserved.'),('archive-v2','destination-v2-archive.json','Archive metadata read and every125 member identity compared against both exact archive bytes and local file bytes; no binary visual claim.')]
for ident,n,note in extras:
 f=p/n;m['sources'].append({'id':ident,'path':str(f),'sha256':sha(f),'portions':[{'id':'whole','locator':'entire report; binary identities as explicitly described','disposition':'required','reason':note,'evidence':[]}]});m['required_topics'][0]['source_portions'].append({'source_id':ident,'portion_id':'whole'});t['source_reads'].append({'source_id':ident,'portion_id':'whole','status':'read','reviewed_sha256':sha(f),'note':note})
# Bind binary evidence bytes without claiming new visual/source-content reading.
for ident,f,note in [('canonical-preview',p/'destination-v2/preview-final2/verified-build.pdf','Entire file identity verified via archive comparison; actual all-page visual scope is the bound reviewer report.'),('complete-destination-archive',az,'Every member fully extracted in memory and compared byte-for-byte to recorded/local identities; visual and semantic scope is in bound reports.'),('final-reconciliation',e/'final-review.md','Complete current author reconciliation of actual external reports, preserved reconstruction and exact limits.')]:
 m['sources'].append({'id':ident,'path':str(f),'sha256':sha(f),'portions':[{'id':'whole','locator':'whole bytes with inspection scope stated','disposition':'required','reason':note,'evidence':[]}]});m['required_topics'][0]['source_portions'].append({'source_id':ident,'portion_id':'whole'});t['source_reads'].append({'source_id':ident,'portion_id':'whole','status':'read','reviewed_sha256':sha(f),'note':note})
t['requirements']=ot['requirements']
for k,v in t['requirements'].items():
 v['status']='pass';v['dependencies']=[];v['evidence']=[ev(e/'final-review.md')]+(v['evidence'] if int(k[1:])<=10 else [])
 if k=='T11':v['reason']='Current actual GitHub preservation, documented native-anchor syntax and positive all-seven relationships, markup/CSS style review and separate full internal preview accepted within disclosed non-live scope.'
 elif k=='T12':v['reason']='Actual complete fresh reader, root original source/presolution/current route, complete final destination and issue disposition read and reconciled. No unresolved material issue within scoped content acceptance; publication remains root-owned.'
 else:v['reason']+=' Final fresh reader and full external evidence now admitted; exact source and output remain unchanged.'
t['gaps']=ot['gaps']
for g in t['gaps']:
 g.update(status='resolved',reason='Actual final destination report and root acceptance now verify this exact repaired output; see full final author reconciliation and scoped limits.',next_action='No further teaching repair required by current evidence.',evidence=[ev(e/'final-review.md')],dependencies=[])
m['output_checks']=om['output_checks']
for c in m['output_checks']:
 c.update(status='pass',evidence=[ev(e/'final-review.md')],dependencies=[])
 if c['id']=='final_review':c['reason']='Complete author/root/reader/destination route reconciled at final exact bytes; no unresolved material issue within recorded scope.'
 elif c['id']=='sasis':c['reason']='Full fresh v2 original and access log read; root admission verifies entire baseline and teaching, repaired initial truncation, instruction-only isolation.'
 elif c['id']=='destination':c['reason']='Actual immutable GitHub raw/parser/CSS and documented native navigation checked; full source-faithful internal preview separately inspected by reviewer. No live-pixel/client-click claim.'
for ident,reason in [('internal_preview','Exact AST, all eleven reviewer-inspected pages, stable canonical PDF/raster identity and all native links verified; internal derivative only.'),('evidence_preservation','Both prior author checkpoints and all 125 destination archive members match exact recorded bytes.')]:m['output_checks'].append({'id':ident,'description':reason,'applicable':True,'status':'pass','reason':reason,'evidence':[ev(e/'final-review.md'),ev(e/'preservation-and-archive-check.json')],'dependencies':[]})
save(st/'manifest.json',m);save(st/'topics/d014.json',t)
for name,args in [('topic',['--topic','d014']),('global',[])]:
 r=subprocess.run(['python','scripts/prof_state.py','dependencies','--state',str(st),*args],capture_output=True,text=True,check=True);(e/f'{name}-dependencies.json').write_text(r.stdout);deps=json.loads(r.stdout)
 if name=='topic':
  for v in list(t['requirements'].values())+t['gaps']:v['dependencies']=deps
 else:
  for v in m['output_checks']:v['dependencies']=deps
save(st/'manifest.json',m);save(st/'topics/d014.json',t)
(st/'RUN.md').write_text('''D014 final content acceptance recovery

Exact latest request: ../request.txt. Incoming actual frozen r20 skill is author/v2-evidence/frozen-inputs/SKILL-r20.md; future outgoing r21 metadata does not rebind this record. Output teaching-v2.md remains SHA256 caf74a9a150f61d2531e8b2768abb1448fb7d5304818a9e1fcc73d02bead826b. Single file, no companions/figures.

Full current reconciliation: ../final-review.md. Manifest binds original source/baseline/control records, exact new reader/admission, complete actual destination reports, root full acceptance/issues and archived binary proof. Earlier v1 and v2 pending states remain untouched and historically pending.

All T1–T12 and applicable content output checks now have current supporting evidence within explicit server/documented-navigation/internal-preview scope. Live browser pixels/client clicks are unobserved; no learner mastery or historical-write completeness claim. No new teaching or substantive skill edit.

Next action: root independently inspect final helper/evidence and perform authorized publication/readback/closure; the author does not publish or change queue counts. Full helper freshness is not publication or semantic proof.
''')
for name,args in [('topic',['--topic','d014']),('full',[])]:
 r=subprocess.run(['python','scripts/prof_state.py','check','--state',str(st),*args],capture_output=True,text=True);(e/f'helper-{name}-check.txt').write_text(r.stdout+r.stderr+f'\nexit_code={r.returncode}\n');print(name,r.returncode,r.stdout);assert r.returncode==0
