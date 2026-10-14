"""Independent numerical/exact-arithmetic checks of the original Lecture 9 PDF.

Reads the original source only for hashing. Writes calculation evidence beside
this script. Uses Python's standard library; no previous work is consulted.
"""
from decimal import Decimal, getcontext
from fractions import Fraction as F
from hashlib import sha256
from math import comb, factorial
from pathlib import Path
import json

getcontext().prec = 80
OUT = Path(__file__).resolve().parent
SOURCE = OUT.parents[2] / "original-inputs" / "mit-18.01-fall-2006-lec9.pdf"

def poly_product(a, b):
    c = [F(0)] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            c[i+j] += ai*bj
    return c

def s(value):
    return str(value)

# Independently derive binomial coefficients using their product definition.
def binomial_coefficients(r, degree):
    c = [F(1)]
    for k in range(1, degree + 1):
        c.append(c[-1] * (r-k+1) / k)
    return c

exp_minus_2 = [F((-2)**k, factorial(k)) for k in range(4)]
recip_sqrt = binomial_coefficients(F(-1,2), 3)
composite = poly_product(exp_minus_2, recip_sqrt)
assert composite[:4] == [F(1), F(-5,2), F(27,8), F(-163,48)]
A0, Ap0, App0 = F(-5,2), F(1,2), F(-1)
f0, fp0 = F(1), A0
fpp0 = A0*A0 + Ap0
fppp0 = A0**3 + 3*A0*Ap0 + App0
assert [f0, fp0, fpp0/2, fppp0/6] == composite[:4]
linear_product = poly_product([F(1),F(-2)], [F(1),F(-1,2)])
quadratic_product = poly_product(exp_minus_2[:3], recip_sqrt[:3])
assert linear_product == [F(1), F(-5,2), F(1)]
assert quadratic_product == [F(1),F(-5,2),F(27,8),F(-7,4),F(3,4)]

# Exact polynomial establishes the lecture's limit without informal ~ division.
power10 = [comb(10,k)*2**k for k in range(11)]
assert power10[0] == 1 and power10[1] == 20

# Relativistic numerical example using precisely the lecture's rounded c.
v, c = Decimal(4), Decimal(300000)
z = (v/c)**2
gamma = Decimal(1)/(Decimal(1)-z).sqrt()
linear_gamma = 1+z/2
quad_correction = Decimal(3)*z*z/8
quadratic_gamma = linear_gamma+quad_correction
leading_omitted = Decimal(5)*z**3/16
assert gamma > quadratic_gamma > linear_gamma > 1
assert abs((gamma-quadratic_gamma)/leading_omitted-1) < Decimal("1e-8")

samples = []
for rawx in ["-0.1", "-0.01", "0.01", "0.1"]:
    x = Decimal(rawx)
    actual = (-2*x).exp()/(1+x).sqrt()
    L = 1-Decimal(5)*x/2
    Q = L+Decimal(27)*x*x/8
    samples.append({"x":rawx, "actual":s(actual), "linear":s(L),
                    "quadratic":s(Q), "linear_signed_error_actual_minus_approx":s(actual-L),
                    "quadratic_signed_error_actual_minus_approx":s(actual-Q)})

# Smooth counterexamples to broad qualitative readings of source statements.
x = F(1,100)
f = x*x-100*x**3
assert f == 0
finite_comparison = {"function":"x^2 - 100*x^3", "basepoint":"0", "x":s(x),
                     "f(x)":s(f), "L(x)":"0", "Q(x)":s(x*x),
                     "linear_abs_error":"0", "quadratic_abs_error":s(x*x)}
distance_counterexample = [{"x":s(t), "abs_error_for_f=x+x^2(1-x)^2_and_L=x":s(t*t*(1-t)**2)}
                           for t in [F(0),F(1,2),F(1)]]

out = {
    "source_sha256":sha256(SOURCE.read_bytes()).hexdigest(),
    "precision_decimal_digits":getcontext().prec,
    "composite_exact":{
       "exp(-2x)_coeffs_degree_0_through_3":list(map(s,exp_minus_2)),
       "(1+x)^(-1/2)_coeffs_degree_0_through_3":list(map(s,recip_sqrt)),
       "correct_product_coeffs_degree_0_through_3":list(map(s,composite[:4])),
       "product_of_linear_truncations_all_coeffs":list(map(s,linear_product)),
       "product_of_quadratic_truncations_all_coeffs":list(map(s,quadratic_product)),
       "derivatives_at_zero_orders_0_through_3":list(map(s,[f0,fp0,fpp0,fppp0]))},
    "(1+2x)^10_exact_coefficients_degrees_0_through_10":power10,
    "limit_((1+2x)^10-1)/x_as_x_to_0":power10[1],
    "planet_quirk":{
       "v_km_s":s(v),"c_km_s":s(c),"z=v^2/c^2":s(z),
       "z^2":s(z*z),"gamma_exact_to_working_precision":s(gamma),
       "gamma_minus_1":s(gamma-1),"linear_gamma":s(linear_gamma),
       "quadratic_correction_3z^2/8":s(quad_correction),
       "quadratic_gamma":s(quadratic_gamma),
       "linear_abs_error":s(gamma-linear_gamma),
       "quadratic_abs_error":s(gamma-quadratic_gamma),
       "leading_omitted_cubic_5z^3/16":s(leading_omitted),
       "delta_seconds_for_T=86400_seconds":s((gamma-1)*86400),
       "quadratic_correction_seconds_for_T=86400_seconds":s(quad_correction*86400)},
    "composite_numerical_samples":samples,
    "quadratic_not_always_more_accurate_at_a_fixed_point":finite_comparison,
    "linear_error_need_not_increase_monotonically_with_distance":distance_counterexample,
}
(OUT/"calculations.json").write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"status":"all assertions passed", "output":str(OUT/"calculations.json"),
                  "source_sha256":out["source_sha256"],"planet_quirk":out["planet_quirk"]},indent=2))
