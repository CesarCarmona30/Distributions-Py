# Uniform Distribution

The **Continuous Uniform distribution** models outcomes that are equally likely across a fixed interval [A, B]. It is often used when there is no reason to favor any sub‑interval over another within the range.

Use the Uniform distribution when you need a simple model for a continuous variable that could fall anywhere between A and B with equal probability.

## Theory

$$X \sim \mathrm{U}(A, B)\quad\text{or}\quad f(x; A, B)$$

- **Parameters**

  - `A`: lower bound of the interval (real, A < B)
  - `B`: upper bound of the interval (real, B > A)

- **Support**
  - `x ∈ [A, B]`

### Probability Density Function (PDF)

$$
 f(x; A, B) =
    \begin{cases}
      \frac{1}{B - A}, & A \le x \le B \\
      0, & \text{otherwise}
    \end{cases}
$$

### Cumulative Distribution Function (CDF)

$$
 F(x; A, B) = P(X \le x) =
    \begin{cases}
      0, & x < A \\
      \frac{x - A}{B - A}, & A \le x \le B \\
      1, & x > B
    \end{cases}
$$

### Mean and Variance

- **Mean:** $(E[X] = \frac{A + B}{2}$
- **Variance:** $\mathrm{Var}(X) = \frac{(B - A)^2}{12}$
- **Standard Deviation:** $\sigma = \sqrt{\frac{(B - A)^2}{12}}$
