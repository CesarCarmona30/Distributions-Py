# Geometric Distribution

The Geometric Distribution models the number of trials needed to get the first success in a sequence of independet Bernoulli(p) trials.

## Theory

$$X \sim \mathrm{Geom}(p)$$

**Parameter**  
– `p`: success probability, 0 < p ≤ 1  


### Probability Mass Function (PMF)

$$P(X = x) = pq^{x-1}$$


### Cumulative Distribution Funtion (CDF)

$$P(X \le x) = 1 - q^x$$

### Mean and Variance

- Mean: $E[X] = \frac{1}{p}$
- Variance: $Var(x) = \frac{1 - p}{p^2}$

