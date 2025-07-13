# Geometric Distribution

The Geometric Distribution models the number of trials needed to get the first success in a sequence of independet Bernoulli(p) trials.

## Theory

$$X \sim \mathrm{Geom}(p)$$

- **Parameter**  
  – `p`: success probability, 0 < p ≤ 1
  - `x`: Trials to first success, 1, 2, 3, ...

### Probability Mass Function (PMF)

$$P(X = x) = pq^{x-1}$$


### Cumulative Distribution Funtion (CDF)

$$P(X \le x) = \sum_{i = 0}{x} pq^{i-1}$$

### Mean and Variance

- Mean: $E[X] = \frac{1}{p}$
- Variance: $Var(x) = \frac{1 - p}{p^2}$
- **Standard Deviation: $\sqrt{\mathrm{Var}(X)}$
