"""D007 author corroboration, using only Python's standard library."""
import hashlib,json,math,pathlib,platform
W=pathlib.Path(__file__).resolve().parent
checks=[]
def check(name,f,df,points):
 for x in points:
  h=1e-6
  numerical=(f(x+h)-f(x-h))/(2*h)
  analytic=df(x)
  err=abs(numerical-analytic)
  tolerance=2e-7*max(1,abs(analytic))
  checks.append(dict(name=name,x=x,h=h,numerical=numerical,analytic=analytic,absolute_error=err,tolerance=tolerance,pass_check=err<tolerance))
check('sinh',math.sinh,math.cosh,[-1.3,0.0,0.7])
check('cosh',math.cosh,math.sinh,[-1.3,0.0,0.7])
check('Q1',lambda x:math.cosh(2*x)-math.sinh(2*x),lambda x:-2*math.exp(-2*x),[-0.7,0.0,0.8])
check('Q2-F',lambda x:(1+x*x)*math.sin(3*x),lambda x:2*x*math.sin(3*x)+3*(1+x*x)*math.cos(3*x),[-0.7,0.2,1.2])
check('Q2-G',lambda x:math.sin(3*x)/(1+x*x),lambda x:(3*(1+x*x)*math.cos(3*x)-2*x*math.sin(3*x))/(1+x*x)**2,[-0.7,0.2,1.2])
check('worked-R',lambda x:x/(1+x*x),lambda x:(1-x*x)/(1+x*x)**2,[-1.7,0,0.4])
check('Q3-upper',lambda x:math.sqrt(5-x*x),lambda x:-x/math.sqrt(5-x*x),[1])
check('Q3-lower',lambda x:-math.sqrt(5-x*x),lambda x:x/math.sqrt(5-x*x),[1])
check('Q4-arccos',math.acos,lambda x:-1/math.sqrt(1-x*x),[-0.7,0.2,0.6])
check('arcsin',math.asin,lambda x:1/math.sqrt(1-x*x),[-0.7,0.2,0.6])
check('arctan',math.atan,lambda x:1/(1+x*x),[-1.3,0.2,0.6])
check('Q5-cos',math.cos,lambda x:-math.sin(x),[-1.3,0.2,0.6])
check('sin',math.sin,math.cos,[-1.3,0.2,0.6])
check('tan',math.tan,lambda x:1/math.cos(x)**2,[-0.7,0.2,0.6])
check('sec',lambda x:1/math.cos(x),lambda x:math.tan(x)/math.cos(x),[-0.7,0.2,0.6])
check('exp',math.exp,math.exp,[-1.3,0.2,0.6])
check('log',math.log,lambda x:1/x,[0.4,1,2.3])
check('Q6-f',lambda x:x**math.sqrt(2),lambda x:math.sqrt(2)*x**(math.sqrt(2)-1),[0.4,1,2.3])
check('Q6-g',lambda x:math.sqrt(2)**x,lambda x:math.sqrt(2)**x*math.log(math.sqrt(2)),[0.4,1,2.3])
check('power-pi',lambda x:x**math.pi,lambda x:math.pi*x**(math.pi-1),[0.4,1,2.3])
for r in [-2,0,2/3]:check('power-'+str(r),lambda x,r=r:x**r,lambda x,r=r:r*x**(r-1),[0.4,1,2.3])
check('source-final-E',lambda x:math.exp(x*math.atan(x)),lambda x:math.exp(x*math.atan(x))*(math.atan(x)+x/(1+x*x)),[-0.7,0.2,1.2])
check('Q7-J',lambda x:math.exp(x*math.atan(x))/(1+x*x),lambda x:math.exp(x*math.atan(x))*((1+x*x)*math.atan(x)-x)/(1+x*x)**2,[-0.7,0.2,1.2])
identities=[]
for x in [-1.3,0,0.7]:
 value=math.cosh(x)**2-math.sinh(x)**2
 identities.append({'x':x,'cosh_squared_minus_sinh_squared':value,'pass_check':abs(value-1)<1e-12})
result={'runtime':platform.python_version(),'library':'standard-library math; no SymPy used or claimed','teaching_sha256':hashlib.sha256((W/'teaching.md').read_bytes()).hexdigest(),'method':'Central finite differences at non-symmetric interior inputs corroborate analytic derivations; do not prove them or check domain endpoints. Domains and zeros checked by exact reasoning in math-review.md.','derivative_checks':checks,'identity_checks':identities,'all_checks_pass':all(c['pass_check'] for c in checks+identities)}
(W/'math-numerical-checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'checks':len(checks),'identity_checks':len(identities),'all_checks_pass':result['all_checks_pass'],'max_abs_error':max(c['absolute_error'] for c in checks)},indent=2))
