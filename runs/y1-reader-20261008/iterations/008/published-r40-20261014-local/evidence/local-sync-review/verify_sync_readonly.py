"""Independent read-only current GitHub main / installed PROF status verification.

All writes are confined to this review directory. Nothing is installed/fetched
into the repository. Published package files are downloaded into memory only.
"""
import concurrent.futures
from datetime import datetime, timezone
import hashlib
import json
import re
import subprocess
import urllib.parse
import urllib.request
from pathlib import Path

ROOT=Path(__file__).resolve().parent
PROJECT=ROOT.parents[2]
MAINT=PROJECT/".prof-maintenance/20261014"
REPO=MAINT/"repository"
INSTALLED=Path("C:/Users/alver/.codex/skills/prof")


def git(*args):return subprocess.check_output(["git","-C",str(REPO),*args])
def sha(raw):return hashlib.sha256(raw).hexdigest()
def read(p):return json.loads(p.read_text(encoding="utf-8-sig"))
def save(name,data):(ROOT/name).write_text(json.dumps(data,indent=2)+"\n",encoding="utf-8")
def inventory(root):
    result={}
    for p in root.rglob("*"):
        assert not p.is_symlink() and not p.is_junction() and p.resolve().is_relative_to(root.resolve()),str(p)
        if p.is_file():result[p.relative_to(root).as_posix()]={"sha256":sha(p.read_bytes()),"bytes":p.stat().st_size}
    return result
def package_tree(commit):
    result={}
    for entry in filter(None,git("ls-tree","-rz",commit).split(b"\0")):
        meta,name=entry.split(b"\t",1);mode,kind,oid=meta.decode().split();name=name.decode()
        if name=="SKILL.md" or name.split("/")[0] in {"agents","assets","references","scripts"}:
            assert mode=="100644" and kind=="blob"
            result[name]=oid
    return result
def download(item):
    name,oid,commit=item
    url="https://raw.githubusercontent.com/alverstris/PROF-Skill.md-/"+commit+"/"+urllib.parse.quote(name,safe="/")
    req=urllib.request.Request(url,headers={"User-Agent":"PROF-read-only-sync-verification"})
    with urllib.request.urlopen(req,timeout=45) as response:
        raw=response.read()
    assert hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()==oid,"Published blob identity mismatch: "+name
    local=git("cat-file","blob",oid)
    assert local==raw,"Local immutable Git object differs from live published bytes: "+name
    return name,raw,url


