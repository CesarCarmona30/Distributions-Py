# Poisson Distribution

The **Poisson distribution** models the number of events occurring in a fixed interval of time or space, when events happen independently at a constant average rate.

## Theory

$$X \sim \mathrm{Poisson}(\lambda)$$  

- **Parameter**  

– `λ` : average rate (\(\lambda>0\))

### Probability Mass Function (PMF)

$$p(x; k) =
    \begin{cases}
     \frac{e^{-\lambda} \lambda^x}{x!}, & \quad x = 0, 1, 2, \dots; \lambda > 0\\
     0, & \quad otherwise
    \end{cases}
$$


### Cumulative Distribution Function (CDF)

$$P(X \leq x) = F(x; \lambda) = \sum_{i=0}^{x} \frac{e^{-\lambda} \lambda^i}{i!}$$


### Mean and Variance

- Mean: $E[X] = \lambda$
- Variance: $Var(x) = \lambda$
