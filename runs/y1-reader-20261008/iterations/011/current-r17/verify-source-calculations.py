from pathlib import Path
import sympy as s,json
x,D,h,c,L,V,t=s.symbols('x D h c L V t',positive=True)
q=s.symbols('q',real=True)
checks={
'radar_sqrt_derivative':s.simplify(s.diff(s.sqrt(900+x*x),x)-x/s.sqrt(900+x*x))==0,
'radar_inverse_branch':s.simplify(s.diff(s.sqrt(D*D-900),D)-D/s.sqrt(D*D-900))==0,
'cone_volume':s.simplify(s.pi*(s.Rational(2,5)*h)**2*h/3-4*s.pi*h**3/75)==0,
'cone_height_rate':s.simplify(q/s.diff(4*s.pi*h**3/75,h)-25*q/(4*s.pi*h**2))==0,
'satellite_sensitivity':s.simplify(s.diff(s.sqrt(h*h-c*c),h)-h/s.sqrt(h*h-c*c))==0,
'satellite_curvature':s.simplify(s.diff(s.sqrt(h*h-c*c),h,2)+c*c/(h*h-c*c)**s.Rational(3,2))==0,
'changing_c_direct_chain':s.simplify(s.diff(s.sqrt((5+s.Rational(1,5)*t)**2-(3-s.Rational(1,10)*t)**2),t).subs(t,0)-s.Rational(13,40))==0,
'leaking_cone_rate':s.simplify((2-h/5)/s.diff(4*s.pi*h**3/75,h)-5*(10-h)/(4*s.pi*h**2))==0,
}
assert all(checks.values())
out={'method':'Independent symbolic identities and discriminating direct time-parametrization; no authored solutions read','checks':checks,'source_radar_rate':str(s.Rational(50,40)*-80),'exact_speed_limit_ft_s':str(s.Rational(65*5280,3600)),'source_cone_rate_ft_min':str((25*q/(4*s.pi*h*h)).subs({h:5,q:2})),'RR2_height_rate_ft_min':str((5*(10-h)/(4*s.pi*h*h)).subs(h,5)),'RR3_exact_delta_km':str((s.sqrt(s.Rational(501,100)**2-9)-4).evalf(30))}
b=Path('/workspace/scratch/6a5c7131498d/prof-r17/runs/y1-reader-20261008/iterations/011/current-r17')
(b/'root-source-calculations.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
