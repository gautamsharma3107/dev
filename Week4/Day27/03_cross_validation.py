"""
Day 27 - Cross-Validation
==========================
Learn: Model evaluation, K-Fold CV, stratified sampling

Key Concepts:
- Cross-validation gives more reliable performance estimates
- It uses multiple train-test splits
- K-Fold divides data into K parts for training and testing
- Stratified K-Fold maintains class distribution
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import (
    cross_val_score,
    cross_validate,
    KFold,
    StratifiedKFold,
    LeaveOneOut,
    train_test_split
)
from sklearn.datasets import load_iris, load_wine
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler

# ========== WHY CROSS-VALIDATION? ==========
print("=" * 60)
print("WHY CROSS-VALIDATION?")
print("=" * 60)

print("""
Problems with simple train-test split:
1. Results depend on how data is split
2. May not use all data for training
3. May not test on all data
4. Can be unreliable with small datasets

Cross-Validation Solution:
1. Divide data into K folds
2. Train on K-1 folds, test on 1 fold
3. Repeat K times (each fold is test set once)
4. Average the results

Benefits:
- More reliable performance estimate
- Uses all data for both training and testing
- Reduces variance in results
""")

# ========== BASIC CROSS-VALIDATION ==========
print("\n" + "=" * 60)
print("BASIC CROSS-VALIDATION")
print("=" * 60)

# Load Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

print(f"Dataset: Iris")
print(f"Samples: {len(X)}")
print(f"Features: {X.shape[1]}")
print(f"Classes: {len(np.unique(y))}")

# Create a simple model
model = LogisticRegression(max_iter=200, random_state=42)

# Simple cross-validation with 5 folds
scores = cross_val_score(model, X, y, cv=5)

print(f"\n5-Fold Cross-Validation Results:")
print(f"Scores: {scores}")
print(f"Mean Accuracy: {scores.mean():.4f}")
print(f"Std Deviation: {scores.std():.4f}")
print(f"95% Confidence Interval: {scores.mean():.4f} +/- {scores.std() * 2:.4f}")

# ========== DIFFERENT CV STRATEGIES ==========
print("\n" + "=" * 60)
print("DIFFERENT CV STRATEGIES")
print("=" * 60)

# 1. K-Fold Cross-Validation
print("\n1. K-Fold Cross-Validation")
kfold = KFold(n_splits=5, shuffle=True, random_state=42)
scores_kfold = cross_val_score(model, X, y, cv=kfold)
print(f"   Mean: {scores_kfold.mean():.4f}, Std: {scores_kfold.std():.4f}")

# 2. Stratified K-Fold (maintains class distribution)
print("\n2. Stratified K-Fold (maintains class distribution)")
stratified_kfold = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores_stratified = cross_val_score(model, X, y, cv=stratified_kfold)
print(f"   Mean: {scores_stratified.mean():.4f}, Std: {scores_stratified.std():.4f}")

# 3. Leave-One-Out (LOO)
print("\n3. Leave-One-Out (computationally expensive)")
loo = LeaveOneOut()
scores_loo = cross_val_score(model, X, y, cv=loo)
print(f"   Mean: {scores_loo.mean():.4f}, Std: {scores_loo.std():.4f}")

# ========== VISUALIZING K-FOLD SPLITS ==========
print("\n" + "=" * 60)
print("VISUALIZING K-FOLD SPLITS")
print("=" * 60)

# Create visualization of splits
fig, axes = plt.subplots(3, 1, figsize=(12, 8))

# Regular K-Fold
kfold_viz = KFold(n_splits=5, shuffle=False)
for i, (train_idx, test_idx) in enumerate(kfold_viz.split(X)):
    axes[0].scatter(train_idx, [i] * len(train_idx), c='blue', marker='s', s=10, label='Train' if i == 0 else '')
    axes[0].scatter(test_idx, [i] * len(test_idx), c='red', marker='s', s=10, label='Test' if i == 0 else '')
axes[0].set_ylabel('Fold')
axes[0].set_xlabel('Sample Index')
axes[0].set_title('K-Fold (5 folds, no shuffle)')
axes[0].legend(loc='upper right')
axes[0].set_yticks(range(5))

# Shuffled K-Fold
kfold_shuffle = KFold(n_splits=5, shuffle=True, random_state=42)
for i, (train_idx, test_idx) in enumerate(kfold_shuffle.split(X)):
    axes[1].scatter(train_idx, [i] * len(train_idx), c='blue', marker='s', s=10)
    axes[1].scatter(test_idx, [i] * len(test_idx), c='red', marker='s', s=10)
axes[1].set_ylabel('Fold')
axes[1].set_xlabel('Sample Index')
axes[1].set_title('K-Fold (5 folds, shuffled)')
axes[1].set_yticks(range(5))

# Stratified K-Fold
strat_kfold = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
for i, (train_idx, test_idx) in enumerate(strat_kfold.split(X, y)):
    axes[2].scatter(train_idx, [i] * len(train_idx), c='blue', marker='s', s=10)
    axes[2].scatter(test_idx, [i] * len(test_idx), c='red', marker='s', s=10)
axes[2].set_ylabel('Fold')
axes[2].set_xlabel('Sample Index')
axes[2].set_title('Stratified K-Fold (5 folds, maintains class distribution)')
axes[2].set_yticks(range(5))

plt.tight_layout()
plt.savefig('01_cv_splits.png', dpi=100, bbox_inches='tight')
plt.close()
print("Plot saved: 01_cv_splits.png")

# ========== MULTIPLE METRICS ==========
print("\n" + "=" * 60)
print("CROSS-VALIDATION WITH MULTIPLE METRICS")
print("=" * 60)

# Get multiple metrics at once
scoring = ['accuracy', 'precision_macro', 'recall_macro', 'f1_macro']
results = cross_validate(
    model, X, y, cv=5,
    scoring=scoring,
    return_train_score=True
)

print("\nResults from cross_validate:")
print("-" * 50)
for metric in scoring:
    test_key = f'test_{metric}'
    train_key = f'train_{metric}'
    print(f"\n{metric}:")
    print(f"  Test:  {results[test_key].mean():.4f} (+/- {results[test_key].std():.4f})")
    print(f"  Train: {results[train_key].mean():.4f} (+/- {results[train_key].std():.4f})")

# ========== COMPARING MODELS ==========
print("\n" + "=" * 60)
print("COMPARING MODELS WITH CV")
print("=" * 60)

# Scale data for fair comparison
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Define models to compare
models = {
    'Logistic Regression': LogisticRegression(max_iter=200, random_state=42),
    'Decision Tree': DecisionTreeClassifier(random_state=42),
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
    'SVM': SVC(random_state=42)
}

# Compare with cross-validation
cv_results = {}
print("\nModel Comparison (5-Fold CV):")
print("-" * 60)
print(f"{'Model':<25} {'Mean Accuracy':<15} {'Std Dev':<15}")
print("-" * 60)

for name, model in models.items():
    scores = cross_val_score(model, X_scaled, y, cv=5)
    cv_results[name] = scores
    print(f"{name:<25} {scores.mean():.4f}          {scores.std():.4f}")

# Visualize comparison
plt.figure(figsize=(10, 6))
plt.boxplot(
    [cv_results[name] for name in models.keys()],
    labels=models.keys()
)
plt.ylabel('Accuracy')
plt.title('Model Comparison using 5-Fold Cross-Validation')
plt.grid(True, alpha=0.3)
plt.xticks(rotation=15)
plt.savefig('02_model_comparison.png', dpi=100, bbox_inches='tight')
plt.close()
print("\nPlot saved: 02_model_comparison.png")

# ========== CV VS SIMPLE SPLIT ==========
print("\n" + "=" * 60)
print("CV VS SIMPLE TRAIN-TEST SPLIT")
print("=" * 60)

# Run multiple simple splits to show variance
n_iterations = 20
simple_split_scores = []
cv_scores_all = []

model = LogisticRegression(max_iter=200, random_state=42)

for i in range(n_iterations):
    # Simple split (different each time)
    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=i
    )
    model.fit(X_train, y_train)
    simple_split_scores.append(model.score(X_test, y_test))
    
    # Cross-validation (same each time)
    cv_score = cross_val_score(model, X_scaled, y, cv=5).mean()
    cv_scores_all.append(cv_score)

print(f"\nSimple Split (20 iterations):")
print(f"  Mean: {np.mean(simple_split_scores):.4f}")
print(f"  Std:  {np.std(simple_split_scores):.4f}")
print(f"  Range: {np.min(simple_split_scores):.4f} - {np.max(simple_split_scores):.4f}")

print(f"\n5-Fold CV (20 iterations):")
print(f"  Mean: {np.mean(cv_scores_all):.4f}")
print(f"  Std:  {np.std(cv_scores_all):.4f}")
print(f"  Range: {np.min(cv_scores_all):.4f} - {np.max(cv_scores_all):.4f}")

# Visualize
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.hist(simple_split_scores, bins=10, edgecolor='black', alpha=0.7)
plt.axvline(np.mean(simple_split_scores), color='red', linestyle='--', label=f'Mean: {np.mean(simple_split_scores):.4f}')
plt.xlabel('Accuracy')
plt.ylabel('Frequency')
plt.title('Simple Train-Test Split Variance')
plt.legend()

plt.subplot(1, 2, 2)
plt.hist(cv_scores_all, bins=10, edgecolor='black', alpha=0.7)
plt.axvline(np.mean(cv_scores_all), color='red', linestyle='--', label=f'Mean: {np.mean(cv_scores_all):.4f}')
plt.xlabel('Accuracy')
plt.ylabel('Frequency')
plt.title('5-Fold CV Variance')
plt.legend()

plt.tight_layout()
plt.savefig('03_cv_vs_split.png', dpi=100, bbox_inches='tight')
plt.close()
print("\nPlot saved: 03_cv_vs_split.png")

# ========== PRACTICAL EXAMPLE ==========
print("\n" + "=" * 60)
print("PRACTICAL: WINE CLASSIFICATION")
print("=" * 60)

# Load wine dataset
wine = load_wine()
X_wine = wine.data
y_wine = wine.target

print(f"Dataset: Wine")
print(f"Samples: {len(X_wine)}")
print(f"Features: {X_wine.shape[1]}")
print(f"Classes: {len(np.unique(y_wine))}")

# Scale data
scaler_wine = StandardScaler()
X_wine_scaled = scaler_wine.fit_transform(X_wine)

# Compare models
models_wine = {
    'Logistic Regression': LogisticRegression(max_iter=1000, random_state=42),
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
    'SVM': SVC(random_state=42)
}

print("\nModel Comparison (Stratified 5-Fold CV):")
print("-" * 60)

for name, model in models_wine.items():
    # Use stratified K-fold for imbalanced classes
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    
    results = cross_validate(
        model, X_wine_scaled, y_wine, cv=cv,
        scoring=['accuracy', 'f1_macro'],
        return_train_score=True
    )
    
    print(f"\n{name}:")
    print(f"  Test Accuracy: {results['test_accuracy'].mean():.4f} (+/- {results['test_accuracy'].std():.4f})")
    print(f"  Test F1-Macro: {results['test_f1_macro'].mean():.4f} (+/- {results['test_f1_macro'].std():.4f})")

# ========== BEST PRACTICES ==========
print("\n" + "=" * 60)
print("CROSS-VALIDATION BEST PRACTICES")
print("=" * 60)

print("""
1. Use Stratified K-Fold for classification problems
   - Maintains class distribution in each fold
   
2. Choose appropriate K value:
   - K=5 or K=10 are common choices
   - Smaller K: higher bias, lower variance
   - Larger K: lower bias, higher variance
   
3. Always shuffle data (unless time-series)
   - shuffle=True in KFold/StratifiedKFold
   
4. Report mean and standard deviation
   - Shows both performance and stability
   
5. Use same CV strategy when comparing models
   - Use same random_state for fair comparison
   
6. Don't use CV for final model training
   - After selection, train on full training set
""")

print("\n" + "=" * 60)
print("✅ Cross-Validation - Complete!")
print("=" * 60)
