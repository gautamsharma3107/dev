"""
Day 27 - PCA (Principal Component Analysis)
============================================
Learn: Dimensionality reduction, variance explanation, feature transformation

Key Concepts:
- PCA reduces dimensions while preserving variance
- It finds principal components (new orthogonal axes)
- Useful for visualization and noise reduction
- Always scale data before applying PCA
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris, load_digits

# ========== WHAT IS PCA? ==========
print("=" * 60)
print("WHAT IS PCA?")
print("=" * 60)

print("""
PCA (Principal Component Analysis) is a technique that:
1. Reduces the number of features (dimensions)
2. Preserves as much variance as possible
3. Creates new features (principal components) that are uncorrelated

Why use PCA?
- Reduce computational cost
- Visualize high-dimensional data
- Remove noise
- Handle multicollinearity

Key Terms:
- Principal Components: New axes that capture maximum variance
- Explained Variance: How much information each component retains
- Loading: Contribution of original features to each component
""")

# ========== PCA ON IRIS DATASET ==========
print("\n" + "=" * 60)
print("PCA ON IRIS DATASET")
print("=" * 60)

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target
feature_names = iris.feature_names
target_names = iris.target_names

print(f"Original shape: {X.shape}")
print(f"Features: {feature_names}")
print(f"Classes: {target_names}")

# Step 1: Scale the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("\nData scaled to zero mean and unit variance")

# Step 2: Apply PCA
pca = PCA(n_components=2)  # Reduce to 2 dimensions
X_pca = pca.fit_transform(X_scaled)

print(f"\nReduced shape: {X_pca.shape}")

# Explained variance
print(f"\nExplained variance ratio:")
for i, var in enumerate(pca.explained_variance_ratio_):
    print(f"  PC{i+1}: {var:.4f} ({var*100:.2f}%)")
print(f"Total variance retained: {sum(pca.explained_variance_ratio_)*100:.2f}%")

# Visualize
plt.figure(figsize=(10, 8))
colors = ['navy', 'turquoise', 'darkorange']
for color, i, target_name in zip(colors, [0, 1, 2], target_names):
    plt.scatter(
        X_pca[y == i, 0], X_pca[y == i, 1],
        color=color, alpha=0.8, lw=2, label=target_name
    )
plt.xlabel(f'PC1 ({pca.explained_variance_ratio_[0]*100:.1f}% variance)')
plt.ylabel(f'PC2 ({pca.explained_variance_ratio_[1]*100:.1f}% variance)')
plt.title('PCA of Iris Dataset (4D → 2D)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('01_pca_iris.png', dpi=100, bbox_inches='tight')
plt.close()
print("\nPlot saved: 01_pca_iris.png")

# ========== UNDERSTANDING COMPONENTS ==========
print("\n" + "=" * 60)
print("UNDERSTANDING PRINCIPAL COMPONENTS")
print("=" * 60)

# Component loadings (contribution of each feature)
print("\nPrincipal Component Loadings:")
print("(How much each original feature contributes to each PC)")
print("-" * 50)

loadings = pca.components_
for i, pc in enumerate(loadings):
    print(f"\nPC{i+1}:")
    for j, (name, loading) in enumerate(zip(feature_names, pc)):
        print(f"  {name}: {loading:.4f}")

# Visualize loadings
plt.figure(figsize=(10, 5))
x_pos = np.arange(len(feature_names))
width = 0.35

plt.bar(x_pos - width/2, loadings[0], width, label='PC1', color='steelblue')
plt.bar(x_pos + width/2, loadings[1], width, label='PC2', color='coral')
plt.xticks(x_pos, feature_names, rotation=45, ha='right')
plt.xlabel('Original Features')
plt.ylabel('Loading')
plt.title('Feature Contributions to Principal Components')
plt.legend()
plt.tight_layout()
plt.savefig('02_pca_loadings.png', dpi=100, bbox_inches='tight')
plt.close()
print("\nPlot saved: 02_pca_loadings.png")

# ========== CHOOSING NUMBER OF COMPONENTS ==========
print("\n" + "=" * 60)
print("CHOOSING NUMBER OF COMPONENTS")
print("=" * 60)

# Fit PCA with all components
pca_full = PCA()
pca_full.fit(X_scaled)

# Cumulative explained variance
cumulative_variance = np.cumsum(pca_full.explained_variance_ratio_)

print("\nExplained Variance by Number of Components:")
print("-" * 40)
for i, (var, cum_var) in enumerate(zip(
    pca_full.explained_variance_ratio_,
    cumulative_variance
)):
    print(f"PC{i+1}: {var*100:.2f}% (Cumulative: {cum_var*100:.2f}%)")

# Plot explained variance
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Individual variance
axes[0].bar(range(1, 5), pca_full.explained_variance_ratio_, color='steelblue')
axes[0].set_xlabel('Principal Component')
axes[0].set_ylabel('Explained Variance Ratio')
axes[0].set_title('Variance Explained by Each PC')
axes[0].set_xticks(range(1, 5))

# Cumulative variance
axes[1].plot(range(1, 5), cumulative_variance, 'ro-', linewidth=2)
axes[1].axhline(y=0.95, color='g', linestyle='--', label='95% Threshold')
axes[1].set_xlabel('Number of Components')
axes[1].set_ylabel('Cumulative Explained Variance')
axes[1].set_title('Cumulative Variance Explained')
axes[1].set_xticks(range(1, 5))
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('03_pca_variance.png', dpi=100, bbox_inches='tight')
plt.close()
print("\nPlot saved: 03_pca_variance.png")

# ========== PCA WITH VARIANCE THRESHOLD ==========
print("\n" + "=" * 60)
print("PCA WITH VARIANCE THRESHOLD")
print("=" * 60)

# Keep 95% of variance
pca_95 = PCA(n_components=0.95)
X_pca_95 = pca_95.fit_transform(X_scaled)

print(f"Components needed for 95% variance: {pca_95.n_components_}")
print(f"Actual variance retained: {sum(pca_95.explained_variance_ratio_)*100:.2f}%")

# ========== PCA ON DIGITS DATASET ==========
print("\n" + "=" * 60)
print("PCA ON DIGITS DATASET (64D → 2D)")
print("=" * 60)

# Load digits dataset
digits = load_digits()
X_digits = digits.data
y_digits = digits.target

print(f"Original shape: {X_digits.shape}")
print(f"Each digit is an 8x8 image = 64 features")

# Scale and apply PCA
scaler_digits = StandardScaler()
X_digits_scaled = scaler_digits.fit_transform(X_digits)

pca_digits = PCA(n_components=2)
X_digits_pca = pca_digits.fit_transform(X_digits_scaled)

print(f"Reduced shape: {X_digits_pca.shape}")
print(f"Variance retained: {sum(pca_digits.explained_variance_ratio_)*100:.2f}%")

# Visualize
plt.figure(figsize=(12, 10))
scatter = plt.scatter(
    X_digits_pca[:, 0], X_digits_pca[:, 1],
    c=y_digits, cmap='tab10', s=10, alpha=0.7
)
plt.colorbar(scatter, label='Digit')
plt.xlabel(f'PC1 ({pca_digits.explained_variance_ratio_[0]*100:.1f}%)')
plt.ylabel(f'PC2 ({pca_digits.explained_variance_ratio_[1]*100:.1f}%)')
plt.title('PCA of Digits Dataset (64D → 2D)')
plt.savefig('04_pca_digits.png', dpi=100, bbox_inches='tight')
plt.close()
print("\nPlot saved: 04_pca_digits.png")

# How many components for 95% variance?
pca_digits_95 = PCA(n_components=0.95)
pca_digits_95.fit(X_digits_scaled)
print(f"\nComponents needed for 95% variance: {pca_digits_95.n_components_}")

# ========== PRACTICAL: PCA + CLUSTERING ==========
print("\n" + "=" * 60)
print("PRACTICAL: PCA + K-MEANS CLUSTERING")
print("=" * 60)

from sklearn.cluster import KMeans

# Reduce dimensions then cluster
X_digits_reduced = PCA(n_components=10).fit_transform(X_digits_scaled)
print(f"Reduced from 64 to 10 dimensions")

# Cluster
kmeans = KMeans(n_clusters=10, random_state=42, n_init=10)
cluster_labels = kmeans.fit_predict(X_digits_reduced)

# Visualize in 2D
X_viz = PCA(n_components=2).fit_transform(X_digits_scaled)

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# True labels
scatter1 = axes[0].scatter(X_viz[:, 0], X_viz[:, 1], c=y_digits, cmap='tab10', s=10, alpha=0.7)
axes[0].set_title('True Digit Labels')
plt.colorbar(scatter1, ax=axes[0])

# Cluster labels
scatter2 = axes[1].scatter(X_viz[:, 0], X_viz[:, 1], c=cluster_labels, cmap='tab10', s=10, alpha=0.7)
axes[1].set_title('K-Means Cluster Labels (on PCA-reduced data)')
plt.colorbar(scatter2, ax=axes[1])

plt.tight_layout()
plt.savefig('05_pca_clustering.png', dpi=100, bbox_inches='tight')
plt.close()
print("Plot saved: 05_pca_clustering.png")

# ========== INVERSE TRANSFORM ==========
print("\n" + "=" * 60)
print("INVERSE TRANSFORM - RECONSTRUCTION")
print("=" * 60)

# Show how PCA can reconstruct data
n_components_list = [2, 10, 20, 40]

fig, axes = plt.subplots(2, 5, figsize=(15, 6))

# Original image
sample_idx = 0
original = X_digits[sample_idx].reshape(8, 8)
axes[0, 0].imshow(original, cmap='gray')
axes[0, 0].set_title('Original')
axes[0, 0].axis('off')

# Reconstructions with different n_components
for i, n_comp in enumerate(n_components_list):
    pca_temp = PCA(n_components=n_comp)
    X_temp = pca_temp.fit_transform(X_digits_scaled)
    X_reconstructed = pca_temp.inverse_transform(X_temp)
    X_reconstructed = scaler_digits.inverse_transform(X_reconstructed)
    
    reconstructed = X_reconstructed[sample_idx].reshape(8, 8)
    axes[0, i+1].imshow(reconstructed, cmap='gray')
    axes[0, i+1].set_title(f'{n_comp} PCs')
    axes[0, i+1].axis('off')

# Another sample
sample_idx = 100
original = X_digits[sample_idx].reshape(8, 8)
axes[1, 0].imshow(original, cmap='gray')
axes[1, 0].set_title('Original')
axes[1, 0].axis('off')

for i, n_comp in enumerate(n_components_list):
    pca_temp = PCA(n_components=n_comp)
    X_temp = pca_temp.fit_transform(X_digits_scaled)
    X_reconstructed = pca_temp.inverse_transform(X_temp)
    X_reconstructed = scaler_digits.inverse_transform(X_reconstructed)
    
    reconstructed = X_reconstructed[sample_idx].reshape(8, 8)
    axes[1, i+1].imshow(reconstructed, cmap='gray')
    axes[1, i+1].set_title(f'{n_comp} PCs')
    axes[1, i+1].axis('off')

plt.suptitle('Image Reconstruction with Different Number of Principal Components')
plt.tight_layout()
plt.savefig('06_pca_reconstruction.png', dpi=100, bbox_inches='tight')
plt.close()
print("Plot saved: 06_pca_reconstruction.png")

print("\n" + "=" * 60)
print("✅ PCA - Complete!")
print("=" * 60)
