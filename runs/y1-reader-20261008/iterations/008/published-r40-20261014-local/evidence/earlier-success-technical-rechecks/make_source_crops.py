from pathlib import Path
import sys,json,hashlib
out=Path(__file__).resolve().parent
sys.path.insert(0,str(out/'runtime/python-packages'))
import pymupdf
jobs=[
 ('D007',5,'anything-and-example',(80,105,535,270)),
 ('D009',2,'critical-point-terminology',(80,170,535,450)),
 ('D009',6,'selected-sequence-tail',(80,130,535,260)),
 ('D009',8,'inflection-definition',(80,15,535,85)),
 ('D012',3,'denominator-contrast',(185,515,535,615)),
 ('D012',4,'iterate-table-and-digits',(80,110,535,260)),
 ('D012',5,'cycle-body-and-caption',(80,425,535,700)),
 ('D012',6,'distance-label-and-constraint',(80,150,535,545)),
 ('D013',4,'decreasing-definition',(80,485,535,535)),
 ('D015',3,'gaussian-sign',(80,575,535,660)),
 ('D015',4,'family-minus-two-member',(230,560,385,660))]
r=[]
for case,n,label,rect in jobs:
 pdf=next((out/case/'originals').glob('*.pdf'));doc=pymupdf.open(pdf)
 d=out/case/'source-crops';d.mkdir(exist_ok=True)
 p=d/f'{label}-pdf-page-{n}.png'
 doc[n-1].get_pixmap(matrix=pymupdf.Matrix(4,4),clip=pymupdf.Rect(*rect),alpha=False).save(p)
 b=p.read_bytes();r.append({'case':case,'original_pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'pdf_page':n,'clip_pdf_points':rect,'scale':4,'file':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
(out/'source-crop-identities.json').write_text(json.dumps(r,indent=2),encoding='utf-8')
print('Created',len(r),'direct-PDF high-resolution crops; each is supplemental to viewed full page context.')
