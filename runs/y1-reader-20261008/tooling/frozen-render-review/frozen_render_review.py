#!/usr/bin/env python3
"""Frozen GitHub representation evidence and internal PDF preview preparation.

Generalized from the D002 v1 checks. Never claims live-browser or visual review.
Requires Python stdlib, Pandoc, pdflatex, pdfinfo, pdftotext and pdftoppm.
"""
import argparse
from collections import Counter
from html.parser import HTMLParser
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
import urllib.parse
import urllib.request

INLINE = re.compile(r'\$`(.*?)`\$', re.S)
DISPLAY = re.compile(r'^```math\n(.*?)\n```', re.S | re.M)
LIMITS = [
    'Actual GitHub server-delivered markup, not live client pixels or MathJax execution.',
    'GitHub-prefixed destination markup is checked; clicking and JavaScript fragment handling are unobserved.',
    'Local pdflatex preview is a secondary renderer, not evidence of GitHub CSS, responsive layout or hyperlink parity.',
    'Every complete final PDF page still requires visual opening and inspection; automatic evidence is not visual sign-off.',
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def fetch(url):
    request = urllib.request.Request(url, headers={'User-Agent': 'PROF frozen representation verification'})
    with urllib.request.urlopen(request, timeout=50) as response:
        data = response.read()
        return data, {'requested_url': url, 'final_url': response.url,
                      'status': response.status, 'bytes': len(data), 'sha256': sha(data)}


class EmbeddedData(HTMLParser):
    def __init__(self):
        super().__init__()
        self.active = False
        self.parts = []

    def handle_starttag(self, tag, attrs):
        if tag == 'script' and dict(attrs).get('data-target') == 'react-app.embeddedData':
            self.active = True

    def handle_data(self, data):
        if self.active:
            self.parts.append(data)

    def handle_endtag(self, tag):
        if tag == 'script':
            self.active = False


def extract_article(page):
    parser = EmbeddedData()
    parser.feed(page.decode('utf-8'))
    data = json.loads(''.join(parser.parts))
    return data['payload']['codeViewBlobRoute']['richText']


class Article(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.tags = Counter()
        self.text, self.ids, self.links, self.paragraphs, self.maths, self.images = [], [], [], [], [], []
        self.paragraph = self.link = self.math = None
        self.pending_ids = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags[tag] += 1
        if tag == 'p':
            self.paragraph = {'text': '', 'ids': self.pending_ids, 'links': []}
            self.pending_ids = []
            self.paragraphs.append(self.paragraph)
        if 'id' in attrs:
            self.ids.append(attrs['id'])
            (self.paragraph['ids'] if self.paragraph is not None else self.pending_ids).append(attrs['id'])
        if tag == 'a' and 'href' in attrs:
            self.link = {'href': attrs['href'], 'text': ''}
            self.links.append(self.link)
            if self.paragraph is not None:
                self.paragraph['links'].append(self.link)
        if tag == 'math-renderer':
            self.math = {'type': attrs.get('class'), 'text': ''}
            self.maths.append(self.math)
        if tag == 'img':
            self.images.append(attrs)

    def handle_data(self, data):
        self.text.append(data)
        for item in [self.paragraph, self.link, self.math]:
            if item is not None:
                item['text'] += data

    def handle_endtag(self, tag):
        if tag == 'p': self.paragraph = None
        if tag == 'a': self.link = None
        if tag == 'math-renderer': self.math = None


def math_payloads(source):
    return {'inline': INLINE.findall(source), 'display': DISPLAY.findall(source)}


def convert_math(source):
    converted = INLINE.sub(lambda m: '$' + m[1] + '$', source)
    return DISPLAY.sub(lambda m: '$$\n' + m[1] + '\n$$', converted)


def prose_stream(source):
    # Protect TeX before removing Markdown links: TeX can contain [..](..).
    protected = []
    def protect(match, delimiter):
        protected.append(delimiter + match[1] + delimiter)
        return f'MATHPLACEHOLDER{len(protected)-1}END'
    text = INLINE.sub(lambda m: protect(m, '$'), source)
    text = DISPLAY.sub(lambda m: protect(m, '$$'), text)
    text = re.sub(r'<a id="[^"]+"></a>', '', text)
    text = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', text)
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', lambda m: m[1], text)
    return re.sub(r'MATHPLACEHOLDER(\d+)END', lambda m: protected[int(m[1])], text)


def audit_article(source, article_html):
    article = Article()
    article.feed(article_html)
    actual_text = ''.join(article.text)
    expected = math_payloads(source)
    actual = {
        'inline': [m['text'][1:-1] for m in article.maths if m['type'] == 'js-inline-math'],
        'display': [m['text'][2:-2] for m in article.maths if m['type'] == 'js-display-math'],
    }
    normalize = lambda text: re.sub(r'\s+', ' ', text).strip()
    source_labels = re.findall(r'^\[P\d+\]', source, re.M)
    actual_labels = re.findall(r'\[P\d+\]', actual_text)
    source_ids = re.findall(r'<a id="([^"]+)"></a>', source)
    anchor_to_paragraph, pending = {}, []
    for p in article.paragraphs:
        pending.extend(p['ids'])
        match = re.match(r'\[P\d+\]', p['text'])
        if match:
            for anchor in pending:
                anchor_to_paragraph[anchor] = match[0]
            pending = []
    link_checks = []
    for p in article.paragraphs:
        match = re.match(r'\[P\d+\]', p['text'])
        label = match[0] if match else None
        for link in p['links']:
            if link['href'].startswith('#'):
                target = 'user-content-' + link['href'][1:]
                link_checks.append({'from': label, **link, 'github_prefixed_id': target,
                                    'target_paragraph': anchor_to_paragraph.get(target),
                                    'present_once': article.ids.count(target) == 1})
    # Compare every source internal href in order, including all return links.
    without_math = DISPLAY.sub('', INLINE.sub('', source))
    source_internal = re.findall(r'\[[^\]]+\]\((#[^)]+)\)', without_math)
    actual_internal = [link['href'] for link in article.links if link['href'].startswith('#')]
    question_ids = [i for i in source_ids if re.fullmatch(r'q\d+', i)]
    question_checks = []
    for q in question_ids:
        n = q[1:]
        q_label = anchor_to_paragraph.get('user-content-' + q)
        question_checks.append({
            'question': q, 'paragraph': q_label,
            'hint_target': anchor_to_paragraph.get('user-content-h' + n),
            'solution_target': anchor_to_paragraph.get('user-content-s' + n),
            'question_to_hint': any(l['from'] == q_label and l['href'] == '#h' + n for l in link_checks),
            'question_to_solution': any(l['from'] == q_label and l['href'] == '#s' + n for l in link_checks),
            'return_link_count': sum(l['text'].lower() == 'return to ' + q and l['href'] == '#' + q for l in link_checks),
        })
    hints = [i for i in source_ids if re.fullmatch(r'h\d+', i)]
    solutions = [i for i in source_ids if re.fullmatch(r's\d+', i)]
    group_order = (not hints or not solutions or
                   max(source_ids.index(i) for i in hints) < min(source_ids.index(i) for i in solutions))
    checks = {
        'complete_text_equal_after_documented_markup_normalization': normalize(prose_stream(source)) == normalize(actual_text),
        'paragraph_labels_match_source_in_order': source_labels == actual_labels,
        'paragraph_labels_unique': len(actual_labels) == len(set(actual_labels)),
        'all_inline_math_payloads_exact': expected['inline'] == actual['inline'],
        'all_display_math_payloads_exact': expected['display'] == actual['display'],
        'all_anchor_ids_match_source_in_order': article.ids == ['user-content-' + i for i in source_ids],
        'all_internal_hrefs_match_source_in_order': source_internal == actual_internal,
        'all_internal_targets_present_once': all(l['present_once'] for l in link_checks),
        'plain_prose_no_bold_italic_or_heading_tags': not any(article.tags[t] for t in ['em','i','b','strong','h1','h2','h3','h4','h5','h6']),
        'source_has_no_atx_headings': not re.search(r'^#{1,6}\s', source, re.M),
        'all_q_h_s_matching_links_and_returns': all(q['hint_target'] and q['solution_target'] and q['question_to_hint'] and q['question_to_solution'] and q['return_link_count'] == 2 for q in question_checks),
        'hint_entries_all_before_solution_entries': group_order,
    }
    result = {
        'checks': checks, 'checks_pass': all(checks.values()),
        'source_bytes': len(source.encode()), 'source_sha256': sha(source.encode()),
        'actual_github_article_tags': dict(article.tags), 'paragraph_labels': actual_labels,
        'math': {kind: {'source_count': len(expected[kind]), 'github_count': len(actual[kind]),
                       'exact_all': expected[kind] == actual[kind],
                       'source_payloads': expected[kind], 'github_payloads': actual[kind]}
                 for kind in expected},
        'anchor_to_paragraph': anchor_to_paragraph,
        'internal_link_count': len(link_checks), 'all_internal_link_checks': link_checks,
        'questions': question_checks, 'hints': hints, 'solutions': solutions,
        'image_markup': article.images, 'limitations': LIMITS,
    }
    return result, article


def immutable_paths(url):
    parsed = urllib.parse.urlparse(url)
    match = re.fullmatch(r'/([^/]+)/([^/]+)/blob/([0-9a-fA-F]{40})/(.+)', parsed.path)
    if parsed.scheme != 'https' or parsed.netloc != 'github.com' or not match or parsed.query or parsed.fragment:
        raise ValueError('--url must be an immutable https://github.com/OWNER/REPO/blob/40_HEX_COMMIT/PATH URL')
    owner, repo, commit, path = match.groups()
    raw_root = f'https://raw.githubusercontent.com/{owner}/{repo}/{commit}/'
    return {'owner': owner, 'repo': repo, 'commit': commit, 'path': path, 'raw_root': raw_root}


def image_overrides(values):
    mapping = {}
    for value in values:
        reference, separator, filename = value.partition('=')
        if not separator or not reference or not filename:
            raise ValueError('--image must be MARKDOWN_RELATIVE_REFERENCE=/absolute/local/image.png')
        mapping[reference] = Path(filename).resolve()
    return mapping


def verify_images(source_path, source, article, frozen, overrides, out):
    references = re.findall(r'!\[[^\]]*\]\(([^)]+)\)', source)
    if len(references) != len(article.images):
        raise ValueError('Source and actual article image counts differ')
    if set(overrides) - set(references):
        raise ValueError('An --image override does not match a source Markdown image reference')
    results = []
    for reference, markup in zip(references, article.images):
        rel = PurePosixPath(reference)
        if rel.is_absolute() or '..' in rel.parts or urllib.parse.urlparse(reference).scheme:
            raise ValueError('This existing workflow supports relative constituent image paths without .. only')
        local = overrides.get(reference, source_path.parent / reference)
        expected = local.read_bytes()
        repo_path = str(PurePosixPath(frozen['path']).parent / rel)
        wanted_src = f"/{frozen['owner']}/{frozen['repo']}/raw/{frozen['commit']}/{repo_path}"
        if markup.get('src') != wanted_src:
            raise ValueError(f'Image markup does not reference the expected frozen path: {reference}')
        data, fetch_record = fetch(frozen['raw_root'] + repo_path)
        destination = out / reference
        if destination.resolve() == local.resolve():
            raise ValueError('Output image would overwrite its input')
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(data)
        results.append({'reference': reference, 'local_path': str(local), 'local_sha256': sha(expected),
                        'local_bytes': len(expected), 'actual_markup': markup, **fetch_record,
                        'exactly_matches_local_constituent': data == expected})
    write_json(out / 'image-fetch.json', results)
    if not all(i['exactly_matches_local_constituent'] for i in results):
        raise ValueError('A frozen remote image does not match its local constituent')
    return results


def run(command, out, log_name=None):
    result = subprocess.run(command, cwd=out, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if log_name:
        (out / log_name).write_text(result.stdout)
    if result.returncode:
        raise RuntimeError(f'Command failed ({result.returncode}): {command}; see {log_name or result.stdout}')
    return result.stdout


def verify_ast_math(ast, expected):
    values = []
    def visit(obj):
        if isinstance(obj, dict):
            if obj.get('t') == 'Math': values.append(obj['c'])
            for value in obj.values(): visit(value)
        elif isinstance(obj, list):
            for value in obj: visit(value)
    visit(ast)
    return {
        'inline_payloads_exact': [v[1] for v in values if v[0]['t'] == 'InlineMath'] == expected['inline'],
        'display_payloads_exact_after_removing_conversion_wrapper_newlines':
            [v[1][1:-1] for v in values if v[0]['t'] == 'DisplayMath'] == expected['display'],
    }


def prepare_preview(source, out):
    converted = convert_math(source)
    (out / 'preview.md').write_text(converted)
    (out / 'preview-header.tex').write_text('\\providecommand{\\gt}{>}\n\\providecommand{\\lt}{<}\n')
    ast = json.loads(run(['pandoc', 'preview.md', '-f', 'markdown', '-t', 'json'], out))
    write_json(out / 'preview-ast.json', ast)
    ast_checks = verify_ast_math(ast, math_payloads(source))
    if not all(ast_checks.values()):
        raise ValueError('Pandoc AST did not retain every mathematical payload')
    run(['pandoc', 'preview.md', '-f', 'markdown', '-s', '-V', 'fontsize=11pt', '-V',
         'geometry:margin=25mm', '-H', 'preview-header.tex', '--resource-path=.', '-o', 'preview.tex'], out, 'pandoc.txt')
    for n in [1, 2]:
        run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error', '-jobname=preview', 'preview.tex'], out, f'pdflatex-pass{n}.txt')
    info = run(['pdfinfo', 'preview.pdf'], out, 'pdfinfo.txt')
    page_count = int(re.search(r'^Pages:\s+(\d+)', info, re.M)[1])
    run(['pdftoppm', '-r', '120', '-png', 'preview.pdf', 'page'], out, 'pdftoppm.txt')
    run(['pdftotext', '-layout', 'preview.pdf', 'preview-text.txt'], out)
    pdf_text = (out / 'preview-text.txt').read_text()
    diagnostics = re.findall(r'^.*(?:Overfull|Underfull|Warning|Missing|undefined|!).*$', (out / 'preview.log').read_text(), re.M)
    # These are inspection candidates, never automatically marked visually passed.
    page_text = pdf_text.split('\f')
    return {
        'role': 'Internal preview QA only; source Markdown remains the requested product.',
        'conversion': 'Only protected-inline and fenced-math delimiters changed; all mathematical payloads retained.',
        'pandoc_ast_checks': ast_checks, 'preview_md_sha256': sha(converted.encode()),
        'pdf_sha256': sha((out / 'preview.pdf').read_bytes()), 'page_count': page_count,
        'font_size_pt': 11, 'margins_mm': 25, 'page_size': 'US Letter (Pandoc default)',
        'log_diagnostics': diagnostics,
        'pdf_paragraph_labels_match_source': re.findall(r'\[P\d+\]', pdf_text) == re.findall(r'^\[P\d+\]', source, re.M),
        'full_page_visual_review': 'PENDING; open every complete final page before recording findings',
        'page_inspections': [{'page': i, 'image': f'page-{i:0{len(str(page_count))}d}.png',
                              'paragraph_labels_starting_on_page': re.findall(r'\[P\d+\]', page_text[i-1]),
                              'complete_page_viewed': False, 'findings': None}
                             for i in range(1, page_count+1)],
        'preview_only_differences_to_consider': [
            'Pandoc may promote image alt text to a figure caption and float the figure.',
            'Page breaks may separate a paragraph and display; this does not establish a GitHub defect.',
            'Hint and solution groups need not occupy different PDF pages.',
        ],
        'hyperlink_parity_claimed': False, 'limitations': LIMITS,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, required=True)
    parser.add_argument('--url', required=True, help='Immutable GitHub blob URL containing a full 40-hex commit')
    parser.add_argument('--out', type=Path, required=True, help='New or empty scratch evidence directory')
    parser.add_argument('--image', action='append', default=[], metavar='REFERENCE=LOCAL_PATH', help='Optional repeatable constituent image path override')
    parser.add_argument('--markup-only', action='store_true', help='Fetch/check actual markup and image identity without creating a PDF')
    args = parser.parse_args()
    source_path, out = args.source.resolve(), args.out.resolve()
    frozen = immutable_paths(args.url)
    overrides = image_overrides(args.image)
    if out.exists() and any(out.iterdir()):
        parser.error('--out must be new or empty; prior frozen evidence is never overwritten')
    source_bytes = source_path.read_bytes()
    source = source_bytes.decode('utf-8')
    out.mkdir(parents=True, exist_ok=True)
    page, page_fetch = fetch(args.url)
    (out / 'github-page.html').write_bytes(page)
    article_html = extract_article(page)
    (out / 'github-article.html').write_text(article_html)
    audit, article = audit_article(source, article_html)
    (out / 'github-article-text.txt').write_text(''.join(article.text))
    audit.update({'url': args.url, 'frozen_commit': frozen['commit'], 'github_fetch': page_fetch})
    write_json(out / 'markup-audit.json', audit)
    raw, raw_fetch = fetch(frozen['raw_root'] + frozen['path'])
    raw_fetch['exactly_matches_local_frozen_source'] = raw == source_bytes
    write_json(out / 'source-fetch.json', raw_fetch)
    if raw != source_bytes:
        raise ValueError('Actual frozen raw source does not match the supplied local source')
    images = verify_images(source_path, source, article, frozen, overrides, out)
    record = {'source_path': str(source_path), 'immutable_url': args.url, 'frozen_commit': frozen['commit'],
              'source': raw_fetch, 'images': images, 'actual_markup_checks': audit['checks'],
              'actual_markup_checks_pass': audit['checks_pass'], 'live_github_pixels_mathjax_navigation': 'UNOBSERVED',
              'preview': None, 'limitations': LIMITS}
    write_json(out / 'preview-check.json', record)
    if not audit['checks_pass']:
        raise ValueError('Actual markup check failed; inspect markup-audit.json before previewing')
    if not args.markup_only:
        record['preview'] = prepare_preview(source, out)
        write_json(out / 'preview-check.json', record)
    if source_path.read_bytes() != source_bytes:
        raise ValueError('Source changed while review evidence was prepared; freeze must be re-established')
    print(json.dumps({'out': str(out), 'markup_checks_pass': True, 'image_count': len(images),
                      'inline_math_count': audit['math']['inline']['source_count'],
                      'display_math_count': audit['math']['display']['source_count'],
                      'page_count': record['preview']['page_count'] if record['preview'] else None,
                      'visual_review': 'PENDING' if record['preview'] else 'NOT_PREPARED',
                      'live_github': 'UNOBSERVED'}))


if __name__ == '__main__':
    main()
