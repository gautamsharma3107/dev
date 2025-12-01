"""
Day 26 - Classification Exercises
==================================
Practice exercises for classification models
Complete each exercise to reinforce your learning!
"""

import numpy as np
from sklearn.datasets import load_breast_cancer, load_iris, make_classification
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

print("=" * 60)
print("DAY 26 - CLASSIFICATION EXERCISES")
print("=" * 60)

# ============================================================
# EXERCISE 1: Logistic Regression Basics
# ============================================================
print("\n" + "=" * 60)
print("EXERCISE 1: Logistic Regression Basics")
print("=" * 60)

print("""
Task: Train a logistic regression model on the Iris dataset
      - Use only 2 classes (setosa and versicolor)
      - Print accuracy and classification report
      - Try different values of C (0.01, 0.1, 1, 10)
""")

# Your code here:
# Hint: Use iris.target < 2 to filter for 2 classes

# Load Iris data
iris = load_iris()
X = iris.data[iris.target < 2]  # Only first 2 classes
y = iris.target[iris.target < 2]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# YOUR CODE: Try different C values
print("\nYour solution here...")




# ============================================================
# EXERCISE 2: Decision Tree Exploration
# ============================================================
print("\n" + "=" * 60)
print("EXERCISE 2: Decision Tree Exploration")
print("=" * 60)

print("""
Task: Explore decision tree parameters
      - Train decision trees with max_depth = [2, 4, 6, 8, 10, None]
      - Plot training accuracy vs test accuracy
      - Find the optimal max_depth that balances train/test performance
      
Use breast cancer dataset.
""")

# Your code here:
data = load_breast_cancer()
X, y = data.data, data.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# YOUR CODE: Try different max_depth values
print("\nYour solution here...")




# ============================================================
# EXERCISE 3: Random Forest Feature Importance
# ============================================================
print("\n" + "=" * 60)
print("EXERCISE 3: Random Forest Feature Importance")
print("=" * 60)

print("""
Task: Use Random Forest to find important features
      - Train a Random Forest on breast cancer data
      - Print the top 5 most important features
      - Train a new model using ONLY the top 5 features
      - Compare accuracy with full model
""")

# Your code here:
data = load_breast_cancer()
X, y = data.data, data.target
feature_names = data.feature_names

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# YOUR CODE: Find important features and compare models
print("\nYour solution here...")




# ============================================================
# EXERCISE 4: Model Comparison
# ============================================================
print("\n" + "=" * 60)
print("EXERCISE 4: Model Comparison")
print("=" * 60)

print("""
Task: Compare 3 classification models using cross-validation
      - Logistic Regression
      - Decision Tree
      - Random Forest
      
      Use 5-fold cross-validation and report mean ± std accuracy
      Use breast cancer dataset.
""")

# Your code here:
data = load_breast_cancer()
X, y = data.data, data.target

# Scale for logistic regression
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# YOUR CODE: Compare models with cross-validation
print("\nYour solution here...")




# ============================================================
# EXERCISE 5: Handling Imbalanced Data
# ============================================================
print("\n" + "=" * 60)
print("EXERCISE 5: Handling Imbalanced Data")
print("=" * 60)

print("""
Task: Work with an imbalanced dataset
      - Create imbalanced data (95% class 0, 5% class 1)
      - Train logistic regression without class weights
      - Train logistic regression WITH class_weight='balanced'
      - Compare accuracy, precision, recall, and F1 for class 1
""")

# Your code here:
# Create imbalanced dataset
X_imb, y_imb = make_classification(
    n_samples=1000,
    n_features=20,
    n_informative=10,
    n_classes=2,
    weights=[0.95, 0.05],
    random_state=42
)

X_train, X_test, y_train, y_test = train_test_split(
    X_imb, y_imb, test_size=0.2, random_state=42
)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# YOUR CODE: Compare models with and without class weights
print("\nYour solution here...")




# ============================================================
# BONUS EXERCISE: Grid Search for Best Model
# ============================================================
print("\n" + "=" * 60)
print("BONUS EXERCISE: Grid Search for Best Model")
print("=" * 60)

print("""
Task: Find the best Random Forest parameters using GridSearchCV
      - Parameters to tune: n_estimators, max_depth, min_samples_split
      - Use breast cancer dataset
      - Print best parameters and best score
      - Evaluate on test set
""")

