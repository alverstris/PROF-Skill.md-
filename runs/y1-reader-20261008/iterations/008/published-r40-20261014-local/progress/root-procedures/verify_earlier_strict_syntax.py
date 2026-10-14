"""Independent exact-blob/payload check; no teaching or queue mutation."""
from pathlib import Path
import hashlib
import json
import re
import subprocess

WORK = Path(__file__).resolve().parents[2]
REPO = WORK/'.prof-maintenance/20261014/repository'
AUDIT = WORK/'.prof-sasis/20261014-d008-r39/earlier-success-review'
PIN = '0c0031cf996d7f47d4db878709f31676594aa08f'
inventory = json.loads((AUDIT/'accepted-teaching-exposure-inventory.json').read_bytes())
arts = [(case,a) for case in inventory['cases'] for a in case['artifacts']]
oids = sorted({a['blob'] for case,a in arts})
raw = subprocess.run(['git','-C',str(REPO),'cat-file','--batch'],input=('\n'.join(oids)+'\n').encode(),capture_output=True,check=True).stdout
objects = {}; pos=0
for oid in oids:
    end=raw.index(b'\n',pos); header=raw[pos:end].split(); assert header[0].decode()==oid and header[1]==b'blob'
    pos=end+1; size=int(header[2]); objects[oid]=raw[pos:pos+size]; pos+=size; assert raw[pos:pos+1]==b'\n'; pos+=1
assert pos==len(raw)
tree={}
for entry in filter(None,subprocess.check_output(['git','-C',str(REPO),'ls-tree','-rz',PIN]).split(b'\0')):
    meta,name=entry.split(b'\t',1); tree[name.decode()]=meta.split()[2].decode()
failures=[]; by_case={}; command_count=0
for case,a in arts:
    data=objects[a['blob']]
    assert tree[a['path']]==a['blob'] and len(data)==a['bytes'] and hashlib.sha256(data).hexdigest()==a['sha256']
    text=data.decode('utf-8-sig')
    spans=[m.span('body') for m in re.finditer(r'\$`(?P<body>[\s\S]*?)`\$',text)]
    spans += [m.span('body') for m in re.finditer(r'(?<![\\$])\$(?![`$])(?P<body>[^$\n]+?)(?<![\\`])\$(?!\$)',text)]
    spans += [m.span('body') for m in re.finditer(r'\$\$(?P<body>[\s\S]*?)\$\$',text)]
    spans += [m.span('body') for m in re.finditer(r'(?m)^```math[^\n]*\n(?P<body>[\s\S]*?)^```[^\n]*(?:\n|$)',text)]
    actual=[]
    for m in re.finditer(r'\\(?:lt|gt)(?![A-Za-z])',text):
        command_count+=1
        assert any(start<=m.start() and m.end()<=end for start,end in spans), (a['path'],m.start(),'strict command outside known mathematical payload')
        if text[m.end():m.end()+1]==' ':continue
        line=text.count('\n',0,m.start())+1; previous=text.rfind('\n',0,m.start()); column=m.start()-previous
        actual.append((line,column,m.group()))
        failures.append({'material_id':case['material_id'],'path':a['path'],'blob':a['blob'],'sha256':a['sha256'],'line':line,'column':column,'token':m.group(),'following':text[m.end():m.end()+10]})
    expected=[(e['line'],e['column'],e['token']) for e in a['scan']['strict_no_space']]
    assert actual==expected,(a['path'],actual,expected)
    if actual:by_case[case['material_id']]=by_case.get(case['material_id'],0)+len(actual)
assert len(arts)==21 and command_count==366 and len(failures)==68 and len(by_case)==7
record={'checked_commit':PIN,'markdown_blobs_verified':21,'strict_comparison_commands_in_math_payloads':command_count,
        'missing_literal_space_occurrences':len(failures),'affected_cases':by_case,'failures':failures,
        'requirement':'Published PROF SKILL.md requires a terminating literal space after every mathematical \\lt and \\gt command.',
        'source_format_requirement':'fail','rendering_or_mathematical_failure_inferred':False,
        'queue_or_teaching_modified':False}
(AUDIT/'root-strict-syntax-verification.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in record.items() if k!='failures'}))
