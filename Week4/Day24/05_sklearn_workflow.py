"""
Day 24 - Scikit-learn Workflow
===============================
Learn: Complete ML workflow using scikit-learn

Key Concepts:
- End-to-end ML pipeline
- Loading datasets
- Training and evaluating models
- Making predictions
- Building your first ML model
"""

import numpy as np

# ========== SCIKIT-LEARN INTRODUCTION ==========
print("=" * 60)
print("SCIKIT-LEARN (sklearn)")
print("=" * 60)

sklearn_intro = """
Scikit-learn is THE most popular ML library in Python!

Features:
- Consistent API across all algorithms
- Extensive documentation
- Built-in datasets for practice
- Tools for preprocessing, evaluation, selection

Installation: pip install scikit-learn

The API pattern is always:
1. Import the algorithm
2. Create instance: model = Algorithm()
3. Train: model.fit(X_train, y_train)
4. Predict: predictions = model.predict(X_test)
5. Evaluate: score = model.score(X_test, y_test)
"""
print(sklearn_intro)

# ========== LOADING BUILT-IN DATASETS ==========
print("\n" + "=" * 60)
print("LOADING BUILT-IN DATASETS")
print("=" * 60)

from sklearn.datasets import load_iris, load_wine

# Load Iris dataset (most famous ML dataset!)
iris = load_iris()

print("IRIS Dataset (Classification):")
print("-" * 50)
print(f"Features: {iris.feature_names}")
print(f"Target classes: {iris.target_names}")
print(f"Data shape: {iris.data.shape}")
print(f"Target shape: {iris.target.shape}")
print(f"\nFirst 3 samples:")
for i in range(3):
    print(f"  Sample {i+1}: {iris.data[i]} → {iris.target_names[iris.target[i]]}")

# ========== COMPLETE ML WORKFLOW ==========
print("\n" + "=" * 60)
print("COMPLETE ML WORKFLOW")
print("=" * 60)

workflow_steps = """
Step 1: Load and explore data
Step 2: Split into train/test sets
Step 3: Scale features (if needed)
Step 4: Choose and create model
Step 5: Train model
Step 6: Make predictions
Step 7: Evaluate model
Step 8: Tune and improve (optional)
"""
print(workflow_steps)

# ========== STEP 1: LOAD DATA ==========
print("\n" + "-" * 60)
print("STEP 1: Load and Explore Data")
print("-" * 60)

X = iris.data
y = iris.target

print(f"Features (X): {X.shape[0]} samples, {X.shape[1]} features")
print(f"Target (y): {y.shape[0]} labels")
print(f"Classes: {np.unique(y)} → {iris.target_names}")
print(f"\nClass distribution:")
for i, name in enumerate(iris.target_names):
    print(f"  {name}: {np.sum(y == i)} samples")

# ========== STEP 2: SPLIT DATA ==========
print("\n" + "-" * 60)
print("STEP 2: Split Data")
print("-" * 60)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=0.2, 
    random_state=42,
    stratify=y  # Maintain class balance
)

print(f"Training samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")
print(f"Training class distribution: {np.bincount(y_train)}")
print(f"Testing class distribution: {np.bincount(y_test)}")

# ========== STEP 3: SCALE FEATURES ==========
print("\n" + "-" * 60)
print("STEP 3: Scale Features")
print("-" * 60)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("Before scaling:")
print(f"  X_train mean: {X_train.mean(axis=0).round(2)}")
print(f"  X_train std: {X_train.std(axis=0).round(2)}")

print("\nAfter scaling:")
print(f"  X_train_scaled mean: {X_train_scaled.mean(axis=0).round(10)}")
print(f"  X_train_scaled std: {X_train_scaled.std(axis=0).round(2)}")

# ========== STEP 4: CREATE MODEL ==========
print("\n" + "-" * 60)
print("STEP 4: Create Model")
print("-" * 60)

from sklearn.linear_model import LogisticRegression

# Create model instance
model = LogisticRegression(random_state=42, max_iter=200)

print("Model: Logistic Regression")
print("This is a classification algorithm that predicts probabilities.")
print(f"Model parameters: {model.get_params()}")

