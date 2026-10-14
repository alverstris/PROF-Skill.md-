from pathlib import Path
from hashlib import sha256
from decimal import Decimal as D, getcontext, ROUND_HALF_UP
import re, json, sys
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')
root=Path(__file__).resolve().parent
teach=root.parent/'fresh-author'/'teaching'
getcontext().prec=80
frozen={
 'main.md':(21509,'8c71112d8b623a4e24e977cc95b62e0491d0780c5833921ecf0715800eccb1b6'),
 'hints.md':(2690,'4d6ce039fbafff05a7b462aba2f5ab4eea663f91738f994d690531b8a70e73ee'),
 'solutions.md':(5424,'86d9e7312727219b62bd5895a413f4a5125777024da8d152b724d8474d8a3f5e'),
 'figures/log-tangent.png':(76096,'4a0190d0257a5e57caa3a7750be6e62d910b6f049d1c5c330d052ff97d669dc5'),
 'figures/trig-linear.png':(74379,'1813baec8e58aea9e3124a8d1940ce5d255dd729af3f4abfee1cafa5693b8bce'),
 'figures/cos-quadratic.png':(84960,'036806369aeede438b672d051127e9a8783f4ebf90c7000455203ffdf2f2ce0f')}
identities=[]; texts={}; inventory=[]; anchors={}; routes=[]; syntax=[]
for file,(count,digest) in frozen.items():
 data=(teach/file).read_bytes(); h=sha256(data).hexdigest()
 item={'file':file,'bytes':len(data),'sha256':h,'matches':len(data)==count and h==digest}
 if file.endswith('.png'):
  im=Image.open(teach/file); item['dimensions']=im.size; item['format']=im.format
 identities.append(item)
 if not file.endswith('.md'): continue
 text=data.decode('utf-8'); texts[file]=text
 anchors[file]=re.findall(r'<a id="([^"]+)"></a>',text)
 displays=list(re.finditer(r'^```math\n(.*?)^```\s*$',text,re.M|re.S))
 spans=[m.span() for m in displays]
 for m in displays:
  start=text[:m.start()].count('\n')+1; end=text[:m.end()].count('\n')+1
  inventory.append({'file':file,'line':start,'end_line':end,'kind':'display','payload':m.group(1).rstrip('\n')})
 for m in re.finditer(r'\$`([^`]+)`\$',text):
  if any(a<=m.start()<b for a,b in spans): raise RuntimeError('inline nested in display')
  inventory.append({'file':file,'line':text[:m.start()].count('\n')+1,'kind':'inline','payload':m.group(1)})
 for m in re.finditer(r'\[([^\]]*)\]\(([^)]+)\)',text):
  url=m.group(2)
  if url.startswith('http'): continue
  target,sep,frag=url.partition('#'); target=target or file
  routes.append({'source_file':file,'source_line':text[:m.start()].count('\n')+1,'label':m.group(1),'target_file':target,'fragment':frag})
 masked=text
 for m in sorted(displays,key=lambda x:x.start(),reverse=True):
  masked=masked[:m.start()]+' '*len(m.group())+masked[m.end():]
 masked=re.sub(r'\$`[^`]+`\$','',masked)
 if '$' in masked: syntax.append({'file':file,'problem':'unaccounted dollar','count':masked.count('$')})
 if re.search(r'^#{1,6}\s|^={3,}$|\*\*|(?<!\*)\*[^\n*]+\*',masked,re.M): syntax.append({'file':file,'problem':'possible prose heading/emphasis markup'})
for i,item in enumerate(sorted(inventory,key=lambda z:(list(texts).index(z['file']),z['line'],0 if z['kind']=='inline' else 1)),1):
 item['id']=f'M{i:03d}'
 p=item['payload']; violations=[]
 if '<' in p or '>' in p: violations.append('literal strict comparison glyph')
 if re.search(r'\\(?:lt|gt)(?! )',p): violations.append('strict comparison command without terminating literal space')
 if r'\operatorname' in p: violations.append('unverified named-function command')
 item['source_format_violations']=violations
 inventory[i-1]=item
for route in routes:
 route['target_exists']=route['target_file'] in anchors and route['fragment'] in anchors[route['target_file']]
all_anchors=[a for aa in anchors.values() for a in aa]
stats={'identities':identities,'math_counts':{file:{kind:sum(1 for x in inventory if x['file']==file and x['kind']==kind) for kind in ('inline','display')} for file in texts},'math_total':len(inventory),'math_source_format_violation_count':sum(len(x['source_format_violations']) for x in inventory),'syntax_concerns':syntax,'anchors':anchors,'global_anchor_unique':len(all_anchors)==len(set(all_anchors)),'route_count':len(routes),'broken_routes':[r for r in routes if not r['target_exists']],'render_limit':'This is the complete source inventory plus manual semantic checking; actual GitHub client-render preservation and click behaviour are root-owned checks.'}
(root/'math-payload-inventory.json').write_text(json.dumps(inventory,indent=2),encoding='utf-8')
(root/'source-routes.json').write_text(json.dumps(routes,indent=2),encoding='utf-8')
(root/'teaching-identity-and-source-checks.json').write_text(json.dumps(stats,indent=2),encoding='utf-8')

