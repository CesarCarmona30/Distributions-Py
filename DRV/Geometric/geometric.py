# geometric.py

import matplotlib.pyplot as plt

def pmf(x: int, p: float) -> float:
  return p * (1 - p) ** (x - 1)

def cdf(x: int, p: float) -> float:
  return sum(pmf(i, p) for i in range(1, x + 1))

def mean(p: float) -> float:
  return (1 / p)

def var(p: float) -> float:
  return ((1 - p) / p ** 2)

def pmf_plot(xs: list[int], px: list[float], p: float, x_label: str):
  plt.figure()
  plt.bar(xs, px)
  plt.title(f"Geometric PMF (p={p:.2f})")
  plt.xlabel(x_label)
  plt.ylabel("Probability: f(k) = P(X = k)")
  plt.show()

def cdf_plot(xs: list[int], cum_prob: list[float], p: float):
  plt.figure()
  plt.step(xs, cum_prob, where="post")
  plt.title(f"Geometric CDF (p={p:.2f})")
  plt.xlabel("X = x")
  plt.ylabel("F(k) = P(X <= k)")
  plt.show()
