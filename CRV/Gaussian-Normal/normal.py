# normal.py
import math
import numpy as np
import matplotlib.pyplot as plt

def factorial(n: int) -> int:
  return 1 if n == 0 or n == 1 else n * factorial(n - 1)

def pdf(x: float, mu: float = 0, sigma: float = 1) -> float:
  if sigma <= 0:
    raise ValueError("Standard deviation must be greater than zero")
  return (1.0 / (math.sqrt(2 * math.pi) * sigma)) * math.exp(-((x - mu) ** 2) / (2 * sigma ** 2))

def taylor_series(z: float, n: int = 4) -> float:
  return (1 / math.sqrt(2 * math.pi)) * (sum(((-1) ** i * (z) ** (2 * i + 1))/(factorial(i) * 2 ** i * (2 * i + 1)) for i in range(n + 1)))

def cdf(mu: float, sigma: float, upper = 'inf', lower = '-inf') -> float:
  if lower == '-inf':
    z = (upper - mu) / sigma
    return 0.5 + taylor_series(z)
  # elif upper == 'inf':
  #   z = (lower - mu) / sigma
  #   return 0.5 - taylor_series(z)
  else:
    return cdf(mu, sigma, upper) - cdf(mu, sigma, lower)
  
  if lower >= upper:
    raise ValueError("Lower bound must be less than upper bound")