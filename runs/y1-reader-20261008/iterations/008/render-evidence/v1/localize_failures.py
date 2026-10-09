from pathlib import Path
import sys,json,re,hashlib,difflib
from lxml import html
ROOT=Path(__file__).parent;sys.path.insert(0,str(ROOT.parents[1]/'d008-render-review-prep'));import review_helpers as h
source=(ROOT/'teaching-original.md').read_bytes().decode('utf-8');data=json.loads((ROOT/'embedded-data.json').read_text());dom=html.fromstring(data['payload']['codeViewBlobRoute']['richText'])
blocks=re.split(r'<!--\s*(P\d+)\s*-->',source)[1:];blocks=list(zip(blocks[::2],blocks[1::2]));paragraphs=dom.xpath('./p');assert len(blocks)==len(paragraphs)==145
records=[];counts={'exact':0,'changed_payload':0,'unwrapped':0,'extra_wrapper':0,'entity_payload':0,'lost_thinspace':0};failures=[]
for (label,block),p in zip(blocks,paragraphs):
 sm=h.math_tokens(block);gm=[]
 for e in p.xpath('.//math-renderer'):
  text=''.join(e.itertext());typ=e.get('class');width=2 if typ=='js-display-math' else 1;gm.append({'type':typ,'payload':text[width:-width],'raw_text':text})
 pairs=[(m['type'],m['payload']) for m in sm];actual=[(m['type'],m['payload']) for m in gm];rec={'paragraph':label,'source_count':len(sm),'destination_count':len(gm),'source_math':sm,'destination_math':gm,'exact_all':pairs==actual};records.append(rec)
 for op,a,b,c,d in difflib.SequenceMatcher(a=pairs,b=actual,autojunk=False).get_opcodes():
  if op=='equal':counts['exact']+=b-a;continue
  if op=='delete':counts['unwrapped']+=b-a
  elif op=='insert':counts['extra_wrapper']+=d-c
  elif op=='replace':
   counts['changed_payload']+=min(b-a,d-c);counts['unwrapped']+=max(0,(b-a)-(d-c));counts['extra_wrapper']+=max(0,(d-c)-(b-a))
   for s,g in zip(sm[a:b],gm[c:d]):
    if '&lt;' in g['payload'] or '&gt;' in g['payload']:counts['entity_payload']+=1
    if s['payload'].count('\\,')>g['payload'].count('\\,'):counts['lost_thinspace']+=s['payload'].count('\\,')-g['payload'].count('\\,')
  failures.append({'paragraph':label,'operation':op,'source_math_range':[a,b],'destination_math_range':[c,d],'source_math':sm[a:b],'destination_math':gm[c:d],'actual_paragraph_text':''.join(p.itertext()) if op in ['delete','insert'] or (b-a)!=(d-c) else None,'paragraph_links':[dict(x.attrib)|{'text':''.join(x.itertext())} for x in p.xpath('.//a[@href]')]})
result={'source_math_count':sum(x['source_count'] for x in records),'destination_math_count':sum(x['destination_count'] for x in records),'counts':counts,'failures':failures,'paragraphs_with_math_failure':[x['paragraph'] for x in records if not x['exact_all']],'normalization':'One independent ordinary lxml parse of original richText, no recursive entity unescape. Per-paragraph alignment prevents a missing wrapper from shifting later comparisons. Exact syntax/payload comparison, not mathematical equivalence.'}
(ROOT/'paragraph-math-comparison.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n');(ROOT/'localized-destination-failures.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(result,ensure_ascii=False,indent=2))
