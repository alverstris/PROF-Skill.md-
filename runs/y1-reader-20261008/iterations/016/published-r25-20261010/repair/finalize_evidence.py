from pathlib import Path
import json, hashlib, subprocess, re, shutil, datetime

p=Path('/workspace/scratch/f9c0b7fc7e76/d016-published-r25')
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def save(path,obj): path.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n')
root_evidence=Path('/workspace/scratch/f9c0b7fc7e76/root-review-d016-r25')
shutil.copytree(root_evidence,p/'reviews/root-independent',dirs_exist_ok=True)
audit=p/'reviews/coordinator-disposition.md'
text=audit.read_text()
old='The narrowly affected earlier units check and candidate review are recorded in the accompanying root evidence before publication.'
new='Root also inspected every matching units/dimension/average/integral passage in the 17 immutable accepted constituents and found no matching unconditional integral/average units contrast. The coordinator read all supplied unique hit contexts in two bounded returns after an initially truncated JSON view; no additional reopening is justified. Root\'s post-reader disposition accepts the focused r26 diff for publication validation while requiring fresh generation. These checks and their limits are preserved in root-independent/.'
assert old in text
audit.write_text(text.replace(old,new))

# Basic candidate checks plus exact preservation of the unmodified package.
old_manifest=json.loads((p/'package-sha-manifest.json').read_text())
candidate=p/'repair/candidate/prof'
changed=[]
for item in old_manifest['files']:
    a=p/'inputs/prof'/item['path']; b=candidate/item['path']
    assert sha(a)==item['sha256']
    if a.read_bytes()!=b.read_bytes(): changed.append(item['path'])
assert changed==['SKILL.md','references/execution-protocol.md']
links=[]
for rel in changed:
    source=candidate/rel
    for target in re.findall(r'\]\(([^)]+)\)',source.read_text()):
        if '://' in target or target.startswith('#'):continue
        dest=(source.parent/target.split('#')[0]).resolve()
        links.append({'source':rel,'target':target,'exists':dest.exists()})
assert all(x['exists'] for x in links)
result=subprocess.run(['python',str(p/'repair/quick_validate.py'),str(candidate)],text=True,capture_output=True)
assert result.returncode==0
freeze=json.loads((p/'freeze.json').read_text())
for f in freeze['files']:assert sha(p/'output'/f['path'])==f['sha256']
for f in json.loads((p/'repair/probe-input-identities.json').read_text()):assert sha(p/'repair/probe-input'/f['path'])==f['sha256']
save(p/'repair/validation.json',{
 'candidate_version':'2026-10-10-r26','checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'quick_validate':{'exit':result.returncode,'stdout':result.stdout.strip(),'scope':'basic frontmatter/name/description validation only'},
 'all_36_package_files_accounted':True,'changed_files':changed,'other_34_files_byte_identical':True,
 'unchanged_baseline_and_reader_role':True,'metadata_review':'Existing openai.yaml display name, description, invocation text and icons remain aligned; no regeneration needed.',
 'changed_file_relative_links':links,'all_frozen_teaching_hashes_unchanged':True,
 'probe_inputs_unchanged':True,'probe_report_sha256':sha(p/'repair/probe-original.md'),
 'forward_probe':'Fresh no-history ordinary reference audit detected both failure types and retained the valid comparison/figure. It imposed no practice or SASIS trial on reference-only audit.',
 'limits':'No r26 D016 teaching has been generated or accepted. Publication/readback and a fresh-context whole generation remain required.'})

# Declare the already performed r25 author/audit work without manufacturing readiness.
state=p/'.prof-state'
manifest=json.loads((state/'manifest.json').read_text())
topic=json.loads((state/'topics/definite-integrals.json').read_text())
sources=[]; reads=[]; assignments=[]
def source(id,rel,portions,note):
    file=p/rel; digest=sha(file)
    src={'id':id,'path':str(file),'sha256':digest,'portions':[]}
    for pid,locator in portions:
        src['portions'].append({'id':pid,'locator':locator,'disposition':'required','reason':'Required assigned source, operational baseline, or actually used skill support.','evidence':[]})
        assignments.append({'source_id':id,'portion_id':pid})
        reads.append({'source_id':id,'portion_id':pid,'status':'read','reviewed_sha256':digest,'note':note+' See author/admission.md and reviews/coordinator-disposition.md for actual scope and semantic witnesses.'})
    sources.append(src)

source('baseline','inputs/prof/references/sasis/ocr-baseline-20261007/student-baseline.txt',[('full','Complete 247840-byte four-subject baseline; all 1377 LF physical lines, actual nontruncated ranges in admission.md.')],'Complete operational starting knowledge read before drafting; signed integration, FTC, sums and average are present, while pyramid law and condition meanings need supplied teaching.')
for i,file in enumerate(sorted((p/'inputs/source').glob('*'))):
    if not file.is_file():continue
    rel=str(file.relative_to(p)); ident='original-'+str(i+1)
    if file.suffix=='.pdf':
        portions=[('page-'+str(j),'Physical PDF page '+str(j)+(' (cover)' if j==1 else ', printed page '+str(j-1))) for j in range(1,7)]
        note='All six original PDF pages inspected through supplied exact text and full page PNGs; all five source figures accounted for.'
    else:
        portions=[('whole','Whole original source-packet constituent '+file.name)]
        note='Original source identity, literal extraction or full page visual inspected; mathematical details checked against the original page images.'
    source(ident,rel,portions,note)
