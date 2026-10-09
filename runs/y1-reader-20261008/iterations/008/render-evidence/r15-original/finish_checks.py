from pathlib import Path
from collections import Counter
from lxml import html
import re,json,sys,hashlib
sys.dont_write_bytecode=True
ROOT=Path(__file__).parent
sys.path.insert(0,str(ROOT.parents[1]/'d008-render-review-prep'))
import review_helpers as h

def save(name,obj):
 with (ROOT/name).open('x') as f:json.dump(obj,f,ensure_ascii=False,indent=2);f.write('\n')
def norm(s):return re.sub(r'\s+',' ',s).strip()
source=(ROOT/'teaching-original.md').read_text();article_html=(ROOT/'github-article.html').read_text();dom=html.fromstring(article_html)
# Each independent parse is one ordinary parse of the actual HTML bytes, never an unescape of parsed text.
blocks={};ordered=[];current=None
for el in dom:
 text=''.join(el.itertext());m=re.match(r'\s*(P\d{3})\.',text)
 if m:current=m[1];ordered.append(current);blocks[current]={'text':[],'links':[],'html_paragraphs':0}
 if current:
  blocks[current]['text'].append(text);blocks[current]['html_paragraphs']+=1
  blocks[current]['links'] += [{'label':''.join(a.itertext()),'href':a.get('href')} for a in el.iter('a') if a.get('href')]
source_blocks=re.findall(r'^(P\d{3})\.(.*?)(?=^P\d{3}\.|\Z)',source,re.M|re.S)
rows=[]
for label,body in source_blocks:
 source_block=label+'.'+body
 maths=[]
 def protect(m):
  fmt=next(x for x in ['fence','protected','display','inline'] if m.group(x) is not None);d='$$' if fmt in ['fence','display'] else '$';maths.append(d+m.group(fmt+'_body')+d);return f'PROF_MATH_TOKEN_{len(maths)-1}_END'
 protected=h.MATH.sub(protect,source_block)
 expected=re.sub(r'<a\s+(?:id|name)="[^"]+"\s*></a>','',protected)
 expected=re.sub(r'(?<!!)\[([^\]]+)\]\(([^)]+)\)',lambda m:m[1],expected)
 expected=re.sub(r'PROF_MATH_TOKEN_(\d+)_END',lambda m:maths[int(m[1])],expected)
 actual=' '.join(blocks[label]['text'])
 rows.append({'label':label,'exact_after_only_whitespace_folding':norm(expected)==norm(actual),'expected':norm(expected),'actual':norm(actual),'destination_paragraph_count':blocks[label]['html_paragraphs'],'links':blocks[label]['links']})
assert ordered==[f'P{i:03}' for i in range(1,69)]
failed=[r['label'] for r in rows if not r['exact_after_only_whitespace_folding']]
assert failed==['P010','P014','P015','P026','P033','P034','P040','P051','P062']
source_math=json.loads((ROOT/'source-math.json').read_text());github_math=json.loads((ROOT/'github-math.json').read_text())
formats=Counter(x['format'] for x in source_math)
residual=h.MATH.sub('',source)
assert '$' not in residual and '`' not in residual
prompts=[]
for i,label in enumerate(['P011','P034','P045','P051'],1):
 row=next(r for r in rows if r['label']==label)
 idx=[n for n,x in enumerate(source_math,1) if x['paragraph']==label]
 prompts.append({'task':f'A{i}','paragraph':label,'full_block_exact':row['exact_after_only_whitespace_folding'],'math_indices':idx,'failing_math_indices':[n for n in idx if source_math[n-1]['payload']!=github_math[n-1]['payload']],'numeric_tokens_exact':re.findall(r'\d+(?:\.\d+)?',row['expected'])==re.findall(r'\d+(?:\.\d+)?',row['actual']),'prose_note':'Whole-document outside-math prose equality is checked in markup-navigation-audit.json. Full prompt blocks retained in paragraph-block-comparison.json.'})
expected_navigation={'P002':['#hints','#solutions'],'P011':['#h1','#s1','#after-a1'],'P034':['#h2','#s2','#after-a2'],'P045':['#h3','#s3','#after-a3'],'P051':['#h4','#s4'],'P054':['#a1','#a2','#a3','#a4'],'P056':['#a1'],'P057':['#a2'],'P058':['#a3'],'P059':['#a4'],'P060':['#start','#a1','#a2','#a3','#a4'],'P062':['#a1','#after-a1'],'P064':['#a2','#after-a2'],'P066':['#a3','#after-a3'],'P068':['#a4','#start']}
nav=[]
for label,expected in expected_navigation.items():
 actual=[x['href'] for x in blocks[label]['links']]
 nav.append({'paragraph':label,'expected_hrefs':expected,'actual_hrefs':actual,'exact':expected==actual})
assert all(x['exact'] for x in nav)
# Preserve literal article snippets without decoding escaped payloads a second time.
wrappers=re.findall(r'<math-renderer\b[^>]*>.*?</math-renderer>',article_html,re.S)
defects=json.loads((ROOT/'localized-math-failures.json').read_text())['localized']
for x in defects:x['literal_richText_wrapper']=wrappers[x['math_index']-1]
save('paragraph-block-comparison.json',{'source_labels': [label for label,_ in source_blocks], 'destination_labels':ordered,'all_68_visible_labels_exactly_once_and_in_order':True,'failed_blocks':failed,'rows':rows,'normalization':'One ordinary lxml HTML parse of original article for this independent block check; no further unescape. Source math syntax replaced with destination delimiters, explicit anchors and Markdown link syntax removed, then whitespace folded only. Exact math bytes remain separately checked.'})
save('prompt-group-navigation-checks.json',{'source_formats':dict(formats),'all_source_dollars_and_backticks_accounted_for':True,'prompts':prompts,'explicit_navigation':nav,'group_boundaries':{'core':'P001–P054','hint_heading':'P055','hints':'P056–P059','end_hints':'P060','solution_heading':'P061','solutions':'P062–P068'},'scope':'Only representation, numbering, links and group ordering; no learner response, reasoning adequacy or SASIS evaluation.'})
save('literal-destination-defects.json',defects)
print(json.dumps({'visible_labels':len(ordered),'source_formats':dict(formats),'failed_blocks':failed,'explicit_navigation_rows':len(nav),'all_explicit_navigation_exact':all(x['exact'] for x in nav)},indent=2))
