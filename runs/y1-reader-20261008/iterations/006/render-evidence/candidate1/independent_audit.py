#!/usr/bin/env python3
"""Read frozen candidate and saved capture; write separate diagnostic evidence."""
from pathlib import Path
from lxml import html
import copy
import difflib
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parent
source = (ROOT/'frozen-teaching.md').read_text()
article_html = (ROOT/'capture-initial/github-article.html').read_text()
dom = html.fromstring(article_html)
normalize = lambda text: re.sub(r'\s+', ' ', text).strip()
MATH = re.compile(r'(?<!\\)\$\$(.*?)\$\$|(?<!\\)\$(?!\$)(.*?)(?<!\\)\$', re.S)
matches = list(MATH.finditer(source))
labels = list(re.finditer(r'<!-- (P\d{3}) -->', source))
def locator(offset):
    return [m[1] for m in labels if m.start() < offset][-1]
source_math = []
typed_counts = {'inline': 0, 'display': 0}
for match in matches:
    kind = 'display' if match[1] is not None else 'inline'
    typed_counts[kind] += 1
    source_math.append({'kind': kind, 'payload': match[1] if kind == 'display' else match[2],
                        'index_1_based': typed_counts[kind], 'locator': locator(match.start()),
                        'line_1_based': source.count('\n', 0, match.start()) + 1})
actual_nodes = dom.xpath('.//math-renderer')
assert len(source_math) == len(actual_nodes)
differences = []
all_math = []
for src, node in zip(source_math, actual_nodes):
    kind = 'display' if node.get('class') == 'js-display-math' else 'inline'
    width = 2 if kind == 'display' else 1
    raw_text = node.text_content()
    assert raw_text.startswith('$'*width) and raw_text.endswith('$'*width)
    actual = raw_text[width:-width]
    rec = {**src, 'actual_kind': kind, 'actual_payload': actual, 'exact': kind == src['kind'] and actual == src['payload']}
    all_math.append(rec)
    if not rec['exact']:
        rec['raw_renderer_html'] = html.tostring(node, encoding='unicode', with_tail=False)
        rec['classification'] = 'angle_entity_text' if actual == src['payload'].replace('<', '&lt;').replace('>', '&gt;') else 'percent_escape_lost' if actual == src['payload'].replace('\\%', '%') else 'other'
        differences.append(rec)

def prose_normalize(text):
    text = re.sub(r'<!-- P\d{3} -->', '', text)
    text = re.sub(r'<a id="[^"]+"></a>', '', text)
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', lambda m: m[1], text)
    text = re.sub(r'^- ', '', text, flags=re.M)
    return normalize(text)
expected_text = prose_normalize(source)
actual_text = normalize(dom.text_content())
text_differences = [{'type': op, 'source': expected_text[a:b], 'actual': actual_text[c:d]}
                    for op,a,b,c,d in difflib.SequenceMatcher(None, expected_text, actual_text, autojunk=False).get_opcodes() if op != 'equal']
counter = iter(range(len(matches)))
masked_source = MATH.sub(lambda m: f'MATHPLACEHOLDER{next(counter)}END', source)
masked_dom = copy.deepcopy(dom)
for i,node in enumerate(masked_dom.xpath('.//math-renderer')):
    node.text = f'MATHPLACEHOLDER{i}END'
    for child in list(node): node.remove(child)
non_math_prose_equal = prose_normalize(masked_source) == normalize(masked_dom.text_content())

source_anchors = list(re.finditer(r'<a id="([^"]+)"></a>', source))
source_anchor_ids = [m[1] for m in source_anchors]
actual_ids = [e.get('id') for e in dom.iter() if e.get('id')]
source_links = []
for m in re.finditer(r'\[([^\]]+)\]\(([^)]+)\)', source):
    source_links.append({'text':m[1], 'href':m[2], 'locator':locator(m.start()), 'offset':m.start()})
actual_links = [{'text':e.text_content(), 'href':e.get('href')} for e in dom.xpath('.//a[@href]')]
assert len(source_links) == len(actual_links)
for src, act in zip(source_links, actual_links):
    act['source_locator'] = src['locator']
    act['exact'] = src['text'] == act['text'] and src['href'] == act['href']

anchor_map = {}
for anchor in source_anchors:
    following = next(m for m in labels if m.start() > anchor.end())
    anchor_map[anchor[1]] = {'source_locator':following[1], 'actual_id':'user-content-'+anchor[1],
                             'actual_target_count':actual_ids.count('user-content-'+anchor[1])}
