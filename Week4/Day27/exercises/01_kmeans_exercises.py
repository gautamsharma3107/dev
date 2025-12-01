"""
Day 27 - K-Means Clustering Exercises
======================================
Practice exercises for K-Means clustering
"""

import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

print("=" * 60)
print("K-MEANS CLUSTERING EXERCISES")
print("=" * 60)

# ============================================================
# Exercise 1: Basic K-Means
# ============================================================
print("\n" + "=" * 60)
print("Exercise 1: Basic K-Means Clustering")
print("=" * 60)

print("""
Task: Create sample data with 4 clusters and apply K-Means.
1. Generate data using make_blobs with 4 centers
2. Apply K-Means with n_clusters=4
3. Print the cluster labels and inertia
""")

# Generate sample data
X, y_true = make_blobs(n_samples=200, centers=4, random_state=42)

# TODO: Apply K-Means clustering
# Your code here:




# ============================================================
# Exercise 2: Elbow Method
# ============================================================
print("\n" + "=" * 60)
print("Exercise 2: Elbow Method")
print("=" * 60)

print("""
Task: Use the elbow method to find optimal K.
1. Run K-Means for K values from 1 to 10
2. Store the inertia for each K
3. Plot K vs Inertia
4. Identify the elbow point
""")

# TODO: Implement the elbow method
# Your code here:




# ============================================================
# Exercise 3: Silhouette Score
# ============================================================
print("\n" + "=" * 60)
print("Exercise 3: Silhouette Score")
print("=" * 60)

print("""
Task: Calculate silhouette score for different K values.
1. Run K-Means for K values from 2 to 8
2. Calculate silhouette score for each K
3. Print the K with highest silhouette score
""")

# TODO: Calculate silhouette scores
# from sklearn.metrics import silhouette_score
# Your code here:




# ============================================================
# Exercise 4: Scaling Before Clustering
# ============================================================
print("\n" + "=" * 60)
print("Exercise 4: Scaling Before Clustering")
print("=" * 60)

print("""
Task: Compare clustering with and without scaling.
1. Create data with different scales for each feature
2. Apply K-Means without scaling
3. Apply K-Means with StandardScaler
4. Compare the results
""")

# Create data with different scales
np.random.seed(42)
X_unscaled = np.column_stack([
    np.random.randn(100) * 100,  # Large scale
    np.random.randn(100)          # Small scale
])

# TODO: Compare clustering with and without scaling
# Your code here:




# ============================================================
# Exercise 5: Cluster Analysis
# ============================================================
print("\n" + "=" * 60)
print("Exercise 5: Cluster Analysis")
print("=" * 60)

print("""
Task: Analyze cluster characteristics.
1. Generate data with 3 clusters
2. Fit K-Means with K=3
3. Print the number of points in each cluster
4. Print the cluster centers
5. Calculate the mean and std of each feature per cluster
""")

# Generate data
X_analysis, _ = make_blobs(n_samples=150, centers=3, random_state=42)

# TODO: Analyze clusters
# Your code here:




print("\n" + "=" * 60)
print("✅ Complete all exercises and verify your solutions!")
print("=" * 60)

"""
SOLUTIONS
=========

Exercise 1:
kmeans = KMeans(n_clusters=4, random_state=42)
labels = kmeans.fit_predict(X)
print(f"Cluster labels: {np.unique(labels)}")
print(f"Inertia: {kmeans.inertia_:.2f}")

Exercise 2:
inertias = []
K_range = range(1, 11)
for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X)
    inertias.append(kmeans.inertia_)

plt.plot(K_range, inertias, 'bo-')
plt.xlabel('K')
plt.ylabel('Inertia')
plt.title('Elbow Method')
plt.show()

Exercise 3:
from sklearn.metrics import silhouette_score
best_k, best_score = 2, -1
for k in range(2, 9):
    kmeans = KMeans(n_clusters=k, random_state=42)
    labels = kmeans.fit_predict(X)
    score = silhouette_score(X, labels)
    print(f"K={k}: Silhouette = {score:.3f}")
    if score > best_score:
        best_k, best_score = k, score
print(f"Best K: {best_k} with score {best_score:.3f}")

Exercise 4:
# Without scaling
kmeans_unscaled = KMeans(n_clusters=3, random_state=42)
labels_unscaled = kmeans_unscaled.fit_predict(X_unscaled)

# With scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_unscaled)
kmeans_scaled = KMeans(n_clusters=3, random_state=42)
labels_scaled = kmeans_scaled.fit_predict(X_scaled)

print("Compare the cluster assignments - they will be different!")

Exercise 5:
kmeans = KMeans(n_clusters=3, random_state=42)
labels = kmeans.fit_predict(X_analysis)

print(f"Points per cluster: {np.bincount(labels)}")
print(f"Cluster centers:\\n{kmeans.cluster_centers_}")

for i in range(3):
    mask = labels == i
    cluster_data = X_analysis[mask]
    print(f"\\nCluster {i}:")
    print(f"  Mean: {cluster_data.mean(axis=0)}")
    print(f"  Std: {cluster_data.std(axis=0)}")
"""
