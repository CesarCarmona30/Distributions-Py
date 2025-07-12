# binomial.py
import random
import matplotlib.pyplot as plt

def fact(n: int) -> int:
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n - 1)

def comb(n: int, r: int) -> int:
    return fact(n) // (fact(n - r) * fact(r))

def pmf(k: int, n: int, p: float) -> float:
    return comb(n, k) * p**k * (1 - p)**(n - k)

def cdf(k: int, n: int, p: float) -> float:
    return sum(pmf(i, n, p) for i in range(k + 1))

def sample(n: int, p: float, size: int = 1) -> list[int]:
    return [sum(random.random() < p for _ in range(n)) for _ in range(size)]

def mean(n: int, p: float) -> float:
    return n * p

def var(n: int, p: float) -> float:
    return n * p * (1 - p)

def pmf_plot(ks: list[int], pk: list[float], n: int, p: float, x_label: str):
    plt.figure()
    plt.bar(ks, pk)
    plt.title(f"Binomial PMF (n={n}, p={p:.2f})")
    plt.xlabel(x_label)
    plt.ylabel("Probability: f(k) = P(X = k)")
    plt.show()

def cdf_plot(ks: list[int], cum_prob: list[float], n: int, p: float):
    plt.figure()
    plt.step(ks, cum_prob, where="post")
    plt.title(f"Binomial CDF (n={n}, p={p:.2f})")
    plt.xlabel("X = k")
    plt.ylabel("F(k) = P(X <= k)")
    plt.show()