sections = {}
for i,anchor in enumerate(source_anchors):
    end = source_anchors[i+1].start() if i+1 < len(source_anchors) else len(source)
    sections[anchor[1]] = [l for l in source_links if anchor.end() <= l['offset'] < end]
routes=[]
for i in range(1,7):
    task,hint,solution = f'task-a{i}',f'hint-a{i}',f'solution-a{i}'
    expected_routes=[(task,'#'+hint),(task,'#'+solution),(hint,'#'+task),(solution,'#'+task),(solution,'#'+hint)]
    checks=[]
    for start,target in expected_routes:
        found=[l for l in sections[start] if l['href']==target]
        checks.append({'from_anchor':start,'to_href':target,'source_link_locators':[l['locator'] for l in found],
                       'count':len(found),'target_locator':anchor_map[target[1:]]['source_locator'],
                       'actual_target_count':anchor_map[target[1:]]['actual_target_count'],
                       'pass':len(found)==1 and anchor_map[target[1:]]['actual_target_count']==1})
    routes.append({'task':f'A{i}','task_locator':anchor_map[task]['source_locator'],
                   'hint_locator':anchor_map[hint]['source_locator'],'solution_locator':anchor_map[solution]['source_locator'],
                   'routes':checks,'pass':all(c['pass'] for c in checks)})
grouping = max(source_anchor_ids.index(f'hint-a{i}') for i in range(1,7)) < source_anchor_ids.index('solutions') < min(source_anchor_ids.index(f'solution-a{i}') for i in range(1,7))
checks={'source_locator_comments_exactly_P001_to_P194':[m[1] for m in labels]==[f'P{i:03d}' for i in range(1,195)],
        'all_math_payloads_exact':not differences,'non_math_visible_prose_equal':non_math_prose_equal,
        'full_normalized_text_equal':expected_text==actual_text,
        'no_diagnostic_locator_labels_visible':not re.search(r'\bP\d{3}\b',actual_text),
        'anchors_exact_order_and_unique':actual_ids==['user-content-'+x for x in source_anchor_ids] and len(actual_ids)==len(set(actual_ids)),
        'all_link_text_href_pairs_exact':all(l['exact'] for l in actual_links),
        'all_internal_targets_unique':all(actual_ids.count('user-content-'+l['href'][1:])==1 for l in actual_links if l['href'].startswith('#')),
        'custom_A1_A6_routes_returns_and_solution_to_hint_links':all(r['pass'] for r in routes),
        'all_hints_before_solutions':grouping,
        'no_heading_table_or_explicit_prose_emphasis_elements':not any(dom.xpath('.//'+t) for t in ['h1','h2','h3','h4','h5','h6','table','th','strong','b','em','i'])}
result={'verdict':'FAIL actual frozen math serialization; independent navigation and prose findings reported separately',
        'source_sha256':hashlib.sha256(source.encode()).hexdigest(),'checks':checks,
        'math_counts':{'source':typed_counts,'actual':{'inline':sum(n.get('class')=='js-inline-math' for n in actual_nodes),'display':sum(n.get('class')=='js-display-math' for n in actual_nodes)},
                       'mismatches':len(differences),'by_kind':{k:sum(d['kind']==k for d in differences) for k in ['inline','display']},
                       'by_classification':{k:sum(d['classification']==k for d in differences) for k in ['angle_entity_text','percent_escape_lost','other']}},
        'math_differences':differences,'all_math_comparisons':all_math,'full_text_differences':text_differences,
        'navigation':routes,'anchors':anchor_map,'all_links':actual_links,
        'counts':{'comment_locators':len(labels),'anchors':len(actual_ids),'internal_links':sum(l['href'].startswith('#') for l in actual_links),'external_links':sum(not l['href'].startswith('#') for l in actual_links)},
        'normalization':'Remove only invisible locator comments, source HTML anchor tags, Markdown link destinations and the two unordered-list markers; normalize whitespace. Preserve all TeX characters, dollars and source display delimiter-interior newlines. No additional entity decoding.',
        'helper_scope':'Initial helper only recognizes protected-backtick inline and fenced math. This candidate uses ordinary dollar inline and double-dollar displays. Its zero source-math counts are unsupported-syntax diagnostics, not a valid payload inventory. Its visible-label scanner is not applicable to invisible Pnnn comments.',
        'limits':['Ordinary lxml HTML parse of actual saved article; no browser, client pixels, MathJax execution or clicking.', 'An unchanged source-faithful PDF preview cannot establish that altered GitHub payloads render correctly.']}
(ROOT/'independent-audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'checks':checks,'math_counts':result['math_counts'],'counts':result['counts']}))
