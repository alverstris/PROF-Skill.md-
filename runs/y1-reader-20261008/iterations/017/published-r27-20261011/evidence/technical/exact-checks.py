from fractions import Fraction as F
from math import comb, exp
from pathlib import Path
import json

def integral(coeffs,a,b):
    return sum(F(c,k+1)*(F(b)**(k+1)-F(a)**(k+1)) for k,c in enumerate(coeffs))

def result(name,computed,expected):
    assert computed == expected,(name,computed,expected)
    return {'case':name,'computed':str(computed),'expected':str(expected),'pass':True}

checks=[]
checks.append(result('source x^5 on [0,1]',integral([0,0,0,0,0,1],0,1),F(1,6)))
checks.append(result('Q1 x^2 on [-1,2]',integral([0,0,1],-1,2),F(3)))
checks.append(result('worked velocity first piece',integral([-1,1],0,1),F(-1,2)))
checks.append(result('worked velocity second piece',integral([-1,1],1,2),F(1,2)))
checks.append(result('Q2 first piece',integral([-2,2],0,1),F(-1)))
checks.append(result('Q2 second piece',integral([-2,2],1,3),F(4)))
checks.append(result('orientation x^2 on [2,1]',integral([0,0,1],2,1),F(-7,3)))
checks.append(result('nonordered additivity',integral([0,0,1],0,2)+integral([0,0,1],2,1),integral([0,0,1],0,1)))
checks.append(result('source linear lower bound integral',integral([1,1],0,1),F(3,2)))
checks.append(result('Q4 linear lower bound integral',integral([1,1],0,2),F(4)))
# Expand source (x^3+2)^4 x^2 independently using the binomial theorem.
source7=[0]*15
for k in range(5): source7[3*k+2]=comb(4,k)*2**(4-k)
checks.append(result('source substitution versus direct expansion',integral(source7,1,2),F(10**5-3**5,15)))
checks.append(result('decreasing substitution direct expansion',integral([4,-4,1],0,1),F(7,3)))
# x(1+x^2)^3 = x+3x^3+3x^5+x^7.
checks.append(result('Q5 direct expansion',integral([0,1,0,3,0,3,0,1],0,1),F(15,8)))
checks.append(result('Q6 first piece',integral([0,-1,0,1],0,1),F(-1,4)))
checks.append(result('Q6 second piece',integral([0,-1,0,1],1,2),F(9,4)))
checks.append(result('Q6 total',integral([0,-1,0,1],0,2),F(2)))
checks.append(result('Q6 reversed',integral([0,-1,0,1],2,0),F(-2)))
checks.append(result('Q6 geometric area',-integral([0,-1,0,1],0,1)+integral([0,-1,0,1],1,2),F(5,2)))
checks.append({'case':'numerical sanity of exponential bounds (not a proof)','e_ge_2':exp(1)>=2,'e_ge_5_over_2':exp(1)>=2.5,'e_squared_ge_5':exp(2)>=5})
Path('evidence/technical/exact-checks.json').write_text(json.dumps(checks,indent=2))
print(f'{len(checks)-1} exact rational checks passed; exponential numerical sanity checks passed.')
