#!/usr/bin/env python3
"""Independent D006 representation evidence; no extra HTML entity decoding."""
from pathlib import Path
import difflib
import hashlib
import importlib.util
import json
import re
import sys
import lxml.html

sys.dont_write_bytecode = True
OUT = Path(__file__).resolve().parent
CAPTURE = OUT / 'capture-initial'
SOURCE = OUT / 'frozen-teaching-v1.md'
HELPER = Path('/workspace/scratch/ac36b9c5ff31/PROF-repo/runs/y1-reader-20261008/tooling/frozen-render-review/frozen_render_review.py')
spec = importlib.util.spec_from_file_location('frozen_helper', HELPER)
helper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper)
source = SOURCE.read_text()
html = (CAPTURE / 'github-article.html').read_text()
page = (CAPTURE / 'github-page.html').read_bytes()
captured = json.loads((CAPTURE / 'markup-audit.json').read_text())
dom = lxml.html.fromstring(html)
normalize = lambda text: re.sub(r'\s+', ' ', text).strip()
sha = lambda data: hashlib.sha256(data).hexdigest()

actual_maths = dom.xpath('.//math-renderer')
math_checks = {}
for kind, pattern, width in [('inline', helper.INLINE, 1), ('display', helper.DISPLAY, 2)]:
    expected = pattern.findall(source)
    actual = [m.text_content()[width:-width] for m in actual_maths if m.get('class') == f'js-{kind}-math']
    math_checks[kind] = {'source_count': len(expected), 'actual_count': len(actual),
                         'all_payloads_exact_in_order': expected == actual,
                         'differences': [{'index_1_based': i, 'source': a, 'actual': b}
                                         for i, (a, b) in enumerate(zip(expected, actual), 1) if a != b]}

# The sole source pipe table has no escaped pipes or pipe-bearing cell math.
# Transform only its documented Markdown row syntax; verify every cell first.
table_match = re.search(r'^\| Curve \|.*?(?=\n\n)', source, re.S | re.M)
assert table_match is not None
table_lines = table_match[0].splitlines()
assert len(table_lines) == 4
source_rows = [[cell.strip() for cell in line.split('|')[1:-1]] for line in table_lines]
assert all(re.fullmatch(r':?-+:?', c) for c in source_rows[1])
semantic_rows = [source_rows[0], *source_rows[2:]]
expected_rows = [[normalize(helper.prose_stream(cell)) for cell in row] for row in semantic_rows]
tables = dom.xpath('.//table')
assert len(tables) == 1
actual_rows = [[normalize(cell.text_content()) for cell in row.xpath('./th|./td')] for row in tables[0].xpath('.//tr')]
table_checks = {'logical_paragraph': '[P17]', 'source_lines': [source.count('\n', 0, table_match.start()) + 1, source.count('\n', 0, table_match.end()) + 1],
                'source_rows': expected_rows, 'actual_rows': actual_rows,
                'all_12_cells_exact_in_order': expected_rows == actual_rows,
                'header_rows': 1, 'body_rows': 2, 'columns': 4}
table_text = '\n'.join(' '.join(row) for row in semantic_rows)
table_aware_source = source[:table_match.start()] + table_text + source[table_match.end():]
expected_text = normalize(helper.prose_stream(table_aware_source))
actual_text = normalize(dom.text_content())
old_expected = normalize(helper.prose_stream(source))
old_differences = [{'type': op, 'source': old_expected[i:j], 'actual': actual_text[k:l]}
                   for op, i, j, k, l in difflib.SequenceMatcher(None, old_expected, actual_text, autojunk=False).get_opcodes() if op != 'equal']

labels = []
ids = []
pending = []
anchor_to_paragraph = {}
links = []
current_label = None
for node in dom.iter():
    if node.tag == 'p':
        match = re.match(r'^\[P\d+\]', node.text_content())
        if match:
            current_label = match[0]
            labels.append(current_label)
            for anchor in pending:
                anchor_to_paragraph[anchor] = current_label
            pending = []
    if node.get('id'):
        ids.append(node.get('id'))
        pending.append(node.get('id'))
    if node.tag == 'a' and node.get('href'):
        links.append({'from': current_label, 'href': node.get('href'), 'text': node.text_content()})
source_ids = re.findall(r'<a id="([^"]+)"></a>', source)
without_math = helper.DISPLAY.sub('', helper.INLINE.sub('', source))
source_links = [{'text': m[1], 'href': m[2]} for m in re.finditer(r'\[([^\]]+)\]\(([^)]+)\)', without_math)]
actual_pairs = [{'text': m['text'], 'href': m['href']} for m in links]