refs=['references/execution-protocol.md','references/domain-patterns.md','references/state-tool.md','references/sasis.md','references/sasis/profile-manifest.json','references/sasis/student-role.txt','references/sasis/student-testing-contract.txt','references/sasis/rewrite-guide.md','references/findings-and-rationale.md','references/execution-research.md']
for i,ref in enumerate(refs):
    timing='Read completely before drafting' if i<8 else 'Read completely after freeze for method repair, not used as a pre-freeze historical diagnosis'
    source('prof-ref-'+str(i+1),'inputs/prof/'+ref,[('whole','Whole required reference '+ref)],timing+'; governs the actual source/reconstruction/reader/repair/evidence workflow.')
source('author-admission','author/admission.md',[('whole','Complete admission, capability and convention record')],'Records original actual input ranges and conventions used for this generation.')
manifest['sources']=sources
outputs=[]
for i,f in enumerate(freeze['files']):outputs.append({'id':'output-'+str(i+1),'path':'output/'+f['path'],'sha256':f['sha256']})
manifest['outputs']=outputs
manifest['required_topics'][0].update({'title':'D016: definite integrals, geometric construction, accumulation and simple-interest totals','source_portions':assignments,'outputs':[o['id'] for o in outputs]})
topic['source_reads']=reads
lines=audit.read_text().splitlines()
def evidence(fragment):
    n=next(i+1 for i,line in enumerate(lines) if fragment in line)
    return [{'path':'reviews/coordinator-disposition.md','sha256':sha(audit),'locator':{'kind':'lines','start':n,'end':n}}]
requirements={
 'T1':('fail','F1: the categorical units statement lacks the dimensional condition; other new concepts/hypotheses have usable meanings.','F1, teaching 154'),
 'T2':('pass','The exact unfamiliar sum, solid, endpoint and weighted-contribution forms were reconstructed; destination preservation is a separate unverified output check.','The main reconstruction is complete'),
 'T3':('fail','F1: the categorical units statement exceeds the admitted formula scope; other substantive warrants remain sound.','F1, teaching 154'),
 'T4':('pass','Every new capability has connected worked reasoning and interpreted results.','The main reconstruction is complete'),
 'T5':('pass','Study scope triggers practice; early P1 and changed/integrated P2–P6 cover the declared capabilities.','All practice was checked'),
 'T6':('pass','P1–P6 each require discriminating operations/justifications and have supported prerequisites at their positions.','All practice was checked'),
 'T7':('pass','Six matched grouped hints advance decisions; all full solutions were reconstructed and independently checked.','All practice was checked'),
 'T8':('pass','P6 provides a later retrieval and changed-application opportunity, without claiming human retention.','All practice was checked'),
 'T9':('pass','Actual baseline knowledge supports compression and the new geometry/conditions are bridged; minor label collision remains recorded.','The main reconstruction is complete'),
 'T10':('fail','F1: independent dimensional reconstruction disproves the units contrast, despite correct source comparisons and all exercise answers.','F1, teaching 154'),
 'T11':('fail','F2: exported explanatory glyphs are clipped; full live destination evidence is separately unverified.','F2, teaching Figure 2'),
 'T12':('pass','The full final route/help/source and all supported issues were audited, with explicit refusal of acceptance.','T1 fails only')}
for key,(status,reason,fragment) in requirements.items():topic['requirements'][key]={'applicable':True,'status':status,'reason':reason,'evidence':evidence(fragment),'dependencies':[]}
topic['gaps']=[]
for id,question,fragment in [('units-scope','False unconditional units distinction','F1, teaching 154'),('export-clipping','Saved figure title and tick clipping','F2, teaching Figure 2')]:
    topic['gaps'].append({'id':id,'question':question,'consequential':True,'status':'open','reason':'Verified failure remains in the unchanged frozen lesson.','next_action':'Publish verified PROF repair; fresh-context whole generation and new independent reviews. Never patch frozen teaching.','evidence':evidence(fragment),'dependencies':[]})
checks=[
 ('coverage','Complete assigned original source and declared capabilities located','pass','All six original PDF pages'),
 ('final_review','Whole final route, help and all acceptance conditions','fail','D016 is not accepted.'),
 ('figure_export','Actual complete exported figures and glyphs','fail','F2, teaching Figure 2'),
 ('local_navigation','Task, hint, solution matching and local file destinations','pass','The local lexical/navigation record'),
 ('destination','Actual GitHub mathematical preservation, prose typography, image display and navigation','unverified','The actual immutable teaching')]
manifest['output_checks']=[{'id':id,'description':description,'applicable':True,'status':status,'reason':description+'; see actual bounded evidence and limits.','evidence':evidence(fragment),'dependencies':[]} for id,description,status,fragment in checks]
save(state/'manifest.json',manifest);save(state/'topics/definite-integrals.json',topic)
script=p/'inputs/prof/scripts/prof_state.py'
def deps(extra):
    r=subprocess.run(['python',str(script),'dependencies','--state',str(state)]+extra,capture_output=True,text=True)
    assert r.returncode==0,r.stdout+r.stderr
    return json.loads(r.stdout)
td=deps(['--topic','definite-integrals']); gd=deps([])
save(p/'reviews/topic-dependencies.json',td);save(p/'reviews/global-dependencies.json',gd)
print(json.dumps({'topic_dependency_keys':list(td) if isinstance(td,dict) else type(td).__name__,'global_dependency_keys':list(gd) if isinstance(gd,dict) else type(gd).__name__,'source_count':len(sources),'output_count':len(outputs)}))
