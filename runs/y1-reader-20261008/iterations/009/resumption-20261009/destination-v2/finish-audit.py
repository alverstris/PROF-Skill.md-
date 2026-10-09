from pathlib import Path
from html.parser import HTMLParser
import json,re,hashlib
p=Path(__file__).parent;s=(p.parent/'author/teaching-r15-recovery-v2.md').read_text();expected=json.loads((p/'source-math.json').read_text());actual=json.loads((p/'destination-math.json').read_text())
# Full prose equality independent of every expression: replace math at each source/destination position.
ss=s
for i,t in reversed(list(enumerate(expected))):ss=ss[:t['span'][0]]+f'MATH_{i}_END'+ss[t['span'][1]:]
ss=re.sub(r'<a name="[^"]+"></a>','',ss);ss=re.sub(r'!\[[^\]]*\]\([^)]*\)','',ss);ss=re.sub(r'\[([^\]]*)\]\([^)]*\)',r'\1',ss)
class Prose(HTMLParser):
 def __init__(self):super().__init__(convert_charrefs=True);self.inside=False;self.out=[];self.i=0
 def handle_starttag(self,t,a):
  if t=='math-renderer':self.inside=True;self.out.append(f'MATH_{self.i}_END');self.i+=1
 def handle_endtag(self,t):
  if t=='math-renderer':self.inside=False
 def handle_data(self,d):
  if not self.inside:self.out.append(d)
a=Prose();a.feed((p/'github-article.html').read_text());norm=lambda x:re.sub(r'\s+',' ',x).strip();eq=norm(ss)==norm(''.join(a.out))
nav=json.loads((p/'navigation.json').read_text());targets={x['value']:x['element'] for x in nav['targets']};links=[x for x in nav['links'] if x['href'].startswith('#')];bad=[]
for i,(e,d) in enumerate(zip(expected,actual),1):
 if e['payload']!=d['payload']:bad.append({'ordinal':i,'paragraph':e['paragraph'],'source':e['payload'],'destination_parsed':d['payload']})
record={'prose_exact_after_math_replaced_with_positional_tokens_and_whitespace_folded':eq,'paragraph_labels_exact':re.findall(r'^P\d+\.',s,re.M)==re.findall(r'P\d+\.',norm(''.join(a.out))),'source_math_count':len(expected),'destination_math_count':len(actual),'inline_expression_mismatches':sum(d['type']=='js-inline-math' and e['payload']!=d['payload'] for e,d in zip(expected,actual)),'display_expression_mismatches':sum(d['type']=='js-display-math' and e['payload']!=d['payload'] for e,d in zip(expected,actual)),'exact_mismatches':bad,'internal_link_count':len(links),'all_internal_targets_unique':all(sum(1 for y in nav['targets'] if y['value']=='user-content-'+x['href'][1:])==1 for x in links),'hints_group_before_solutions':targets['user-content-hint-c']<targets['user-content-solutions'],'no_bold_or_italic_prose_tags':not any(t in json.loads((p/'element-style-evidence.json').read_text())['tags'] for t in ['b','i','em','strong','h1','h2','th']),'style_status':'Observed destination CSS body normal weight 400; no emphasis-bearing prose elements. No live computed-style or browser pixel observation.','preview_status':'Compiled internal PDF and raster pages exist but are NOT visually inspected; root requested stopping v2 preview after parsed-math blocker. No v2 preview pass claimed.','live_github_pixels':'UNOBSERVED'}
(p/'final-audit.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps({k:v for k,v in record.items() if k!='exact_mismatches'},indent=2))
