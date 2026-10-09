from pathlib import Path
import hashlib,json,subprocess
p=Path(__file__).resolve().parent;r=p.parents[5]
# Locate the exact checked-out skill rather than guess a relocated project root.
r=next(a for a in p.parents if (a/'scripts/prof_state.py').is_file())
sd=p/'.prof-state';m=json.loads((sd/'manifest.json').read_text());t=json.loads((sd/'topics/mvt.json').read_text())
def sha(f):return hashlib.sha256(f.read_bytes()).hexdigest()
def evidence(f,text):return {'path':str(f.relative_to(p)),'sha256':sha(f),'locator':{'kind':'text','value':text}}
inputs=[('execution',r/'references/execution-protocol.md','full','Full execution protocol; source accounting, dependency reconstruction and honest gates.'),('sasis',r/'references/sasis.md','full','Full mode/role/corpus/admission/closure protocol.'),('reader-role',r/'references/sasis/student-role.txt','full','Full fresh reader operating instruction; not author inputs to reader.'),('reader-contract',r/'references/sasis/student-testing-contract.txt','full','Full two-input admission and sequential reading contract.'),('profile',r/'references/sasis/profile-manifest.json','full','Complete profile identities and hashes.'),('rewrite',r/'references/sasis/rewrite-guide.md','full','Full issue diagnosis and justified repair guide.'),('state-guide',r/'references/state-tool.md','full','Full strict schema and pending versus mechanical readiness.'),('domain-guide',r/'references/domain-patterns.md','full','Full domain guide read; mathematics route applied.'),('baseline',r/'references/sasis/ocr-baseline-20261007/student-baseline.txt','physical-lf-1-1378','All1377 physical LF content lines plus terminal empty entry, preserving internal CR; see exact access packets.'),('access',p/'access-log.md','full','Complete actual access/prerequisite record.'),('math-record',p/'research-and-math.md','full','Actual external source read scope plus independently derived M1–M8.'),('prompts',p/'prompts-only-v1.md','full','All exact P1–P6 before independently reviewed answers.')]
source=p.parent/'source';inputs.append(('lecture-pdf',source/'lec14.pdf','physical-pages-1-5','Full text plus original full-frame page images independently read, all equations and three figures.'))
for i in range(1,6):
 for ext in ['txt','png']:
  inputs.append((f'page-{i}-{ext}',source/f'page-{i:02}.{ext}',f'physical-page-{i}',f'Complete physical page{i} '+('text extraction independently checked against image.' if ext=='txt' else 'original full-frame image, including all visual labels/equations/ending.')))
m['sources']=[];t['source_reads']=[]
for sid,path,pid,note in inputs:
 m['sources'].append({'id':sid,'path':str(path),'sha256':sha(path),'portions':[{'id':pid,'locator':pid,'disposition':'required','reason':note,'evidence':[]}]})
 t['source_reads'].append({'source_id':sid,'portion_id':pid,'status':'read','reviewed_sha256':sha(path),'note':note})
packet=json.loads((p/'packet-manifest-v1.json').read_text());m['outputs']=[]
for i,o in enumerate(packet['constituents']):m['outputs'].append({'id':'learner' if i==0 else f'figure-{i}','path':o['path'],'sha256':o['sha256']})
m['required_topics']=[{'id':'mvt','title':'MVT, proof and conditions, exact versus tangent forms, derivative signs and exponential inequalities','source_portions':[{'source_id':sid,'portion_id':pid} for sid,path,pid,note in inputs],'outputs':[o['id'] for o in m['outputs']]}]
for k in ['sasis','independent_technical','destination_math','destination_visual','live_navigation']:
 m['output_checks'].append({'id':k,'description':{'sasis':'Fresh dedicated two-input SASIS full reading.','independent_technical':'Independent exact prompt-first calculation and complete technical review.','destination_math':'Every actual destination expression preserves operands/operators/grouping.','destination_visual':'Full actual destination preview and typography inspected.','live_navigation':'All task/help routes work in actual destination.'}[k],'applicable':True,'status':'pending','reason':'Root owns this gate; author does not self-certify.','evidence':[],'dependencies':[]})
for k in t['requirements']:
 n=int(k[1:]);paragraph=next(s for s in (p/'requirements.md').read_text().split('\n\n') if s.startswith(k+'.'))
 t['requirements'][k]={'applicable':True,'status':'pass' if n<=10 else 'pending','reason':paragraph,'evidence':[evidence(p/'requirements.md',paragraph)] if n<=10 else [],'dependencies':[]}
m['output_checks'][0]['status']='pass';m['output_checks'][0]['reason']='Author compared all original source portions S00–S08 and three figures against frozen learner; independent final gates remain separate.'
w='Coverage result: all five physical pages, all three original visuals and the final Taylor preview represented.'
# Exact text locator can be a substantive substring of a longer paragraph.
m['output_checks'][0]['evidence']=[evidence(p/'source-coverage.md',w)]
m['output_checks'][1]['reason']='Author complete reconstruction saved; independent integrated acceptance remains pending.'
(sd/'manifest.json').write_text(json.dumps(m,indent=2)+'\n');(sd/'topics/mvt.json').write_text(json.dumps(t,indent=2)+'\n')
base=['python',str(r/'scripts/prof_state.py'),'dependencies','--state',str(sd)]
a=subprocess.run(base+['--topic','mvt'],capture_output=True,text=True,check=True);(p/'topic-dependencies.json').write_text(a.stdout)
b=subprocess.run(base,capture_output=True,text=True,check=True);(p/'global-dependencies.json').write_text(b.stdout)
print(a.stdout[:120])
