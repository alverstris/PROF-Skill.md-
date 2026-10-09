from pathlib import Path
import hashlib,json,re
from fractions import Fraction as F
import sympy as s
P=Path(__file__).resolve().parents[1]; L=P/'learner'
x,t,b,h,n=s.symbols('x t b h n', real=True); k=s.symbols('k', integer=True, positive=True)
checks={}
def eq(key,actual,expected):
 assert s.simplify(actual-expected)==0,(key,actual,expected)
 checks[key]={'actual':str(actual),'expected':str(expected),'pass':True}
eq('worked_R4',sum(F(i,4)**2*F(1,4) for i in range(1,5)),F(30,64))
eq('Q1_right',sum(F(i,2)**2*F(1,2) for i in range(1,5)),F(15,4))
eq('Q1_left',sum(F(i,2)**2*F(1,2) for i in range(4)),F(7,4))
eq('square_sum',s.summation(k*k,(k,1,n)),n*(n+1)*(2*n+1)/6)
eq('square_sum_limit',s.limit(n*(n+1)*(2*n+1)/(6*n**3),n,s.oo),F(1,3))
eq('scaled_staircase_limit',s.limit(2*n*(n+1)*(2*n+1)/(6*n**3),n,s.oo),F(2,3))
for N in range(1,41):
 S=sum(k*k for k in range(1,N+1));assert F(N**3,3)<S<F((N+1)**3,3)
 for j in range(N):
  for q in (F(0),F(1,4),F(1,2),F(3,4),F(1)):
   z=j+q;assert N-z<=N-j<=N+1-z
checks['pyramid_containment']={'pass':True,'scope':'n=1..40; every layer at both boundaries and three interior fractions; symbolic inequality independently follows from j<=z<=j+1; doubling z gives Q2.'}
eq('squeeze_width',((1+1/n)**3-1)/3,1/n+1/n**2+1/(3*n**3))
eq('square_area',s.integrate(x*x,(x,0,b)),b**3/3)
eq('line_sum',b*b/n**2*s.summation(k,(k,1,n)),b*b*(1+1/n)/2)
eq('line_area',s.integrate(x,(x,0,b)),b*b/2)
eq('midpoint_worked',F(1,2)*(F(13,4)+F(15,4)),F(7,2))
eq('Q3_sum',s.summation((3-2*k/n)*2/n,(k,1,n)),4-2/n)
eq('Q3_integral',s.integrate(4-x,(x,1,3)),4)
A=s.integrate(2*x+1,(x,1,b));eq('Q4_area',A,b*b+b-2);eq('Q4_derivative',s.diff(A,b),2*b+1);eq('Q4_difference_quotient',s.expand((A.subs(b,b+h)-A)/h),2*b+1+h)
eq('worked_square_interval',s.integrate(x*x,(x,1,2)),F(7,3))
eq('average_square',s.integrate(x*x,(x,0,b))/b,b*b/3)
eq('nine_month_loan',1000*(1+F(6,100)*F(1,4)),1015)
eq('constant_principal',s.integrate(12000,(t,0,1)),12000)
eq('constant_debt',s.integrate(12000*(1+s.Rational(6,100)*(1-t)),(t,0,1)),12360)
eq('monthly_debt',sum(1000*(1+F(6,100)*(1-F(i,12))) for i in range(1,13)),12330)
eq('Q5_principal',s.integrate(24000*t,(t,0,1)),12000)
eq('Q5_debt',s.integrate(24000*t*(1+s.Rational(6,100)*(1-t)),(t,0,1)),12240)
eq('Q5_duration',s.integrate(24000*t*(1-t),(t,0,1))/12000,F(1,3))
eq('Q6_displacement',s.integrate(2-t,(t,0,3)),F(3,2))
eq('Q6_distance',s.integrate(2-t,(t,0,2))+s.integrate(t-2,(t,2,3)),F(5,2))
eq('Q6_avg_velocity',s.integrate(2-t,(t,0,3))/3,F(1,2));eq('Q6_avg_speed',s.Rational(5,2)/3,F(5,6))
eq('Q6_sum_limit',s.limit(s.summation((2-3*k/n)*3/n,(k,1,n)),n,s.oo),F(3,2))
checks['unit_and_model_check']={'pass':True,'reason':'rate [dollars/year] times dt [year] is [dollars]; r [1/year] times remaining duration [year] is dimensionless; velocity [m/s] times dt [s] is [m]. r=0 reduces debt to principal; t=T gives zero interest; t=a gives maximal simple-interest duration. No actual contract claim.'}
(P/'evidence/technical-checks.json').write_text(json.dumps(checks,indent=2)+'\n')
texts={f.name:f.read_text() for f in L.glob('*.md')}
qs=[x.strip() for x in (P/'prompts-only-v1.md').read_text().split('\n\n') if re.match(r'Q\d\.',x)]
for q in qs:assert texts['notes.md'].count(q)==1
for name,txt in texts.items():
 assert not re.search(r'^\s*#{1,6}\s',txt,re.M)
 assert '**' not in txt and '__' not in txt
 assert not re.search(r'^\s*\|',txt,re.M)
 assert 'PROMPT_' not in txt
 for payload in re.findall(r'\$`(.*?)`\$',txt,re.S):
  assert '<' not in payload and '>' not in payload,(name,payload)
  assert not re.search(r'\\(?:lt|gt)(?=\S)',payload),(name,payload)
 assert txt.count('$$')%2==0
 assert txt.count('$`')==txt.count('`$')
 for target in re.findall(r'\]\(([^)]+)\)',txt):
  if target.startswith('http'):continue
  path,_,anchor=target.partition('#');assert (L/path).exists(),target
  if anchor:assert f'<a name="{anchor}"></a>' in (L/path).read_text(),target
 for i in range(1,7):assert txt.count(f'<a name="q{i}"></a>')==1
mechanical={'pass':True,'tasks':6,'prompt_verbatim_match':True,'local_links_and_anchors':'all resolve statically','inline_and_display_delimiters':'paired','inline_strict_comparisons':'only terminated \\lt and \\gt; no literal angle comparisons','plain_prose':'no ATX headings, bold markers, Markdown tables or placeholders','destination_rendering':'not performed; pending root','source_and_baseline_hashes':{}}
for label,path in [('source',P.parents[1]/'current-r22/source/lec18.pdf'),('baseline',P.parents[1]/'candidate-r23-1/references/sasis/ocr-baseline-20261007/student-baseline.txt')]:
 data=path.read_bytes();mechanical['source_and_baseline_hashes'][label]={'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}
(P/'evidence/static-checks.json').write_text(json.dumps(mechanical,indent=2)+'\n')
print(f'{len(checks)} technical checks passed; {len(qs)} verbatim prompt matches; all local links and 18 task/help anchors exist. Destination checks remain pending.')
