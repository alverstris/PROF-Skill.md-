"""Inspect frozen Markdown structure without mutating the teaching."""
import hashlib
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
base = root / 'teaching'
rows = []
for path in sorted(base.glob('*.md')):
    text = path.read_text()
    displays = re.findall(r'^```math\n(.*?)^```\s*$', text, re.M | re.S)
    inline = re.findall(r'\$`([^`]*?)`\$', text)
    prose = re.sub(r'^```math\n.*?^```\s*$', '', text, flags=re.M | re.S)
    prose = re.sub(r'\$`[^`]*?`\$', '', prose)
    ids = re.findall(r'<a id="([^"]+)"></a>', text)
    links = []
    for label, target in re.findall(r'\[([^\]]+)\]\(([^)]+)\)', text):
        if target.startswith(('http:', 'https:')):
            continue
        name, _, anchor = target.partition('#')
        dst = (path.parent / name).resolve() if name else path
        good = dst.is_file()
        if good and anchor:
            good = bool(re.search(r'<a id="' + re.escape(anchor) + r'"></a>', dst.read_text()))
        links.append({'label': label, 'target': target, 'local_target_exists': good})
    rows.append({
        'path': str(path.relative_to(root)),
        'sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
        'display_math_blocks': len(displays),
        'protected_inline_expressions': len(inline),
        'unprotected_dollar_count': prose.count('$'),
        'inline_literal_strict_comparators': [s for s in inline if '<' in s or '>' in s],
        'atx_headings': re.findall(r'^#{1,6}\s+.*$', prose, re.M),
        'setext_lines': re.findall(r'^\s*(?:={3,}|-{3,})\s*$', prose, re.M),
        'prose_emphasis_markers': [m.group(0) for m in re.finditer(r'(?<!\w)[*_]{1,3}(?=\S)', prose)],
        'prose_literal_backtick_lines': [i+1 for i, line in enumerate(text.splitlines()) if '`' in re.sub(r'\$`[^`]*?`\$', '', line) and not line.startswith('```')],
        'anchors': ids,
        'unique_anchors': len(ids) == len(set(ids)),
        'local_links': links,
    })
result = {'method': 'Source structure and local anchor/file checks only; no destination styling, parsed GitHub math, pixel or click verification is implied.', 'files': rows}
(root / 'review/frozen-structure-check.json').write_text(json.dumps(result, indent=2) + '\n')
assert all(all(link['local_target_exists'] for link in row['local_links']) for row in rows)
assert all(row['unique_anchors'] and not row['unprotected_dollar_count'] and not row['inline_literal_strict_comparators'] and not row['atx_headings'] and not row['setext_lines'] and not row['prose_emphasis_markers'] for row in rows)
print(json.dumps({'files':len(rows), 'inline':sum(r['protected_inline_expressions'] for r in rows), 'display':sum(r['display_math_blocks'] for r in rows), 'local_links':sum(len(r['local_links']) for r in rows), 'literal_backticks':{r['path']:r['prose_literal_backtick_lines'] for r in rows}}))
