import argparse
import copy
import hashlib
import json
from pathlib import Path

p = argparse.ArgumentParser()
p.add_argument('--release-commit', required=True)
p.add_argument('--reopen', nargs='+', required=True)
a = p.parse_args()
assert len(a.reopen)==2 and set(a.reopen)=={'D008','D016'}
w = Path('/workspace/scratch/f9c0b7fc7e76/d013-clean-r32-20261012')
old = json.loads((w / 'bookkeeping/queue.json').read_text())
q = copy.deepcopy(old)
prefix = 'iterations/013/published-r32-20261012/'
fields = ['status', 'source_access', 'source_preparation', 'incoming_revision',
          'incoming_commit', 'activation', 'current_teaching', 'current_frozen_commit',
          'incoming_prof', 'outgoing_prof', 'document_revision', 'document_commit',
          'final_document_sha256', 'current_review_status', 'current_iteration', 'published_commit']
for row in q['sessions']:
    mid = row['material_id']
    if mid not in set(a.reopen) | {'D013'}:
        continue
    previous = {k: copy.deepcopy(row[k]) for k in fields if k in row}
    if mid != 'D013':
        assert row['status'] == 'closed' and row['readability']['eligible']
        row.setdefault('reopening_history', []).append({
            'date': '2026-10-12', 'previous_state': previous,
            'reason': 'Actual failed first-use/return navigation with images preceding the fragment target; complete controlled image-reservation diagnosis establishes the relevant dependency. Successful warmed repeats do not erase the recorded failed route.',
            'evidence': [prefix + 'evidence/final-adjudication.json', prefix + 'evidence/earlier-image-dependency-census.json', prefix + 'evidence/root-complete-original-reassembly.json'],
            'repair_package': '2026-10-12-r33', 'verified_package_commit': a.release_commit})
        row['source_access'] = 'Original sources remain readable. Acceptance reopened only after an actual failed destination route and its demonstrated image-layout dependency; prior content and review evidence are preserved. Fresh full generation and review under the verified repaired package are required.'
        row['current_review_status'] = {'destination': 'fail: actual off-target return and image-layout dependency', 'iteration_closure': 'reopened; prior evidence preserved', 'required_next': 'fresh complete generation under current published repaired PROF'}
        row['current_iteration'] = {'state': 'reopened_pending_fresh_generation', 'incoming_prof': '2026-10-12-r33', 'verified_package_commit': a.release_commit, 'evidence': prefix + 'evidence/final-adjudication.json'}
    else:
        row.setdefault('iteration_history', []).append({'superseded_by': 'published-r32-20261012', 'previous_current_fields': previous})
        row.update({'source_access': 'All five original pages/figures, full baseline, six frozen teaching constituents, all42 prompt demands and complete source/reader/technical/destination audits inspected. Content and mathematical preservation pass; actual first-use return navigation fails with demonstrated unreserved-image geometry cause. Frozen teaching remains unchanged and unaccepted.',
                    'incoming_revision': '2026-10-12-r32', 'incoming_commit': '167f268eaa01d3fabb7bea7d00e53298717f8728',
                    'incoming_prof': '2026-10-12-r32', 'outgoing_prof': '2026-10-12-r33',
                    'activation': prefix + 'evidence/package-admission.json',
                    'current_teaching': prefix + 'teaching/main.md',
                    'current_frozen_commit': '36e3d042ba459f3048e1489fd12045029f61abbb',
                    'document_commit': '36e3d042ba459f3048e1489fd12045029f61abbb',
                    'document_revision': 'published-r32-20261012',
                    'final_document_sha256': 'fc7ca6bf452873ec74e7e982e55dff5bbc2c857d6f1fd76d88716e24ffcdac1d',
                    'published_commit': a.release_commit,
                    'current_review_status': {'technical_source': 'complete; no material subject defect', 'fresh_reader': 'complete and admitted with reconstructed-access-log qualification', 'destination': 'fail: first-use return target displaced by unreserved images; all314math/prose and native figures preserved', 'iteration_closure': 'not accepted; full r33 repair published and verified; fresh D013 required'},
                    'current_iteration': {'state': 'published_r33_verified_fresh_generation_required', 'incoming_prof': '2026-10-12-r32', 'outgoing_prof': '2026-10-12-r33', 'verified_package_commit': a.release_commit, 'frozen_teaching_commit': '36e3d042ba459f3048e1489fd12045029f61abbb', 'evidence': prefix + 'evidence/final-adjudication.json', 'publication_readback': prefix + 'evidence/repair-release-readback.json', 'next_action': 'Fresh same-material D013 author reads actual complete published package/full baseline/original source only before whole freeze.'}})
    row['status'] = 'pending'
    row['evidence'].extend(x for x in [prefix + 'evidence/final-adjudication.json', prefix + 'evidence/repair-release-readback.json', prefix + 'repair-checkpoint.md'] if x not in row['evidence'])

