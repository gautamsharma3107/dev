"""
Day 26 - Evaluation Metrics
============================
Learn: Accuracy, Precision, Recall, F1-Score for classification

Key Concepts:
- Accuracy is not always the best metric
- Precision vs Recall trade-off
- F1-Score balances precision and recall
- Choose metrics based on problem context
"""

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_breast_cancer, make_classification
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report
)

# ========== WHY MULTIPLE METRICS? ==========
print("=" * 60)
print("WHY MULTIPLE METRICS?")
print("=" * 60)

print("""
Imagine a spam detector on 1000 emails:
- 950 normal emails, 50 spam emails

A model that predicts EVERYTHING as "normal":
- Gets 95% accuracy! 
- But catches 0% of spam (completely useless)

This is why we need multiple metrics!

Key Question: What type of error is worse?
- Missing spam? (False Negative)
- Marking normal as spam? (False Positive)
""")

# ========== THE FOUR OUTCOMES ==========
print("\n" + "=" * 60)
print("THE FOUR OUTCOMES (Binary Classification)")
print("=" * 60)

print("""
                    PREDICTED
                 Neg    |   Pos
              ─────────┼─────────
ACTUAL  Neg  |   TN    |   FP    |  
        Pos  |   FN    |   TP    |  
              ─────────┼─────────

TN (True Negative):  Correctly predicted negative
FP (False Positive): Incorrectly predicted positive (Type I Error)
FN (False Negative): Incorrectly predicted negative (Type II Error)  
TP (True Positive):  Correctly predicted positive

Example - Disease Detection:
- TP: Sick patient correctly diagnosed as sick
- TN: Healthy patient correctly diagnosed as healthy
- FP: Healthy patient incorrectly diagnosed as sick
- FN: Sick patient incorrectly diagnosed as healthy (DANGEROUS!)
""")

# ========== SETUP EXAMPLE DATA ==========
print("\n" + "=" * 60)
print("SETUP: Creating Example Predictions")
print("=" * 60)

# Create a scenario
y_true = np.array([1, 1, 1, 1, 1, 0, 0, 0, 0, 0])  # 5 positive, 5 negative
y_pred = np.array([1, 1, 1, 0, 0, 0, 0, 0, 1, 1])  # Model predictions

print("Actual:    ", y_true)
print("Predicted: ", y_pred)

# Count outcomes
TP = np.sum((y_true == 1) & (y_pred == 1))
TN = np.sum((y_true == 0) & (y_pred == 0))
FP = np.sum((y_true == 0) & (y_pred == 1))
FN = np.sum((y_true == 1) & (y_pred == 0))

print(f"\nTP (True Positives):  {TP}")
print(f"TN (True Negatives):  {TN}")
print(f"FP (False Positives): {FP}")
print(f"FN (False Negatives): {FN}")

# ========== ACCURACY ==========
print("\n" + "=" * 60)
print("ACCURACY")
print("=" * 60)

print("""
Accuracy = (TP + TN) / Total
         = (Correct predictions) / (All predictions)

When to use:
- When classes are balanced
- When all errors are equally bad

When NOT to use:
- Imbalanced datasets
- When one type of error is worse
""")

accuracy = (TP + TN) / (TP + TN + FP + FN)
accuracy_sklearn = accuracy_score(y_true, y_pred)

print(f"Manual calculation: {accuracy:.4f}")
print(f"Sklearn: {accuracy_sklearn:.4f}")

# ========== PRECISION ==========
print("\n" + "=" * 60)
print("PRECISION")
print("=" * 60)

print("""
Precision = TP / (TP + FP)
          = (True Positives) / (All Predicted Positives)

Question: "Of all positive predictions, how many were correct?"

When precision is important:
- Spam detection (don't mark good emails as spam)
- Recommendation systems (users trust recommendations)
- When False Positives are costly

High Precision = Few false alarms
""")

precision = TP / (TP + FP) if (TP + FP) > 0 else 0
precision_sklearn = precision_score(y_true, y_pred)

print(f"Manual calculation: {precision:.4f}")
print(f"Sklearn: {precision_sklearn:.4f}")

# ========== RECALL (SENSITIVITY) ==========
print("\n" + "=" * 60)
print("RECALL (SENSITIVITY)")
print("=" * 60)