numeric=[]
def check(loc,claim,formula,inputs,value,quantum,expected,units='dimensionless'):
 rounded=value.quantize(D(quantum),rounding=ROUND_HALF_UP)
 numeric.append({'location':loc,'printed_claim':claim,'formula':formula,'inputs':inputs,'computed':str(value),'round_quantum':quantum,'rounded':str(rounded),'expected':expected,'pass':rounded==D(expected),'units':units})
ln102=D('1.02').ln()
check('main59','ln(1.02)=0.0198026273','ln(x)',{'x':'1.02'},ln102,'0.0000000001','0.0198026273')
check('main59;solutions20','absolute error0.0001973727','abs(ln(1.02)-.02)',{'x':'1.02','linear':'.02'},abs(ln102-D('.02')),'0.0000000001','0.0001973727')
check('main250','quadratic value.0198','h-h²/2',{'h':'.02'},D('.02')-D('.02')**2/2,'.0001','.0198')
check('main250','quadratic error.0000026273','abs(ln(1.02)-.0198)',{'h':'.02'},abs(ln102-D('.0198')),'.0000000001','.0000026273')
q=(D(4)/D(300000))**2
check('main199','daily difference7.68e-6','T*q/2',{'v_km_s':'4','c_km_s':'300000','T_s':'86400'},D(86400)*q/2,'0.00000001','0.00000768','s')
check('main264','3q²/8=1.185185e-20','3q²/8',{'q':'(4/300000)^2'},3*q*q/8,'1e-26','1.185185e-20')
check('main264','correction1.2e-20','3q²/8',{'q':'(4/300000)^2'},3*q*q/8,'1e-21','1.2e-20')
check('main264','leading change8.9e-11','q/2',{'q':'(4/300000)^2'},q/2,'1e-12','8.9e-11')
x=D('.02'); fx=(-2*x).exp()/(1+x).sqrt(); L=1-D(5)*x/2; Q=L+D(27)*x*x/8
check('main300','f(.02)=.9513233025','exp(-2x)/sqrt(1+x)',{'x':'.02'},fx,'.0000000001','.9513233025')
check('main300','L=.95','1-5x/2',{'x':'.02'},L,'.01','.95')
check('main300','Q=.95135','1-5x/2+27x²/8',{'x':'.02'},Q,'.00001','.95135')
check('main300','linear error.0013233025','abs(f(.02)-L(.02))',{'x':'.02'},abs(fx-L),'.0000000001','.0013233025')
check('main300','quadratic error.0000266975','abs(f(.02)-Q(.02))',{'x':'.02'},abs(fx-Q),'.0000000001','.0000266975')
suppliedln2=D('.69314718056'); A1=suppliedln2+D('.5')*D('.04')
check('solutions16-17','A1=.713147','supplied ln2+.5*(2.04-2)',{'ln2':str(suppliedln2),'h':'.04'},A1,'.000001','.713147')
check('solutions20','true ln2.04=.7129498079','ln(2.04)',{'x':'2.04'},D('2.04').ln(),'.0000000001','.7129498079')
check('solutions20','A1 error.0001973727','abs(supplied-ln2 tangent-ln(2.04))',{'estimate':str(A1),'x':'2.04'},abs(A1-D('2.04').ln()),'.0000000001','.0001973727')
q3=D('.6')**2; L3=1+q3/2; Q3=L3+3*q3*q3/8; exact3=1/(1-q3).sqrt()
for label,val,quant,expected in [('q',q3,'.01','.36'),('exact',exact3,'.01','1.25'),('linear',L3,'.01','1.18'),('quadratic correction',3*q3*q3/8,'.0001','.0486'),('quadratic',Q3,'.0001','1.2286'),('linear error',abs(exact3-L3),'.01','.07'),('quadratic error',abs(exact3-Q3),'.0001','.0214')]:
 check('main270;solutions50-65',label,'q=.6²;L=1+q/2;Q=L+3q²/8;exact=(1-q)^(-1/2)',{'v/c':'.6'},val,quant,expected)
# Independent decimal cosine from its convergent alternating series.
t=D(1); cosx=t
for n in range(1,80):
 t *= -(D('.2')**2)/(D(2*n-1)*D(2*n)); cosx+=t
check('main314','cos(.2) reference.98006657784','decimal cosine alternating series',{'x_rad':'.2','terms':80},cosx,'.00000000001','.98006657784')
ref=D('.98006657784')
check('solutions107','linear cosine error.01993342216','abs(supplied reference-1)',{'reference':str(ref)},abs(ref-1),'.00000000001','.01993342216')
check('solutions109','quadratic cosine error.00006657784','abs(supplied reference-.98)',{'reference':str(ref)},abs(ref-D('.98')),'.00000000001','.00006657784')
check('solutions65','lecture q1.78e-10','(4/300000)^2',{'v_km_s':'4','c_km_s':'300000'},q,'1e-12','1.78e-10')
(root/'numeric-validation.json').write_text(json.dumps(numeric,indent=2),encoding='utf-8')
print(json.dumps(stats,indent=2))
print('Numerical checks:',len(numeric),'failures:',[n for n in numeric if not n['pass']])
print('Distinct math commands:',sorted(set(re.findall(r'\\([A-Za-z]+)', '\n'.join(x['payload'] for x in inventory)))))
