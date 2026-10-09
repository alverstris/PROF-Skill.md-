# D121 technical source preparation

This is a source review for future PROF input, not teaching, SASIS, or session closure. The assignment is studio 26: Chapter 12 in its entirety (PDF 1–41; printed 0–40), presentation 1–42, and associated PRS 1–10. I read the complete extracted text and personally opened every full page image in those ranges. No predecessor reading or contact sheet substitutes for that reading. `source-map.json` and `access-validation.json` give exact assets, hashes, page coverage, and provenance. All three cached PDFs match their assigned SHA-256 and page counts; all 93 full-page images decode. No cache recovery was needed for D121.

## Laws, model, and conventions

The introduced model is ideal, linear, lumped RLC circuit theory, with prescribed sinusoidal source, constant component values, and the sinusoidal particular response after dissipative transients have decayed. The underlying laws are charge conservation/Kirchhoff junction rule, the circuit loop balance including inductive emf, and constitutive relations vR=Ri, vL=L di/dt, vC=q/C with i=dq/dt into the positively referenced capacitor plate. The last sign is a reference convention, not a consequence of initially zero charge. Positive amplitudes and signed phases must be kept separate.

Taking v=V0 sin(ωt), the positive-amplitude series response is i=(V0/Z)sin(ωt−φ), Z=√[R²+(ωL−1/ωC)²], φ=atan2(ωL−1/ωC,R). Thus φ>0 means current lags. The consistent charge is q=−V0 cos(ωt−φ)/(ωZ). Substitution gives Lq''+Rq'+q/C=V0 sin(ωt). XL=ωL and XC=1/(ωC) are positive reactance magnitudes in ohms; calling them resistance is only an analogy and does not imply dissipation. Z here means impedance magnitude, not the complex impedance R+j(XL−XC).

The phasors rotate counterclockwise and the vertical projection represents sine. A change from source phase zero to current phase zero is legitimate: i=I0 sin(ωt), v=V0 sin(ωt+φ). Presentation p30 states it explicitly; Chapter p11 changes to it without stating the time-origin change. Phasor amplitudes add as vectors. Neither the diagram lengths for voltage versus current nor their overlaid plot heights are directly comparable physical units. Tables on Chapter pp13,22–23 and presentation p21 are valid ideal-element sinusoidal relationships, including the series limits C→∞ and L→0. These limits do not describe initial-condition transients or arbitrary waveforms.

Direct integration/differentiation yields resistive in-phase response, capacitor current leading by π/2, and inductor current lagging by π/2. A pure ideal inductor admits an additional constant current: the sinusoidal response implicitly selects zero DC offset; with exactly zero loss that offset does not decay. A source-driven lossless LC at resonance has no bounded sinusoidal steady-state solution. The simple steady-state formulas require R>0 for a finite series resonant current.

For series RLC, current resonance is exactly ω0=1/√LC for constant V0 and R. Imax=V0/R, φ=0, and the reactive voltages cancel while each may greatly exceed V0. RMS is peak/√2 only for the sinusoid. Cycle averaging gives ⟨P⟩=V0I0 cosφ/2=Irms²R, with no net cycle energy absorption in ideal L or C. Half-power occurs at |XL−XC|=R; ω±=√[ω0²+(R/2L)²]±R/(2L), Δω=R/L, Q=ω0L/R. This is a power FWHM, not current-amplitude FWHM (whose exact width is √3 R/L). The undriven oscillation frequency √[ω0²−(R/2L)²] and charge-amplitude resonance √[ω0²−R²/(2L²)] are distinct when applicable.

For parallel RLC, i=V0[(1/R)sinωt+(ωC−1/ωL)cosωt], so the admittance magnitude is √[R⁻²+(ωC−1/ωL)²]. Its current-leading phase θ has tanθ=R(ωC−1/ωL); with the original current-lag convention φ=−θ. At ω0 the source current is minimum V0/R, Z is maximum R, and the branch reactive currents cancel. For fixed ideal voltage, resistor power is V0²/(2R) at every frequency; resonance does not maximize that power. Transformer ratios assume common linked flux, negligible loss/leakage, and consistent winding voltage senses: |V2/V1|=N2/N1, |I1/I2|=N2/N1 for the ideal loaded model. Signs need winding polarity/current references; the undotted drawing alone does not fix them. A DC battery gives only switching transients, not continuous transformation.

