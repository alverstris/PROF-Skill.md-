# D137 source review

Identity: official MIT8.022 session L14; PDF printed Lecture12. The official session and printed PDF numbers are preserved. One assigned PDF, 9 physical pages / 18 numbered slides.

Official asset: https://ocw.mit.edu/courses/8-022-physics-ii-electricity-and-magnetism-fall-2004/8e5a529371d7ebc503049d075cfae958_lecture12.pdf
Resource: https://ocw.mit.edu/courses/8-022-physics-ii-electricity-and-magnetism-fall-2004/resources/lecture12/
Original SHA-256: 3ae24de9c79f0231b021dc850f7ec756d905e92ba79c0507bb9250b9d0a4e253; 105874 bytes; matches recorded original-cache hash.

Complete original PDF text read; all full original-page images actually inspected, including every diagram, label and equation. All current PNGs decode and have nonuniform content. No failed derivatives, source/cache edits, or historical-audit changes.
# Complete coverage

- p1, slides1–2: Title/topics; xy capacitor plates, perpendicular E arrows, L and L/γ widths, xyz axes and field transformation.
- p2, slides3–4: yz capacitor plates before/after boost, unchanged height and contracted separation, parallel E arrows/axes; classical and relativistic p/E with full series.
- p3, slides5–6: Boosted xyz frames; four-momentum transformation; initial-rest force, displacement and kinetic-energy change equations.
- p4, slides7–8: Full longitudinal/transverse force transformations and limiting calculations; no additional figures.
- p5, slides9–10: Lab-frame wire boundaries, positive/negative charge rows, u/v/current arrows and Q; explicitly rejected first density argument and corrected second argument.
- p6, slides11–12: Lab force law and right-hand-rule statement; charge-rest-frame wire, stationary Q, moving charge rows/arrows and relativistic u-prime.
- p7, slides13–14: Full density/gamma-composition algebra, net line charge, E-prime and force; all dense fraction signs inspected.
- p8, slides15–16: Both frame forces and reused comparison law, physical interpretation text.
- p9, slides17–18: Summary of mechanical and electromagnetic transformations; outlook.

# Technical findings

- D137-F1 (confirmed source typo, p2 slide3): Plates are in yz and field drawing/boxed E_parallel are along x, but bullet says electric field parallel z. Normal is x.
- D137-F2 (confirmed source definition errors, p2–3 slides4–5): Gamma definition is printed 1/(1−u²/c²) (and later1/(1−βv²)), omitting square root. Correct γu=(1−u²/c²)^−1/2. Slide5 also labels this γu while using γv for the frame boost. Slide4 final expansion calls γu mc² Ekin; that is total E, while K=(γu−1)mc².
- D137-F3 (confirmed source signed-inequality error, p5 slide10, second/corrected attempt): The accepted formula λminus_rest=−λ0/γ is right for λ0>0, γ>1, but the printed λminus_rest<λminus_moving is false for signed densities: −λ0/γ>−λ0. Magnitudes obey the printed less-than relation. The earlier first attempt is explicitly marked WRONG and is not counted as an endorsed source result. Its correct follow-up also uses boost symbol v where electron-rest boost is u.
- D137-F4 (confirmed source frame-label inconsistency, p8 slide15): With this slide’s primes meaning Q-rest, source correctly computes Fprime=γv F_lab, then claims consistency with Fprime_y=F_y/γ. The earlier law was derived with unprimed particle instantaneously at rest. It applies here only after relabeling rest/lab, giving F_lab=F_rest/γ. The unqualified same-prime equation on slide15 contradicts its two displayed force values.
- D137-C1 (conditional models / missing conditions, p1–4 slides2–8): Capacitor formulas assume ideal large plates, invariant Q, negligible edges and B=0 in the capacitor rest frame. Eperpprime=γEperp is not the general mixed-field transform. Force rules Fxprime=Fx and Fyprime=Fy/γ apply at an event where particle u=0 in O; they are not universal force-component transformation rules for arbitrary moving particles. Small acceleration alone does not bound velocity for long times; the t→0 limit supplies the local condition.
- D137-C2 (conditional models and unresolved wording, p5–9 slides9–17): Wire is ideal infinite, steady, locally neutral in lab; E=0 is a model assumption beyond global neutrality. λ0,u,v are positive magnitudes; repulsion assumes Q>0 and both electron/test-charge velocities +x. The charge-frame drawing shows electrons left, requiring u<v; algebra works either sign of u−v. Lab current has signed Ix=−λ0u; printed I=λ0u is magnitude. Summary pure B “looks like E” cannot mean pure E only: a magnetic-dominated field retains nonzero B in every inertial frame. Slide14 explicitly retains Bprime. Invariants E²−B² and E·B prevent arbitrary interchange of pure electric and pure magnetic fields.

# Independent checks


For an ideal plate capacitor with rest B=0, a tangential boost contracts area to A/γ and raises charge density/Eperp by γ; a normal boost leaves charge density and Eparallel unchanged. Under an explicitly equal-time gap voltage V=∫E·dl, the normal-boost question gives dprime=d/γ, Vprime=V/γ and Cprime=γC. This is a reviewer deduction for the ideal gap, not a supplied source answer or general moving-circuit capacitance law.


Correct four-momentum equations Eprime=γv(E−vpx), pxprime=γv(px−vE/c²), pyprime=py, pzprime=pz preserve E²−c²p²=m²c⁴. Low-speed E=mc²+mu²/2+O(u⁴/c²); K omits the rest term. The handout2 justification is cited but not part of this assigned PDF.


For general particle velocity u, dtprime=γv(1−vux/c²)dt and Fxprime=[Fx−v(F·u)/c²]/[1−vux/c²], Fyprime=Fy/[γv(1−vux/c²)]. At u=0 they reduce to the source’s local rules. Thus the apparent contrast between capacitor Eperp rising and rest-particle transverse force falling is not a contradiction: a moving test charge also experiences magnetic force.


Independent four-current check of the wire: (λlab,Ix)=(0,−λ0u), so λprime=γv(λlab−vIx/c²)=γvλ0uv/c². Separately λplusprime=γvλ0 and λminusprime=−γv(1−uv/c²)λ0, using γuprime=γuγv(1−uv/c²). Their sum agrees. With transverse r unchanged, Eprime=2λprime/r and Frest=QEprime=γvFlab. For Q>0,u>0,v>0 both forces point away from the wire; Q<0 reverses them. Limits u=0 or v=0 remove induced net density and this transverse force.

# Limits

- No numerical experimental claim or outside handout was independently audited.
- No external research required: key conclusions follow from source algebra, four-current/four-momentum transformations and field invariants.

No learner diagnosis, lesson authoring, skill judgment or additional-asset inspection claims.
