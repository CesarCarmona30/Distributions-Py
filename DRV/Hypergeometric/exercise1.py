"""A certain type of digital camera comes in a 
3-megapixel version and a 4-megapixel version. 
A camera store receives a shipment of 15 of these 
cameras, of which 6 have a resolution of 3 megapixels.
Suppose 5 of these cameras are randomly selected 
to be kept behind the counter; 
the remaining 10 are placed in storage.
Let X be the number of 3-megapixel cameras 
among the 5 selected to be kept behind the counter."""

import hypergeometric as hpg
import math
# 3 mpx -> E, 4mpx -> F
# N: 15, M: 6, N - M: 9
# n: 5

n, M, N = 5, 6, 15
xs = [_ for _ in range(N + 1)]

px = [hpg.pmf(x, n, M, N) for x in xs]
cum = [hpg.cdf(x, n, M, N) for x in xs]

print("Probability Mass Function:")
for x, p in zip(xs, px):
  print(f"P(X = {x}) = {p:.3f}")

print()
print("Cumulative Distribution Function:")
for x, cx in zip(xs, cum):
  print(f"P(X <= {x}) = {cx:.3f}")

print()

print(f"Mean(x) = {hpg.mean(n, M, N)}")
print(f"Var(x) = {hpg.var(n, M, N)}")

hpg.pmf_plot(xs, px, n, M, N, 
             f"X = number of 3mpx cameras, n = Quantity of 3Mpx in a M={M} population")

hpg.cdf_plot(xs, cum, n, M, N)

