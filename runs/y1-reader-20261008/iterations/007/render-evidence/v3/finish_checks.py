#!/usr/bin/env python3
from pathlib import Path
import json,re,hashlib
ROOT=Path(__file__).parent
def save(n,x): (ROOT/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
source=(ROOT/'normalized-for-audit.md').read_text()
audit=json.loads((ROOT/'scoped-markup-navigation-audit.json').read_text())
maths=audit['source_math'];actual=audit['github_math']
pat=re.compile(r'\$\$(.*?)\$\$|(?<!\$)\$(?!\$)(.*?)(?<!\$)\$(?!\$)',re.S)
source_matches=list(pat.finditer(source))
locs=[]
for i,(s,g,m) in enumerate(zip(maths,actual,source_matches),1):
 if s!=g:
  locs.append({'math_index':i,'paragraph':re.findall(r'<!-- (P\d{3}) -->',source[:m.start()])[-1],'source_payload':s['payload'],'github_payload':g['payload'],'lost_thinspace_backslashes':s['payload'].count('\\,')-g['payload'].count('\\,'),'source_numeric_tokens':re.findall(r'\d+(?:\.\d+)?',s['payload']),'github_numeric_tokens':re.findall(r'\d+(?:\.\d+)?',g['payload'])})
expected=(ROOT/'expected-prose-stream.txt').read_text().strip();got=(ROOT/'actual-prose-stream.txt').read_text().strip()
norm=lambda x:re.sub(r'\s+',' ',x).strip()
prose_expected=pat.sub(' MATH_PAYLOAD ',expected);prose_actual=pat.sub(' MATH_PAYLOAD ',got)
save('payload-and-prose-findings.json',{'math_mismatches':locs,'math_payload_count':len(maths),'math_payload_exact_count':sum(s==g for s,g in zip(maths,actual)),'prose_only_exact_with_each_math_replaced_by_same_token':norm(prose_expected)==norm(prose_actual),'all_numeric_tokens_in_full_stream_same_order':re.findall(r'\d+(?:\.\d+)?',expected)==re.findall(r'\d+(?:\.\d+)?',got),'no_extra_entity_decoding':True,'findings':'See exact counts and localized mismatches; no recursive HTML decoding.'})
# Scoped source-location navigation check. Earlier count checks are retained, not silently replaced.
blocks=re.split(r'(?=<a name=")',source)
source_sections={re.search(r'<a name="([^"]+)"></a>',b)[1]:b for b in blocks if re.search(r'<a name="([^"]+)"></a>',b)}
taskchecks=[]
for i in range(1,8):
 t,h,s=[f'{name}-q{i}' for name in ['task','hint','solution']]
 taskchecks.append({'task':f'Q{i}','task_to_hint':f'[Hint Q{i}](#{h})' in source_sections[t],'task_to_solution':f'[Solution Q{i}](#{s})' in source_sections[t],'hint_return_to_task':f'[Return to Q{i}](#{t})' in source_sections[h],'solution_return_to_task':f'[Return to Q{i}](#{t})' in source_sections[s],'solution_to_own_hint':f'[Hint Q{i}](#{h})' in source_sections[s],'task_hint_solution_titles':[audit['anchors_to_visible_paragraphs']['user-content-'+v] for v in [t,h,s]]})
save('task-section-navigation.json',{'tasks':taskchecks,'all_relationships_true':all(all(v for k,v in r.items() if isinstance(v,bool)) for r in taskchecks),'source_to_server_link_stream_exact':audit['checks']['all_source_link_texts_and_hrefs_in_order'],'all_internal_targets_present_once':audit['checks']['all_internal_destinations_once'],'internal_link_count':sum(l['href'].startswith('#') for l in audit['links']),'anchor_count':len(audit['github_anchor_ids']),'group_order':audit['checks']['all_tasks_before_all_hints_before_all_solutions'],'external_links':audit['external_links'],'scope':'Source section context plus exact complete server href/text order and exact sanitized target order. No clicks or client fragment execution observed.'})
dom=json.loads((ROOT/'dom-structure.json').read_text())
elements=dom['all_article_elements']+dom['ancestors'];classes={c for e in elements for c in e['attrs'].get('class','').split()};tags={e['tag'] for e in elements}
allrules=[];candidates=[]
for p in sorted((ROOT/'current-css').glob('*.css')):
 text=p.read_text()
 for m in re.finditer(r'([^{}]+)\{([^{}]*)\}',text):
  selector,decl=m[1].strip(),m[2]
  if re.search(r'(?:^|;)(?:font-weight|font-style|font)\s*:',decl):
   r={'file':str(p.relative_to(ROOT)),'selector':selector,'declarations':decl,'offset':m.start()};allrules.append(r)
   toks=set(re.findall(r'\.([A-Za-z_][\w-]*)',selector))
   if toks&classes or not toks: candidates.append(r)
save('all-css-font-declarations.json',allrules)
save('css-font-candidates.json',{'present_tags':sorted(tags),'present_classes':sorted(classes),'font_rules_involving_present_classes_or_without_classes':candidates,'inline_styles':dom['inline_styles'],'style_blocks':dom['page_style_blocks'],'extraction_limit':'Preserved all font/font-weight/font-style leaf rules for manual contextual review; this is not a computed cascade or browser selector engine.'})
print(json.dumps({'math_mismatch_paragraphs':[x['paragraph'] for x in locs],'math_mismatch_count':len(locs),'lost_backslashes':sum(x['lost_thinspace_backslashes'] for x in locs),'css_font_rule_count':len(allrules),'css_candidate_count':len(candidates),'navigation_checks':taskchecks},ensure_ascii=False))
