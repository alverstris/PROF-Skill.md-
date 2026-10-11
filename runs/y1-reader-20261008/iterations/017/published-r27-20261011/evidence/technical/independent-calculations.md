# D017 r27 independent calculations

Performed from author/prompts-only.md before opening output/teaching.md or any proposed solutions. The original five source page texts had been read; no author solution record was consulted.

Q1: F'(x)=x², continuous everywhere, hence FTC on [-1,2]. F(2)-F(-1)=(8/3+7)-(-1/3+7)=3. Equal additive constants cancel.

Q2: v=2(t-1) is negative for 0≤t<1 and positive for 1<t≤3; direction changes at t=1 s. Displacement = integral_0^3 (2t-2)dt = [t²-2t]_0^3 = 3 m. Integral_0^1 v=-1 m; integral_1^3 v=4 m; distance = -(-1)+4=5 m, equivalently integral_0^3 |v|dt. This is one-dimensional signed velocity, not speed.

Q3: integral_a^b f + integral_b^c f = integral_a^c f, so integral_a^b f=7-10=-3. Reversal gives integral_c^b f=-10 and integral_c^a f=-7. Increasing endpoint order does not force a nonnegative integral: f may be negative, with net negative contribution on [a,b].

Q4: On [0,2], 1+x≤e^x and integration preserves order. Integral_0^2(1+x)dx=[x+x²/2]_0^2=4; integral_0^2e^x dx=e²-1. Thus e²≥5. Reversal negates both: integral_2^0(1+x)dx=-4 ≥ 1-e²=integral_2^0e^x dx. Multiplication by -1 reverses the comparison.

Q5: A contains x dx, and u=1+x² gives du=2x dx, x dx=du/2. Endpoints x=0,1 give u=1,2. A=(1/2)integral_1^2u³du=[u^4/8]_1^2=(16-1)/8=15/8. B lacks x, so dx cannot be replaced by du/2; that replacement would imply du=2dx rather than du=2x dx. Direct expansion could evaluate B but is not requested.

Q6: Recall statement: if f is continuous on [a,b] and F'=f on the interval (with endpoint evaluations defined), integral_a^b f=F(b)-F(a). For reversed endpoints use the corresponding oriented convention. With f=x(x²-1)=x³-x, antiderivative F=x^4/4-x²/2. Roots on [0,2] are 0 and 1; f<0 on (0,1), f>0 on (1,2]. I=F(2)-F(0)=4-2=2. Signed first piece=-1/4; signed second piece=2-(-1/4)=9/4. Geometric area=1/4+9/4=5/2. J=-I=-2. Polynomial expansion/integration is an efficient exact method. The area differs because the negative piece contributes positively to area. A substitution u=x²-1 also works, but is unnecessary. This audit is an independent expert calculation, not observed student recall or student understanding.
