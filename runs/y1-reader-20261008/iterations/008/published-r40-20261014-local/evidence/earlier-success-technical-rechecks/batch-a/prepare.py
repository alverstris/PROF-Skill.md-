from pathlib import Path
import json, hashlib, urllib.request, subprocess
from pypdf import PdfReader

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
OLD=ROOT/'.prof-sasis/20261014-d008-r39/earlier-success-review'
INV=json.loads((OLD/'accepted-teaching-exposure-inventory.json').read_text(encoding='utf-8'))
QUEUE=json.loads((ROOT/'.prof-sasis/20261014-d008-r40/run-state/queue.json').read_text(encoding='utf-8'))
SOURCES={
 'D003':('23c2c1b1ab31c9f10745b18e7b0bf131_lec3.pdf','ccf25930cfad63d99e3fd5045e7931860051bbbb3eedd2bd8cd9318ebd32845a'),
 'D005':('18d6a86a30a4bc046c5f7034d47587f1_lec5.pdf','d0ed3d4624b0a15cc5c65cff6aece48f70e185f5c417ba7d37a7c935b652848c'),
 'D006':('f9af0e98490296c99d330faf47389507_lec6.pdf','e36b81f73c0e6265a814de8875c3898b1255d2e0aa656547a731b8274a00f66d')
}
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
POPPLER=Path('C:/Users/alver/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/poppler/Library/bin/pdftoppm.exe')
records=[]
for case in INV['cases']:
 cid=case['material_id']
 if cid not in SOURCES: continue
 dest=HERE/cid; dest.mkdir(parents=True,exist_ok=True)
 artifact=case['artifacts'][0]
 sourcecopy=next((OLD/cid).glob('teaching__*.md'))
 assert sha(sourcecopy)==artifact['sha256']
 (dest/'teaching-line-numbered.txt').write_text('\n'.join(f'{i}: {l}' for i,l in enumerate(sourcecopy.read_text(encoding='utf-8').splitlines(),1))+'\n',encoding='utf-8')
 remote,expected=SOURCES[cid]
 url='https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/'+remote
 pdf=dest/'original.pdf'
 if not pdf.exists():
  with urllib.request.urlopen(url) as r: pdf.write_bytes(r.read())
 assert sha(pdf)==expected, (cid,sha(pdf),expected)
 reader=PdfReader(pdf)
 (dest/'original-extraction.txt').write_text('\n'.join(f'\nPHYSICAL PDF PAGE {i+1}\n{page.extract_text()}' for i,page in enumerate(reader.pages)),encoding='utf-8')
 pages={'D003':[2],'D005':[2,3,4,5],'D006':[3,4,5,8]}[cid]
 for n in pages:
  output=dest/f'original-page-{n:02d}'
  if not output.with_suffix('.png').exists():
   subprocess.run([str(POPPLER),'-f',str(n),'-l',str(n),'-singlefile','-r','180','-png',str(pdf),str(output)],check=True)
 rec={'material_id':cid,'revision':case['revision'],'accepted_commit':case['commit'],'teaching_artifact':artifact,'accepted_copy':str(sourcecopy),'actual_teaching_sha256':sha(sourcecopy),'original_url':url,'original_pdf':str(pdf),'original_sha256':sha(pdf),'original_page_count':len(reader.pages),'rendered_pages':[{ 'physical_page':n,'path':str(dest/f'original-page-{n:02d}.png'),'sha256':sha(dest/f'original-page-{n:02d}.png')} for n in pages]}
 records.append(rec)
(HERE/'identities.json').write_text(json.dumps({'scope':'D003,D005,D006 source attribution and numerical validation rechecks only','prof_revision':QUEUE.get('current_prof_revision'),'prof_package_commit':QUEUE.get('current_prof_package_commit'),'queue_sha256':sha(ROOT/'.prof-sasis/20261014-d008-r40/run-state/queue.json'),'cases':records},indent=2),encoding='utf-8')
print(json.dumps([{'case':x['material_id'],'teaching_sha256':x['actual_teaching_sha256'],'original_sha256':x['original_sha256'],'pages':x['original_page_count']} for x in records],indent=2))
