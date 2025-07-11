# Binomial Distribution

The **Binomial distribution** models the number of successes in a fixed number of independent Bernoulli trials, each with the same probability of success.

Many experiments fit exactly or approximately the following set of requirements:

1. The experiment consists of a sequence of **n** smaller experiments, called **trials**, where **n** is fixed in advance.

2. Each trial results in one of the same two possible outcomes (**dichotomous trials**), which are labeled as **success (S)** and **failure (F)**.

3. The trials are **independent**, meaning that the outcome of any particular trial does not affect the outcome of any other trial.

4. The **probability of success**, denoted by **p**, remains constant from trial to trial.

A **binomial experiment** is made up of several **Bernoulli trials**.

## Theory

$$x~Bin(n, p) - Bin(x; n, p)$$

- **Parameters**  
  - `n` — number of trials (integer, n ≥ 0)  
  - `p` — probability of success on each trial (0 ≤ p ≤ 1)

- **Support**  
  k = 0, 1, 2, …, n

### Probability Mass Function (PMF)

$$P(X = k) = \binom{n}{k} p^k (1 − p)^{n − k}$$

where 
$$\binom{n}{k}$$ 
is the binomial coefficient 
$$\frac{n!}{k! (n − k)!}$$.

### Cumulative Distribution Function (CDF)

$$F(k) = P(X ≤ k) = \sum_{i=0}^{k} \binom{n}{i} p^i (1 − p)^{n − i}$$

### Mean and Variance

- Mean: $E[X] = n * p$  
- Variance: $Var(X) = n * p * (1 − p)$
