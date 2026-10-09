from pathlib import Path
import re,hashlib,json
p=Path(__file__).resolve().parents[1]
s=(p/'teaching.md').read_text()
plain=re.sub(r'<!-- P\d+ -->\n','',s)
original=(p/'task-prompts-original.md').read_text()
checks={}
for n in range(1,5):
 a=original.index(f'A{n}.');b=original.index(f'A{n+1}.') if n<4 else len(original)
 checks[f'prompt_A{n}_verbatim']=original[a:b].strip() in plain
markers=re.findall(r'<!-- P(\d+) -->',s)
checks['sequential_locators']=markers==[f'{n:03}' for n in range(1,len(markers)+1)]
anchors=re.findall(r'<a name="([^"]+)"></a>',s)
targets=re.findall(r'\]\(#([^\)]+)\)',s)
checks['unique_anchors']=len(anchors)==len(set(anchors))
checks['all_fragment_targets_exist']=set(targets)<=set(anchors)
checks['four_matched_tasks_hints_solutions']=all(x in anchors for n in range(1,5) for x in [f'a{n}',f'h{n}',f's{n}'])
checks['all_hints_before_all_solutions']=max(s.index(f'<a name="h{n}"') for n in range(1,5))<s.index('<a name="solutions"')
checks['all_solutions_have_returns']=all(f'[Return to A{n}](#a{n}) · [Hint A{n}](#h{n})' in s for n in range(1,5))
prose=re.sub(r'\$\$[\s\S]*?\$\$','',s)
prose=re.sub(r'\$[^$\n]*\$','',prose)
checks['no_atx_or_setext_headers']=not re.search(r'(?m)^\s{0,3}#{1,6}\s|^\s{0,3}(?:===+|---+)\s*$',prose)
checks['no_bold_italic_markers']=not any(x in prose for x in ['**','__','<b>','<strong>','<i>','<em>']) and '*' not in prose
checks['no_markdown_table_headers']=not re.search(r'(?m)^\s*\|.*\|\s*$',prose)
checks['no_placeholders']=not any(x in s for x in ['@@','TODO','TBD','FIXME'])
checks['no_external_learner_constituents']=not re.search(r'!\[',s)
checks['original_preserved']=hashlib.sha256((p/'teaching-original.md').read_bytes()).hexdigest()==hashlib.sha256((p/'teaching.md').read_bytes()).hexdigest()
report={'teaching_sha256':hashlib.sha256((p/'teaching.md').read_bytes()).hexdigest(),'teaching_bytes':len((p/'teaching.md').read_bytes()),'teaching_utf8_characters':len(s),'prompt_sha256':hashlib.sha256((p/'task-prompts-original.md').read_bytes()).hexdigest(),'checks':checks,'anchors':anchors,'fragment_link_count':len(targets),'limits':'These are source-level checks only. No actual GitHub rendered styling, math conversion, anchor scroll or visibility test was performed. Parent-owned destination check remains pending.'}
(p/'author/mechanical-checks.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
assert all(checks.values())
