"""Post-freeze read-only teaching audit; output stays in technical-review."""
from pathlib import Path
import hashlib
import json
import math
import re
from decimal import Decimal, getcontext

HERE=Path(__file__).resolve().parent
TEACH=HERE.parent/'fresh-author'/'teaching'
files=['main.md','hints.md','solutions.md']
contents={p:(TEACH/p).read_text(encoding='utf-8') for p in files}
anchors={p:set(re.findall(r'<a id="([^"]+)"',s)) for p,s in contents.items()}
report={'files':{},'local_link_errors':[],'math_payload_issues':[],'duplicate_anchors':[]}
math_inventory=[]
all_ids={}
for p,s in contents.items():
    inline=list(re.finditer(r'\$`([^`]*?)`\$',s,re.S))
    displays=list(re.finditer(r'```math\s*\n(.*?)\n```',s,re.S))
    report['files'][p]={'sha256':hashlib.sha256((TEACH/p).read_bytes()).hexdigest(),
        'lines':len(s.splitlines()),'anchors':sorted(anchors[p]),
        'inline_math':len(inline),'display_math':len(displays)}
    for a in anchors[p]:
        if a in all_ids:report['duplicate_anchors'].append([a,all_ids[a],p])
        all_ids[a]=p
    for m in inline+displays:
        payload=m.group(1)
        loc={'file':p,'line':s.count('\n',0,m.start())+1}
        math_inventory.append({**loc,'type':'inline' if m in inline else 'display','payload':payload})
        if '<' in payload or '>' in payload:
            report['math_payload_issues'].append({**loc,'issue':'literal strict comparison'})
        if re.search(r'\\(?:lt|gt)(?!\s)',payload):
            report['math_payload_issues'].append({**loc,'issue':'missing terminating space after comparison command'})
    for m in re.finditer(r'\[[^\]]*\]\(([^)]+)\)',s):
        target=m.group(1)
        if target.startswith('http'):continue
        parts=target.split('#',1)
        filename=parts[0] or p
        if filename not in anchors:
            report['local_link_errors'].append({'file':p,'target':target,'issue':'file absent'})
        elif len(parts)==2 and parts[1] not in anchors[filename]:
            report['local_link_errors'].append({'file':p,'target':target,'issue':'anchor absent'})
    report['files'][p]['atx_or_setext_headings']=re.findall(r'(?m)^(?:#{1,6}\s.*|=+\s*|-{3,}\s*)$',s)
    report['files'][p]['bold_markers']=s.count('**')+s.count('__')

getcontext().prec=60
D=Decimal
composite=lambda v:(-2*v).exp()/(1+v).sqrt()
z=(D(4)/D(300000))**2
report['numerical_checks']={
    'ln1p1':str(D('1.1').ln()),'ln0p96':str(D('0.96').ln()),
    'cos0p2':repr(math.cos(.2)),
    'cos_linear_error':repr(1-math.cos(.2)),
    'cos_quadratic_error':repr(math.cos(.2)-.98),
    'composite0p05':str(composite(D('.05'))),
    'composite0p05_float':repr(math.exp(-.1)/math.sqrt(1.05)),
    'composite0p05_linear':str(1-D(5)/2*D('.05')),
    'composite0p05_quadratic':str(1-D(5)/2*D('.05')+D(27)/8*D('.05')**2),
    'composite0p05_true_linear_error':str(composite(D('.05'))-D('.875')),
    'composite0p05_true_quadratic_error':str(D('.8834375')-composite(D('.05'))),
    'sensor_linear_2p1':str(D(3)+D('.4')*D('.1')),
    'sensor_quadratic_2p1':str(D(3)+D('.4')*D('.1')-D('.1')*D('.1')**2),
    'sensor_cubic_counterexample_error':str(D(2)*D('.1')**3),
    'sqrt4p04':str(D('4.04').sqrt()),
    'clock_extra_86400s':str(D(86400)*3*z*z/8),
    'clock_doubled_extra':str(16*3*z*z/8),
    'clock_high_speed_L':str(1+D('.64')/2),
    'clock_high_speed_Q':str(1+D('.64')/2+3*D('.64')**2/8),
}
prep=json.loads((HERE/'prep-manifest.json').read_text(encoding='utf-8-sig'))
report['prep_seal_matches']={e['path']:hashlib.sha256((HERE/e['path']).read_bytes()).hexdigest()==e['sha256'] for e in prep['files']}
attempt=json.loads((HERE/'prompt-first-seal.json').read_text(encoding='utf-8-sig'))
report['prompt_first_seal_matches']=hashlib.sha256((HERE/attempt['path']).read_bytes()).hexdigest()==attempt['sha256']
freeze=json.loads((HERE.parent/'fresh-author'/'evidence'/'teaching-freeze.json').read_text(encoding='utf-8-sig'))
report['teaching_freeze_matches']={e['path']:hashlib.sha256((HERE.parent/'fresh-author'/e['path']).read_bytes()).hexdigest()==e['sha256'] for e in freeze['files']}
(HERE/'audit-check-results.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
(HERE/'source-math-inventory.json').write_text(json.dumps(math_inventory,indent=2),encoding='utf-8')
print(json.dumps(report,indent=2))
