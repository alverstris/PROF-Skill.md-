from pathlib import Path
import sympy as s,json
x,t,a,b=s.symbols('x t a b',real=True); rows=[]
def check(name,actual,expected):
 ok=s.simplify(actual-expected)==0;rows.append({'id':name,'actual':str(actual),'expected':str(expected),'pass':ok});assert ok,name
check('source-E1',s.integrate(x*x,(x,a,b)),(b**3-a**3)/3)
check('source-E2',s.integrate(s.sin(x),(x,0,s.pi)),2)
check('source-E3',s.integrate(x**5,(x,0,1)),s.Rational(1,6))
check('source-E4',s.integrate(s.sin(x),(x,0,2*s.pi)),0)
check('sine-negative-hump',s.integrate(s.sin(x),(x,s.pi,2*s.pi)),-2)
check('source-E5-lower',s.integrate(1,(x,0,1)),1)
check('source-E5-exp',s.integrate(s.exp(x),(x,0,1)),s.E-1)
check('source-E6-lower',s.integrate(1+x,(x,0,1)),s.Rational(3,2))
check('source-E7',s.integrate(s.expand((x**3+2)**4*x*x),(x,1,2)),s.Rational(10**5-3**5,15))
check('source-E7-derivative',s.diff((x**3+2)**5/15,x),(x**3+2)**4*x*x)
check('motion-worked-net',s.integrate(t-1,(t,0,2)),0)
check('motion-worked-distance',-s.integrate(t-1,(t,0,1))+s.integrate(t-1,(t,1,2)),1)
check('P1',s.integrate(x**5,(x,1,2)),s.Rational(21,2))
check('P2-net',s.integrate(2*t-2,(t,0,3)),3)
check('P2-distance',-s.integrate(2*t-2,(t,0,1))+s.integrate(2*t-2,(t,1,3)),5)
check('P2-reverse',s.integrate(2*t-2,(t,3,0)),-3)
check('P3-lower',s.integrate(1+t,(t,0,2)),4)
check('P3-exponential',s.integrate(s.exp(t),(t,0,2)),s.exp(2)-1)
check('P3-reverse-lower',s.integrate(1+t,(t,2,0)),-4)
check('P4-expand',s.integrate(s.expand(x*(2-x*x)**4),(x,0,1)),s.Rational(31,10))
check('P4-derivative',s.diff(-(2-x*x)**5/10,x),x*(2-x*x)**4)
check('P5-net-expanded',s.integrate(2*t**3-2*t,(t,0,s.sqrt(2))),0)
check('P5-first-leg',s.integrate(2*t**3-2*t,(t,0,1)),-s.Rational(1,2))
check('P5-second-leg',s.integrate(2*t**3-2*t,(t,1,s.sqrt(2))),s.Rational(1,2))
check('P5-distance',-s.integrate(2*t**3-2*t,(t,0,1))+s.integrate(2*t**3-2*t,(t,1,s.sqrt(2))),1)
for name,val in [('e-lower2',s.E-2),('e-lower2.5',s.E-s.Rational(5,2)),('e2-lower5',s.exp(2)-5)]:rows.append({'id':name,'positive_margin_approx':str(val.evalf()),'pass':float(val)>0})
report={'sympy_version':s.__version__,'scope':'Independent algebraic/numerical checks against stated outputs, not proof of teaching adequacy; root separately solved prompt-only packet before seeing proposed solutions.','results':rows}
Path(__file__).with_name('calculation-results.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