# Your code here:
from sklearn.model_selection import GridSearchCV

data = load_breast_cancer()
X, y = data.data, data.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# YOUR CODE: Perform grid search
print("\nYour solution here...")




print("\n" + "=" * 60)
print("EXERCISES COMPLETE!")
print("=" * 60)
print("""
Check your solutions against the solution file.
Make sure you understand WHY each solution works!

Key takeaways:
- Different models have different strengths
- Hyperparameter tuning improves performance
- Class imbalance requires special handling
- Feature importance helps understand your data
""")

"""
SOLUTION KEY
============

Exercise 1:
for c in [0.01, 0.1, 1, 10]:
    model = LogisticRegression(C=c, random_state=42, max_iter=1000)
    model.fit(X_train_scaled, y_train)
    accuracy = model.score(X_test_scaled, y_test)
    print(f"C={c}: Accuracy = {accuracy:.4f}")

Exercise 2:
depths = [2, 4, 6, 8, 10, None]
for depth in depths:
    tree = DecisionTreeClassifier(max_depth=depth, random_state=42)
    tree.fit(X_train, y_train)
    train_acc = tree.score(X_train, y_train)
    test_acc = tree.score(X_test, y_test)
    print(f"max_depth={depth}: Train={train_acc:.3f}, Test={test_acc:.3f}")

Exercise 3:
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
full_accuracy = rf.score(X_test, y_test)

# Get top 5 features
importances = rf.feature_importances_
indices = np.argsort(importances)[::-1][:5]
print("Top 5 features:", [feature_names[i] for i in indices])

# Train with only top 5 features
X_train_top = X_train[:, indices]
X_test_top = X_test[:, indices]
rf_top = RandomForestClassifier(n_estimators=100, random_state=42)
rf_top.fit(X_train_top, y_train)
top_accuracy = rf_top.score(X_test_top, y_test)

print(f"Full model accuracy: {full_accuracy:.4f}")
print(f"Top 5 features accuracy: {top_accuracy:.4f}")

Exercise 4:
models = {
    'Logistic Regression': LogisticRegression(random_state=42, max_iter=1000),
    'Decision Tree': DecisionTreeClassifier(random_state=42),
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42)
}

for name, model in models.items():
    X_data = X_scaled if 'Logistic' in name else X
    scores = cross_val_score(model, X_data, y, cv=5, scoring='accuracy')
    print(f"{name}: {scores.mean():.4f} (+/- {scores.std():.4f})")

Exercise 5:
from sklearn.metrics import precision_score, recall_score, f1_score

# Without class weights
model_no_weight = LogisticRegression(random_state=42, max_iter=1000)
model_no_weight.fit(X_train_scaled, y_train)
y_pred_no_weight = model_no_weight.predict(X_test_scaled)

# With class weights
model_weighted = LogisticRegression(class_weight='balanced', random_state=42, max_iter=1000)
model_weighted.fit(X_train_scaled, y_train)
y_pred_weighted = model_weighted.predict(X_test_scaled)

print("Without class weights:")
print(f"  Accuracy: {accuracy_score(y_test, y_pred_no_weight):.4f}")
print(f"  Precision: {precision_score(y_test, y_pred_no_weight):.4f}")
print(f"  Recall: {recall_score(y_test, y_pred_no_weight):.4f}")
print(f"  F1: {f1_score(y_test, y_pred_no_weight):.4f}")

print("With class weights (balanced):")
print(f"  Accuracy: {accuracy_score(y_test, y_pred_weighted):.4f}")
print(f"  Precision: {precision_score(y_test, y_pred_weighted):.4f}")
print(f"  Recall: {recall_score(y_test, y_pred_weighted):.4f}")
print(f"  F1: {f1_score(y_test, y_pred_weighted):.4f}")

Bonus Exercise:
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [5, 10, None],
    'min_samples_split': [2, 5, 10]
}

grid_search = GridSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1
)
grid_search.fit(X_train, y_train)

print(f"Best parameters: {grid_search.best_params_}")
print(f"Best CV score: {grid_search.best_score_:.4f}")
print(f"Test accuracy: {grid_search.best_estimator_.score(X_test, y_test):.4f}")
"""
