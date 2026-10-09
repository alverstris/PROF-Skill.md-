from pathlib import Path
import re,json,hashlib
p=Path('teaching.md');raw=p.read_bytes();s=raw.decode();checks={}
ids=re.findall(r'<a id="([^"]+)"',s);links=re.findall(r'\]\(#([^\)]+)\)',s)
checks['anchor_ids_unique']=len(ids)==len(set(ids));checks['all_internal_targets_exist']=all(x in ids for x in links)
checks['matched_six_tasks_hints_solutions']=all(f'{kind}-a{i}' in ids for kind in ['task','hint','solution'] for i in range(1,7))
checks['hints_group_precedes_solutions']=s.index('<a id="hint-a6"')<s.index('<a id="solutions"')
checks['all_tasks_before_hints']=s.index('<a id="task-a6"')<s.index('<a id="hints"')
checks['no_atx_headings']=not re.search(r'^\s*#{1,6}\s',s,re.M)
checks['no_setext_headings']=not re.search(r'^[=-]{3,}\s*$',s,re.M)
checks['no_tables_with_forced_header_emphasis']=not re.search(r'^\s*\|',s,re.M)
prose=re.sub(r'\$\$.*?\$\$|\$[^$]*\$','',s,flags=re.S)
prose=re.sub(r'\]\([^)]*\)',']',prose)
checks['no_prose_emphasis_markers']=not re.search(r'\*|_',prose)
checks['no_control_characters_except_newlines']=not any(ord(c)<32 and c!='\n' for c in s)
checks['no_placeholders']=not re.search(r'TODO|FIXME|TBD|PLACEHOLDER',s)
checks['display_delimiters_even']=s.count('$$')%2==0
withoutdisplays=re.sub(r'\$\$.*?\$\$','',s,flags=re.S)
checks['inline_delimiters_even']=withoutdisplays.count('$')%2==0
commands=sorted(set(re.findall(r'\\([A-Za-z]+)',s)))
checks['saved_tex_commands_present']=all(x in commands for x in ['frac','ln','lim','to','infty','Delta','Rightarrow','times'])
para=re.findall(r'<!-- (P\d{3}) -->',s)
checks['stable_paragraph_ids_unique_complete']=para==[f'P{i:03}' for i in range(1,195)]
checks['no_backslash_doubled_by_shell']=not re.search(r'\\\\[A-Za-z]',s)
report={'teaching_sha256':hashlib.sha256(raw).hexdigest(),'checks':checks,'all_pass':all(checks.values()),'counts':{'anchors':len(ids),'internal_links':len(links),'paragraphs':len(para),'display_delimiters':s.count('$$'),'lines':len(s.splitlines())},'tex_commands':commands,'limits':'Source-byte and internal structure checks only. Actual GitHub rendering, mathematical typesetting, typography, anchor navigation, fresh SASIS and publication remain pending. No alternative renderer was used as destination evidence.'}
Path('mechanical-checks.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
