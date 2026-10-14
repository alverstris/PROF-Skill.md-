from pathlib import Path
from decimal import Decimal, localcontext
import math,json,hashlib
ROOT=Path(__file__).resolve().parents[1]
texts={p.name:p.read_text(encoding='utf-8') for p in (ROOT/'teaching').glob('*.md')}
checks=[]
def witness(file, printed, result, formula, rounding, units='dimensionless'):
    # Printed representation is checked against independently formatted result.
    expected=format(result,rounding)
    numeric_printed=printed
    okay=printed==expected and printed in texts[file]
    line=next((i for i,l in enumerate(texts[file].splitlines(),1) if printed in l),None)
    checks.append(dict(file=file,line=line,printed=printed,result=str(result),formula=formula,
                       rounding=rounding,units=units,expected=expected,pass_check=okay))
ln102=math.log(1.02); f002=math.exp(-.04)/math.sqrt(1.02)
witness('main.md','0.0198026273',ln102,'ln(1.02)','.10f')
witness('main.md','0.0001973727',abs(.02-ln102),'abs(0.02-ln(1.02))','.10f')
witness('main.md','0.0198',.02-.02**2/2,'0.02-0.02^2/2','.4f')
witness('main.md','0.0000026273',abs(ln102-(.02-.02**2/2)),'abs(ln(1.02)-(0.02-0.02^2/2))','.10f')
witness('main.md','0.95',1-2.5*.02,'1-(5/2)(0.02)','.2f')
witness('main.md','0.95135',1-2.5*.02+(27/8)*.02**2,'1-(5/2)(0.02)+(27/8)(0.02)^2','.5f')
witness('main.md','0.9513233025',f002,'exp(-2*0.02)/sqrt(1+0.02)','.10f')
witness('main.md','0.0013233025',abs(f002-.95),'abs(f(0.02)-0.95)','.10f')
witness('main.md','0.0000266975',abs(f002-.95135),'abs(f(0.02)-0.95135)','.10f')
witness('main.md','0.98006657784',math.cos(.2),'cos(0.2), radians','.11f')
witness('solutions.md','0.7129498079',math.log(2.04),'ln(2.04)','.10f')
witness('solutions.md','0.71314718056',.69314718056+.5*.04,'supplied ln2 + (1/2)*0.04','.11f')
witness('solutions.md','0.713147',.69314718056+.5*.04,'same estimate, rounded six decimals','.6f')
witness('solutions.md','0.0001973727',abs(.69314718056+.02-math.log(2.04)),'abs(estimate-ln(2.04))','.10f')
with localcontext() as ctx:
    ctx.prec=65; D=Decimal
    q=(D(4)/D(300000))**2
    # Source math syntax in main is compared to independent scientific notation fields.
    for needle,result,digits,formula in [
        ('7.68\\times10^{-6}',D(86400)*q/2,'.2E','86400*(4/300000)^2/2 seconds'),
        ('1.185185\\times10^{-20}',3*q*q/8,'.6E','3*((4/300000)^2)^2/8'),
        ('1.2\\times10^{-20}',3*q*q/8,'.1E','same quadratic correction, two significant figures'),
        ('8.9\\times10^{-11}',q/2,'.1E','(4/300000)^2/2, two significant figures')]:
        expected=format(result,digits)
        mantissa,exponent=expected.split('E'); normalized=mantissa+'\\times10^{'+str(int(exponent))+'}'
        checks.append(dict(file='main.md',printed=needle,result=str(result),formula=formula,
                           rounding=digits,expected=normalized,pass_check=needle==normalized and needle in texts['main.md']))
    q=D('.6')**2; exact=1/(1-q).sqrt(); line=1+q/2; quad=line+3*q*q/8
    for printed,result,rounding,formula in [
        ('0.36',q,'.2f','0.6^2'),('1.18',line,'.2f','1+0.36/2'),
        ('0.0486',3*q*q/8,'.4f','3*0.36^2/8'),('1.2286',quad,'.4f','1+0.36/2+3*0.36^2/8'),
        ('0.07',abs(exact-line),'.2f','abs(1.25-1.18)'),('0.0214',abs(exact-quad),'.4f','abs(1.25-1.2286)')]:
        witness('solutions.md',printed,result,formula,rounding)
    supplied=D('.98006657784')
    witness('solutions.md','0.01993342216',abs(supplied-1),'abs(supplied0.98006657784-1)','.11f')
    witness('solutions.md','0.00006657784',abs(supplied-D('.98')),'abs(supplied0.98006657784-0.98)','.11f')
result={'revision':'D008-r40-fresh-author-1','checks':checks,'count':len(checks),
        'failed':[c for c in checks if not c['pass_check']],
        'note':'Each printed validation value was located in frozen source and compared to a fresh formula/input calculation with declared rounding. Fractions/derivative coefficients checked in author-audit and independent source audit. Nominal sample inputs do not supply experimental uncertainty.'}
(ROOT/'evidence'/'final-numerical-checks.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'count':len(checks),'failed':result['failed']},indent=2))
