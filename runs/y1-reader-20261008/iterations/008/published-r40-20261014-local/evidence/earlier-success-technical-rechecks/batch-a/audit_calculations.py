from pathlib import Path
import sys,json,hashlib,re
from decimal import Decimal,localcontext,ROUND_HALF_UP
from fractions import Fraction

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
PACKAGES=HERE.parent/'runtime/python-packages'
sys.path.insert(0,str(PACKAGES))
import pymupdf
assert Path(pymupdf.__file__).resolve().is_relative_to(PACKAGES.resolve())
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
identities=json.loads((HERE/'identities.json').read_text(encoding='utf-8'))
crop_specs={
 'D003':[(2,'missing-primes-context',(75,245,535,465))],
 'D005':[(2,'rational-circle-context',(75,190,535,670)),(3,'implicit-inverse-context',(75,95,535,650))],
 'D006':[(3,'coordinate-prose-context',(75,350,535,535)),(4,'coordinate-figure-context',(125,425,480,710)),(5,'inverse-box-context',(75,280,535,650))]
}
for c in identities['cases']:
 cid=c['material_id']; d=HERE/cid; doc=pymupdf.open(d/'original.pdf')
 c['additional_rendered_pages']=[]
 for p in {'D003':[3,4,5],'D005':[],'D006':[2,6,7]}[cid]:
  target=d/f'original-page-{p:02d}.png'
  doc[p-1].get_pixmap(matrix=pymupdf.Matrix(2.5,2.5),alpha=False).save(target)
  c['additional_rendered_pages'].append({'physical_page':p,'path':str(target),'sha256':sha(target)})
 c['crops']=[]
 for p,label,coords in crop_specs[cid]:
  target=d/f'crop-{label}.png'
  doc[p-1].get_pixmap(matrix=pymupdf.Matrix(4,4),clip=pymupdf.Rect(*coords),alpha=False).save(target)
  c['crops'].append({'physical_page':p,'label':label,'pdf_clip_points':coords,'path':str(target),'sha256':sha(target)})

numeric=[]
with localcontext() as ctx:
 ctx.prec=70
 D=Decimal
 def add(cid,line,label,formula,inputs,value,printed,places,unit):
  q=D(1).scaleb(-places); rounded=value.quantize(q,rounding=ROUND_HALF_UP)
  ok=rounded==D(printed)
  assert ok,(cid,label,value,rounded,printed)
  teaching=next(x for x in identities['cases'] if x['material_id']==cid)
  raw=Path(teaching['accepted_copy']).read_text(encoding='utf-8').splitlines()[line-1]
  assert printed in raw,(label,printed,raw)
  numeric.append({'material_id':cid,'line':line,'label':label,'learner_formula':formula,'stated_inputs':inputs,'computed_decimal_70_digit_context':str(value),'printed_value':printed,'decimal_places':places,'unit':unit,'rounding_rule':'nearest, half up; no tie occurs','rounded_result':str(rounded),'printed_line':raw,'pass':ok})
 q=D('1.1')**10; e=D(1).exp()
 add('D006',364,'k=10 sequence value','(1+1/k)^k',{'k':'10'},q,'2.59374',5,'dimensionless')
 add('D006',364,'comparison e','exp(1)',{'exponent':'1'},e,'2.71828',5,'dimensionless')
 add('D006',364,'relative shortfall below e','100*(e-(1.1)^10)/e',{'denominator':'e'},100*(e-q)/e,'4.58',2,'percent below e')
 add('D006',428,'one-day positive growth','100*(exp(0.03*t)-1)',{'t':'1 day','continuous relative rate':'0.03 per day'},100*(D('.03').exp()-1),'3.045',3,'percent')
 add('D006',677,'50 point fall from 300','100*(-50)/300',{'initial':'300 points','change':'-50 points'},D(-50)/D(300)*100,'-16.67',2,'percent')
 add('D006',678,'50 point fall from 10000','100*(-50)/10000',{'initial':'10000 points','change':'-50 points'},D(-50)/D(10000)*100,'-0.5',1,'percent (exact)')
 add('D006',689,'one-day negative growth','100*(exp(-0.02*t)-1)',{'t':'1 day','continuous relative rate':'-0.02 per day'},100*(D('-.02').exp()-1),'-1.9801',4,'percent')
 # Supplement ordinary exact decimal arithmetic; these are not reclassified as check-labelled decimals.
 arithmetic=[
 {'case':'D003','line':47,'formula':'3*0.2-0.5','exact':str(D(3)*D('.2')-D('.5')),'unit':'V/s'},
 {'case':'D003','line':257,'formula':'2*0.30-0.40','exact':str(D(2)*D('.30')-D('.40')),'unit':'V/s'},
 {'case':'D003','line':264,'formula':'(-0.2)*4+3*0.5','exact':str(D('-.2')*4+D(3)*D('.5')),'unit':'m^2/s'},
 {'case':'D006','line':428,'formula':'80*0.03','exact':str(D(80)*D('.03')),'unit':'points/day coefficient'},
 {'case':'D006','line':670,'formula':'300*(-0.02), 10000*(-0.02), 100*(-0.02)','exact':[str(D(300)*D('-.02')),str(D(10000)*D('-.02')),str(100*D('-.02'))],'unit':['points/day','points/day','percent/day']}
 ]
allscan={}
for c in identities['cases']:
 text=Path(c['accepted_copy']).read_text(encoding='utf-8')
 allscan[c['material_id']]={'line_count':len(text.splitlines()),'terms':[{'line':i,'text':line} for i,line in enumerate(text.splitlines(),1) if re.search(r'\b(?:directly|independent|check|source|printed|compressed|approximate|approximation)\b',line,re.I)]}
(HERE/'identities.json').write_text(json.dumps(identities,indent=2),encoding='utf-8')
(HERE/'numeric-final-value-witnesses.json').write_text(json.dumps({'precision':70,'method':'Python Decimal exact rational arithmetic and Decimal.exp, independently recomputed from final teaching formulas','rounded_checks':numeric,'supplementary_exact_arithmetic':arithmetic},indent=2),encoding='utf-8')
(HERE/'all-candidate-passages.json').write_text(json.dumps(allscan,indent=2),encoding='utf-8')
(HERE/'tool-origin.json').write_text(json.dumps({'python':sys.executable,'pymupdf_origin':pymupdf.__file__,'pymupdf_version':pymupdf.__version__,'package_write_owner':'parent created runtime; this worker reads it; -B used','crop_raster_scale':'4 pixels/PDF point','new_whole_page_scale':'2.5 pixels/PDF point','initial_poppler_pages':'pdftoppm 180 dpi; display-font warnings Symbol and ArialUnicode retained in review limitation; target crops additionally rendered directly with pymupdf'},indent=2),encoding='utf-8')
print(json.dumps({'rounding_checks':len(numeric),'passed':all(n['pass'] for n in numeric),'pymupdf_origin':pymupdf.__file__,'crop_count':sum(len(c['crops']) for c in identities['cases'])},indent=2))
