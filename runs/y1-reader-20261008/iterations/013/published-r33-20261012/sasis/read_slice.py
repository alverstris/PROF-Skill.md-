from pathlib import Path
import sys,json,hashlib,datetime
out=Path(__file__).parent
path=Path(sys.argv[1]); start=int(sys.argv[2]); end=int(sys.argv[3]); label=sys.argv[4]
with path.open('rb') as f:
 f.seek(start); b=f.read(end-start)
r={'event':'text_read','label':label,'path':str(path),'range':[start,start+len(b)],'requested_range':[start,end],'sha256':hashlib.sha256(b).hexdigest(),'clipping':False,'recovery':None,'order_deviation':False,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
with (out/'access-log.jsonl').open('a') as f:f.write(json.dumps(r)+'\n')
print(json.dumps(r))
print(b.decode('utf-8'),end='')
