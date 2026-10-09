from pathlib import Path
import sympy as s
import json,re,hashlib
r,V,x=s.symbols('r V x',positive=True)
f=s.log(x)/x; A=(x*x+(1-x)**2)/16
checks={}
checks['log_derivative']=s.simplify(s.diff(f,x)-(1-s.log(x))/x**2)==0
checks['log_limits']=[str(s.limit(f,x,0,dir='+')),str(s.limit(f,x,s.oo))]
for n in (1,2):
 S=n*s.pi*r*r+2*V/r; opt=(V/(n*s.pi))**s.Rational(1,3);h=V/(s.pi*opt*opt);val=s.simplify(S.subs(r,opt))
 checks[f'can_{n}_bases']={'radius':str(opt),'height_radius_ratio':str(s.simplify(h/opt)),'area':str(val),'stationary':s.simplify(s.diff(S,r).subs(r,opt))==0,'second_derivative':str(s.diff(S,r,2)),'ends':[str(s.limit(S,r,0,dir='+')),str(s.limit(S,r,s.oo))]}
checks['wire_derivative']=str(s.factor(s.diff(A,x)))
checks['wire_completed_square']=s.simplify(A-(s.Rational(1,32)+(x-s.Rational(1,2))**2/8))==0
checks['wire_values']={str(q):str(A.subs(x,q)) for q in [0,s.Rational(1,4),s.Rational(1,2),s.Rational(3,4),1]}
checks['q1_endpoint_values']=[str(f.subs(x,1)),str(s.simplify(f.subs(x,s.sqrt(s.E))))]
# Discriminating direct dimensions: V=8pi gives r=h=2 and S=12pi, rejecting source pi^(-1/3).
checks['open_can_V8pi']={'r':2,'h':2,'volume':str(s.pi*2**2*2),'direct_area':str(s.pi*2**2+2*s.pi*2*2),'formula_area':str(s.simplify(3*s.pi**s.Rational(1,3)*(8*s.pi)**s.Rational(2,3)))}
p=Path(__file__).parent; txt=(p/'teaching-v1.md').read_text();clean=re.sub(r'```math\n.*?```','',txt,flags=re.S);clean=re.sub(r'\$`.*?`\$','',clean)
checks['static']={'paragraph_labels':re.findall(r'^P\d{3}\.',txt,re.M),'anchors':re.findall(r'<a id="([^"]+)"',txt),'fragment_links':re.findall(r'\]\(#([^)]*)\)',txt),'remaining_dollars':clean.count('$'),'prose_headings':re.findall(r'^#{1,6}\s.*',clean,re.M),'emphasis_markers':re.findall(r'\*\*|\*|_',clean),'image_paths':[a for a in re.findall(r'!\[[^]]*\]\(([^)]+)\)',txt)]}
checks['static']['links_match']=set(checks['static']['fragment_links'])<=set(checks['static']['anchors'])
checks['static']['all_figures_exist']=all((p/a).is_file() for a in checks['static']['image_paths'])
checks['static']['labels_sequential']=checks['static']['paragraph_labels']==[f'P{i:03d}.' for i in range(1,50)]
(p/'technical-check-results.json').write_text(json.dumps(checks,indent=2)+'\n');print(json.dumps(checks,indent=2))
