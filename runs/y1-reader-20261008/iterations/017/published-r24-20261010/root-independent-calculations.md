# Independent calculations before seeing authored solutions

Material: D017, generated from published PROF r24.

Reviewer: root coordinator. Inputs for these calculations were the prompts-only packet and the original source already inspected. The generated lesson, hints and solutions had not been opened when this record was written. This is a mathematical reference for later comparison, not a SASIS reader report or a teaching acceptance decision.

## Learner prompts

P1. Take F(x)=x^3-2x. Its derivative is 3x^2-2, F(2)=4 and F(-1)=1. The integral is 4-1=3. Adding C to both endpoint values leaves their difference unchanged.

P2. cos(t) is positive before pi/2, zero at pi/2 and negative afterwards on this interval. The velocity changes sign, so the turning time is pi/2 seconds. The displacement is sin(pi)-sin(0)=0 metres. The distance is [sin(pi/2)-sin(0)]-[sin(pi)-sin(pi/2)]=2 metres. The return portion contributes negatively to displacement and positively to distance.

P3. Additivity gives the integral from -1 to 4 as 5+(-3)=2. Reversing it gives -2; reversing the supplied second integral gives 3. The geometric area is not uniquely fixed; it is at least |5|+|-3|=8. This bound can be attained by a continuous function: use (10/9)(2-x) on [-1,2] and -(3/2)(x-2) on [2,4]. Both pieces meet at zero, with the required integrals and no within-piece cancellation. Adding 10 sin(2 pi (x+1)/3) to the first piece preserves its integral and its endpoint value at x=2, but creates a negative region within that piece (for example at x=5/4). Its unsigned area is then greater than 5, so the total exceeds 8. Thus continuity does not remove the nonuniqueness.

P4. For x>=0, r'(x)=e^x-1-x>=0 by the given earlier bound, and r(0)=0. Therefore r(x)>=0 and e^x>=1+x+x^2/2. Integration from 0 to 1 yields e-1>=1+1/2+1/6=5/3, hence e>=8/3. This exceeds 5/2 by 1/6. The derivative comparison and its domain must precede the integration conclusion.

P5. With u=4-x^2, du=-2x dx. The old endpoints 1 and 2 map respectively to 3 and 0. The integral is -(1/2) integral_3^0 u^3 du=-(1/8)(0^4-3^4)=81/8. The original integrand is nonnegative on [1,2] and positive before the upper endpoint, consistent with this positive result.

P6. Under the usual endpoint-evaluation hypotheses (continuous integrand on the interval and an antiderivative there), the oriented integral is F(b)-F(a). Here F(x)=e^(x^2-3x), whose derivative is exactly the supplied f. Both endpoint values are e^-2, so the signed integral is zero. The exponential factor is strictly positive; f is negative on [1,3/2), zero at 3/2, and positive on (3/2,2]. At the split, F(3/2)=e^(-9/4). The geometric area is 2(e^-2-e^(-9/4)), strictly positive. Equal opposite signed contributions cancel without making their separate magnitudes zero.

## Worked source results

1. Integral_a^b x^2 dx=(b^3-a^3)/3, including reversed endpoints.
2. Integral_0^pi sin(x) dx=2, using -cos(x).
3. Integral_0^1 x^5 dx=1/6, using x^6/6.
4. Integral_0^(2pi) sin(x) dx=0. Its two signed halves are +2 and -2; geometric area is 4.
5. Integral_3^1 2x dx=-8. Integral_1^2 2x dx=3 and integral_2^3 2x dx=5; their sum is 8.
6. On x>=0, e^x>=1 gives integral_0^1 e^x dx=e-1>=1, so e>=2. For h(x)=e^x-1-x, h(0)=0 and h'(x)=e^x-1>=0 imply e^x>=1+x. Its integral then yields e-1>=3/2, so e>=5/2.
7. For integral_1^2 (x^3+2)^4 x^2 dx, let u=x^3+2 and du=3x^2 dx. The bounds are 3 and 10; the result is (10^5-3^5)/15=99757/15.

## Scope and subsequent check

These are independently derived answers, not evidence that every explanation in the generated document is accessible or correct. Once the document is frozen, compare its actual claims, method conditions, sign decisions, units and help against these calculations. Numerical cross-checks, if present in the adjacent JSON, corroborate selected results and do not replace the analytic arguments above.
