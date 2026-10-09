from pathlib import Path
import sympy as s, json, datetime
x=s.symbols("x",real=True)
items=[("cubic",3*x-x**3,3-3*x**2,-6*x), ("reciprocal",1/x,-1/x**2,2/x**3), ("shifted_cubic",x**3-3*x**2+3*x,3*(x-1)**2,6*(x-1)), ("logarithmic",s.log(x)/x,(1-s.log(x))/x**2,(2*s.log(x)-3)/x**3), ("A",x**3-3*x+2,3*(x-1)*(x+1),6*x), ("B_even",x**4,4*x**3,12*x**2), ("B_odd",x**3,3*x**2,6*x), ("C",(x-1)/x**2,(2-x)/x**3,2*(x-3)/x**4)]
checks=[]
for name,f,d,dd in items:
 for order,expected in [(1,d),(2,dd)]:
  residual=s.simplify(s.diff(f,x,order)-expected)
  checks.append({"name":name,"order":order,"residual":str(residual),"pass":residual==0})
 for value in ([-3,-1,s.Rational(-1,2),s.Rational(1,2),1,2,3,5] if name!="logarithmic" else [s.Rational(1,2),1,2,3,5]):
  checks.append({"name":name,"input":str(value),"value":str(f.subs(x,value)),"derivative_sign":str(s.sign(d.subs(x,value))),"concavity_sign":str(s.sign(dd.subs(x,value)))})
limits=[]
for name,f,_,_ in items:
 for a,side in ([(0,"+"),(s.oo,"-")] if name=="logarithmic" else [(0,"+"),(0,"-"),(s.oo,"-"),(-s.oo,"+")]):
  limits.append({"name":name,"input":str(a),"side":side,"limit":str(s.limit(f,x,a,dir=side))})
identities=[("r factorization",(x**3-3*x+2)-(x-1)**2*(x+2)),("shifted cubic",(x**3-3*x**2+3*x)-((x-1)**3+1)),("C global maximum",s.Rational(1,4)-(x-1)/x**2-(x-2)**2/(4*x**2)),("log antiderivative",s.diff(2*s.sqrt(x),x)-1/s.sqrt(x))]
ident=[{"name":n,"residual":str(s.simplify(e)),"pass":s.simplify(e)==0} for n,e in identities]
out={"observed_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),"conditions":"Root fresh independent symbolic recomputation after reading authored text; NOT pre-solution blind. Historical independent-before-solutions record preserved separately.","checks":checks,"limits":limits,"identities":ident,"all_equalities_pass":all(c.get("pass",True) for c in checks+ident),"limits_on_log":"Only its real positive-input domain used."}
Path(__file__).with_suffix(".json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps({"all_equalities_pass":out["all_equalities_pass"],"limits":limits,"identities":ident},indent=2))