# ========== STEP 5: TRAIN MODEL ==========
print("\n" + "-" * 60)
print("STEP 5: Train Model")
print("-" * 60)

# Fit model to training data
model.fit(X_train_scaled, y_train)

print("Model training complete!")
print("The model has learned patterns from the training data.")
print(f"Model coefficients shape: {model.coef_.shape}")

# ========== STEP 6: MAKE PREDICTIONS ==========
print("\n" + "-" * 60)
print("STEP 6: Make Predictions")
print("-" * 60)

# Predict on test data
y_pred = model.predict(X_test_scaled)

print("Predictions vs Actual (first 10 samples):")
print("-" * 50)
print("Sample | Predicted | Actual | Correct?")
print("-" * 50)
for i in range(10):
    correct = "✅" if y_pred[i] == y_test[i] else "❌"
    print(f"  {i+1:2}   |     {y_pred[i]}     |   {y_test[i]}    |    {correct}")

# Get prediction probabilities
y_proba = model.predict_proba(X_test_scaled)
print(f"\nPrediction probabilities for first sample:")
print(f"  Classes: {iris.target_names}")
print(f"  Probabilities: {y_proba[0].round(3)}")
print(f"  Predicted class: {iris.target_names[y_pred[0]]}")

# ========== STEP 7: EVALUATE MODEL ==========
print("\n" + "-" * 60)
print("STEP 7: Evaluate Model")
print("-" * 60)

from sklearn.metrics import (
    accuracy_score, 
    precision_score, 
    recall_score, 
    f1_score,
    confusion_matrix,
    classification_report
)

# Basic accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2%}")

# Using model's built-in score method
score = model.score(X_test_scaled, y_test)
print(f"Model score: {score:.2%}")

# Detailed metrics
print("\nDetailed Metrics:")
print(f"Precision (weighted): {precision_score(y_test, y_pred, average='weighted'):.2%}")
print(f"Recall (weighted): {recall_score(y_test, y_pred, average='weighted'):.2%}")
print(f"F1 Score (weighted): {f1_score(y_test, y_pred, average='weighted'):.2%}")

# Confusion matrix
print("\nConfusion Matrix:")
cm = confusion_matrix(y_test, y_pred)
print(cm)
print(f"\nInterpretation:")
print(f"  - Diagonal: Correct predictions")
print(f"  - Off-diagonal: Misclassifications")

# Classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

# ========== TRYING DIFFERENT ALGORITHMS ==========
print("\n" + "=" * 60)
print("TRYING DIFFERENT ALGORITHMS")
print("=" * 60)

from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

algorithms = [
    ("Logistic Regression", LogisticRegression(random_state=42, max_iter=200)),
    ("K-Nearest Neighbors", KNeighborsClassifier(n_neighbors=5)),
    ("Decision Tree", DecisionTreeClassifier(random_state=42)),
    ("Random Forest", RandomForestClassifier(random_state=42, n_estimators=100)),
    ("SVM", SVC(random_state=42)),
]

print("Comparing different algorithms on Iris dataset:")
print("-" * 50)
print(f"{'Algorithm':<25} | Accuracy")
print("-" * 50)

for name, algo in algorithms:
    algo.fit(X_train_scaled, y_train)
    acc = algo.score(X_test_scaled, y_test)
    print(f"{name:<25} | {acc:.2%}")

# ========== MAKING PREDICTIONS ON NEW DATA ==========
print("\n" + "=" * 60)
print("MAKING PREDICTIONS ON NEW DATA")
print("=" * 60)

# Simulate new flower measurements
new_flower = np.array([[5.1, 3.5, 1.4, 0.2]])  # Sepal/petal measurements
print(f"New flower measurements: {new_flower[0]}")
print(f"Features: {iris.feature_names}")

# Scale using the same scaler
new_flower_scaled = scaler.transform(new_flower)

# Predict
prediction = model.predict(new_flower_scaled)
probabilities = model.predict_proba(new_flower_scaled)

print(f"\nPrediction: {iris.target_names[prediction[0]]}")
print(f"Probabilities:")
for i, name in enumerate(iris.target_names):
    print(f"  {name}: {probabilities[0][i]:.1%}")

