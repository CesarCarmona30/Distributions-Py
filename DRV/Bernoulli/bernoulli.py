import matplotlib.pyplot as plt


def pmf(p: float, x: int = 1):
    return (p ** x) * (1 - p) ** (1 - x)


if __name__ == "__main__":
    X = [0, 1]
    p = 1 - (0.1 / 100)
    
    be_x = [pmf(p, x) for x in X]

    print("Bernoulli PMF:")
    for x, be in zip(X, be_x):
        print(f"P(X={x}) = {be:.3f}")
    
    plt.figure()
    plt.bar(X, be_x)
    plt.title(f"Bernoulli PMF (p={p})")
    plt.xlabel("0: Software failure, 1: Software success")
    plt.ylabel("Probability of Software not failure")
    plt.show()
