Prospective GitHub mathematics check

This independent fixture checks representation support. It is not a revision of the frozen lecture or evidence of teaching acceptance. Read all expressions, then open the two disclosures and inspect their mathematics.

Plain content

P1. Named function inline: $`\mathrm{Aux}(u)=u^2`$.

P2. Strict comparisons inline: $`u\lt v\gt w`$.

P3. Named function, square root, prime and comparisons in a display:

```math
\mathrm{Aux}'(u)=2u,\qquad \sqrt{u^2}=u\quad(u\gt 0).
```

P4. A displayed piecewise expression:

```math
M(u)=\begin{cases}u,&u\lt 0,\\u^2,&u\ge 0.\end{cases}
```

Initially closed content

<details>
<summary>Open closed test group</summary>

C1. Named function inline: $`\mathrm{Aux}(v)=v^2`$.

C2. Fenced display within initially closed disclosure:

```math
\mathrm{Aux}'(v)=2v\quad(v\lt 0).
```

C3. Double-dollar display within initially closed disclosure:

$$
\mathrm{Aux}'(w)=2w\quad(w\gt 0).
$$

</details>

Initially open content

<details open>
<summary>Open test group</summary>

O1. Named function inline: $`\mathrm{Aux}(z)=z^2`$.

O2. Fenced display within initially open disclosure:

```math
\mathrm{Aux}'(z)=2z\quad(z\lt 0).
```

O3. Double-dollar display within initially open disclosure:

$$
\mathrm{Aux}'(y)=2y\quad(y\gt 0).
$$

</details>

End of fixture. Expected mathematical expressions: ten, consisting of four inline and six display expressions. Every operand, comparison, case row and closing delimiter must remain visible; raw TeX or an error notice is a failed expression.
