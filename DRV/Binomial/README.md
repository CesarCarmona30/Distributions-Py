# Binomial Distribution

The **Binomial distribution** models the number of successes in a fixed number of independent Bernoulli trials, each with the same probability of success.

## Theory

- **Parameters**  
  - `n` — number of trials (integer, n ≥ 0)  
  - `p` — probability of success on each trial (0 ≤ p ≤ 1)

- **Support**  
  k = 0, 1, 2, …, n

### Probability Mass Function (PMF)

P(X = k) = C(n, k) * p^k * (1 − p)^(n − k)

where `C(n, k)` is the binomial coefficient (`n! / (k! * (n − k)!`).

### Cumulative Distribution Function (CDF)

F(k) = P(X ≤ k) = sum_{i=0}^k [C(n, i) * p^i * (1 − p)^(n − i)]

### Mean and Variance

- Mean: E[X] = n * p  
- Variance: Var(X) = n * p * (1 − p)
