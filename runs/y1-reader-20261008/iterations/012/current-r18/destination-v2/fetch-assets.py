from pathlib import Path
import json,subprocess,concurrent.futures,hashlib
p=Path(__file__).resolve().parent
items=[]
for m in json.loads((p/'image-markup.json').read_text()):
 name=Path(m['src']).name;url='https://raw.githubusercontent.com'+m['src'].replace('/raw/','/')
 items.append((url,p/'figures'/name,'image'))
for url in dict.fromkeys(json.loads((p/'element-style-evidence.json').read_text())['css_urls']):
 if url:items.append((url,p/'css'/Path(url).name,'css'))
def get(it):
 url,dest,kind=it;dest.parent.mkdir(exist_ok=True);r=subprocess.run(['curl','-L','--fail','--max-time','55','--silent','--show-error',url,'-o',str(dest)],capture_output=True,text=True);v={'url':url,'file':str(dest.relative_to(p)),'kind':kind,'exit':r.returncode,'stderr':r.stderr}
 if r.returncode==0:
  v.update(bytes=dest.stat().st_size,sha256=hashlib.sha256(dest.read_bytes()).hexdigest())
  if kind=='image':v['exact_local_bytes']=dest.read_bytes()==(p.parent/'author/figures'/dest.name).read_bytes()
 return v
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:records=list(pool.map(get,items))
(p/'asset-fetch.json').write_text(json.dumps(records,indent=2)+'\n');print(json.dumps(records,indent=2))
