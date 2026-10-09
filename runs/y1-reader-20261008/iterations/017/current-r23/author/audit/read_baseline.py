from pathlib import Path
import sys,json,hashlib
p=Path(__file__).resolve().parent;r=json.loads((p/'baseline-ranges.json').read_text()); b=Path(r['path']).read_bytes(); i=int(sys.argv[1]);s,e=r['ranges'][i-1]; print(f'BASELINE chunk {i} bytes [{s},{e})');print(b[s:e].decode());
with (p/'baseline-access.jsonl').open('a') as f:f.write(json.dumps({'chunk':i,'start':s,'end':e,'sha256':hashlib.sha256(b[s:e]).hexdigest()})+'\n')
