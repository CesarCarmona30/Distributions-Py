# Weibull Distribution

The **Weibull distribution** models life data, reliability, and failure times, with a flexible hazard function that can increase or decrease over time.

Use the Weibull distribution for modeling lifetimes of products, materials, or systems.

## Theory

$$X \sim \mathrm{Weibull}(\alpha, \beta)\quad\text{or}\quad f(x; \alpha, \beta)$$

- **Parameters**

  - $\alpha$ > 0: shape parameter (real)
  - $\beta$ > 0: scale parameter (real)

- **Support**
  - `x ≥ 0`

### Probability Density Function (PDF)

$$
 f(x; \alpha, \beta) =
 \begin{cases}
   \frac{\alpha}{\beta^{\alpha}} x^{\alpha-1} e^{-(\frac{x}{\beta})^\alpha}, & x > 0, \alpha > 0, \beta > 0 \\
   0, & x \le 0
 \end{cases}
$$

### Cumulative Distribution Function (CDF)

$$
 F(x; \alpha, \beta) =
 \begin{cases}
   1 - e^{-(x/\beta)^\alpha}, & x \ge 0, \\
   0, & x < 0
 \end{cases}
$$

### Mean and Variance

- **Mean:** $E[X] = \beta\Gamma(1 + \frac{1}{\alpha})$
- **Variance:** $\mathrm{Var}(X) = \beta^2[\Gamma(1 + \frac{1}{\alpha}) - (\Gamma(1 + \frac{1}{\alpha}))^2]$
- **Standard Deviation:** $\sigma = \sqrt{\mathrm{Var}(X)}$
