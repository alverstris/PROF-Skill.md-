from pathlib import Path
import sympy as s,json,hashlib,re
from decimal import Decimal,getcontext
p=Path(__file__).parent; x=s.symbols('x'); checks={}
def record(name,value):checks[name]=value
v=s.Integer(1);it=[v]
for k in range(4):v=s.factor((v+3/v)/2);it.append(v)
assert it==[1,2,s.Rational(7,4),s.Rational(97,56),s.Rational(18817,10864)]
record('sqrt3_iterates',[str(t) for t in it]);record('sqrt3_errors',[str(s.N(abs(t-s.sqrt(3)),16)) for t in it])
r=s.sqrt(3);assert s.simplify((x+3/x)/2-r-(x-r)**2/(2*x))==0
record('error_identity','symbolically equal; positive x denominator')
getcontext().prec=40;lo=Decimal('1.73205080')**2;hi=Decimal('1.73205081')**2;assert lo<3<hi;record('square_bracket',[str(lo),str(hi)])
h=-x**3+x;N=x-h/s.diff(h,x)
for cur in [-1/s.sqrt(5),1/s.sqrt(5)]:assert s.simplify(N.subs(x,cur)+cur)==0
record('cycle_h','both +/-1/sqrt(5) map exactly to opposite input; derivatives2/5')
f=x*x-5;n=s.factor((x-f/s.diff(f,x)).subs(x,2));assert n==s.Rational(9,4);assert f.subs(x,n)==s.Rational(1,16);record('Q1',[str(n),str(f.subs(x,n))])
f=x**3-2*x+2;N=x-f/s.diff(f,x);seq=[s.Integer(0)]
for k in range(3):seq.append(s.factor(N.subs(x,seq[-1])))
assert seq==[0,1,0,1];assert f.subs(x,-s.Rational(3,2))==s.Rational(13,8);record('Q2',{'iterates':list(map(str,seq)),'residuals':[str(f.subs(x,v)) for v in seq],'midpoint_value':'13/8','interval':['-2','-3/2']})
for label,a,b,L in [('worked',8,3,10),('Q3',6,2,10),('Q4',8,0,10),('negative_b_check',6,-2,10)]:
 D=s.sqrt(L*L-a*a);xx=s.factor(s.Rational(a,2)*(1-b/D));yy=(b-D)/2;r1=s.sqrt(xx**2+yy**2);r2=s.sqrt((a-xx)**2+(b-yy)**2)
 assert s.simplify(r1+r2-L)==0;assert s.simplify(xx/r1-(a-xx)/r2)==0;assert yy<0 and yy<b and 0<xx<a
 assert s.simplify(a*a+(b-2*yy)**2-L*L)==0
 record(label,{'D':str(D),'x':str(xx),'y':str(yy),'r1':str(r1),'r2':str(r2),'angle_deg':str(s.N(s.asin(s.Rational(a,L))*180/s.pi,12))})
f=x*x-7;v=s.factor((x-f/s.diff(f,x)).subs(x,3));assert v==s.Rational(8,3);record('Q4_newton',{'estimate':str(v),'residual':str(f.subs(x,v))})
a,b,L,D=s.symbols('a b L D',positive=True);xx=a*(D-b)/(2*D);yy=(b-D)/2
assert s.factor(xx**2+yy**2-(L*(D-b)/(2*D))**2).subs(L**2,a**2+D**2).simplify()==0
record('ring_length_identity','squared left distance equals [L(D-b)/(2D)]^2 when L^2=a^2+D^2; right via b -> -b; positive lengths licensed by D>|b|')
record('force_check','equal angles with sin>0 gives T1=T2; vertical T=mg/(2cos alpha)>0; consistent dimensions and signs')
record('reflection_check','n=u1+u2 perpendicular to tangent from differentiated distance sum; n dot u1=n dot u2=1+u1 dot u2; n nonzero if L>AB. Reflection of incoming u1 across tangent is u1-2(u1 dot n)n/(n dot n)=-u2 since n dot n=2(1+u1 dot u2).')
text=(p/'teaching-v1.md').read_text();anchors=re.findall(r'<a name="([^"]+)"></a>',text);refs=re.findall(r'\]\(#([^\)]+)\)',text);assert len(anchors)==len(set(anchors));assert set(refs)<=set(anchors)
assert re.findall(r'^P(\d{3})\.',text,re.M)==[f'{n:03}' for n in range(1,47)]
prose=re.sub(r'\$\$.*?\$\$', '',text,flags=re.S);prose=re.sub(r'\$`.*?`\$', '',prose,flags=re.S)
assert not re.search(r'^(#{1,6}\s|\|)',prose,re.M);assert '**' not in text and '<strong' not in text and '<em>' not in text
record('source_markup_checks',{'paragraphs':46,'anchors':len(anchors),'internal_links':len(refs),'inline_math':len(re.findall(r'\$`(.*?)`\$',text,re.S)),'display_math':len(re.findall(r'^\$\$$',text,re.M))//2,'images':re.findall(r'!\[[^\]]*\]\(([^)]+)\)',text),'destination_preservation':'pending; markup check is not destination evidence'})
record('scope','author technical checks, not independent root/SASIS or learning evidence')
(p/'technical-checks-v1.json').write_text(json.dumps(checks,indent=2))
print(json.dumps(checks,indent=2))
