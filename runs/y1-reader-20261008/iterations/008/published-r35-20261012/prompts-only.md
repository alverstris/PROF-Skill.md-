Exercise D008-E1. An early approximation

Estimate $`\sqrt{4.08}`$ using a tangent approximation to $`f(x)=\sqrt{x}`$ at $`x_0=4`$. State the increment, construct the tangent formula, and explain why this is an estimate rather than an identity. Your response should show how the base point and derivative enter, not only a decimal.

Exercise D008-E2. A limit from local change

For $`g(x)=e^{3x}(1-2x)`$, construct its linear approximation at zero by combining basic approximations. Then determine

```math
\lim_{x\to0}\frac{e^{3x}(1-2x)-1}{x}.
```

Explain what licenses the limit: use the derivative definition with an independently computed derivative, or explicitly show that the omitted error divided by $`x`$ tends to zero. An approximate equality by itself is not a proof of a limit.

Exercise D008-E3. Move the base point

Construct the quadratic approximation to $`f(x)=\ln x`$ at $`x_0=2`$ and use it to estimate $`\ln(2.1)-\ln2`$. Keep the displacement from the base point explicit and show why the coefficient of its square is half the second derivative. No numerical value of $`\ln2`$ is needed.

Exercise D008-E4. When the first change cancels

Find the linear and quadratic approximations at zero of $`H(x)=e^x/\sqrt{1+2x}`$, for $`x`$ near zero with $`1+2x\gt 0`$. Show all contributions through degree two. Explain what the linear approximation misses and what the quadratic approximation predicts about the leading change on the two sides of zero. Distinguish a local prediction from an identity for all allowed inputs.

Exercise D008-E5. Choose enough accuracy

In the stated constant-speed, gravity-free clock model, let $`z=v^2/c^2=10^{-4}`$ and let the onboard proper interval be $`T=1000\,\mathrm{s}`$. The ground-frame interval is $`T'=T F(z)`$, where $`F(z)=(1-z)^{-1/2}`$. Use the linear and quadratic approximations of $`F`$ at zero to estimate $`T'-T`$.

The required absolute error in $`T'`$ is at most $`10^{-5}\,\mathrm{s}`$. On $`0\le z\le10^{-4}`$, you may use the verified bound $`|F''(z)|\le1`$ and the linear-error bound $`|F(z)-F(0)-F'(0)z|\le z^2/2`$. Decide whether the linear calculation alone already meets the requirement. Compare the quadratic correction with that requirement and explain why a small next term alone would not generally be a complete error guarantee. Show the units and the variable in which each approximation is linear or quadratic.

Exercise D008-E6. Return later and choose the method

After a break of a length convenient for you, first write the formulas for a linear and a quadratic approximation at a general base point from memory, then check them against the notes. This is a recall opportunity, not a scored test. Next justify each of these decisions using the notes:

- Does moving from the linear to the quadratic approximation at zero improve the polynomial used for $`\sin x`$? Identify the first nonzero correction available in the stated sine expansion.
- Is $`e^{50x}\approx1+50x`$ justified as a small-input estimate at $`x=0.02`$ merely because $`x`$ is numerically small? Identify the effective input and explain the limitation.
- Can the usual finite-slope tangent formula at zero approximate $`\sqrt{x}`$ for small positive $`x`$? Check the derivative requirement using its difference quotient at zero.

Your response should state the condition or coefficient controlling each choice. This changed application is distinct from recalling the formulas.
