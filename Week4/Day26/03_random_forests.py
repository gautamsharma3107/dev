"""
Day 26 - Random Forests
========================
Learn: Ensemble learning with random forests

Key Concepts:
- Random Forest = Many decision trees combined
- Uses bagging (bootstrap aggregating)
- Reduces overfitting compared to single trees
- More accurate and robust
"""

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.datasets import load_breast_cancer, load_iris
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt

# ========== WHAT IS A RANDOM FOREST? ==========
print("=" * 60)
print("WHAT IS A RANDOM FOREST?")
print("=" * 60)

print("""
Random Forest is an ENSEMBLE method - it combines many models:

Single Tree:          Random Forest:
    🌳                 🌳🌳🌳🌳🌳
     │                  │ │ │ │ │
  Decision          Many decisions
     │                  │ │ │ │ │
  Prediction         Vote/Average

How it works:
1. Create multiple decision trees (e.g., 100 trees)
2. Each tree is trained on a random subset of data (bagging)
3. Each split considers a random subset of features
4. For classification: trees vote, majority wins
5. For regression: average the predictions

Why it's better than single trees:
- Reduces overfitting
- More stable predictions
- Better accuracy
- Handles high-dimensional data well
""")

# ========== BASIC EXAMPLE ==========
print("\n" + "=" * 60)
print("BASIC EXAMPLE: Breast Cancer Classification")
print("=" * 60)

# Load dataset
data = load_breast_cancer()
X, y = data.data, data.target
feature_names = data.feature_names
target_names = data.target_names

print(f"Dataset shape: {X.shape}")
print(f"Features: {len(feature_names)}")
print(f"Classes: {target_names}")

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ========== TRAINING RANDOM FOREST ==========
print("\n" + "=" * 60)
print("TRAINING RANDOM FOREST")
print("=" * 60)

# Create and train model
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

print("✅ Random Forest trained!")
print(f"Number of trees: {rf.n_estimators}")
print(f"Number of features: {rf.n_features_in_}")

# Make predictions
y_pred = rf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"\nAccuracy: {accuracy:.4f} ({accuracy*100:.1f}%)")

# ========== COMPARING WITH SINGLE DECISION TREE ==========
print("\n" + "=" * 60)
print("RANDOM FOREST vs DECISION TREE")
print("=" * 60)

from sklearn.tree import DecisionTreeClassifier

# Train single tree
tree = DecisionTreeClassifier(random_state=42)
tree.fit(X_train, y_train)
tree_accuracy = tree.score(X_test, y_test)

print(f"Single Decision Tree Accuracy: {tree_accuracy:.4f}")
print(f"Random Forest Accuracy:        {accuracy:.4f}")
print(f"Improvement: {(accuracy - tree_accuracy)*100:.2f}%")

# ========== EFFECT OF NUMBER OF TREES ==========
print("\n" + "=" * 60)
print("EFFECT OF NUMBER OF TREES (n_estimators)")
print("=" * 60)

print("""
More trees generally = better accuracy, but diminishing returns.
Also increases training time.
""")

n_trees_list = [1, 5, 10, 25, 50, 100, 200]
accuracies = []

for n_trees in n_trees_list:
    rf_n = RandomForestClassifier(n_estimators=n_trees, random_state=42)
    rf_n.fit(X_train, y_train)
    acc = rf_n.score(X_test, y_test)
    accuracies.append(acc)
    print(f"n_estimators={n_trees:3d}: Accuracy = {acc:.4f}")

# ========== FEATURE IMPORTANCE ==========
print("\n" + "=" * 60)
print("FEATURE IMPORTANCE")
print("=" * 60)

print("""
Random Forest provides feature importance based on:
- How much each feature decreases impurity
- Averaged across all trees

This is more reliable than single tree importance.
""")

importances = rf.feature_importances_
feature_importance = list(zip(feature_names, importances))
feature_importance.sort(key=lambda x: x[1], reverse=True)

print("\nTop 10 most important features:")
for i, (name, importance) in enumerate(feature_importance[:10], 1):
    bar = "█" * int(importance * 50)
    print(f"{i:2d}. {name:25s}: {importance:.4f} {bar}")

# ========== KEY HYPERPARAMETERS ==========
print("\n" + "=" * 60)
print("KEY HYPERPARAMETERS")
print("=" * 60)

print("""
RandomForestClassifier parameters:

1. n_estimators (default=100):
   - Number of trees in the forest
   - More trees = better but slower

2. max_depth (default=None):
   - Maximum depth of each tree
   - None = trees expand until pure leaves

3. min_samples_split (default=2):
   - Minimum samples needed to split a node

4. min_samples_leaf (default=1):
   - Minimum samples in leaf node

5. max_features (default='sqrt'):
   - Number of features to consider at each split
   - 'sqrt' = sqrt(n_features)
   - 'log2' = log2(n_features)
   - int/float = exact number or fraction

6. bootstrap (default=True):
   - Whether to use bootstrap samples

7. oob_score (default=False):
   - Whether to use out-of-bag samples for validation
""")

