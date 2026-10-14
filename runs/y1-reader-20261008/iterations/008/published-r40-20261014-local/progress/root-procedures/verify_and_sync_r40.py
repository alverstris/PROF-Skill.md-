"""Verify downloaded immutable Git objects; synchronise only after main publication."""
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent
REPO = ROOT / 'repository'
COMMIT = '0c0031cf996d7f47d4db878709f31676594aa08f'
TARGET = Path('C:/Users/alver/.codex/skills/prof')
BACKUPS = Path('C:/Users/alver/.codex/skill-backups/prof')
STAGE = ROOT / ('downloaded-prof-r40-' + COMMIT[:12])
RECORD = ROOT / 'r40-published-package-readback.json'

def git(*args):
    return subprocess.check_output(['git', '-C', str(REPO), *args])

def sha(data):
    return hashlib.sha256(data).hexdigest()

def inventory(root):
    answer = {}
    for p in root.rglob('*'):
        if p.is_symlink() or p.is_junction() or not p.resolve().is_relative_to(root.resolve()):
            raise RuntimeError('Unexpected linked or escaped path: ' + str(p))
        if p.is_file():
            answer[p.relative_to(root).as_posix()] = sha(p.read_bytes())
    return answer

def check_manifests(root):
    path = root / 'references/sasis/profile-manifest.json'
    m = json.loads(path.read_bytes())
    checks = [(path.parent / m['file_hashes_base_directory'] / p, h) for p, h in m['file_hashes'].items()]
    checks += [(path.parent / p, h) for p, h in m['control_file_hashes'].items()]
    checks += [(path.parent / e['path'], e['sha256']) for e in m['subject_files']]
    for p, h in checks:
        assert p.resolve().is_relative_to(root.resolve()) and sha(p.read_bytes()) == h, str(p)
    assert len(checks) == 26
    for p in root.rglob('*.json'):
        json.loads(p.read_bytes())
    return len(checks)

def downloaded_identities():
    assert git('remote', 'get-url', 'origin').decode().strip() == 'https://github.com/alverstris/PROF-Skill.md-.git'
    assert git('rev-parse', COMMIT).decode().strip() == COMMIT
    tree = {}
    for entry in filter(None, git('ls-tree', '-rz', COMMIT).split(b'\0')):
        meta, name = entry.split(b'\t', 1)
        mode, kind, oid = meta.split()
        tree[name.decode()] = (mode.decode(), kind.decode(), oid.decode())
    index = json.loads((ROOT / 'r40-publication-inputs.json').read_bytes())
    object_ids = sorted({e['git_blob_sha'] for e in index['items'] + index['package']})
    result = subprocess.run(['git','-C',str(REPO),'cat-file','--batch'], input=('\n'.join(object_ids)+'\n').encode(), capture_output=True, check=True)
    objects = {}
    cursor = 0
    for oid in object_ids:
        end = result.stdout.index(b'\n', cursor)
        returned, kind, size = result.stdout[cursor:end].split()
        assert returned.decode() == oid and kind == b'blob'
        cursor = end + 1
        objects[oid] = result.stdout[cursor:cursor+int(size)]
        cursor += int(size)
        assert result.stdout[cursor:cursor+1] == b'\n'
        cursor += 1
    assert cursor == len(result.stdout)
    checked = {}
    for e in index['items'] + index['package']:
        mode, kind, oid = tree[e['path']]
        assert mode == '100644' and kind == 'blob' and oid == e['git_blob_sha'], e['path']
        data = objects[oid]
        assert len(data) == e['bytes'] and sha(data) == e['sha256'], e['path']
        checked[e['path']] = e['sha256']
    package = {p: oid for p, (mode, kind, oid) in tree.items() if p == 'SKILL.md' or p.split('/')[0] in {'agents','assets','references','scripts'}}
    assert set(package) == {e['path'] for e in index['package']} and len(package) == 36
    return index, package, checked

