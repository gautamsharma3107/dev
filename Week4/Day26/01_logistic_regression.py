"""
Day 26 - Logistic Regression
=============================
Learn: Binary and multiclass classification with logistic regression

Key Concepts:
- Logistic regression predicts probabilities (0 to 1)
- Uses sigmoid function to transform outputs
- Great for binary classification
- Can handle multiclass with one-vs-rest
"""

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_breast_cancer, load_iris
from sklearn.metrics import accuracy_score, classification_report

# ========== WHAT IS LOGISTIC REGRESSION? ==========
print("=" * 60)
print("WHAT IS LOGISTIC REGRESSION?")
print("=" * 60)

print("""
Logistic Regression is used for CLASSIFICATION, not regression!

Why "Regression" in the name?
- It uses a regression technique internally
- But outputs probabilities for classification

How it works:
1. Linear combination: z = w1*x1 + w2*x2 + ... + b
2. Sigmoid function: P(y=1) = 1 / (1 + e^(-z))
3. If P > 0.5, predict class 1, else class 0

Use cases:
- Spam detection
- Disease diagnosis
- Customer churn prediction
- Credit risk assessment
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
print(f"Class distribution: {np.bincount(y)}")

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"\nTraining samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")

# ========== FEATURE SCALING ==========
print("\n" + "=" * 60)
print("FEATURE SCALING (Important!)")
print("=" * 60)

print("""
Logistic regression is sensitive to feature scales!
Always scale your features before training.
""")

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("✅ Features scaled using StandardScaler")
print(f"Mean after scaling: {X_train_scaled.mean():.4f}")
print(f"Std after scaling: {X_train_scaled.std():.4f}")

# ========== TRAINING THE MODEL ==========
print("\n" + "=" * 60)
print("TRAINING LOGISTIC REGRESSION")
print("=" * 60)

# Create and train model
model = LogisticRegression(random_state=42)
model.fit(X_train_scaled, y_train)

print("✅ Model trained!")
print(f"Coefficients shape: {model.coef_.shape}")
print(f"Intercept: {model.intercept_[0]:.4f}")

# ========== MAKING PREDICTIONS ==========
print("\n" + "=" * 60)
print("MAKING PREDICTIONS")
print("=" * 60)

# Predict classes
y_pred = model.predict(X_test_scaled)

# Predict probabilities
y_proba = model.predict_proba(X_test_scaled)

print("First 5 predictions:")
print("-" * 40)
for i in range(5):
    print(f"Sample {i+1}:")
    print(f"  Predicted class: {y_pred[i]} ({target_names[y_pred[i]]})")
    print(f"  Actual class: {y_test[i]} ({target_names[y_test[i]]})")
    print(f"  Probabilities: {y_proba[i]}")
    print()

# ========== EVALUATING THE MODEL ==========
print("=" * 60)
print("MODEL EVALUATION")
print("=" * 60)

accuracy = accuracy_score(y_test, y_pred)
print(f"\nAccuracy: {accuracy:.4f} ({accuracy*100:.1f}%)")

print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=target_names))

# ========== UNDERSTANDING COEFFICIENTS ==========
print("=" * 60)
print("UNDERSTANDING COEFFICIENTS")
print("=" * 60)

print("""
In logistic regression, coefficients tell us:
- Positive coefficient: increases probability of positive class
- Negative coefficient: decreases probability of positive class
- Larger magnitude = stronger influence
""")

# Get top features by absolute coefficient value
coef = model.coef_[0]
feature_importance = list(zip(feature_names, coef))
feature_importance.sort(key=lambda x: abs(x[1]), reverse=True)

print("Top 5 most influential features:")
for name, coef_value in feature_importance[:5]:
    direction = "increases" if coef_value > 0 else "decreases"
    print(f"  {name}: {coef_value:.4f} ({direction} malignant probability)")

# ========== MULTICLASS CLASSIFICATION ==========
print("\n" + "=" * 60)
print("MULTICLASS CLASSIFICATION (Iris Dataset)")
print("=" * 60)

# Load Iris dataset (3 classes)
iris = load_iris()
X_iris, y_iris = iris.data, iris.target

print(f"Dataset shape: {X_iris.shape}")
print(f"Classes: {iris.target_names}")

# Split and scale
X_train_i, X_test_i, y_train_i, y_test_i = train_test_split(
    X_iris, y_iris, test_size=0.2, random_state=42
)

scaler_i = StandardScaler()
X_train_i_scaled = scaler_i.fit_transform(X_train_i)
X_test_i_scaled = scaler_i.transform(X_test_i)

# Train multiclass model
model_multi = LogisticRegression(multi_class='multinomial', random_state=42)
model_multi.fit(X_train_i_scaled, y_train_i)

# Evaluate
y_pred_i = model_multi.predict(X_test_i_scaled)
accuracy_i = accuracy_score(y_test_i, y_pred_i)

print(f"\nMulticlass Accuracy: {accuracy_i:.4f}")
print("\nClassification Report:")
print(classification_report(y_test_i, y_pred_i, target_names=iris.target_names))

# ========== HYPERPARAMETERS ==========
print("=" * 60)
print("IMPORTANT HYPERPARAMETERS")
print("=" * 60)

print("""
LogisticRegression key parameters:

1. C (default=1.0):
   - Inverse of regularization strength
   - Smaller C = stronger regularization
   - Helps prevent overfitting

2. penalty (default='l2'):
   - 'l1' = Lasso (can zero out features)
   - 'l2' = Ridge (shrinks coefficients)
   - 'elasticnet' = Both

3. solver (default='lbfgs'):
   - 'lbfgs' = Good for small datasets
   - 'sag', 'saga' = Good for large datasets
   - 'liblinear' = Good for L1 penalty

4. max_iter (default=100):
   - Maximum iterations for convergence
   - Increase if you get convergence warnings
""")

# Example with different C values
print("\nEffect of C (regularization strength):")
for c_val in [0.01, 0.1, 1.0, 10.0]:
    model_c = LogisticRegression(C=c_val, random_state=42, max_iter=1000)
    model_c.fit(X_train_scaled, y_train)
    score = model_c.score(X_test_scaled, y_test)
    print(f"  C={c_val:5.2f}: Accuracy = {score:.4f}")

# ========== PRACTICAL TIPS ==========
print("\n" + "=" * 60)
print("PRACTICAL TIPS")
print("=" * 60)

print("""
1. Always scale your features
2. Check for class imbalance
3. Use class_weight='balanced' for imbalanced data
4. Start with default parameters
5. Use cross-validation for parameter tuning
6. Check convergence warnings
""")

# Example with class weights
print("\nUsing class_weight='balanced':")
model_balanced = LogisticRegression(class_weight='balanced', random_state=42)
model_balanced.fit(X_train_scaled, y_train)
score_balanced = model_balanced.score(X_test_scaled, y_test)
print(f"Accuracy with balanced weights: {score_balanced:.4f}")

print("\n" + "=" * 60)
print("✅ Logistic Regression - Complete!")
print("=" * 60)
