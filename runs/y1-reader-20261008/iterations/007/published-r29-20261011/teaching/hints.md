Lecture 7 — hints

Use the hint for the first decision that blocks you, then return to the prompt. The full answers are in the separate [solutions file](solutions.md).

<a id="h1"></a>

Hint P1

Write the definition as $`q(x)=(e^{2x}+e^{-2x})/2`$. The two inner inputs have derivatives $`2`$ and $`-2`$. Keep those multipliers attached to their exponentials before combining anything. For the value at zero, both exponential values are 1. [Return to P1](lesson.md#p1)

<a id="h2"></a>

Hint P2

For a quotient-rule route use $`u=\sin x`$ and $`v=1+\cos x`$. Then $`u'=\cos x`$ and $`v'=-\sin x`$. The second term in $`u'v-uv'`$ consequently has two minus signs. After expansion, look for $`\sin^2x+\cos^2x`$. The denominator restriction comes from $`1+\cos x=0`$ in the original function. [Return to P2](lesson.md#p2)

<a id="h3"></a>

Hint P3

Differentiate $`xy`$ as $`1\cdot y+xy'`$. The derivative of $`y^2`$ is $`2yy'`$. Put terms containing $`y'`$ on one side, factor out $`y'`$, then substitute the point. A tangent of slope $`m`$ through $`(1,2)`$ has equation $`y-2=m(x-1)`$. [Return to P3](lesson.md#p3)

<a id="h4"></a>

Hint P4

After applying the addition identity, the numerator is $`\cos x\cos h-\sin x\sin h-\cos x`$. Group the first and last terms together. That gives one multiple of $`(\cos h-1)/h`$ and one multiple of $`\sin h/h`$. Only $`h`$ varies in the limit. [Return to P4](lesson.md#p4)

<a id="h5"></a>

Hint P5

For positive $`x`$, either write $`y=e^{x\ln x}`$ or take logarithms to obtain $`\ln y=x\ln x`$. The exponent, or the right-hand side of the logarithmic equation, is a product of two varying factors. Differentiate both factors using the product rule. [Return to P5](lesson.md#p5)

<a id="h6"></a>

Hint P6

(a) Set $`y=\arcsin(2x)`$, so $`\sin y=2x`$. The derivative of the right side is 2. To eliminate $`y`$, use $`\cos^2y=1-(2x)^2`$ and the principal arcsine range. Check separately when $`2x`$ is an allowed arcsine input and when the eventual denominator is nonzero.

(b) Call the exponent $`w=x^2\arctan x`$. Write $`B'=e^w w'`$ first. To obtain $`w'`$, the factors $`x^2`$ and $`\arctan x`$ contribute derivatives $`2x`$ and $`1/(1+x^2)`$, respectively. Do not insert $`x=1`$ before differentiating. [Return to P6](lesson.md#p6)

[Return to the lesson](lesson.md) · [Open the complete solutions](solutions.md)
