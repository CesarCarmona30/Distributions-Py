# Exponential Distribution

The **Exponential distribution** describes the time between independent events that occur continuously and at a constant average rate. It is memoryless: the probability of an event occurring in the future does not depend on how much time has already elapsed.

Use the Exponential distribution to model waiting times in Poisson processes (e.g., time between customer arrivals at a service desk).

## Theory

$$X \sim \mathrm{Exp}(\lambda)\quad\text{or}\quad f(x; \lambda)$$

- **Parameter**

  - `λ > 0`: rate parameter (events per unit time)

- **Support**
  - `x ≥ 0`

### Probability Density Function (PDF)

$$
 f(x; \lambda) =
 \begin{cases}
   \lambda e^{-\lambda x}, & x \ge 0, \\
   0, & \text{otherwise}
 \end{cases}
$$

### Cumulative Distribution Function (CDF)

$$
 F(x; \lambda) =
 \begin{cases}
   1 - e^{-\lambda x}, & x \ge 0, \\
   0, & x < 0
 \end{cases}
$$

### Mean and Variance

- **Mean:** $E[X] = \lambda$
- **Variance:** $\mathrm{Var}(X) = \lambda^2$
- **\*Standard Deviation:** $\sigma = \lambda$
