from pathlib import Path
import re,json,hashlib,difflib
p=Path(__file__).resolve().parent
v1=(p/'teaching-v1.md').read_text(); assert hashlib.sha256(v1.encode()).hexdigest()=='8a9845299b276ba13c3f2c18862bdde3ed9b0227451e89fb57f9fe2719e573f0'
failures=json.loads((p.parent/'destination-v1/complete-math-failure-map.json').read_text())
pattern=re.compile(r'\$\$(.*?)\$\$|\$`(.*?)`\$',re.S)
old=list(pattern.finditer(v1)); assert len(old)==309
repairs=[]
for failure in failures:
 m=old[failure['ordinal']-1]; payload=m.group(2) if m.group(2) is not None else m.group(1)
 assert payload==failure['source']
 if m.group(2) is not None:
  new=payload.replace('<',r'\lt ').replace('>',r'\gt ')
  assert new!=payload and payload.count('<')+payload.count('>')==failure['affected_operator_count']
  span=m.span(2)
 else:
  assert failure['ordinal']==159 and payload.count('\n a-x=')==1
  new=payload.replace('\n a-x=','\na-x='); span=m.span(1)
 repairs.append({'ordinal':failure['ordinal'],'paragraph':failure['paragraph'],'type':failure['type'],'source_span':list(span),'before':payload,'after':new,'comparison_count':failure['affected_operator_count']})
v2=v1
for r in reversed(repairs):
 a,b=r['source_span']; v2=v2[:a]+r['after']+v2[b:]
assert len(repairs)==21 and sum(r['comparison_count'] for r in repairs)==23
newmatches=list(pattern.finditer(v2)); assert len(newmatches)==309
inverse=v2
for r in reversed(repairs):
 m=newmatches[r['ordinal']-1]; span=m.span(2) if m.group(2) is not None else m.span(1)
 assert v2[span[0]:span[1]]==r['after']
 inverse=inverse[:span[0]]+r['before']+inverse[span[1]:]
assert inverse==v1
assert not any('<' in m.group(2) or '>' in m.group(2) for m in newmatches if m.group(2) is not None)
for m in newmatches:
 if m.group(2) is not None: assert not re.search(r'\\(?:lt|gt)[A-Za-z]',m.group(2))
# Prose, anchors, images, text ordering, pre-existing math commands and all untouched math are exact.
assert pattern.sub('MATH',v1)==pattern.sub('MATH',v2)
changed={r['ordinal'] for r in repairs}
assert all(a.group()==b.group() for i,(a,b) in enumerate(zip(old,newmatches),1) if i not in changed)
for r in repairs:
 if r['comparison_count']:
  assert r['after'].replace(r'\lt ','<').replace(r'\gt ','>')==r['before']
(p/'teaching-v2.md').write_text(v2)
(p/'v1-to-v2.diff').write_text(''.join(difflib.unified_diff(v1.splitlines(True),v2.splitlines(True),fromfile='teaching-v1.md',tofile='teaching-v2.md')))
proof={'scope':'Local representation repair only; no destination, fresh SASIS or final acceptance claim','v1_sha256':hashlib.sha256(v1.encode()).hexdigest(),'v2_sha256':hashlib.sha256(v2.encode()).hexdigest(),'v2_bytes':len(v2.encode()),'changed_inline_payloads':20,'comparison_replacements':23,'changed_display_payloads':1,'all_309_math_nodes_preserved_in_order':True,'all_nonmath_prose_anchors_links_image_markup_exact':True,'inverse_restores_complete_v1_bytes':inverse.encode()==(p/'teaching-v1.md').read_bytes(),'all_other_math_payloads_byte_exact':True,'semantic_justification':'TeX relation control sequences \\lt and \\gt denote the same strict inequalities as literal < and >. Each newly inserted control word ends with an ordinary delimiting space, avoiding name merging. Existing commands, operands and grouping remain unchanged. The sole removed leading display space is ordinary math whitespace following an explicit \\qquad; TeX mathematical spacing and tokens are unchanged.','repairs':repairs}
(p/'v2-repair-equivalence.json').write_text(json.dumps(proof,indent=2)+'\n')
print(json.dumps({k:v for k,v in proof.items() if k!='repairs'},indent=2))