# ========== OUT-OF-BAG SCORE ==========
print("\n" + "=" * 60)
print("OUT-OF-BAG (OOB) SCORE")
print("=" * 60)

print("""
OOB Score is a free validation score!

How it works:
- Each tree is trained on ~63% of data (bootstrap sample)
- Remaining ~37% is "out-of-bag" for that tree
- OOB score = average prediction error on OOB samples

It's like cross-validation but free!
""")

rf_oob = RandomForestClassifier(
    n_estimators=100,
    oob_score=True,  # Enable OOB scoring
    random_state=42
)
rf_oob.fit(X_train, y_train)

print(f"OOB Score: {rf_oob.oob_score_:.4f}")
print(f"Test Score: {rf_oob.score(X_test, y_test):.4f}")

# ========== HYPERPARAMETER TUNING ==========
print("\n" + "=" * 60)
print("HYPERPARAMETER TUNING")
print("=" * 60)

from sklearn.model_selection import GridSearchCV

# Define parameter grid (smaller for speed)
param_grid = {
    'n_estimators': [50, 100],
    'max_depth': [5, 10, None],
    'min_samples_split': [2, 5],
}

print("Running Grid Search (this may take a moment)...")

grid_search = GridSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid,
    cv=3,
    scoring='accuracy',
    n_jobs=-1  # Use all CPU cores
)
grid_search.fit(X_train, y_train)

print(f"\nBest parameters: {grid_search.best_params_}")
print(f"Best CV score: {grid_search.best_score_:.4f}")
print(f"Test accuracy: {grid_search.best_estimator_.score(X_test, y_test):.4f}")

# ========== MULTICLASS CLASSIFICATION ==========
print("\n" + "=" * 60)
print("MULTICLASS CLASSIFICATION (Iris)")
print("=" * 60)

iris = load_iris()
X_iris, y_iris = iris.data, iris.target

X_train_i, X_test_i, y_train_i, y_test_i = train_test_split(
    X_iris, y_iris, test_size=0.2, random_state=42
)

rf_multi = RandomForestClassifier(n_estimators=100, random_state=42)
rf_multi.fit(X_train_i, y_train_i)
y_pred_i = rf_multi.predict(X_test_i)

print(f"Accuracy: {accuracy_score(y_test_i, y_pred_i):.4f}")
print("\nClassification Report:")
print(classification_report(y_test_i, y_pred_i, target_names=iris.target_names))

# Feature importance for Iris
print("\nFeature Importance (Iris):")
for name, imp in zip(iris.feature_names, rf_multi.feature_importances_):
    print(f"  {name}: {imp:.4f}")

# ========== CROSS-VALIDATION ==========
print("\n" + "=" * 60)
print("CROSS-VALIDATION")
print("=" * 60)

rf_cv = RandomForestClassifier(n_estimators=100, random_state=42)
cv_scores = cross_val_score(rf_cv, X, y, cv=5, scoring='accuracy')

print("5-Fold Cross-Validation Results:")
print(f"Scores: {cv_scores}")
print(f"Mean: {cv_scores.mean():.4f} (+/- {cv_scores.std()*2:.4f})")

# ========== ADVANTAGES AND DISADVANTAGES ==========
print("\n" + "=" * 60)
print("ADVANTAGES AND DISADVANTAGES")
print("=" * 60)

print("""
✅ ADVANTAGES:
- High accuracy
- Reduces overfitting (vs single tree)
- Handles high-dimensional data
- Feature importance built-in
- Can handle missing values
- Works well out-of-the-box
- OOB score for free validation

❌ DISADVANTAGES:
- Less interpretable than single tree
- Slower to train with many trees
- Larger model size
- Memory intensive
- Not great for sparse data

💡 WHEN TO USE:
- When accuracy is more important than interpretability
- For classification and regression
- When you have lots of features
- As a strong baseline model
""")

# ========== PRACTICAL TIPS ==========
print("\n" + "=" * 60)
print("PRACTICAL TIPS")
print("=" * 60)

print("""
1. Start with n_estimators=100, increase if needed
2. Use max_features='sqrt' for classification
3. Enable oob_score=True for free validation
4. Use n_jobs=-1 to speed up training
5. Tune max_depth to prevent overfitting
6. Check feature importance for feature selection
7. Random Forest usually works well with default settings
""")

# ========== SAVING AND LOADING MODELS ==========
print("\n" + "=" * 60)
print("SAVING AND LOADING MODELS")
print("=" * 60)

import pickle

# Save model
with open('/tmp/random_forest_model.pkl', 'wb') as f:
    pickle.dump(rf, f)
print("✅ Model saved to /tmp/random_forest_model.pkl")

# Load model
with open('/tmp/random_forest_model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)

# Verify it works
loaded_accuracy = loaded_model.score(X_test, y_test)
print(f"Loaded model accuracy: {loaded_accuracy:.4f}")

print("\n" + "=" * 60)
print("✅ Random Forests - Complete!")
print("=" * 60)
