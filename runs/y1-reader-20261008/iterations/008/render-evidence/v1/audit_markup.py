#!/usr/bin/env python3
"""D008 original diagnostic, actual immutable markup only. No PDF or gate closure."""
from pathlib import Path
from collections import Counter
from html.parser import HTMLParser
import sys,json,re,hashlib,urllib.request,urllib.parse,concurrent.futures,datetime
from lxml import html
ROOT=Path(__file__).parent
PREP=ROOT.parents[1]/'d008-render-review-prep/review_helpers.py'
sys.path.insert(0,str(PREP.parent));import review_helpers as h
sys.path.insert(0,'/workspace/scratch/ac36b9c5ff31/PROF-repo/runs/y1-reader-20261008/tooling/frozen-render-review');import frozen_render_review as base
sha=lambda b:hashlib.sha256(b).hexdigest()
def save(name,obj):
 with (ROOT/name).open('x') as f:json.dump(obj,f,ensure_ascii=False,indent=2);f.write('\n')
def norm(s):return re.sub(r'\s+',' ',s).strip()
source_bytes=(ROOT/'teaching-original.md').read_bytes();source=source_bytes.decode('utf-8');page_bytes=(ROOT/'github-page.html').read_bytes()
embedded=base.EmbeddedData();embedded.feed(page_bytes.decode('utf-8'));data=json.loads(''.join(embedded.parts));save('embedded-data.json',data)
identity=h.destination_identity(data,source_bytes,'e0f87210f8085487a1fb6e29bb4ca821cadca5e5','runs/y1-reader-20261008/iterations/008/author-work-r14/teaching-original.md','006fe68f52c3a4c9177f2da4fbddc5a06823314b49e4e1ac482f23a5cc169ae9');save('source-identity.json',identity)
article_html=data['payload']['codeViewBlobRoute']['richText'];(ROOT/'github-article.html').write_text(article_html)
article=h.DestinationArticle();article.feed(article_html)
sm=h.math_tokens(source);gm=article.math_payloads();math_compare=h.compare_math(sm,gm);save('math-comparison.json',math_compare);save('source-math.json',sm);save('github-math.json',gm)
# Protect all TeX before Markdown-link parsing so [..](..) in TeX cannot become a false link.
render_math=[]
def protect(m):
 i=len(render_math);fmt=next(x for x in ['fence','protected','display','inline'] if m.group(x) is not None);payload=m.group(fmt+'_body');wrap='$$' if fmt in ['fence','display'] else '$';render_math.append(wrap+payload+wrap);return f'PROF_MATH_TOKEN_{i}_END'
protected=h.MATH.sub(protect,source)
anchor_pattern=re.compile(r'<a\s+(?:name|id)="([^"]+)"\s*></a>')
source_anchors=anchor_pattern.findall(protected)
source_links=re.findall(r'(?<!!)\[([^\]]+)\]\(([^)]+)\)',protected)
expected=re.sub(r'<!--\s*P\d+\s*-->','',protected);expected=anchor_pattern.sub('',expected);expected=re.sub(r'(?<!!)\[([^\]]+)\]\(([^)]+)\)',lambda m:m[1],expected)
expected=re.sub(r'PROF_MATH_TOKEN_(\d+)_END',lambda m:render_math[int(m[1])],expected)
actual=''.join(article.text)
(ROOT/'expected-prose-math-stream.txt').write_text(norm(expected)+'\n');(ROOT/'actual-prose-math-stream.txt').write_text(norm(actual)+'\n')
source_prose=h.MATH.sub(' MATH_PAYLOAD ',source);source_prose=re.sub(r'<!--\s*P\d+\s*-->','',source_prose);source_prose=anchor_pattern.sub('',source_prose);source_prose=re.sub(r'(?<!!)\[([^\]]+)\]\(([^)]+)\)',lambda m:m[1],source_prose)
# Source has only the documented dollar forms; normalize destination text similarly for prose-only check.
actual_prose=re.sub(r'\$\$(.*?)\$\$|(?<!\$)\$(?!\$)(.*?)(?<!\$)\$(?!\$)',' MATH_PAYLOAD ',actual,flags=re.S)
map_rows=[{'label':f'A{i}','task':f'a{i}','hint':f'h{i}','solution':f's{i}'} for i in range(1,5)]
relationships=h.check_task_relationships(article,map_rows)
# Include solution->own hint and hint->own solution relationships explicitly.
for row in relationships:
 mp=row['mapping'];sects=row['section_links'];row['solution_to_hint']=any(x['href']=='#'+mp['hint'] for x in (sects['solution'] or []));row['hint_to_solution']=any(x['href']=='#'+mp['solution'] for x in (sects['hint'] or []))
targets=[]
for t in article.targets:
 key=(t['element'],t['value'])
 if key not in [(x['element'],x['value']) for x in targets]:targets.append(t)
