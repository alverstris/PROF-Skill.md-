from pathlib import Path
from hashlib import sha256
from decimal import Decimal, getcontext
import json, sys
from PIL import Image
from pypdf import PdfReader

sys.stdout.reconfigure(encoding='utf-8')
root=Path(__file__).resolve().parent
src=root.parent/'original-inputs'
manifest=json.loads((src/'source-identities.json').read_text(encoding='utf-8'))
out={'source_files':[]}
for item in manifest['files']:
    data=(src/item['file']).read_bytes()
    actual=sha256(data).hexdigest()
    out['source_files'].append({'file':item['file'],'bytes':len(data),'sha256':actual,'matches':len(data)==item['bytes'] and actual==item['sha256']})
reader=PdfReader(src/'mit-18.01-fall-2006-lec9.pdf')
out['pdf_pages']=len(reader.pages)
out['pdf_metadata']=str(reader.metadata)
for i,p in enumerate(reader.pages,1):
    (root/f'original-pdf-page-{i}-pypdf.txt').write_text(p.extract_text(),encoding='utf-8')
for page,box in [(3,(180,380,1090,470)),(4,(180,680,1090,765)),(5,(180,675,1090,765))]:
    im=Image.open(src/f'page-{page}.png')
    crop=im.crop(box)
    crop.resize((crop.width*2,crop.height*2)).save(root/f'original-page-{page}-disputed-glyphs.png')
getcontext().prec=80
v=Decimal(4); c=Decimal(300000); z=v*v/(c*c)
gamma=1/(1-z).sqrt()
out['planet_quirk']={k:str(val) for k,val in {'v_km_s':v,'c_km_s':c,'z':z,'z_squared':z*z,'linear_increment':z/2,'quadratic_increment':3*z*z/8,'gamma':gamma,'linear_gamma':1+z/2,'quadratic_gamma':1+z/2+3*z*z/8,'linear_error':gamma-(1+z/2),'quadratic_error':gamma-(1+z/2+3*z*z/8),'one_day_kinematic_seconds':Decimal(86400)*z/2}.items()}
# Direct logarithmic derivative: f'/f=-2-1/(2(1+x)); f''/f=(f'/f)^2+1/(2(1+x)^2).
out['combined_function_at_zero']={'f':'1','f_prime':'-5/2','f_double_prime':'27/4','linear_coefficient':'-5/2','quadratic_coefficient':'27/8','direct_derivative_warrant':'f_prime/f=-2-1/(2(1+x)); f_double_prime/f=(-2-1/(2(1+x)))^2+1/(2(1+x)^2)'}
out['binomial_limit']={'function':'(1+2x)^10','linear_coefficient':'20','quadratic_coefficient':'180','limit':'20','warrant':'finite binomial polynomial: difference quotient=20+180x+...; every remaining term has a positive power of x'}
(root/'original-check-results.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