mapping = [
    ('a', '[P09]', '[P09]', '[P45]', '[P51]', '[P51]'),
    ('b', '[P26]', '[P26]', '[P46]', '[P52]', '[P54]'),
    ('c', '[P33]', '[P34]', '[P47]', '[P55]', '[P56]'),
    ('d', '[P40]', '[P40]', '[P48]', '[P57]', '[P59]'),
    ('e', '[P41]', '[P42]', '[P49]', '[P60]', '[P63]'),
]
routes = []
for letter, task, outgoing, hint, solution, solution_return in mapping:
    targets = {'task': f'task-{letter}', 'hint': f'hint-{letter}', 'solution': f'solution-{letter}'}
    check = {
        'task': letter.upper(), 'task_start_paragraph': task, 'outgoing_links_paragraph': outgoing,
        'hint_paragraph': hint, 'solution_start_paragraph': solution, 'solution_return_paragraph': solution_return,
        'anchor_destinations_exact': all(anchor_to_paragraph.get('user-content-' + targets[k]) == p for k, p in [('task', task), ('hint', hint), ('solution', solution)]),
        'task_to_matching_hint_once': sum(m['from'] == outgoing and m['href'] == '#' + targets['hint'] for m in links) == 1,
        'task_to_matching_solution_once': sum(m['from'] == outgoing and m['href'] == '#' + targets['solution'] for m in links) == 1,
        'hint_return_once': sum(m['from'] == hint and m['href'] == '#' + targets['task'] and m['text'] == 'Return to Task ' + letter.upper() for m in links) == 1,
        'solution_return_once': sum(m['from'] == solution_return and m['href'] == '#' + targets['task'] and m['text'] == 'Return to Task ' + letter.upper() for m in links) == 1,
        'exactly_two_named_returns': sum(m['href'] == '#' + targets['task'] and m['text'] == 'Return to Task ' + letter.upper() for m in links) == 2,
    }
    check['pass'] = all(v for v in check.values() if isinstance(v, bool))
    routes.append(check)
hints_before_solutions = max(source_ids.index('hint-' + x) for x in 'abcde') < source_ids.index('solutions') < min(source_ids.index('solution-' + x) for x in 'abcde')
actual_hints_before_solutions = max(ids.index('user-content-hint-' + x) for x in 'abcde') < ids.index('user-content-solutions') < min(ids.index('user-content-solution-' + x) for x in 'abcde')
checks = {
    'frozen_source_matches_expected_hash': sha(SOURCE.read_bytes()) == 'd2946240bb9d5442919d1fb22f1f93b2f7626b69ad2e5a04178c283005f5bfdf',
    'captured_page_hash_exact': sha(page) == captured['github_fetch']['sha256'],
    'reextracted_article_exact': helper.extract_article(page) == html,
    'all_math_payloads_exact': all(v['all_payloads_exact_in_order'] for v in math_checks.values()),
    'all_table_cells_exact': table_checks['all_12_cells_exact_in_order'],
    'complete_text_equal_after_explicit_table_markup_normalization': expected_text == actual_text,
    'labels_exactly_P01_through_P63': labels == [f'[P{i:02d}]' for i in range(1, 64)],
    'all_prefixed_anchor_ids_exact_in_order': ids == ['user-content-' + a for a in source_ids],
    'all_anchor_ids_unique': len(ids) == len(set(ids)),
    'all_link_text_href_pairs_exact_in_order': source_links == actual_pairs,
    'all_internal_targets_unique': all(ids.count('user-content-' + m['href'][1:]) == 1 for m in links if m['href'].startswith('#')),
    'custom_A_to_E_routes_and_returns_exact': all(r['pass'] for r in routes),
    'source_and_actual_hints_grouped_before_solutions': hints_before_solutions and actual_hints_before_solutions,
}
result = {'verdict': 'PASS with documented table-aware source normalization; original helper failure retained',
          'source_sha256': sha(SOURCE.read_bytes()), 'source_bytes': len(SOURCE.read_bytes()),
          'source_origin': 'Direct immutable raw GitHub fetch, not mutable worktree',
          'checks': checks, 'checks_pass': all(checks.values()), 'math': math_checks,
          'table': table_checks, 'A_to_E_navigation': routes,
          'anchor_to_paragraph': anchor_to_paragraph, 'all_links': links,
          'counts': {'logical_paragraphs': len(labels), 'anchors': len(ids), 'internal_links': sum(m['href'].startswith('#') for m in links), 'external_links': sum(not m['href'].startswith('#') for m in links)},
          'initial_helper_diagnosis': {'failed_check': 'complete_text_equal_after_documented_markup_normalization',
              'cause': 'prose_stream retains Markdown pipe-table delimiters and alignment separator; actual HTML table text omits these syntax characters',
              'source_locator': '[P17], source lines 67-70', 'differences': old_differences,
              'original_audit_unchanged': True, 'generic_Q_H_S_checks_not_applicable': True},
          'normalization_added': 'For the sole verified four-column table, remove only outer/inter-cell pipe syntax and the alignment row; retain all 12 cell texts and their order. Then apply existing helper Markdown/whitespace normalization.',
          'html_parsing': 'One ordinary lxml HTML parse; no extra entity-unescape pass',
          'limits': ['Saved server-delivered markup only; client pixels and MathJax execution unobserved.',
                     'Href/ID presence and routing intent checked; live clicking and JavaScript fragment behavior unobserved.']}
(OUT / 'independent-audit.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
assert all(checks.values()), checks
print(json.dumps({'checks_pass': result['checks_pass'], 'counts': result['counts'], 'math': math_checks, 'table_exact': table_checks['all_12_cells_exact_in_order']}))
