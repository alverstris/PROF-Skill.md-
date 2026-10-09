from pathlib import Path
import sys,json,hashlib
p=Path("references/sasis/ocr-baseline-20261007/student-baseline.txt")
b=p.read_bytes(); lines=b.split(b"\n"); a,z=map(int,sys.argv[1:]); print("\n".join(f"{i}: "+lines[i-1].decode() for i in range(a,z+1)))
with Path("runs/y1-reader-20261008/iterations/011/current-r17/author/baseline-access.jsonl").open("a") as f:f.write(json.dumps({"range":[a,z],"physical_lf":True,"sha256":hashlib.sha256(b).hexdigest()})+"\n")
