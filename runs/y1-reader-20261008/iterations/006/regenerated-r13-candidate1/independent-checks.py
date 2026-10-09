from pathlib import Path
from math import exp, log, log1p, expm1, e
import json

def centered(f,x,h=1e-6):
    return (f(x+h)-f(x-h))/(2*h)
checks=[]
def check(name,actual,expected,tol=1e-7):
    error=abs(actual-expected)/max(1,abs(expected))
    checks.append({'name':name,'actual':actual,'expected':expected,'scaled_error':error,'pass':error<tol})
for a in [0.5,1,2,4,10]:
    for x in [-0.7,0.4,1.3]:
        check(f'constant base a={a} x={x}',centered(lambda z:a**z,x),log(a)*a**x)
for x in [.3,1,4]:
    check(f'ln derivative at {x}',centered(log,x),1/x)
for x in [.2,1,2]:
    check(f'x^x at {x}',centered(lambda z:z**z,x),x**x*(log(x)+1))
for x in [-.7,.2,1.4]:
    check(f'A3 varying base and exponent at {x}',centered(lambda z:(1+z)**(z*z),x),(1+x)**(x*x)*(2*x*log1p(x)+x*x/(1+x)))
check('A1 point slope',centered(lambda z:exp(2*z-1),.5),2)
check('A2f at .4',centered(lambda z:.5**(3*z),.4),3*log(.5)*.5**1.2)
check('A2g at .4',centered(lambda z:log(5-2*z),.4),-2/(5-.8))
check('A3 point slope',centered(lambda z:(1+z)**(z*z),0),0)
check('A5 F prime0',centered(lambda t:300*exp(-.02*t),0),-6,1e-6)
check('A5 G prime0',centered(lambda t:10000*exp(-.02*t),0),-200,1e-6)
limits=[]
for k in [10,100,1000,1000000]:
    logb=k*log1p(1/k);logchanged=3*k*log1p(-2/k);logc=k*k*log1p(1/k)
    limits.append({'k':k,'source_log':logb,'source_value':exp(logb),'A4_log':logchanged,'A4_value':exp(logchanged),'A6_log':logc})
report={'method':'Standard-library centered finite differences and numerically stable log1p/expm1; diagnostic checks, not proofs. Independent analytic deductions are in math-review.md.','checks':checks,'all_numerical_checks_pass':all(c['pass'] for c in checks),'limits':limits,'secants':{'2':(2-1)/(1-0),'4':(1-.5)/(0-(-.5))},'M2':log(2),'M4':log(4),'k10':{'value':1.1**10,'relative_error_percent':100*((1.1**10)/e-1)},'finite_changes_percent':{'50_from300':100*(-50)/300,'50_from10000':100*(-50)/10000,'A5_one_day':100*expm1(-.02),'worked_one_day':100*expm1(.03)}}
Path('math-checks.json').write_text(json.dumps(report,indent=2)+'\n')
print('all_numerical_checks_pass',report['all_numerical_checks_pass'],'count',len(checks))
print(json.dumps({k:report[k] for k in ['limits','M2','M4','k10','finite_changes_percent']},indent=2))