def main():
    index, package, checked = downloaded_identities()
    expected = {e['path']: e['sha256'] for e in index['package']}
    if sys.argv[1] == 'verify':
        assert not STAGE.exists() and STAGE.resolve().parent == ROOT.resolve()
        STAGE.mkdir()
        for relative, oid in package.items():
            p = STAGE / relative
            assert p.resolve().is_relative_to(STAGE.resolve())
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(git('cat-file', 'blob', oid))
        assert inventory(STAGE) == expected
        manifests = check_manifests(STAGE)
        record = {'repository':'alverstris/PROF-Skill.md-', 'commit':COMMIT,
                  'verified_at':datetime.now(timezone.utc).isoformat(),
                  'downloaded_git_objects_verified':True, 'main_publication_verified':False,
                  'package_files':len(package), 'upload_files':len(index['items']),
                  'unique_verified_blobs':len(checked), 'operative_manifest_checks':manifests,
                  'stage':str(STAGE), 'package_sha256':expected, 'new_lecture_acceptance_claimed':False}
        RECORD.write_text(json.dumps(record, indent=2)+'\n', encoding='utf-8')
        print(json.dumps({k:v for k,v in record.items() if k != 'package_sha256'}))
        return
    assert sys.argv[1] == 'install'
    remote_head = git('ls-remote', 'origin', 'refs/heads/main').decode().split()[0]
    assert remote_head == COMMIT, 'main does not identify the verified published package'
    assert inventory(STAGE) == expected
    check_manifests(STAGE)
    assert TARGET.resolve(strict=True) == TARGET.absolute() and not TARGET.is_symlink() and not TARGET.is_junction()
    before = inventory(TARGET)
    BACKUPS.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    backup = BACKUPS / (stamp + '-r39-before-r40')
    assert not backup.exists() and backup.resolve().parent == BACKUPS.resolve()
    rename_failure = None
    try:
        TARGET.rename(backup)
    except OSError as exc:
        rename_failure = {'type':type(exc).__name__, 'message':str(exc), 'winerror':getattr(exc,'winerror',None)}
        assert TARGET.is_dir() and not backup.exists()
        assert set(before) == set(expected), 'fallback is forbidden for unequal inventories'
        shutil.copytree(TARGET, backup)
        assert inventory(backup) == before
        assert inventory(TARGET) == before, 'installation changed during backup'
        for relative in expected:
            destination = TARGET / relative
            assert destination.resolve().is_relative_to(TARGET.resolve())
            destination.write_bytes((STAGE / relative).read_bytes())
        method = 'equal-inventory complete file-content replacement after verified backup; blocked directory rename preserved'
    else:
        assert inventory(backup) == before
        try:
            STAGE.rename(TARGET)
        except BaseException:
            assert not TARGET.exists() and backup.resolve().parent == BACKUPS.resolve()
            backup.rename(TARGET)
            raise
        method = 'whole-directory replacement from verified stage after complete old-directory backup'
    assert inventory(TARGET) == expected
    assert inventory(backup) == before
    manifests = check_manifests(TARGET)
    record = {'repository':'alverstris/PROF-Skill.md-', 'commit':COMMIT, 'prof_revision':'2026-10-14-r40',
              'verified_at':datetime.now(timezone.utc).isoformat(), 'destination':str(TARGET),
              'backup':str(backup), 'method':method, 'original_rename_failure':rename_failure,
              'published_git_blobs_verified':len(package), 'installed_files_overwritten_and_verified':len(expected),
              'manifest_checks':manifests, 'backup_complete_inventory_and_bytes_match':True,
              'package_sha256':expected, 'new_lecture_acceptance_claimed':False}
    (ROOT/'r40-installation-verification.json').write_text(json.dumps(record, indent=2)+'\n', encoding='utf-8')
    publication = json.loads(RECORD.read_bytes())
    publication['main_publication_verified'] = True
    publication['main_verified_at'] = datetime.now(timezone.utc).isoformat()
    RECORD.write_text(json.dumps(publication, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k:v for k,v in record.items() if k != 'package_sha256'}))

if __name__ == '__main__':
    main()
