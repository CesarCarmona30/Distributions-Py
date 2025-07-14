# Gaussian (Normal) Distribution

The **Normal distribution** describes real-valued data that tend to cluster around a central mean. It arises naturally in the Central Limit Theorem for sums of independent, identically distributed variables.

Use the Normal distribution to model measurement errors, test scores, or any phenomena where many small independent factors combine.

## Theory

$$X \sim N(\mu, \sigma)\quad\text{or}\quad f(x; \mu, \sigma)$$

- **Parameters**

  - `μ ∈ ℝ`: mean (real)
  - `σ > 0`: standard deviation (real)

- **Support**
  - `x` $∈ (-\infty,\infty)$

### Probability Density Function (PDF)

$$
 f(x; \mu, \sigma) =
 \frac{1}{\sqrt{2\pi\sigma}}e^{\Bigl(-\frac{(x - \mu)^2}{2\sigma^2}\Bigr)}.
$$

### Cumulative Distribution Function (CDF)

$$
 P(a \le X \le b) = F(x; \mu, \sigma) =
 \frac{1}{\sqrt{2\pi\sigma}} \int_{a}{b} e^{\Bigl(-\frac{(x - \mu)^2}{2\sigma^2}\Bigr)}.
$$

### Mean and Variance

- **Mean:** $\(E[X] = \mu\)$
- **Variance:** $\(\mathrm{Var}(X) = \sigma^2\)$
- **Standard Deviation:** $\sigma$

> **Special case:** Standard Normal when \(μ=0, σ=1\).