# ========== CROSS-VALIDATION ==========
print("\n" + "=" * 60)
print("CROSS-VALIDATION FOR BETTER EVALUATION")
print("=" * 60)

from sklearn.model_selection import cross_val_score

# 5-fold cross-validation
cv_scores = cross_val_score(model, X_train_scaled, y_train, cv=5)

print("5-Fold Cross-Validation Results:")
print(f"Scores: {cv_scores.round(3)}")
print(f"Mean accuracy: {cv_scores.mean():.2%}")
print(f"Standard deviation: {cv_scores.std():.2%}")
print(f"\nFinal result: {cv_scores.mean():.2%} (+/- {cv_scores.std() * 2:.2%})")

# ========== SAVING AND LOADING MODELS ==========
print("\n" + "=" * 60)
print("SAVING AND LOADING MODELS")
print("=" * 60)

import joblib
import os

save_info = """
For production, save both the model AND the scaler!

import joblib

# Save model and scaler
joblib.dump(model, 'model.pkl')
joblib.dump(scaler, 'scaler.pkl')

# Load model and scaler
loaded_model = joblib.load('model.pkl')
loaded_scaler = joblib.load('scaler.pkl')

# Use for predictions
X_new_scaled = loaded_scaler.transform(X_new)
predictions = loaded_model.predict(X_new_scaled)
"""
print(save_info)

# Demonstrate saving (to temp directory)
temp_dir = '/tmp/ml_demo'
os.makedirs(temp_dir, exist_ok=True)

model_path = os.path.join(temp_dir, 'iris_model.pkl')
scaler_path = os.path.join(temp_dir, 'iris_scaler.pkl')

joblib.dump(model, model_path)
joblib.dump(scaler, scaler_path)

print(f"Model saved to: {model_path}")
print(f"Scaler saved to: {scaler_path}")

# Load and verify
loaded_model = joblib.load(model_path)
loaded_scaler = joblib.load(scaler_path)

# Test loaded model
test_pred = loaded_model.predict(loaded_scaler.transform(new_flower))
print(f"\nLoaded model prediction: {iris.target_names[test_pred[0]]}")
print("✅ Model successfully saved and loaded!")

# Clean up
os.remove(model_path)
os.remove(scaler_path)

# ========== COMPLETE WORKFLOW SUMMARY ==========
print("\n" + "=" * 60)
print("COMPLETE WORKFLOW SUMMARY")
print("=" * 60)

summary_code = """
# COMPLETE ML WORKFLOW TEMPLATE

# 1. Import libraries
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib

# 2. Load data
from sklearn.datasets import load_iris
data = load_iris()
X, y = data.data, data.target

# 3. Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 4. Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 5. Create and train model
model = LogisticRegression(random_state=42)
model.fit(X_train_scaled, y_train)

# 6. Evaluate
y_pred = model.predict(X_test_scaled)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2%}")
print(classification_report(y_test, y_pred))

# 7. Cross-validation
cv_scores = cross_val_score(model, X_train_scaled, y_train, cv=5)
print(f"CV Accuracy: {cv_scores.mean():.2%} (+/- {cv_scores.std()*2:.2%})")

# 8. Save model
joblib.dump(model, 'model.pkl')
joblib.dump(scaler, 'scaler.pkl')

# 9. Use in production
loaded_model = joblib.load('model.pkl')
loaded_scaler = joblib.load('scaler.pkl')
new_prediction = loaded_model.predict(loaded_scaler.transform(X_new))
"""
print(summary_code)

print("\n" + "=" * 60)
print("🎉 Congratulations! You've built your first ML model!")
print("=" * 60)
print("""
What you learned today:
✅ What Machine Learning is
✅ Supervised vs Unsupervised Learning
✅ Train-Test Split
✅ Feature Scaling
✅ Complete Scikit-learn Workflow
✅ Building and evaluating a classification model

Next steps:
→ Day 25: Regression Models
→ Day 26: Classification Models (in depth)
→ Day 27: Unsupervised Learning
""")
