"""Inspect the saved official Markdown API response; never claims live pixels."""
from pathlib import Path
from html.parser import HTMLParser
import importlib.util
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
RUN = HERE.parent
REPO = RUN.parents[4]
spec = importlib.util.spec_from_file_location('frozen_review', REPO / 'runs/y1-reader-20261008/tooling/frozen-render-review/frozen_render_review.py')
helper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper)
source = (RUN / 'generation/lesson.md').read_text()
html = (RUN / 'github-api-render.html').read_text()
article = helper.Article()
article.feed(html)

class Names(HTMLParser):
    def __init__(self):
        super().__init__()
        self.names = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'a' and attrs.get('name'):
            self.names.append(attrs['name'])

names = Names()
names.feed(html)
source_names = re.findall(r'<a name="([^"]+)"></a>', source)
source_text = helper.prose_stream(re.sub(r'<a name="[^"]+"></a>', '', source))
# The six source labels are Markdown ordered-list items. Their numerals are
# represented by ol/start attributes, not text nodes. Check them separately.
source_list_numbers = re.findall(r'^(\d+)\. ', source_text, re.M)
source_text = re.sub(r'^\d+\. ', '', source_text, flags=re.M)
actual_list_numbers = []
for attrs in re.findall(r'<ol\b([^>]*)>', html):
    match = re.search(r' start="(\d+)"', attrs)
    actual_list_numbers.append(match[1] if match else '1')
normalize = lambda text: re.sub(r'\s+', ' ', text).strip()
original, _ = helper.audit_article(source, html)
checks = {key: original['checks'][key] for key in [
    'all_inline_math_payloads_exact', 'all_display_math_payloads_exact',
    'all_internal_hrefs_match_source_in_order',
    'plain_prose_no_bold_italic_or_heading_tags', 'source_has_no_atx_headings']}
checks.update({
    'complete_prose_and_math_stream_exact': normalize(source_text) == normalize(''.join(article.text)),
    'six_ordered_label_numbers_preserved': source_list_numbers == actual_list_numbers == [str(i) for i in range(1, 7)],
    'named_anchors_preserved_in_order': names.names == ['user-content-' + name for name in source_names],
    'all_38_internal_targets_have_one_github_prefixed_named_anchor': all(names.names.count('user-content-' + link['href'][1:]) == 1 for link in article.links if link['href'].startswith('#')),
    'hints_group_precedes_solutions_group': source.index('name="hint-p6"') < source.index('name="solution-p1"'),
})
routes = []
for n in range(1, 7):
    route = {'task': f'p{n}'}
    for anchor, targets in [(f'p{n}', [f'hint-p{n}', f'solution-p{n}']), (f'hint-p{n}', [f'p{n}', f'solution-p{n}']), (f'solution-p{n}', [f'p{n}'])]:
        block = html.split(f'<a name="user-content-{anchor}"></a>', 1)[1].split('<a name=', 1)[0]
        route[anchor] = {target: f'href="#{target}"' in block for target in targets}
    routes.append(route)
checks['six_task_hint_solution_routes_match'] = all(all(value.values()) for route in routes for key, value in route.items() if key != 'task')
result = {
    'scope': 'Official GitHub Markdown API response to the exact frozen full source; not the repository blob page and not live visual inspection.',
    'source_sha256': hashlib.sha256(source.encode()).hexdigest(),
    'api_response_sha256': hashlib.sha256(html.encode()).hexdigest(),
    'inline_count': 184, 'display_count': 26, 'named_anchor_count': len(source_names),
    'internal_link_count': sum(link['href'].startswith('#') for link in article.links),
    'checks': checks, 'all_checks_pass': all(checks.values()), 'routes': routes,
    'helper_false_flags_explained': 'The earlier helper recognizes id anchors and [P01] labels, whereas this frozen source uses name anchors and P1 labels. It also does not remove numbered-list markers when comparing text nodes. This audit keeps the original output and explicitly checks the actual source format; it does not edit the teaching.',
    'remaining_unverified': ['live MathJax/CSS pixels', 'actual repository richText response', 'click/JavaScript hash handling', 'embedded image scaling and live image loading'],
}
(HERE / 'api-format-audit.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({key: result[key] for key in ['source_sha256', 'checks', 'all_checks_pass']}, indent=2))
