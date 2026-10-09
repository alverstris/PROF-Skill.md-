from pathlib import Path
import re,json,hashlib
from PIL import Image
root=Path(__file__).resolve().parents[1];d=root/'learner';out={'revision':'D017-original-r23-author-v1','files':[],'defects':[],'limits':['Static source check does not establish actual GitHub parsing, visual expression preservation, typography or live link behavior.']}
for p in sorted(d.glob('*.md')):
 txt=p.read_text(); tokens=re.findall(r'\$\$[\s\S]*?\$\$|(?<!\$)\$(?!\$)[^$\n]*?\$(?!\$)',txt); stripped=txt
 for tok in tokens:stripped=stripped.replace(tok,'MATH',1)
 anchors=re.findall(r'<a id="([^"]+)"></a>',txt)
 assert len(anchors)==len(set(anchors))
 assert not re.search(r'^#{1,6}\s|^\s*(?:===+|---+)\s*$',stripped,re.M)
 assert not re.search(r'\*|(?<!\w)_(?!\w)|<strong|<em\b|<h[1-6]\b',stripped)
 assert not re.search(r'\b(?:TODO|FIXME|TBD)\b',txt)
 assert stripped.count('$')==0
 for tok in tokens:
  if '<' in tok or '>' in tok:out['defects'].append({'kind':'literal_angle_in_math','file':p.name,'payload':tok})
  for m in re.finditer(r'\\(?:lt|gt)(?![a-zA-Z])(?=\S)',tok):
   loc=txt.index(tok);line=txt[:loc].count('\n')+1
   out['defects'].append({'kind':'missing_explicit_space_after_strict_comparison_command','file':p.name,'line':line,'payload':tok,'command':m.group()})
 links=[]
 for link in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)',txt):
  if link.startswith('https://'):continue
  path,_,anchor=link.partition('#');target=p.parent/path
  assert target.is_file(),(p,link)
  if anchor:assert f'<a id="{anchor}"></a>' in target.read_text(),(p,link)
  links.append(link)
 out['files'].append({'file':p.name,'lines':len(txt.splitlines()),'math_expressions':len(tokens),'unique_anchors':anchors,'local_links_valid':len(links),'prose_source_emphasis_markers':0})
for i in range(1,6):
 for name,anchor in [('lesson',f'p{i}'),('hints',f'h{i}'),('solutions',f's{i}')]:assert f'<a id="{anchor}"></a>' in (d/f'{name}.md').read_text()
m=json.loads((root/'learner-manifest.json').read_text())
for f in m['constituents']:
 p=Path(f['path']);assert p.stat().st_size==f['bytes'];assert hashlib.sha256(p.read_bytes()).hexdigest()==f['sha256']
out['freeze_hashes_unchanged']=True
out['images']=[{'path':p.name,'size_px':list(Image.open(p).size)} for p in sorted((d/'figures').glob('*.png'))]
out['status']='fail' if out['defects'] else 'pass'
(root/'audit/mechanical-original-v1.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(1 if out['defects'] else 0)
