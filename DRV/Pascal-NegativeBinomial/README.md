# Binomial Negative (Pascal) Distrbution

The **Negative Binomial distribution** (also known as the Pascal distribution when the number of successes is integer) models the number of failures before the $k$-th success in a sequence of independent Bernoulli(p) trials.

1. The experiment is a sequence of independent trials.  
2. Each trial yields a success (S) or a failure (F).  
3. The probability of success \(p\) is the same for every trial.  
4. Trials continue until exactly \(r\) successes have occurred, where \(r\) is a fixed positive integer.


## Theory

$$X \sim \mathrm{NB}(k, p)\quad\text{or}\quad \mathrm{NBin}(x; k, p)$$

- **Parameters**
 - `x`: number of failures before the $k^{\text{th}}$ success
 - `k`: number of success (integer, n ≥ 0)
 - `p`: probability of success on each trial (0 ≤ p ≤ 1)

### Probability Mass Function

$$P(X = x) = \binom{k + x - 1}{k - 1} p^k (1 - p)^x$$

### Cumulative Distribution Function

$$F(k) = P(X \le x) = \sum_{i=0}^{x} \binom{k + i - 1}{k - 1} p^k (1 - p)^i$$

### Mean and Variance

- Mean: $E[X] = \frac{k\(1-p\)}{p}$
- Variance: $Var(X) = \frac{k\(1-p\)}{p^2}$
- **Standard Deviation: $\sqrt{\mathrm{Var}(X)}$
