import math
import random


# Helper function to compute Euclidean Distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


# Step 1: Define Unlabeled Dataset (2D Points)
data = [[1, 2], [1, 4], [2, 2], [8, 8], [9, 10], [8, 9]]

k = 2  # Number of clusters
max_iter = 10

# Step 2: Initialize Centroids Randomly
random.seed(42)
centroids = random.sample(data, k)

# Step 3: K-Means Clustering Algorithm

for iteration in range(max_iter):
    clusters = [[] for _ in range(k)]

    # Assign points to nearest centroid
    for point in data:
        distances = [euclidean_distance(point, c) for c in centroids]
        closest_index = distances.index(min(distances))
        clusters[closest_index].append(point)

    # Compute new centroids
    new_centroids = []
    for cluster in clusters:
        mean_x = sum(pt[0] for pt in cluster) / len(cluster)
        mean_y = sum(pt[1] for pt in cluster) / len(cluster)
        new_centroids.append([mean_x, mean_y])

    # Check for convergence
    if new_centroids == centroids:
        break
    centroids = new_centroids

# Step 4: Output Results
print("--- K-Means Clustering Complete ---")
for i, cluster in enumerate(clusters):
    print(
        f"Cluster {i+1} Centroid: [{centroids[i][0]:.2f}, {centroids[i][1]:.2f}]"
    )
    print(f"  Assigned Points: {cluster}")
