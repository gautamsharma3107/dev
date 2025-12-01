# Day 26 Quick Reference Cheat Sheet

## Classification vs Regression
```python
# Classification: Predict discrete labels (categories)
# Examples: spam/not spam, disease/no disease, cat/dog

# Regression: Predict continuous values
# Examples: house price, temperature, sales
```

## Logistic Regression
```python
from sklearn.linear_model import LogisticRegression

# Create and train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict classes
y_pred = model.predict(X_test)

# Predict probabilities
y_proba = model.predict_proba(X_test)

# Key parameters
LogisticRegression(
    C=1.0,              # Inverse of regularization strength
    max_iter=100,       # Maximum iterations
    solver='lbfgs',     # Algorithm to use
    multi_class='auto'  # For multiclass problems
)
```

## Decision Trees
```python
from sklearn.tree import DecisionTreeClassifier

# Create and train
tree = DecisionTreeClassifier(
    max_depth=5,          # Max tree depth
    min_samples_split=2,  # Min samples to split
    min_samples_leaf=1,   # Min samples in leaf
    criterion='gini'      # 'gini' or 'entropy'
)
tree.fit(X_train, y_train)

# Predict
y_pred = tree.predict(X_test)

# Feature importance
importances = tree.feature_importances_
```

## Random Forests
```python
from sklearn.ensemble import RandomForestClassifier

# Create and train
rf = RandomForestClassifier(
    n_estimators=100,     # Number of trees
    max_depth=10,         # Max depth of each tree
    min_samples_split=2,
    random_state=42
)
rf.fit(X_train, y_train)

# Predict
y_pred = rf.predict(X_test)

# Feature importance
importances = rf.feature_importances_
```

## Evaluation Metrics
```python
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report
)

# Accuracy: (TP + TN) / Total
accuracy = accuracy_score(y_true, y_pred)

# Precision: TP / (TP + FP) - "How precise are positive predictions?"
precision = precision_score(y_true, y_pred)

# Recall: TP / (TP + FN) - "What % of actual positives found?"
recall = recall_score(y_true, y_pred)

# F1 Score: 2 * (precision * recall) / (precision + recall)
f1 = f1_score(y_true, y_pred)

# Complete report
print(classification_report(y_true, y_pred))
```

## Confusion Matrix
```python
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

# Create confusion matrix
cm = confusion_matrix(y_true, y_pred)
# Format: [[TN, FP], [FN, TP]]

# Visualize
disp = ConfusionMatrixDisplay(cm, display_labels=['Negative', 'Positive'])
disp.plot(cmap='Blues')
plt.show()
```

## Confusion Matrix Layout
```
                    Predicted
                 Neg    |   Pos
              -------+--------
Actual  Neg  |   TN   |   FP   |  → FP = Type I Error
        Pos  |   FN   |   TP   |  → FN = Type II Error
              -------+--------

TN = True Negative (correctly predicted negative)
FP = False Positive (incorrectly predicted positive)
FN = False Negative (incorrectly predicted negative)
TP = True Positive (correctly predicted positive)
```

## When to Use Each Metric
```python
# Accuracy: When classes are balanced
# Precision: When false positives are costly (e.g., spam filter)
# Recall: When false negatives are costly (e.g., disease detection)
# F1 Score: When you need balance between precision and recall
```

## Cross-Validation
```python
from sklearn.model_selection import cross_val_score

# 5-fold cross-validation
scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')
print(f"Accuracy: {scores.mean():.3f} (+/- {scores.std():.3f})")
```

## Model Comparison Template
```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scale features (important for logistic regression)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train and evaluate multiple models
models = {
    'Logistic Regression': LogisticRegression(),
    'Decision Tree': DecisionTreeClassifier(),
    'Random Forest': RandomForestClassifier()
}

for name, model in models.items():
    model.fit(X_train_scaled, y_train)
    score = model.score(X_test_scaled, y_test)
    print(f"{name}: {score:.3f}")
```

## Common Datasets for Practice
```python
from sklearn.datasets import (
    load_iris,          # 3-class classification
    load_breast_cancer, # Binary classification
    load_digits,        # Multi-class (0-9)
    make_classification # Generate synthetic data
)

# Load breast cancer dataset (binary)
data = load_breast_cancer()
X, y = data.data, data.target

# Generate synthetic data
X, y = make_classification(
    n_samples=1000,
    n_features=20,
    n_classes=2,
    random_state=42
)
```

## Tips for Better Classification
```python
# 1. Always scale features for logistic regression
# 2. Use random_state for reproducibility
# 3. Check class balance before training
# 4. Use stratified splits for imbalanced data
# 5. Start simple, then add complexity
# 6. Use cross-validation for reliable estimates
```

---
**Keep this handy for quick reference!** 🚀
