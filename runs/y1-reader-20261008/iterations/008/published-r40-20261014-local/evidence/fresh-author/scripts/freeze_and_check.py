from pathlib import Path
import hashlib, json, re
ROOT=Path(__file__).resolve().parents[1]
TEACH=ROOT/'teaching'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
files=sorted(p for p in TEACH.rglob('*') if p.is_file())
manifest={'revision':'D008-r40-fresh-author-1','frozen_before_review':True,
          'policy':'Learner-facing constituents are preserved unchanged. Checks do not repair teaching.',
          'files':[{'path':p.relative_to(ROOT).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p)} for p in files]}
(ROOT/'evidence'/'teaching-freeze.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
anchors={}; texts={}; expressions=[]; findings=[]; links=[]
for p in files:
    if p.suffix!='.md': continue
    t=p.read_text(encoding='utf-8'); texts[p]=t
    aa=re.findall(r'<a id="([^"]+)"></a>',t); anchors[p]=set(aa)
    if len(aa)!=len(set(aa)): findings.append({'type':'duplicate_anchor','file':p.name})
    if re.search(r'^\s{0,3}#{1,6}\s|^\s*(?:={3,}|-{3,})\s*$',t,re.M): findings.append({'type':'prose_heading_markup','file':p.name})
    if '**' in t or '__' in t: findings.append({'type':'bold_markup','file':p.name})
    if '<details' in t or '<summary' in t: findings.append({'type':'disclosure','file':p.name})
    if re.search(r'\b(?:TODO|TBD|FIXME|PLACEHOLDER)\b',t): findings.append({'type':'unresolved_placeholder','file':p.name})
    for m in re.finditer(r'\$`([^`]+)`\$|```math\n(.*?)\n```',t,re.S):
        payload=m.group(1) if m.group(1) is not None else m.group(2)
        line=t[:m.start()].count('\n')+1
        expressions.append({'id':f'{p.stem}-m{len([e for e in expressions if e["file"]==p.name])+1:03d}',
                            'file':p.name,'line':line,'type':'inline' if m.group(1) is not None else 'display',
                            'source':payload})
        if '<' in payload or '>' in payload: findings.append({'type':'literal_strict_comparison','file':p.name,'line':line})
        for bad in re.finditer(r'\\(?:lt|gt)(?! )',payload): findings.append({'type':'comparison_missing_space','file':p.name,'line':line,'payload':payload})
    # Every inline math delimiter pair and display fence must occur in inventory.
    expected=t.count('$`')+t.count('```math\n')
    actual=sum(e['file']==p.name for e in expressions)
    if expected!=actual: findings.append({'type':'math_inventory_mismatch','file':p.name,'expected':expected,'actual':actual})
    for m in re.finditer(r'\[([^\]]+)\]\(([^)]+)\)',t):
        links.append({'source':p.name,'line':t[:m.start()].count('\n')+1,'label':m.group(1),'target':m.group(2)})
allanchors=[a for aset in anchors.values() for a in aset]
if len(allanchors)!=len(set(allanchors)): findings.append({'type':'cross_file_anchor_reuse'})
for li in links:
    if li['target'].startswith('https://'): continue
    pp, _, frag=li['target'].partition('#')
    dest=(TEACH/pp).resolve() if pp else TEACH/li['source']
    if not dest.exists(): findings.append({'type':'missing_link_file',**li})
    elif frag and frag not in anchors.get(dest,set()): findings.append({'type':'missing_fragment',**li})
for p,t in texts.items():
    for src,w,h in re.findall(r'<img src="([^"]+)"[^>]+width="(\d+)" height="(\d+)"',t):
        from PIL import Image
        fp=p.parent/src; im=Image.open(fp)
        if im.size!=(int(w),int(h)): findings.append({'type':'image_geometry', 'file':p.name,'src':src})
tasks=['a1','a2','a3','a4','r1']
for task in tasks:
    mainanchor='main-d008-revisit' if task=='r1' else 'main-d008-'+task
    for name,anchor in [('main.md',mainanchor),('hints.md','hints-d008-'+task),('solutions.md','solutions-d008-'+task)]:
        if anchor not in anchors[TEACH/name]: findings.append({'type':'unmatched_task','task':task,'file':name})
inventory={'revision':manifest['revision'],'source_files':[f for f in manifest['files'] if f['path'].endswith('.md')],
           'expressions':expressions, 'count':len(expressions)}
(ROOT/'evidence'/'math-expression-inventory.json').write_text(json.dumps(inventory,indent=2)+'\n',encoding='utf-8')
(ROOT/'evidence'/'link-inventory.json').write_text(json.dumps(links,indent=2)+'\n',encoding='utf-8')
result={'revision':manifest['revision'],'constituents':len(files),'math_count':len(expressions),
        'file_math_counts':{p.name:sum(e['file']==p.name for e in expressions) for p in texts},
        'task_ids':tasks,'local_links':sum(not x['target'].startswith('https://') for x in links),
        'findings':findings,'status':'pass' if not findings else 'fail',
        'limits':'Source syntax, identity, existence and correspondence only. Actual GitHub rendering and live click routes are not certified.'}
(ROOT/'evidence'/'mechanical-checks.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
