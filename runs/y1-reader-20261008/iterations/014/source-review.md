# D014 source review

Mapping: D014 = MIT 18.01 Fall 2006, Lecture 15, Differentials and Antiderivatives. SOURCE preparation only. All five cached text files were checked/read; cached PDF-page-5 text was empty, so that page's 1016-character text was re-extracted directly from the verified PDF and read. All five 1224 by 1584 page renders were individually inspected, including all displayed formulas. There are no figures. PDF page 1 is the cover; PDF pages 2-5 are printed pages 1-4.

PDF: /workspace/scratch/ac36b9c5ff31/prof-readability/audit-1801-notes/L15/lec15.pdf
Official asset: https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/c07ab6e13cf8684dd98b2650b64672fb_lec15.pdf
SHA-256 recomputed: 10c3dc97fa877d3ed97c5561b5082dca3006c632d85e58e01d059484ae455323. Exact audit.json match; 130,496 bytes, five pages.

Evidence discrepancy, resolved: audit.json records 1016 text characters for PDF p5, but lec15-p05.txt currently contains zero. The verified PDF's page 5 re-extracts to 1016 characters, and its existing full-page render shows the complete page. The supplement is saved in this packet as lec15-p05-reextracted.txt. The original audit/cache files were not modified. All other text lengths across L13-L15 match their manifests. This is a cache discrepancy, not a source-content defect or missing PDF page.

## Page coverage

| PDF page | Printed page | Content and visual inspection |
| --- | --- | --- |
| 1 | cover | MIT OCW course, term and terms notice. |
| 2 | 1 | Differential notation; cube-root approximation by linearization and binomial approximation; 64.1 variant. |
| 3 | 2 | Differential method for the same approximation; antiderivative definition; all six basic formulas; logarithm derivative for x<0. |
| 4 | 3 | Antiderivative uniqueness proof; substitution examples 1-3, including all chain factors and constants. |
| 5 | 4 | Examples 4-6: Gaussian factor, equivalent trigonometric primitives, and 1/(x ln x); read recovered text and full render. |

## Resolved mathematical witnesses

At base point a, dy=f'(a)dx is the exact differential, while Δy=f(a+dx)-f(a)=dy+o(|dx|). Thus dy is generally not the actual finite change. For f(x)=x^(1/3), f'(64)=1/48, and all three methods correctly produce the linear approximation 65^(1/3)≈4+1/48=193/48≈4.02. Actual 65^(1/3)≈4.020725758589, while 193/48≈4.020833333333. In particular (193/48)³=65+577/110592, directly disproving exact equality. Since f''(x)=-2/(9x^(5/3))<0 on this interval, the tangent overestimates. For h≥0 near this example, the error magnitude is at most h²/9216 on [64,64+h]; at h=1 its actual value is about 0.0001075747443, and at h=0.1 the approximation 4+1/480 has error about 0.00000108412852. The stated numeric approximations are appropriate. The binomial step uses the new small parameter h/64, not the original coordinate x.

The six basic primitives differentiate correctly on their real domains:

| Integrand | Primitive | Domain qualification |
| --- | --- | --- |
| sin x | -cos x+C | All real x. |
| x^n | x^(n+1)/(n+1)+C | n≠-1; work on an interval where the chosen real power is defined and differentiable. For arbitrary real n, x>0 is a uniform sufficient domain. Integer and certain rational powers admit larger domains. |
| 1/x | ln|x|+C | Each of (-∞,0) and (0,∞), with potentially different constants. |
| sec²x | tan x+C | Each interval avoiding π/2+kπ. |
| 1/√(1-x²) | arcsin x+C | -1<x<1. The primitive extends continuously to ±1 but the integrand and finite derivative do not. |
| 1/(1+x²) | arctan x+C | All real x. |

For x<0, ln|x|=ln(-x), whose chain-rule derivative (1/(-x))(-1)=1/x is correct. The inverse-trig notation refers to principal inverse functions, not reciprocals. The derivative of x^(1/3) is used only at 64; its finite derivative formula does not extend to x=0.

