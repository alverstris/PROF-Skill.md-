from pathlib import Path
import json,hashlib,re,subprocess,copy
E=Path(__file__).resolve().parent; A=E.parent; B=A/'v2'; R=A.parents[5]; S=E/'.prof-state'; TOOL=R/'scripts/prof_state.py'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,d):p.write_text(json.dumps(d,indent=2)+'\n')
def run(*args):
 r=subprocess.run(['python',str(TOOL),*args],text=True,capture_output=True);assert r.returncode in [0,1],r.stderr;return r
# Source-level full inventory of the actual revised files.
links=[];issues=[];counts={};anchors={}
for name in ['teaching.md','hints.md','solutions.md']:
 text=(B/name).read_text();anchors[name]=re.findall(r'<a name="([^"]+)"></a>',text)
 assert len(anchors[name])==len(set(anchors[name]))
 counts[name]={'inline':len(re.findall(r'\$`(.*?)`\$',text,re.S)),'display':len(re.findall(r'```math\n(.*?)\n```',text,re.S))}
 outside=re.sub(r'```.*?```|\$`.*?`\$','',text,flags=re.S)
 assert not re.search(r'^\s{0,3}#{1,6}\s|^\s*(?:={3,}|-{3,})\s*$|\*\*|__',outside,re.M)
 for payload in re.findall(r'\$`(.*?)`\$',text,re.S):assert '<' not in payload and '>' not in payload
for name in anchors:
 for target in re.findall(r'\]\(([^)]+)\)',(B/name).read_text()):
  if target.startswith(('http:','https:')):continue
  path,_,anchor=target.partition('#');p=B/(path or name);ok=p.is_file() and (not anchor or anchor in anchors.get(path or name,[]))
  links.append({'from':name,'target':target,'resolved':ok});assert ok,(name,target)
for n in range(1,6):assert f'q{n}' in anchors['teaching.md'] and f'h{n}' in anchors['hints.md'] and f'a{n}' in anchors['solutions.md']
dump(E/'structural-checks-v2.json',{'issues':issues,'links':links,'anchors':anchors,'math_counts':counts,'limit':'Source-level links/typography/counts only; actual v2 GitHub parsing, styling and clicked navigation remain pending.'})
# Original preservation and frozen-current integrity.
old=json.loads((A/'author-packet-manifest-v1.json').read_text());checked=[]
for f in old['files']:
 p=A/f['path'];q=A/'v1-original'/f['path'];assert sha(p)==f['sha256'] and p.read_bytes()==q.read_bytes(),f['path'];checked.append(f['path'])
assert (A/'author-packet-manifest-v1.json').read_bytes()==(A/'v1-original/author-packet-manifest-v1.json').read_bytes()
frozen=json.loads((E/'freeze-manifest-v2.json').read_text())
for f in frozen['constituents']:assert sha(B/f['path'])==f['sha256']
dump(E/'preservation-check-v2.json',{'original_files_unchanged':checked,'original_manifest_copy_identical':True,'frozen_v2_constituents_unchanged':9})
# Retain original prerequisite and source-read evidence; new topic note explicitly scopes reuse.
(E/'topic-record-v2.md').write_text('''D015 v2 dependency and source map addendum

The complete original coverage C01–C10, prerequisite and course-convention record is ../topic-record.md; its original bytes are retained and reloaded. Entire baseline/source text and image access remains evidenced by ../input-access.json. The frozen sources are unchanged, so those actual author readings remain applicable; this does not assert a second reading. All C01–C10 locations are unchanged in v2/teaching.md. Full current-route reconstruction is author-audit-v2.md A01–A20.

Only the specified 21 inline comparison characters and three Q5 prose strings changed. The full inverse ledger proves scope across all three text files; the six figure hashes remain identical. All comparison semantics, domains, branches and captions are rechecked in A04–A18. Q5 now asks which conditions fail and explicitly tests both; its hint already supports both and solution gives both failures. The original prompt-first independent calculation remains mathematically applicable because no problem data or requested mathematics changed; no new blind-answer independence is claimed for this revision.

Original G01–G07 deductions/primary evidence remain applicable and were retraced through current teaching in A03–A16. Original G08 remains open for the actual v2 destination. Known v1 parser failures motivate the safe-command replacement, but only current destination inspection can establish their resolution. New issue Q5 is author-resolved by R02 and original issue MATH-1 is source-repaired with actual destination verification pending. No course convention, source scope, prerequisite assumption or skill instruction changed. There is no unobserved student attempt or mastery claim.
''')
if not S.exists():
 r=run('init','--state',str(S),'--skill',str(A/'controls/SKILL.md'),'--request',str(E/'assignment-v2.txt'),'--project-root',str(A),'--topic','d015');assert r.returncode==0
