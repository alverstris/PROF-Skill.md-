from pathlib import Path
import re,json,hashlib
import sympy as s
p=Path(__file__).parent;x=s.symbols('x',real=True)
checks=[]
def ck(name,condition):
 assert condition,name
 checks.append(name)
ck('parabola secant slope',s.Rational(9-1,3-1)==4)
ck('parabola vertical gap',s.expand((x-2)**2-1)==x*x-4*x+3)
ck('parallel tangent derivative at 2',s.diff(x*x,x).subs(x,2)==4)
ck('absolute-value secant',s.Rational(2-1,2-(-1))==s.Rational(1,3))
ck('tangent error polynomial',s.expand(x*x-(2*x-1))==s.expand((x-1)**2))
ck('P1 root squared slope',s.simplify(3*(2/s.sqrt(3))**2)==4)
ck('P3 exact arithmetic',s.Rational(14,10)**2-(2*s.Rational(14,10)-1)==s.Rational(16,100))
ck('P3 c substitution',1+2*s.Rational(12,10)*s.Rational(4,10)==s.Rational(196,100))
ck('P4 log derivative',s.diff(-s.log(x),x)==-1/x)
for n in range(1,9):
 P=sum(x**k/s.factorial(k) for k in range(n+1));Pm=sum(x**k/s.factorial(k) for k in range(n))
 ck(f'finite polynomial derivative n={n}',s.simplify(s.diff(P,x)-Pm)==0)
ck('cubic lower bound at 1',1+1+s.Rational(1,2)+s.Rational(1,6)==s.Rational(8,3))
ck('zero initial remainders',all((s.exp(x)-sum(x**k/s.factorial(k) for k in range(n+1))).subs(x,0)==0 for n in range(4)))
ck('P5 first remainder derivative',s.diff(s.exp(x)-1-x,x)==s.exp(x)-1)
ck('P5 second remainder derivative',s.diff(s.exp(x)-1-x-x*x/2,x)==s.exp(x)-1-x)
ck('strict-increase algebra positive factor',s.expand((x+s.symbols('a')/2)**2+3*s.symbols('a')**2/4)==x*x+s.symbols('a')*x+s.symbols('a')**2)
ck('sqrt bound exact value',s.Rational(3,4)<s.sqrt(4)-s.sqrt(1)<s.Rational(3,2))
ck('P6 F derivative and anchor',s.diff(2*x+3,x)==2 and (2*x+3).subs(x,0)==3)
doc=(p/'learner-v1.md').read_text();prompts=(p/'prompts-only-v1.md').read_text()
ids=re.findall(r'<a id="([^"]+)"></a>',doc);links=re.findall(r'\]\(#([^\)]+)\)',doc)
ck('unique anchors',len(ids)==len(set(ids)))
ck('all internal link targets exist',set(links)<=set(ids))
for i in range(1,7):
 q=prompts.split(f'Task P{i}\n\n',1)[1]
 if i<6:q=q.split(f'\n\nTask P{i+1}',1)[0]
 ck(f'P{i} exact frozen prompt retained',f'Task P{i}\n\n'+q.rstrip() in doc)
 ck(f'P{i} matched hint and solution',all(z+str(i) in ids for z in ['p','h','s']))
ck('all hints precede complete solutions',max(doc.index(f'<a id="h{i}"></a>') for i in range(1,7))<doc.index('<a id="solutions"></a>'))
imgs=re.findall(r'!\[[^\]]*\]\(([^)]+)\)',doc)
ck('all three figures exist',len(imgs)==3 and all((p/v).is_file() for v in imgs))
ck('no placeholders',not any(q in doc for q in ['{{','TODO','TBD','FIXME']))
ck('no Markdown emphasis or heading markup',not re.search(r'(?m)^#{1,6}\s|\*\*|__|(?<!\*)\*(?!\*)',doc))
ck('dollar delimiters balanced',doc.count('$')%2==0)
report={'artifact_sha256':hashlib.sha256((p/'learner-v1.md').read_bytes()).hexdigest(),'passed_checks':checks,'count':len(checks),'limits':'Algebra/navigation/source-format checks only. These do not prove semantic accessibility, general inequalities from numerical instances, live destination preservation, SASIS acceptance or human outcomes.'}
(p/'technical-check-results.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'count':len(checks),'artifact_sha256':report['artifact_sha256'],'result':'pass; limits apply'},indent=2))
