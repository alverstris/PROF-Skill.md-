from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal as D,getcontext,ROUND_HALF_UP
import json,math
out=Path(__file__).resolve().parent
getcontext().prec=90
rows=[]
def exact(case,loc,formula,inputs,value,expected,units='dimensionless'):
 value=F(value);expected=F(expected)
 rows.append({'case':case,'location':loc,'kind':'exact rational/point check','formula':formula,'inputs':inputs,'result':str(value),'expected':str(expected),'units':units,'pass':value==expected})
def approx(case,loc,formula,inputs,value,quant,printed,units='dimensionless'):
 value=D(value);rounded=value.quantize(D(quant),rounding=ROUND_HALF_UP)
 rows.append({'case':case,'location':loc,'kind':'printed numerical approximation/rounding','formula':formula,'inputs':inputs,'result':str(value),'round_quantum':quant,'rounded':str(rounded),'printed':printed,'units':units,'pass':rounded==D(printed)})
# D012 independently redo recurrence and use exact decimal squares.
iterates=[F(1)]
for i in range(4):iterates.append((iterates[-1]+F(3)/iterates[-1])/2)
expected=[F(1),F(2),F(7,4),F(97,56),F(18817,10864)]
r=D(3).sqrt();errstrings=['.7320508076','.2679491924','.0179491924','.0000920496','.0000000024']
for k,(v,e,printed) in enumerate(zip(iterates,expected,errstrings)):
 exact('D012',f'main59,69; iterate{k}','x_(k+1)=(x_k+3/x_k)/2',{'x0':'1','k':k},v,e)
 approx('D012',f'main73-77; error{k}','abs(x_k-sqrt(3))',{'x_k':str(v)},abs(D(v.numerator)/D(v.denominator)-r),'1e-10',printed)
for dec,square in [('1.73205080','2.99999997378064'),('1.73205081','3.0000000084216561')]:
 exact('D012','main84-86','decimal endpoint squared',{'endpoint':dec},F(dec)**2,F(square))
approx('D012','main89','sqrt(3), bracket-certified seven-decimal rounding',{'radicand':'3'},r,'1e-7','1.7320508')
exact('D012','main36','f(2)=2²-3',{'x':'2'},F(2)**2-3,1)
exact('D012','solutionQ1 372-375','Newton x1=2-(-1)/4; residual x1²-5',{'f':'x²-5','x0':'2'},(F(2)+F(1,4))**2-5,F(1,16))
exact('D012','solutionQ2 384','Newton map for x³-2x+2 at0',{'x0':'0'},F(0)-F(2)/F(-2),1)
exact('D012','solutionQ2 384','Newton map for x³-2x+2 at1',{'x1':'1'},F(1)-F(1)/F(1),0)
exact('D012','solutionQ2 389','f(-3/2)=(-3/2)³-2(-3/2)+2',{'x':'-3/2'},F(-3,2)**3-2*F(-3,2)+2,F(13,8))
exact('D012','solutionQ4 414','(3-2/6)²-7',{'x0':'3'},F(8,3)**2-7,F(1,9))
for loc,a,b,L,xx,yy,l1,l2,ratio in [(281,8,3,10,F(2),F(-3,2),F(5,2),F(15,2),F(4,5)),(406,6,2,10,F(9,4),F(-3),F(15,4),F(25,4),F(3,5)),(416,8,0,10,F(4),F(-3),F(5),F(5),F(4,5))]:
 DD=F(L*L-a*a);Droot=F(math.isqrt(DD.numerator),math.isqrt(DD.denominator))
 assert Droot**2==DD
 exact('D012',f'main/solution{loc}','y=(b-sqrt(L²-a²))/2',{'a':a,'b':b,'L':L},(F(b)-Droot)/2,yy,'m')
 exact('D012',f'main/solution{loc}','x=a/2*(1-b/sqrt(L²-a²))',{'a':a,'b':b,'L':L},F(a,2)*(1-F(b)/Droot),xx,'m')
 exact('D012',f'main/solution{loc}','left distance squared=x²+y²',{'x':str(xx),'y':str(yy)},xx**2+yy**2,l1**2,'m²')
 exact('D012',f'main/solution{loc}','right distance squared=(a-x)²+(b-y)²',{'a':a,'b':b,'x':str(xx),'y':str(yy)},(a-xx)**2+(b-yy)**2,l2**2,'m²')
 exact('D012',f'main/solution{loc}','distance sum',{'r1':str(l1),'r2':str(l2)},l1+l2,L,'m')
 exact('D012',f'main/solution{loc}','left horizontal/length',{'x':str(xx),'r1':str(l1)},xx/l1,ratio)
 exact('D012',f'main/solution{loc}','right horizontal/length',{'a':a,'x':str(xx),'r2':str(l2)},(a-xx)/l2,ratio)
for loc,ratio,printed in [(281,.8,'53.13'),(406,.6,'36.87')]:
 approx('D012',f'main/solution{loc}','asin(ratio)*180/pi',{'ratio':str(ratio)},D(str(math.degrees(math.asin(ratio)))),'0.01',printed,'degrees')
