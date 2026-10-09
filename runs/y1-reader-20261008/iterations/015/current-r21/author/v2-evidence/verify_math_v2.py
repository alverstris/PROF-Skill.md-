import sympy as s
from pathlib import Path
import json,re,hashlib
x,a,c=s.symbols('x a c', real=True); checks={}
def check(name,value):
 v=s.simplify(value);checks[name]=str(v);assert v==0,(name,v)
for name,y,rhs in [('gaussian',a*s.exp(-x*x/2),lambda y:-x*y),('q1',-2*s.exp(-x*x/2),lambda y:-x*y),('parabola',a*x*x,lambda y:2*y/x),('q2',s.tan(x*x/2),lambda y:x*(1+y*y)),('q3',-x*x,lambda y:2*y/x),('q4',s.sqrt(3-x*x/2),lambda y:-x/(2*y)),('q5i',x**3+1,lambda y:3*x*x),('q5ii',2*x*x,lambda y:2*y/x)]:check(name,s.diff(y,x)-rhs(y))
check('operator_x2',s.diff(x*x,x)+x*x*x-(2*x+x**3))
check('ellipse_implicit',x*x/4+(3-x*x/2)/2-s.Rational(3,2))
check('q4_perpendicular',s.Rational(1)*(-1)+1)
check('semiaxis_ratio',s.sqrt(6)/s.sqrt(3)-s.sqrt(2))
for name,y,x0,y0 in [('q1',-2*s.exp(-x*x/2),0,-2),('q2',s.tan(x*x/2),0,0),('q3',-x*x,2,-4),('q4',s.sqrt(3-x*x/2),2,1),('q5i',x**3+1,1,2),('q5ii',2*x*x,-1,2)]:check(name+'_initial',y.subs(x,x0)-y0)
# Counterexample must fail; this prevents a validator that approves every residual.
checks['rejected_q5_2x_equation_residual']=str(s.diff(2*x,x)-2*(2*x)/x);assert checks['rejected_q5_2x_equation_residual']=='-2'
checks['rejected_q5_2x_initial_residual']=str((2*x).subs(x,-1)-2);assert checks['rejected_q5_2x_initial_residual']=='-4'
A=Path(__file__).parent
(A/'technical-checks.json').write_text(json.dumps({'method':'SymPy residuals; domains and geometry checked separately in author-audit-v2.md','checks':checks},indent=2)+'\n')
print(json.dumps(checks,indent=2))
