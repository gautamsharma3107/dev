"""
Day 27 - Cross-Validation Exercises
=====================================
Practice exercises for model evaluation with cross-validation
"""

import numpy as np
from sklearn.model_selection import (
    cross_val_score,
    cross_validate,
    KFold,
    StratifiedKFold
)
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris, load_wine
from sklearn.preprocessing import StandardScaler

print("=" * 60)
print("CROSS-VALIDATION EXERCISES")
print("=" * 60)

# ============================================================
# Exercise 1: Basic Cross-Validation
# ============================================================
print("\n" + "=" * 60)
print("Exercise 1: Basic Cross-Validation")
print("=" * 60)

print("""
Task: Perform 5-fold cross-validation on Iris dataset.
1. Load Iris dataset
2. Create a LogisticRegression model
3. Use cross_val_score with cv=5
4. Print individual fold scores, mean, and std
""")

# Load data
iris = load_iris()
X, y = iris.data, iris.target

# TODO: Perform cross-validation
# Your code here:




# ============================================================
# Exercise 2: K-Fold vs Stratified K-Fold
# ============================================================
print("\n" + "=" * 60)
print("Exercise 2: K-Fold vs Stratified K-Fold")
print("=" * 60)

print("""
Task: Compare KFold and StratifiedKFold.
1. Create KFold with 5 splits and shuffle=True
2. Create StratifiedKFold with 5 splits
3. Run cross_val_score with each
4. Compare the results (mean and std)
""")

# TODO: Compare K-Fold strategies
# Your code here:




# ============================================================
# Exercise 3: Multiple Metrics
# ============================================================
print("\n" + "=" * 60)
print("Exercise 3: Multiple Metrics")
print("=" * 60)

print("""
Task: Evaluate model with multiple metrics.
1. Use cross_validate instead of cross_val_score
2. Include metrics: accuracy, precision_macro, recall_macro, f1_macro
3. Set return_train_score=True
4. Print test scores for all metrics
""")

# TODO: Multiple metrics evaluation
# Your code here:




# ============================================================
# Exercise 4: Compare Models
# ============================================================
print("\n" + "=" * 60)
print("Exercise 4: Compare Models with CV")
print("=" * 60)

print("""
Task: Compare multiple models using cross-validation.
1. Create models: LogisticRegression, RandomForestClassifier
2. Use the Wine dataset (scale it first)
3. Perform 5-fold CV for each model
4. Print comparison of mean scores
5. Identify the best model
""")

# Load Wine dataset
wine = load_wine()
X_wine, y_wine = wine.data, wine.target

# TODO: Compare models
# Your code here:




# ============================================================
# Exercise 5: Different K Values
# ============================================================
print("\n" + "=" * 60)
print("Exercise 5: Different K Values")
print("=" * 60)

print("""
Task: Analyze effect of different K values in K-Fold CV.
1. Run cross-validation with K = 3, 5, 10, 20
2. For each K, record mean score and std
3. Print results for all K values
4. Discuss trade-offs of different K values
""")

# TODO: Test different K values
# Your code here:




print("\n" + "=" * 60)
print("✅ Complete all exercises and verify your solutions!")
print("=" * 60)

"""
SOLUTIONS
=========

Exercise 1:
model = LogisticRegression(max_iter=200)
scores = cross_val_score(model, X, y, cv=5)
print(f"Scores: {scores}")
print(f"Mean: {scores.mean():.4f}")
print(f"Std: {scores.std():.4f}")

Exercise 2:
kfold = KFold(n_splits=5, shuffle=True, random_state=42)
stratified = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

model = LogisticRegression(max_iter=200)
scores_kfold = cross_val_score(model, X, y, cv=kfold)
scores_strat = cross_val_score(model, X, y, cv=stratified)

print(f"KFold: {scores_kfold.mean():.4f} (+/- {scores_kfold.std():.4f})")
print(f"Stratified: {scores_strat.mean():.4f} (+/- {scores_strat.std():.4f})")

Exercise 3:
model = LogisticRegression(max_iter=200)
scoring = ['accuracy', 'precision_macro', 'recall_macro', 'f1_macro']
results = cross_validate(model, X, y, cv=5, scoring=scoring, return_train_score=True)

for metric in scoring:
    test_scores = results[f'test_{metric}']
    print(f"{metric}: {test_scores.mean():.4f} (+/- {test_scores.std():.4f})")

Exercise 4:
scaler = StandardScaler()
X_wine_scaled = scaler.fit_transform(X_wine)

models = {
    'Logistic Regression': LogisticRegression(max_iter=1000),
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42)
}

best_model, best_score = None, 0
for name, model in models.items():
    scores = cross_val_score(model, X_wine_scaled, y_wine, cv=5)
    print(f"{name}: {scores.mean():.4f} (+/- {scores.std():.4f})")
    if scores.mean() > best_score:
        best_model, best_score = name, scores.mean()
print(f"\\nBest model: {best_model}")

Exercise 5:
model = LogisticRegression(max_iter=200)
for k in [3, 5, 10, 20]:
    scores = cross_val_score(model, X, y, cv=k)
    print(f"K={k}: Mean={scores.mean():.4f}, Std={scores.std():.4f}")

# Trade-offs:
# - Small K: Higher bias, lower variance, faster
# - Large K: Lower bias, higher variance, slower
# - K=5 or K=10 are common choices
"""
