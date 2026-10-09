from pathlib import Path
import re,json,difflib
from lxml import html
r=Path(__file__).parent
s=(r/'teaching.md').read_text();d=json.loads((r/'embedded-data.json').read_text());a=html.fromstring(d['payload']['codeViewBlobRoute']['richText'])
pat=re.compile(r'\$\$(.*?)\$\$|(?<!\$)\$(?!\$)(.*?)(?<!\$)\$(?!\$)',re.S)
blocks=re.split(r'<!-- (P\d{3}) -->',s)[1:];source=list(zip(blocks[::2],blocks[1::2]));actual=a.xpath('./p');assert len(source)==len(actual)==165
out=[];records=[];total=0
for (label,block),p in zip(source,actual):
 sm=[{'type':'js-display-math' if m[1] is not None else 'js-inline-math','text':m[0],'payload':m[1] if m[1] is not None else m[2]} for m in pat.finditer(block)]
 gm=[]
 for e in p.xpath('.//math-renderer'):
  t=''.join(e.itertext());typ=e.get('class');gm.append({'type':typ,'text':t,'payload':t[2:-2] if typ=='js-display-math' else t[1:-1]})
 total+=len(sm)
 record={'paragraph':label,'source_math':sm,'github_math':gm,'source_count':len(sm),'github_count':len(gm),'exact':sm==gm};records.append(record)
 if sm!=gm:
  if len(sm)==len(gm):
   for i,(x,y) in enumerate(zip(sm,gm),1):
    if x!=y:out.append({'paragraph':label,'index_in_paragraph':i,'source':x,'github':y,'lost_thinspace_backslashes':x['payload'].count('\\,')-y['payload'].count('\\,')})
  else:out.append({'paragraph':label,'count_mismatch':True,'source_math':sm,'github_math':gm,'actual_full_paragraph':''.join(p.itertext())})
plain=lambda x:re.sub(r'\s+',' ',x).strip()
prose=[]
for (label,b),p in zip(source,actual):
 x=pat.sub(' MATH_PAYLOAD ',b);x=re.sub(r'<a name="[^"]+"></a>','',x);x=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',lambda m:m[1],x)
 # Replace each actual math-renderer with placeholder once; retain literal missed math as text.
 pc=html.fromstring(html.tostring(p,encoding='unicode'))
 for e in pc.xpath('.//math-renderer'):
  replacement=html.Element('span');replacement.text=' MATH_PAYLOAD ';replacement.tail=e.tail;e.getparent().replace(e,replacement)
 y=''.join(pc.itertext());prose.append({'paragraph':label,'exact_outside_wrapped_math':plain(x)==plain(y),'source':plain(x),'github':plain(y)})
result={'source_math_count':total,'github_math_count':sum(z['github_count'] for z in records),'source_paragraph_count':len(source),'github_paragraph_count':len(actual),'localized_failures':out,'paragraphs_with_changed_math':[z['paragraph'] for z in records if not z['exact']],'prose_mismatches':[z for z in prose if not z['exact_outside_wrapped_math']],'lost_thinspace_backslashes':sum(z.get('lost_thinspace_backslashes',0) for z in out),'limits':'One lxml HTML parse of richText for per-paragraph localization; no html.unescape. Prior primary HTMLParser audit is separately retained. Failed wrapper is retained as visible literal source text.'}
(r/'localized-destination-failures.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');(r/'paragraph-math-comparison.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
