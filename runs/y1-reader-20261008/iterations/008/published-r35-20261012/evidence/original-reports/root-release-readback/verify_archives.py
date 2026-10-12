from pathlib import Path
import json,hashlib,zipfile,io,sys
ROOT=Path(__file__).resolve().parent.parent
OUT=Path(__file__).resolve().parent/sys.argv[1]
PUB=OUT/'published-files'
sha=lambda b:hashlib.sha256(b).hexdigest()
def unique(name):
    matches=list(PUB.rglob(name))
    assert len(matches)==1,(name,[str(x) for x in matches])
    return matches[0]
def verify_zip(name,manifest_name,base,parts_name=None):
    manifest=json.loads(unique(manifest_name).read_text())
    if parts_name:
        reassembly=json.loads(unique(parts_name).read_text())
        pieces=[]
        for p in reassembly['parts']:
            data=unique(Path(p['path']).name).read_bytes()
            assert len(data)==p['bytes'] and sha(data)==p['sha256']
            pieces.append(data)
        data=b''.join(pieces)
        expected=reassembly.get('archive',reassembly)
        assert len(data)==expected.get('original_bytes',expected.get('bytes'))
        assert sha(data)==expected.get('original_sha256',expected.get('sha256'))
    else:
        data=unique(name).read_bytes()
    assert len(data)==manifest.get('archive_bytes',manifest.get('bytes'))
    assert sha(data)==manifest.get('archive_sha256',manifest.get('sha256'))
    z=zipfile.ZipFile(io.BytesIO(data))
    assert z.testzip() is None
    expected_members=manifest['members']
    assert set(z.namelist())=={m['path'] for m in expected_members}
    assert len(z.namelist())==len(expected_members)
    records=[]
    for m in expected_members:
        b=z.read(m['path']);assert len(b)==m['bytes'] and sha(b)==m['sha256'],m['path']
        local=base/m['path'];assert local.is_file(),local
        assert b==local.read_bytes(),str(local)
        records.append({'path':m['path'],'bytes':len(b),'sha256':sha(b),'local_byte_equal':True})
    return {'archive':name,'archive_bytes':len(data),'archive_sha256':sha(data),'member_count':len(records),'member_bytes':sum(m['bytes'] for m in records),'all_members':records,'zip_crc_pass':True,'scope':'Actual published blobs reassembled and every original member compared mechanically; no future semantics displayed.'}
rows=[
    verify_zip('d008-complete-original-evidence.zip','evidence-archive-manifest.json',ROOT/'d008-clean-r35-20261012','evidence-archive-reassembly.json'),
    verify_zip('d116-d118-prepared-20261012.zip','d116-d118-prepared-20261012-manifest.json',ROOT),
    verify_zip('d119-d121-prepared-20261012.zip','d119-d121-prepared-20261012-manifest.json',ROOT,'d119-d121-prepared-20261012-reassembly-manifest.json')
]
(OUT/'archive-readback.json').write_text(json.dumps(rows,indent=2)+'\n')
print(json.dumps([{k:r[k] for k in ['archive','archive_bytes','archive_sha256','member_count','member_bytes','zip_crc_pass']} for r in rows],indent=2))
