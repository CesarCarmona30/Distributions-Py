# Poisson Distribution


## Theory


### Probability Mass Function (PMF)

$$p(x; k) =
    \begin{cases}
     \frac{e^{-\lambda} \lambda^x}{x!}, & \quad x = 0, 1, 2, \dots; \lambda > 0\\
     0, & \quad otherwise
    \end{cases}
$$


### Cumulative Distribution Function (CDF)

$$P(X \leq x) = F(x; \lambda) = \sum_{i=0}^{x} \frac{e^{\lambda} \lambda^i}{i!}$$


### Mean and Variance

- Mean: $E[X] = \lambda$
- Variance: $Var(x) = \lambda$
