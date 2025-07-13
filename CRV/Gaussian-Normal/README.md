# Gaussian (Normal) Distribution

The **Normal distribution** describes real-valued data that tend to cluster around a central mean. It arises naturally in the Central Limit Theorem for sums of independent, identically distributed variables.

Use the Normal distribution to model measurement errors, test scores, or any phenomena where many small independent factors combine.

## Theory

$$X \sim N(\mu, \sigma^2)\quad\text{or}\quad f(x; \mu, \sigma^2)$$

- **Parameters**

  - `μ ∈ ℝ`: mean (real)
  - `σ > 0`: standard deviation (real)

- **Support**
  - `$x ∈ (-\infty,\infty)$`

### Probability Density Function (PDF)

$$
 f(x; \mu, \sigma^2) =
 \frac{1}{\sqrt{2\pi\,\sigma^2}}^\Bigl(-\frac{(x - \mu)^2}{2\,\sigma^2}\Bigr).
$$

### Cumulative Distribution Function (CDF)

$$
 F(x; \mu, \sigma^2) = \frac{1}{2}\Bigl[1 + \mathrm{erf}\Bigl(\frac{x - \mu}{\sigma\sqrt{2}}\Bigr)\Bigr].
$$

### Mean and Variance

- **Mean:** \(E[X] = \mu\)
- **Variance:** \(\mathrm{Var}(X) = \sigma^2\)
- **Standard Deviation:** \(σ\)

> **Special case:** Standard Normal when \(μ=0, σ=1\).
