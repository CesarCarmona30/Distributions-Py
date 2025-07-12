# hypergeometric.py

import matplotlib.pyplot as plt

def factorial(n: int) -> int:
  return 1 if n == 0 or n ==1 else n * factorial(n - 1)

def combinatory(n: int, r: int) -> int:
  return factorial(n) // (factorial(r) * factorial(n - r))

def pmf(x: int, n: int, M: int, N: int) -> float:
  if max(0, n - N + M) <= x <= min(n, M):
    return (combinatory(M, x) * combinatory(N - M, n - x)) / combinatory(N, n)
  return 0.0

def cdf(x: int, n:int, M: int, N: int) -> float:
  return sum(pmf(i, n, M, N) for i in range(x + 1))

def mean(n: int, M: int, N: int) -> float:
  return n * (M / N)

def var(n: int, M: int, N: int) -> float:
  return ((N - n) / (N - 1)) * n * (M / N) * (1 - (M / N))

def pmf_plot(xs: list[int], px: list[float], n: int, M: int, N: int, x_label: int):
  plt.figure()
  plt.bar(xs, px)
  plt.title(f"Hypergeometric PMF (n={n}, M={M}, N={N})")
  plt.xlabel(x_label)
  plt.ylabel("Probability: f(x) = P(X = x)")
  plt.show()

def cdf_plot(xs: list[int], cum_prob, n: int, M: int, N: int):
  plt.figure()
  plt.step(xs, cum_prob, where="post")
  plt.title(f"Hypergeometric CDF (n={n}, M={M}, N={N})")
  plt.xlabel("X = x")
  plt.ylabel("F(x) = P(X <= x")
  plt.show()