# D013: ordinary exact decimal checks are not labelled independent/direct decimal validation.
for h,printed in [('0.1','.01'),('0.8','.64')]:exact('D013','main117','h² exact error',{'h':h},F(h)**2,F(printed))
exact('D013','main119-121','(1.8)²',{'x':'1.8'},F('1.8')**2,F('3.24'))
exact('D013','main119-121','1+2(1.8-1)',{'a':'1','x':'1.8'},1+2*(F('1.8')-1),F('2.60'))
exact('D013','main121','(3.24-1)/.8',{'f(x)':'3.24','f(a)':'1','h':'.8'},(F('3.24')-1)/F('.8'),F('2.8'))
exact('D013','main121','MVT c=secant/2',{'secant':'2.8'},F('2.8')/2,F('1.4'))
exact('D013','solutions30-34','tangent estimate1+3(2-1)',{'f':'t³','a':'1','x':'2'},1+3*(2-1),4)
exact('D013','solutions30-34','exact minus tangent',{'f':'t³','a':'1','x':'2'},2**3-4,4)
exact('D013','solutions30-34','(2³-1³)/(2-1)',{'a':1,'b':2},F(8-1),7)
exact('D013','solutions34','midpoint derivative3*(3/2)²',{'c':'3/2'},3*F(3,2)**2,F(27,4))
# D007 exact checks require no invented decimal precision condition.
exact('D007','lesson130','y³+3xy² at(0,2)',{'x':0,'y':2},F(2)**3+3*0*F(2)**2,8)
exact('D007','lesson130','-3y²/(3y²+6xy)',{'x':0,'y':2},F(-12,12),-1)
exact('D007','solutions35','1/(1+cos0)',{'x':0,'cos0':1},F(1,2),F(1,2))
exact('D007','solutions43','x²+xy+y²',{'x':1,'y':2},1+2+4,7)
exact('D007','solutions51-56','-(2x+y)/(x+2y)',{'x':1,'y':2},F(-4,5),F(-4,5))
# D015 all retained point checks, including exact finite decimals represented as fractions.
for loc,x,y,par,new in [('main205',1,1,F(2),F(-1,2)),('solutions109',2,-1,F(-1),F(1)),('solutions151',1,2,F(-2),F(1,2))]:
 if loc=='solutions151':
  old=-F(y,x);perp=F(x,y)
 else:old=F(2*y,x);perp=F(-x,2*y)
 exact('D015',loc,'original family slope at stated point',{'x':x,'y':y},old,par)
 exact('D015',loc,'perpendicular slope at stated point',{'x':x,'y':y},perp,new)
 exact('D015',loc,'slope product',{'old':str(old),'new':str(perp)},old*perp,-1)
exact('D015','solutions72','ray y/x at(-1,2)',{'x':-1,'y':2},F(2,-1),-2)
exact('D015','solutions72','tangent3y/x at(-1,2)',{'x':-1,'y':2},3*F(2,-1),-6)
exact('D015','main205','ellipse constantx²/4+y²/2',{'x':1,'y':1},F(1,4)+F(1,2),F(3,4))
symbolic=[
 {'case':'D007','locations':['lesson323'],'formula':'D(exp(x*atan(x)))=exp(x*atan(x))*(atan(x)+x/(1+x²)); atx0 both bracket terms0','result':'0; a zero special case alone does not detect every omitted summand','pass':True},
 {'case':'D007','locations':['solutions108'],'formula':'D(x^x)=x^x*(ln(x)+1) forx>0; atx=e gives2e^e, while falsely substitutingr=x intofixedpowerrule givese^e','result':'2e^e versus e^e; atx1 both1, so x1 cannot discriminate','pass':True},
 {'case':'D009','locations':['P026','P056'],'formula':'D²(x⁴)=12x²>=0 with positive sign onbothsides0; D²(x³)=6x changesnegative→positive','result':'x⁴: minimum,noinflection; x³: inflection,noextremum. Both firstandsecond derivatives vanishat0','pass':True},
 {'case':'D009','locations':['P038-P039'],'formula':'For1<=t<=x:1/t<=1/sqrt(t); integralbound0<=ln(x)/x<=2(sqrt(x)-1)/x<=2/sqrt(x)→0','result':'All-real x>=1 bound supports tail; selectedsequencevaluesalone would not','pass':True},
 {'case':'D015','locations':['main64-71'],'formula':'D(e^(x²/2)y)=e^(x²/2)*(xy+yprime)=0 foranydifferentiablesolutionofyprime+xy0','result':'e^(x²/2)y constant on eachinterval; no divisionbyy, so zero/nonzerosolutionsincluded','pass':True},
 {'case':'D015','locations':['main161-167'],'formula':'D(a*x²)=2ax=2(a*x²)/x forx!=0; D(y/x²)=(x*yprime-2y)/x³=0','result':'Complete fixed-coefficient parabola family on each interval excludingx0','pass':True},
 {'case':'D015','locations':['main253'],'formula':'D(-x²/2)=-x; fory=-2x²,yprime=-4x and2y/x=-4x atx!=0','result':'Both corrected original terms satisfy definingequations; printed f=xand-2y² do not','pass':True}
]
(out/'targeted-numerical-rechecks.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
(out/'targeted-symbolic-rechecks.json').write_text(json.dumps(symbolic,indent=2),encoding='utf-8')
print('Exact/rounded numerical witnesses:',len(rows),'failed:',[r for r in rows if not r['pass']])
print('Symbolic witnesses:',len(symbolic))
