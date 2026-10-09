from pathlib import Path
from decimal import Decimal as D, getcontext
from fractions import Fraction as F
import json, re, hashlib

getcontext().prec = 70
h = D('1e-12')
f = lambda x: (-2*x).exp() / (1+x).sqrt()
g = lambda x: (2*x).exp() * (1-x).sqrt()
checks = {
    'method': 'Exact rational arithmetic, separately differentiated factor values and high-precision symmetric finite differences; not a symbolic proof engine.',
    'source_product': {
        'direct_value': str(f(D(0))),
        'derivative_from_product_rule': str(F(-2)-F(1,2)),
        'second_derivative_from_product_rule': str(F(4)+2*F(-2)*F(-1,2)+F(3,4)),
        'first_derivative_numeric': str((f(h)-f(-h))/(2*h)),
        'second_derivative_numeric': str((f(h)-2*f(D(0))+f(-h))/(h*h)),
        'square_coefficient': str(F(2)+F(1)+F(3,8)),
    },
    'source_limit_direct_chain_rule': '10*2*(1+0)^9 = 20',
    'a1': {'slope': str(F(1,4)), 'value': str(F(2)+F(1,4)*F(4,100)), 'squared_estimate': str(D('2.01')**2)},
    'a2': {'direct_second_derivative_half': str(F(-4,2)),
        'negative_probe': str(((1-2*h).ln()+2*h)/(h*h)),
        'positive_probe': str(((1+2*h).ln()-2*h)/(h*h))},
    'a4': {'direct_slope': str(F(2)-F(1,2)),
        'direct_second_derivative': str(F(4)+2*F(2)*F(-1,2)-F(1,4)),
        'square_coefficient': str(F(2)-F(1)-F(1,8)),
        'first_derivative_numeric': str((g(h)-g(-h))/(2*h)),
        'second_derivative_numeric': str((g(h)-2*g(D(0))+g(-h))/(h*h)),
        'limit_positive_probe': str((g(h)-1-D('1.5')*h)/(h*h)),
        'limit_negative_probe': str((g(-h)-1+D('1.5')*h)/(h*h))},
    'log_check': str(D('1.02').ln()),
}
z=D('0.1');cos=sum((-1)**n*z**(2*n)/D(__import__('math').factorial(2*n)) for n in range(15))
checks['cos_check'] = str(cos)
q=D('0.0001');gamma=1/(1-q).sqrt();lin=100*(1+q/2);quad=100*(1+q/2+3*q*q/8)
checks['a3']={'gamma':str(gamma),'linear_time':str(lin),'quad_time':str(quad),'linear_error':str(100*gamma-lin),'quadratic_error':str(100*gamma-quad),'reference_rounded_16':str(gamma.quantize(D('1e-16')))}
q=(D(4)/D(300000))**2
checks['source_relativity']={'q':str(q),'linear_fraction':str(q/2),'linear_day_seconds':str(86400*q/2),'quadratic_fraction':str(3*q*q/8),'quadratic_day_seconds':str(86400*3*q*q/8)}
src=Path('teaching.md').read_text(); labels=re.findall(r'^P(\d{3})\.',src,re.M)
anchors=re.findall(r'<a id="([^"]+)"></a>',src);links=re.findall(r'\]\(#([^)]*)\)',src)
checks['mechanical']={'sha256':hashlib.sha256(Path('teaching.md').read_bytes()).hexdigest(),'original_identical':Path('teaching.md').read_bytes()==Path('teaching-original.md').read_bytes(),'paragraph_labels_contiguous_unique':labels==[f'{i:03d}' for i in range(1,69)],'anchor_unique':len(anchors)==len(set(anchors)),'local_links':len(links),'unresolved_anchors':sorted(set(links)-set(anchors)),'inline_math_count':len(re.findall(r'\$`(.*?)`\$',src)),'display_math_count':src.count('$$')//2,'heading_lines':re.findall(r'^#{1,6}\s.*',src,re.M),'emphasis_tokens':bool('**' in src or '__' in src),'placeholder_lines':re.findall(r'^.*(?:TODO|TBD|FIXME).*$' ,src,re.M)}
Path('verification-results.json').write_text(json.dumps(checks,indent=2)+'\n')
print(json.dumps(checks,indent=2))
