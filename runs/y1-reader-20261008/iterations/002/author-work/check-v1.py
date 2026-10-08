from pathlib import Path
import re,json,hashlib,math

p=Path(__file__).resolve().parents[1]/'teaching-v1.md'
s=p.read_text();checks={}
checks['consecutive_paragraph_labels']=re.findall(r'^\[P(\d+)\]',s,re.M)==[f'{i:02}' for i in range(1,73)]
checks['no_markdown_headings']=not re.search(r'^\s{0,3}#{1,6}\s',s,re.M)
checks['no_prose_emphasis_or_table_headers']=not re.search(r'\*\*|__|(?<!\*)\*(?!\*)|^\|.*\|$',s,re.M)
checks['balanced_fences']=s.count('```math')==len(re.findall(r'^```$',s,re.M))
inline=re.findall(r'\$`(.*?)`\$',s,re.S); display=re.findall(r'```math\n(.*?)\n```',s,re.S)
res=re.sub(r'\$`.*?`\$','',s,flags=re.S)
checks['no_unmatched_dollars_or_backticks_outside_fences']=('$' not in res and '`' not in re.sub(r'```math\n.*?\n```','',res,flags=re.S))
checks['no_literal_comparison_characters_in_math']=all('<' not in z and '>' not in z for z in inline+display)
checks['math_fence_blank_boundaries']=all(s[max(0,m.start()-2):m.start()]=='\n\n' and s[m.end():m.end()+2]=='\n\n' for m in re.finditer(r'```math\n.*?\n```',s,re.S))
checks['balanced_math_braces']=all(z.count('{')==z.count('}') for z in inline+display)
checks['no_row_separator_at_source_line_end']=all(not re.search(r'\\\\\s*\n',z) for z in display)
ids=re.findall(r'<a id="([^"]+)"></a>',s);links=re.findall(r'\]\(#([^\)]+)\)',s)
checks['unique_anchors']=len(ids)==len(set(ids));checks['all_internal_links_resolve']=all(x in ids for x in links)
checks['six_tasks_hints_solutions']=all(f'{kind}{n}' in ids for kind in ['q','h','s'] for n in range(1,7))
checks['grouped_help']=s.index('id="h1"')<s.index('id="h6"')<s.index('id="solutions"')<s.index('id="s1"')
checks['no_placeholders']=not re.search(r'\b(TODO|TBD|FIXME|PLACEHOLDER)\b',s)
checks['local_figure_exists']=(p.parent/'figures/unit-circle-proof-v1.png').is_file()
# These independent numerical probes discriminate signs/factors; analytic checks
# are recorded separately and do not rely on floating-point approximation.
eps=1e-5;alt=3.;ran=5.;L=lambda h,s:math.sqrt(h*h-s*s)
checks['gps_range_slope_sign_and_scale']=abs((L(ran+eps,alt)-L(ran-eps,alt))/(2*eps)-1.25)<1e-8
checks['gps_altitude_slope_sign_and_scale']=abs((L(ran,alt+eps)-L(ran,alt-eps))/(2*eps)+.75)<1e-8
Y=lambda z:160*z-16*z*z
checks['motion_translation_samples']=all(400-16*t*t==Y(t+5) for t in [-5,-2,0,2,5])
checks['motion_endpoint_quotients']=abs((Y(eps)-Y(0))/eps-(160-16*eps))<1e-8 and abs((Y(10-eps)-Y(10))/(-eps)-(-160+16*eps))<1e-7
checks['trig_signed_small_inputs']=all(abs(math.sin(3*x)/x-3)<1e-6 and abs((1-math.cos(2*x))/x)<.003 and abs((1-math.cos(2*x))/(x*x)-2)<1e-6 for x in [-.0001,.0001])
checks['oscillation_subsequences']=all(abs(math.sin(math.pi/2+2*math.pi*n)-1)<1e-12 and abs(math.sin(3*math.pi/2+2*math.pi*n)+1)<1e-12 for n in range(5))
checks['shifted_symmetry']=all(Y(5+r)==Y(5-r) for r in [-5,-2,0,2,5])
result={'scope':'bounded mechanical, numerical and navigation checks; not explanatory/rendered/SASIS acceptance','sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size,'characters':len(s),'paragraphs':72,'inline_math_count':len(inline),'display_math_count':len(display),'checks':checks,'all_pass':all(checks.values()),'symbolic_tool_limit':'SymPy unavailable in both shell Python and bundled primary Python; no symbolic-tool success claimed. Analytic checks performed by author and independent mathematics checker.'}
p.parent.joinpath('author-work/mechanical-checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
