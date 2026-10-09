"""Independent D010 source calculations; not blind to the source's printed answers."""
import sympy as s
r,V,x=s.symbols('r V x',positive=True)
rstar=(V/s.pi)**s.Rational(1,3)
S=s.pi*r*r+2*V/r
A=(x*x+(1-x)**2)/16
checks=[s.diff(S,r)-(2*s.pi*r-2*V/r**2),s.diff(S,r,2)-(2*s.pi+4*V/r**3),s.pi*rstar**3-V,V/(s.pi*rstar**2)-rstar,S.subs(r,rstar)-3*s.pi**s.Rational(1,3)*V**s.Rational(2,3),s.diff(A,x)-(2*x-1)/8,A-((x-s.Rational(1,2))**2/8+s.Rational(1,32)),s.diff(s.log(x)/x,x)-(1-s.log(x))/x**2,x/8-s.Rational(1,8)+x/8-s.diff(A,x)]
assert all(s.simplify(c)==0 for c in checks)
assert s.limit(S,r,0,dir='+')==s.oo and s.limit(S,r,s.oo)==s.oo
assert [A.subs(x,a) for a in [0,s.Rational(1,2),1]]==[s.Rational(1,16),s.Rational(1,32),s.Rational(1,16)]
print('All nine identities, two domain limits and three wire values agree.')
