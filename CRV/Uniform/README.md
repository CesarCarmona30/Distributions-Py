# Uniform Distribution

## Theory

$$x \sim \mathrm{U}(A, B)\quad\text{or}\quad\mathrm{U}(x; A, B)$$

- **Parameters**
  – `A`:

  - `B`:

- **Support**
  - `x = 0` (failure) or `x = 1` (success)

### Probability Mass Function PMF

$$
f(x; A, B) =
    \begin{cases}
      \frac{1}{B-A}, & \quad A \le x \le B\\
      0, & \quad otherwise
    \end{cases}
$$

### Cumulative Distribution Function CDF

$$
P(X \le x) = F(x; a, b) = (b - a)^{-1} \int_{a}^{x} dx =
    \begin{cases}
      0, & \quad x < a.\\
      \frac{x - a}{b - a}, & \quad a \le x \le b\\
      1, & \quad x > b
    \end{cases}
$$

### Mean and Variance

- Mean: $E[X] = \mu = \frac{A + B}{2}$
- Variance: $Var(x) = \sigma^2 = \frac{(B - A)^2}{12}$

\*\* Standard deviation: $\sigma = \sqrt{Var(x)}$.
