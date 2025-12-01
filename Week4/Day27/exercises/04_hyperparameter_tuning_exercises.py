"""
Day 27 - Hyperparameter Tuning Exercises
=========================================
Practice exercises for GridSearchCV and hyperparameter optimization
"""

import numpy as np
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV, train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_breast_cancer
from scipy.stats import randint

print("=" * 60)
print("HYPERPARAMETER TUNING EXERCISES")
print("=" * 60)

# Load data for all exercises
data = load_breast_cancer()
X, y = data.data, data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ============================================================
# Exercise 1: Basic GridSearchCV
# ============================================================
print("\n" + "=" * 60)
print("Exercise 1: Basic GridSearchCV")
print("=" * 60)

print("""
Task: Use GridSearchCV to tune a Random Forest classifier.
1. Define param_grid with:
   - n_estimators: [50, 100]
   - max_depth: [3, 5, 7]
2. Create GridSearchCV with cv=5
3. Fit on training data
4. Print best parameters and best score
""")

# TODO: Implement GridSearchCV
# Your code here:




# ============================================================
# Exercise 2: Evaluate on Test Set
# ============================================================
print("\n" + "=" * 60)
print("Exercise 2: Evaluate Best Model on Test Set")
print("=" * 60)

print("""
Task: Evaluate the tuned model on the test set.
1. Get the best estimator from GridSearchCV
2. Predict on test data
3. Calculate and print test accuracy
4. Compare with CV score (check for overfitting)
""")

# TODO: Evaluate on test set
# Your code here:




# ============================================================
# Exercise 3: RandomizedSearchCV
# ============================================================
print("\n" + "=" * 60)
print("Exercise 3: RandomizedSearchCV")
print("=" * 60)

print("""
Task: Use RandomizedSearchCV for more efficient tuning.
1. Define param_distributions with:
   - n_estimators: randint(50, 200)
   - max_depth: randint(3, 15)
   - min_samples_split: randint(2, 20)
2. Create RandomizedSearchCV with n_iter=20, cv=5
3. Fit and print best parameters
4. Compare time with GridSearchCV (comment on efficiency)
""")

# TODO: Implement RandomizedSearchCV
# Your code here:




# ============================================================
# Exercise 4: Tune SVM
# ============================================================
print("\n" + "=" * 60)
print("Exercise 4: Tune SVM Classifier")
print("=" * 60)

print("""
Task: Tune SVM hyperparameters.
1. Define param_grid with:
   - C: [0.1, 1, 10]
   - kernel: ['rbf', 'linear']
   - gamma: ['scale', 'auto']
2. Use GridSearchCV with cv=5
3. Print best parameters and score
4. Evaluate on test set
""")

# TODO: Tune SVM
# Your code here:




# ============================================================
# Exercise 5: Custom Scoring
# ============================================================
print("\n" + "=" * 60)
print("Exercise 5: GridSearchCV with Custom Scoring")
print("=" * 60)

print("""
Task: Optimize for different metrics.
1. Run GridSearchCV with scoring='f1'
2. Run GridSearchCV with scoring='recall'
3. Compare best parameters for each metric
4. Discuss when to use which metric
""")

# TODO: Custom scoring
# Your code here:




print("\n" + "=" * 60)
print("✅ Complete all exercises and verify your solutions!")
print("=" * 60)

"""
SOLUTIONS
=========

Exercise 1:
param_grid = {
    'n_estimators': [50, 100],
    'max_depth': [3, 5, 7]
}
rf = RandomForestClassifier(random_state=42)
grid_search = GridSearchCV(rf, param_grid, cv=5, n_jobs=-1)
grid_search.fit(X_train_scaled, y_train)
print(f"Best params: {grid_search.best_params_}")
print(f"Best score: {grid_search.best_score_:.4f}")

Exercise 2:
best_model = grid_search.best_estimator_
test_score = best_model.score(X_test_scaled, y_test)
print(f"Test accuracy: {test_score:.4f}")
print(f"CV score: {grid_search.best_score_:.4f}")
print(f"Difference: {abs(test_score - grid_search.best_score_):.4f}")

Exercise 3:
param_distributions = {
    'n_estimators': randint(50, 200),
    'max_depth': randint(3, 15),
    'min_samples_split': randint(2, 20)
}
rf = RandomForestClassifier(random_state=42)
random_search = RandomizedSearchCV(rf, param_distributions, n_iter=20, cv=5, random_state=42)
random_search.fit(X_train_scaled, y_train)
print(f"Best params: {random_search.best_params_}")
print(f"Best score: {random_search.best_score_:.4f}")

Exercise 4:
svm_grid = {
    'C': [0.1, 1, 10],
    'kernel': ['rbf', 'linear'],
    'gamma': ['scale', 'auto']
}
svm = SVC(random_state=42)
svm_search = GridSearchCV(svm, svm_grid, cv=5)
svm_search.fit(X_train_scaled, y_train)
print(f"Best params: {svm_search.best_params_}")
print(f"Best CV score: {svm_search.best_score_:.4f}")
print(f"Test score: {svm_search.best_estimator_.score(X_test_scaled, y_test):.4f}")

Exercise 5:
param_grid = {'n_estimators': [50, 100], 'max_depth': [3, 5]}
rf = RandomForestClassifier(random_state=42)

# F1 scoring
grid_f1 = GridSearchCV(rf, param_grid, cv=5, scoring='f1')
grid_f1.fit(X_train_scaled, y_train)
print(f"F1 - Best params: {grid_f1.best_params_}")

# Recall scoring
grid_recall = GridSearchCV(rf, param_grid, cv=5, scoring='recall')
grid_recall.fit(X_train_scaled, y_train)
print(f"Recall - Best params: {grid_recall.best_params_}")

# Use F1 for balance between precision and recall
# Use recall when false negatives are costly (e.g., medical diagnosis)
"""
