# Benchmark Ground-Truth Solutions (Math and Science)

---

## Mathematics Reference Solutions

### P06 (Algebra I - System of Equations) 
* **Given System:**
    1. $3x - 4y = 18$
    2. $5x + 2y = 4$
* **Step-by-Step Elimination:**
    * Multiply bottom equation by 2: $10x + 4y = 8$.
    * Add the resulting equation to equation 1:
        $$(3x - 4y) + (10x + 4y) = 18 + 8 \implies 13x = 26 \implies x = 2$$
    * Substitute $x = 2$ into equation 2:
        $$5(2) + 2y = 4 \implies 10 + 2y = 4 \implies 2y = -6 \implies y = -3$$
* **Final Answer:** $(x,y) = (2,-3)$

---

### P07 (Trigonometry - Identity Simplification)
* **Expression:** $\frac{\sin(x)}{1 + \cos(x)} + \frac{1 + \cos(x)}{\sin(x)}$
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