internal=[x for x in article.links if x['href'].startswith('#')]
checks={'complete_prose_and_math_stream':norm(expected)==norm(actual),'prose_outside_math_exact':norm(source_prose)==norm(actual_prose),'all_numeric_tokens_in_order':re.findall(r'\d+(?:\.\d+)?',expected)==re.findall(r'\d+(?:\.\d+)?',actual),'all_math_exact':math_compare['exact_all'],'all_source_links_in_order':source_links==[(x['text'],x['href']) for x in article.links],'all_source_targets_in_order':[x['value'] for x in targets]==['user-content-'+x for x in source_anchors],'each_internal_target_once':all(len(article.target_elements('user-content-'+x['href'][1:]))==1 for x in internal),'all_four_task_relationships':all(all(row[k] for k in ['task_to_hint','task_to_solution','hint_to_task','solution_to_task','solution_to_hint','hint_to_solution']) and all(n==1 for n in row['target_element_counts'].values()) for row in relationships),'all_tasks_before_all_hints_before_all_solutions':max(source_anchors.index(f'a{i}') for i in range(1,5))<min(source_anchors.index(f'h{i}') for i in range(1,5)) and max(source_anchors.index(f'h{i}') for i in range(1,5))<min(source_anchors.index(f's{i}') for i in range(1,5)),'P001_P145_in_order':h.LABEL.findall(source)==[f'P{i:03}' for i in range(1,146)],'no_heading_table_or_emphasis_tags':not any(article.tags[x] for x in ['h1','h2','h3','h4','h5','h6','b','strong','em','i','table','th','caption','figcaption']),'no_external_constituent_images':not any(e['tag']=='img' for e in article.elements)}
save('markup-navigation-audit.json',{'checks':checks,'tags':dict(article.tags),'source_math_count':len(sm),'github_math_counts':dict(Counter(x['type'] for x in gm)),'source_links':source_links,'destination_links':article.links,'source_anchors':source_anchors,'destination_targets':article.targets,'task_map':map_rows,'task_relationships':relationships,'internal_link_count':len(internal),'external_links':[x for x in article.links if not x['href'].startswith('#')],'normalization':'One ordinary HTMLParser parse with convert_charrefs=True. No html.unescape. Protect all TeX before stripping comments/anchors/Markdown-link syntax; preserve literal operator/entities; fold only prose stream whitespace. Math payloads separately exact. Source task text that is plain ASCII is compared as prose, not invented math markup.','limits':['Diagnostic original only; not final accepted teaching.','No browser, MathJax execution, click/scroll or computed-style observations.','No PDF, SASIS, scientific/source-content acceptance or final global gate.']})
# Localize independently by exact source offsets; equal lengths permit direct alignment.
localized=[]
if len(sm)==len(gm):
 for i,(s,g) in enumerate(zip(sm,gm),1):
  if (s['type'],s['payload'])!=(g['type'],g['payload']) or not g['wrapper_valid']:
   localized.append({'math_index':i,'paragraph':s['paragraph'],'source':s,'github':g})
save('localized-math-failures.json',{'equal_source_and_destination_counts':len(sm)==len(gm),'localized':localized,'exact_count':sum((s['type'],s['payload'])==(g['type'],g['payload']) and g['wrapper_valid'] for s,g in zip(sm,gm)) if len(sm)==len(gm) else None,'warning':'No direct positional defect count if wrappers are missing; use aligned math-comparison hunks.'})
doc=html.fromstring(page_bytes);adom=doc.xpath('//article')[0]
save('dom-structure.json',{'article_attrs':dict(adom.attrib),'article_elements':[{'tag':e.tag,'attrs':dict(e.attrib)} for e in adom.iter()],'ancestors':[{'tag':e.tag,'attrs':dict(e.attrib)} for e in adom.iterancestors()],'inline_styles':[{'tag':e.tag,'style':e.get('style')} for e in [*adom.iter(),*adom.iterancestors()] if e.get('style')],'style_blocks':[e.text for e in doc.xpath('//style')],'server_DOM_article_text_equals_richText':norm(''.join(adom.itertext()))==norm(actual)})
links=[dict(e.attrib) for e in doc.xpath('//link[@rel="stylesheet"]')];base_url=json.loads((ROOT/'fetch-records.json').read_text())['github-page.html']['final_url'];urls=list(dict.fromkeys(urllib.parse.urljoin(base_url,e['href']) for e in links if 'href'in e));cssroot=ROOT/'current-css';cssroot.mkdir(exist_ok=True)
def get(item):
 i,url=item;path=cssroot/f'{i:02}-{url.rsplit("/",1)[-1]}'
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'PROF immutable representation review'}),timeout=50) as f:b=f.read();status=f.status;final=f.url
  with path.open('xb') as f:f.write(b)
  return {'url':url,'final_url':final,'status':status,'path':str(path.relative_to(ROOT)),'bytes':len(b),'sha256':sha(b),'fetched_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 except Exception as exc:return {'url':url,'error':repr(exc)}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:fetches=list(pool.map(get,enumerate(urls,1)))
save('current-css-inventory.json',{'page_sha256':sha(page_bytes),'links':links,'fetches':fetches,'prior_css_reused':False})
print(json.dumps({'identity':identity,'checks':checks,'source_math_count':len(sm),'github_math_count':len(gm),'localized_failures':len(localized),'CSS_count':len(fetches),'CSS_errors':[x for x in fetches if 'error'in x]},ensure_ascii=False))
