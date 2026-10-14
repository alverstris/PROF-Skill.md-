<a id="d008-hints-start"></a>
Hints for Linear and quadratic approximations

Use the matching hint when you need an intermediate step. Complete solutions are in a different file so you can return to the problem before seeing an answer. Parts of a multi-part hint follow the order of that problem. These are hints for the generated Attempts A–F in the main teaching file.

<a id="d008-hints-a"></a>
Hint A

Write the target input as $`1+u=0.96`$. The tangent's value change is its slope 1 multiplied by that signed $`u`$. To explain the approximation sign, compare the derivative of $`\ln x`$ at a variable $`x`$ with the constant derivative of the tangent.

[Return to Attempt A](main.md#d008-main-task-a) · [Complete solution A](solutions.md#d008-solutions-a)

<a id="d008-hints-b"></a>
Hint B

Rewrite the denominator as a factor:

```math
g(x)=e^{3x}(1-2x)^{-1/2}.
```

Use $`u=3x`$ for the exponential and $`u=-2x`$, $`r=-1/2`$ for the other factor. Compute $`ru`$ before multiplying. The real reciprocal square root needs $`1-2x\gt 0`$. In the product, both a linear term times a constant and a constant times a linear term contribute to the slope.

[Return to Attempt B](main.md#d008-main-task-b) · [Complete solution B](solutions.md#d008-solutions-b)

<a id="d008-hints-c"></a>
Hint C

Write the function as its degree-two polynomial plus $`E_2(x)`$. Place that whole expression into the numerator before cancelling anything. The local-error statement you need is $`E_2(x)/x^2\to0`$; compare it with the weaker statement available from a linear model.

[Return to Attempt C](main.md#d008-main-task-c) · [Complete solution C](solutions.md#d008-solutions-c)

<a id="d008-hints-d"></a>
Hint D

(a) Replace $`v`$ by $`2v`$ inside $`z=v^2/c^2`$. Then follow that change through a term proportional to $`z`$ and one proportional to $`z^2`$.

(b) Start with the original added term $`1.19\times10^{-20}`$. Apply the factor from part (a), then put both results into the same power-of-ten scale as $`10^{-19}`$.

(c) The expansion variable is the square of 0.8. Use that number in both polynomials. The exact factor is $`1/0.6`$. An improvement between two polynomial estimates can occur even when the small-input justification is weak; compare both with the exact value to judge this case.

[Return to Attempt D](main.md#d008-main-task-d) · [Complete solution D](solutions.md#d008-solutions-d)

<a id="d008-hints-e"></a>
Hint E

Set $`h=t-2\ \mathrm{s}`$. The quadratic coefficient is half the second derivative, so its units must cancel the two powers of time in $`h^2`$. To investigate the claimed error guarantee, imagine adding a cubic term $`Kh^3`$ to the polynomial. Its value, first derivative and second derivative all vanish at $`h=0`$. The supplied local measurements cannot detect its coefficient $`K`$.

[Return to Attempt E](main.md#d008-main-task-e) · [Complete solution E](solutions.md#d008-solutions-e)

<a id="d008-hints-f"></a>
Hint F

(a) Start from $`a+bh+dh^2`$ with $`h=x-x_0`$. Its first two derivatives at the basepoint determine $`b`$ and $`2d`$.

(b) Use $`u=2x`$ inside the logarithm, including its square. For the reciprocal factor use $`r=-1`$, $`u=x`$. In the product there is no constant from the logarithm. List the products of total degree one and two.

(c) Replace $`H`$ by its polynomial plus an error whose ratio to $`x^2`$ tends to zero. Check what remains after subtracting the stated term.

(d) A zero second derivative at one point removes one coefficient. A function that is exactly affine has no higher-degree terms anywhere. Decide which fact applies to each example.

[Return to Attempt F](main.md#d008-main-task-f) · [Complete solution F](solutions.md#d008-solutions-f)

[Return to the reading route](main.md#d008-main-linear) · [Complete solutions](solutions.md#d008-solutions-start)
