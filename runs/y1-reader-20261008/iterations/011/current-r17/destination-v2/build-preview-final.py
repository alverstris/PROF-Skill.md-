from pathlib import Path
import re,json,subprocess,shutil,hashlib,fitz
b=Path(__file__).resolve().parent;o=b/'preview-final';o.mkdir();r=b.parents[5];s=(b.parent/'author/teaching-v2.md').read_text();expected=json.loads((b/'source-math.json').read_text())
shutil.copy(r/'assets/latex/prof.sty',o/'prof.sty');shutil.copy(r/'assets/latex/main.tex',o/'template-original.tex');shutil.copytree(b.parent/'author/figures',o/'figures')
converted=re.sub(r'\$`(.*?)`\$',lambda m:'$'+m[1]+'$',s,flags=re.S);converted=re.sub(r'^```math\n(.*?)\n```',lambda m:'$$\n'+m[1]+'\n$$',converted,flags=re.M|re.S);(o/'preview.md').write_text(converted)
def run(cmd,name):
 p=subprocess.run(cmd,cwd=o,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True);(o/name).write_text(p.stdout);assert p.returncode==0,(cmd,p.stdout[-3000:]);return p.stdout
ast=json.loads(run(['pandoc','preview.md','-f','markdown-smart-fancy_lists-implicit_figures','-t','json'],'preview-ast-initial.json'))
def nodes(x,t):
 if isinstance(x,dict):
  if x.get('t')==t:yield x
  for v in x.values():yield from nodes(v,t)
 elif isinstance(x,list):
  for v in x:yield from nodes(v,t)
ms=list(nodes(ast,'Math'));assert len(ms)==len(expected)
for n,e in zip(ms,expected):
 assert n['c'][1].strip()==e['payload'].strip();n['c'][1]=e['payload']
# Preserve named Markdown anchors as native Pandoc spans, so generated links are actual PDF destinations.
for n in nodes(ast,'RawInline'):
 if n['c'][0]=='html':
  if n['c'][1]=='</a>':n.update(t='Str',c='');continue
  m=re.fullmatch(r'<a id="([^"]+)">',n['c'][1]);assert m
  ident=m[1];n.update(t='Span',c=[[ident,[],[]],[]])
# A PDF-only section break keeps all hints apart from all complete solutions.
for i,block in enumerate(ast['blocks']):
 if any(n['c'][0][0]=='solutions' for n in nodes(block,'Span')):
  ast['blocks'].insert(i,{'t':'RawBlock','c':['latex',r'\clearpage']});break
(o/'preview-ast.json').write_text(json.dumps(ast));tex=run(['pandoc','preview-ast.json','-f','json','-t','latex'],'body.tex')
# Constrain source PNG dimensions without changing bytes; no caption emphasis or math changes.
tex=tex.replace('\\includegraphics{','\\includegraphics[width=0.85\\linewidth]{')
head='\\documentclass[11pt,a4paper]{article}\n\\usepackage{prof}\n\\ProfHeader{Related rates — internal review}\n\\providecommand{\\gt}{>}\n\\providecommand{\\lt}{<}\n\\providecommand{\\tightlist}{}\n\\begin{document}\n'
(o/'main.tex').write_text(head+tex+'\n\\end{document}\n')
for i in [1,2]:run(['pdflatex','-interaction=nonstopmode','-halt-on-error','main.tex'],f'pass-{i}.txt');shutil.copy(o/'main.log',o/f'pass-{i}.log')
d=fitz.open(o/'main.pdf');pages=[]
for i,p in enumerate(d,1):
 name=f'page-{i:02}.png';p.get_pixmap(matrix=fitz.Matrix(1.5,1.5)).save(o/name);pages.append({'page':i,'image':name,'text':p.get_text(),'links':p.get_links(),'visual_review':'PENDING'})
(o/'pages.json').write_text(json.dumps(pages,indent=2,default=str));record={'page_count':len(d),'source_sha256':hashlib.sha256(s.encode()).hexdigest(),'pdf_sha256':hashlib.sha256((o/'main.pdf').read_bytes()).hexdigest(),'math_count':len(ms),'payloads_exact':all(n['c'][1]==e['payload'] for n,e in zip(ms,expected)),'diagnostics':re.findall(r'^.*(?:Overfull|Underfull|Warning|undefined|Missing).*$',(o/'main.log').read_text(),re.M),'role':'Internal source-faithful PDF review derivative, not GitHub pixels or user deliverable. Adapter changes delimiters, maps anchors, constrains figure width, begins complete solutions on separate page.'};(o/'preview-check.json').write_text(json.dumps(record,indent=2));print(json.dumps(record,indent=2))
