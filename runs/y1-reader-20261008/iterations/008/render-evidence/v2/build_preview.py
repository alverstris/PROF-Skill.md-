#!/usr/bin/env python3
from pathlib import Path
import subprocess,json,re,hashlib
import fitz
from PIL import Image
root=Path(__file__).parent;out=root/'preview';out.mkdir(exist_ok=True)
def run(args,log):
 p=subprocess.run(args,cwd=out,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
 (out/log).write_text(p.stdout)
 if p.returncode:raise RuntimeError(f'{args}: exit {p.returncode}; see {log}')
 return p.stdout
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
source=root/'teaching-v2.md';original=source.read_bytes().decode()
pat=re.compile(r'^```math\n(.*?)\n```|\$`(.*?)`\$',re.S|re.M)
expected=[]
def convert(m):
 payload=m[1] if m[1] is not None else m[2];typ='js-display-math' if m[1] is not None else 'js-inline-math';expected.append({'type':typ,'payload':payload})
 return '$$'+payload+'$$' if m[1] is not None else '$'+payload+'$'
converted=pat.sub(convert,original);(out/'preview.md').write_text(converted)
# Prove the adapter alters only complete delimiters and can reconstruct exact bytes.
standard=re.compile(r'\$\$(.*?)\$\$|(?<!\$)\$(?!\$)(.*?)(?<!\$)\$(?!\$)',re.S)
inverse=standard.sub(lambda m:'```math\n'+m[1]+'\n```' if m[1] is not None else '$`'+m[2]+'`$',converted)
assert inverse.encode()==source.read_bytes()
(out/'preview-header.tex').write_text('\\providecommand{\\gt}{>}\n\\providecommand{\\lt}{<}\n')
ast=json.loads(run(['pandoc','preview.md','-f','markdown-fancy_lists','-t','json'],'preview-ast.json'))
math=[]
def walk(x):
 if isinstance(x,dict):
  if x.get('t')=='Math':math.append(x['c'])
  for v in x.values():walk(v)
 elif isinstance(x,list):
  for v in x:walk(v)
walk(ast)
actual=[{'type':'js-display-math' if x[0]['t']=='DisplayMath' else 'js-inline-math','payload':x[1]} for x in math]
github_source=[{'type':x['type'],'payload':x['payload']} for x in json.loads((root/'source-math.json').read_text())]
checks={'source_sha256':sha(source),'source_byte_identity_with_immutable_GitHub_fetch':sha(source)=='7848e012a83c08cdeedf25c91d1800e646f30a3db77cac034bb9d07802f53b72','preview_input_sha256':sha(out/'preview.md'),'delimiter_only_adapter_inverse_byte_exact':inverse.encode()==source.read_bytes(),'source_math_count':len(expected),'math_AST_count':len(actual),'all_math_payloads_exact_including_internal_newlines':expected==actual,'all_expected_payloads_equal_actual_GitHub_audit_source':expected==github_source,'all_math_mismatches':[{'index':i,'source':e,'ast':a} for i,(e,a) in enumerate(zip(expected,actual),1) if e!=a],'adapter':'Protected inline and math fences become Pandoc dollar delimiters; payloads, prose, links, anchors, comments all unchanged. Boundary fence newlines are Markdown delimiter syntax. Exact inverse recovers frozen input bytes.'}
(out/'ast-math-check.json').write_text(json.dumps(checks,indent=2)+'\n');assert checks['all_math_payloads_exact_including_internal_newlines'] and checks['all_expected_payloads_equal_actual_GitHub_audit_source']
run(['pandoc','preview.md','-f','markdown-fancy_lists','-s','-V','fontsize=11pt','-V','geometry:margin=25mm','-H','preview-header.tex','-o','preview.tex'],'pandoc.txt')
compiler_capture=[]
for i in [1,2]:
 run(['pdflatex','-interaction=nonstopmode','-halt-on-error','-jobname=preview','preview.tex'],f'pdflatex-pass{i}.txt')
 log_bytes=(out/'preview.log').read_bytes()
 (out/f'compiler-pass{i}-tex-log.txt').write_bytes(log_bytes)
 compiler_capture.append({'pass':i,'stdout_file':f'pdflatex-pass{i}.txt','stdout_sha256':sha(out/f'pdflatex-pass{i}.txt'),'tex_log_snapshot':f'compiler-pass{i}-tex-log.txt','tex_log_bytes':len(log_bytes),'tex_log_sha256':sha(out/f'compiler-pass{i}-tex-log.txt')})
(out/'compiler-evidence-capture.json').write_text(json.dumps(compiler_capture,indent=2)+'\n')
run(['pdfinfo','preview.pdf'],'pdfinfo.txt');run(['pdffonts','preview.pdf'],'pdffonts.txt');run(['pdftotext','-layout','preview.pdf','preview-text.txt'],'pdftotext.txt')
images=[];before=sha(out/'preview.pdf')
with fitz.open(out/'preview.pdf') as doc:
 count=len(doc)
 for i,page in enumerate(doc,1):
  p=out/f'page-{i:02}.png';page.get_pixmap(matrix=fitz.Matrix(1.5,1.5),alpha=False).save(p)
  with Image.open(p) as im:im.verify()
  with Image.open(p) as im:im.load();images.append({'path':p.name,'size':list(im.size),'mode':im.mode,'sha256':sha(p),'fully_decoded':True})
log=(out/'pdflatex-pass2.txt').read_text()+'\n'+(out/'compiler-pass2-tex-log.txt').read_text();diagnostics=re.findall(r'^.*(?:overfull|underfull|warning|missing|undefined|^!).*$',log,re.M|re.I)
record={'AST':checks,'page_count':count,'PNG_count':len(images),'PNG_complete':len(images)==count,'images':images,'pdf_sha256':before,'PDF_unchanged_after_export':sha(out/'preview.pdf')==before,'log_diagnostics_case_insensitive':diagnostics,'compiler_evidence_capture':compiler_capture,'full_page_visual_review':'PENDING','role':'Read-only source-faithful internal review derivative, not a learner PDF; no GitHub pixels/CSS/hyperlink parity claim.','rasterizer':'PyMuPDF 1.5x full pages, individually decoded by PIL'}
(out/'preview-check.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps({'pages':count,'pdf_sha256':before,'AST':checks,'diagnostics':diagnostics},indent=2))
