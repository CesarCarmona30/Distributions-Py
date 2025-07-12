# Bernoulli Distribution

**Bernoulli distribution** has exactly two possible outcomes-mutually exclusive-and is usually labeled "success" and "failure".

## Theory

$$x \sim \mathrm{Bernoulli}(p)\quad\text{or}\quad\mathrm{Bern}(x; p)$$

- **Parameter**
– `p` : probability of success, with 0 ≤ p ≤ 1 (we usually write q = 1 – p for the failure probability)

### Probability Mass Function (PMF)

$$P(X = x) = 
    \begin{cases}
      p^x(1-p)^{1-x}, & \quad x = 0,1\\
      0, & \quad otherwise
    \end{cases}
$$

### Mean and Variance

- Mean: $E[X] = \mu = p$
- Variance: $Var(x) = \sigma = p(1-p)$

** Standard deviation: $\(\sqrt{p(1-p)}\)$.
