# uniform.py
import random
import numpy as np
import matplotlib.pyplot as plt

def pdf(x: float, a: float, b: float) -> float:
    """
    Probability Density Function of the continuous uniform distribution U(a, b).

    Parameters:
        x: point at which to evaluate the density
        a: lower bound
        b: upper bound

    Returns:
        density at x
    """
    if a >= b:
        raise ValueError("Lower bound a must be less than upper bound b.")
    return 1.0 / (b - a) if a <= x <= b else 0.0


def cdf(x: float, a: float, b: float) -> float:
    """
    Cumulative Distribution Function of U(a, b).

    Parameters:
        x: point at which to evaluate the CDF
        a: lower bound
        b: upper bound

    Returns:
        P(X <= x)
    """
    if a >= b:
        raise ValueError("Lower bound a must be less than upper bound b.")
    if x < a:
        return 0.0
    elif x > b:
        return 1.0
    else:
        return (x - a) / (b - a)


def sample(a: float, b: float, size: int = 1) -> list[float]:
    """
    Generate random samples from U(a, b).

    Parameters:
        a: lower bound
        b: upper bound
        size: number of samples

    Returns:
        list of samples
    """
    if a >= b:
        raise ValueError("Lower bound a must be less than upper bound b.")
    return [random.uniform(a, b) for _ in range(size)]


def mean(a: float, b: float) -> float:
    """
    Mean of U(a, b).

    Returns:
        (a + b) / 2
    """
    if a >= b:
        raise ValueError("Lower bound a must be less than upper bound b.")
    return (a + b) / 2


def var(a: float, b: float) -> float:
    """
    Variance of U(a, b).

    Returns:
        (b - a)**2 / 12
    """
    if a >= b:
        raise ValueError("Lower bound a must be less than upper bound b.")
    return (b - a) ** 2 / 12.0


def pdf_plot(a: float, b: float, num_points: int = 500):
    """
    Plot the PDF of U(a, b).
    """
    xs = np.linspace(a - (b - a) * 0.1, b + (b - a) * 0.1, num_points)
    ys = [pdf(x, a, b) for x in xs]
    plt.figure()
    plt.plot(xs, ys, label=f"PDF U({a}, {b})")
    plt.title(f"Uniform PDF (a={a}, b={b})")
    plt.xlabel("x")
    plt.ylabel("f(x) = P(a <= x <= b)")
    plt.legend()
    plt.show()


def cdf_plot(a: float, b: float, num_points: int = 500):
    """
    Plot the CDF of U(a, b).
    """
    xs = np.linspace(a - (b - a) * 0.1, b + (b - a) * 0.1, num_points)
    ys = [cdf(x, a, b) for x in xs]
    plt.figure()
    plt.step(xs, ys, where='post', label=f"CDF U({a}, {b})")
    plt.title(f"Uniform CDF (a={a}, b={b})")
    plt.xlabel("x")
    plt.ylabel("F(x) = P(X ≤ x)")
    plt.legend()
    plt.show()
