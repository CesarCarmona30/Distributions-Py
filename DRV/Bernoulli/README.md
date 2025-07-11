# Bernoulli Distribution

**Bernoulli distribution** only have two possible results, mutually excludes as name sucess and failure

## Theory

$$x~Be(p) o Be(x; p)$$

- **Parameters**
  - `p` - success: 0 ≤ p ≤ 1 
  - `q` - failure: 1 - p


### Probability Mass Function (PMF)

$$P(X = x) = 
    \begin{cases}
      p^x(1-p)^{1-x}, & \quad x = 0,1\\
      0, & \quad otherwise
    \end{cases}
$$

### Mean and Variance

- Mean: $E[X] = \mu = p$
- Variancce: $Var(x) = \sigma = p(1-p)$
