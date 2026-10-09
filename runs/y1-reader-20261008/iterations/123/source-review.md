# D123 technical source review — studio 30

This is source preparation only, not teaching authoring, SASIS, acceptance, or closure. Exact assignment: MIT 8.02T Spring 2005 studio 30, full Chapter 13 (51 pages), full presentation (29 pages), full PRS (4 pages): 84 assigned pages. This reviewer read all extracted text and personally opened all original full pages. The 51-page chapter was completely read once for the integral shared D122/D123 record; this packet's 33 unique pages were then read in full. No predecessor coverage is used.

The integral chapter review is `../shared-reading-review.md`, with exact complete text/visual coverage in `../shared-reading-map.json`. Every chapter finding, deduction and limit applies here, including the complete conducting-sheet appendix, solved problems, conceptual questions and all ten additional problems. Chapter sharing does not extend to any unread section; none remains unread.

## Assets and access

| Asset | Actual pages | SHA-256 |
|---|---:|---|
|Chapter 13|51|328d921f86d61450481a06feb2187f739c277c1eb0eb8fa21f9e90f8630479d7|
|presentation_w13d1|29|f0b0b8d2db376c52c2d7c409ee6e314bda67781978611e9f8ed1506b05e21ffe|
|prs_w13d1|4|5f6ad8498e8a40660fd567b6d4093f34296ed05e9905c2bcc5471472785e57c2|

All actual PDFs match the assignment; every original cached page image decodes. No D123 recovery was needed. The rotated/native slide text extraction has disrupted reading order, so personally opened full slide images control symbols, signs, diagrams and question content. `source-map.json` contains exact original boundaries (each complete PDF), verified assets, text hashes and all page-image hashes with specific coverage. Source/repository/predecessor files remain unchanged.

## Traveling and standing waves, presentation pp1–10

The outline and transition slides were read. Pages 3–4 use y=y0sin[k(x+vt)] with positive speed v; fixed phase moves −x. Page 5 uses sin(kx−ωt), fixed phase +x. Thus the changed sign is an explicit propagation convention, not a contradiction. The graphs distinguish amplitude from peak-to-peak displacement, spatial wavelength λ from temporal period T. All relations k=2π/λ,ω=2πf,T=1/f,|v|=ω/k=λf are correct for positive k,ω. The phrase moving left “at velocity v” should mean signed x-velocity−v or speed v.

Pages 7/10 independently recompute sin(kx−ωt)+sin(kx+ωt)=2sin(kx)cos(ωt), provided both waves have the same frequency, wavenumber, amplitude and scalar component/polarization. Merely having opposite directions does not establish that exact standing wave. A node is a position whose amplitude vanishes for all time, x=nλ/2; electric antinodes occur at x=(2n+1)λ/4. All-space instantaneous zeros when cosωt=0 are not additional permanent nodes. The p8 diagram's nodes and antinodes were inspected and match those positions. Musical instruments and microwave cavities are examples with distinct physical variables and boundary conditions; E is not literal string displacement.

If the scalar E on p7 is Ey for a vacuum wave, its companion must be Bz=−2(E0/c)cos(kx)sin(ωt), because the backward wave's B sign reverses. Hence E and B have spatially shifted nodes and temporal quadrature. Sx=−E0²sin(2kx)sin(2ωt)/(μ0c), whose mean signed value is zero. It is incorrect to apply the single traveling-wave E/B=c or same-phase assertion to this sum. This sine/cosine phase differs legitimately from the chapter's chosen standing-wave time origin.

Page 9 is a Tacoma Narrows oscillation pointer, with no quantitative force or collapse model. It can motivate a spatial mode discussion but cannot establish that elementary externally forced resonance caused the collapse. The official WSDOT account describes torsional flutter and self-excited motion as the primary explanation while noting disputed details. This is a limitation on the analogy, not a claim that the slide explicitly states a false causal mechanism. No linked bridge film or PBS page was read or played. Page 10's “Problem 2” is an unidentified worksheet pointer; only the displayed wave relation is available for review, and no missing worksheet is invented.

## Maxwell equations and wave derivation, presentation pp11–27

Page 12's four integral Maxwell equations and separate Lorentz law have correct constants and signs for the vacuum/total-source formulation, with consistently oriented contours and spanning surfaces. They are introduced physical laws; the wave equation is a deduction from them under stated source and field restrictions. The Lorentz law is not one of the four Maxwell equations. Fixed-contour Faraday form does not by itself give motional emf for a moving circuit.

The p14 plane-wave static frame and axes were opened. The image shows field vectors at positions, not a particle trajectory, and its drawing scales do not equate V/m with tesla. Page 15 adds polarization vector Ê to the same traveling-wave relations. For propagation+x the pure transverse Ê must have no x component. Page 16's c≈3×10⁸m/s, orthogonality, in-phase E/B and E×B direction are valid for one traveling vacuum plane wave. They are not universal for near fields or superposed/standing waves. Ratios at common zeros are undefined; the vector identity B=p̂×E/c is more robust. Page 17 is a PRS pointer; p18 states the derivation objective.

The red rectangle in pp19–20 lies in the xz plane. With its normal+y and paired contour sense, ∮B·dl=[Bz(x)−Bz(x+dx)]l, while the electric flux derivative tends to l dx ∂tEy. This yields −∂xBz=μ0ε0∂tEy. The exact finite-width flux is an integral over x; the displayed l dx field form is its differential-limit approximation. The derivation has set J=0 and assumed Ey,Bz depend only on x,t. It does not follow merely from a zero net current through one arbitrarily chosen loop.

