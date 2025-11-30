# Day 27 Quick Reference Cheat Sheet

## K-Means Clustering
```python
from sklearn.cluster import KMeans
import numpy as np

# Create K-Means model
kmeans = KMeans(n_clusters=3, random_state=42)

# Fit and predict
labels = kmeans.fit_predict(X)

# Get cluster centers
centers = kmeans.cluster_centers_

# Get inertia (within-cluster sum of squares)
inertia = kmeans.inertia_

# Elbow method for optimal k
inertias = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X)
    inertias.append(kmeans.inertia_)
```

## PCA (Principal Component Analysis)
```python
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Always scale before PCA
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Create PCA (keep n components or variance ratio)
pca = PCA(n_components=2)  # Reduce to 2 dimensions
# OR
pca = PCA(n_components=0.95)  # Keep 95% variance

# Fit and transform
X_pca = pca.fit_transform(X_scaled)

# Explained variance ratio
print(pca.explained_variance_ratio_)
print(f"Total variance: {sum(pca.explained_variance_ratio_):.2f}")

# Component loadings (feature importance)
print(pca.components_)
```

## Cross-Validation
```python
from sklearn.model_selection import (
    cross_val_score,
    cross_validate,
    KFold,
    StratifiedKFold,
    LeaveOneOut
)

# Basic cross-validation
scores = cross_val_score(model, X, y, cv=5)
print(f"Mean: {scores.mean():.3f}, Std: {scores.std():.3f}")

# Multiple metrics
results = cross_validate(
    model, X, y, cv=5,
    scoring=['accuracy', 'f1', 'precision', 'recall']
)

# Custom K-Fold
kfold = KFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X, y, cv=kfold)

# Stratified K-Fold (maintains class distribution)
stratified_kfold = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X, y, cv=stratified_kfold)

# Leave-One-Out (LOO)
loo = LeaveOneOut()
scores = cross_val_score(model, X, y, cv=loo)
```

## Hyperparameter Tuning
```python
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV

# Grid Search (exhaustive)
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [3, 5, 7, None],
    'min_samples_split': [2, 5, 10]
}

grid_search = GridSearchCV(
    model,
    param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1,  # Use all cores
    verbose=1
)

grid_search.fit(X_train, y_train)

# Best parameters and score
print(f"Best params: {grid_search.best_params_}")
print(f"Best score: {grid_search.best_score_:.3f}")
best_model = grid_search.best_estimator_

# Random Search (faster for large grids)
from scipy.stats import randint, uniform

param_distributions = {
    'n_estimators': randint(50, 200),
    'max_depth': randint(3, 10),
    'min_samples_split': randint(2, 20)
}

random_search = RandomizedSearchCV(
    model,
    param_distributions,
    n_iter=50,  # Number of random combinations
    cv=5,
    random_state=42
)
random_search.fit(X_train, y_train)
```

## Clustering Evaluation Metrics
```python
from sklearn.metrics import (
    silhouette_score,
    calinski_harabasz_score,
    davies_bouldin_score
)

# Silhouette Score (-1 to 1, higher is better)
silhouette = silhouette_score(X, labels)

# Calinski-Harabasz Index (higher is better)
ch_score = calinski_harabasz_score(X, labels)

# Davies-Bouldin Index (lower is better)
db_score = davies_bouldin_score(X, labels)
```

## Customer Segmentation Pipeline
```python
# Complete pipeline
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('pca', PCA(n_components=2)),
    ('kmeans', KMeans(n_clusters=4, random_state=42))
])

# Fit and get labels
labels = pipeline.fit_predict(X)
```

## Common Patterns
```python
# Scale data before clustering
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Visualize clusters (2D)
import matplotlib.pyplot as plt
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=labels, cmap='viridis')
plt.scatter(centers[:, 0], centers[:, 1], c='red', marker='X', s=200)
plt.title('K-Means Clustering')
plt.show()

# Elbow method visualization
plt.plot(range(1, 11), inertias, marker='o')
plt.xlabel('Number of clusters (k)')
plt.ylabel('Inertia')
plt.title('Elbow Method')
plt.show()
```

## Tips and Best Practices
```python
# 1. Always scale features for clustering
# 2. Use elbow method or silhouette score to choose k
# 3. Use cross-validation to evaluate models
# 4. Use GridSearchCV for small parameter spaces
# 5. Use RandomizedSearchCV for large parameter spaces
# 6. Set random_state for reproducibility
# 7. Use n_jobs=-1 to parallelize
# 8. Start with simple models, then tune
```

---
**Keep this handy for quick reference!** 🚀
