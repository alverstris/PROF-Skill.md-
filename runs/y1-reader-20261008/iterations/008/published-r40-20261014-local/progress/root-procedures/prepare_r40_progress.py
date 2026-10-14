"""Preserve former closures; reopen verified format failures without teaching edits."""
from pathlib import Path
import hashlib
import json
import subprocess
from datetime import datetime, timezone

WORK=Path(__file__).resolve().parents[2]
MAINT=Path(__file__).resolve().parent
REPO=MAINT/'repository'
CASE=WORK/'.prof-sasis/20261014-d008-r40'
STATE=CASE/'run-state'; STATE.mkdir(parents=True,exist_ok=True)
OLD=WORK/'.prof-sasis/20261014-d008-r39'
AUDIT=OLD/'earlier-success-review'
PIN='0c0031cf996d7f47d4db878709f31676594aa08f'
raw=subprocess.check_output(['git','-C',str(REPO),'show',PIN+':runs/y1-reader-20261008/queue.json'])
assert raw==(OLD/'run-state/queue.json').read_bytes()
queue=json.loads(raw)
verified=json.loads((AUDIT/'root-strict-syntax-verification.json').read_bytes())
affected=verified['affected_cases']; assert len(affected)==7 and sum(affected.values())==68
previous=STATE/'previous-accepted-sessions';previous.mkdir(exist_ok=True)
now=datetime.now(timezone.utc).isoformat()
for s in queue['sessions']:
    mid=s['material_id']
    if mid in affected:
        assert s['status']=='closed'
        (previous/(mid+'.json')).write_text(json.dumps(s,indent=2)+'\n',encoding='utf-8')
        s['historical_acceptance_preserved']=True
        s['status']='pending'
        s['current_iteration']={'state':'reopened_pending_fresh_generation','incoming_prof':'2026-10-14-r40',
          'verified_package_commit':PIN,'reopened_at':now,
          'reason':'Verified explicit strict-comparison source-format requirement failure; no rendering or mathematical defect inferred.',
          'verified_occurrences':affected[mid],
          'reopening_evidence':'iterations/008/published-r40-20261014-local/progress/earlier-success-review/root-strict-syntax-verification.json',
          'previous_whole_session':'iterations/008/published-r40-20261014-local/progress/run-state/previous-accepted-sessions/'+mid+'.json',
          'fresh_author_started':False}
    if mid=='D008':
        s['current_iteration']={'state':'fresh_generation_in_progress','incoming_prof':'2026-10-14-r40',
          'verified_package_commit':PIN,'fresh_author_started':True,'fresh_author':'/root/author_d008_r40_fresh',
          'local_synchronisation':'iterations/008/published-r40-20261014-local/progress/r40-installation-verification.json',
          'fresh_generation_root':'iterations/008/published-r40-20261014-local/teaching/',
          'acceptance':'pending'}
queue['active_readability_scope']['closed']=8
queue['active_readability_scope']['remaining']=68
queue['active_material_id']='D008'
queue['current_prof_package_commit']=PIN
queue['current_prof_revision']='2026-10-14-r40'
assert len(queue['sessions'])==147
assert sum(s['status']=='closed' for s in queue['sessions'])==8
assert sum(s['status']=='pending' for s in queue['sessions'])==68
assert sum(s['status']=='excluded_by_user_readability_scope' for s in queue['sessions'])==71
(STATE/'queue.json').write_text(json.dumps(queue,indent=2)+'\n',encoding='utf-8')
run={'objective':'you are to continue the iteration until it is done.','canonical_repository':'alverstris/PROF-Skill.md-',
     'pinned_package_commit':PIN,'prof_revision':'2026-10-14-r40','active_material':'D008',
     'original_sessions':147,'eligible':76,'excluded':71,'currently_closed':8,'pending':68,
     'historical_closed_before_rechecks':15,'reopened':list(affected),
     'local_prof_synchronisation':'verified complete36file overwrite and26manifest checks, backup retained',
     'fresh_author':'/root/author_d008_r40_fresh','fresh_reader':'pending frozen generation and verified production binding',
     'next_action':'Freeze complete new D008 generation; independently audit and run a separate fresh full SASIS reader using published r40 controls. Complete earlier reopened cases and affected checks without patching old teaching; preserve complete queue and original inputs.',
     'updated_at':now,'new_lecture_acceptance_claimed':False}
(STATE/'RUN.json').write_text(json.dumps(run,indent=2)+'\n',encoding='utf-8')
for name in ['r40-published-package-readback.json','r40-installation-verification.json']:
    (STATE/name).write_bytes((MAINT/name).read_bytes())
print(json.dumps(run))
