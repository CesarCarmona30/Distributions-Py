# Gamma Distribution

The **Gamma distribution** generalizes the Exponential by modeling the time until the k-th event in a Poisson process with rate λ. It is used when waiting times accumulate.

Use the Gamma distribution for sums of k independent Exponential(λ) random variables (e.g., time until k arrivals).

## Theory

$$X \sim \Gamma(\alpha, \beta)\quad\text{or}\quad f(x; \alpha, \beta)$$

- **Parameters**

  - $\alpha$ > 0: shape parameter (real)
  - $\beta$ > 0: scale parameter (real)

- **Support**
  - `x ≥ 0`

### Probability Density Function (PDF)

$$
 f(x; \alpha, \beta) =
 \begin{cases}
   \frac{1}{\beta^{\alpha} \Gamma(\alpha)} x^{\alpha - 1} e^{\frac{-x}{\beta}}, & x \ge 0, \\
   0, & \text{otherwise}
 \end{cases}
$$

where $\Gamma(\alpha)=\int_{0}^{\infty} x^{\alpha - 1} e^{-x}dx$.

### Cumulative Distribution Function (CDF)

$$
 F(x; \alpha, \beta) = \frac{1}{\Gamma(\alpha)}\,\gamma\bigl(\alpha, x \beta\bigr),
$$

where $\gamma(s,z)=\int_{0}^{z} x^{s - 1} e^{-x}dx$

### Mean and Variance

- **Mean:** $E[X] = \alpha \beta$
- **Variance:** $\mathrm{Var}(X) = \sigma^2 = \alpha \beta^2$
- **Standard Deviation:** $\sigma = \sqrt{\alpha \beta^2}$
