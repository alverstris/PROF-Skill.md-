import collections
import hashlib
import html
import json
import pathlib
import posixpath
import re
import subprocess
import urllib.parse

REPO = '/workspace/scratch/f9c0b7fc7e76/prof-iteration'
OUT = pathlib.Path('/workspace/scratch/f9c0b7fc7e76/d008-clean-r30-20261011/reviews/earlier-navigation')
HEAD = '663311ba27f25206ed868ce9bbfd016447528ef3'
PREFIX = 'runs/y1-reader-20261008/'
QUEUE = pathlib.Path('/workspace/scratch/f9c0b7fc7e76/d008-clean-r30-20261011/progress/queue.json')

def batch(specs):
    p = subprocess.run(['git', '-C', REPO, 'cat-file', '--batch'], input=('\n'.join(specs)+'\n').encode(), capture_output=True, check=True)
    tail = p.stdout
    result = {}
    for spec in specs:
        header, tail = tail.split(b'\n', 1)
        bits = header.split()
        if bits[-1] == b'missing':
            raise RuntimeError('Missing object '+spec)
        size = int(bits[-1])
        data, tail = tail[:size], tail[size+1:]
        result[spec] = {'git_blob': bits[0].decode(), 'bytes': size, 'sha256': hashlib.sha256(data).hexdigest(), 'data': data}
    assert not tail
    return result

q = json.loads(QUEUE.read_bytes())
closed = [s for s in q['sessions'] if s['status'] == 'closed']
assert len(closed) == 14
records = {
    'D001': ('0716ea92991d7f9fe2814e137bcc830d91a27511', ['iterations/001/teaching-v4.md'], ['iterations/001/closure.md']),
    'D002': ('f1c0e91c24e9140049d50c7ca965f41e36f3e1a2', ['iterations/002/teaching-v1.md'], ['iterations/002/closure.md']),
    'D003': ('4cbf83f2dc2859d5123fc01a0c311a268d580483', ['iterations/003/teaching-v1.md'], ['iterations/003/closure.md']),
    'D004': ('197b57555834d36952e948d4100d2f835c86b20c', ['iterations/004/teaching-v1.md'], ['iterations/004/closure.md']),
    'D005': ('32c553f279ac1e5771ff05b78a9951cbff3fee38', ['iterations/005/teaching-v2.md'], ['iterations/005/closure.md']),
    'D006': ('28825d27b93baef43a5751eacecac81fa46841bc', ['iterations/006/regenerated-r13-candidate1/teaching-v3.md'], ['iterations/006/closure.md']),
    'D007': ('4765d39aa399a0a1ff09223cae21b15ce6c7f720', ['iterations/007/published-r29-20261011/teaching/'+f+'.md' for f in ['lesson','hints','solutions']], ['iterations/007/published-r29-20261011/closure.md','iterations/007/published-r29-20261011/freeze-manifest.json']),
    'D009': ('9840e70de6aa7d2c718b60dd13ace7e6f795a50e', ['iterations/009/resumption-20261009/author/teaching-r15-recovery-v3.md'], ['iterations/009/closure.md','iterations/009/resumption-20261009/final-acceptance.md']),
    'D010': ('629feb501ffd69447b70011d852ece5bf8a04641', ['iterations/010/current-r16/author/teaching-v2.md'], ['iterations/010/closure.md','iterations/010/current-r16/final-acceptance.md','iterations/010/current-r16/author/freeze-v2.json']),
    'D011': ('d493bae7f5f680e33f2fa891c5d0310bf43e5d23', ['iterations/011/current-r17/author/teaching-v3.md'], ['iterations/011/closure.md','iterations/011/current-r17/final-acceptance.md','iterations/011/current-r17/author/freeze-manifest-v3.json']),
    'D012': ('12f468d985cbc1cb462e41948f0f017a161a2099', ['iterations/012/current-r18/author/teaching-v2.md'], ['iterations/012/closure.md','iterations/012/current-r18/final-acceptance.md','iterations/012/current-r18/author/packet-v2.json']),
    'D014': ('40151288dfc73314e6efb7ef74794dfa75a0a5ee', ['iterations/014/current-r20/author/teaching-v2.md'], ['iterations/014/closure.md','iterations/014/current-r20/final-acceptance.md','iterations/014/current-r20/author/v2-evidence/teaching-freeze-v2.json','iterations/014/current-r20/frozen-v2-readback.json']),
    'D016': ('51a78beccef858072b1da8d057ef3dff09878409', ['iterations/016/published-r26-20261010/fresh-r26b/teaching/'+f+'.md' for f in ['lesson','hints','solutions']], ['iterations/016/published-r26-20261010/fresh-r26b/closure-20261011/closure.md','iterations/016/published-r26-20261010/fresh-r26b/freeze-manifest.json','iterations/016/published-r26-20261010/fresh-r26b/closure-20261011/final-state/review/final-acceptance-20261011.md']),
    'D017': ('a7b7de5e040882fa605716e3a954ee067d3ce9a6', ['iterations/017/published-r27-20261011/output/teaching.md'], ['iterations/017/published-r27-20261011/closure-20261011/closure.md','iterations/017/published-r27-20261011/evidence/final-acceptance.md','iterations/017/published-r27-20261011/evidence/freeze-manifest.json']),
}
assert set(records) == {s['material_id'] for s in closed}
specs = [HEAD+':'+PREFIX+'queue.json']
for pin, files, evidence in records.values():
    specs += [c+':'+PREFIX+path for path in files for c in [pin,HEAD]]
    specs += [HEAD+':'+PREFIX+path for path in evidence]
