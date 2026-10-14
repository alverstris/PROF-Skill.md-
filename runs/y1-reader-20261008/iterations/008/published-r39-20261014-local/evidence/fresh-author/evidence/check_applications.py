from decimal import Decimal, getcontext
from fractions import Fraction as F
from pathlib import Path
import json
getcontext().prec=80
root=Path(r"C:/Users/alver/.codex/.chatgpt-projects/g-p-6aa4088af61c8191a4b578a4310457ae/.prof-sasis/20261014-d008-r39/fresh-author")
D=Decimal
z=(D(4)/D(300000))**2
out={
"A":{"model":str(D(".96")-1),"exact_ln":str(D(".96").ln())},
"B":{"derivative_at_zero":"3*1 + 1*1 = 4","L":"1+4x","domain":"x<1/2"},
"C":{"f_second_derivative":str(F(25,4)+F(1,2)),"limit":str((F(25,4)+F(1,2))/2)},
"D":{"z":str(z),"z_half":str(z/2),"added":str(D(3)*z*z/8),"added_double_speed":str(D(3)*(4*z)**2/8),
"high_speed_z":str(D(".8")**2),"high_speed_exact":str(1/(1-D(".8")**2).sqrt()),
"high_speed_L":str(1+D(".64")/2),"high_speed_Q":str(1+D(".64")/2+D(3)*D(".64")**2/8)},
"E":{"L_2_1":str(D(3)+D(".4")*D(".1")),"Q_2_1":str(D(3)+D(".4")*D(".1")-D(".1")*D(".1")**2),
"cubic_counterexample_error":str(D(2)*D(".1")**3)},
"F":{"H_second_derivative_at0":str(-4+2*2*(-1)+0*2),"limit":"-4"},
"numeric_checks":{}
}
for xs in [".001",".000001","-.000001"]:
    x=D(xs)
    f=(-2*x).exp()/(1+x).sqrt()
    H=(1+2*x).ln()/(1+x)
    g=(3*x).exp()/(1-2*x).sqrt()
    out["numeric_checks"][xs]={"C":str((f-1+D("2.5")*x)/(x*x)),"F":str((H-2*x)/(x*x)),"B_difference_quotient":str((g-1)/x)}
assert out["C"]["limit"]=="27/8"
assert D(out["D"]["added"]) < D("1e-19") < D(out["D"]["added_double_speed"])
assert out["D"]["high_speed_Q"]=="1.4736"
assert out["E"]["Q_2_1"]=="3.039"
assert D(out["E"]["cubic_counterexample_error"])>D(".001")
(root/"evidence/generated-application-checks.json").write_text(json.dumps(out,indent=2),encoding="utf8")
print(json.dumps(out,indent=2))