## Source defects and missing premises

| Location (PDF page) | Classification and independently checked resolution |
|---|---|
| Chapter p9 text below Fig12.2.6 | The positive π/2 describes the magnitude of the lead, but the previously defined signed φ is −π/2. Preserve the distinction. |
| Chapter p10, Eqs12.3.4–8 | Source sign error, not a usable alternative convention: positive Q0 cos(ωt−φ) with their φ and i=dq/dt yields negative I0 and the negative of the specified forcing. Correct q with a leading minus and use I0=+V0/Z. The assertion that initial zero charge establishes the sign of i is also a missing reference convention. |
| Chapter p11, Eq12.3.9 | Valid under a reset time origin/current-reference phase; cannot simultaneously retain source V0 sinωt with nonzero φ. Presentation p30 explains the missing convention. |
| Chapter p17, Eqs12.4.12,14 | Source algebra error: the radicand uses (R/4L)²; quadratic formula requires (R/2L)². Their Δω=R/L and Q remain correct because the common erroneous square root cancels in the difference. |
| Chapter p19, Eq12.6.3 | Definite integral from 0 to t is V0(1−cosωt)/(ωL), not −V0 cosωt/(ωL). The printed final expression is the zero-offset sinusoidal particular response, requiring an initial current −V0/(ωL). |
| Chapter pp20–23, parallel phase | The plotted/formula φ is a current lead, opposite the chapter's initial current-lag φ. Correctable convention change if explicitly declared; inconsistent in a shared formula sheet without that declaration. Power factor is unaffected because cosine is even. |
| Chapter p25, Fig12.8.2 and surrounding text | Parallel-circuit inequalities are reversed: inductive branch dominance IL0>IC0 means XL<XC; capacitive dominance means XL>XC. The arrows/current dominance are physically consistent; the reactance captions are not. |
| Chapter p32, Eq12.9.27 | Printed Z=1/√(R²+ω²L²) has units of siemens. Correct Z=√(R²+ω²L²); the subsequent current formula already uses the correct denominator. |
| Chapter p33, Eq12.9.34 and sentence | VC(t)=I(t)XC is not an instantaneous relation. Capacitor energy peaks at zero current, a quarter cycle away from current magnitude peaks. The reported maximum UC,max=LV0²/(2R²) is nevertheless correct, because VC0=I0XC relates amplitudes. UL,max has the same value at resonance at different times. |
| Chapter p33, part(h) | Prose ω=2ω0=1/√LC is missing the factor 2 in its last member. The working uses 2/√LC and obtains the correct φ=atan[(3/2R)√(L/C)]. |
| Chapter p34, Eq12.9.40 prose | φ here is the input-to-output phase, not the angle between VL and VR (which is always π/2). Voltage symbols in the ratio must denote amplitudes. XR means R. |
| Chapter p35 high-pass chain | Its intermediate numerator ω²L² over √(R²+ω²L²) is wrong and dimensionful; use ωL. First and last expressions correctly give XL/√(R²+XL²). |
| Presentation pp8–11 | An undamped driven mass equation is followed by a finite rounded resonant displacement peak. That peak needs damping and a steady-state premise; at exact undamped resonance amplitude grows rather than staying constant. With viscous damping the displacement peak is slightly below the undamped ω0, not exactly at it. The plot is qualitative, unlike the exact series-current resonance later. |
| Presentation p4 | The underdamped envelope rate R/(2L) and criterion R<2ω0L are correct. With initially charged capacitor and zero current, q(t)=q0e^(−αt)[cosωdt+(α/ωd)sinωdt]; the schematic envelope labelled q0e^(−αt) is not the exact envelope for that initial state. |
| Presentation p17 | Hollow-square element/subscript is a source glyph defect. Generic element role is resolved by pp18–21; no new circuit element is implied. |
| Presentation p34 | Fourth equation is labelled VL although it is the capacitor equation VC=I0XC sin(ωt−π/2). The plotted capacitor row and phase are correct. |
| Presentation p38 | Width drawn on I0-versus-ω is qualitative. Do not infer that its half-height current width is the Chapter12 power width R/L. |
| Chapter pp24,36; presentation p13 | Minor wording/cross-reference defects: 'voltage and the phase' should say voltage and current; Fig12.10.1(b) reference in problem12.11.1 is Fig12.11.1(b). EMF is energy per charge (volts), not literally a mechanical force. |

