# exercise_uniform.py

"""
Exercise: Explore the continuous Uniform(a, b) distribution
using your uniform.py module.

Tasks:
1. Choose a = 1.5, b = 4.5.
2. Print out:
     • PDF at x = a, x = (a+b)/2, and x = b.
     • CDF at the same three points.
     • Theoretical mean and variance.
3. Plot the PDF and CDF (via the built‑in pdf_plot & cdf_plot).
4. Draw 10,000 samples, then:
     • Plot a histogram of your samples (normalized).
     • Compute and print the sample mean & variance.
     • Compare them to the theoretical values.
5. Compute the probability that X lies in [2.0, 3.5] both by
   integrating your PDF and by using the CDF difference.
"""

import numpy as np
import matplotlib.pyplot as plt

# 1. Import your uniform module
import uniform

# 2. Set parameters
a, b = 1.5, 4.5
test_points = [a, (a + b)/2, b]

# 3. Print PDF and CDF at key points
print("PDF values:")
for x in test_points:
    print(f"  pdf({x:.1f}) =", uniform.pdf(x, a, b))

print("\nCDF values:")
for x in test_points:
    print(f"  cdf({x:.1f}) =", uniform.cdf(x, a, b))

# 4. Theoretical moments
theo_mean = uniform.mean(a, b)
theo_var  = uniform.var(a, b)
print(f"\nTheoretical mean = {theo_mean:.3f}")
print(f"Theoretical variance = {theo_var:.3f}")

# 5. Plot PDF & CDF
uniform.pdf_plot(a, b)
uniform.cdf_plot(a, b)

# 6. Sampling
N = 10_000
samples = uniform.sample(a, b, size=N)

# 7. Histogram of samples
plt.figure()
plt.hist(samples, bins=30, density=True, alpha=0.7)
plt.title(f"Histogram of {N} draws from U({a}, {b})")
plt.xlabel("x")
plt.ylabel("Density")
plt.grid(True)
plt.show()

# 8. Sample moments
sample_mean = np.mean(samples)
sample_var  = np.var(samples, ddof=0)
print(f"\nSample mean = {sample_mean:.3f}")
print(f"Sample variance = {sample_var:.3f}")

# 9. Probability P(2.0 ≤ X ≤ 3.5)
p_interval_pdf = (3.5 - 2.0) / (b - a)
p_interval_cdf = uniform.cdf(3.5, a, b) - uniform.cdf(2.0, a, b)
print(f"\nP(2.0 ≤ X ≤ 3.5) via PDF integration = {p_interval_pdf:.3f}")
print(f"P(2.0 ≤ X ≤ 3.5) via CDF difference  = {p_interval_cdf:.3f}")

