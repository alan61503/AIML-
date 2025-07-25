import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Generate synthetic 1D data
np.random.seed(42)
data = np.concatenate([
    np.random.normal(loc=2, scale=0.5, size=100),
    np.random.normal(loc=6, scale=0.7, size=100)
])

# Initialize parameters
k = 2
means = np.random.choice(data, k)
stds = np.full(k, 1.0)
weights = np.full(k, 1 / k)

# EM algorithm
for _ in range(100):
    # E-step: responsibilities
    resp = np.zeros((len(data), k))
    for i in range(k):
        resp[:, i] = weights[i] * norm.pdf(data, means[i], stds[i])
    resp /= resp.sum(axis=1, keepdims=True)

    # M-step: update parameters
    for i in range(k):
        r = resp[:, i]
        total = r.sum()
        means[i] = np.sum(r * data) / total
        stds[i] = np.sqrt(np.sum(r * (data - means[i]) ** 2) / total)
        weights[i] = total / len(data)

# Assign clusters (for coloring points)
labels = np.argmax(resp, axis=1)

# Plot
x_vals = np.linspace(min(data) - 1, max(data) + 1, 300)
plt.figure(figsize=(10, 6))
plt.hist(data, bins=30, density=True, alpha=0.4, color='gray', label='Histogram')

# Gaussian curves
for i in range(k):
    plt.plot(x_vals, weights[i] * norm.pdf(x_vals, means[i], stds[i]), label=f'Gaussian {i+1}')

# Scatter points by cluster color
colors = ['red', 'blue']
for i in range(k):
    plt.scatter(data[labels == i], [0.01] * sum(labels == i), c=colors[i], label=f'Cluster {i+1}', s=20)

plt.title("1D Data Clustering with EM (GMM)")
plt.xlabel("Data")
plt.ylabel("Density")
plt.legend()
plt.grid(True)
plt.show()