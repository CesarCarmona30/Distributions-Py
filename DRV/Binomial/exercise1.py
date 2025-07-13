"""
When circuit boards are used in the manufacture
of compact disc players they are tested; 
the percentage of defective ones is 5%. 
If X is the number of defective cards 
in a random sample of size n = 25, 
then X~Bin(25, 0.05).
"""

import binomial as bin

n, p = 25, 0.05
xs = [_ for _ in range(n + 1)]
ps = [bin.pmf(x, n, p) for x in xs]
cum = [bin.cdf(x, n, p) for x in xs]

print(f"Probability Mass Function: ")
for x, px in zip(xs, ps):
  print(f"P(X = {x}) = {px:.3f}")

print()
print("Cumulative distribution function")
for x, cx in zip(xs, cum):
  print(f"P(X <= {x}) = {cx:.3f}")

bin.pmf_plot(xs, ps, n, p, "X = Number of defectives CD's")
bin.cdf_plot(xs, cum, n, p)