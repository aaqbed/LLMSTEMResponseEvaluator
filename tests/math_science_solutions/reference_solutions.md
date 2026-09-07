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
   $$P(\text{Round Green}) = P(\text{Round}) \times P(\text{Green}) = \frac{3}{4} \times \frac{1}{4} = \frac{3}{16} = 0.1875$$.
   This corresponds to **18.75%**.

### Final Answer
* **Expected Phenotypic Ratio:** 9:3:3:1 (Round Yellow : Round Green : Wrinkled Yellow : Wrinkled Green)
* **Exact Probability of Round Green:** $\frac{3}{16}$ (or 0.1875, 18.75%)

---

### P12 (High School Chemistry - Stoichiometry & Ideal Gas Law)

### Problem Statement
Consider the complete combustion of propane:
$$\text{C}_3\text{H}_8(g) + 5\text{O}_2(g) \rightarrow 3\text{CO}_2(g) + 4\text{H}_2\text{O}(g)$$.
If $44.1\text{ g}$ of propane reacts with $128.0\text{ g}$ of oxygen gas at $1.00\text{ atm}$ and $298\text{ K}$, identify the limiting reactant, calculate the theoretical yield of $\text{CO}_2$ in grams, and determine the volume of $\text{CO}_2$ produced in liters using $R = 0.08206\text{ L}\cdot\text{atm}/(\text{mol}\cdot\text{K})$.

* **Molar Masses:**
    * $M(\text{C}_3\text{H}_8) = 3(12.011\text{ g/mol}) + 8(1.008\text{ g/mol}) = 36.033\text{ g/mol} + 8.064\text{ g/mol} = 44.097\text{ g/mol} \approx 44.1\text{ g/mol}$
   * $M(\text{O}_2) = 2(16.00\text{ g/mol}) = 32.00\text{ g/mol}$
   * $M(\text{CO}_2) = 1(12.011\text{ g/mol}) + 2(16.00\text{ g/mol}) = 12.011\text{ g/mol} + 32.00\text{ g/mol} = 44.011\text{ g/mol} \approx 44.01\text{ g/mol}$
* **Initial Moles:**
    * $n(\text{C}_3\text{H}_8) = \frac{44.1\text\{ g}}{44.097\text{ g/mol}} = 1.000\text{ mol}$
    * $n(\text{O}_2) = \frac{128.0\text{ g}}{32.00\text{ g/mol}} = 4.000\text{ mol}$
* **Limiting Reactant Identification:**
    * Stoichiometric ratio requires $5\text{ mol }\text{O}_2$ per $1\text{ mol }\text{C}_3\text{H}_8$.
    * For $1.000\text{ mol }\text{C}_3\text{H}_8$, $5.000\text{ mol }\text{O}_2$ is needed, but only $4.000\text{ mol }\text{O}_2$ is available.
    * Therefore, **$\text{O}_2$ is the limiting reactant**.
* **Theoretical Yield of $\text{CO}_2$:**
    * Moles of $\text{CO}_2$ formed:
        $$n(\text{CO}_2) = 4.000\text{ mol }\text{O}_2 \times \frac{3\text{ mol }\text{CO}_2}{5\text{ mol }\text{O}_2} = 2.400\text{ mol }\text{CO}_2$$
   * Mass of $\text{CO}_2$:
     $$\text{Mass} = 2.400\text{ mol} \times 44.01\text{ g/mol} = 105.624\text{ g} \approx 105.6\text{ g}$$
* **Volume of $\text{CO}_2$ via Ideal Gas Law ($PV = nRT$):**
    $$V = \frac{nRT}{P} = \frac{(2.400\text{ mol})(0.08206\text{ L}\cdot\text{atm}/(\text{mol}\cdot\text{K}))(298\text{ K})}{1.00\text{ atm}} = 58.69\text{ L} \approx 58.7\text{ L}$$

### Final Answer
* **Limiting Reactant:** $\text{O}_2$ (Oxygen gas)
* **Theoretical Yield of $\text{CO}_2$:** $105.6\text{ g}$
* **Volume of $\text{CO}_2$:** $58.7\text{ L}$

---

### P13 (AP Chemistry - Chemical Equilibrium & ICE Table)

### Problem Statement
At $500\text{ K}$, the reaction $\text{N}_2(g) + 3\text{H}_2(g) \rightleftharpoons 2\text{NH}_3(g)$ has an equilibrium constant $K_c = 0.060$. If a $2.0\text{ L}$ rigid vessel initially contains $0.40\text{ mol}$ of $\text{N}_2$, $0.60\text{ mol}$ of $\text{H}_2$, and $0.00\text{ mol}$ of $\text{NH}_3$, set up the ICE table, write the equilibrium expression, and state the equation needed to solve for the equilibrium concentrations.
* **Initial Concentrations ($C = \frac{n}{V}$, where $V = 2.0\text{ L}$):**
   * $[\text{N}_2]_0 = \frac{0.40\text{ mol}}{2.0\text{ L}} = 0.20\text{ M}$
   * $[\text{H}_2]_0 = \frac{0.60\text{ mol}}{2.0\text{ L}} = 0.30\text{ M}$
   * $[\text{NH}_3]_0 = \frac{0.00\text{ mol}}{2.0\text{ L}} = 0.00\text{ M}$

* **ICE Table Setup (Let $x$ be the extent of reaction in M):**

| Species | Initial (M) | Change (M) | Equilibrium (M) |
| :--- | :---: | :---: | :---: |
| **$\text{N}_2$** | $0.20$ | $-x$ | $0.20 - x$ |
| **$\text{H}_2$** | $0.30$ | $-3x$ | $0.30 - 3x$ |
| **$\text{NH}_3$** | $0.00$ | $+2x$ | $2x$ |

