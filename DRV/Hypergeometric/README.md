# Poisson Distribution


## Theory


### Probability Mass Function (PMF)

$$P(X = x) =
    \begin{cases}
     \frac{\binom{M}{x} \binom{N-M}{n-x}}{\binom{N}{n}}, & \quad x = 0, 1, 2, \dots min(M > 0, n)\\
     0, & \quad otherwise
    \end{cases}
$$


### Cumulative Distribution Function (CDF)

$$P(X \leq x) = \sum_{i=0}^{x} \frac{\binom{M}{i} \binom{N-M}{n-i}}{\binom{N}{n}}$$


### Mean and Variance

- Mean: $E[X] = \frac{nM}{N} $ 
- Variance: $Var(x) = n\frac{M}{N}(1-\frac{M}{N})(\frac{N-n}{N-1})$
