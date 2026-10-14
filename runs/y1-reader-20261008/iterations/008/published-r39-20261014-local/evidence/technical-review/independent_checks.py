"""Independent pre-teaching checks. Reads only original source; writes review output."""
from pathlib import Path
import hashlib
import json
import math
from decimal import Decimal, getcontext
from fractions import Fraction as F
from pypdf import PdfReader
from PIL import Image

HERE = Path(__file__).resolve().parent
ORIG = HERE.parent / 'original-inputs'
def binomial_coeffs(a, n):
    out = [F(1)]
    for k in range(1,n+1):
        out.append(out[-1]*(a-k+1)/k)
    return out

def product_coeffs(a,b):
    out = [F(0)]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b):
            out[i+j] += u*v
    return out

exp_minus2 = [F((-2)**k,math.factorial(k)) for k in range(4)]
reciprocal_root = binomial_coeffs(F(-1,2),3)
composite = product_coeffs(exp_minus2,reciprocal_root)[:4]
result = {
    'calculation_method':'Exact rational binomial/exponential coefficients and convolution; analytic derivative checks recorded independently in source-reconstruction.md. Decimal high-precision numeric check. Initial SymPy/mpmath attempt unavailable, not claimed as executed.',
    'sin_coefficients_through_cubic':['0','1','0','-1/6'],
    'cos_coefficients_through_cubic':['1','0','-1/2','0'],
    'exp_coefficients_through_cubic':[str(F(1,math.factorial(k))) for k in range(4)],
    'log1p_coefficients_through_cubic':['0','1','-1/2','1/3'],
    'exp_minus2_coefficients_through_cubic':list(map(str,exp_minus2)),
    'reciprocal_root_coefficients_through_cubic':list(map(str,reciprocal_root)),
    'composite_coefficients_through_cubic':list(map(str,composite)),
    'exam_power_coefficients':[str(F(math.comb(10,k)*2**k)) for k in range(11)],
    'exam_limit':str(math.comb(10,1)*2),
    'quadratic_product_full_coefficients':list(map(str,product_coeffs(exp_minus2[:3],reciprocal_root[:3]))),
}
getcontext().prec = 70
D = Decimal
z = (D(4)/D(300000))**2
gamma = 1/(1-z).sqrt()
result['relativity'] = {k:str(v) for k,v in {
    'z=(v/c)^2':z,
    'gamma-1':gamma-1,
    'linear_correction=z/2':z/2,
    'quadratic_correction=3z^2/8':3*z*z/8,
    'error_after_linear':gamma-(1+z/2),
    'error_after_quadratic':gamma-(1+z/2+3*z*z/8),
    'kinematic_lag_seconds_per_86400s':D(86400)*(1-(1-z).sqrt()),
}.items()}
result['composite_numerical'] = []
for v in ['0.1','-0.1','0.01','-0.01']:
    t = D(v)
    exact = (-2*t).exp()/(1+t).sqrt()
    L = 1-D(5)/2*t
    Q = L+D(27)/8*t*t
    result['composite_numerical'].append({
        'x':v,'exact':str(exact),'linear':str(L),
        'quadratic':str(Q),'linear_error':str(exact-L),
        'quadratic_error':str(exact-Q)})
pdf = ORIG/'mit-18.01-fall-2006-lec9.pdf'
reader = PdfReader(pdf)
result['pdf_validation'] = {
    'sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),
    'bytes':pdf.stat().st_size,'pages':len(reader.pages),
    'title_page_text':reader.pages[0].extract_text(),
    'page_dimensions_points':[[float(p.mediabox.width),float(p.mediabox.height)] for p in reader.pages],
    'page_images':[]}
for n in range(1,8):
    p = ORIG/f'page-{n}.png'
    with Image.open(p) as im:
        im.load()
        result['pdf_validation']['page_images'].append({'page':n,'size':list(im.size),
            'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
(HERE/'independent-check-results.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2))
