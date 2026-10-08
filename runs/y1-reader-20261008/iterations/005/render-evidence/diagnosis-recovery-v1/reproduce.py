#!/usr/bin/env python3
"""Read-only reproduction of the D005 captured serialization diagnosis.

Writes only diagnosis.json beside this script. No fetch, preview or extra HTML
unescape is performed. The existing helper and frozen evidence are not changed.
"""
from pathlib import Path
import difflib
import hashlib
import importlib.util
import json
import re
import subprocess
import sys

sys.dont_write_bytecode = True
ROOT = Path('/workspace/scratch/ac36b9c5ff31')
REPO = ROOT / 'PROF-repo'
SOURCE = REPO / 'runs/y1-reader-20261008/iterations/005/teaching-v1.md'
HELPER = REPO / 'runs/y1-reader-20261008/tooling/frozen-render-review/frozen_render_review.py'
CAPTURE = ROOT / 'prof-readability/d005-render-review/v1'
OUT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('frozen_helper', HELPER)
helper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper)
source_bytes = SOURCE.read_bytes()
source = source_bytes.decode('utf-8')
article_html = (CAPTURE / 'github-article.html').read_text()
page_bytes = (CAPTURE / 'github-page.html').read_bytes()
saved_audit = json.loads((CAPTURE / 'markup-audit.json').read_text())
source_fetch = json.loads((CAPTURE / 'source-fetch.json').read_text())
audit, article = helper.audit_article(source, article_html)
sha = lambda data: hashlib.sha256(data).hexdigest()
normalize = lambda value: re.sub(r'\s+', ' ', value).strip()

# An independent ordinary HTML parser, with no post-parse entity decoding.
import lxml.html
dom = lxml.html.fromstring(article_html)
dom_maths = dom.xpath('.//math-renderer')
raw_maths = list(re.finditer(r'<math-renderer\b[^>]*>(.*?)</math-renderer>', article_html, re.S))
source_labels = list(re.finditer(r'^\[P\d+\]', source, re.M))
mismatches = []
for kind, pattern, wrapper in [('inline', helper.INLINE, 1), ('display', helper.DISPLAY, 2)]:
    expected = list(pattern.finditer(source))
    typed_raw = [m for m in raw_maths if f'class="js-{kind}-math"' in m[0]]
    actual = audit['math'][kind]['github_payloads']
    for ordinal, (match, observed, raw) in enumerate(zip(expected, actual, typed_raw), 1):
        if match[1] == observed:
            continue
        label = [m for m in source_labels if m.start() <= match.start()][-1]
        label_end = next((m.start() for m in source_labels if m.start() > label.start()), len(source))
        block_matches = [m for m in expected if label.start() <= m.start() < label_end]
        mismatches.append({
            'kind': kind, 'global_math_ordinal_1_based': ordinal,
            'paragraph': label[0], 'within_paragraph_math_ordinal_1_based': block_matches.index(match) + 1,
            'source_line_1_based': source.count('\n', 0, match.start()) + 1,
            'source_column_1_based': match.start() - source.rfind('\n', 0, match.start()),
            'source_payload': match[1], 'ordinary_html_parsed_payload': observed,
            'raw_article_inner_html': raw[1],
            'raw_article_html_character_offset_0_based': raw.start(),
        })

expected_text = normalize(helper.prose_stream(source))
actual_text = normalize(''.join(article.text))
text_differences = []
for tag, i, j, k, l in difflib.SequenceMatcher(None, expected_text, actual_text, autojunk=False).get_opcodes():
    if tag != 'equal':
        text_differences.append({
            'type': tag, 'source': expected_text[i:j], 'ordinary_html_parsed': actual_text[k:l],
            'normalized_source_offset_0_based': i, 'normalized_actual_offset_0_based': k,
            'source_context': expected_text[max(0, i-35):min(len(expected_text), j+35)]})
commit = saved_audit['frozen_commit']
git_read = subprocess.run(['git', 'show', f'{commit}:{SOURCE.relative_to(REPO)}'], cwd=REPO,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
result = {
    'status': 'FAIL: actual frozen serialized inline payload mismatch; live client appearance unobserved',
    'immutable_url': saved_audit['url'], 'frozen_commit': commit,
    'source_path': str(SOURCE), 'helper_path': str(HELPER),
    'method': 'JSON extraction followed by ordinary HTML parsing; no extra entity-unescape pass',
    'source_bytes': len(source_bytes), 'source_sha256': sha(source_bytes),
    'input_file_sha256': {str(path): sha(path.read_bytes()) for path in [SOURCE, HELPER, *[CAPTURE / name for name in [
        'github-page.html', 'github-article.html', 'markup-audit.json', 'source-fetch.json']]]},
    'identity_checks': {
        'local_source_hash_matches_captured_audit': sha(source_bytes) == saved_audit['source_sha256'],
        'local_source_hash_matches_source_fetch_record': sha(source_bytes) == source_fetch['sha256'],
        'source_fetch_record_reported_exact_match': source_fetch['exactly_matches_local_frozen_source'],
        'page_hash_matches_captured_fetch_record': sha(page_bytes) == saved_audit['github_fetch']['sha256'],
        'article_reextracted_from_page_equals_saved_article': helper.extract_article(page_bytes) == article_html,
        'recomputed_math_audit_equals_saved_audit': audit['math'] == saved_audit['math'],
        'recomputed_all_checks_equal_saved_checks': audit['checks'] == saved_audit['checks'],
        'independent_lxml_all_text_equals_helper': dom.text_content() == ''.join(article.text),
        'independent_lxml_math_text_equals_helper': [m.text_content() for m in dom_maths] == [m['text'] for m in article.maths],
    },
    'optional_local_git_object_check': {
        'returncode': git_read.returncode,
        'stderr': git_read.stderr.decode('utf-8').strip(),
        'equal_if_available': source_bytes == git_read.stdout if git_read.returncode == 0 else None,
        'interpretation': 'Local object lookup is supplementary; captured HTTP source identity is recorded separately.'},
    'counts': {'source_inline': 280, 'actual_inline': 280, 'matching_inline': 267, 'mismatching_inline': 13,
               'source_display': 23, 'actual_display': 23, 'matching_display': 23,
               'affected_logical_paragraphs': len(set(m['paragraph'] for m in mismatches)),
               'unequal_normalized_text_spans': len(text_differences)},
    'mismatches': mismatches, 'normalized_text_differences': text_differences,
    'all_text_differences_are_observed_angle_entity_spellings': all(
        (d['source'], d['ordinary_html_parsed']) in [('<', '&lt;'), ('>', '&gt;')] for d in text_differences),
    'captured_checks': audit['checks'],
    'limits': ['Frozen saved server response only; no new network fetch.',
               'Live GitHub client pixels, client entity handling, MathJax execution and link clicking unobserved.',
               'No PDF generated or inspected; no teaching-content review performed.'],
}
(OUT / 'diagnosis.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
assert all(result['identity_checks'].values())
assert len(mismatches) == 13 and len(text_differences) == 17
assert result['all_text_differences_are_observed_angle_entity_spellings']
print(json.dumps({'output': str(OUT / 'diagnosis.json'), 'mismatches': len(mismatches),
                  'identity_checks_pass': True, 'normalized_text_differences': len(text_differences)}))
