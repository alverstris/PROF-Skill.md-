from pathlib import Path
import re,json,hashlib,difflib
out=Path(__file__).parent;author=out.parent;case=author.parent
h=lambda b:hashlib.sha256(b).hexdigest()
original_manifest=json.loads((author/'author-packet-manifest.json').read_text())
preserved=[]
for f in original_manifest['files']:
 p=author/f['relative_path']; b=p.read_bytes();preserved.append({'path':f['relative_path'],'matches_original':len(b)==f['bytes'] and h(b)==f['sha256']})
assert all(x['matches_original'] for x in preserved)
s=(author/'teaching-v1.md').read_text();v=s; edits=[]
def edit(old,new,issue):
 global v
 assert v.count(old)==1,(issue,old,v.count(old))
 v=v.replace(old,new,1);edits.append({'issue':issue,'old':old,'new':new})
rows=json.loads((case/'root-destination-math-failure-verification.json').read_text())['rows']
assert len(rows)==12 and sum(r['source'].count('\\,') for r in rows)==13
for r in rows:edit(r['source'],r['source'].replace('\\,',' '),'MATH-1')
edit('Read L1–L8 in order and pause at the numbered attempts. P7 is a later return to the ideas. The hints H1–H7 are grouped after the lesson; complete solutions S1–S7 follow all the hints.', 'Read [L1–L8](#d014-l1) in order and pause at the numbered attempts. [P7](#d014-p7) is a later return to the ideas. The [hints H1–H7](#d014-hints) are grouped after the lesson; [complete solutions S1–S7](#d014-solutions) follow all the hints.','NAV-1')
for i in range(1,8):
 edit(f'Help: H{i}; full solution: S{i}.',f'Help: [H{i}](#d014-h{i}); full solution: [S{i}](#d014-s{i}).','NAV-1')
 # A hint is one paragraph; retain it and add useful routes after it.
 old=re.search(rf'^H{i}\. .*$',v,re.M).group()
 edit(old,old+f' [Return to P{i}](#d014-p{i}) or [read S{i}](#d014-s{i}).','NAV-1')
# Solution return comes after the complete solution, including all equations.
for i in range(1,8):
 match=re.search(rf'^S{i}\. .*?(?=\nS\d\.|\Z)',v,re.M|re.S);old=match.group()
 trailing=old[len(old.rstrip()):]
 edit(old,old.rstrip()+f'\n\n[Return to P{i}](#d014-p{i}).'+trailing,'NAV-1')
for label,name in [('Reading route.','d014-reading-route'),('L1.','d014-l1'),('Hints.','d014-hints'),('Complete solutions.','d014-solutions')]+[(f'{c}{i}.',f'd014-{c.lower()}{i}') for c in ['P','H','S'] for i in range(1,8)]:
 old=re.search(r'^'+re.escape(label)+r' .*$',v,re.M).group()
 edit(old,f'<a name="{name}"></a>\n\n'+old,'NAV-1')
for label in ['Hints.','Complete solutions.']:
 old=re.search(r'^'+re.escape(label)+r' .*$',v,re.M).group()
 edit(old,old+' [Return to the reading route](#d014-reading-route).','NAV-1')
(author/'teaching-v2.md').write_text(v)
(out/'exact-edits.json').write_text(json.dumps(edits,indent=2)+'\n')
(out/'v1-to-v2.diff').write_text(''.join(difflib.unified_diff(s.splitlines(True),v.splitlines(True),fromfile='teaching-v1.md',tofile='teaching-v2.md')))
# Reverse each exact mutation in reverse order: a stronger check than a word diff.
r=v
for e in reversed(edits):
 assert r.count(e['new'])==1,(e['issue'],e['new'],r.count(e['new']))
 r=r.replace(e['new'],e['old'],1)
assert r==s
extract=lambda x:[('inline',m.group(1)) if m.group(1) is not None else ('display',m.group(2)) for m in re.finditer(r'\$`(.*?)`\$|\$\$(.*?)\$\$',x,re.S)]
a,b=extract(s),extract(v);assert len(a)==len(b)==346
comparison=[]
for i,(before,after) in enumerate(zip(a,b),1):
 same=before==after; allowed=before[0]==after[0]=='display' and after[1]==before[1].replace('\\,',' ')
 assert same or allowed
 comparison.append({'index':i,'kind':before[0],'exact':same,'allowed_spacing_change':not same and allowed,'changed_commands':before[1].count('\\,') if not same else 0})
anchors=re.findall(r'<a name="([^"]+)"></a>',v);links=re.findall(r'\[([^\]]+)\]\(#([^\)]+)\)',v)
assert len(anchors)==len(set(anchors))==25
assert all(t in anchors for _,t in links)
triples=[]
for i in range(1,8):
 blocks={c:re.search(rf'<a name="d014-{c.lower()}{i}"></a>\n\n(.*?)(?=\n<a name=|\Z)',v,re.S).group(1) for c in ['P','H','S']}
 row={'id':i,'task_to_hint':f'](#d014-h{i})' in blocks['P'],'task_to_solution':f'](#d014-s{i})' in blocks['P'],'hint_to_task':f'](#d014-p{i})' in blocks['H'],'hint_to_solution':f'](#d014-s{i})' in blocks['H'],'solution_to_task':f'](#d014-p{i})' in blocks['S']}
 assert all(value for key,value in row.items() if key!='id');triples.append(row)
assert v.index('<a name="d014-h7"')<v.index('<a name="d014-s1"')
report={'v1_sha256':h(s.encode()),'v2_sha256':h(v.encode()),'v2_bytes':len(v.encode()),'v2_physical_lf_lines':len(v.splitlines()),'reversible_exact_edit_log':r==s,'original_23_files':preserved,'all_original_files_unchanged':all(q['matches_original'] for q in preserved),'math_count':len(a),'inline_exact':sum(q['kind']=='inline' and q['exact'] for q in comparison),'display_exact':sum(q['kind']=='display' and q['exact'] for q in comparison),'display_spacing_changed':sum(q['allowed_spacing_change'] for q in comparison),'spacing_commands_changed':sum(q['changed_commands'] for q in comparison),'math_comparison':comparison,'named_anchors':anchors,'internal_link_count':len(links),'all_link_targets_exist':True,'triples':triples,'hint_solution_separation':True,'figures':[],'pending':'Fresh SASIS and actual destination/final acceptance; these local checks do not establish client rendering or clicks.'}
(out/'repair-checks.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k not in ['math_comparison','original_23_files','named_anchors','triples']},indent=2))
