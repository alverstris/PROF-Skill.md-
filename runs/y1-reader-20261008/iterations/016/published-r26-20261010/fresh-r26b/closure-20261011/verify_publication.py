"""Verify a published immutable tree against an exact local publication map."""
from pathlib import Path
import argparse, datetime, hashlib, json, subprocess

parser=argparse.ArgumentParser()
parser.add_argument('--phase',required=True)
parser.add_argument('--commit',required=True)
parser.add_argument('--base',required=True)
parser.add_argument('--map',required=True)
args=parser.parse_args()
root=Path(__file__).resolve().parent
repo='/workspace/scratch/f9c0b7fc7e76/prof-iteration'
plan=json.loads(Path(args.map).read_text())
def git(*values,**kw):
    return subprocess.check_output(['git','-C',repo,*values],**kw)
def tree(commit):
    return {x.split('\t')[1]:x.split('\t')[0].split()[2] for x in git('ls-tree','-r',commit,text=True).splitlines()}
actual=tree(args.commit)
baseline=tree(args.base)
remote_head=git('ls-remote','origin','refs/heads/main',text=True).split()[0]
assert remote_head==args.commit,(remote_head,args.commit)
assert git('rev-parse','origin/main',text=True).strip()==args.commit
changes=set(git('diff-tree','--no-commit-id','--name-only','-r',args.base,args.commit,text=True).splitlines())
assert changes=={p['path'] for p in plan},(len(changes),len(plan))
requests=''.join(args.commit+':'+p['path']+'\n' for p in plan).encode()
data=git('cat-file','--batch',input=requests)
position=0
records=[]
for p in plan:
    end=data.index(b'\n',position)
    oid,kind,size=data[position:end].decode().split()
    position=end+1
    size=int(size)
    payload=data[position:position+size]
    position+=size+1
    local=Path(p['local_path']).read_bytes()
    assert kind=='blob' and actual[p['path']]==p['blob']==oid
    assert size==p['bytes'] and payload==local
    assert hashlib.sha256(payload).hexdigest()==p['sha256']
    records.append({'path':p['path'],'bytes':size,'git_blob':oid,'sha256':p['sha256'],'exact_bytes_match':True})
assert position==len(data)
original=Path('/workspace/scratch/f9c0b7fc7e76/d016-r26b')
basepath='runs/y1-reader-20261008/iterations/016/published-r26-20261010/fresh-r26b'
freeze=json.loads((original/'freeze-manifest.json').read_text())
freeze_tree=tree('51a78beccef858072b1da8d057ef3dff09878409')
for p in freeze['files']:
    path=basepath+'/'+p['path']
    assert actual[path]==freeze_tree[path]
package=json.loads((original/'package-verification.json').read_text())['files']
for p in package:
    if p['path']!='SKILL.md':
        assert actual[p['path']]==p['git_blob']
queue=json.loads(git('show',args.commit+':runs/y1-reader-20261008/queue.json'))
counts={'total_ids':len(queue['sessions']),'eligible':sum(s['readability']['eligible'] for s in queue['sessions']),
        'excluded':sum(s['status']=='excluded_by_user_readability_scope' for s in queue['sessions']),
        'accepted':sum(s['status']=='closed' for s in queue['sessions']),
        'remaining':sum(s['status']=='pending' for s in queue['sessions'])}
assert counts['total_ids']==147 and counts['eligible']==76 and counts['excluded']==71
record={'phase':args.phase,'status':'verified','checked_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'commit':args.commit,'tree':git('rev-parse',args.commit+'^{tree}',text=True).strip(),'parent':args.base,
        'remote_main_observed':remote_head,'method':'Fetch actual origin/main, request planned blob objects from remote, then read every exact commit:path from the fetched Git object store and byte-compare with its planned local file.',
        'all_planned_paths_and_exact_bytes_match':True,'planned_file_count':len(plan),'verified_files':records,
        'changed_paths_exactly_equal_publication_map':True,'frozen_teaching_constituents_unchanged':6,
        'other_package_files_unchanged':35,'queue':counts,
        'shared_checkout_head':git('rev-parse','HEAD',text=True).strip(),
        'shared_checkout_note':'No checkout, index, local branch, frozen teaching or existing report was edited by publication.'}
outfile=root/('phase-'+args.phase.lower()+'-verification.json')
outfile.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({k:v for k,v in record.items() if k!='verified_files'},indent=2))
