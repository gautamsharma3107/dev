"""
Day 27 - K-Means Clustering
============================
Learn: K-Means algorithm, clustering concepts, elbow method

Key Concepts:
- K-Means is an unsupervised learning algorithm
- It groups similar data points into K clusters
- The algorithm minimizes within-cluster variance
- You need to specify the number of clusters (K) beforehand
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
from sklearn.datasets import make_blobs

# ========== WHAT IS K-MEANS? ==========
print("=" * 60)
print("WHAT IS K-MEANS CLUSTERING?")
print("=" * 60)

print("""
K-Means is an unsupervised learning algorithm that:
1. Groups similar data points together
2. Creates K clusters based on feature similarity
3. Does NOT require labeled data

Algorithm Steps:
1. Initialize K random centroids
2. Assign each point to nearest centroid
3. Update centroids as mean of assigned points
4. Repeat steps 2-3 until convergence

Use Cases:
- Customer segmentation
- Image compression
- Document clustering
- Anomaly detection
""")

# ========== GENERATE SAMPLE DATA ==========
print("\n" + "=" * 60)
print("GENERATING SAMPLE DATA")
print("=" * 60)

# Create synthetic data with clear clusters
X, y_true = make_blobs(
    n_samples=300,
    centers=4,
    cluster_std=0.60,
    random_state=42
)

print(f"Data shape: {X.shape}")
print(f"Features: {X.shape[1]}")
print(f"Samples: {X.shape[0]}")

# Visualize the data
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.scatter(X[:, 0], X[:, 1], s=30, alpha=0.7)
plt.title('Raw Data (Unknown Clusters)')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')

plt.subplot(1, 2, 2)
plt.scatter(X[:, 0], X[:, 1], c=y_true, s=30, cmap='viridis', alpha=0.7)
plt.title('True Clusters (Ground Truth)')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')

plt.tight_layout()
plt.savefig('01_sample_data.png', dpi=100, bbox_inches='tight')
plt.close()
print("Plot saved: 01_sample_data.png")

# ========== BASIC K-MEANS ==========
print("\n" + "=" * 60)
print("BASIC K-MEANS CLUSTERING")
print("=" * 60)

# Create K-Means model with 4 clusters
kmeans = KMeans(
    n_clusters=4,
    random_state=42,
    n_init=10  # Number of times to run with different initializations
)

# Fit the model and predict cluster labels
labels = kmeans.fit_predict(X)

print(f"Cluster labels assigned: {np.unique(labels)}")
print(f"Points per cluster: {np.bincount(labels)}")

# Get cluster centers
centers = kmeans.cluster_centers_
print(f"\nCluster centers:\n{centers}")

# Inertia (within-cluster sum of squares)
print(f"\nInertia (lower is better): {kmeans.inertia_:.2f}")

# Visualize results
plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c=labels, s=30, cmap='viridis', alpha=0.7)
plt.scatter(
    centers[:, 0], centers[:, 1],
    c='red', marker='X', s=200, edgecolors='black',
    label='Centroids'
)
plt.title('K-Means Clustering Results')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.savefig('02_kmeans_results.png', dpi=100, bbox_inches='tight')
plt.close()
print("Plot saved: 02_kmeans_results.png")

# ========== ELBOW METHOD ==========
print("\n" + "=" * 60)
print("ELBOW METHOD - FINDING OPTIMAL K")
print("=" * 60)

print("""
The Elbow Method helps find the optimal number of clusters:
1. Run K-Means for different values of K
2. Plot inertia vs K
3. Look for the "elbow" point where improvement slows
""")

# Calculate inertia for different K values
inertias = []
K_range = range(1, 11)

for k in K_range:
    kmeans_temp = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans_temp.fit(X)
    inertias.append(kmeans_temp.inertia_)
    print(f"K={k}: Inertia = {kmeans_temp.inertia_:.2f}")

# Plot elbow curve
plt.figure(figsize=(8, 5))
plt.plot(K_range, inertias, 'bo-', linewidth=2, markersize=8)
plt.xlabel('Number of Clusters (K)')
plt.ylabel('Inertia')
plt.title('Elbow Method for Optimal K')
plt.axvline(x=4, color='r', linestyle='--', label='Optimal K=4')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('03_elbow_method.png', dpi=100, bbox_inches='tight')
plt.close()
print("\nPlot saved: 03_elbow_method.png")

# ========== SILHOUETTE SCORE ==========
print("\n" + "=" * 60)
print("SILHOUETTE SCORE - EVALUATING CLUSTERS")
print("=" * 60)

print("""
Silhouette Score measures cluster quality:
- Range: -1 to 1
- Higher is better
- Measures how similar points are to their cluster vs other clusters
""")

silhouette_scores = []

for k in range(2, 11):  # Silhouette needs at least 2 clusters
    kmeans_temp = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels_temp = kmeans_temp.fit_predict(X)
    score = silhouette_score(X, labels_temp)
    silhouette_scores.append(score)
    print(f"K={k}: Silhouette Score = {score:.3f}")

# Plot silhouette scores
plt.figure(figsize=(8, 5))
plt.plot(range(2, 11), silhouette_scores, 'go-', linewidth=2, markersize=8)
plt.xlabel('Number of Clusters (K)')
plt.ylabel('Silhouette Score')
plt.title('Silhouette Score for Different K')
plt.grid(True, alpha=0.3)
plt.savefig('04_silhouette_scores.png', dpi=100, bbox_inches='tight')
plt.close()
print("\nPlot saved: 04_silhouette_scores.png")

# ========== SCALING DATA ==========
print("\n" + "=" * 60)
print("IMPORTANCE OF SCALING")
print("=" * 60)

print("""
Why scale before K-Means?
- K-Means uses Euclidean distance
- Features with larger scales dominate
- Scaling ensures equal contribution from all features
""")

# Create data with different scales
np.random.seed(42)
X_unscaled = np.column_stack([
    np.random.randn(200) * 100,  # Large scale
    np.random.randn(200)          # Small scale
])

# Scale the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_unscaled)

# Compare clustering results
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Unscaled
kmeans_unscaled = KMeans(n_clusters=3, random_state=42, n_init=10)
labels_unscaled = kmeans_unscaled.fit_predict(X_unscaled)
axes[0].scatter(X_unscaled[:, 0], X_unscaled[:, 1], c=labels_unscaled, cmap='viridis')
axes[0].set_title('K-Means on Unscaled Data')
axes[0].set_xlabel('Feature 1 (Scale: 100)')
axes[0].set_ylabel('Feature 2 (Scale: 1)')

# Scaled
kmeans_scaled = KMeans(n_clusters=3, random_state=42, n_init=10)
labels_scaled = kmeans_scaled.fit_predict(X_scaled)
axes[1].scatter(X_scaled[:, 0], X_scaled[:, 1], c=labels_scaled, cmap='viridis')
axes[1].set_title('K-Means on Scaled Data')
axes[1].set_xlabel('Feature 1 (Standardized)')
axes[1].set_ylabel('Feature 2 (Standardized)')

plt.tight_layout()
plt.savefig('05_scaling_comparison.png', dpi=100, bbox_inches='tight')
plt.close()
print("Plot saved: 05_scaling_comparison.png")

# ========== PRACTICAL EXAMPLE ==========
print("\n" + "=" * 60)
print("PRACTICAL EXAMPLE: SIMPLE CUSTOMER SEGMENTATION")
print("=" * 60)

# Simulated customer data
np.random.seed(42)
n_customers = 200

# Features: Annual Income (thousands), Spending Score (1-100)
customers = np.vstack([
    np.random.randn(50, 2) * [10, 15] + [30, 20],   # Low income, low spending
    np.random.randn(50, 2) * [10, 15] + [30, 80],   # Low income, high spending
    np.random.randn(50, 2) * [10, 15] + [80, 20],   # High income, low spending
    np.random.randn(50, 2) * [10, 15] + [80, 80],   # High income, high spending
])

# Scale the data
scaler = StandardScaler()
customers_scaled = scaler.fit_transform(customers)

# Find optimal K
print("Finding optimal number of customer segments...")
for k in range(2, 7):
    kmeans_temp = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels_temp = kmeans_temp.fit_predict(customers_scaled)
    score = silhouette_score(customers_scaled, labels_temp)
    print(f"K={k}: Silhouette = {score:.3f}")

# Use K=4 (since we know there are 4 segments)
kmeans_customers = KMeans(n_clusters=4, random_state=42, n_init=10)
customer_labels = kmeans_customers.fit_predict(customers_scaled)

# Visualize segments
plt.figure(figsize=(10, 6))
scatter = plt.scatter(
    customers[:, 0], customers[:, 1],
    c=customer_labels, cmap='viridis', s=50, alpha=0.7
)
plt.colorbar(scatter, label='Segment')
plt.xlabel('Annual Income (thousands $)')
plt.ylabel('Spending Score (1-100)')
plt.title('Customer Segmentation')

# Add segment descriptions
segment_names = ['Budget Savers', 'Big Spenders', 'High Earners (Low Spend)', 'Premium Customers']
for i, name in enumerate(segment_names):
    mask = customer_labels == i
    center = customers[mask].mean(axis=0)
    plt.annotate(name, center, fontsize=10, ha='center',
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

plt.savefig('06_customer_segments.png', dpi=100, bbox_inches='tight')
plt.close()
print("\nPlot saved: 06_customer_segments.png")

# Segment analysis
print("\n" + "=" * 60)
print("SEGMENT ANALYSIS")
print("=" * 60)

for i in range(4):
    mask = customer_labels == i
    segment_data = customers[mask]
    print(f"\nSegment {i}:")
    print(f"  Count: {mask.sum()}")
    print(f"  Avg Income: ${segment_data[:, 0].mean():.1f}k")
    print(f"  Avg Spending Score: {segment_data[:, 1].mean():.1f}")

print("\n" + "=" * 60)
print("✅ K-Means Clustering - Complete!")
print("=" * 60)
