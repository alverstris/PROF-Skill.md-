from pathlib import Path
import hashlib,json,subprocess,shutil,datetime

p=Path('/workspace/scratch/f9c0b7fc7e76/d016-published-r25')
bare=p/'current-verification.git'
plan=json.loads((p/'repair/publication-plan.json').read_text())
commit='a5e86eac9e9805921473419c48b329bde7bd46ec'
tree='d49885153f1a733f5fdbcb6558ef627a7ea5eccc'
def git(*args):return subprocess.check_output(['git','--git-dir='+str(bare),*args])
def sha(b):return hashlib.sha256(b).hexdigest()
def save(path,obj):path.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n')
assert git('rev-parse','FETCH_HEAD').decode().strip()==commit
assert git('rev-parse',commit+'^{tree}').decode().strip()==tree
records=[]
for f in plan['files']:
    b=git('show',commit+':'+f['path'])
    assert len(b)==f['bytes'] and sha(b)==f['sha256']
    assert b==Path(f['local_path']).read_bytes()
    actual_blob=git('rev-parse',commit+':'+f['path']).decode().strip()
    assert actual_blob==f['git_blob']
    records.append({'path':f['path'],'bytes':len(b),'sha256':sha(b),'git_blob':actual_blob,'exact_saved_bytes_match':True})
package=[]
for f in plan['all_36_package_expected']:
    b=git('show',commit+':'+f['path'])
    assert len(b)==f['bytes'] and sha(b)==f['sha256']
    package.append({'path':f['path'],'bytes':len(b),'sha256':sha(b),'git_blob':git('rev-parse',commit+':'+f['path']).decode().strip()})
freeze=json.loads((p/'freeze.json').read_text())
for f in freeze['files']:assert sha((p/'output'/f['path']).read_bytes())==f['sha256']
readback={'verified_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'repository':plan['repository'],'branch':'main','published_commit':commit,'published_tree':tree,'expected_parent':plan['expected_head'],'package_version':'2026-10-10-r26','publication_files':records,'package_files':package,'publication_file_count':len(records),'package_file_count':len(package),'all_exact':True,'frozen_r25_teaching_unchanged':True,'teaching_acceptance':'D016 remains pending complete fresh generation and all required checks. No acceptance or count increment.'}
save(p/'repair/publication-readback.json',readback)

new=p.parent/'d016-published-r26'
assert not new.exists()
(new/'inputs/prof').mkdir(parents=True)
for f in package:
    dest=new/'inputs/prof'/f['path'];dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_bytes(git('show',commit+':'+f['path']))
shutil.copytree(p/'inputs/source',new/'inputs/source')
shutil.copyfile(p/'source-sha-manifest.json',new/'source-sha-manifest.json')
source_manifest=json.loads((new/'source-sha-manifest.json').read_text())
source_files=source_manifest['files'] if isinstance(source_manifest,dict) else source_manifest
for f in source_files:
    dest=new/'inputs/source'/f['path']
    assert sha(dest.read_bytes())==f['sha256']
save(new/'package-sha-manifest.json',{'repository':plan['repository'],'branch':'main','package_commit':commit,'package_tree':tree,'version':'2026-10-10-r26','all_36_fetched_file_hashes_verified':True,'files':package})
save(new/'package-verification.json',{'actual_main_fetched':commit,'tree':tree,'version':'2026-10-10-r26','all_36_actual_files_verified':True,'source_packet_files_verified':len(source_files),'baseline_sha256':'3749d2e59631b7981e2dcdf3ec05225a0f375d93728b593ccef44fae916942e5','note':'Task-only operational identity record; no old teaching or report is included.'})
(new/'original-task.txt').write_text('Original operative user messages, as supplied by root:\n“could you continue the iteration scheme? apply SASIS. tell me what the scheme is before starting” (root already explained the scheme).\n“1: which PROF? PROF from where? 2: you are not to repair the document. you are to repair PROF always, to ensure that PROF knows what it should be doing 3: just push the revised PROF to github. then, from there, cleanse your memory other than the key aspects about what you\'re doing and the tasks you need to do, then go back to step 1”.\n\nBinding task constraints: canonical actual current main root PROF/supporting package at alverstris/PROF-Skill.md-. Complete source and complete frozen baseline admission before generation. Fresh author and fresh reader contexts without inherited history; instruction-confined access, no claim of erased pretraining. Complete repo-native GitHub Markdown teaching with necessary figures, examples, practice, separately grouped hints and full solutions. No bold or italic prose. Prompts-only to root immediately when finalized, before proposed solutions. Freeze every complete constituent unchanged; independent full SASIS and technical/source/PROF/destination audits. Every verified material failure is repaired in PROF, never by patching generated teaching. Publish revised package and verify actual saved bytes, then restart from original inputs in a fresh context. Preserve all147 stable IDs,76 eligible and71 excluded; current15 accepted61 remaining. No installed Windows skill edits, user-computer operations or automation changes. Coordinate sole publication ownership with root.\n')
handover=json.loads((p/'handover.json').read_text())
handover.update({'published_package_commit':commit,'published_package_tree':tree,'version':'2026-10-10-r26','packet':str(new),'output':str(new/'output'),'evidence_directory':'runs/y1-reader-20261008/iterations/016/published-r26-20261010/','original_task':'original-task.txt','package_verification':'package-verification.json'})
handover['access_and_ownership']=['Root assigns sole publisher ownership; no concurrent mutations. The prior coordinator returns ownership only after its readback evidence publication.','Published GitHub is canonical. Normal git push lacks credentials; authenticated GitHub connector mutations, binary-safe transport and expected-head guards are available.','The packet contains only the verified current package, original source, original operative task and task-only metadata. Do not read prior teaching, diagnoses, reports or detailed author reasoning before the whole fresh generation is frozen.','No schedule mutations, installed-skill edits or user-computer operation.','A prior destination preview was unavailable; actual new destination preservation, styling, visual and navigation checks remain required. Evidence-only main commits with identical36package bytes do not invalidate this pin.']
save(new/'handover.json',handover)
print(json.dumps({'published_commit':commit,'tree':tree,'publication_files_verified':len(records),'package_files_verified':len(package),'source_files_verified':len(source_files),'clean_packet':str(new),'handover':str(new/'handover.json')}))
