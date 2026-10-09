from pathlib import Path
import sympy as s
import mpmath as m
import json,hashlib,re
A=Path(__file__).resolve().parent;x=s.symbols('x',real=True);m.mp.dps=60
cases={
'f':(3*x-x**3,3*(1-x**2),-6*x,[-2,-1,-.5,0,.5,1,2]),
'q':(1/x,-1/x**2,2/x**3,[-3,-1,-.2,.2,1,3]),
's':(x**3-3*x**2+3*x,3*(x-1)**2,6*(x-1),[-1,0,.5,1,1.5,3]),
'L':(s.log(x)/x,(1-s.log(x))/x**2,(2*s.log(x)-3)/x**3,[.1,.5,1,2,3,5,10]),
'r':(x**3-3*x+2,3*(x-1)*(x+1),6*x,[-3,-2,-1,0,1,2]),
'v':(x**4,4*x**3,12*x**2,[-2,-.5,0,.5,2]),
'w':(x**3,3*x**2,6*x,[-2,-.5,0,.5,2]),
'h':((x-1)/x**2,(2-x)/x**3,2*(x-3)/x**4,[-3,-1,-.2,.2,1,2,2.5,3,4,10])}
records=[]
for name,(f,d1,d2,points) in cases.items():
 assert s.simplify(s.diff(f,x)-d1)==0
 assert s.simplify(s.diff(f,x,2)-d2)==0
 fn=s.lambdify(x,f,'mpmath');ds=[s.lambdify(x,d,'mpmath') for d in (d1,d2)]
 for p in points:
  p=m.mpf(str(p))
  for order in [1,2]:
   observed=m.diff(fn,p,order);expected=ds[order-1](p)
   err=abs(observed-expected);passed=err<m.mpf('1e-45')*(1+abs(expected))
   assert passed
   records.append({'function':name,'x':str(p),'order':order,'numeric_derivative':str(observed),'formula_value':str(expected),'absolute_error':str(err),'pass':bool(passed)})
# Independently evaluate exact locations, tails and the rational absolute bound.
assert s.expand((x-1)**3+1)==cases['s'][0]
assert s.expand((x-1)**2*(x+2))==cases['r'][0]
assert s.simplify(s.Rational(1,4)-cases['h'][0]-(x-2)**2/(4*x**2))==0
limits=[]
for name,p,side,answer in [('f',s.oo,'-',-s.oo),('f',-s.oo,'+',s.oo),('q',0,'-',-s.oo),('q',0,'+',s.oo),('q',s.oo,'-',0),('q',-s.oo,'+',0),('s',-s.oo,'+',-s.oo),('s',s.oo,'-',s.oo),('L',0,'+',-s.oo),('L',s.oo,'-',0),('r',-s.oo,'+',-s.oo),('r',s.oo,'-',s.oo),('h',0,'-',-s.oo),('h',0,'+',-s.oo),('h',-s.oo,'+',0),('h',s.oo,'-',0)]:
 result=s.limit(cases[name][0],x,p,dir=side);assert result==answer
 limits.append({'function':name,'endpoint':str(p),'direction':side,'value':str(result)})
values=[]
for name,p,answer in [('f',-1,-2),('f',1,2),('f',-s.sqrt(3),0),('f',0,0),('f',s.sqrt(3),0),('s',0,0),('s',1,1),('L',1,0),('L',s.E,1/s.E),('L',s.exp(s.Rational(3,2)),s.Rational(3,2)/s.exp(s.Rational(3,2))),('r',-2,0),('r',-1,4),('r',0,2),('r',1,0),('h',1,0),('h',2,s.Rational(1,4)),('h',3,s.Rational(2,9))]:
 result=s.simplify(cases[name][0].subs(x,p));assert s.simplify(result-answer)==0
 values.append({'function':name,'x':str(p),'value':str(result)})
teaching=A/'teaching-r15-recovery-v2.md';t=teaching.read_text()
anchors=re.findall(r'<a name="([^"]+)"></a>',t);links=re.findall(r'\]\(#([^)]+)\)',t);images=re.findall(r'!\[[^\]]*\]\(([^)]+)\)',t)
assert all(z in anchors for z in links);assert len(anchors)==len(set(anchors));assert all((A/z).is_file() for z in images)
assert re.findall(r'^P(\d{3})\.',t,re.M)==[f'{i:03d}' for i in range(1,63)]
assert not re.search(r'^\s*#{1,6}\s|\*\*|^\|',t,re.M)
result={'revision':'r15-recovery-v2','kind':'new recovery-author technical checks; not historical checks or SASIS','teaching_sha256':hashlib.sha256(teaching.read_bytes()).hexdigest(),'symbolic_derivative_identities':16,'numeric_point_cases':sum(len(c[3]) for c in cases.values()),'numeric_derivative_comparisons':len(records),'numeric_method':'mpmath 60-digit numerical differentiation versus separately entered analytic derivative formulae; SymPy independently differentiates original functions','records':records,'limits':limits,'exact_points':values,'new_algebra_identities':3,'mechanical':{'paragraphs':62,'anchors':len(anchors),'links':len(links),'images':images,'local_images_exist':True,'source_typography_scan':'no ATX headings, bold markers or Markdown tables','destination_parser':'not inspected by this script'}}
(A/'new-technical-checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['records','limits','exact_points']},indent=2))