eligible = [x for x in q['sessions'] if x['readability']['eligible']]
accepted = sum(x['status'] == 'closed' for x in eligible)
assert len(q['sessions']) == 147 and len(eligible) == 76
assert [x['id'] for x in q['sessions']] == [x['id'] for x in old['sessions']]
assert [x['order'] for x in q['sessions']] == [x['order'] for x in old['sessions']]
assert sum(not x['readability']['eligible'] for x in q['sessions']) == 71
for before, after in zip(old['sessions'], q['sessions']):
    assert all(x in after['evidence'] for x in before['evidence'])
    if after['material_id'] not in set(a.reopen) | {'D013'}:
        assert before == after
q['active_readability_scope']['closed'] = accepted
q['active_readability_scope']['remaining'] = 76 - accepted
q['active_material_id'] = 'D013'
next_pending = next(x['material_id'] for x in eligible if x['status'] != 'closed' and x['material_id'] != 'D013')
assert accepted == 13 and next_pending == 'D008'
out = w / 'checkpoint'
out.mkdir(exist_ok=True)
(out / 'queue.json').write_text(json.dumps(q, indent=2, ensure_ascii=False) + '\n')
text = f'''Current checkpoint — 2026-10-12 D013 delivery repair, PROF 2026-10-12-r33

D013 complete frozen teaching and whole audits are preserved; it is not accepted. Source coverage, all42 prompt demands, full-baseline SASIS with its reconstructed-access qualification, all314 actual math expressions and whole prose/figures were inspected. Actual first-use returns missed their targets after unreserved images expanded. The controlled two-arm fixture preserves text/math/image bytes and shows intrinsic dimension reservation prevents the tested displacement; warmed repeat success does not erase first-use failure.

Complete36-file cumulative r33 repair and original evidence were published at {a.release_commit} and fetched for actual byte/hash/blob verification. Only general navigation instructions and revision metadata change in three package files; other33 are unchanged. Frozen D013 teaching was never patched. The helper reports the actual failed destination gate, not readiness.

Earlier exact-pin source census covered all15 prior accepted lessons and50 constituents. Actual affected earlier routes reopen {', '.join(a.reopen)}; other records retain their existing evidence. All147 IDs/order and71 exclusions are preserved. Accepted{accepted}, remaining{76-accepted} of76eligible. Active D013 must be generated afresh under the published package; next pending after this active retry is {next_pending}. Continue the whole eligible corpus with fresh author/reader contexts, original inputs and sole publication ownership.

Evidence and repair checkpoint: {prefix}repair-checkpoint.md. Publication readback: {prefix}evidence/repair-release-readback.json.

Earlier checkpoints retained below unchanged.

'''
for name in ['RUN.md', 'CHANGELOG.md']:
    original = (w / 'bookkeeping' / name).read_bytes()
    combined = text.encode() + original
    assert combined.endswith(original)
    (out / name).write_bytes(combined)
(out / 'repair-checkpoint.md').write_text(text)
(w / 'evidence/checkpoint-preservation.json').write_text(json.dumps({'records':147,'eligible':76,'excluded':71,'accepted':accepted,'remaining':76-accepted,'active':'D013','next_pending_after_active':next_pending,'reopened':a.reopen,'ids_order_preserved':True,'all_prior_evidence_preserved':True,'unaffected_records_equal':True,'old_RUN_and_CHANGELOG_bytes_preserved_as_suffix':True,'release_commit':a.release_commit},indent=2)+'\n')
print(json.dumps({'accepted':accepted,'remaining':76-accepted,'active':'D013','next':next_pending,'reopened':a.reopen}))
