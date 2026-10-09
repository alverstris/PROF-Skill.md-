#!/usr/bin/env python3
"""Read-only local Git/evidence binding check; writes only its scratch JSON output."""
import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[1] / 'PROF-repo'
MAIN = 'e35a59a64ed1b01f7ae43e4ef46042f23cc7e2d6'
PREFIX = 'runs/y1-reader-20261008/iterations/'

def digest(data):
    return hashlib.sha256(data).hexdigest()

def blob(commit, path):
    return subprocess.run(['git', 'show', f'{commit}:{path}'], cwd=REPO,
                          check=True, capture_output=True).stdout

def binding(path, frozen=None, expected=None):
    path = Path(path)
    if not path.is_absolute():
        path = REPO / path
    rel = str(path.relative_to(REPO))
    data = path.read_bytes()
    main = blob(MAIN, rel)
    record = {'path': rel, 'bytes': len(data), 'sha256': digest(data),
              'published_reference_commit': MAIN,
              'published_reference_blob_sha256': digest(main),
              'local_equals_published_reference_blob': data == main}
    if expected is not None:
        record['recorded_sha256'] = expected
        record['local_equals_recorded_sha256'] = digest(data) == expected
    if frozen is not None:
        old = blob(frozen, rel)
        record.update(frozen_commit=frozen, frozen_blob_sha256=digest(old),
                      local_equals_frozen_blob=data == old)
    assert data == main, f'Main-reference mismatch: {rel}'
    assert expected is None or digest(data) == expected, f'Recorded hash mismatch: {rel}'
    assert frozen is None or data == old, f'Frozen mismatch: {rel}'
    return record

cases = []
first = json.loads((ROOT / 'd001-d003/mapping.json').read_text())['materials']
for item in first:
    teaching = item['teaching']
    records = [binding(item[key]['path']) for key in
               ['closure', 'final_original_render_report', 'final_original_markup_record',
                'final_original_preview_record']]
    extra = []
    if 'constituent_image' in item:
        image = item['constituent_image']
        extra.append(binding(image['path'], image['frozen_commit'], image['recorded_sha256']))
    cases.append({'material_id': item['material_id'],
                  'teaching': binding(teaching['path'], teaching['frozen_commit'], teaching['recorded_sha256']),
                  'constituents': extra, 'historical_evidence': records})

middle = json.loads((ROOT / 'd004-d005/local-evidence-verification.json').read_text())['records']
extra_paths = {
    'D004': ['004/closure.md', '004/render-markup-v1.json', '004/render-preview-v1.json'],
    'D005': ['005/closure.md', '005/render-evidence/v2/markup-audit.json',
             '005/render-evidence/v2/preview-check.json', '005/parent-acceptance-v2.md']}
for item in middle:
    teaching = item['accepted_teaching']
    cases.append({'material_id': item['case'],
                  'teaching': binding(teaching['path'], teaching['commit'], teaching['working']['expected_sha256']),
                  'constituents': [],
                  'historical_evidence': [binding(item['original_final_report']['path'])] +
                      [binding(PREFIX + p) for p in extra_paths[item['case']]]})

last = json.loads((ROOT / 'd006-d007/mapping.json').read_text())['cases']
for item in last:
    teaching = item['final_artifact']
    report = next(x['path'] for x in item['reviewed_evidence_identity'] if x['path'].endswith('/report.md'))
    audit_path = str(Path(report).with_name('scoped-markup-navigation-audit.json'))
    audit = json.loads((REPO / audit_path).read_text())
    src, dest = audit['source_math'], audit['github_math']
    unequal = [i + 1 for i, (s, d) in enumerate(zip(src, dest))
               if s['type'] != d['type'] or s['payload'] != d['payload']]
    assert len(src) == len(dest) == item['destination_math']['total']
    assert not unequal
    cases.append({'material_id': item['material_id'],
                  'teaching': binding(teaching['path'], teaching['freeze_commit'], teaching['sha256']),
                  'constituents': [],
                  'historical_evidence': [binding(x['path'], expected=x['sha256'])
                                          for x in item['reviewed_evidence_identity']] + [binding(audit_path)],
                  'retained_payload_array_comparison': {
                      'source_count': len(src), 'destination_count': len(dest),
                      'unequal_type_or_payload_positions': unequal,
                      'scope': 'Recomputed from preserved complete source/destination arrays; no fresh destination capture.'}})

out = {'prepared_at_utc': datetime.now(timezone.utc).isoformat(),
       'scope': 'Historical frozen-object and published-reference byte bindings only. No candidate pass, live renderer, regeneration, or publication performed.',
       'git_operation': 'Local git show only; explicit commit, no network/fetch/worktree mutation.',
       'published_reference_commit': MAIN, 'cases': cases}
(ROOT / 'exact-bindings.json').write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps({'case_count': len(cases),
                  'teaching_and_constituent_bindings': sum(1 + len(x['constituents']) for x in cases),
                  'historical_evidence_bindings': sum(len(x['historical_evidence']) for x in cases),
                  'all_assertions_succeeded': True,
                  'output': str(ROOT / 'exact-bindings.json')}, indent=2))