On a common interval, F'=G'=f implies (G-F)'=0, and the MVT implies G-F is one constant. On disconnected domains, the constant can vary by component. For example, on R without zero, F=ln|x| and G=ln|x| for x<0 but G=ln|x|+1 for x>0 have the same derivative without a single global difference constant.

Every worked substitution/guessing example was checked by differentiation:

| Example | Verified primitive | Derivative witness and boundaries |
| --- | --- | --- |
| 1, PDF p4 | (x⁴+2)⁶/24+C | Chain factor (6/24)(x⁴+2)⁵(4x³)=x³(x⁴+2)⁵; all real x, including 0. Global invertibility of u=x⁴+2 is unnecessary for this indefinite-antiderivative identity. |
| 2, PDF p4 | √(1+x²)+C | Derivative (1/2)(1+x²)^(-1/2)(2x)=x/√(1+x²); denominator positive for every real x. |
| 3, PDF p4 | e^(6x)/6+C | Derivative e^(6x); all real x. |
| 4, PDF p5 | -e^(-x²)/2+C | Derivative (-1/2)e^(-x²)(-2x)=xe^(-x²); all real x. |
| 5, PDF p5 | sin²x/2+C or -cos²x/2+C | Both derivatives equal sin x cos x; the two chosen primitives differ by 1/2. Their families agree after shifting the constant, not by keeping equal numerical constants in both forms. |
| 6, PDF p5 | ln|ln x|+C | On (0,1) and (1,∞), derivative is (1/ln x)(1/x)=1/(x ln x). Independent constants may be chosen on the two components. |

In example 6, u=ln x and du=dx/x are valid for x>0. For 0<x<1, u<0, so the primitive of 1/u must use ln|u|. At x=1, the original integrand is undefined. On x>1 alone, the source's ln(ln x)+C is correct. For a concrete missing branch, at x=1/2 the integrand equals -2/ln 2, a finite real number, while ln(ln(1/2)) is not real.

## Confirmed source errors

1. PDF p2, printed p1: Method 1 uses an exact equals sign from 65^(1/3) to its first-order approximation. It must be ≈; the exact cube discrepancy above is a witness.
2. PDF p3, printed p2: Method 3 again states 65^(1/3)=4+1/48 exactly. It must be ≈. The differential dy=1/48 itself is exact for dx=1 at the base point; the finite increment is not.
3. PDF p3, printed p2: 'Proof of Property 2' actually proves listed property 3, the 1/x logarithm formula.
4. PDF p4, printed p3: 'constant factor c' in G=F+c should be additive constant c, as the heading and proof correctly say.
5. PDF p4, printed p3: example 1 briefly writes the primitive u⁶/[4(6)] without +C and then sets it equal to u⁶/24+C. With arbitrary C those two expressions are not literally equal. Include +C at the first evaluated primitive, or explicitly speak of selected representatives; the final answer and derivative are correct.
6. PDF p5, printed p4: example 6 claims ln(ln x)+C under only x>0. That expression is not a real antiderivative on the permitted interval (0,1). Correct it to ln|ln x|+C on each component, or explicitly strengthen the problem to x>1. This is a confirmed domain/formula mismatch, not a mere unproved step.

## Missing conditions and pedagogical omissions

- Differential notation needs the distinction between exact dy=f'(a)dx and approximate Δy≈dy; the finite-difference quotient requires nonzero Δx. The example's exact-equality errors are listed separately above.
- General real powers and the trigonometric/logarithmic primitive table need the domains in the table. In particular inverse-sine derivative endpoints, tangent poles and x=0 for 1/x must be excluded.
- Uniqueness up to one constant requires a common interval; otherwise it is componentwise, as the counterexample shows.
- Example 6 must exclude x=1 even under its stated x>0 assumption. Its additional omission of | | has a concrete failure on (0,1), classified above as a source error.
- F=∫f dx denotes a chosen antiderivative or the family of all antiderivatives, according to convention; it must not be interpreted as guaranteeing a unique primitive before an additive constant/base value is fixed. Substitution is justified here by the chain rule and verified derivatives.

Open technical uncertainties: none. The text-cache discrepancy was resolved without changing the source or its cache. No teaching audit, external record, or repository was edited.
