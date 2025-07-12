# Hypergeometric Distribution

The assumptions that lead to the hypergeometric distribution are the following:

1. The population or set to be sampled consists of N individuals, objects, or elements (a finite population).

2. Each individual can be classified as a success (S) or a failure (F), and there are M successes in the population.

3. A sample of n individuals is selected without replacement, in such a way that each subset of size n is equally likely to be chosen.

The random variable of interest is X, the number of successes in the sample.
The probability distribution of X depends on the parameters n, M, and N, so we aim to find the probability P(X = x), denoted as shown in the next section.

## Theory

$$X \sim \mathrm{Hypergeometric}(N, M, n)\quad\text{or}\quad h(x; N,M,n)$$

- **Parameters**  
  - `x` — Number of observed success in the sample
  - `n` — Number of draws (sample size)
  - `M` — Number of successes in the population
  - `N` — Population size

### Probability Mass Function (PMF)

$$P(X = x) =
    \begin{cases}
     \frac{\binom{M}{x} \binom{N-M}{n-x}}{\binom{N}{n}}, & \quad x = \max(0,\,n+M-N),\,\dots,\,\min(M,\,n)\\
     0, & \quad otherwise
    \end{cases}
$$


### Cumulative Distribution Function (CDF)

$$P(X \leq x) = \sum_{i=0}^{x} \frac{\binom{M}{i} \binom{N-M}{n-i}}{\binom{N}{n}}$$


### Mean and Variance

- Mean: $E[X] = \frac{nM}{N} $ 
- Variance: $Var(x) = n\frac{M}{N}(1-\frac{M}{N})(\frac{N-n}{N-1})$
