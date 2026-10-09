from pathlib import Path
from fractions import Fraction as Q
import sympy as s
import json,hashlib,re
A=Path(__file__).parent
n=s.symbols('n',integer=True,positive=True); x,t,b=s.symbols('x t b',real=True);i=s.symbols('i',integer=True)
checks=[]
def check(name,actual,expected):
 ok=s.simplify(actual-expected)==0
 checks.append({'id':name,'actual':str(actual),'expected':str(expected),'pass':bool(ok)});assert ok,name
sq=s.summation(i*i,(i,1,n));check('square-sum-normalized',sq/n**3,s.Rational(1,3)+1/(2*n)+1/(6*n**2))
check('outer-volume-gap',(n+1)**3/3-sq,(n+1)*(3*n+2)/6)
check('inner-volume-gap',sq-n**3/3,n*(3*n+1)/6)
check('square-area',s.limit(b**3*sq/n**3,n,s.oo),b**3/3)
check('pyramid-cross-sectional-check',s.integrate((n-x)**2,(x,0,n)),n**3/3)
check('line-area',s.limit(b*b*s.summation(i,(i,1,n))/n**2,n,s.oo),b*b/2)
check('square-LR-gap',b**3/n**3*(sq-s.summation(i*i,(i,0,n-1))),b**3/n)
check('P1-R',sum(Q(k,2)**2*Q(1,2) for k in range(1,5)),Q(15,4))
check('P1-L',sum(Q(k,2)**2*Q(1,2) for k in range(4)),Q(7,4))
check('P2-R',2/n*s.summation(2-2*i/n,(i,1,n)),2-2/n)
check('P2-L',2/n*s.summation(2-2*(i-1)/n,(i,1,n)),2+2/n)
check('worked-borrow',s.integrate(12000*(1+s.Rational(6,100)*(1-t)),(t,0,1)),12360)
check('P3-principal',s.integrate(6000*t,(t,0,1)),3000)
check('P3-debt',s.integrate(6000*t*(1+s.Rational(6,100)*(1-t)),(t,0,1)),3060)
check('P3-duration',s.integrate(6000*t*(1-t),(t,0,1))/3000,s.Rational(1,3))
check('P3-uniform',s.integrate(3000*(1+s.Rational(6,100)*(1-t)),(t,0,1)),3090)
check('P4-signed',s.integrate(3-2*x,(x,0,2)),2)
check('P4-positive',s.integrate(3-2*x,(x,0,s.Rational(3,2))),s.Rational(9,4))
check('P4-negative',s.integrate(3-2*x,(x,s.Rational(3,2),2)),-s.Rational(1,4))
check('P4-derivative',s.diff(s.integrate(3-2*x,(x,0,b)),b).subs(b,2),-1)
# Numerical containment distinguishes centre alignment and layer ordering.
for nn in range(1,11):
 for k in range(nn):
  for f in [Q(0),Q(1,4),Q(1,2),Q(3,4),Q(999,1000)]:
   z=k+f;assert nn-z<=nn-k<=nn+1-z
checks.append({'id':'pyramid-containment-samples','pass':True,'scope':'n=1..10, every slab, five distinct heights; general warrant in teaching C2'})
# Composite numerical sums check limiting debt independently of symbolic primitive.
for N in [100,1000,10000]:
 debt=sum(6000*((k+.5)/N)*(1+.06*(1-(k+.5)/N))/N for k in range(N))
 assert abs(debt-3060)<.01
checks.append({'id':'midpoint-debt-numerical','pass':True,'last_n':N,'last_value':debt})
files=['teaching.md','hints.md','solutions.md']; links=[]; issues=[]
for fn in files:
 txt=(A/fn).read_text(); prose=re.sub(r'```math\n.*?```','',txt,flags=re.S);prose=re.sub(r'\$`.*?`\$','',prose,flags=re.S)
 for line in prose.splitlines():
  if re.match(r'^\s{0,3}#{1,6}\s',line) or '**' in line or re.search(r'(?<!\w)[*_][^*_]+[*_](?!\w)',line) or re.match(r'^\s*\|',line): issues.append([fn,line])
 for dest in re.findall(r'(?<!!)\[[^\]]+\]\(([^)]+)\)',txt):
  path,sep,frag=dest.partition('#'); p=(A/path).resolve();ok=p.exists()
  if frag and ok:ok=f'<a name="{frag}"></a>' in p.read_text()
  links.append({'from':fn,'to':dest,'pass':ok}); assert ok,(fn,dest)
 for dest in re.findall(r'!\[[^\]]*\]\(([^)]+)\)',txt):assert (A/dest).is_file()
 assert txt.count('```')%2==0
 assert not re.search(r'\b(TODO|TBD|FIXME)\b',txt)
assert not issues,issues
for fn,prefix in [('teaching.md','p'),('hints.md','h'),('solutions.md','s')]:
 names=re.findall('<a name="([^"]+)"', (A/fn).read_text());assert names==[prefix+str(k) for k in range(1,5)]
result={'mathematical_checks':checks,'navigation_local_source':links,'typography_source_issues':issues,'task_hint_solution_ids':'P1..P4 exact matching','limits':'Symbolic/numerical/source syntax checks and inspected PNG figures do not establish actual GitHub parsed mathematics/style/navigation. Those external gates remain pending. Pyramid cross-section integration is an independent author check using baseline calculus, not the logical basis of the learner geometric argument.'}
(A/'author-checks.json').write_text(json.dumps(result,indent=2)+'\n');print(len(checks),'mathematical checks passed;',len(links),'local links passed; source typography clean')
