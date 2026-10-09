from pathlib import Path
import re,json,hashlib,difflib
p=Path(__file__).parent
old=(p/'teaching-v2.md').read_text()
phrase='At the specified instant it is'
replacement='Returning to the worked approaching-car example, at its specified instant the relation is'
assert old.count(phrase)==1
clarified=old.replace(phrase,replacement)
chunks=re.split(r'(```math\n.*?\n```)',clarified,flags=re.S)
count=0
for i in range(0,len(chunks),2):
 chunks[i],n=re.subn(r'\$([^$\n]+)\$',lambda m:'$`'+m.group(1)+'`$',chunks[i]);count+=n
new=''.join(chunks);assert count==185
(p/'teaching-v3.md').write_text(new)
def payloads(s,protected):
 pat=r'```math\n(.*?)\n```|\$`([^`\n]+)`\$' if protected else r'```math\n(.*?)\n```|\$([^$\n]+)\$'
 return [{'format':'display' if m.group(1) is not None else 'inline','payload':m.group(1) if m.group(1) is not None else m.group(2)} for m in re.finditer(pat,s,re.S)]
a,b=payloads(old,False),payloads(new,True);assert a==b and len(a)==201
unprotect=re.sub(r'\$`([^`\n]+)`\$',lambda m:'$'+m.group(1)+'$',new)
assert unprotect==clarified
sha=lambda f:hashlib.sha256(f.read_bytes()).hexdigest()
preserved={}
for version in (1,2):
 manifest=json.loads((p/f'freeze-manifest-v{version}.json').read_text());preserved[f'v{version}']=all(sha(Path(x['path']))==x['sha256'] for x in manifest['learner_constituents']);assert preserved[f'v{version}']
report={'source_sha256':sha(p/'teaching-v2.md'),'target_sha256':sha(p/'teaching-v3.md'),'inline_count':185,'display_count':16,'all201_ordered_payloads_exact':a==b,'fenced_display_bytes_exact':re.findall(r'```math\n.*?\n```',old,re.S)==re.findall(r'```math\n.*?\n```',new,re.S),'only_prose_change':{'paragraph':'P014','old':phrase,'new':replacement},'prose_otherwise_exact':unprotect==clarified,'figures_paths_unchanged':re.findall(r'!\[[^\]]*\]\(([^)]+)\)',old)==re.findall(r'!\[[^\]]*\]\(([^)]+)\)',new),'original_frozen_constituents_preserved':preserved,'destination_status':'PENDING: exact source preservation is not proof of actual destination parsing','prose_diff_after_unprotect':''.join(difflib.unified_diff(old.splitlines(True),unprotect.splitlines(True)))}
(p/'comparison-v3.json').write_text(json.dumps(report,indent=2)+'\n');(p/'math-payloads-v3.json').write_text(json.dumps(b,indent=2)+'\n');print(json.dumps(report,indent=2))
