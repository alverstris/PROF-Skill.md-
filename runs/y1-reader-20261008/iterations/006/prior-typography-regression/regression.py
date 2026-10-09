#!/usr/bin/env python3
"""Read-only, narrow T11 representation regression; own outputs only."""
from pathlib import Path
from collections import Counter
import hashlib
import json
import re
import subprocess
import lxml.html

BASE = Path('/workspace/scratch/ac36b9c5ff31')
REPO = BASE / 'PROF-repo'
OUT = Path(__file__).resolve().parent
CSS_BASE = BASE / 'prof-readability/d006-render-review/v1'
CANDIDATE = 'a2389390c0709d65af4a3cf070a04e396e4a4792'
CASES = [
    ('D001', '001', '4', '0716ea92991d7f9fe2814e137bcc830d91a27511', '402485baa2767af9625146721e356f92bad76e4cfb738e5729c6c8b94ea79401', BASE / 'prof-readability/d001-render-review/v4'),
    ('D002', '002', '1', 'f1c0e91c24e9140049d50c7ca965f41e36f3e1a2', '8139080278edb96287576629e7d80933b380c1b82af60d3ede888d500cb68a3a', BASE / 'prof-readability/d002-render-review/v1'),
    ('D003', '003', '1', '4cbf83f2dc2859d5123fc01a0c311a268d580483', 'cd7426a9b70d0ac41aa3ca0418db8c89c391b67304016a7ad38f8379fe98b5a8', BASE / 'prof-readability/d003-render-review/v1'),
    ('D004', '004', '1', '197b57555834d36952e948d4100d2f835c86b20c', '5adb3e95c2fa47c94b4c665d85dc2fe669e2c0086dbc2ebc194cd59720d5d8ad', BASE / 'prof-readability/d004-render-review/v1-corrected'),
    ('D005', '005', '2', '32c553f279ac1e5771ff05b78a9951cbff3fee38', '4ae6d0f33e2957ebaf3bbd31c34e154c4a7c5eaab4bc3a09a9e909574b1a48e6', REPO / 'runs/y1-reader-20261008/iterations/005/render-evidence/v2'),
]
sha = lambda b: hashlib.sha256(b).hexdigest()
norm = lambda s: re.sub(r'\s+', ' ', s).strip()
git = lambda spec: subprocess.check_output(['git', 'show', spec], cwd=REPO)
inputs = {}

def read(p):
    p = Path(p)
    b = p.read_bytes()
    inputs[str(p)] = {'sha256': sha(b), 'bytes': len(b)}
    return b

def markup_source_text(source):
    # Only the actual five documents' math, empty anchors, images and link syntax.
    protected = []
    def math(m, delimiters):
        protected.append(delimiters + m[1] + delimiters)
        return f'PROTECTEDMATH{len(protected)-1}END'
    s = re.sub(r'\$`(.*?)`\$', lambda m: math(m, '$'), source, flags=re.S)
    s = re.sub(r'^```math\n(.*?)\n```', lambda m: math(m, '$$'), s, flags=re.S | re.M)
    s = re.sub(r'<a id="[^"]+"></a>', '', s)
    s = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', s)
    s = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', lambda m: m[1], s)
    return re.sub(r'PROTECTEDMATH(\d+)END', lambda m: protected[int(m[1])], s)

def entry(node):
    return {'tag': node.tag, 'attributes': dict(node.attrib), 'text': norm(node.text_content())}

css_inventory_path = CSS_BASE / 'css-typography-evidence/css-fetch-inventory.json'
css_inventory = json.loads(read(css_inventory_path))
css_files = []
css_rule_evidence = []
css_typography_scoped_rules = []
relevant_selectors = {
    'body', '.markdown-body', '.markdown-body a:not([href])',
    '.markdown-body p,.markdown-body blockquote,.markdown-body ul,.markdown-body ol,.markdown-body dl,.markdown-body table,.markdown-body pre,.markdown-body details',
    '.markdown-body img', '.markdown-body table th',
    '.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6',
    '.markdown-body dl dt', '.text-bold',
}
for fetch in css_inventory['fetches']:
    p = CSS_BASE / fetch['saved_file']
    b = read(p)
    css_files.append({'path': str(p), 'url': fetch['requested_url'], 'recorded_status': fetch['status'],
                      'sha256': sha(b), 'bytes': len(b), 'matches_recorded_hash': sha(b) == fetch['sha256']})
    text = b.decode('utf-8')
    # A lexical extraction of exact flat rules, not CSS execution or a cascade engine.
    for m in re.finditer(r'([^{}]+)\{([^{}]*)\}', text):
        selector, declarations = m.groups()
        selector = selector.strip()
        item = {'file': str(p), 'url': fetch['requested_url'], 'css_sha256': sha(b),
                'offset_0_based': m.start(), 'selector': selector, 'declarations': declarations,
                'exact_rule': m[0]}
        if selector in relevant_selectors:
            css_rule_evidence.append(item)
        if any(c in selector for c in ['.markdown-body', '.entry-content', '.container-lg', '.js-inline-math', '.js-display-math']) and re.search(r'(?:^|;)(?:font(?:-weight|-style)?):', declarations):
            css_typography_scoped_rules.append(item)
    for token in ['--base-text-weight-normal:400', '--base-text-weight-semibold:600']:
        for m in re.finditer(re.escape(token), text):
            css_rule_evidence.append({'file': str(p), 'url': fetch['requested_url'], 'css_sha256': sha(b), 'offset_0_based': m.start(), 'declaration': token})

