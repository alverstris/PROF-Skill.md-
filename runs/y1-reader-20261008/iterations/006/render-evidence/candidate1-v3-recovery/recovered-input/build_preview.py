#!/usr/bin/env python3
from pathlib import Path
import subprocess,json,re,hashlib,shutil
from PIL import Image
root=Path(__file__).parent;out=root/'preview';out.mkdir(exist_ok=True)
def run(args,log):
 p=subprocess.run(args,cwd=out,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
 (out/log).write_text(p.stdout)
 if p.returncode:raise RuntimeError(f'{args}: exit {p.returncode}; see {log}')
 return p.stdout
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
source=root/'teaching-v3.md';shutil.copyfile(source,out/'preview.md')
(out/'preview-header.tex').write_text('\\providecommand{\\gt}{>}\n\\providecommand{\\lt}{<}\n')
ast=json.loads(run(['pandoc','preview.md','-f','markdown','-t','json'],'preview-ast.json'))
math=[]
def walk(x):
 if isinstance(x,dict):
  if x.get('t')=='Math':math.append(x['c'])
  for v in x.values():walk(v)
 elif isinstance(x,list):
  for v in x:walk(v)
walk(ast)
expected=json.loads((root/'scoped-markup-navigation-audit.json').read_text())['source_math']
actual=[{'type':'js-display-math' if x[0]['t']=='DisplayMath' else 'js-inline-math','payload':x[1]} for x in math]
exp=[{'type':x['type'],'payload':x['payload']} for x in expected]
checks={'preview_input_byte_identical':source.read_bytes()==(out/'preview.md').read_bytes(),'math_source_count':len(exp),'math_AST_count':len(actual),'all_math_payloads_exact_including_display_newlines':exp==actual,'source_sha256':sha(source),'all_math_mismatches':[{'index':i,'source':e,'ast':a} for i,(e,a) in enumerate(zip(exp,actual),1) if e!=a]}
(out/'ast-math-check.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2)+'\n')
assert checks['preview_input_byte_identical'] and checks['all_math_payloads_exact_including_display_newlines']
run(['pandoc','preview.md','-f','markdown','-s','-V','fontsize=11pt','-V','geometry:margin=25mm','-H','preview-header.tex','-o','preview.tex'],'pandoc.txt')
for i in [1,2]:run(['pdflatex','-interaction=nonstopmode','-halt-on-error','-jobname=preview','preview.tex'],f'pdflatex-pass{i}.txt')
run(['pdfinfo','preview.pdf'],'pdfinfo.txt');run(['pdffonts','preview.pdf'],'pdffonts.txt');run(['pdftotext','-layout','preview.pdf','preview-text.txt'],'pdftotext.txt')
before=sha(out/'preview.pdf')
run(['pdftoppm','-r','120','-png','preview.pdf','page'],'pdftoppm.txt')
images=[]
for p in sorted(out.glob('page-*.png')):
 with Image.open(p) as im: im.verify()
 with Image.open(p) as im: im.load();images.append({'path':p.name,'size':list(im.size),'mode':im.mode,'sha256':sha(p),'fully_decoded':True})
count=int(re.search(r'^Pages:\s+(\d+)',(out/'pdfinfo.txt').read_text(),re.M)[1])
(out/'preview-check.json').write_text(json.dumps({'AST':checks,'page_count':count,'PNG_count':len(images),'PNG_complete':len(images)==count,'images':images,'pdf_sha256':before,'PDF_unchanged_after_export':sha(out/'preview.pdf')==before,'log_diagnostics':re.findall(r'^.*(?:Overfull|Underfull|Warning|Missing|undefined|!).*$',(out/'preview.log').read_text(),re.M),'full_page_visual_review':'PENDING','role':'Internal secondary renderer only; not a learner PDF and not GitHub pixels or CSS.'},indent=2)+'\n')
print(json.dumps({'pages':count,'pdf_sha256':before,'AST':checks,'diagnostics':re.findall(r'^.*(?:Overfull|Underfull|Warning|Missing|undefined|!).*$',(out/'preview.log').read_text(),re.M)},ensure_ascii=False))