print("""
Recall = TP / (TP + FN)
       = (True Positives) / (All Actual Positives)

Question: "Of all actual positives, how many did we find?"

When recall is important:
- Disease detection (don't miss sick patients!)
- Fraud detection (don't miss fraudulent transactions)
- When False Negatives are costly

High Recall = Find most positives (few missed)
""")

recall = TP / (TP + FN) if (TP + FN) > 0 else 0
recall_sklearn = recall_score(y_true, y_pred)

print(f"Manual calculation: {recall:.4f}")
print(f"Sklearn: {recall_sklearn:.4f}")

# ========== PRECISION-RECALL TRADE-OFF ==========
print("\n" + "=" * 60)
print("PRECISION-RECALL TRADE-OFF")
print("=" * 60)

print("""
There's usually a trade-off:
- Higher precision → Lower recall
- Higher recall → Lower precision

Example - Security System:
- Very sensitive (high recall): catches all intruders
  BUT also triggers many false alarms (low precision)
  
- Very strict (high precision): never false alarms
  BUT might miss some intruders (low recall)

Balance depends on your use case!
""")

# ========== F1 SCORE ==========
print("\n" + "=" * 60)
print("F1 SCORE (Harmonic Mean)")
print("=" * 60)

print("""
F1 = 2 * (Precision * Recall) / (Precision + Recall)

- Harmonic mean of precision and recall
- Punishes extreme imbalances
- Range: 0 to 1 (higher is better)

When to use:
- When you need balance between precision and recall
- For imbalanced datasets
- When FP and FN are equally bad

Why harmonic mean?
- Regular average of 0.9 and 0.1 = 0.5
- Harmonic mean of 0.9 and 0.1 = 0.18
- Penalizes when either metric is low!
""")

f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
f1_sklearn = f1_score(y_true, y_pred)

print(f"Manual calculation: {f1:.4f}")
print(f"Sklearn: {f1_sklearn:.4f}")

# ========== REAL-WORLD EXAMPLE ==========
print("\n" + "=" * 60)
print("REAL-WORLD EXAMPLE: Breast Cancer Classification")
print("=" * 60)

# Load data
data = load_breast_cancer()
X, y = data.data, data.target

# Split and scale
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train model
model = LogisticRegression(random_state=42, max_iter=1000)
model.fit(X_train_scaled, y_train)
y_pred = model.predict(X_test_scaled)

# Calculate all metrics
print(f"\nResults for Breast Cancer Classification:")
print("-" * 40)
print(f"Accuracy:  {accuracy_score(y_test, y_pred):.4f}")
print(f"Precision: {precision_score(y_test, y_pred):.4f}")
print(f"Recall:    {recall_score(y_test, y_pred):.4f}")
print(f"F1 Score:  {f1_score(y_test, y_pred):.4f}")

# ========== CLASSIFICATION REPORT ==========
print("\n" + "=" * 60)
print("CLASSIFICATION REPORT (All-in-One)")
print("=" * 60)

print("""
sklearn's classification_report gives you everything:
- Precision, recall, F1 for each class
- Support (number of samples per class)
- Macro average (simple average across classes)
- Weighted average (weighted by support)
""")

print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=data.target_names))

# ========== IMBALANCED DATASET EXAMPLE ==========
print("=" * 60)
print("IMBALANCED DATASET EXAMPLE")
print("=" * 60)

# Create imbalanced dataset
X_imb, y_imb = make_classification(
    n_samples=1000,
    n_features=20,
    n_informative=10,
    n_classes=2,
    weights=[0.95, 0.05],  # 95% class 0, 5% class 1
    random_state=42
)

print(f"Class distribution: {np.bincount(y_imb)}")
print(f"Class 0: {np.sum(y_imb==0)} ({np.sum(y_imb==0)/len(y_imb)*100:.1f}%)")
print(f"Class 1: {np.sum(y_imb==1)} ({np.sum(y_imb==1)/len(y_imb)*100:.1f}%)")

# Split data
X_train_i, X_test_i, y_train_i, y_test_i = train_test_split(
    X_imb, y_imb, test_size=0.2, random_state=42
)

# Model that predicts everything as 0
y_pred_all_0 = np.zeros_like(y_test_i)

