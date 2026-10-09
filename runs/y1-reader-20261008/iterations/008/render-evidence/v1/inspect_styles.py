from pathlib import Path
import re,json,hashlib
ROOT=Path(__file__).parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
inv=json.loads((ROOT/'current-css-inventory.json').read_text());assert all(x.get('status')==200 for x in inv['fetches'])
for rec in inv['fetches']:assert sha(ROOT/rec['path'])==rec['sha256']
dom=json.loads((ROOT/'dom-structure.json').read_text());elements=dom['article_elements']+dom['ancestors'];classes={c for e in elements for c in e['attrs'].get('class','').split()};tags={e['tag'] for e in elements};ids={e['attrs']['id'] for e in elements if 'id'in e['attrs']};names={e['attrs']['name'] for e in elements if 'name'in e['attrs']}
def selector_parts(s):
 parts=[];start=0;depth=0;quote=None;escaped=False
 for i,c in enumerate(s):
  if escaped:escaped=False;continue
  if c=='\\':escaped=True;continue
  if quote:
   if c==quote:quote=None
   continue
  if c in '\"\'':quote=c;continue
  if c in '([':depth+=1
  elif c in ')]':depth=max(0,depth-1)
  elif c==',' and depth==0:parts.append(s[start:i].strip());start=i+1
 parts.append(s[start:].strip());return parts
allrules=[];candidates=[];variables=[]
for p in sorted((ROOT/'current-css').glob('*.css')):
 text=p.read_text()
 for m in re.finditer(r'([^{}]+)\{([^{}]*)\}',text):
  selector,decl=m[1].strip(),m[2]
  if '--base-text-weight-normal:' in decl:variables.append({'file':str(p.relative_to(ROOT)),'selector':selector,'definitions':re.findall(r'--base-text-weight-normal:[^;}]+',decl)})
  if re.search(r'(?:^|;)(?:font-weight|font-style|font)\s*:',decl):
   record={'file':str(p.relative_to(ROOT)),'selector':selector,'declarations':decl,'offset':m.start()};allrules.append(record);parts=selector_parts(selector);relevant=[]
   for branch in parts:
    cs=set(re.findall(r'\.([A-Za-z_][\w-]*)',branch))
    if not cs or cs&classes or ':not(' in branch:relevant.append(branch)
   if relevant:candidates.append(record|{'candidate_branches':relevant})
prior=ROOT.parents[1]/'d007-render-review/v3';old=json.loads((prior/'current-css-inventory.json').read_text());same_css={x['url']:x['sha256'] for x in inv['fetches']}=={x['url']:x['sha256'] for x in old['fetches']};old_dom=json.loads((prior/'dom-structure.json').read_text())
clean=lambda d:[{'tag':x['tag'],'attrs':{k:v for k,v in x['attrs'].items() if k!='initial-path'}} for x in d['ancestors']]
record={'CSS_count':len(inv['fetches']),'all_current_CSS_fetched_and_hash_verified':True,'same_bytes_as_D007_v3_independent_review':same_css,'same_ancestors_except_route':clean(dom)==clean(old_dom),'present_classes':sorted(classes),'present_tags':sorted(tags),'present_ids':sorted(ids),'present_names':sorted(names),'font_rule_count':len(allrules),'font_candidate_count':len(candidates),'candidate_rules':candidates,'normal_weight_definitions':variables,'unique_inline_styles':sorted({json.dumps(x,sort_keys=True) for x in dom['inline_styles']}),'style_blocks':dom['style_blocks'],'limit':'Leaf declaration inventory and conservative selector review aid, not a browser selector/cascade engine. Top-level selector branches considered individually; any negation branch retained rather than excluded by absent classes. Complete stylesheet bytes and DOM preserved for manual contextual inspection.'}
(ROOT/'all-css-font-declarations.json').write_text(json.dumps(allrules,indent=2)+'\n');(ROOT/'css-scope-review.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record,indent=2))
