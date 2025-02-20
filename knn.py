import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

def euclidean_distance(p1, p2):
    return np.sqrt(np.sum((np.array(p1) - np.array(p2))**2))

# Dataset
points = np.array([
    [1, 1], [2, 2], [1, 3], [2, 3],  # Class A
    [6, 5], [7, 7], [8, 6], [6, 7]   # Class B
])
labels = np.array(['A', 'A', 'A', 'A', 'B', 'B', 'B', 'B'])

# New point to classify
x_new = np.array([3, 3])

def knn_classification(x_new, k):
    distances = [euclidean_distance(x_new, point) for point in points]
    sorted_indices = np.argsort(distances)
    k_nearest_labels = labels[sorted_indices[:k]]
    most_common = Counter(k_nearest_labels).most_common(1)
    return most_common[0][0]

# Finding the optimal k
k_values = range(1, 9)
k_results = [knn_classification(x_new, k) for k in k_values]

# Print predictions for different k values
for k, result in zip(k_values, k_results):
    print(f"For k={k}, Predicted Class: {result}")

# Finding the best k
best_k = Counter(k_results).most_common(1)[0][0]
print(f"\nOptimal k value: {best_k}")

# Plot dataset
plt.figure(figsize=(8, 6))
for i, point in enumerate(points):
    plt.scatter(point[0], point[1], color='red' if labels[i] == 'A' else 'blue', label=f"Class {labels[i]}")
plt.scatter(x_new[0], x_new[1], color='green', marker='*', s=200, label='New Point (3,3)')
plt.xlabel('x1')
plt.ylabel('x2')
plt.title('K-Nearest Neighbors Classification')
plt.legend()
plt.show()

# Conclusion
print("\nConclusion:")
print("For smaller k values, predictions might be sensitive to noise, while larger k values smooth out the decision boundary.")