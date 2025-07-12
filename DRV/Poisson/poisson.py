# poisson.py

import math
import matplotlib.pyplot as plt

def factorial(n: int) -> int:
  return 1 if n == 0 or n == 1 else n * factorial(n - 1)

def pmf(x: int, lamb: float) -> float:
  return (math.e ** -lamb * lamb ** x) / factorial(x)

def cdf(x: int, lamb: float) -> float:
  return sum(pmf(i, lamb) for i in range(x + 1))

# mean(x) = variance(x) => lambda: value

def std(lamb: float) -> float:
    return math.sqrt(lamb)

def pmf_plot(xs: list[int], ps: list[float], lamb: float, x_label: str):
  plt.figure()
  plt.bar(xs, ps)
  plt.title(f"Poisson PMF (lambda = {lamb})")
  plt.xlabel(x_label)
  plt.ylabel("Probability: f(x) = P(X = x)")
  plt.show()

def cdf_plot(xs: list[int], cum_prob: list[float], lamb: float):
  plt.figure()
  plt.step(xs, cum_prob, where="post")
  plt.title(f"Poisson CDF (lambda = {lamb})")
  plt.xlabel("X = x")
  plt.ylabel("F(x) = P(X <= x)")
  plt.show()