print("\n--- Model that predicts all zeros ---")
print(f"Accuracy:  {accuracy_score(y_test_i, y_pred_all_0):.4f} (looks good!)")
print(f"Precision: {precision_score(y_test_i, y_pred_all_0, zero_division=0):.4f}")
print(f"Recall:    {recall_score(y_test_i, y_pred_all_0):.4f} (terrible!)")
print(f"F1 Score:  {f1_score(y_test_i, y_pred_all_0):.4f} (terrible!)")

# Train actual model
scaler_i = StandardScaler()
X_train_i_scaled = scaler_i.fit_transform(X_train_i)
X_test_i_scaled = scaler_i.transform(X_test_i)

model_i = LogisticRegression(random_state=42, max_iter=1000)
model_i.fit(X_train_i_scaled, y_train_i)
y_pred_i = model_i.predict(X_test_i_scaled)

print("\n--- Actual Logistic Regression Model ---")
print(f"Accuracy:  {accuracy_score(y_test_i, y_pred_i):.4f}")
print(f"Precision: {precision_score(y_test_i, y_pred_i):.4f}")
print(f"Recall:    {recall_score(y_test_i, y_pred_i):.4f}")
print(f"F1 Score:  {f1_score(y_test_i, y_pred_i):.4f}")

# ========== MULTICLASS METRICS ==========
print("\n" + "=" * 60)
print("MULTICLASS METRICS")
print("=" * 60)

print("""
For multiclass problems, use 'average' parameter:

- average='micro':    Calculate globally (total TP, FP, FN)
- average='macro':    Calculate per-class, then average
- average='weighted': Calculate per-class, weight by support

Example:
precision_score(y_true, y_pred, average='macro')
""")

from sklearn.datasets import load_iris

iris = load_iris()
X_iris, y_iris = iris.data, iris.target

X_train_m, X_test_m, y_train_m, y_test_m = train_test_split(
    X_iris, y_iris, test_size=0.2, random_state=42
)

model_m = LogisticRegression(random_state=42, max_iter=1000)
model_m.fit(X_train_m, y_train_m)
y_pred_m = model_m.predict(X_test_m)

print("\nMulticlass (Iris) Metrics:")
print("-" * 40)
print(f"Accuracy:           {accuracy_score(y_test_m, y_pred_m):.4f}")
print(f"Precision (macro):  {precision_score(y_test_m, y_pred_m, average='macro'):.4f}")
print(f"Precision (micro):  {precision_score(y_test_m, y_pred_m, average='micro'):.4f}")
print(f"Precision (weighted): {precision_score(y_test_m, y_pred_m, average='weighted'):.4f}")
print(f"Recall (macro):     {recall_score(y_test_m, y_pred_m, average='macro'):.4f}")
print(f"F1 (macro):         {f1_score(y_test_m, y_pred_m, average='macro'):.4f}")

# ========== CHOOSING THE RIGHT METRIC ==========
print("\n" + "=" * 60)
print("CHOOSING THE RIGHT METRIC")
print("=" * 60)

print("""
Use Case                    | Best Metric
----------------------------|------------------
Balanced classes            | Accuracy
Imbalanced classes          | F1 Score
FP is costly (spam)         | Precision
FN is costly (disease)      | Recall
Need overall performance    | F1 Score
Equal classes, all matter   | Macro F1
Imbalanced, all matter      | Weighted F1

Key Questions to Ask:
1. Are classes balanced?
2. Which error type is worse?
3. What does business need?
4. What are the consequences of wrong predictions?
""")

# ========== SUMMARY ==========
print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
┌────────────┬───────────────────────────────────────┐
│ Metric     │ Formula                               │
├────────────┼───────────────────────────────────────┤
│ Accuracy   │ (TP + TN) / Total                     │
│ Precision  │ TP / (TP + FP)                        │
│ Recall     │ TP / (TP + FN)                        │
│ F1 Score   │ 2 * (Precision * Recall) / (P + R)    │
└────────────┴───────────────────────────────────────┘

Remember:
✅ Accuracy can be misleading for imbalanced data
✅ Precision = "How trustworthy are positive predictions?"
✅ Recall = "How complete is our positive detection?"
✅ F1 = Best when you need balance
""")

print("\n" + "=" * 60)
print("✅ Evaluation Metrics - Complete!")
print("=" * 60)
