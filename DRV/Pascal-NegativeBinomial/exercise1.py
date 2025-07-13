"""
A pediatrician wants to recruit five couples—each 
expecting their first child—to take part in a new 
natural childbirth program. Let pp be the probability 
that a randomly selected couple agrees to participate; 
here p=0.2 (i.e. one out of five couples is willing). 
Let X be the number of failures (couples who decline) 
before the 5th success (couple who agrees).
"""

import negative_bin as nbin

p = 0.2
k = 5

xs = [_ for _ in range(1, 31)]
ps = [nbin.pmf(x, k, p) for x in xs]
cum = [nbin.cdf(x, k, p) for x in xs]

print("Probability Mass Function PMF")
for x, px in zip(xs, ps):
  print(f"P(X = {x}) = {px:.3f}")

print()

print("Cumulative Distribution Function CDF")
for x, cx in zip(xs, cum):
  print(f"P(X <= {x}) = {cx:.3f}")

print()
print(f"Mean(x) = {nbin.mean(k, p)}")
print(f"Var(x) = {nbin.var(k, p)}")

nbin.pmf_plot(xs, ps, k, p, f"X = The number of couples who decline before the {k}th couple who agrees")
nbin.cdf_plot(xs, cum, k, p)
