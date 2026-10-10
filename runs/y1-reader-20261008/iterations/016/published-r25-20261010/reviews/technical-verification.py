from fractions import Fraction as Q
from pathlib import Path
import json

root = Path('/workspace/scratch/f9c0b7fc7e76/d016-published-r25')
out = {}
# Direct finite sums, independently of a quoted closed formula.
rows = []
for n in (1,2,4,17):
    S = sum(k*k for k in range(1,n+1))
    R = Q(8,n**3)*S
    L = Q(8,n**3)*sum(k*k for k in range(n))
    assert Q(n**3,3) <= S <= Q((n+1)**3,3)
    assert L <= Q(8,3) <= R
    assert R-L == Q(8,n)
    rows.append(dict(n=n,S=S,L=str(L),R=str(R),gap=str(R-L)))
out['source_sum_and_P1'] = rows
assert rows[2]['L']=='7/4' and rows[2]['R']=='15/4'
# Check all slab boundary/midpoint side comparisons for asymmetric sample n.
rows=[]
for n in (1,4,17):
    for thickness in (1,2):
        for j in range(n):
            for f in (Q(0),Q(1,7),Q(1,2),Q(6,7),Q(1)):
                z=thickness*(j+f)
                assert n-z/thickness <= n-j <= n+1-z/thickness
        V=thickness*sum(k*k for k in range(1,n+1))
        lower=Q(thickness*n**3,3)
        upper=Q(thickness*(n+1)**3,3)
        assert lower <= V <= upper
        rows.append(dict(n=n,thickness=thickness,lower=str(lower),volume=V,upper=str(upper)))
out['P2_containment_samples']=rows
rows=[]
for n in (1,2,7,19):
    dx=Q(2,n)
    R=sum((2*(1+i*dx)-3)*dx for i in range(1,n+1))
    assert R==2+Q(4,n)
    rows.append({'n':n,'Rn':str(R)})
out['P3_direct_sums']=rows
out['P3_areas']={'negative_triangle':str(Q(1,4)),'positive_triangle':str(Q(9,4)),'signed':2,'geometric':str(Q(5,2))}
# Polynomial integral helper, coefficients in ascending powers.
def integral(c,a,b):
    a,b=Q(a),Q(b)
    return sum(Q(x,k+1)*(b**(k+1)-a**(k+1)) for k,x in enumerate(c))
for b in (Q(1),Q(3,2),Q(3),Q(7)):
    assert integral([1,2],1,b)==b*b+b-2
out['P4']={'A1':0,'A3':10,'average':5,'derivative_coefficients':[1,2]}
# Interest by integrating cumulative principal outstanding, rather than the
# displayed remaining-time weighted integrand. Same declared simple-interest model.
principal=Q(24000)*Q(1,2)
I_early=Q(6,100)*(integral([0,24000],0,Q(1,2))+integral([12000],Q(1,2),1))
I_uniform=Q(6,100)*integral([0,12000],0,1)
assert principal==12000 and I_early==540 and I_uniform==360
out['P5_independent_accumulated_principal_check']={'principal':str(principal),'interest_early':str(I_early),'debt_early':str(principal+I_early),'interest_uniform':str(I_uniform),'debt_uniform':str(principal+I_uniform),'difference':str(I_early-I_uniform)}
B=integral([6000,6000],0,2)
I=Q(1,10)*integral([0,6000,3000],0,2)
D_weighted=integral([7200,6600,-600],0,2)
assert B==24000 and I==2000 and D_weighted==B+I==26000
out['P6_two_routes']={'principal':str(B),'average_rate':str(B/2),'interest_integral_of_accumulated_principal':str(I),'debt_weighted_integral':str(D_weighted),'all_principal_full_duration':str(B*Q(6,5)),'weighted_mean_time_left':str(I/(Q(1,10)*B))}
(root/'reviews/technical-calculations.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
