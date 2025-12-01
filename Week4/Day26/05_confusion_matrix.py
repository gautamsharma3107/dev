"""
Day 26 - Confusion Matrix
==========================
Learn: Understanding and visualizing confusion matrices

Key Concepts:
- Confusion matrix shows all prediction outcomes
- Helps identify where model makes mistakes
- Essential for understanding model performance
- Useful for both binary and multiclass
"""

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_breast_cancer, load_iris, load_digits
from sklearn.metrics import (
    confusion_matrix,
    ConfusionMatrixDisplay,
    classification_report
)
import matplotlib.pyplot as plt

# ========== WHAT IS A CONFUSION MATRIX? ==========
print("=" * 60)
print("WHAT IS A CONFUSION MATRIX?")
print("=" * 60)

print("""
A confusion matrix shows how predictions compare to actual values:

Binary Classification:
                      PREDICTED
                   Neg    |   Pos
                ─────────┼─────────
ACTUAL   Neg   |   TN    |   FP    |  
         Pos   |   FN    |   TP    |  
                ─────────┼─────────

Reading the matrix:
- Diagonal (TN, TP): Correct predictions
- Off-diagonal (FP, FN): Mistakes

Why "Confusion" Matrix?
- It shows where the model gets "confused"!
- High numbers off diagonal = model confusion
""")

# ========== SIMPLE EXAMPLE ==========
print("\n" + "=" * 60)
print("SIMPLE EXAMPLE")
print("=" * 60)

# Create simple predictions
y_true = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])
y_pred = np.array([0, 0, 0, 1, 0, 1, 1, 1, 1, 1])

print("Actual:    ", y_true)
print("Predicted: ", y_pred)

# Create confusion matrix
cm = confusion_matrix(y_true, y_pred)

print("\nConfusion Matrix:")
print(cm)

print("""
Reading this matrix:
[[3, 1],    Row 0: Actual Negative (4 samples)
 [1, 5]]    Row 1: Actual Positive (6 samples)

- [0,0] = 3: TN (correctly predicted negative)
- [0,1] = 1: FP (incorrectly predicted positive)
- [1,0] = 1: FN (incorrectly predicted negative)
- [1,1] = 5: TP (correctly predicted positive)
""")

# Calculate metrics from confusion matrix
TN, FP, FN, TP = cm.ravel()
print(f"TN={TN}, FP={FP}, FN={FN}, TP={TP}")

accuracy = (TP + TN) / (TP + TN + FP + FN)
precision = TP / (TP + FP)
recall = TP / (TP + FN)

print(f"\nFrom confusion matrix:")
print(f"Accuracy:  {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall:    {recall:.4f}")

# ========== VISUALIZING CONFUSION MATRIX ==========
print("\n" + "=" * 60)
print("VISUALIZING CONFUSION MATRIX")
print("=" * 60)

print("""
Visualization makes patterns easier to see:
- Darker colors = higher counts
- Perfect model = dark diagonal, light off-diagonal
""")

# Create visualization
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Raw counts
disp1 = ConfusionMatrixDisplay(cm, display_labels=['Negative', 'Positive'])
disp1.plot(ax=axes[0], cmap='Blues')
axes[0].set_title('Confusion Matrix (Counts)')

# Normalized (percentages)
cm_normalized = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
disp2 = ConfusionMatrixDisplay(cm_normalized, display_labels=['Negative', 'Positive'])
disp2.plot(ax=axes[1], cmap='Blues', values_format='.2%')
axes[1].set_title('Confusion Matrix (Normalized)')

plt.tight_layout()
plt.savefig('/tmp/confusion_matrix_simple.png', dpi=150, bbox_inches='tight')
plt.close()

print("✅ Saved visualization to /tmp/confusion_matrix_simple.png")

# ========== REAL-WORLD EXAMPLE: BREAST CANCER ==========
print("\n" + "=" * 60)
print("REAL-WORLD EXAMPLE: Breast Cancer Detection")
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

# Create confusion matrix
cm_cancer = confusion_matrix(y_test, y_pred)

print("Confusion Matrix:")
print(cm_cancer)

# Interpret
TN, FP, FN, TP = cm_cancer.ravel()
print(f"""
Interpretation (Cancer Detection):
- TN ({TN}): Correctly identified as benign (no cancer)
- FP ({FP}): Benign incorrectly diagnosed as malignant
- FN ({FN}): Malignant missed (diagnosed as benign) - DANGEROUS!
- TP ({TP}): Correctly identified as malignant (cancer)

In medical diagnosis:
- FN (False Negatives) are critical - missing cancer!
- We want high recall (catch all cancer cases)
""")

