#!/usr/bin/env python3
"""Narrow audit for normal dollar math and invisible P001-P194 comments.
No extra HTML entity decoding: article is fed through HTMLParser once.
"""
from pathlib import Path
import json,re,hashlib,sys,datetime,urllib.request,concurrent.futures
from html.parser import HTMLParser
from collections import Counter
from lxml import html
ROOT=Path(__file__).parent
HELPER=Path('/workspace/scratch/ac36b9c5ff31/PROF-repo/runs/y1-reader-20261008/tooling/frozen-render-review/frozen_render_review.py')
sys.path.insert(0,str(HELPER.parent))
import frozen_render_review as f
def save(n,x): (ROOT/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def sha(x):return hashlib.sha256(x).hexdigest()
def norm(s):return re.sub(r'\s+',' ',s).strip()
source_bytes=(ROOT/'teaching-v3.md').read_bytes(); source=source_bytes.decode()
page=(ROOT/'generic-markup/github-page.html').read_bytes()
emb=f.EmbeddedData();emb.feed(page.decode()); data=json.loads(''.join(emb.parts))
payload=data['payload']; route=payload['codeViewBlobRoute']
save('embedded-data.json',data)
article_html=route['richText']; article=f.Article();article.feed(article_html)
pat=re.compile(r'\$\$(.*?)\$\$|(?<!\$)\$(?!\$)(.*?)(?<!\$)\$(?!\$)',re.S)
smaths=[{'type':'js-display-math' if m[1] is not None else 'js-inline-math','text':m[0],'payload':m[1] if m[1] is not None else m[2]} for m in pat.finditer(source)]
gm=[{**m,'payload':m['text'][2:-2] if m['type']=='js-display-math' else m['text'][1:-1]} for m in article.maths]
# Strip only nonvisible comments, HTML anchor markup, Markdown links and list markers.
# Preserve all math delimiters/payloads and prose punctuation; whitespace-only folding.
expected=re.sub(r'<!-- P\d{3} -->','',source)
expected=re.sub(r'<a id="[^"]+"></a>','',expected)
expected=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',lambda m:m[1],expected)
expected=re.sub(r'^- ', '',expected,flags=re.M)
actual=''.join(article.text)
(ROOT/'expected-prose-stream.txt').write_text(norm(expected)+'\n')
(ROOT/'actual-prose-stream.txt').write_text(norm(actual)+'\n')
rawlines=payload['codeViewBlobLayoutRoute.StyledBlob']['rawLines']; raw='\n'.join(rawlines).encode()
layout=payload['codeViewLayoutRoute'];blobroute=payload['codeViewBlobLayoutRoute']
identity={'source_bytes':len(source_bytes),'source_sha256':sha(source_bytes),'source_expected_identity':len(source_bytes)==28777 and sha(source_bytes)=='311afdef083a4468f18bcdd11a68975d2e6622661e0be3405a5c9f58b3f3a813','layout_path':layout['path'],'layout_refInfo':layout['refInfo'],'blob_path':blobroute['path'],'blob_refInfo':blobroute['refInfo'],'embedded_raw_lines_rejoined_bytes':len(raw),'embedded_raw_lines_plus_terminal_newline_exact':raw+b'\n'==source_bytes,'richTextTruncated':route['richTextTruncated'],'helper_sha256':sha(HELPER.read_bytes()),'raw_fetch':json.loads((ROOT/'generic-markup/source-fetch.json').read_text())}
save('source-identity.json',identity)
source_ids=re.findall(r'<a id="([^"]+)"></a>',source)
source_links=re.findall(r'\[([^\]]+)\]\(([^)]+)\)',source)
anchors={};pending=[]
for p in article.paragraphs:
 pending+=p['ids']
 if p['text'].strip():
  for a in pending:anchors[a]=p['text']
  pending=[]
nav=[]
for n in range(1,7):
 task=f'task-a{n}';hint=f'hint-a{n}';sol=f'solution-a{n}'
 nav.append({'task':f'A{n}','task_target_text':anchors.get('user-content-'+task),'hint_target_text':anchors.get('user-content-'+hint),'solution_target_text':anchors.get('user-content-'+sol),'all_targets_once':all(article.ids.count('user-content-'+v)==1 for v in [task,hint,sol]),'task_to_hint':sum(l=={'href':'#'+hint,'text':f'Hint A{n}'} for l in article.links)==2,'task_to_solution':sum(l=={'href':'#'+sol,'text':f'Solution A{n}'} for l in article.links)==1,'return_links':sum(l=={'href':'#'+task,'text':f'Return to A{n}'} for l in article.links),'target_order':[source_ids.index(x) for x in [task,hint,sol]]})
checks={'complete_prose_and_math_stream_after_only_documented_markup_and_whitespace_normalization':norm(expected)==norm(actual),'every_math_payload_and_wrapper_exact_after_one_HTML_parse':smaths==gm,'all_inline_math_exact':[x for x in smaths if x['type']=='js-inline-math']==[x for x in gm if x['type']=='js-inline-math'],'all_display_math_exact_including_internal_newlines':[x for x in smaths if x['type']=='js-display-math']==[x for x in gm if x['type']=='js-display-math'],'all_source_link_texts_and_hrefs_in_order':source_links==[(x['text'],x['href']) for x in article.links],'all_source_anchor_ids_in_order':article.ids==['user-content-'+s for s in source_ids],'all_internal_destinations_once':all(article.ids.count('user-content-'+x['href'][1:])==1 for x in article.links if x['href'].startswith('#')),'all_tasks_before_all_hints_before_all_solutions':max(source_ids.index('task-a'+str(i)) for i in range(1,7))<min(source_ids.index('hint-a'+str(i)) for i in range(1,7)) and max(source_ids.index('hint-a'+str(i)) for i in range(1,7))<min(source_ids.index('solution-a'+str(i)) for i in range(1,7)),'all_P001_P194_source_comments_in_order':re.findall(r'<!-- (P\d{3}) -->',source)==[f'P{i:03}' for i in range(1,195)],'no_heading_or_emphasis_or_table_or_caption_DOM':not any(article.tags[t] for t in ['h1','h2','h3','h4','h5','h6','b','strong','em','i','table','th','caption','figcaption']),'no_external_assets':not article.images}
save('scoped-markup-navigation-audit.json',{'checks':checks,'tags':dict(article.tags),'math_counts':dict(Counter(m['type'] for m in gm)),'source_math':smaths,'github_math':gm,'math_mismatches':[{'index':i,'source':s,'github':g} for i,(s,g) in enumerate(zip(smaths,gm),1) if s!=g],'source_anchor_ids':source_ids,'github_anchor_ids':article.ids,'anchors_to_visible_paragraphs':anchors,'links':article.links,'external_links':[l for l in article.links if not l['href'].startswith('#')],'tasks':nav,'fragment_semantics':'GitHub sanitizes id to user-content-* while href stays #*. All literal prefixed targets exist exactly once. Client click/scroll translation is not observed.','normalization':'One ordinary HTMLParser parse with convert_charrefs=True. No html.unescape or recursive entity decoding. Complete source stream strips only invisible comments, exact anchor markup, Markdown link wrappers and list marker prefix; then folds whitespace. Per-math equality is exact including display newlines.','limitations':['No live pixels, MathJax execution, computed styles, browser clicks or client JavaScript observed.','This is a representation/navigation/typography review, not SASIS or global teaching acceptance.']})
doc=html.fromstring(page);article_dom=doc.xpath('//article')[0]
save('dom-structure.json',{'article_attrs':dict(article_dom.attrib),'all_article_elements':[{'tag':e.tag,'attrs':dict(e.attrib)} for e in article_dom.iter()],'ancestors':[{'tag':e.tag,'attrs':dict(e.attrib)} for e in article_dom.iterancestors()],'server_DOM_article_text_equals_embedded_article_text':norm(''.join(article_dom.itertext()))==norm(actual),'inline_styles':[{'tag':e.tag,'style':e.get('style')} for e in [*article_dom.iter(),*article_dom.iterancestors()] if e.get('style')],'page_style_blocks':[e.text for e in doc.xpath('//style')]})
# Every exact href-linked current stylesheet, plus data-href inventory (inactive theme assets).
links=[dict(e.attrib) for e in doc.xpath('//link[@rel="stylesheet"]')]
cssroot=ROOT/'current-css';cssroot.mkdir(exist_ok=True)
urls=list(dict.fromkeys(e['href'] for e in links if 'href'in e))
def get(item):
 i,url=item;path=cssroot/f'{i:02}-{url.rsplit("/",1)[-1]}'
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'PROF immutable destination rendering audit'})
  with urllib.request.urlopen(req,timeout=50) as r: body=r.read();status=r.status;final=r.url
  path.write_bytes(body)
  return {'url':url,'final_url':final,'status':status,'path':str(path.relative_to(ROOT)),'bytes':len(body),'sha256':sha(body),'current_fetch_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 except Exception as exc:return {'url':url,'error':repr(exc)}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool: records=list(pool.map(get,enumerate(urls,1)))
save('current-css-inventory.json',{'page_sha256':sha(page),'links':links,'fetches':records,'prior_css_reused':False})
print(json.dumps({'identity':identity,'checks':checks,'math_counts':dict(Counter(m['type'] for m in gm)),'css_fetches':len(records),'css_errors':[r for r in records if 'error'in r]},ensure_ascii=False))
