"""
Day 26 - Evaluation Exercises
==============================
Practice exercises for evaluation metrics and confusion matrices
Complete each exercise to reinforce your learning!
"""

import numpy as np
from sklearn.datasets import load_breast_cancer, make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)
import matplotlib.pyplot as plt

print("=" * 60)
print("DAY 26 - EVALUATION EXERCISES")
print("=" * 60)

# ============================================================
# EXERCISE 1: Manual Metric Calculation
# ============================================================
print("\n" + "=" * 60)
print("EXERCISE 1: Manual Metric Calculation")
print("=" * 60)

print("""
Task: Calculate ALL metrics manually from scratch
      Given the predictions below, calculate:
      - TP, TN, FP, FN
      - Accuracy
      - Precision
      - Recall
      - F1 Score
      
      Verify your answers with sklearn!
""")

y_true = np.array([1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1])
y_pred = np.array([1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1])

print("y_true:", y_true)
print("y_pred:", y_pred)

# YOUR CODE: Calculate metrics manually
print("\nYour solution here...")
# TP = ?
# TN = ?
# FP = ?
# FN = ?
# Accuracy = ?
# Precision = ?
# Recall = ?
# F1 = ?




# ============================================================
# EXERCISE 2: Confusion Matrix Analysis
# ============================================================
print("\n" + "=" * 60)
print("EXERCISE 2: Confusion Matrix Analysis")
print("=" * 60)

print("""
Task: Analyze the following confusion matrix and answer:
      
      Confusion Matrix:
      [[85, 15],
       [10, 90]]
       
      1. What is the accuracy?
      2. What is the precision for class 1?
      3. What is the recall for class 1?
      4. What is the F1 score for class 1?
      5. Which error is more common: FP or FN?
""")

# YOUR CODE: Analyze the matrix
cm = np.array([[85, 15], [10, 90]])
print("Confusion Matrix:")
print(cm)

print("\nYour analysis here...")




# ============================================================
# EXERCISE 3: Comparing Metrics Across Thresholds
# ============================================================
print("\n" + "=" * 60)
print("EXERCISE 3: Comparing Metrics Across Thresholds")
print("=" * 60)

print("""
Task: Explore how prediction threshold affects metrics
      - Train a logistic regression on breast cancer data
      - Get predicted probabilities
      - Calculate metrics at different thresholds: 0.3, 0.5, 0.7
      - Observe the precision-recall trade-off
""")

# Setup
data = load_breast_cancer()
X, y = data.data, data.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LogisticRegression(random_state=42, max_iter=1000)
model.fit(X_train_scaled, y_train)

# Get probabilities
y_proba = model.predict_proba(X_test_scaled)[:, 1]

# YOUR CODE: Calculate metrics at different thresholds
print("\nYour solution here...")
# For threshold in [0.3, 0.5, 0.7]:
#   y_pred = (y_proba >= threshold).astype(int)
#   Calculate and print precision, recall, F1




# ============================================================
# EXERCISE 4: Multiclass Confusion Matrix
# ============================================================
print("\n" + "=" * 60)
print("EXERCISE 4: Multiclass Confusion Matrix")
print("=" * 60)

print("""
Task: Create and analyze a multiclass confusion matrix
      - Use the Iris dataset (3 classes)
      - Train a Random Forest classifier
      - Create and visualize the confusion matrix
      - Identify which classes are most confused
      - Print classification report
""")

from sklearn.datasets import load_iris

iris = load_iris()
X_iris, y_iris = iris.data, iris.target

X_train_i, X_test_i, y_train_i, y_test_i = train_test_split(
    X_iris, y_iris, test_size=0.2, random_state=42
)

# YOUR CODE: Train model, create confusion matrix, analyze
print("\nYour solution here...")




# ============================================================
# EXERCISE 5: Cost-Sensitive Analysis
# ============================================================
print("\n" + "=" * 60)
print("EXERCISE 5: Cost-Sensitive Analysis")
print("=" * 60)

print("""
Task: Analyze a medical diagnosis scenario
      
      Scenario: Detecting a disease
      - False Negative (missing disease): Cost = $10,000 (dangerous!)
      - False Positive (unnecessary test): Cost = $100
      
      Given two models with these confusion matrices:
      
      Model A:           Model B:
      [[90, 10],         [[70, 30],
       [ 5, 95]]          [ 1, 99]]
       
      1. Calculate the total cost for each model
      2. Which model is better for this scenario?
      3. Calculate precision and recall for each
""")

# YOUR CODE: Calculate costs and compare models
print("\nYour solution here...")

# Model A
cm_a = np.array([[90, 10], [5, 95]])

# Model B
cm_b = np.array([[70, 30], [1, 99]])

# Cost per error type
cost_fp = 100
cost_fn = 10000




# ============================================================
# BONUS EXERCISE: ROC Curve and AUC
# ============================================================
print("\n" + "=" * 60)
print("BONUS EXERCISE: ROC Curve and AUC")
print("=" * 60)

