from pathlib import Path
import hashlib,json,difflib,shutil
p=Path(__file__).resolve().parents[1]
src=p/'verified-prof'; dst=p/'release-prof'
for f in src.rglob('*'):
    if f.is_file():
        g=dst/f.relative_to(src);g.parent.mkdir(parents=True,exist_ok=True);g.write_bytes(f.read_bytes())
changes={
'SKILL.md': ('For LaTeX/PDF read', 'For linked GitHub teaching files, give anchors document-specific names so corresponding prompts, hints and solutions do not reuse the same fragment across sibling files. Check actual forward and return clicks after the destination has settled, including a later target reached from an already-fragmented URL. Verify that the intended content is visible, not merely that the URL and anchor exist. Preserve a failed route and follow the active repair mode; see execution-protocol.md for the destination check.'),
'references/execution-protocol.md': ('Before final delivery, reconcile', 'For linked teaching/help, inventory the source and target file and fragment for each route. In GitHub Markdown, use distinct document-specific anchor names across sibling files. Exercise ordinary forward and return clicks, including later targets below the initial viewport and successive cross-file navigation from a URL that already has a fragment. After the article and rendering settle, observe the matching target in the viewport; a correct href, preserved anchor, loaded file or manually opened deep URL does not establish the click route. Separate transient load states and screenshot-induced scrolling from a reproducible settled failure. If an alternative is needed, verify it in a separate bounded destination fixture before using it, and recheck the whole final artifact. Reopen earlier acceptance only where inspection establishes the demonstrated dependency; syntax presence alone is not a browser failure.'),
'references/sasis.md': ('Shared tools remain technically available', 'For retrieval of linked or interleaved teaching, prepare an exact ordered route before dispatch: file identities, byte or line ranges with their convention, and each complete figure at its first-use position. Verify that the route covers every text byte and constituent, including prompts, help and endings, without exposing a later section early. Supply this subject-free routing metadata, not excerpts, answers or findings, alongside the two subject inputs. The reader retrieves only the next bounded slice or figure, records its actual access, and then advances; do not guess heading boundaries or batch across a scheduled exercise or figure. Before admitting chronological evidence, compare actual ordered access with that route as well as total coverage. Preserve accidental early exposure or delayed required figure access as a reader-procedure failure; rereading cannot restore first exposure. Complete the audit, repair routing, and dispatch a fresh reader on the unchanged frozen inputs. This recovery does not repair a teaching defect or waive the publication-first fresh-generation rule for a verified material iteration failure.'),
'references/sasis/student-role.txt': ('At every substantive definition', 'When exact routing metadata is supplied, retrieve only its next text slice or complete figure before advancing. Do not guess boundaries or include later sections in a larger read. Inspect each figure at its listed first-use position. Log actual ordered access and disclose any early exposure or delayed figure inspection; rereading does not restore first exposure.'),
'references/sasis/student-testing-contract.txt': ('A path, hash, window-size guess', 'For linked or interleaved retrieval, supply the exact ordered, subject-free file/range/figure route required by sasis.md. Compare the actual access sequence and complete coverage before admission. Preserve order deviations; complete the audit and use a fresh reader after routing repair, without changing the frozen teaching.')
}
for name,(marker,addition) in changes.items():
    f=dst/name;b=f.read_bytes();nl=b'\r\n' if b'\r\n' in b else b'\n';target=marker.encode();assert b.count(target)==1,name
    b=b.replace(target,addition.encode()+nl+nl+target);f.write_bytes(b)
for name,old,new in [
('SKILL.md','version: "2026-10-11-r30"','version: "2026-10-11-r31"'),
('references/sasis.md','Protocol revision: 2026-10-10-r24.','Protocol revision: 2026-10-11-r31.'),
('references/sasis/student-testing-contract.txt','revision 2026-10-10-r24','revision 2026-10-11-r31'),
('references/sasis/profile-manifest.json','"protocol_revision": "2026-10-10-r24"','"protocol_revision": "2026-10-11-r31"')]:
    f=dst/name;b=f.read_bytes();assert b.count(old.encode())==1;f.write_bytes(b.replace(old.encode(),new.encode()))
rows=[];diff=[]
for f in sorted(src.rglob('*')):
    if not f.is_file():continue
    rel=str(f.relative_to(src));old=f.read_bytes();new=(dst/rel).read_bytes();changed=old!=new
    rows.append({'path':rel,'bytes':len(new),'sha256':hashlib.sha256(new).hexdigest(),'git_blob':hashlib.sha1(b'blob '+str(len(new)).encode()+b'\0'+new).hexdigest(),'changed':changed})
    if changed:diff.extend(difflib.unified_diff(old.decode().splitlines(True),new.decode().splitlines(True),fromfile='r30/'+rel,tofile='r31/'+rel))
assert len(rows)==36
(p/'release-package-manifest.json').write_text(json.dumps({'version':'2026-10-11-r31','status':'candidate_pending_root_review_and_publication','file_count':36,'change':'General destination navigation and sequential reader delivery/admission repairs; no subject-matter rule or baseline change','files':rows},indent=2)+'\n')
(p/'repair/r30-to-r31.diff').write_text(''.join(diff))
print(json.dumps({'file_count':len(rows),'changed':[r['path'] for r in rows if r['changed']],'diff_sha256':hashlib.sha256((p/'repair/r30-to-r31.diff').read_bytes()).hexdigest()},indent=2))