# Visualize
fig, ax = plt.subplots(figsize=(8, 6))
disp = ConfusionMatrixDisplay(cm_cancer, display_labels=data.target_names)
disp.plot(ax=ax, cmap='Blues')
ax.set_title('Breast Cancer Classification - Confusion Matrix')
plt.tight_layout()
plt.savefig('/tmp/confusion_matrix_cancer.png', dpi=150, bbox_inches='tight')
plt.close()

print("\n✅ Saved to /tmp/confusion_matrix_cancer.png")

print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=data.target_names))

# ========== MULTICLASS CONFUSION MATRIX ==========
print("=" * 60)
print("MULTICLASS CONFUSION MATRIX (Iris)")
print("=" * 60)

# Load Iris data
iris = load_iris()
X_iris, y_iris = iris.data, iris.target

X_train_i, X_test_i, y_train_i, y_test_i = train_test_split(
    X_iris, y_iris, test_size=0.2, random_state=42
)

# Train model
model_iris = LogisticRegression(random_state=42, max_iter=1000)
model_iris.fit(X_train_i, y_train_i)
y_pred_i = model_iris.predict(X_test_i)

# Create confusion matrix
cm_iris = confusion_matrix(y_test_i, y_pred_i)

print("Confusion Matrix (3 classes):")
print(cm_iris)

print("""
Reading multiclass confusion matrix:
- Rows = Actual classes
- Columns = Predicted classes
- Diagonal = Correct predictions
- Off-diagonal = Mistakes between classes

Example: cm[0,1] = predicted class 1 when actual was class 0
""")

# Visualize
fig, ax = plt.subplots(figsize=(8, 6))
disp_iris = ConfusionMatrixDisplay(cm_iris, display_labels=iris.target_names)
disp_iris.plot(ax=ax, cmap='Blues')
ax.set_title('Iris Classification - Confusion Matrix')
plt.tight_layout()
plt.savefig('/tmp/confusion_matrix_iris.png', dpi=150, bbox_inches='tight')
plt.close()

print("\n✅ Saved to /tmp/confusion_matrix_iris.png")

print("\nClassification Report:")
print(classification_report(y_test_i, y_pred_i, target_names=iris.target_names))

# ========== COMMON PATTERNS IN CONFUSION MATRICES ==========
print("\n" + "=" * 60)
print("COMMON PATTERNS IN CONFUSION MATRICES")
print("=" * 60)

print("""
1. PERFECT CLASSIFIER:
   [[50,  0],
    [ 0, 50]]
   → All predictions on diagonal

2. BIASED CLASSIFIER (predicts all positive):
   [[ 0, 50],
    [ 0, 50]]
   → One column has all predictions

3. RANDOM CLASSIFIER:
   [[25, 25],
    [25, 25]]
   → Uniform distribution

4. CONFUSED BETWEEN TWO CLASSES (multiclass):
   [[50,  0,  0],
    [ 0, 40, 10],
    [ 0, 15, 35]]
   → Class 1 and 2 often confused

Look for patterns to understand model weaknesses!
""")

# ========== NORMALIZED CONFUSION MATRIX ==========
print("=" * 60)
print("NORMALIZED CONFUSION MATRIX")
print("=" * 60)

print("""
Normalize by:
- 'true': Divide by sum of each row (actual class)
- 'pred': Divide by sum of each column (predicted class)
- 'all': Divide by total

Normalization helps when classes are imbalanced.
""")

# Create normalized matrices
cm_true = confusion_matrix(y_test_i, y_pred_i, normalize='true')
cm_pred = confusion_matrix(y_test_i, y_pred_i, normalize='pred')

print("Normalized by true (row-wise):")
print(np.round(cm_true, 3))

print("\nNormalized by predicted (column-wise):")
print(np.round(cm_pred, 3))

# ========== COMPARING MODELS ==========
print("\n" + "=" * 60)
print("COMPARING MODELS WITH CONFUSION MATRICES")
print("=" * 60)

# Load breast cancer data again
X_train_bc, X_test_bc, y_train_bc, y_test_bc = train_test_split(
    load_breast_cancer().data,
    load_breast_cancer().target,
    test_size=0.2,
    random_state=42
)

# Scale for logistic regression
scaler_bc = StandardScaler()
X_train_bc_scaled = scaler_bc.fit_transform(X_train_bc)
X_test_bc_scaled = scaler_bc.transform(X_test_bc)

# Train two models
lr = LogisticRegression(random_state=42, max_iter=1000)
rf = RandomForestClassifier(n_estimators=100, random_state=42)

