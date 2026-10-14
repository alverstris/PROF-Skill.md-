"""Root audit of a terminated reader's metadata only; never admits a partial route."""
from pathlib import Path
import collections
import hashlib
import json
import shutil

root = Path(__file__).resolve().parent
inputs = root / 'reader-inputs'
output = root / 'reader-admission'
output.mkdir(exist_ok=True)
config = json.loads((inputs / 'frozen-route.json').read_text(encoding='utf-8'))
state = json.loads((inputs / 'runtime/state.json').read_text(encoding='utf-8'))
events = [json.loads(line) for line in (inputs / 'runtime/access.jsonl').read_text(encoding='utf-8').splitlines()]
counts = collections.Counter(event['event'] for event in events)
accesses = [event for event in events if event['event'] == 'verified_access_receipt']
expected = config['steps'][:24]
assert state['cursor'] == len(accesses) == len(expected) == 24
assert state['pending_figure'] is None
assert [a['requested_step'] for a in accesses] == [s['id'] for s in expected]
for actual, step in zip(accesses, expected):
    assert actual['sha256'] == step['sha256']
    assert actual['start'] == step['start'] and actual['byte_length'] == step['length']
assert state['baseline_read'] == [f'B{i:04d}' for i in range(1,23)]
assert counts['python_subject_open_audit'] == counts['bounded_bytes_read'] == 24
assert counts['text_output_delivered'] == 23
assert counts['view_invocation'] == counts['view_result'] == counts['image_output_delivered'] == 1
assert not any(event.get('requested_step') == 'main-02' for event in events)
snapshots = {}
authorised = (inputs/'fixed_adapter.js').read_text(encoding='utf-8').replace('const STEP_ID = "B0001";', 'const STEP_ID = "main-02";')
failed = (root/'reader-report/failed-main-02-call.js').read_text(encoding='utf-8')
good = '0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,0x748f82ee'
bad = '0x2748774c,0x34b0bcb5,0x682e6ff3,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x748f82ee'
assert authorised.count(good) == 1 and failed == authorised.replace(good,bad)
for source, name in [(inputs/'runtime/access.jsonl','original-access.jsonl'),
                     (inputs/'runtime/state.json','original-state.json'),
                     (root/'reader-report/original-reader-report.md','original-reader-report.md'),
                     (root/'reader-report/failed-main-02-call.js','failed-main-02-call.js'),
                     (root/'reader-report/failed-main-02-result.txt','failed-main-02-result.txt')]:
    destination = output/name
    if destination.exists():
        assert destination.read_bytes() == source.read_bytes(), f'Existing immutable snapshot differs: {name}'
    else:
        shutil.copy2(source,destination)
    snapshots[name] = {'bytes':destination.stat().st_size,
                       'sha256':hashlib.sha256(destination.read_bytes()).hexdigest()}
record = {'route_id':config['route_id'],'route_sha256':state['route_sha256'],
          'complete_route_admitted':False,'teaching_verdict':'unverified outside inspected opening',
          'valid_completed_prefix_steps':24,'total_scheduled_steps':len(config['steps']),
          'full_baseline_prefix_verified':True,'first_figure_delivery_receipts_verified':True,
          'later_subject_access_in_fixed_launcher_ledger':False,
          'event_counts':dict(counts),'snapshot_files':snapshots,
          'full_route_checker_result':{'operational_route_audit_passed':False,'error':'route/display evidence incomplete'},
          'procedure_failure':'Reader report records changed SHA256 constant order; self-check failed before main-02 launcher invocation.',
          'archived_failed_call_difference_verified':'Only the reported k-array constant order differs from the authorised adapter with the intended main-02 ID.',
          'evidence_limit':'Original failed call/result were archived from the former reader conversation after its original report was sealed; this metadata ledger does not authenticate other available tool use or prove semantic inspection.',
          'technical_confinement_proven':False,'human_learning_proven':False}
(output/'admission-rejection.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'prefix_verified':True,'complete_route_admitted':False,'counts':dict(counts),'snapshots':snapshots},indent=2))
