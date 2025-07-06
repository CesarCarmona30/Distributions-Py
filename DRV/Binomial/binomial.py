import math
import random
import numpy as np
import matplotlib.pyplot as plt


def pmf(k: int, n: int, p: float) -> float:
    """Probability mass function for Binomial(n, p) at value k."""
    return math.comb(n, k) * p**k * (1 - p)**(n - k)


def cdf(k: int, n: int, p: float) -> float:
    """Cumulative distribution function for Binomial(n, p) up to k."""
    return sum(pmf(i, n, p) for i in range(k + 1))


def sample(n: int, p: float, size: int = 1) -> list[int]:
    """Generate `size` samples from Binomial(n, p)."""
    return [sum(random.random() < p for _ in range(n)) for _ in range(size)]


if __name__ == "__main__":
    # Parameters
    n, p = 10, 0.3
    ks = list(range(n + 1))

    # Compute PMF and CDF
    pmf_vals = [pmf(k, n, p) for k in ks]
    cdf_vals = [cdf(k, n, p) for k in ks]

    print("Binomial PMF:")
    for k, prob in zip(ks, pmf_vals):
        print(f"P(X={k}) = {prob:.4f}")

    print("\nBinomial CDF:")
    for k, cum_prob in zip(ks, cdf_vals):
        print(f"P(X≤{k}) = {cum_prob:.4f}")

    # Plot PMF
    plt.figure()
    plt.bar(ks, pmf_vals)
    plt.title(f"Binomial PMF (n={n}, p={p})")
    plt.xlabel("Number of successes k")
    plt.ylabel("Probability")
    plt.show()

    # Plot CDF
    plt.figure()
    plt.step(ks, cdf_vals, where='post')
    plt.title(f"Binomial CDF (n={n}, p={p})")
    plt.xlabel("k")
    plt.ylabel("F(k)")
    plt.show()