print("""
Task: Plot ROC curve and calculate AUC
      - Train logistic regression on breast cancer data
      - Calculate ROC curve points
      - Plot the curve
      - Calculate and print AUC score
      
      Use sklearn.metrics: roc_curve, auc, roc_auc_score
""")

from sklearn.metrics import roc_curve, auc, roc_auc_score

# YOUR CODE: Create ROC curve
print("\nYour solution here...")




print("\n" + "=" * 60)
print("EXERCISES COMPLETE!")
print("=" * 60)
print("""
Check your solutions against the solution key below.
Understanding evaluation metrics is CRUCIAL for real-world ML!

Key takeaways:
- Different metrics tell different stories
- Threshold choice affects precision/recall trade-off
- Cost-sensitive analysis matters in real applications
- ROC-AUC provides threshold-independent evaluation
""")

"""
SOLUTION KEY
============

Exercise 1:
TP = np.sum((y_true == 1) & (y_pred == 1))  # 6
TN = np.sum((y_true == 0) & (y_pred == 0))  # 4
FP = np.sum((y_true == 0) & (y_pred == 1))  # 2
FN = np.sum((y_true == 1) & (y_pred == 0))  # 3

Accuracy = (TP + TN) / (TP + TN + FP + FN) = (6 + 4) / 15 = 0.6667
Precision = TP / (TP + FP) = 6 / 8 = 0.75
Recall = TP / (TP + FN) = 6 / 9 = 0.6667
F1 = 2 * (0.75 * 0.6667) / (0.75 + 0.6667) = 0.7059

# Verify with sklearn
print(f"Accuracy: {accuracy_score(y_true, y_pred):.4f}")
print(f"Precision: {precision_score(y_true, y_pred):.4f}")
print(f"Recall: {recall_score(y_true, y_pred):.4f}")
print(f"F1: {f1_score(y_true, y_pred):.4f}")

Exercise 2:
TN, FP, FN, TP = 85, 15, 10, 90
Total = 200

1. Accuracy = (85 + 90) / 200 = 0.875
2. Precision = 90 / (90 + 15) = 0.857
3. Recall = 90 / (90 + 10) = 0.9
4. F1 = 2 * (0.857 * 0.9) / (0.857 + 0.9) = 0.878
5. FP (15) is more common than FN (10)

Exercise 3:
for threshold in [0.3, 0.5, 0.7]:
    y_pred_t = (y_proba >= threshold).astype(int)
    precision = precision_score(y_test, y_pred_t)
    recall = recall_score(y_test, y_pred_t)
    f1 = f1_score(y_test, y_pred_t)
    print(f"Threshold {threshold}:")
    print(f"  Precision: {precision:.4f}")
    print(f"  Recall: {recall:.4f}")
    print(f"  F1: {f1:.4f}")

Exercise 4:
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train_i, y_train_i)
y_pred_i = rf.predict(X_test_i)

cm_iris = confusion_matrix(y_test_i, y_pred_i)
print("Confusion Matrix:")
print(cm_iris)

# Visualize
fig, ax = plt.subplots(figsize=(8, 6))
ConfusionMatrixDisplay(cm_iris, display_labels=iris.target_names).plot(ax=ax)
plt.title("Iris Classification")
plt.savefig('/tmp/iris_cm_exercise.png')
plt.close()

print("\\nClassification Report:")
print(classification_report(y_test_i, y_pred_i, target_names=iris.target_names))

Exercise 5:
# Model A
FP_a, FN_a = 10, 5
cost_a = FP_a * cost_fp + FN_a * cost_fn
# cost_a = 10 * 100 + 5 * 10000 = 51,000

precision_a = 95 / (95 + 10)  # 0.905
recall_a = 95 / (95 + 5)      # 0.95

# Model B
FP_b, FN_b = 30, 1
cost_b = FP_b * cost_fp + FN_b * cost_fn
# cost_b = 30 * 100 + 1 * 10000 = 13,000

precision_b = 99 / (99 + 30)  # 0.767
recall_b = 99 / (99 + 1)      # 0.99

# Model B is better! Lower total cost despite lower precision.
# In medical diagnosis, recall (catching all diseases) is more important.

print(f"Model A cost: ${cost_a:,}")
print(f"Model B cost: ${cost_b:,}")
print(f"Model B is better for this scenario (higher recall, lower cost)")

Bonus Exercise:
# Get probabilities
y_proba_bonus = model.predict_proba(X_test_scaled)[:, 1]

# Calculate ROC curve
fpr, tpr, thresholds = roc_curve(y_test, y_proba_bonus)
roc_auc = auc(fpr, tpr)

# Or directly
auc_score = roc_auc_score(y_test, y_proba_bonus)

print(f"AUC Score: {auc_score:.4f}")

# Plot
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='blue', label=f'ROC Curve (AUC = {roc_auc:.4f})')
plt.plot([0, 1], [0, 1], color='gray', linestyle='--', label='Random Classifier')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend()
plt.savefig('/tmp/roc_curve_exercise.png')
plt.close()
"""
