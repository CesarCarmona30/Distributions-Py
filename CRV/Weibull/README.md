# Weibull Distribution

The **Weibull distribution** models life data, reliability, and failure times, with a flexible hazard function that can increase or decrease over time.

Use the Weibull distribution for modeling lifetimes of products, materials, or systems.

## Theory

$$X \sim \mathrm{Weibull}(k, \lambda)\quad\text{or}\quad f(x; k, \lambda)$$

- **Parameters**

  - `k > 0`: shape parameter (real)
  - `λ > 0`: scale parameter (real)

- **Support**
  - `x ≥ 0`

### Probability Density Function (PDF)

$$
 f(x; k, \lambda) =
 \begin{cases}
   \frac{k}{\lambda}(x/\lambda)^{k-1}e^{-(x/\lambda)^k}, & x \ge 0, \\
   0, & \text{otherwise}
 \end{cases}
$$

### Cumulative Distribution Function (CDF)

$$
 F(x; k, \lambda) =
 \begin{cases}
   1 - e^{-(x/\lambda)^k}, & x \ge 0, \\
   0, & x < 0
 \end{cases}
$$

### Mean and Variance

- **Mean:** \(E[X] = \lambda\,\Gamma(1 + 1/k)\)
- **Variance:** \(\mathrm{Var}(X) = \lambda^2[\Gamma(1 + 2/k) - (\Gamma(1 + 1/k))^2]\)
- **Standard Deviation:** \(σ = \sqrt{\mathrm{Var}(X)}\)