m=json.loads((A/'.prof-state/manifest.json').read_text()); t=json.loads((A/'.prof-state/topics/d015.json').read_text())
m['request']={'path':str(E/'assignment-v2.txt'),'sha256':sha(E/'assignment-v2.txt')};m['project_root']=str(A)
new_sources=[('v2-topic',E/'topic-record-v2.md','Full current coverage/prerequisite/convention addendum'),('v2-issues',A.parent/'issue-register-v1.md','Complete original consolidated issue register'),('v1-reader',A.parent/'sasis-v1/report.md','Complete original SASIS report'),('v1-reader-access',A.parent/'sasis-v1/access-log.md','Complete original SASIS access log'),('v1-reader-disposition',A.parent/'root-sasis-v1-disposition.md','Complete root original SASIS disposition'),('v1-destination',A.parent/'destination-v1/review.md','Complete original actual destination report'),('v1-destination-audit',A.parent/'destination-v1/final-audit.json','Complete original actual destination audit'),('v1-destination-disposition',A.parent/'root-destination-v1-disposition.md','Complete root original destination disposition'),('v1-comparison-map',A.parent/'destination-v1/all21-comparison-character-positions.json','All21 exact mapped original comparison characters'),('v1-author-disposition',A.parent/'root-author-v1-disposition.md','Complete root original author disposition'),('v1-teaching-review',A.parent/'root-teaching-v1-review.md','Complete root original teaching review'),('v2-inverse',E/'edit-inverse-ledger-v2.json','Complete exact24 edit and inverse proof across all3 texts and6 figures')]
for id,p,loc in new_sources:
 src={'id':id,'path':str(p),'sha256':sha(p),'portions':[{'id':'whole','locator':loc,'disposition':'required','reason':'Original full audit evidence and exact authorized repair boundary; no prior verdict replaces current author reconstruction.','evidence':[]}]};m['sources'].append(src)
 t['source_reads'].append({'source_id':id,'portion_id':'whole','status':'read','reviewed_sha256':sha(p),'note':loc+' read; repair limited to supported comparison-token and Q5 prompt ambiguity findings.'})
m['outputs']=[{'id':'file'+str(i+1),'path':'v2/'+f['path'],'sha256':f['sha256']} for i,f in enumerate(frozen['constituents'])]
m['required_topics'][0]['source_portions']=[{'source_id':s['id'],'portion_id':p['id']} for s in m['sources'] for p in s['portions']]
def ev(file,line):return {'path':'v2-evidence/'+file,'sha256':sha(E/file),'locator':{'kind':'text','value':line}}
def cond(status,reason,evidence=[]):return {'applicable':True,'status':status,'reason':reason,'evidence':evidence,'dependencies':[]}
audit=(E/'author-audit-v2.md').read_text()
for n in range(1,13):
 line=next(x for x in audit.splitlines() if x.startswith(f'T{n} '));t['requirements'][f'T{n}']=cond('pass' if n<=10 else 'pending',line,[ev('author-audit-v2.md',line)])