objects = batch(list(dict.fromkeys(specs)))
queue_object = objects[HEAD+':'+PREFIX+'queue.json']
assert queue_object['data'] == QUEUE.read_bytes()

files = []
for session in closed:
    sid = session['material_id']
    pin, paths, evidence = records[sid]
    for path in paths:
        path = PREFIX+path
        o = objects[pin+':'+path]
        current = objects[HEAD+':'+path]
        assert o['data'] == current['data'], path
        body = o['data'].decode()
        anchors = []
        for m in re.finditer(r'<(?:a|[a-z][a-z0-9]*)\b[^>]*?\b(?:id|name)\s*=\s*([\"\'])(.*?)\1[^>]*>', body, re.I):
            anchors.append({'fragment':html.unescape(m[2]),'line':body.count('\n',0,m.start())+1,'offset':m.start(),'kind':'explicit_html'})
        # GitHub heading IDs are inventory candidates only; exact destination normalization is not claimed.
        heading_counts = collections.Counter()
        for m in re.finditer(r'^(#{1,6})\s+(.+?)\s*#*\s*$',body,re.M):
            label = re.sub(r'<[^>]+>','',m[2]).lower()
            slug = re.sub(r'[^\w\- ]','',label).replace(' ','-')
            n=heading_counts[slug]; heading_counts[slug]+=1
            anchors.append({'fragment':slug+('-'+str(n) if n else ''),'line':body.count('\n',0,m.start())+1,'offset':m.start(),'kind':'inferred_heading'})
        anchors.sort(key=lambda a:a['offset'])
        link_matches=[]
        for m in re.finditer(r'(?<!!)\[([^\n]*?)\]\(\s*(<[^>]+>|[^\s)]+)(?:\s+[^)]*)?\)',body):
            link_matches.append((m.start(),m[1],m[2].strip('<>'),'markdown_inline'))
        for m in re.finditer(r'<a\b[^>]*?\bhref\s*=\s*([\"\'])(.*?)\1[^>]*>',body,re.I):
            link_matches.append((m.start(),'',html.unescape(m[2]),'html_href'))
        reference_definitions={m[1].lower():m[2].strip('<>') for m in re.finditer(r'^\s{0,3}\[([^\]]+)\]:\s*(<[^>]+>|\S+)',body,re.M)}
        for m in re.finditer(r'(?<!!)\[([^\n]*?)\]\[([^\]]*)\]',body):
            href=reference_definitions.get((m[2] or m[1]).lower())
            if href:link_matches.append((m.start(),m[1],href,'markdown_reference'))
        links=[]
        for offset,label,href,kind in sorted(link_matches):
            url=urllib.parse.urlsplit(href)
            if url.scheme or url.netloc:continue
            if not url.fragment:continue
            target=posixpath.normpath(posixpath.join(posixpath.dirname(path),urllib.parse.unquote(url.path))) if url.path else path
            prior=[a for a in anchors if a['offset']<=offset]
            links.append({'source_path':path,'source_line':body.count('\n',0,offset)+1,'source_anchor_context':prior[-1]['fragment'] if prior else None,'label':label,'href':href,'target_path':target,'target_fragment':urllib.parse.unquote(url.fragment),'is_cross_file':target!=path,'syntax':kind})
        files.append({'material_id':sid,'session_id':session['id'],'frozen_commit':pin,'path':path,'bytes':o['bytes'],'sha256':o['sha256'],'git_blob':o['git_blob'],'current_head_byte_identical':True,'queue_final_sha256_match':(session.get('final_document_sha256')==o['sha256']) if path==PREFIX+paths[0] and session.get('final_document_sha256') else None,'line_count':len(body.splitlines()),'anchors':anchors,'relative_anchor_links':links,'reference_definition_count':len(reference_definitions),'body':body})