cases = []
for doc, iteration, version, commit, expected_hash, capture in CASES:
    relative = f'runs/y1-reader-20261008/iterations/{iteration}/teaching-v{version}.md'
    source_bytes = read(REPO / relative)
    source = source_bytes.decode('utf-8')
    closure_path = REPO / f'runs/y1-reader-20261008/iterations/{iteration}/closure.md'
    closure = read(closure_path).decode('utf-8')
    page_bytes = read(capture / 'github-page.html')
    article_bytes = read(capture / 'github-article.html')
    audit = json.loads(read(capture / 'markup-audit.json'))
    page = lxml.html.fromstring(page_bytes.decode('utf-8'))
    payload = json.loads(page.xpath('//script[@data-target="react-app.embeddedData"]')[0].text)['payload']
    layout = payload['codeViewBlobLayoutRoute']
    blob = payload['codeViewBlobRoute']
    rawlines = payload['codeViewBlobLayoutRoute.StyledBlob']['rawLines']
    reconstructed = ('\n'.join(rawlines) + '\n').encode('utf-8')
    article = lxml.html.fromstring(article_bytes.decode('utf-8'))
    semantic_tags = ['table', 'thead', 'tbody', 'tr', 'th', 'td', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'strong', 'em', 'b', 'i', 'caption', 'figcaption', 'figure', 'dl', 'dt', 'dd', 'blockquote', 'summary']
    counts = Counter(n.tag for n in article.iter())
    hrefs = list(dict.fromkeys(page.xpath('//link[@rel="stylesheet"]/@href')))
    images = []
    for img in article.xpath('.//img'):
        p = img.getparent().getparent()
        preceding = p.getprevious()
        while preceding is not None and not norm(preceding.text_content()):
            preceding = preceding.getprevious()
        following = p.getnext()
        while following is not None and not norm(following.text_content()):
            following = following.getnext()
        prefix = '/alverstris/PROF-Skill.md-/raw/' + commit + '/'
        img_relative = img.get('src').removeprefix(prefix)
        local_img = read(REPO / img_relative)
        saved_relative = 'figures/unit-circle-proof-v1.png' if doc == 'D002' else 'product-increment-v1.png'
        saved_img = read(capture / saved_relative)
        images.append({'image': entry(img), 'wrapper_outer_html': lxml.html.tostring(p, encoding='unicode'),
                       'wrapper_ancestry': [entry(n) for n in [img.getparent(), p]],
                       'preceding_prose': entry(preceding) if preceding is not None else None,
                       'following_prose': entry(following) if following is not None else None,
                       'image_source_path': img_relative, 'image_sha256': sha(local_img),
                       'captured_reference_pins_accepted_commit': img.get('src').startswith(prefix),
                       'saved_image_matches_accepted_git_blob': saved_img == local_img == git(commit + ':' + img_relative),
                       'interpretation': 'Plain p > a > img wrapper; neighboring explanatory prose is p[dir=auto]. No caption element or emphasis class/style. Existing image teaching content not retested.'})
    proofs = {
        'source_sha256_equals_accepted_closure': sha(source_bytes) == expected_hash and expected_hash in closure,
        'closure_names_exact_accepted_commit': commit in closure,
        'source_bytes_equal_accepted_git_object': source_bytes == git(commit + ':' + relative),
        'captured_page_source_path_exact': layout['path'] == relative,
        'captured_page_source_commit_exact': layout['refInfo']['currentOid'] == commit,
        'captured_page_rawlines_plus_final_lf_equal_accepted_source_bytes': reconstructed == source_bytes,
        'captured_richtext_not_truncated': blob['richTextTruncated'] is False,
        'captured_source_not_truncated': layout['blob']['truncated'] is False,
        'article_exactly_equals_page_embedded_richtext': blob['richText'].encode('utf-8') == article_bytes,
        'audit_source_hash_agrees_but_not_used_as_only_evidence': audit.get('source_sha256') == sha(source_bytes),
        'whole_article_text_equals_source_after_explicit_markup_normalization': norm(article.text_content()) == norm(markup_source_text(source)),
        'all_actual_linked_stylesheet_urls_covered_by_hashed_current_css': set(hrefs) == {x['url'] for x in css_files},
    }
    math_counts = {k: len(article.xpath(f'.//math-renderer[@class="js-{k}-math"]')) for k in ['inline', 'display']}
    prose_inline_styles = [entry(n) for n in article.iter() if n.tag != 'math-renderer' and n.get('style')]
    cases.append({'document': doc, 'source_path': str(REPO / relative), 'source_commit': commit,
                  'source_sha256': sha(source_bytes), 'source_bytes': len(source_bytes),
                  'closure_path': str(closure_path), 'capture_directory': str(capture),
                  'page_sha256': sha(page_bytes), 'article_sha256': sha(article_bytes),
                  'rawline_reconstruction': 'Join page JSON rawLines with LF and append one final LF; byte comparison, no prose or math normalization.',
                  'reconstructed_source_sha256': sha(reconstructed), 'identity_and_completeness_checks': proofs,
                  'article_attributes': dict(article.attrib), 'whole_dom_tag_counts': dict(counts),
                  'semantic_structure_counts': {t: counts[t] for t in semantic_tags},
                  'all_class_counts': dict(Counter(c for n in article.iter() for c in n.get('class', '').split())),
                  'all_inline_style_counts': dict(Counter(n.get('style') for n in article.iter() if n.get('style'))),
                  'nonmath_inline_style_elements': prose_inline_styles,
                  'math_renderer_counts_exempt_from_prose_emphasis': math_counts,
                  'first_title_paragraph': entry(article.xpath('.//p')[0]),
                  'images_and_explanatory_wrappers': images,
                  'current_css_table_header_rule_matches': counts['th'],
                  'current_css_heading_rule_matches': sum(counts[t] for t in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']),
                  'current_css_definition_term_emphasis_rule_matches': counts['dt'],
                  'actual_linked_stylesheet_urls': hrefs,
                  'inactive_data_href_only_stylesheets': len(page.xpath('//link[@rel="stylesheet" and @data-href and not(@href)]')),
                  'affected_by_narrow_forced_prose_emphasis_trigger': False,
                  'disposition': 'No matching forced-emphasis representation found in inspected article; no lesson regeneration supported by this trigger.'})

candidate_skill = git(CANDIDATE + ':SKILL.md')
candidate_t11 = next(x for x in candidate_skill.decode().splitlines() if x.startswith('| T11 '))
limits = [
    'Only this proposed T11 destination-emphasis trigger is regressed. No SASIS, student/subject test, teaching re-authoring, mathematical regrading or broad teaching acceptance was performed.',
    'Saved GitHub server markup and page-embedded source identities are inspected; no live pixels, browser/CUA, computed-style execution, MathJax execution or client state is claimed.',
    'CSS bytes come from the already saved D006 current HTTP retrieval of the exact linked asset URLs; hashes independently verified. They are not claimed to be historical stylesheet bytes at the D001–D005 original capture times.',
    'The CSS evidence is targeted exact-rule inspection and lexical inventory of scoped font declarations, not a complete executable CSS cascade. Inactive data-href theme placeholders and dynamic/interaction styling are not executed.',
    'Conventional mathematical notation in math-renderer elements is exempt from prose emphasis; no italic-variable failure is inferred. D002/D003 accepted image contents are not reopened; actual wrappers and adjacent explanatory prose are inspected.',
    'No earlier accepted artifact exercises the newly observed table-header case. The empty affected set therefore does not establish a positive regression test of a conversion that removes forced table-header emphasis.',
]
result = {'scope': 'Independent narrow representation regression for accepted D001–D005 under proposed PROF T11 destination-emphasis trigger',
          'candidate_commit': CANDIDATE, 'candidate_skill_sha256': sha(candidate_skill), 'candidate_T11': candidate_t11,
          'conclusion': 'NO_AFFECTED_EARLIER_ACCEPTED_ARTIFACT_FOUND', 'affected_set': [],
          'all_identity_and_completeness_checks_true': all(all(c['identity_and_completeness_checks'].values()) for c in cases),
          'cases': cases, 'css_evidence': {'provenance': str(css_inventory_path), 'current_saved_css_files': css_files,
                                        'all_css_hashes_match_fetch_inventory': all(x['matches_recorded_hash'] for x in css_files),
                                        'exact_relevant_rules_and_tokens': css_rule_evidence,
                                        'all_lexically_found_font_rules_for_actual_article_class_names': css_typography_scoped_rules},
          'unresolved_limits': limits, 'preservation': {'all_read_inputs_unchanged_at_end': all(Path(p).read_bytes() and sha(Path(p).read_bytes()) == h['sha256'] for p,h in inputs.items()),
                                                       'no_original_artifact_skill_helper_source_or_repo_write_performed': True,
                                                       'subagents_used': False, 'browser_used': False, 'new_http_fetches': False},
          'input_hashes': inputs}
(OUT / 'regression.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'conclusion': result['conclusion'], 'identities_complete': result['all_identity_and_completeness_checks_true'], 'css_hashes_exact': result['css_evidence']['all_css_hashes_match_fetch_inventory'], 'preserved': result['preservation']['all_read_inputs_unchanged_at_end'], 'counts': {c['document']: c['whole_dom_tag_counts'] for c in cases}}, indent=2))