For pp21–22's xy rectangle with normal+z, ∮E·dl=[Ey(x+dx)−Ey(x)]l and Faraday gives ∂xEy=−∂tBz. Both rectangle orientations, component labels and difference signs were personally checked against the images. Spatial derivatives of these coupled equations give ∂x²Ey=μ0ε0∂t²Ey (p23), assuming sufficient smoothness to commute mixed derivatives. Substitution f(x−vt) on p24 gives v²=1/(μ0ε0) for a nontrivial wave shape; a constant or affine function alone cannot determine a speed through its zero second derivatives. The general 1D solution also includes the opposite branch f(x+ct), not just the displayed example.

**Source error, p25:** The instruction says take the x derivative of the first equation, but the displayed algebra actually takes its **t derivative**. The displayed chain ∂t²Bz=−∂t∂xEy=−∂x∂tEy=(1/μ0ε0)∂x²Bz and final magnetic wave equation are correct. Only the verbal derivative direction is wrong.

Pages 26–27 correctly emphasize that two arbitrary scalar solutions of the wave equation cannot independently be chosen as E and B; the first-order Maxwell relations couple them. However “the same” profile applies only to the stipulated single forward branch Ey=E0f(x−vt),Bz=B0f(x−vt), which gives vB0=E0 for nonconstant f and vacuum v=c. In general Ey=F(x−ct)+G(x+ct) and Bz=[F(x−ct)−G(x+ct)]/c, so they need not have the same spatial/time shape. Uniform background solutions also require initial/boundary specifications. A shared wave equation is a necessary, not sufficient, condition for an electromagnetic field pair. Dimensions check: E/B has units m/s, not a dimensionless equal amplitude.

## Conductor-reflection group problem, presentation p28

This complete five-part question was read and independently solved; no worked source answer is supplied. Assume k,ω>0,ω=ck, incidence from z<0 onto a stationary perfect conducting plane at z=0, and no extra static/background fields. The wave Einc=E0cos(kz−ωt)x̂ moves +z. The relevant conductor condition is zero **tangential** E; the polarization here is entirely tangential, so the total E is zero at the plane. It is not a general statement that the normal electric field outside a conductor vanishes.

1. Etot(0,t)=0.
2. Eref=−E0cos(kz+ωt)x̂, traveling −z.
3. Binc=(E0/c)cos(kz−ωt)ŷ and Bref=(E0/c)cos(kz+ωt)ŷ. The reflected electric sign and reversed propagation together make the reflected magnetic polarization+y.
4. Etot=2E0sin(kz)sin(ωt)x̂ and Btot=2(E0/c)cos(kz)cos(ωt)ŷ on the incident side. Thus B(0−,t)=2(E0/c)cos(ωt)ŷ. Magnetic field doubles at the electric node; setting both to zero would be wrong. These expressions satisfy Faraday and Ampere-Maxwell for ω=ck. Their flux is Sz=E0²sin(2kz)sin(2ωt)/(μ0c), with zero time-mean signed flux, though incident/reflected powers are nonzero.
5. Surface current density K(t)=2E0cos(ωt)/(μ0c)x̂, peak 2E0/(μ0c) A/m. Using normal+z from incident vacuum to conductor, ẑ×(Binside−Boutside)/μ0=K yields +x for positive cosine. It reverses each half-cycle. The question's unspecified “current” is current per transverse width; a total number of amperes cannot be obtained without a width. The ideal sheet/conductor boundary permits finite K while tangential E tends to zero; treating J=E/ρ by substituting two zeros directly is not a derivation.

The displayed cosine-sum identity is correct and suffices for these sums. Analytic recomputation plus numerical trigonometric checks verified the two superpositions, boundary E and surface-current sign. The shared appendix review supplies the finite-resistive-sheet model, its limitations, and peak-versus-average pressure correction. Page 29's “next time” image is an inspected plane-source static frame; it provides no actual apparatus dimensions, wiring or measured data.

## PRS: both question/answer pairs

| PDF pages | Independent result and correction |
|---|---|
|1–2|E=E0sin(kz+ωt)ŷ propagates −z. Since ŷ×x̂=−ẑ, B=(E0/c)sin(kz+ωt)x̂: choice 1. The depicted coordinate axes and both field-arrow polarities agree. B0=E0/c is needed to complete the amplitude, not just direction.|
|3–4|B=B0sin(ky−ωt)ẑ propagates +y. Since (−x̂)×ẑ=+ŷ, E=−cB0sin(ky−ωt)x̂: choice 4. The answer p4 omits E0 from the displayed E expression. Restore E0=cB0; otherwise the dimensional amplitude is missing. The polarization conclusion remains correct.|

The unit-vector cross products on answer pages describe positive polarization coefficients, not a claim that an oscillating instantaneous field always points in that direction. All options were read; choices parallel to propagation violate transverse-wave conditions, and the wrong transverse sign reverses energy propagation. No numerical amplitudes or experimental results are given.

## Targeted primary research and remaining limits

For the bridge analogy, opened and read the official Washington State Department of Transportation page *Tacoma Narrows Bridge history — Lessons from failure*: https://wsdot.wa.gov/TNBhistory/bridges-failure.htm. Actual returned text scope was lines10–144, with the relevant causal discussion in 104–132. No linked photographs, film, archival report or PBS resource was claimed as read. The source describes self-excited torsional motion and acknowledges disagreements over details; it supports restricting the slide's analogy rather than replacing it with an overconfident simple-resonance explanation. No unrelated search result supplied an accepted technical claim.

The complete shared chapter review separately records narrowly scoped NIST and MIT 6.013 research on μ0 convention, dipole patterns and conductor skin depth. There is no lab protocol in this packet and no basis for invented wiring or outcomes. All assigned text and visual content has been reviewed; source preparation ends here at D123 and does not certify any teaching artifact or downstream closure.
