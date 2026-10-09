from pathlib import Path
import re,json,hashlib
from lxml import html
r=Path(__file__).parent;s=(r/'teaching-v2.md').read_bytes().decode('utf-8');old=(r.parent/'v1/teaching-original.md').read_bytes();a=json.loads((r/'markup-navigation-audit.json').read_text())
changes=[]
def inverse_inline(m):
 payload=m[1];back=payload.replace('\\lt ','<').replace('\\gt ','>')
 if back!=payload:changes.append({'from':payload,'to':back})
 return '$'+back+'$'
x=re.sub(r'\$`(.*?)`\$',inverse_inline,s,flags=re.S)
x,count=re.subn(r'\n```math\n(.*?)\n```\n',lambda m:'$$'+m[1]+'$$',x,flags=re.S)
assert count==27 and x.count('It need not be zero')==1;x=x.replace('It need not be zero','It is not zero');assert x.encode()==old;assert len(changes)==9
source_blocks=dict(zip((z:=re.split(r'<!--\s*(P\d+)\s*-->',s)[1:])[::2],z[1::2]));old_blocks=dict(zip((z:=re.split(r'<!--\s*(P\d+)\s*-->',old.decode())[1:])[::2],z[1::2]));rich=json.loads((r/'embedded-data.json').read_text())['payload']['codeViewBlobRoute']['richText'];doc=html.fromstring(rich);texts=[' '.join(''.join(p.itertext()).split()) for p in doc.xpath('./p')];prompts=[]
for n,pid in enumerate(['P016','P061','P078','P085'],1):
 text=' '.join(source_blocks[pid].split());prompts.append({'task':f'A{n}','paragraph':pid,'plain_task_prose_identical_to_original':source_blocks[pid]==old_blocks[pid],'actual_destination_exact_occurrences':texts.count(text),'task_sha256':hashlib.sha256(source_blocks[pid].encode()).hexdigest()})
assert all(p['plain_task_prose_identical_to_original'] and p['actual_destination_exact_occurrences']==1 for p in prompts)
rec={'source_revision_inverse_exactly_recovers_original_bytes':True,'named_operator_reversions':changes,'display_fence_reversions':count,'added_external_blank_newlines_removed_in_exact_inverse':54,'wording_reversion':'It need not be zero -> It is not zero, exactly once in inverse check only; no file content edited.','source_P012':source_blocks['P012'].strip(),'four_prompt_checks':prompts,'full_destination_prose_math_links_numeric_checks':a['checks']}
(r/'revision-and-prompt-checks.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n');print('Exact inverse and all four actual destination prompt checks pass.')