# Original resolved deductions retained with their original precise witnesses; current audit retraces them.
for g in t['gaps']:g['dependencies']=[]
t['gaps'][-1]['reason']='Actual v2 destination parsing, styling, live appearance and navigation remain root-owned pending checks; source repair is exact but not live evidence.'
t['gaps'][-1]['next_action']='Root inspect the frozen v2 at the actual destination, preserve complete results and assess fresh v2 SASIS before final acceptance.'
checks=[]
for id,desc,line in [('coverage','Full assigned source coverage at revised artifact','A17. Teaching 228–237 retains all six original closing topics, including MVT, separate review-sheet pointer and historical harder-exam warning.'),('author_reconstruction','Complete revised content and help reconstruction','A19. All five tasks have explicit response criteria in teaching, one distinct targeted hint in hints.md and a complete reasoned solution in solutions.md.'),('technical_execution','Current symbolic/manual checks and repair proof','Current mathematical expressions were checked against the unchanged explicit symbolic script, rerun as verify_math_v2.py in this evidence directory.')]:
 checks.append({'id':id,'description':desc,**cond('pass',desc+'; see complete A01–A20 and original coverage C01–C10.',[ev('author-audit-v2.md',line)])})
checks.append({'id':'source_structure','description':'Current local source structure',**cond('pass','Every local reference resolves, task/hint/answer IDs match, all inline math has safe comparison commands; no actual-destination success inferred.',[ev('structural-checks-v2.json','Source-level links/typography/counts only; actual v2 GitHub parsing, styling and clicked navigation remain pending.')])})
for check in m['output_checks']:
 if check['id'] not in [c['id'] for c in checks]:checks.append({'id':check['id'],'description':check['description'],**cond('pending','Root-owned v2 result remains pending in this author packet; original v1 result is not a current pass.')})
m['output_checks']=checks;dump(S/'manifest.json',m);dump(S/'topics/d015.json',t)
assert run('begin-topic','--state',str(S),'--topic','d015').returncode==0
t=json.loads((S/'topics/d015.json').read_text())
for topic in [True,False]:
 args=['dependencies','--state',str(S)]+(['--topic','d015'] if topic else []);r=run(*args);assert r.returncode==0;deps=json.loads(r.stdout);dump(E/('topic-dependencies-v2.json' if topic else 'global-dependencies-v2.json'),deps)
 if topic:
  for c in t['requirements'].values():
   if c['status']=='pass':c['dependencies']=deps
  for g in t['gaps']:
   if g['status']=='resolved':g['dependencies']=deps
  dump(S/'topics/d015.json',t)
 else:
  for c in m['output_checks']:
   if c['status']=='pass':c['dependencies']=deps
  dump(S/'manifest.json',m)
(S/'RUN.md').write_text('D015 r21 v2 author recovery\n\nExact instruction ../assignment-v2.txt; frozen nine-file teaching ../freeze-manifest-v2.json. Original controls and complete baseline/source reads remain under author/controls and author/input-access.json. Current source/prerequisite/convention addendum ../topic-record-v2.md; exact inverse proof ../edit-inverse-ledger-v2.json; complete current author route ../author-audit-v2.md. Read actual SKILL/protocol on recovery.\n\nT1–T10 current author pass; T11/T12, G08 and root-owned destination, native navigation, external review, fresh SASIS and final gates remain pending. All original42 packet files and copied manifest verified unchanged; nine v2 constituents still frozen. No further teaching mutations authorized.\n\nNext action: hand root the v2-evidence packet; root publishes and assesses current external gates.\n')
for topic in [True,False]:
 r=run('check','--state',str(S),*(['--topic','d015'] if topic else []));(E/('topic-check-v2.txt' if topic else 'full-check-v2.txt')).write_text(r.stdout+r.stderr);print(r.stdout)
print('SOURCES',len(m['sources']),'OUTPUTS',len(m['outputs']))
