# Gamma Distribution

The **Gamma distribution** generalizes the Exponential by modeling the time until the k-th event in a Poisson process with rate λ. It is used when waiting times accumulate.

Use the Gamma distribution for sums of k independent Exponential(λ) random variables (e.g., time until k arrivals).

## Theory

$$X \sim \Gamma(k, \theta)\quad\text{or}\quad f(x; k, \theta)$$

- **Parameters**

  - `k > 0`: shape parameter (real)
  - `θ > 0`: scale parameter (real)

- **Support**
  - `x ≥ 0`

### Probability Density Function (PDF)

$$
 f(x; k, \theta) =
 \begin{cases}
   \frac{1}{\Gamma(k)\,\theta^k} \, x^{k-1} \, e^{-x/\theta}, & x \ge 0, \\
   0, & \text{otherwise}
 \end{cases}
$$

where \(\Gamma(k)=\int_0^\infty t^{k-1}e^{-t}dt\).

### Cumulative Distribution Function (CDF)

$$
 F(x; k, \theta) = \frac{1}{\Gamma(k)}\,\gamma\bigl(k, x/\theta\bigr),
$$

where \(\gamma(s,z)=\int_0^z t^{s-1}e^{-t}dt\).

### Mean and Variance

- **Mean:** \(E[X] = k\,\theta\)
- **Variance:** \(\mathrm{Var}(X) = k\,\theta^2\)
- **Standard Deviation:** \(\sigma = \sqrt{k}\,\theta\)
