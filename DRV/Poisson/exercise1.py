"""
Suppose a fast food establishment serves 50 customers
per hour following a Poisson distribution.
- What is the probability that fewer than 
eight customers have to be served between 5:00 p.m. and 5:15 p. m.
"""

# Mean(x) = 50, X~Poisson(lambda = 50) per hour
# Mean(x) = 50/4 = 12.5, X~Poisson(lambda = 12.5) per 15 min

import poisson as psn

lamb = 50 / 4

xs = [_ for _ in range(21)]
ps = [psn.pmf(x, lamb) for x in xs]
cumulative = [psn.cdf(x, lamb) for x in xs]

std_dev = psn.std(lamb)

print("Probability Mass Function:")
for x, p in zip(xs, ps):
  print(f"P(X = {x}) = {p:.5f}")

print()
print("Cumulative Distribution Function")
for x, cx in zip(xs, cumulative):
  print(f"P(X <= {x}) = {cx:.5f}")

print()
print(f"Mean(x) = Variance(x) = {lamb}")
print(f"Standard Deviation = {std_dev}")

psn.pmf_plot(xs, ps, lamb, "X = Number of customers in fifteen minutes")
psn.cdf_plot(xs, cumulative, lamb)
