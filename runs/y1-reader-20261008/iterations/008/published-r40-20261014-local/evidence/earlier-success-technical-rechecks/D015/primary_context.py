from pathlib import Path
import sys,urllib.request,json,hashlib
out=Path(__file__).resolve().parent
sys.path.insert(0,str(out.parent/'runtime/python-packages'))
import pymupdf
d=out/'primary-context';d.mkdir(exist_ok=True)
urls={'harmonic-oscillator.pdf':'https://ocw.mit.edu/courses/5-61-physical-chemistry-fall-2017/ca914a031c803bf4728976edf1852390_MIT5_61F17_lec9.pdf','lec16-resource.html':'https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/resources/lec16/'}
r=[]
for name,url in urls.items():
 b=urllib.request.urlopen(url).read();(d/name).write_bytes(b)
 r.append({'file':name,'url':url,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
doc=pymupdf.open(d/'harmonic-oscillator.pdf')
for n in [2,3,6]:
 p=doc[n-1];im=d/f'oscillator-page-{n}.png';p.get_pixmap(matrix=pymupdf.Matrix(2,2),alpha=False).save(im)
 (d/f'oscillator-page-{n}.txt').write_text(p.get_text(),encoding='utf-8')
 b=im.read_bytes();r.append({'file':im.name,'pdf_page':n,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
(d/'identities.json').write_text(json.dumps(r,indent=2),encoding='utf-8')
print(json.dumps(r,indent=2))
