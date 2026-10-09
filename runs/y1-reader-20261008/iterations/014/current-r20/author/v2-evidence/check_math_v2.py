from pathlib import Path
import sympy as s
import hashlib,json,re
root=Path(__file__).parent
x=s.symbols('x',real=True); n=s.symbols('n',real=True); p=s.symbols('p',positive=True)
checks=[]
def z(name,expr):
 r=s.simplify(s.trigsimp(expr));checks.append({'id':name,'residual':str(r),'pass':r==0})
# Differentiate whole expressions, independently from the prose factor sequences.
for name,F,f in [('sin',-s.cos(x),s.sin(x)),('power',p**(n+1)/(n+1),p**n),('log-positive',s.log(p),1/p),('log-negative',s.log(-x),1/x),('sec2',s.tan(x),1/s.cos(x)**2),('arcsin',s.asin(x),1/s.sqrt(1-x*x)),('arctan',s.atan(x),1/(1+x*x)),('source-substitution',(x**4+2)**6/24,x**3*(x**4+2)**5),('source-sqrt',s.sqrt(1+x*x),x/s.sqrt(1+x*x)),('source-exp',s.exp(6*x)/6,s.exp(6*x)),('source-gaussian',-s.exp(-x*x)/2,x*s.exp(-x*x)),('source-trig-A',s.sin(x)**2/2,s.sin(x)*s.cos(x)),('source-trig-B',-s.cos(x)**2/2,s.sin(x)*s.cos(x)),('source-loglog-upper',s.log(s.log(p)),1/(p*s.log(p))),('source-loglog-lower',s.log(-s.log(p)),1/(p*s.log(p))),('P4',(x**3+2)**6/18-s.Rational(32,9),x*x*(x**3+2)**5),('P5',-1/s.log(p)-1,1/(p*s.log(p)**2)),('P7b',s.sin(3*x)/3+2,s.cos(3*x))]:
 v=p if p in F.free_symbols else x;z(name,s.diff(F,v)-f)
z('P4-value',((x**3+2)**6/18-s.Rational(32,9)).subs(x,0))
z('P5-value',(-1/s.log(p)-1).subs(p,s.exp(-1)))
z('P6-same-function',s.sin(x)**2/2-s.Rational(1,2)+s.cos(x)**2/2)
z('P6-initial',(-s.cos(x)**2/2).subs(x,s.pi/2))
z('P7b-value',(s.sin(3*x)/3+2).subs(x,0)-2)
z('P1-delta',s.Rational(29,10)**2-9+s.Rational(59,100))
z('P2-linear',4-s.Rational(3,10)/48-s.Rational(399375,100000))
num=[]
for v,h in [(65,1),(s.Rational(641,10),s.Rational(1,10)),(s.Rational(637,10),-s.Rational(3,10))]:
 exact=s.real_root(v,3);approx=4+s.Rational(h)/48
 num.append({'input':str(v),'actual':float(exact),'linear':float(approx),'linear_minus_actual':float(approx-exact)})
checks.append({'id':'P4-wrong-pattern-discriminator','actual_derivative_at_zero':str(s.diff(-s.exp(-x*x)/2,x).subs(x,0)),'proposed_integrand_at_zero':'1','pass':s.diff(-s.exp(-x*x)/2,x).subs(x,0)==0})
report={'method':'SymPy whole-function differentiation and exact rational identities; domain conditions independently checked in author-audit.md, not inferred from symbolic simplification','checks':checks,'numerical_approximations':num,'all_pass':all(c['pass'] for c in checks)}
(root/'technical-checks.json').write_text(json.dumps(report,indent=2)+'\n')
text=(root/'../teaching-v2.md').read_text();blocks=re.findall(r'\$`(.*?)`\$|\$\$\n(.*?)\n\$\$',text,re.S);math=[a or b for a,b in blocks]
prose=re.sub(r'\$`.*?`\$|\$\$\n.*?\n\$\$','',text,flags=re.S)
result={'teaching_sha256':hashlib.sha256(text.encode()).hexdigest(),'bytes':len(text.encode()),'physical_lines':len(text.splitlines()),'math_expressions':len(math),'inline_math':len(re.findall(r'\$`',text)),'display_math':text.count('\n$$\n')//2,'math_brace_balance':[i for i,m in enumerate(math) if m.count('{')!=m.count('}')],'raw_angle_comparison_inside_math':[i for i,m in enumerate(math) if '<' in m or '>' in m],'heading_markup':bool(re.search(r'^\s{0,3}#{1,6}\s|^\s*(?:===+|---+)\s*$',prose,re.M)),'emphasis_markers':bool(re.search(r'\*|_',prose)),'tables':bool(re.search(r'^\|',prose,re.M)),'placeholders':bool(re.search(r'TODO|TBD|FIXME|PLACEHOLDER',text)),'task_ids':re.findall(r'^P(\d+)\.',text,re.M),'hint_ids':re.findall(r'^H(\d+)\.',text,re.M),'solution_ids':re.findall(r'^S(\d+)\.',text,re.M),'all_hints_before_solutions':re.search(r'^H7\.',text,re.M).start()<re.search(r'^S1\.',text,re.M).start(),'figures':[],'figure_reason':'No original figures. Differential/tangent relationship mapped algebraically in L1; no visual needed to carry an otherwise unavailable inference.','limits':'Source structure check only; actual destination parsed-content, typography and live visual inspection remain pending external gates.'}
# Source note URLs contain underscore inside Markdown link target: exclude URLs before typography test.
plain=re.sub(r'\]\([^)]*\)',']',prose);result['emphasis_markers']=bool(re.search(r'\*|_',plain))
(root/'structural-checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'math_all_pass':report['all_pass'],'check_count':len(checks),'structure':result},indent=2))