## Recomputed examples and all questions

All figures in the mapped ranges were inspected, including circuit nodes, switch shunts, filter input/output taps, phasor directions, resonance curves, and PRS trace arrows. Numerical values below use unrounded intermediate quantities; rounded source answers agree except where flagged above.

| Item | Independent result and scope |
|---|---|
| 12.9.1 (pp26–27) | XL=32 Ω, XC=50 Ω, Z=43.8634 Ω, I0=0.91192 A, φ=−24.2277°. |
| 12.9.2 (pp27–28) | XC=200 Ω, XL=8 Ω, Z=196.122 Ω, I0=0.764828 A; VR0=30.593 V, VL0=6.11863 V, VC0=152.966 V. The b–d span is L+C, hence |Vbd,0|=146.847 V, not their amplitude sum. |
| 12.9.3 (pp28–29) | ω0=31622.8 rad/s, f0=5032.92 Hz, I0=10 A, Q=15.8114, VL0=3162.28 V. |
| 12.9.4 (pp29–30) | Output spans internal coil resistance R and L, so H=(R+jωL)/(R+r+jωL). Magnitude √[(R²+ω²L²)/((R+r)²+ω²L²)]; f=5.51329 Hz at gain 1/2. Low-frequency gain is 0.4, not zero; high-frequency gain tends to one. It is an unloaded voltage transfer, not a statement that total series current is high-pass. |
| 12.9.5 (pp30–33), parts(a–i) | Closed S1/S2 bypass L/C: i=V0 sinωt/R, ⟨P⟩=V0²/(2R). Only S1 open gives RL response with Z=√(R²+ω²L²), φ=atan(ωL/R). Both open and in phase require C=1/(ω0²L), Z=R. UC,max=UL,max=LV0²/(2R²), at different times. Doubling frequency gives φ=atan[(3/2R)√(L/C)]; XL=XC/2 gives ω=ω0/√2. No switch-opening impulse or apparatus transient is inferred. |
| 12.9.6 (pp33–35) | Output across R gives H=R/(R+jωL), R=138.564 Ω for 30° lag and ωL=80 Ω; magnitude cos30°=0.866025, low-pass. Exchanging R/L makes output across L, H=jωL/(R+jωL), high-pass. |
| 12.10 Q1–6 (pp35–36) | Doubling/halving ω halves/doubles XC. Capacitor returns energy whenever vi<0. Voltage lead implies series ω>ω0. Q3 drawing has VL0>VC0: above resonance; add their difference to VR0, giving a resultant to the right and below horizontal and a positive lead relative to VR0, roughly 30° (drawing not calibrated). Power factor R/√(R²+X²) increases with R for fixed X≠0; changing L or C moves toward or away from X=0, so no universal monotone claim. Battery cannot sustain ideal transformer output at DC. cosφ=1/2 alone gives ±60° and cannot determine lead/lag. |
| 12.11.1 (p36) | Capacitor I0=0.015 A or 0.150 A. Inductor ω=28888.9 rad/s, f=4597.81 Hz, I0=0.230769 A. Equal reactance at f=1061.03 Hz, X=300 Ω, equal to ideal free-LC frequency. |
| 12.11.2 (pp36–37) | Current peak at ω0=1/√LC; Imax=V0/R, φ=0. On high-frequency half-power side I=Imax/√2 gives φ=+π/4, current lag. |
| 12.11.3 (p37) | XC=12500 Ω, Z=13124.4 Ω, Irms=5.38772 mA, φ=−72.2553°, ⟨P⟩=0.116110 W. Peak VR=30.4776 V, VC=95.2424 V; RMS values are these/√2. Instantaneous vR=VR0 sin(ωt−φ), vC=VC0 sin(ωt−φ−π/2). |
| 12.11.4 (pp37–38) | Current leads 45°; input is net capacitive, not at zero-phase resonance; PF=1/√2 and ⟨P⟩=45.2548 W. Input impedance 50∠−45° Ω. Under the stated passive ideal-RLC model there must be dissipation and capacitive contribution, but an inductor cannot be excluded and unique topology/component values cannot be inferred. Without that model even named internal components are not identifiable from one-frequency terminal data. |
| 12.11.5 (pp38–39) | iR=V0 sinωt/R, iL=−V0 cosωt/(ωL), I0=V0√[R⁻²+(ωL)⁻²], Z=[R⁻²+(ωL)⁻²]^−1/2, original-convention lag φ=atan[R/(ωL)]. Zero-offset sinusoidal response stipulated. |
| 12.11.6 (p39) | q/q0=1/2, UC/UC,max=1/4, |i|/Imax=√3/2, UL/UL,max=3/4 at T/6. Signed current depends on the reference; with i=dq/dt it is −√3/2. |
| 12.11.7 (pp39–40) | iR=V0 sinωt/R, iC=ωCV0 cosωt, I0=V0√[R⁻²+(ωC)²], Z=[R⁻²+(ωC)²]^−1/2; current leads atan(ωCR), hence original φ=−atan(ωCR). |
| 12.11.8 (p40) | ω0=1118.034 rad/s, resonant Irms=7.07107 A. At 4000 rad/s: XC=125 Ω, XL=1600 Ω, Z=1475.034 Ω, φ=89.6116°. |
| 12.11.9 (p40) | Ideal antenna-equivalent problem: ω0=10^9 rad/s, Q=10, I0=10^−7 A, VC0=10^−4 V. This is an idealized circuit, not an antenna wiring prescription or a guarantee of useful reception. |
| 12.11.10 (p41), parts(a–j) | Interpret '10^−2 times less' as I(89.5)/I(89.7)=0.01 and equal drive amplitudes. ω0=5.63601722×10^8 rad/s. Minimal L=R√9999/(ω0²/ω1−ω1)=39.74234 μH; C=79.213996 fF; Q=22398.8521. At resonance VL0/V0=VC0/V0=Q. ⟨P⟩0=V0²/(2R), ⟨P⟩1=10^−4⟨P⟩0; φ1=−atan√9999=−89.4270° (capacitive). There is no numerical V0 in this problem; do not reuse the preceding problem's amplitude. These ideal values ignore parasitics and feasibility. |
| PRS pp1–2 | Answer2: red current peaks later than black voltage, so current lags. |
| PRS pp3–4 | Answer3: positive straight I–V line means in phase for same-frequency sinusoids, independent of the drawn line's slope angle. |
| PRS pp5–6 | Answer1: ellipse arrow runs counterclockwise with voltage horizontal/current vertical; starting at positive V maximum, I rises toward its maximum, so I lags by approximately π/2. Without the time arrow the ellipse alone would not fix lead versus lag. |
| PRS pp7–8 | Answer3: current leads, hence XC>XL. 'Dominated by capacitance' here means sign of net reactance; the graph does not establish XC≫R or negligible dissipation. |
| PRS pp9–10 | Answer1: current lags, XL>XC, so ω²>1/(LC). |

## Demonstration and experiment limits

Presentation pp7,10,14,24,39 announce demonstrations but supply no measured outcomes. Pages41–42 identify Experiment11, Part I using exp11a.ds to vary frequency and seek maximum current while looking at I and V; Part II uses exp11b.ds at unspecified listed frequencies to plot I0 versus ω. The assigned packet contains neither those program files, the frequency list, component values, apparatus wiring, instrument settings nor results. Current-max resonance follows the ideal constant-voltage model; a changing source amplitude or effective series resistance must be accounted for in an actual experiment. No missing details or measurements have been invented. External applet/video functionality and separate lab manuals are outside the original assigned boundary.

## Research and remaining limits

No external technical research was necessary for D121: the consequential corrections follow by explicit differentiation, integration, phasor addition, quadratic solution, dimensions, and the numerical recomputations above. The source's 120 V/60 Hz statement is treated only as its nominal historical example, not as a current electrical-service specification. Unresolved limits are the unprovided experiment details, qualitative/unscaled diagrams, terminal-data non-uniqueness, and real-component departures from ideal models. Those limits do not erase the complete text/visual reading. Source preparation does not authorize subsequent teaching or closure.
