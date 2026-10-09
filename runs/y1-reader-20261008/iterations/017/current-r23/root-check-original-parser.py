from pathlib import Path
from html.parser import HTMLParser
import re,json,hashlib,subprocess
BASE=Path(__file__).resolve().parent
class Math(HTMLParser):
 def __init__(self):
  super().__init__(convert_charrefs=True);self.nodes=[];self.current=None;self.em=[];self.inem=False
 def handle_starttag(self,t,attrs):
  a=dict(attrs)
  if t=='math-renderer':
   assert self.current is None
   self.current={'type':'display' if 'js-display-math' in a.get('class','') else 'inline','text':''}
  if t=='em':self.inem=True;self.em.append('')
 def handle_data(self,d):
  if self.current is not None:self.current['text']+=d
  if self.inem:self.em[-1]+=d
 def handle_endtag(self,t):
  if t=='math-renderer':
   v=self.current;delim='$$' if v['type']=='display' else '$';assert v['text'].startswith(delim) and v['text'].endswith(delim)
   v['payload']=v['text'][len(delim):-len(delim)];self.nodes.append(v);self.current=None
  if t=='em':self.inem=False
report=[];totalmissing=totalchanged=totallost=0
for name in ['lesson','hints','solutions']:
 source=(BASE/'author/learner'/f'{name}.md').read_text();raw=(BASE/'destination-v1'/name/'github-page.html').read_text()
 scripts=re.findall(r'<script([^>]*)>(.*?)</script>',raw,re.S)
 payload=next(json.loads(s) for attrs,s in scripts if 'data-target="react-app.embeddedData"' in attrs)
 rich=payload['payload']['codeViewBlobRoute']['richText'];assert rich==(BASE/'destination-v1'/name/'github-article.html').read_text()
 assert 'ae08f92832c91a7a5652ca874ffe807afedf38a9' in raw
 parser=Math();parser.feed(rich)
 expected=[]
 for m in re.finditer(r'\$\$(.*?)\$\$|\$([^$\n]+)\$',source,re.S):
  display=m.group(1) is not None;expected.append({'type':'display' if display else 'inline','payload':m.group(1) if display else m.group(2),'line':source.count('\n',0,m.start())+1})
 actual=parser.nodes;j=0;mapping=[]
 missing_payloads={'F(x)|_a^b','F(x)|_{x=a}^{x=b}'}
 for i,e in enumerate(expected):
  if name=='lesson' and e['payload'] in missing_payloads:
   mapping.append({'source_index':i+1,**e,'status':'missing_math_node','actual':None});totalmissing+=1;continue
  assert j<len(actual),(name,i,j)
  a=actual[j];assert e['type']==a['type'];assert a['payload']==e['payload'].replace('\\,',','),(name,i,j,e,a)
  changed=e['payload']!=a['payload'];lost=e['payload'].count('\\,') if changed else 0
  mapping.append({'source_index':i+1,**e,'actual_index':j+1,'actual_payload':a['payload'],'status':'changed_payload' if changed else 'exact','lost_backslashes':lost})
  j+=1;totalchanged+=int(changed);totallost+=lost
 assert j==len(actual)
 report.append({'file':name+'.md','source_count':len(expected),'actual_count':len(actual),'source_inline':sum(x['type']=='inline' for x in expected),'source_display':sum(x['type']=='display' for x in expected),'em_text':parser.em,'mapping':mapping,'raw_html_sha256':hashlib.sha256(raw.encode()).hexdigest()})
result={'condition':'Independent root implementation; source regex and embedded GitHub JSON extracted directly, stdlib HTMLParser exactly once. No second HTML unescape or reviewer parser imported. Same standard parser family is not an independent browser engine.','commit':'ae08f92832c91a7a5652ca874ffe807afedf38a9','total_source':sum(r['source_count'] for r in report),'total_actual':sum(r['actual_count'] for r in report),'missing':totalmissing,'changed':totalchanged,'lost_thinspace_backslashes':totallost,'full_map':report,'status':'FAIL actual destination preservation'}
(BASE/'root-original-parser-verification.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='full_map'},indent=2))
