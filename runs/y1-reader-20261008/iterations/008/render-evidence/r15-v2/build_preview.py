#!/usr/bin/env python3
from pathlib import Path
import subprocess,json,re,hashlib,sys,copy
import fitz
from PIL import Image
sys.dont_write_bytecode=True
root=Path(__file__).parent;out=root/'preview';out.mkdir()
sys.path.insert(0,str(root.parents[1]/'d008-render-review-prep'));import review_helpers as h
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def save(path,obj):
 with path.open('x') as f:json.dump(obj,f,ensure_ascii=False,indent=2);f.write('\n')
def run(args,log):
 p=subprocess.run(args,cwd=out,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
 with (out/log).open('x') as f:f.write(p.stdout)
 if p.returncode:raise RuntimeError(f'{args}: exit {p.returncode}; see {log}')
 return p.stdout
source=root/'teaching-r15-v2.md';original=source.read_text();tokens=json.loads((root/'source-math.json').read_text());expected=[{'type':x['type'],'payload':x['payload']} for x in tokens]
# Only protected inline delimiters need a Pandoc syntax bridge. Ordinary displays stay byte-exact.
converted=re.sub(r'\$`(.*?)`\$',lambda m:'$'+m[1]+'$',original,flags=re.S)
with (out/'preview.md').open('x') as f:f.write(converted)
standard=re.compile(r'\$\$(.*?)\$\$|(?<!\$)\$(?!\$)(.*?)(?<!\$)\$(?!\$)',re.S)
inverse=standard.sub(lambda m:m[0] if m[1] is not None else '$`'+m[2]+'`$',converted)
assert inverse.encode()==source.read_bytes()
with (out/'preview-header.tex').open('x') as f:f.write('\\providecommand{\\gt}{>}\n\\providecommand{\\lt}{<}\n')
initial_ast=json.loads(run(['pandoc','preview.md','-f','markdown-fancy_lists','-t','json'],'preview-initial-ast.json'))
def math_nodes(x):
 if isinstance(x,dict):
  if x.get('t')=='Math':yield x
  for v in x.values():yield from math_nodes(v)
 elif isinstance(x,list):
  for v in x:yield from math_nodes(v)
initial=list(math_nodes(initial_ast));assert len(initial)==len(expected)==305
boundary=[]
for i,(node,e) in enumerate(zip(initial,expected),1):
 typ='js-display-math' if node['c'][0]['t']=='DisplayMath' else 'js-inline-math';assert typ==e['type']
 if node['c'][1]!=e['payload']:
  assert typ=='js-display-math' and e['payload'].startswith('\n') and e['payload'].endswith('\n') and node['c'][1]==e['payload'][1:-1]
  boundary.append({'math_index':i,'source_payload':e['payload'],'initial_Pandoc_payload':node['c'][1],'difference':'Exactly the two newlines adjacent to ordinary $$ delimiters; no internal newline or mathematical character changes.'})
save(out/'pandoc-boundary-normalization.json',{'initial_AST_math_not_byte_exact':bool(boundary),'boundary_newline_normalization_count':len(boundary),'differences':boundary,'handling':'Explicitly restore exact original payload bytes in a separate final rendering AST; source and initial AST remain unchanged.'})
ast=copy.deepcopy(initial_ast)
for node,e in zip(math_nodes(ast),expected):node['c'][1]=e['payload']
save(out/'preview-ast.json',ast)
actual=[{'type':'js-display-math' if x['c'][0]['t']=='DisplayMath' else 'js-inline-math','payload':x['c'][1]} for x in math_nodes(ast)]
# Prove final AST differs only in the explicitly recorded display-boundary whitespace.
recovered=copy.deepcopy(ast)
for node,e in zip(math_nodes(recovered),initial):node['c'][1]=e['c'][1]
assert recovered==initial_ast
# Independent full prose/math stream comparison against AST text.
def stream(x):
 if isinstance(x,list):return ''.join(stream(v) for v in x)
 if not isinstance(x,dict):return ''
 t=x.get('t');c=x.get('c')
 if t=='Str':return c
 if t in ['Space','SoftBreak','LineBreak']:return ' '
 if t=='Math':
  d='$$' if c[0]['t']=='DisplayMath' else '$';return d+c[1]+d
 if t=='Link':return stream(c[1])
 if t in ['RawInline','RawBlock']:return ''
 if t in ['Para','Plain']:return stream(c)+'\n'
 return stream(c)
norm=lambda s:re.sub(r'\s+',' ',s).strip()
actual_stream=norm(stream(ast['blocks']));expected_stream=(root/'expected-prose-math-stream.txt').read_text().strip()
with (out/'AST-prose-math-stream.txt').open('x') as f:f.write(actual_stream+'\n')
checks={'source_sha256':sha(source),'source_byte_identity_with_immutable_GitHub_fetch':sha(source)=='b6e93b986e2a77763c556a4b5fc5cb42f43269742d0af9bd06021d7aa3ad7668','preview_input_sha256':sha(out/'preview.md'),'delimiter_only_adapter_inverse_byte_exact':inverse.encode()==source.read_bytes(),'source_math_count':len(expected),'math_AST_count':len(actual),'all_final_AST_math_payloads_exact_including_boundary_and_internal_newlines':expected==actual,'final_AST_other_structure_unchanged':recovered==initial_ast,'complete_AST_prose_math_stream_exact_after_whitespace_folding':actual_stream==expected_stream,'initial_Pandoc_boundary_normalization_count':len(boundary),'adapter':'Only protected inline dollar-backtick delimiters become ordinary dollars. Displays/prose/links/anchors/visible P labels unchanged. Pandoc initial AST removes boundary newlines for ordinary $$ displays; this is separately preserved and exact source payloads restored in final rendering AST. TeX conversion uses that final JSON AST.'}
save(out/'ast-math-check.json',checks)
assert checks['all_final_AST_math_payloads_exact_including_boundary_and_internal_newlines'] and checks['complete_AST_prose_math_stream_exact_after_whitespace_folding']
run(['pandoc','preview-ast.json','-f','json','-s','-V','fontsize=11pt','-V','geometry:margin=25mm','-H','preview-header.tex','-o','preview.tex'],'pandoc.txt')
compiler_capture=[]
for i in [1,2]:
 proc=subprocess.run(['pdflatex','-interaction=nonstopmode','-halt-on-error','-jobname=preview','preview.tex'],cwd=out,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
 stdout=out/f'pdflatex-pass{i}.txt'
 with stdout.open('xb') as f:f.write(proc.stdout)
 logfile=out/'preview.log';log_bytes=logfile.read_bytes() if logfile.exists() else b'';snapshot=out/f'compiler-pass{i}-tex-log.txt'
 with snapshot.open('xb') as f:f.write(log_bytes)
 capture={'pass':i,'exit_code':proc.returncode,'stdout_file':stdout.name,'stdout_sha256':sha(stdout),'tex_log_snapshot':snapshot.name,'tex_log_present':logfile.exists(),'tex_log_bytes':len(log_bytes),'tex_log_sha256':sha(snapshot)};compiler_capture.append(capture);save(out/f'compiler-pass{i}-capture.json',capture)
 if proc.returncode:raise RuntimeError(f'pdflatex pass {i} failed; stdout and immediate log snapshot preserved.')
save(out/'compiler-evidence-capture.json',compiler_capture)
run(['pdfinfo','preview.pdf'],'pdfinfo.txt');run(['pdffonts','preview.pdf'],'pdffonts.txt');run(['pdftotext','-layout','preview.pdf','preview-text.txt'],'pdftotext.txt')
images=[];before=sha(out/'preview.pdf')
with fitz.open(out/'preview.pdf') as doc:
 count=len(doc)
 for i,page in enumerate(doc,1):
  p=out/f'page-{i:02}.png';page.get_pixmap(matrix=fitz.Matrix(1.5,1.5),alpha=False).save(p)
  with Image.open(p) as im:im.verify()
  with Image.open(p) as im:im.load();images.append({'path':p.name,'size':list(im.size),'mode':im.mode,'sha256':sha(p),'fully_decoded':True})
log=(out/'pdflatex-pass2.txt').read_text()+'\n'+(out/'compiler-pass2-tex-log.txt').read_text();diagnostics=re.findall(r'^.*(?:overfull|underfull|warning|missing|undefined|^!).*$',log,re.M|re.I)
record={'AST':checks,'page_count':count,'PNG_count':len(images),'PNG_complete':len(images)==count,'images':images,'pdf_sha256':before,'PDF_unchanged_after_export':sha(out/'preview.pdf')==before,'log_diagnostics_case_insensitive':diagnostics,'compiler_evidence_capture':compiler_capture,'full_page_visual_review':'PENDING; see separately created visual-inspection.json after actual full-page opens.','role':'Read-only source-faithful internal review derivative, not a learner PDF; no GitHub pixels/CSS/hyperlink parity claim.','rasterizer':'PyMuPDF 1.5x full pages, individually decoded by PIL'}
save(out/'preview-check.json',record);print(json.dumps({'pages':count,'pdf_sha256':before,'AST':checks,'diagnostics':diagnostics},indent=2))
