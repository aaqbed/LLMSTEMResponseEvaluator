# Benchmark Ground-Truth Solutions (Math and Science)

---

## Mathematics Reference Solutions

### P06 (Algebra I - System of Equations) 

### Problem Statement
Solve the following system of linear equations for $x$ and $y$ using substitution or elimination. Show all algebraic steps:
$$3x - 4y = 18 \quad (1)$$
$$5x + 2y = 4 \quad (2)$$

* **Step-by-Step Elimination:**
    * Multiply bottom equation by 2: $10x + 4y = 8$.
    * Add the resulting equation to equation 1:
        $$(3x - 4y) + (10x + 4y) = 18 + 8 \implies 13x = 26 \implies x = 2$$
    * Substitute $x = 2$ into equation 2:
        $$5(2) + 2y = 4 \implies 10 + 2y = 4 \implies 2y = -6 \implies y = -3$$

### Verification
* Equation $(1)$: $3(2) - 4(-3) = 6 + 12 = 18$ (True)
* Equation $(2)$: $5(2) + 2(-3) = 10 - 6 = 4$ (True)

* **Final Answer:** $(x,y) = (2,-3)$

---

### P07 (Algebra II - Identity Simplification)

### Problem Statement
Simplify the following trigonometric expression into a single trigonometric function or constant, showing each identity applied:
$$\frac{\sin(x)}{1 + \cos(x)} + \frac{1 + \cos(x)}{\sin(x)}$$

* **Step-by-Step Solution:**
    * Combine over common denominator $\sin(x)(1 + \cos(x))$:
        $$\frac{\sin^2(x) + (1 + \cos(x))^2}{\sin(x)(1 + \cos(x))}$$
    * Expand numerator:
        $$\sin^2(x) + 1 + 2\cos(x) + \cos^2(x)$$
    * Apply Pythagorean identity $\sin^2(x) + \cos^2(x) = 1$:
        $$1 + 1 + 2\cos(x) = 2 + 2\cos(x) = 2(1 + \cos(x))$$
    * Simplify fraction:
        $$\frac{2(1 + \cos(x))}{\sin(x)(1 + \cos(x))} = \frac{2}{\sin(x)} = 2\csc(x)$$
* **Final Answer:** $2\csc(x)$

---

### P08 (Calculus I - Extrema and Inflection Points)

### Problem Statement
Find the exact coordinates $(x, y)$ of all local extrema and inflection points for the function $f(x) = (x^2 - 4)e^{-x}$. Show your first and second derivatives and justify using the first or second derivative test.

* **First Derivative $f'(x)$:**
    * $f'(x) = \frac{d}{dx}[x^2 - 4]e^{-x} + (x^2 - 4)\frac{d}{dx}[e^{-x}] = 2xe^{-x} - (x^2 - 4)e^{-x} = (-x^2 + 2x + 4)e^{-x}$$
* **Critical Points ($f'(x) = 0$):**
    $$-x^2 + 2x + 4 = 0 \implies x^2 - 2x - 4 = 0 \implies x = \frac{2 \pm \sqrt{4 - 4(1)(-4)}}{2} = 1 \pm \sqrt{5}$$
* **Second Derivative $f''(x)$:**
    $$f''(x) = \frac{d}{dx}[-x^2 + 2x + 4]e^{-x} + (-x^2 + 2x + 4)\frac{d}{dx}[e^{-x}] = (-2x + 2)e^{-x} + (-x^2 + 2x + 4)(-e^{-x}) = (-2x + 2)e^{-x} + (x^2 - 2x - 4)e^{-x} = (x^2 - 4x - 2)e^{-x}$$
* **Classify Extrema (Second Derivative Test):**
    * For $x = 1 - \sqrt{5} \approx -1.236$:
     $$f''(1 - \sqrt{5}) = ((1-\sqrt{5})^2 - 4(1-\sqrt{5}) - 2)e^{-(1-\sqrt{5})} = 2\sqrt{5}e^{\sqrt{5}-1} > 0 \implies \text{Local Minimum}$$
     $$y\text{-value}: ((1-\sqrt{5})^2 - 4)e^{-(1-\sqrt{5})} = (2 - 2\sqrt{5})e^{\sqrt{5}-1}$$
   * For $x = 1 + \sqrt{5} \approx 3.236$:
     $$f''(1 + \sqrt{5}) = -2\sqrt{5}e^{-(1+\sqrt{5})} < 0 \implies \text{Local Maximum}$$
     $$y\text{-value}: ((1+\sqrt{5})^2 - 4)e^{-(1+\sqrt{5})} = (2 + 2\sqrt{5})e^{-(1+\sqrt{5})}$$
* **Inflection Points ($f''(x) = 0$ with sign change):**
   $$x^2 - 4x - 2 = 0 \implies x = \frac{4 \pm \sqrt{16 - 4(1)(-2)}}{2} = 2 \pm \sqrt{6}$$
   * For $x = 2 - \sqrt{6}$:
     $$y = ((2-\sqrt{6})^2 - 4)e^{-(2-\sqrt{6})} = (6 - 4\sqrt{6})e^{\sqrt{6}-2}$$
   * For $x = 2 + \sqrt{6}$:
     $$y = ((2+\sqrt{6})^2 - 4)e^{-(2+\sqrt{6})} = (6 + 4\sqrt{6})e^{-(2+\sqrt{6})}$$

### Final Answer
* **First Derivative:** $f'(x) = (-x^2 + 2x ++ 4)e^{-x}$
* **Second Derivative:** $f''(x) = (x^2 - 4x - 2)e^{-x}$
* **Local Minimum:** $\left(1 - \sqrt{5}, \, (2 - 2\sqrt{5})e^{\sqrt{5}-1}\right)$
* **Local Maximum:** $\left(1 + \sqrt{5}, \, (2 + 2\sqrt{5})e^{-(1+\sqrt{5})}\right)$
* **Inflection Points:** $\left(2 - \sqrt{6}, \, (6 - 4\sqrt{6})e^{\sqrt{6}-2}\right)$ and $\left(2 + \sqrt{6}, \, (6 + 4\sqrt{6})e^{-(2+\sqrt{6})}\right)$