lr.fit(X_train_bc_scaled, y_train_bc)
rf.fit(X_train_bc, y_train_bc)

y_pred_lr = lr.predict(X_test_bc_scaled)
y_pred_rf = rf.predict(X_test_bc)

# Compare confusion matrices
cm_lr = confusion_matrix(y_test_bc, y_pred_lr)
cm_rf = confusion_matrix(y_test_bc, y_pred_rf)

print("Logistic Regression:")
print(cm_lr)

print("\nRandom Forest:")
print(cm_rf)

# Visualize side by side
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

disp_lr = ConfusionMatrixDisplay(cm_lr, display_labels=['Benign', 'Malignant'])
disp_lr.plot(ax=axes[0], cmap='Blues')
axes[0].set_title('Logistic Regression')

disp_rf = ConfusionMatrixDisplay(cm_rf, display_labels=['Benign', 'Malignant'])
disp_rf.plot(ax=axes[1], cmap='Greens')
axes[1].set_title('Random Forest')

plt.tight_layout()
plt.savefig('/tmp/confusion_matrix_comparison.png', dpi=150, bbox_inches='tight')
plt.close()

print("\n✅ Saved comparison to /tmp/confusion_matrix_comparison.png")

# ========== LARGE MULTICLASS (DIGITS) ==========
print("\n" + "=" * 60)
print("LARGE MULTICLASS EXAMPLE (Digits 0-9)")
print("=" * 60)

# Load digits dataset
digits = load_digits()
X_dig, y_dig = digits.data, digits.target

X_train_d, X_test_d, y_train_d, y_test_d = train_test_split(
    X_dig, y_dig, test_size=0.2, random_state=42
)

# Train model
model_dig = RandomForestClassifier(n_estimators=100, random_state=42)
model_dig.fit(X_train_d, y_train_d)
y_pred_d = model_dig.predict(X_test_d)

# Create confusion matrix
cm_dig = confusion_matrix(y_test_d, y_pred_d)

print("Confusion Matrix shape:", cm_dig.shape)
print("\nConfusion Matrix (10 classes):")
print(cm_dig)

# Visualize
fig, ax = plt.subplots(figsize=(10, 8))
disp_dig = ConfusionMatrixDisplay(cm_dig, display_labels=digits.target_names)
disp_dig.plot(ax=ax, cmap='Blues', values_format='d')
ax.set_title('Digit Classification (0-9) - Confusion Matrix')
plt.tight_layout()
plt.savefig('/tmp/confusion_matrix_digits.png', dpi=150, bbox_inches='tight')
plt.close()

print("\n✅ Saved to /tmp/confusion_matrix_digits.png")

# Find most confused pairs
print("\nMost confused digit pairs:")
np.fill_diagonal(cm_dig, 0)  # Remove diagonal
for _ in range(5):
    i, j = np.unravel_index(np.argmax(cm_dig), cm_dig.shape)
    if cm_dig[i, j] > 0:
        print(f"  Actual {i} predicted as {j}: {cm_dig[i, j]} times")
        cm_dig[i, j] = 0

# ========== PRACTICAL TIPS ==========
print("\n" + "=" * 60)
print("PRACTICAL TIPS")
print("=" * 60)

print("""
1. Always visualize confusion matrices
2. Use normalized version for imbalanced data
3. Focus on off-diagonal elements (mistakes)
4. Identify which classes are confused
5. Use insights to improve model:
   - Add more data for confused classes
   - Engineer features to distinguish confused classes
   - Use class weights for imbalanced data
6. Consider cost of different errors
7. Report along with precision, recall, F1
""")

# ========== SUMMARY ==========
print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
Confusion Matrix:
┌──────────────────────────────────────────────────────┐
│ Binary:                                              │
│                  Predicted                           │
│               Neg    |   Pos                         │
│        Neg   TN      |   FP     → Specificity row    │
│ Actual Pos   FN      |   TP     → Recall row         │
│               ↓          ↓                           │
│            NPV     Precision                         │
└──────────────────────────────────────────────────────┘

Key Insights:
- Diagonal = Correct predictions (want HIGH)
- Off-diagonal = Errors (want LOW)
- Row sums = Actual class counts
- Column sums = Predicted class counts
- Use .ravel() to get TN, FP, FN, TP

Code:
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
cm = confusion_matrix(y_true, y_pred)
ConfusionMatrixDisplay(cm).plot()
""")

print("\n" + "=" * 60)
print("✅ Confusion Matrix - Complete!")
print("=" * 60)
