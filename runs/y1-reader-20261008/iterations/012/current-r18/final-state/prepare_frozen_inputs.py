from pathlib import Path
import hashlib,json,shutil,datetime
repo=Path(__file__).resolve().parents[6]
base=Path(__file__).resolve().parent.parent
out=base/'final-state'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def info(p): return {'path':str(p.relative_to(repo)),'bytes':p.stat().st_size,'sha256':sha(p)}
def save(p,d): p.write_text(json.dumps(d,indent=2)+'\n')
author=base/'author'; m=json.loads((author/'.prof-state/manifest.json').read_text())
originals=sorted(p for p in (author/'.prof-state').rglob('*') if p.is_file())+[author/'helper-checks-v1.json']
before=[info(p) for p in originals]
controls=[repo/'SKILL.md',repo/'runs/y1-reader-20261008/requests.md',repo/'scripts/prof_state.py']
controls += [Path(s['path']) for s in m['sources'] if s['id'] not in ['lecture','source-record','baseline-record']]
rows=[]
for p in controls:
 dest=out/'inputs'/p.relative_to(repo); dest.parent.mkdir(parents=True,exist_ok=True)
 if dest.exists(): assert dest.read_bytes()==p.read_bytes(),str(dest)
 else: shutil.copyfile(p,dest)
 rows.append({'original':info(p),'frozen':info(dest),'identical':True})
assert sha(repo/'SKILL.md')=='ffc6366348e1a9aa97f85adb0a6402b43c2a2c9532e994b3c947e086e0039394'
assert sha(repo/'references/sasis/ocr-baseline-20261007/student-baseline.txt')=='3749d2e59631b7981e2dcdf3ec05225a0f375d93728b593ccef44fae916942e5'
save(out/'incoming-inputs-inventory.json',{'status':'frozen incoming controls only; no acceptance claim','files':rows})
publication=json.loads((base/'packet-publication-readback-v1.json').read_text()); checks=[]
for r in publication['verified_local_blob_ids']:
 p=repo/r['path']; b=p.read_bytes(); blob=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
 checks.append({'path':r['path'],'actual_git_blob':blob,'expected_git_blob':r['sha'],'bytes':len(b),'match':blob==r['sha'] and len(b)==r['size']})
assert len(checks)==32 and all(r['match'] for r in checks)
save(out/'publication-local-revalidation-v1.json',{'commit':publication['commit'],'scope':'All 32 saved remote-readback entries recomputed against actual local bytes; this author did not independently request the remote tree again. No destination render claim.','checks':checks})
evidence_names=['root-technical-review-v1.md','root-sasis-disposition-v1.md','sasis-reader-v1-original.md','root-presolution-record.json','root-presolution-review.md','root-source-review.md','root-source-calculations.json','root-ellipse-optics-verification.md','root-v1-extra-calculations.json','packet-publication-readback-v1.json','sasis-admission-v1.json','author/packet-v1.json','author/author-audit-v1.md','author/source-coverage-v1.md','author/baseline-access.json','author/technical-checks-v1.json','author/technical_checks.py','author/helper-checks-v1.json']
save(out/'evidence-inventory-v1.json',{'scope':'Reconciled v1 evidence identities; read chronology is in author records and reconciliation. Frozen v1 content reviews do not close destination or a future v2.','files':[info(base/n) for n in evidence_names]})
after=[info(p) for p in originals]; assert before==after
save(out/'original-author-state-preservation.json',{'before':before,'after':after,'unchanged':True})
print(json.dumps({'frozen_inputs':len(rows),'publication_blobs_revalidated':len(checks),'original_author_state_unchanged':True,'final_acceptance':'pending; destination defect reported, consolidated review pending'},indent=2))
