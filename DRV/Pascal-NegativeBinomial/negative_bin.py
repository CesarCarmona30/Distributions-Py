# negative_bin.py

import matplotlib.pyplot as plt

def factorial(n: int) -> int:
    return 1 if n == 1 or n == 0 else n * factorial(n - 1)

def comb(n: int, r: int) -> int:
    return factorial(n) // (factorial(n - r) * factorial(r))

def pmf(x: int, k: int, p: float) -> float:
    return comb(k + x - 1, k - 1) * p**k * (1 - p)**x

def cdf(x: int, k: int, p: float) -> float:
    return sum(pmf(i, k, p) for i in range(1, x + 1))

def mean(k: int, p: float) -> float:
    return (k * (1 - p)) / p

def var(k: int, p: float) -> float:
    return (k * (1 - p)) / p ** 2

def pmf_plot(xs: list[int], ps: list[float], k: int, p: float, x_label: str):
    plt.figure()
    plt.bar(xs, ps)
    plt.title(f"Negative Bin. PMF (k={k}, p={p:.2f})")
    plt.xlabel(x_label)
    plt.ylabel("Probability: f(k) = P(X = k)")
    plt.show()

def cdf_plot(xs: list[int], cum_prob: list[float], k: int, p: float):
    plt.figure()
    plt.step(xs, cum_prob, where="post")
    plt.title(f"Negative Bin. CDF (k={k}, p={p:.2f})")
    plt.xlabel("X = k")
    plt.ylabel("F(k) = P(X <= k)")
    plt.show()
