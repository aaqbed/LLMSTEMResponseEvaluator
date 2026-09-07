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
    * $f'(x) = \frac{d}{dx}[x^2 - 4]e^{-x} + (x^2 - 4)\frac{d}{dx}[e^{-x}] = 2xe^{-x} - (x^2 - 4)e^{-x} = (-x^2 + 2x + 4)e^{-x}$
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
* **First Derivative:** $f'(x) = (-x^2 + 2x + 4)e^{-x}$
* **Second Derivative:** $f''(x) = (x^2 - 4x - 2)e^{-x}$
* **Local Minimum:** $\left(1 - \sqrt{5}, (2 - 2\sqrt{5})e^{\sqrt{5}-1}\right)$
* **Local Maximum:** $\left(1 + \sqrt{5}, (2 + 2\sqrt{5})e^{-(1+\sqrt{5})}\right)$
* **Inflection Points:** $\left(2 - \sqrt{6}, (6 - 4\sqrt{6})e^{\sqrt{6}-2}\right)$ and $\left(2 + \sqrt{6}, (6 + 4\sqrt{6})e^{-(2+\sqrt{6})}\right)$

---

### P09 (Calculus II - Integration by Parts)

### Problem Statement
Evaluate the indefinite integral using integration by parts:
$$\int x^2 \ln(x) dx$$.
Show the selection of $u$, $dv$, $du$, $v$, and all algebraic simplification steps.

* **Choose $u$ and $dv$ :**
    * $u = \ln(x) \implies du = \frac{1}{x} dx$
    * $dv = x^2 dx \implies v = \int x^2 dx = \frac{x^3}{3}$
* **Apply the Integration by Parts formula ($\int u dv = uv - \int v du$):**
    $$\int x^2 \ln(x) dx = \ln(x) \cdot \frac{x^3}{3} - \int \frac{x^3}{3} \cdot \frac{1}{x} dx$$
* **Simplify and evaluate the remaining integral:**
    $$\int x^2 \ln(x) dx = \frac{x^3 \ln(x)}{3} - \frac{1}{3} \int x^2 dx = \frac{x^3 \ln(x)}{3} - \frac{1}{3} \left(\frac{x^3}{3}\right) + C$$
    $$= \frac{x^3 \ln(x)}{3} - \frac{x^3}{9} + C$$

### Final Answer
$$\frac{x^3 \ln(x)}{3} - \frac{x^3}{9} + C$$

---

### P10 (Calculus III - Constrained Optimization via Lagrange Multipliers)

### Problem Statement
Use the method of Lagrange multipliers to find the maximum and minimum values of $f(x, y, z) = 2x + 4y + z$ subject to the constraint $g(x, y, z) = x^2 + 2y^2 + z^2 = 28$. Show the gradient setup, system of equations, and check all critical points.

### Solution Derivation
* **Gradient Setup ($\nabla f = \lambda \nabla g$):**
   * $\nabla f = \langle 2, 4, 1 \rangle$
   * $\nabla g = \langle 2x, 4y, 2z \rangle$
* **System of Equations:**
   $$2 = \lambda(2x) \implies x = \frac{1}{\lambda}$$,
   $$4 = \lambda(4y) \implies y = \frac{1}{\lambda}$$,
   $$1 = \lambda(2z) \implies z = \frac{1}{2\lambda}$$
* **Substitute into Constraint Equation:**
   $$\left(\frac{1}{\lambda}\right)^2 + 2\left(\frac{1}{\lambda}\right)^2 + \left(\frac{1}{2\lambda}\right)^2 = 28$$
   $$\frac{1}{\lambda^2} + \frac{2}{\lambda^2} + \frac{1}{4\lambda^2} = 28 \implies \frac{13}{4\lambda^2} = 28 \implies \lambda^2 = \frac{13}{112} \implies \lambda = \pm \frac{\sqrt{91}}{28}$$
* **Find Critical Points:**
   * **For $\lambda = \frac{\sqrt{91}}{28}$:**
     $$x = \frac{4\sqrt{91}}{13}, \quad y = \frac{4\sqrt{91}}{13}, \quad z = \frac{2\sqrt{91}}{13}$$
     $$f_{\max} = 2\left(\frac{4\sqrt{91}}{13}\right) + 4\left(\frac{4\sqrt{91}}{13}\right) + 1\left(\frac{2\sqrt{91}}{13}\right) = 2\sqrt{91}$$
   * **For $\lambda = -\frac{\sqrt{91}}{28}$:**
     $$x = -\frac{4\sqrt{91}}{13}, \quad y = -\frac{4\sqrt{91}}{13}, \quad z = -\frac{2\sqrt{91}}{13}$$
     $$f_{\min} = -2\sqrt{91}$$

### Final Answer
* **Maximum Value:** $2\sqrt{91} \approx 19.08$ at $\left(\frac{4\sqrt{91}}{13}, \, \frac{4\sqrt{91}}{13}, \, \frac{2\sqrt{91}}{13}\right)$
* **Minimum Value:** $-2\sqrt{91} \approx -19.08$ at $\left(-\frac{4\sqrt{91}}{13}, \, -\frac{4\sqrt{91}}{13}, \, -\frac{2\sqrt{91}}{13}\right)$

---



## Science Reference Solutions

### P11 (High School Biology - Dihybrid Cross Probability)

### Problem Statement
In pea plants, round seeds ($R$) are dominant over wrinkled seeds ($r$), and yellow seeds ($Y$) are dominant over green seeds ($y$). Two plants heterozygous for both traits ($RrYy$) are crossed. Assuming independent assortment, state the expected phenotypic ratio of the offspring and calculate the exact probability of obtaining an offspring that has round green seeds.

* **Phenotypic Ratio (Dihybrid Cross RrYy x RrYy):**
   * Cross 1 (Rr x Rr): $P(\text{Round}) = \frac{3}{4}$, $P(\text{Wrinkled}) = \frac{1}{4}$
   * Cross 2 (Yy x Yy): $P(\text{Yellow}) = \frac{3}{4}$, $P(\text{Green}) = \frac{1}{4}$
   * Combined phenotypic ratio:
     * Round Yellow (R_ Y_): $\frac{3}{4} \times \frac{3}{4} = \frac{9}{16}$
     * Round Green (R_ yy): $\frac{3}{4} \times \frac{1}{4} = \frac{3}{16}$
     * Wrinkled Yellow (rr Y_): $\frac{1}{4} \times \frac{3}{4} = \frac{3}{16}$
     * Wrinkled Green (rr yy): $\frac{1}{4} \times \frac{1}{4} = \frac{1}{16}$
   * Expected phenotypic ratio: **9:3:3:1**
* **Probability of Round Green Offspring:**
   $$P(\text{Round Green}) = P(\text{Round}) \times P(\text{Green}) = \frac{3}{4} \times \frac{1}{4} = \frac{3}{16} = 0.1875$$
   This corresponds to **18.75%**.

### Final Answer
* **Expected Phenotypic Ratio:** 9:3:3:1 (Round Yellow : Round Green : Wrinkled Yellow : Wrinkled Green)
* **Exact Probability of Round Green:** $\frac{3}{16}$ (or 0.1875 / 18.75%)