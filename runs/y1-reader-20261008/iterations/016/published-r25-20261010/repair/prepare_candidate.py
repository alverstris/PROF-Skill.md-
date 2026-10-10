from pathlib import Path
import json, shutil, hashlib

root = Path('/workspace/scratch/f9c0b7fc7e76/d016-published-r25')
source = root / 'inputs/prof'
target = root / 'repair/candidate/prof'
manifest = json.loads((root / 'package-sha-manifest.json').read_text())
assert not target.exists()
for item in manifest['files']:
    data = (source / item['path']).read_bytes()
    assert hashlib.sha256(data).hexdigest() == item['sha256']
    dest = target / item['path']
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(data)

p = target / 'SKILL.md'
data = p.read_bytes()
def replace_once(old, new):
    global data
    old, new = old.encode(), new.encode()
    assert data.count(old) == 1, old
    data = data.replace(old, new, 1)
replace_once('version: "2026-10-10-r25"', 'version: "2026-10-10-r26"')
replace_once('A real citation does not prove the surrounding claim. |', 'A real citation does not prove the surrounding claim. Check qualitative summaries against their formulas and admissible special cases; correct example calculations do not validate an unconditional claim. |')
replace_once('Honour the requested format. Attempts, hints, and solutions must be reachable', 'Honour the requested format. Inspect every final exported figure at usable size, including its canvas edges; titles, ticks, labels and legends must remain complete and readable. Attempts, hints, and solutions must be reachable')
p.write_bytes(data)

p = target / 'references/execution-protocol.md'
data = p.read_bytes()
anchor = b'Before final delivery, reconcile the complete required-topic list against the final artifact, including its ending.'
assert data.count(anchor) == 1
addition = (
    'When a qualitative summary interprets a formula, check the summary itself against the stated domain, rather than only checking numerical examples. Derive its unit product or comparison from the formula and test a relevant admissible limiting or exceptional case. For example, multiplying by a dimensionless integration variable does not create a new unit; a claim that units necessarily differ needs the dimensional condition. Retain the correct relation without extending its scope. Apply this check to consequential claims, not as an unrelated catalogue of edge cases.\r\n\r\n'
    'For figures generated or exported for the lesson, inspect the exact saved raster or vector after layout and at the size used in the document. Check all titles, axis and tick labels, legends and annotations, especially at the canvas edges, for missing glyphs, overlap or unreadable scaling. Reserve sufficient export margins and inspect the embedded result too. If text extents are available, compare their actual export coordinates with the canvas as a supplementary check; layout flags, an absence of warnings, and a count of edge pixels alone cannot establish readability. Distinguish intended plot-window cropping from loss of explanatory text. Follow the active repair mode: correct and re-export in ordinary work; preserve a frozen self-iteration artifact, repair PROF and restart from the published revision.\r\n\r\n'
)
data = data.replace(anchor, addition.encode() + anchor, 1)
p.write_bytes(data)

records=[]
for item in manifest['files']:
    b=(target/item['path']).read_bytes()
    records.append({'path':item['path'],'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest(),'changed':b!=(source/item['path']).read_bytes()})
(root/'repair/candidate-package-manifest.json').write_text(json.dumps({'version':'2026-10-10-r26','status':'unpublished candidate; no regenerated teaching validated','files':records},indent=2)+'\n')
print(json.dumps({'candidate':str(target),'files':len(records),'changed':[r['path'] for r in records if r['changed']]}))
