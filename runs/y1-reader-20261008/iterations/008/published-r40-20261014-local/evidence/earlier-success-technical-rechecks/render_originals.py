from pathlib import Path
import sys,hashlib,json,urllib.request
out=Path(__file__).resolve().parent
sys.path.insert(0,str(out/'runtime/python-packages'))
import pymupdf
sys.stdout.reconfigure(encoding='utf-8')
url='https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/a30756fe9d577184f205b09bc6d6d005_lec7.pdf'
d=out/'D007/originals'; d.mkdir(parents=True,exist_ok=True)
pdf=d/'lec7.pdf'
data=urllib.request.urlopen(url).read()
assert len(data)==113363 and hashlib.sha256(data).hexdigest()=='47316203594d35c47220c7049238045ff0a2ac73ba3292d17107f13d575f3602'
pdf.write_bytes(data)
record={'runtime':{'module':pymupdf.__file__,'version':pymupdf.VersionBind,'write_destinations':'All target packages, installation temporary files, pip cache and outputs confined to earlier-success-technical-rechecks/runtime or case subdirectories; interpreter used -B'},'d007_official_url':url,'documents':[]}
for case in ['D007','D009','D012','D013','D015']:
 pdf=next((out/case/'originals').glob('*.pdf'))
 data=pdf.read_bytes(); doc=pymupdf.open(pdf)
 dest=out/case/'fresh-pdf-render'; dest.mkdir(parents=True,exist_ok=True)
 item={'case':case,'pdf':str(pdf),'pdf_bytes':len(data),'pdf_sha256':hashlib.sha256(data).hexdigest(),'page_count':len(doc),'pages':[]}
 for i,page in enumerate(doc,1):
  target=dest/f'page-{i:02d}.png'; page.get_pixmap(matrix=pymupdf.Matrix(2,2),alpha=False).save(target)
  (dest/f'page-{i:02d}.txt').write_text(page.get_text(),encoding='utf-8')
  b=target.read_bytes(); item['pages'].append({'page':i,'image':str(target),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'scale':2,'width':page.rect.width*2,'height':page.rect.height*2})
 record['documents'].append(item)
(out/'original-render-identities.json').write_text(json.dumps(record,indent=2),encoding='utf-8')
print(json.dumps({'runtime':record['runtime'],'documents':[{k:v for k,v in x.items() if k!='pages'} for x in record['documents']]},indent=2))
