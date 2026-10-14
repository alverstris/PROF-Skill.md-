"""Extract immutable Git source paragraphs; no browser or destination checks."""
import datetime
import hashlib
import json
import pathlib
import re
import subprocess
from urllib.parse import quote, urljoin

OUT=pathlib.Path(__file__).resolve().parent
ROOT=OUT.parents[2]
REPO=ROOT/'.prof-maintenance/20261014/repository'
REMOTE='https://github.com/alverstris/PROF-Skill.md-'
TARGETS=[
 ('D005-H1','32c553f279ac1e5771ff05b78a9951cbff3fee38','runs/y1-reader-20261008/iterations/005/teaching-v2.md',190,'h1'),
 ('D007-P5','4765d39aa399a0a1ff09223cae21b15ce6c7f720','runs/y1-reader-20261008/iterations/007/published-r29-20261011/teaching/lesson.md',301,'p5'),
 ('D007-P3-hint','4765d39aa399a0a1ff09223cae21b15ce6c7f720','runs/y1-reader-20261008/iterations/007/published-r29-20261011/teaching/hints.md',21,'h3'),
 ('D007-P5-explanation','4765d39aa399a0a1ff09223cae21b15ce6c7f720','runs/y1-reader-20261008/iterations/007/published-r29-20261011/teaching/solutions.md',108,'s5'),
 ('D009-P062','9840e70de6aa7d2c718b60dd13ace7e6f795a50e','runs/y1-reader-20261008/iterations/009/resumption-20261009/author/teaching-r15-recovery-v3.md',227,None),
]
def git(*args):return subprocess.check_output(['git','-C',str(REPO),*args])
def sha(b):return hashlib.sha256(b).hexdigest()
def write(name,b): (OUT/name).write_bytes(b)
def ident(p):
 p=pathlib.Path(p);b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':sha(b)}
packets=[]
for pid,commit,path,line,anchor in TARGETS:
 tree=git('ls-tree',commit,'--',path).decode('utf-8').strip()
 mode,kind,blobpath=tree.split(' ',2);oid,listedpath=blobpath.split('\t',1)
 assert kind=='blob' and listedpath==path
 b=git('cat-file','blob',oid)
 assert b==git('cat-file','blob',commit+':'+path)
 assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==oid
 lines=b.splitlines(keepends=True)
 assert 1<=line<=len(lines)
 lo=hi=line-1
 while lo>0 and lines[lo-1].strip():lo-=1
 while hi+1<len(lines) and lines[hi+1].strip():hi+=1
 paragraph=b''.join(lines[lo:hi+1]);text=paragraph.decode('utf-8')
 assert text.strip() and not any(x.strip().startswith(b'```') for x in lines[lo:hi+1])
 start=sum(map(len,lines[:lo]));end=start+len(paragraph)
 url=REMOTE+'/blob/'+commit+'/'+quote(path,safe='/')
 before=b''.join(lines[:lo]).decode('utf-8')
 anchors=list(re.finditer(r'<a\s+id="([^"]+)"\s*></a>',before))
 nearest=anchors[-1].group(1) if anchors else None
 if anchor:assert anchor==nearest
 math=[];links=[];ordered=[]
 token=re.compile(r'\$`(?P<math>.*?)`\$|(?<!!)\[(?P<label>[^\]\n]+)\]\((?P<href>[^)\n]+)\)',re.S)
 for m in token.finditer(text):
  if m.group('math') is not None:
   item={'ordinal':len(math)+1,'payload':m.group('math'),'source':m.group(),'char_start':m.start(),'char_end':m.end()};math.append(item);ordered.append({'kind':'math',**item})
  else:
   href=m.group('href');label=m.group('label')
   item={'ordinal':len(links)+1,'label':label,'href':href,'immutable_resolved_url':urljoin(url,href),'source':m.group(),'char_start':m.start(),'char_end':m.end()};links.append(item);ordered.append({'kind':'plain_text_link',**item})
 assert text.count('$`')==len(math) and text.count('`$')==len(math)
 assert not any('$' in re.sub(r'\$`.*?`\$','',text,flags=re.S) for _ in [0])
 file=OUT/(pid+'.paragraph-source.txt');file.write_bytes(paragraph)
 packets.append({'packet_id':pid,'commit':commit,'repository_path':path,'git_mode':mode,'git_blob_oid':oid,'complete_blob_bytes':len(b),'complete_blob_sha256':sha(b),'requested_line':line,'paragraph_lines_one_based_inclusive':[lo+1,hi+1],'paragraph_byte_range_zero_based_half_open':[start,end],'paragraph_source_identity':ident(file),'paragraph_source':text,'immutable_browser_url':url,'immutable_source_line_url':url+f'#L{lo+1}'+(f'-L{hi+1}' if hi>lo else ''),'nearest_preceding_anchor':nearest,'immutable_nearby_anchor_url':url+'#'+nearest if nearest else None,'math_payloads_in_order':math,'plain_text_links_in_order':links,'combined_source_token_order':ordered})
record={'prepared_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'Five exact source paragraphs from specified accepted Git commits. Source inventory only: no browser use, rendered inspection, destination acceptance, or teaching modification. Paragraph identities include the original terminal LF. Git object OIDs validated independently using the Git blob header/hash rule. Line and byte ranges refer to complete immutable blobs.','packets':packets}
write('packets.json',(json.dumps(record,ensure_ascii=False,indent=2)+'\n').encode('utf-8'))
report=['Five immutable source paragraphs for actual GitHub boundary comparisons. No rendering or acceptance claim.','']
for p in packets:
 report += [p['packet_id'], '',f"Commit: {p['commit']}",f"Path: {p['repository_path']}",f"Line: {p['requested_line']}; Git blob: {p['git_blob_oid']}; complete-blob SHA256: {p['complete_blob_sha256']}",f"Browser: {p['immutable_browser_url']}",f"Source-line locator: {p['immutable_source_line_url']}",f"Nearby explicit anchor: {p['immutable_nearby_anchor_url']}",'','Complete paragraph source:','','```markdown',p['paragraph_source'].rstrip('\n'),'```','','Math payloads in order:','']
 for m in p['math_payloads_in_order']:report.append(f"{m['ordinal']}. `{m['payload']}`")
 report += ['','Adjacent plain-text links in source order:','']
 for l in p['plain_text_links_in_order']:report.append(f"- `{l['label']}` → `{l['href']}` → {l['immutable_resolved_url']}")
 report += ['']
write('PACKETS.md','\n'.join(report).encode('utf-8'))
print(json.dumps({'packets':len(packets),'math_payloads':sum(len(p['math_payloads_in_order']) for p in packets),'links':sum(len(p['plain_text_links_in_order']) for p in packets),'packet_summary':[{'id':p['packet_id'],'blob_oid':p['git_blob_oid'],'paragraph_bytes':p['paragraph_source_identity']['bytes'],'paragraph_sha256':p['paragraph_source_identity']['sha256'],'math':len(p['math_payloads_in_order']),'links':len(p['plain_text_links_in_order']),'nearest_anchor':p['nearest_preceding_anchor']} for p in packets],'packet_file':ident(OUT/'PACKETS.md')},indent=2))
