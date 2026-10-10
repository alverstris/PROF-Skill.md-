"""Declare actual already-read inputs and frozen outputs, without promoting checks."""
import hashlib
import json
from pathlib import Path

root=Path(__file__).resolve().parents[1]
state=root/'.prof-state'
manifest=json.loads((state/'manifest.json').read_text())
topic=json.loads((state/'topics/definite-integrals.json').read_text())
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
sources=[]
reads=[]
def source(sid,path,locator,note,url=None):
    entry={'id':sid,'path':str(path),'sha256':sha(path),'portions':[{'id':'read','locator':locator,'disposition':'required','reason':'Required operative/source input for this declared topic.','evidence':[]}]}
    if url: entry['url']=url
    sources.append(entry)
    reads.append({'source_id':sid,'portion_id':'read','status':'read','reviewed_sha256':entry['sha256'],'note':note})

source('baseline',root/'inputs/prof/references/sasis/ocr-baseline-20261007/student-baseline.txt','Complete Python splitlines1–2561, all four subjects','Complete bounded read ranges and gap recovery are recorded in author/input-admission.json. Actual specific dependency locators and their use are in author/coverage-and-research.md; calculus, finite sums, geometry, units and graph area are available, while pyramid volume and the general existence statement are introduced locally.')
refs={
'execution-protocol.md':'Source portions, conventions, learner-route reconstruction, full integration and destination-specific checks govern the saved audit; recovery reread also complete.',
'sasis.md':'Fresh-author/reader boundary, two reader subject inputs, full original report, PROF-only repair and publication-first restart govern this cycle.',
'sasis/profile-manifest.json':'Pins the operational baseline and reader resources; this manifest does not replace their full content.',
'sasis/student-role.txt':'The exact short reader operating instruction was passed to the fresh reader.',
'sasis/student-testing-contract.txt':'Reader continuation after gaps and meaning/premise/connection/conclusion audit, without grading, constrain the separate original report.',
'sasis/rewrite-guide.md':'Every supported issue is audited across the full document; teaching stays frozen and material repairs belong in PROF.',
'domain-patterns.md':'Mathematics route requires representation, assumptions, inference warrants, connected examples and interpretation; no domain example was treated as mandatory topic.',
'state-tool.md':'The helper only tests recorded identities, locators and freshness; current pending destination status must prevent readiness.'}
for i,(name,note) in enumerate(refs.items(),1):source('operative-ref-'+str(i),root/'inputs/prof/references'/name,'Whole file',note)
page_notes={1:'MIT OCW cover establishes source identity and course/lecture provenance.',2:'Curved region, Figure1 rectangle approximation and x² right-endpoint total; retained in PartA and Figure1.',3:'Figures2–3, square sum and enclosing pyramids; the source prism wording is corrected through introduced volume theorem and every-height containment in PartB.',4:'Common x² limit, line/triangle example, Figure4 and area derivative observation; retained in PartsB–D.',5:'General equal-width sampled Riemann sum, Figure5, simple-interest law, borrowing-rate units and month samples; retained in PartsD andF.',6:'Continuous principal and time-weighted debt; corrected money units and fixed-month versus refining-partition distinction in PartF.'}
source('original-pdf',root/'inputs/source/lec18.pdf','All6 pages, cover plus printed1–5','Every source page was read as text and as a full raster image. The separate page declarations bind these actual constituents.', 'https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/d1b3d809b6505825b5cde0cee823fa0f_lec18.pdf')
for i,note in page_notes.items():
    for ext in ['txt','png']:source(f'source-page-{i}-{ext}',root/f'inputs/source/lec18-p{i:02d}.{ext}',f'Complete original PDF page{i}; '+('full image' if ext=='png' else 'extracted text'),note)
source('source-identity',root/'inputs/source/source-identity.json','Whole manifest','Binds unchanged PDF and all six text/image page representations to their original source; no content substitution.')
source('scope-research',root/'author/coverage-and-research.md','Whole authored source/convention/research record','Maps all six declared capabilities to original PDF pages and figures, exact baseline prerequisites and final PartsA–F. It preserves the actually inspected official supplementary passage and source corrections. This is an author record, not subject material supplied to SASIS.')

outputs=[]
for i,p in enumerate(sorted((root/'teaching').rglob('*')),1):
    if p.is_file():outputs.append({'id':'frozen-'+str(i),'path':str(p.relative_to(root)),'sha256':sha(p)})
manifest['sources']=sources
manifest['outputs']=outputs
manifest['required_topics'][0].update(title='D016: construct and interpret definite integrals',source_portions=[{'source_id':s['id'],'portion_id':'read'} for s in sources],outputs=[o['id'] for o in outputs])
extra=[('source_integrity','Every assigned original page/figure and actual operative package is admitted and bound.'),('technical','Independent prompt-first answers and complete frozen mathematical review.'),('reader','Fresh SASIS full-baseline/full-document original report and access verification.'),('native_figures','Every exact saved figure including its canvas edges.'),('source_structure','Markup source, matching tasks/help and local targets.'),('destination','Actual GitHub math preservation, styling, embedded figures and navigation.'),('published_bytes','Exact frozen constituents fetched back from immutable GitHub commit.'),('earlier_cases','Affected accepted cases checked under the current published package.')]
existing={c['id'] for c in manifest['output_checks']}
for cid,description in extra:
    if cid not in existing:manifest['output_checks'].append({'id':cid,'description':description,'applicable':True,'status':'pending','reason':'','evidence':[],'dependencies':[]})
topic['source_reads']=reads
(state/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
(state/'topics/definite-integrals.json').write_text(json.dumps(topic,indent=2)+'\n')
print(json.dumps({'sources':len(sources),'outputs':len(outputs),'checks':'All statuses remain pending until actual reports are reconciled.'}))