def main():
    start=datetime.now(timezone.utc).isoformat()
    remote=git("remote","get-url","origin").decode().strip()
    assert remote=="https://github.com/alverstris/PROF-Skill.md-.git"
    main_before=git("ls-remote","origin","refs/heads/main").decode().split()[0]
    tree=package_tree(main_before)
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        fetched=list(pool.map(download,[(p,oid,main_before) for p,oid in sorted(tree.items())]))
    published={p:raw for p,raw,url in fetched}
    expected={p:{"sha256":sha(raw),"bytes":len(raw),"git_blob":tree[p]} for p,raw in sorted(published.items())}
    installed=inventory(INSTALLED)
    missing=sorted(set(expected)-set(installed));extra=sorted(set(installed)-set(expected))
    mismatch=[p for p in sorted(set(expected)&set(installed)) if installed[p]["sha256"]!=expected[p]["sha256"] or installed[p]["bytes"]!=expected[p]["bytes"]]
    version=re.search(r'^  version: "([^"]+)"',published["SKILL.md"].decode(),re.M).group(1)
    manifest= json.loads(published["references/sasis/profile-manifest.json"])
    base=INSTALLED/"references/sasis"
    checks=[(base/manifest["file_hashes_base_directory"]/p,h) for p,h in manifest["file_hashes"].items()]
    checks += [(base/p,h) for p,h in manifest["control_file_hashes"].items()]
    checks += [(base/e["path"],e["sha256"]) for e in manifest["subject_files"]]
    manifest_results=[]
    for p,h in checks:
        assert p.resolve().is_relative_to(INSTALLED.resolve())
        actual=sha(p.read_bytes());assert actual==h,str(p)
        manifest_results.append({"path":p.relative_to(INSTALLED).as_posix(),"expected_sha256":h,"actual_sha256":actual,"pass":True})
    installation=read(MAINT/"r40-installation-verification.json")
    publication=read(MAINT/"r40-published-package-readback.json")
    previous=read(MAINT/"installation-verification.json")
    publication_index=read(MAINT/"r40-publication-inputs.json")
    prior_package_paths={e["path"] for e in publication_index["package"]}
    assert set(tree)==prior_package_paths,"Current package inventory differs from recorded r40 package"
    published_hashes={p:s["sha256"] for p,s in expected.items()}
    assert published_hashes==installation["package_sha256"]==publication["package_sha256"]
    stage=Path(publication["stage"]);stage_inventory=inventory(stage)
    assert {p:s["sha256"] for p,s in stage_inventory.items()}==published_hashes
    backup=Path(installation["backup"]);backup_inventory=inventory(backup)
    previous_tree=package_tree(previous["published_package_commit"])
    previous_hashes={p:sha(git("cat-file","blob",oid)) for p,oid in previous_tree.items()}
    backup_hashes={p:s["sha256"] for p,s in backup_inventory.items()}
    assert backup_hashes==previous["package_sha256"]==previous_hashes
    assert set(backup_hashes)==set(published_hashes)
    backup_version=re.search(r'^  version: "([^"]+)"',(backup/"SKILL.md").read_text(),re.M).group(1)
    package_at_install=package_tree(installation["commit"])
    assert tree==package_at_install,"Root package Git blobs changed since r40 install"
    main_after=git("ls-remote","origin","refs/heads/main").decode().split()[0]
    assert main_after==main_before,"GitHub main changed during read-only check"
    assert not missing and not extra and not mismatch
    record_files=("r40-installation-verification.json","r40-published-package-readback.json","installation-verification.json","verify_and_sync_r40.py")
    evidence={"review_started_utc":start,"review_finished_utc":datetime.now(timezone.utc).isoformat(),"repository":remote,"main_commit_before":main_before,"main_commit_after":main_after,"live_network_method":"Read-only GitHub main ref followed by in-memory raw.githubusercontent.com downloads of every root package file at that immutable commit; Git blob identity and local object bytes verified.",
      "prof_version":version,"complete_package_files":len(expected),"package_boundary":"SKILL.md plus every tracked agents/, assets/, references/, scripts/ file; excludes prof.zip and runs/ per current sasis.md:25","installed_directory":str(INSTALLED),"installed_files":len(installed),"missing":missing,"extra":extra,"byte_mismatches":mismatch,"all_installed_bytes_equal_current_github_main":True,"operative_manifest_hash_checks":len(checks),"package_unchanged_since_install_commit":installation["commit"],"package_git_blobs_identical_since_install":True,
      "existing_install_record":{"commit":installation["commit"],"time":installation["verified_at"],"method":installation["method"],"rename_failure":installation["original_rename_failure"],"file_count":installation["installed_files_overwritten_and_verified"],"manifest_checks":installation["manifest_checks"]},
      "existing_publication_record":{"commit":publication["commit"],"file_count":publication["package_files"],"recorded_main_verified":publication["main_publication_verified"],"hash_inventory_matches_current_main":True},"retained_stage":{"path":str(stage),"files":len(stage_inventory),"complete_inventory_and_bytes_equal_current_main":True},
      "retained_backup":{"path":str(backup),"exists":True,"version":backup_version,"files":len(backup_inventory),"inventory_matches_current_package_paths":True,"complete_bytes_equal_prior_r39_install_record_and_published_package":True,"prior_published_commit":previous["published_package_commit"]},
      "sync_clauses":{"SKILL.md":[32,36],"references/sasis.md":[23,25,26,27,28,94],"behavior":"Pin current/just-published commit; stage the complete package; verify Git tree/bytes and operative manifests; preserve dated complete backup; replace whole installation. If directory rename is blocked, preserve failure and use every-file replacement only with exact equal inventories, verified backup, confined paths and complete readback. Hold dependent generation on verification failure; reread installed controls before fresh generation."},
      "existing_helper_limit":"verify_and_sync_r40.py remains pinned to installation commit 0c0031cf... and its install mode requires live main to equal that historical commit; it was not executed in this status check.","rollback_limit":"Helper explicitly rolls back a failed stage-to-target rename; fallback write/readback failure has no generic automatic rollback handler. Protocol still requires retaining/restoring backup and holding generation.","verification_limits":["Point-in-time identity verification, not a continuously running synchronizer or unattended watcher.","GitHub main can change after the ending ref check.","Package equality does not establish lecture acceptance, semantic skill application or human learning.","No installation, repository, teaching, reader inputs, or runtime was mutated. Only review files were written."],"source_record_hashes":{n:sha((MAINT/n).read_bytes()) for n in record_files}}
    save("verification.json",evidence)
    save("package-file-identities.json",{"main_commit":main_before,"files":expected,"live_urls":{p:url for p,raw,url in fetched}})
    save("manifest-checks.json",{"checks":manifest_results})
    save("backup-file-identities.json",{"path":str(backup),"version":backup_version,"prior_published_commit":previous["published_package_commit"],"files":backup_inventory})
    print(json.dumps({k:evidence[k] for k in ("main_commit_before","prof_version","complete_package_files","installed_files","missing","extra","byte_mismatches","operative_manifest_hash_checks","package_git_blobs_identical_since_install")},indent=2))


if __name__=="__main__":main()
