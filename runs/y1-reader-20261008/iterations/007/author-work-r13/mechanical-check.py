"""Checks source-level mechanics only; cannot establish GitHub styling or teaching adequacy."""
from pathlib import Path
import hashlib,json,re
w=Path(__file__).resolve().parent
p=w/'teaching.md';b=p.read_bytes();s=b.decode('utf8')
locs=re.findall(r'<!-- P(\d{3}) -->',s)
anchors=re.findall(r'<a name="([^"]+)"></a>',s)
links=re.findall(r'\]\(#([^)]+)\)',s)
prose=re.sub(r'\$\$.*?\$\$','',s,flags=re.S)
prose=re.sub(r'(?<!\$)\$(?!\$).*?(?<!\$)\$(?!\$)','',prose,flags=re.S)
# A URL destination is literal syntax, not prose emphasis. Preserve link labels.
prose=re.sub(r'\]\([^)]*\)',']',prose)
checks={
 'paragraph_locators_unique_and_sequential':locs==[f'{i:03}' for i in range(1,len(locs)+1)] and len(set(locs))==len(locs),
 'anchors_unique':len(anchors)==len(set(anchors)),
 'internal_links_have_targets':all(t in anchors for t in links),
 'all_seven_tasks_hints_solutions':all(anchors.count(f'{kind}-q{i}')==1 for i in range(1,8) for kind in ['task','hint','solution']),
 'hints_grouped_before_full_solutions':s.index('<a name="hint-q1">')<s.index('<a name="hint-q7">')<s.index('<a name="solutions">')<s.index('<a name="solution-q1">'),
 'all_task_prompts_precede_hint_group':all(s.index(f'<a name="task-q{i}">')<s.index('<a name="hints">') for i in range(1,8)),
 'all_named_help_and_return_links':all(f'](#hint-q{i})' in s and f'](#solution-q{i})' in s and f'](#task-q{i})' in s for i in range(1,8)),
 'no_atx_headings':not bool(re.search(r'^\s{0,3}#{1,6}\s',prose,re.M)),
 'no_setext_headings':not bool(re.search(r'^\s*(?:=+|-{3,})\s*$',prose,re.M)),
 'no_prose_bold_or_italic_markers':not bool(re.search(r'\*|_',prose)),
 'no_prose_html_emphasis_or_headings':not bool(re.search(r'<(?:b|strong|em|i|h[1-6])(?:\s|>)',prose,re.I)),
 'no_prose_table_headers':not bool(re.search(r'^\|',prose,re.M)),
 'display_math_delimiters_paired':s.count('$$')%2==0,
 'no_unresolved_placeholders':not bool(re.search(r'\b(?:TODO|TBD|FIXME|PLACEHOLDER)\b',s)),
 'numerical_record_bound_to_current_teaching':json.loads((w/'math-numerical-checks.json').read_text())['teaching_sha256']==hashlib.sha256(b).hexdigest(),
 'prompt_packet_unchanged':hashlib.sha256((w/'task-prompts-original.md').read_bytes()).hexdigest()=='93bed04239828e9206d1e77722ad6c0c28d6644288f3a39a8f6270afafac5978'
}
record={'teaching_sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b),'utf8_characters':len(s),'paragraph_locators':len(locs),'anchors':len(anchors),'internal_link_instances':len(links),'checks':checks,'source_level_checks_pass':all(checks.values()),'not_certified':['Actual GitHub destination style or math rendering','Actual browser navigation','Semantic adequacy or human learning','Parent technical/source review','Fresh SASIS','Iteration acceptance/publication'],'pending_parent_gates':['T11 actual destination review','T12 final acceptance','Independent final technical/source review','Fresh two-input whole-document SASIS','Publication'], 'limits':'These checks inspect the current Markdown source and records. Absence of prose emphasis markers cannot certify destination styling. No substitute renderer was used to claim a GitHub pass.'}
(w/'mechanical-checks.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