by_path={f['path']:f for f in files}
cross=[]
for f in files:
    for l in f['relative_anchor_links']:
        if not l['is_cross_file']:continue
        target=by_path.get(l['target_path'])
        same_source=[a for a in f['anchors'] if a['fragment']==l['target_fragment']]
        target_anchors=[a for a in target['anchors'] if a['fragment']==l['target_fragment']] if target else []
        l.update({'material_id':f['material_id'],'source_commit':f['frozen_commit'],'source_sha256':f['sha256'],'target_in_current_accepted_files':bool(target),'target_commit':target['frozen_commit'] if target else None,'target_sha256':target['sha256'] if target else None,'target_anchor_lines':[a['line'] for a in target_anchors],'target_anchor_kinds':[a['kind'] for a in target_anchors],'fragment_also_defined_in_source':bool(same_source),'source_matching_anchor_lines':[a['line'] for a in same_source],'matches_nearest_source_anchor':l['source_anchor_context']==l['target_fragment'],'classification':'dependency_candidate_only','browser_checked_by_this_inventory':False})
        cross.append(l)
repeated=[]
for sid in records:
    members=[f for f in files if f['material_id']==sid]
    ids=collections.defaultdict(list)
    for f in members:
        for a in f['anchors']:ids[a['fragment']].append({'path':f['path'],'line':a['line'],'kind':a['kind']})
    for fragment,locations in ids.items():
        if len({a['path'] for a in locations})>1:repeated.append({'material_id':sid,'fragment':fragment,'locations':locations})

evidence=[]
for sid,(pin,paths,ev) in records.items():
    for p in ev:
        path=PREFIX+p;o=objects[HEAD+':'+path]
        evidence.append({'material_id':sid,'read_commit':HEAD,'path':path,'bytes':o['bytes'],'sha256':o['sha256'],'git_blob':o['git_blob']})

for f in files:
    del f['body']
    for a in f['anchors']:del a['offset']

inventory={'scope':'feature/dependency inventory only; no browser or defect verdict','canonical_main':HEAD,'repository':'alverstris/PROF-Skill.md-','queue':{'local_path':str(QUEUE),'repo_path':PREFIX+'queue.json','sha256':queue_object['sha256'],'git_blob':queue_object['git_blob'],'local_equals_canonical':True,'closed_material_ids':[s['material_id'] for s in closed]},'method':'Explicit immutable git cat-file --batch object reads; frozen constituents byte-compared with canonical main; only currently accepted Markdown and necessary current identity/acceptance records read. No browser used. Images are listed by acceptance manifests but not image-inspected because bitmap/SVG contents do not create Markdown sibling routes.','limitations':['Matching fragment syntax establishes only a dependency candidate, never GitHub SPA behavior or a defect.','A click can preserve a URL fragment only if the current address already has that fragment; source-position context alone does not prove address state.','Explicit authored HTML IDs/name targets are recorded without claiming GitHub DOM prefix or runtime implementation. Heading fragment normalization, if present, is inferred and separately labeled.','No historical superseded teaching file was read. D016 closure/final-state copies are not counted as additional learner files; the original frozen accepted teaching paths are inventoried.','No evaluation of teaching correctness, complete destination rendering, or reopening/closure decision is made.'],'accepted_files':files,'acceptance_identity_records':evidence,'cross_file_relative_anchor_routes':cross,'repeated_fragments_between_current_sibling_files':repeated,'summary':{'closed_sessions':len(closed),'accepted_markdown_files':len(files),'cross_file_relative_anchor_routes':len(cross),'cross_file_material_ids':sorted({r['material_id'] for r in cross}),'repeated_sibling_fragment_count':len(repeated),'same_fragment_dependency_candidate_routes':sum(r['fragment_also_defined_in_source'] for r in cross),'same_fragment_candidate_material_ids':sorted({r['material_id'] for r in cross if r['fragment_also_defined_in_source']})}}
OUT.mkdir(parents=True,exist_ok=True)
(OUT/'inventory.json').write_text(json.dumps(inventory,indent=2)+'\n')
print(json.dumps(inventory['summary'],indent=2))
for f in files:print(f['material_id'],f['path'],f['sha256'],len(f['anchors']),len(f['relative_anchor_links']))
for r in cross:print(r['material_id'],pathlib.PurePosixPath(r['source_path']).name,':',r['source_line'],r['source_anchor_context'],'->',r['href'],'samefragment',r['fragment_also_defined_in_source'],'contextmatch',r['matches_nearest_source_anchor'])
print('REPEATED',json.dumps(repeated,indent=2))
