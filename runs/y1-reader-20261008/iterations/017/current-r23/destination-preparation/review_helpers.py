"""Preparation helpers only; no D008 source has been opened or checked.

Pure parsers and recorder helpers. There is deliberately no runner, input path,
network access, D008 assertion, fixed task count, or gate verdict.
"""
from collections import Counter
from html.parser import HTMLParser
from itertools import zip_longest
from pathlib import Path
import difflib
import hashlib
import json
import re

# Order matters: fences and protected inline forms precede ordinary dollars.
# Fence boundary newlines belong to Markdown syntax, not to fenced TeX content.
MATH = re.compile(
    r'(?P<fence>^```math\r?\n(?P<fence_body>.*?)\r?\n```[ \t]*$)'
    r'|(?P<protected>\$`(?P<protected_body>.*?)`\$)'
    r'|(?P<display>(?<!\\)\$\$(?P<display_body>.*?)\$\$)'
    r'|(?P<inline>(?<![\\$])\$(?![$`])(?P<inline_body>.*?)(?<!\\)\$(?!\$))',
    re.S | re.M,
)
LABEL = re.compile(r'<!--\s*(P\d+)\s*-->')


def math_tokens(source):
    """Retain exact payload, type, source span, format, and preceding label.

    Supports the documented formats only. Caller must separately inspect code
    spans/fences, escaped-dollar usage and residual delimiters in actual input.
    """
    tokens = []
    for match in MATH.finditer(source):
        fmt = next(name for name in ['fence', 'protected', 'display', 'inline']
                   if match.group(name) is not None)
        body = match.group(fmt + '_body')
        labels = LABEL.findall(source[:match.start()])
        tokens.append({'type': 'js-display-math' if fmt in ['fence', 'display'] else 'js-inline-math',
                       'payload': body, 'format': fmt, 'span': [match.start(), match.end()],
                       'paragraph': labels[-1] if labels else None})
    return tokens


class DestinationArticle(HTMLParser):
    """Exactly one ordinary HTML parse; NEVER add entity-unescape afterward.

    Named and id anchors remain distinguishable in evidence. If a single node
    carries identical name and id values it is one destination, not two nodes.
    """
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.tags = Counter()
        self.text, self.math, self.links, self.targets = [], [], [], []
        self.elements, self.inline_styles = [], []
        self._math = self._link = None
        self._ordinal = 0

    def handle_starttag(self, tag, attrs):
        self._ordinal += 1
        attrs = dict(attrs)
        self.tags[tag] += 1
        self.elements.append({'ordinal': self._ordinal, 'tag': tag, 'attrs': attrs})
        if 'style' in attrs:
            self.inline_styles.append({'ordinal': self._ordinal, 'tag': tag, 'style': attrs['style']})
        candidates = [('id', attrs['id'])] if 'id' in attrs else []
        if tag == 'a' and 'name' in attrs:
            candidates.append(('name', attrs['name']))
        for attr, value in candidates:
            self.targets.append({'element': self._ordinal, 'attribute': attr, 'value': value})
        if tag == 'a' and 'href' in attrs:
            self._link = {'element': self._ordinal, 'href': attrs['href'], 'text': ''}
            self.links.append(self._link)
        if tag == 'math-renderer':
            self._math = {'element': self._ordinal, 'type': attrs.get('class'), 'text': ''}
            self.math.append(self._math)

    def handle_data(self, data):
        self.text.append(data)
        if self._math is not None:
            self._math['text'] += data
        if self._link is not None:
            self._link['text'] += data

    def handle_endtag(self, tag):
        if tag == 'a':
            self._link = None
        if tag == 'math-renderer':
            self._math = None

    def math_payloads(self):
        result = []
        for item in self.math:
            width = 2 if item['type'] == 'js-display-math' else 1
            delim = '$' * width
            wrapped = item['text'].startswith(delim) and item['text'].endswith(delim)
            result.append({'type': item['type'], 'payload': item['text'][width:-width] if wrapped else None,
                           'wrapper_valid': wrapped, 'raw_text': item['text'], 'element': item['element']})
        return result

    def target_elements(self, value):
        return sorted({x['element'] for x in self.targets if x['value'] == value})


