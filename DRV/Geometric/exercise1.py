"""
In a certain manufacturing process, 
on average one out of every 100 items is defective. 
Let X be the number of items inspected until the first defective one appears."
"""
# p = 1 of 100 = 1/100 = 0.01

import geometric as geo


p = 0.01

xs = [_ for _ in range(1, 101)]
ps = [geo.pmf(x, p) for x in xs]
cum = [geo.cdf(x, p) for x in xs]

print("Probability Mass Function PMF")
for x, px in zip(xs, ps):
  print(f"P(X = {x}) = {px:.5f}")

print()
print("Cumulative Distribution Function CDF")
for x, cx, in zip(xs, cum):
  print(f"P(X <= {x}) = {cx:.5f}")

print()

print(f"Mean(x) = {geo.mean(p):.4f}")
print(f"Variance(x) = {geo.var(p):.4f}")

geo.pmf_plot(xs, ps, p, f"X = Number of items inspected until the first defective one appears")
geo.cdf_plot(xs, cum, p)
