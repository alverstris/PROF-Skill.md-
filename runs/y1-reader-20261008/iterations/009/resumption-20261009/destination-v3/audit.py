from pathlib import Path
import importlib.util,json,re,hashlib,difflib
from html.parser import HTMLParser
class Page(HTMLParser):
 def __init__(self):super().__init__();self.active=False;self.parts=[];self.css=[]
 def handle_starttag(self,t,a):
  a=dict(a)
  if t=="script" and a.get("data-target")=="react-app.embeddedData":self.active=True
  if t=="link" and a.get("rel")=="stylesheet":self.css.append(a.get("href"))
 def handle_endtag(self,t):
  if t=="script":self.active=False
 def handle_data(self,d):
  if self.active:self.parts.append(d)
base=Path(__file__).resolve().parent
repo=base.parents[5]
helper=repo/'runs/y1-reader-20261008/iterations/008/render-evidence/r15-v2/dependency-review_helpers.py'
spec=importlib.util.spec_from_file_location('h',helper);h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
source=base.parent/'author/teaching-r15-recovery-v3.md';s=source.read_text();p=(base/'github-page.html').read_bytes();soup=Page();soup.feed(p.decode());data=json.loads(''.join(soup.parts))
article=data['payload']['codeViewBlobRoute']['richText'];h.preserve_new(base/'github-article.html',article)
a=h.DestinationArticle();a.feed(article)
tokens=h.math_tokens(s)
for t in tokens:
 labels=re.findall(r'^(P\d+)\.',s[:t['span'][0]],re.M);t['paragraph']=labels[-1] if labels else None
actual=a.math_payloads();comp=h.compare_math(tokens,actual)
def save(name,v):h.preserve_new(base/name,json.dumps(v,ensure_ascii=False,indent=2)+'\n')
save('source-math.json',tokens);save('destination-math.json',actual);save('math-comparison.json',comp)
commit='9840e70de6aa7d2c718b60dd13ace7e6f795a50e';path=str(source.relative_to(repo))
identity=h.destination_identity(data,source.read_bytes(),commit,path,'5c9e307b08931099316a2d12149ab3d1cd3a75ba2ae75bc48ef60a77b562c244');save('destination-identity.json',identity)
# Keep TeX protected while deleting Markdown representation syntax.
protected=[]
def protect(m):
 token=tokens[len(protected)];d='$$' if token['type']=='js-display-math' else '$';protected.append(d+token['payload']+d);return 'MATHPLACEHOLDER'+str(len(protected)-1)+'END'
expected=h.MATH.sub(protect,s);expected=re.sub(r'<a name="[^"]+"></a>','',expected);expected=re.sub(r'!\[[^\]]*\]\([^)]*\)','',expected);expected=re.sub(r'\[([^\]]*)\]\([^)]*\)',r'\1',expected);expected=re.sub(r'MATHPLACEHOLDER(\d+)END',lambda m:protected[int(m[1])],expected)
norm=lambda x:re.sub(r'\s+',' ',x).strip();expected=norm(expected);actual_text=norm(''.join(a.text))
h.preserve_new(base/'expected-prose-math-stream.txt',expected+'\n');h.preserve_new(base/'actual-prose-math-stream.txt',actual_text+'\n')
changes=[{'operation':op,'expected':expected[i:j],'actual':actual_text[k:l],'expected_context':expected[max(0,i-75):j+75]} for op,i,j,k,l in difflib.SequenceMatcher(a=expected,b=actual_text,autojunk=False).get_opcodes() if op!='equal']
save('prose-comparison.json',{'exact_after_whitespace_folding':expected==actual_text,'changes':changes,'source_paragraph_labels':re.findall(r'^P\d+\.',s,re.M),'actual_paragraph_labels':re.findall(r'P\d+\.',actual_text)})
taskmap=[{'label':x.upper(),'task':'task-'+x,'hint':'hint-'+x,'solution':'solution-'+x} for x in 'abc'];relations=h.check_task_relationships(a,taskmap);save('navigation.json',{'relationships':relations,'targets':a.targets,'links':a.links})
save('image-markup.json',[i['attrs'] for i in a.elements if i['tag']=='img']);save('element-style-evidence.json',{'tags':a.tags,'inline_styles':a.inline_styles,'elements':a.elements,'css_urls':soup.css})
print(json.dumps({'identity':identity,'math':{'count':comp['source_count'],'dest':comp['destination_count'],'exact':comp['exact_all'],'hunks':comp['aligned_difference_hunks']},'prose_exact':expected==actual_text,'prose_changes':changes,'tags':a.tags},indent=2))
