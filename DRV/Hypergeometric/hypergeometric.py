# hypergeometric.py

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