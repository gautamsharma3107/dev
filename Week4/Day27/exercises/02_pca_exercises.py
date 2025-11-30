"""
Day 27 - PCA Exercises
=======================
Practice exercises for Principal Component Analysis
"""

import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris, load_digits
import matplotlib.pyplot as plt

print("=" * 60)
print("PCA EXERCISES")
print("=" * 60)

# ============================================================
# Exercise 1: Basic PCA
# ============================================================
print("\n" + "=" * 60)
print("Exercise 1: Basic PCA")
print("=" * 60)

print("""
Task: Apply PCA to reduce Iris dataset to 2 dimensions.
1. Load Iris dataset
2. Scale the data using StandardScaler
3. Apply PCA with n_components=2
4. Print explained variance ratio for each component
""")

# Load data
iris = load_iris()
X = iris.data

# TODO: Apply PCA
# Your code here:




# ============================================================
# Exercise 2: Choosing Number of Components
# ============================================================
print("\n" + "=" * 60)
print("Exercise 2: Choosing Number of Components")
print("=" * 60)

print("""
Task: Determine how many components to keep for 95% variance.
1. Fit PCA with all components
2. Calculate cumulative explained variance
3. Find minimum components for 95% variance
""")

# TODO: Find optimal number of components
# Your code here:




# ============================================================
# Exercise 3: PCA with Variance Threshold
# ============================================================
print("\n" + "=" * 60)
print("Exercise 3: PCA with Variance Threshold")
print("=" * 60)

print("""
Task: Use PCA to keep 90% of variance automatically.
1. Create PCA with n_components=0.90
2. Fit and transform the scaled data
3. Print how many components were kept
4. Print the actual variance retained
""")

# TODO: PCA with variance threshold
# Your code here:




# ============================================================
# Exercise 4: Visualize PCA Components
# ============================================================
print("\n" + "=" * 60)
print("Exercise 4: Visualize PCA Components")
print("=" * 60)

print("""
Task: Visualize how original features contribute to PCs.
1. Fit PCA with 2 components on scaled Iris data
2. Get the component loadings (pca.components_)
3. Print which original feature contributes most to PC1 and PC2
""")

# TODO: Analyze PCA components
# Your code here:




# ============================================================
# Exercise 5: PCA on High-Dimensional Data
# ============================================================
print("\n" + "=" * 60)
print("Exercise 5: PCA on High-Dimensional Data")
print("=" * 60)

print("""
Task: Apply PCA to reduce digits dataset from 64D to 2D.
1. Load digits dataset (64 features)
2. Scale the data
3. Apply PCA to reduce to 2 dimensions
4. Calculate variance retained
5. Visualize the reduced data colored by digit label
""")

# Load digits
digits = load_digits()
X_digits = digits.data
y_digits = digits.target

# TODO: Apply PCA to digits dataset
# Your code here:




print("\n" + "=" * 60)
print("✅ Complete all exercises and verify your solutions!")
print("=" * 60)

"""
SOLUTIONS
=========

Exercise 1:
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
print(f"PC1 variance: {pca.explained_variance_ratio_[0]:.4f}")
print(f"PC2 variance: {pca.explained_variance_ratio_[1]:.4f}")
print(f"Total: {sum(pca.explained_variance_ratio_):.4f}")

Exercise 2:
pca_full = PCA()
pca_full.fit(X_scaled)
cumulative = np.cumsum(pca_full.explained_variance_ratio_)
n_components_95 = np.argmax(cumulative >= 0.95) + 1
print(f"Components for 95% variance: {n_components_95}")

Exercise 3:
pca_90 = PCA(n_components=0.90)
X_pca_90 = pca_90.fit_transform(X_scaled)
print(f"Components kept: {pca_90.n_components_}")
print(f"Variance retained: {sum(pca_90.explained_variance_ratio_):.4f}")

Exercise 4:
pca = PCA(n_components=2)
pca.fit(X_scaled)
feature_names = iris.feature_names
for i, pc in enumerate(pca.components_):
    max_idx = np.argmax(np.abs(pc))
    print(f"PC{i+1}: {feature_names[max_idx]} (loading: {pc[max_idx]:.4f})")

Exercise 5:
scaler_digits = StandardScaler()
X_digits_scaled = scaler_digits.fit_transform(X_digits)
pca_digits = PCA(n_components=2)
X_digits_pca = pca_digits.fit_transform(X_digits_scaled)
print(f"Variance retained: {sum(pca_digits.explained_variance_ratio_):.4f}")

plt.scatter(X_digits_pca[:, 0], X_digits_pca[:, 1], c=y_digits, cmap='tab10', s=5)
plt.colorbar(label='Digit')
plt.title('PCA of Digits Dataset')
plt.show()
"""