* **Equilibrium Constant Expression:**
   $$K_c = \frac{[\text{NH}_3]^2}{[\text{N}_2][\text{H}_2]^3}$$

* **Substituted Equation to Solve:**
   $$0.060 = \frac{(2x)^2}{(0.20 - x)(0.30 - 3x)^3}$$

### Final Answer
* **Initial Concentrations:** $[\text{N}_2]_0 = 0.20\text{ M}$, $[\text{H}_2]_0 = 0.30\text{ M}$, $[\text{NH}_3]_0 = 0.00\text{ M}$
* **Equilibrium Concentrations:** $[\text{N}_2] = 0.20 - x$, $[\text{H}_2] = 0.30 - 3x$, $[\text{NH}_3] = 2x$
* **Equilibrium Expression & Equation:**
  $$K_c = \frac{[\text{NH}_3]^2}{[\text{N}_2][\text{H}_2]^3} \implies 0.060 = \frac{(2x)^2}{(0.20 - x)(0.30 - 3x)^3}$$

  ---

  ### P14 (AP Physics C Mechanics - Rotational Mechanics & Energy Conservation)
  
  ### Problem Statement
  A uniform thin rod of mass $M = 3.0\text{ kg}$ and length $L = 2.0\text{ m}$ is free to pivot in a vertical plane about a frictionless hinge at one end ($I = \frac{1}{3}ML^2$). The rod is released from rest in a horizontal position. Using energy conservation, calculate the angular velocity $\omega$ of the rod when it reaches the vertical position, and calculate the linear velocity of the rod's lowest tip at that instant (use $g = 9.8\text{ m/s}^2$).

* **Center of Mass (CM) Height Drop:**
   * Center of mass of a uniform rod is at its midpoint: $h_{\text{cm}} = \frac{L}{2}$.
   * When released horizontally and rotating to vertical, the CM falls by $\Delta h = \frac{L}{2} = \frac{2.0}{2} = 1.0\text{ m}$.
* **Conservation of Energy ($E_{\text{initial}} = E_{\text{final}}$):**
   * Initial Energy (pure potential energy relative to vertical CM position):
     $$U_i = M g \left(\frac{L}{2}\right), \quad K_i = 0$$
   * Final Energy (pure rotational kinetic energy at lowest point):
     $$U_f = 0, \quad K_f = \frac{1}{2} I \omega^2$$
   * Equating energies:
     $$M g \left(\frac{L}{2}\right) = \frac{1}{2} \left(\frac{1}{3} M L^2\right) \omega^2 \implies M g L = \frac{1}{3} M L^2 \omega^2 \implies \omega^2 = \frac{3g}{L} \implies \omega = \sqrt{\frac{3g}{L}}$$
* **Calculate Angular Velocity ($\omega$):**
   $$\omega = \sqrt{\frac{3(9.8)}{2.0}} = \sqrt{14.7} \approx 3.834\text{ rad/s}$$
* **Calculate Linear Velocity of Lowest Tip ($v_{\text{tip}}$):**
   * Tip distance from pivot is $r = L = 2.0\text{ m}$.
   * $v_{\text{tip}} = \omega L = \sqrt{\frac{3g}{L}} \cdot L = \sqrt{3gL}$
   $$v_{\text{tip}} = \sqrt{3(9.8)(2.0)} = \sqrt{58.8} \approx 7.668\text{ m/s}$$

### Final Answer
* **Angular Velocity ($\omega$):** $\sqrt{\frac{3g}{L}} = \sqrt{14.7} \approx 3.83\text{ rad/s}$
* **Linear Velocity of Tip ($v$):** $\sqrt{3gL} = \sqrt{58.8} \approx 7.67\text{ m/s}$

---

### P15 (AP Physics C Integration - Rotational Inertia via Non-Uniform Integration)

### Problem Statement
A non-uniform thin rod of length $L$ lies along the $x$-axis with one end at the origin ($x = 0$) and the other end at $x = L$. Its linear mass density is given by $\rho(x) = kx^2$, where $k$ is a positive constant.
* (a) Find the total mass $M$ of the rod in terms of $k$ and $L$.
* (b) Using definite integration ($I = \int x^2 dm$), derive the rotational inertia $I$ of the rod about an axis perpendicular to the rod passing through the origin ($x = 0$) in terms of $M$ and $L$.

#### Part (a): Total Mass $M$
* Express differential mass element: $dm = \rho(x) \, dx = kx^2 \, dx$.
* Integrate across the length from $x = 0$ to $x = L$:
   $$M = \int_0^L dm = \int_0^L kx^2 \, dx = k \left[ \frac{x^3}{3} \right]_0^L = \frac{kL^3}{3}$$
* Express $k$ in terms of $M$ and $L$:
   $$k = \frac{3M}{L^3}$$

#### Part (b): Rotational Inertia $I$
* Set up the integral for rotational inertia about $x = 0$:
   $$I = \int x^2 dm = \int_0^L x^2 (\rho(x) \, dx) = \int_0^L x^2 (kx^2) \, dx = k \int_0^L x^4 \, dx$$
* Evaluate the definite integral:
   $$I = k \left[ \frac{x^5}{5} \right]_0^L = \frac{kL^5}{5}$$
* Substitute $k = \frac{3M}{L^3}$ to express $I$ in terms of $M$ and $L$:
   $$I = \left(\frac{3M}{L^3}\right) \frac{L^5}{5} = \frac{3}{5} M L^2$$

### Final Answer
* **(a) Total Mass:** $M = \frac{kL^3}{3}$
* **(b) Rotational Inertia:** $I = \frac{3}{5}ML^2$