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
* **Function:** $f(x) = (x^2 - 4)e^{-x}$
* **First Derivative:**
    * $f'(x) = 2xe^{-x} + (x^2 - 4)(-e^{-x}) = -e^{-x}(x^2 - 2x - 4)$
    * $f''(x) = e^{-x}(x^2 - 2x - 4) - e^{-x}(2x - 2) = e^{-x}(x^2 - 4x + 2)$