def compare_math(source_tokens, destination_tokens):
    """Exact equality plus aligned hunks; missing wrappers do not inflate counts.

    Hunks are evidence for manual localization, not independent defect counts.
    No fuzzy math equivalence, Unicode normalization, whitespace trimming, or
    HTML unescaping is allowed here.
    """
    source = [(x['type'], x['payload']) for x in source_tokens]
    actual = [(x['type'], x['payload']) for x in destination_tokens]
    align = difflib.SequenceMatcher(a=source, b=actual, autojunk=False)
    hunks = [{'operation': op, 'source_range': [a, b], 'destination_range': [c, d],
              'source': source_tokens[a:b], 'destination': destination_tokens[c:d]}
             for op, a, b, c, d in align.get_opcodes() if op != 'equal']
    return {'source_count': len(source), 'destination_count': len(actual),
            'exact_all': source == actual and all(x['wrapper_valid'] for x in destination_tokens),
            'aligned_difference_hunks': hunks,
            'limit': 'Aligned hunks need manual interpretation; no independent defect count is inferred.'}


def check_task_relationships(article, task_map, prefix='user-content-'):
    """Use an explicit map from the frozen document, never assumed Q/A labels.

    Each row has label/task/hint/solution target names. Sections end at the next
    named/id anchor; if actual documents embed extra anchors, inspect boundaries
    and adapt before interpreting results. Labels are not used to guess IDs.
    """
    positions = sorted({x['element'] for x in article.targets})
    def section_links(target):
        starts = article.target_elements(prefix + target)
        if len(starts) != 1:
            return None
        start = starts[0]
        end = next((p for p in positions if p > start), float('inf'))
        return [x for x in article.links if start <= x['element'] < end]
    rows = []
    for mapping in task_map:
        sections = {kind: section_links(mapping[kind]) for kind in ['task', 'hint', 'solution']}
        def reaches(origin, target):
            links = sections[origin]
            return links is not None and any(x['href'] == '#' + mapping[target] for x in links)
        rows.append({'mapping': mapping, 'target_element_counts': {
            kind: len(article.target_elements(prefix + mapping[kind])) for kind in sections},
            'task_to_hint': reaches('task', 'hint'), 'task_to_solution': reaches('task', 'solution'),
            'hint_to_task': reaches('hint', 'task'), 'solution_to_task': reaches('solution', 'task'),
            'section_links': sections})
    return rows


def destination_identity(page_data, source_bytes, commit, repo_path, expected_sha256):
    """Require immutable actual ref/path and raw source bytes; no main fallback."""
    payload = page_data['payload']
    layout = payload['codeViewLayoutRoute']
    blob = payload['codeViewBlobLayoutRoute']
    raw = '\n'.join(payload['codeViewBlobLayoutRoute.StyledBlob']['rawLines']).encode('utf-8')
    return {'requested_commit': commit, 'requested_path': repo_path,
            'source_sha256': hashlib.sha256(source_bytes).hexdigest(),
            'source_hash_matches': hashlib.sha256(source_bytes).hexdigest() == expected_sha256,
            'layout_commit_matches': layout['refInfo']['currentOid'] == commit,
            'blob_commit_matches': blob['refInfo']['currentOid'] == commit,
            'layout_path_matches': layout['path'] == repo_path,
            'blob_path_matches': blob['path'] == repo_path,
            'rich_text_untruncated': payload['codeViewBlobRoute']['richTextTruncated'] is False,
            'embedded_raw_exact_without_added_newline': raw == source_bytes,
            'embedded_raw_exact_with_one_added_terminal_newline': raw + b'\n' == source_bytes}


def preserve_new(path, data):
    """Exclusive creation prevents accidental replacement of prior evidence."""
    path = Path(path)
    with path.open('xb') as handle:
        handle.write(data if isinstance(data, bytes) else data.encode('utf-8'))
    return {'path': str(path), 'bytes': path.stat().st_size,
            'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}


def compiler_diagnostics(stdout_bytes, tex_log_bytes):
    """Read both preserved sources; empty .log is never a clean-compile claim."""
    pattern = re.compile(r'^.*(?:warning|overfull|underfull|undefined|missing|^!).*$', re.M | re.I)
    return {'stdout_sha256': hashlib.sha256(stdout_bytes).hexdigest(),
            'tex_log_sha256': hashlib.sha256(tex_log_bytes).hexdigest(),
            'tex_log_empty': not bool(tex_log_bytes),
            'stdout_diagnostics': pattern.findall(stdout_bytes.decode('utf-8', errors='replace')),
            'tex_log_diagnostics': pattern.findall(tex_log_bytes.decode('utf-8', errors='replace')),
            'limit': 'Review warnings and underlying context; this function declares no render pass.'}
