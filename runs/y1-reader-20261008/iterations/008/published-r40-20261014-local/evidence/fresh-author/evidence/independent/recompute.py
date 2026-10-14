"""Independent D008 original-source technical audit. No network or installs."""
from pathlib import Path
from decimal import Decimal as D, getcontext
from fractions import Fraction as F
import hashlib, importlib.util, json, math, sys
from PIL import Image
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent
INPUT = ROOT.parents[2] / "original-inputs"
getcontext().prec = 80

def dstr(x):
    return str(x)

def sin(x):
    term = x
    total = term
    k = 1
    while True:
        term *= -x*x / D((2*k)*(2*k+1))
        nxt = total + term
        if nxt == total:
            return total
        total = nxt
        k += 1

def cos(x):
    term = D(1)
    total = term
    k = 1
    while True:
        term *= -x*x / D((2*k-1)*(2*k))
        nxt = total + term
        if nxt == total:
            return total
        total = nxt
        k += 1

manifest = json.loads((INPUT / "source-identities.json").read_text(encoding="utf-8"))
hashes = []
for rec in manifest["files"]:
    file = INPUT / rec["file"]
    actual = hashlib.sha256(file.read_bytes()).hexdigest()
    hashes.append({"file": rec["file"], "bytes": file.stat().st_size,
                   "sha256": actual, "matches_supplied_manifest": actual == rec["sha256"]})
assert all(r["matches_supplied_manifest"] for r in hashes)

reader = PdfReader(INPUT / "mit-18.01-fall-2006-lec9.pdf")
assert len(reader.pages) == 7
(ROOT / "pdf-direct-extraction.txt").write_text(
    "\n\n".join(f"PDF page {i+1}\n{p.extract_text()}" for i,p in enumerate(reader.pages)),
    encoding="utf-8")

# Crops from a new Poppler rendering of the actual PDF at 250 dpi.
crops = [(3, "p3-proof-equalities.png", (85,175,535,410)),
         (4, "p4-derivative-sign.png", (85,295,535,365)),
         (5, "p5-time-factor-exponent.png", (85,300,535,365))]
for page, name, (x0,y0,x1,y1) in crops:
    src = ROOT / f"rendered-source-{page}.png"
    img = Image.open(src)
    sx,sy = img.width/612,img.height/792
    img.crop((round(x0*sx),round(y0*sy),round(x1*sx),round(y1*sy))).save(ROOT / name)

values = []
for sx in ["-0.2", "-0.1", "-0.01", "0", "0.01", "0.1", "0.2", "0.4"]:
    x = D(sx)
    true = (-2*x).exp() / (1+x).sqrt()
    linear = 1-D(5)*x/2
    quadratic = linear+D(27)*x*x/8
    values.append({"x":sx, "f":dstr(true), "L1":dstr(linear), "Q2":dstr(quadratic),
                   "f_minus_L1":dstr(true-linear), "f_minus_Q2":dstr(true-quadratic),
                   "absolute_relative_error_L1":dstr(abs(true-linear)/true),
                   "absolute_relative_error_Q2":dstr(abs(true-quadratic)/true)})

basic = []
for sx in ["-0.1", "0", "0.1"]:
    x=D(sx)
    for name,true,L,Q in [
        ("sin(x)",sin(x),x,x),
        ("cos(x)",cos(x),D(1),1-x*x/2),
        ("exp(x)",x.exp(),1+x,1+x+x*x/2),
        ("ln(1+x)",(1+x).ln(),x,x-x*x/2),
        ("(1+x)^(-1/2)",1/(1+x).sqrt(),1-x/2,1-x/2+3*x*x/8)]:
        basic.append({"function":name,"x":sx,"true":dstr(true),"L1":dstr(L),"Q2":dstr(Q),
                      "true_minus_L1":dstr(true-L),"true_minus_Q2":dstr(true-Q)})

v,c=D(4),D(300000)
beta=v/c
q=beta*beta
gamma=1/(1-q).sqrt()
L=1+q/2
Q=L+3*q*q/8
stable_increment=q/((1-q).sqrt()*(1+(1-q).sqrt()))
assert abs((gamma-1)-stable_increment)<D("1e-78")
quirk={"inputs_km_per_s":{"v":dstr(v),"c":dstr(c)},"beta":dstr(beta),"q":dstr(q),
       "gamma":dstr(gamma),"gamma_minus_1":dstr(gamma-1),
       "linear_factor":dstr(L),"quadratic_factor":dstr(Q),
       "linear_increment_q_over_2":dstr(q/2),"quadratic_correction_3q2_over_8":dstr(3*q*q/8),
       "cubic_leading_term_5q3_over_16":dstr(5*q*q*q/16),
       "gamma_minus_L":dstr(gamma-L),"gamma_minus_Q":dstr(gamma-Q),
       "fractional_error_of_increment_if_q_rounded_to_1e-10":dstr(abs(D("1e-10")/2-q/2)/(q/2)),
       "difference_seconds_if_onboard_T_is_86400_seconds":dstr(D(86400)*(gamma-1)),
       "difference_microseconds_if_onboard_T_is_86400_seconds":dstr(D(86400)*(gamma-1)*D(10)**6),
       "satellite_lag_seconds_if_ground_Tprime_is_86400_seconds":dstr(D(86400)*(1-(1-q).sqrt())),
       "float_gamma_minus_1":repr(1/math.sqrt(1-float(q))-1)}

coeff = [F(math.comb(10,k)*(2**k)) for k in range(11)]
limits=[]
for sx in ["-0.01","-0.001","0.001","0.01"]:
    x=D(sx)
    quotient=((1+2*x)**10-1)/x
    limits.append({"x":sx,"difference_quotient":dstr(quotient),"minus_limit_20":dstr(quotient-20)})
out={"scope":"Independent original-source calculation audit; no author draft or prior reports read.",
     "runtime":{"executable":sys.executable,"version":sys.version,
                "modules":{m:(importlib.util.find_spec(m).origin if importlib.util.find_spec(m) else None)
                           for m in ["pypdf","pdfplumber","PIL","decimal","fractions","sympy","mpmath"]},
                "decimal_precision":getcontext().prec,"installs":[]},
     "inputs_verified":hashes,"pdf_pages":len(reader.pages),
     "source_page_png_dimensions":{f.name:Image.open(f).size for f in INPUT.glob("page-*.png")},
     "product_function_checks":values,"basic_function_checks":basic,
     "planet_quirk":quirk,"binomial_coefficients_(1+2x)^10":[str(z) for z in coeff],
     "limit_numeric_checks":limits}
(ROOT/"recomputed-values.json").write_text(json.dumps(out,indent=2),encoding="utf-8")
print(json.dumps({"hashes_ok":True,"pdf_pages":7,"product_function_checks":values,
                  "planet_quirk":quirk,"limit_numeric_checks":limits},indent=2))
