"""
Day 26 - Mini Project: Heart Disease Classification
====================================================
Build an end-to-end classification pipeline to predict heart disease

This project covers:
- Data loading and exploration
- Feature analysis
- Model training (multiple algorithms)
- Model evaluation and comparison
- Confusion matrix analysis
- Feature importance
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
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

print("=" * 70)
print("MINI PROJECT: Heart Disease Classification")
print("=" * 70)

# ============================================================
# PART 1: DATA LOADING AND EXPLORATION
# ============================================================
print("\n" + "=" * 70)
print("PART 1: DATA LOADING AND EXPLORATION")
print("=" * 70)

# We'll create a synthetic heart disease dataset
# In real projects, you would load from CSV: pd.read_csv('heart.csv')
np.random.seed(42)

n_samples = 1000

# Features (inspired by real heart disease datasets)
data = {
    'age': np.random.normal(55, 10, n_samples).astype(int),
    'sex': np.random.binomial(1, 0.65, n_samples),  # 65% male
    'chest_pain': np.random.randint(0, 4, n_samples),
    'resting_bp': np.random.normal(130, 20, n_samples),
    'cholesterol': np.random.normal(245, 50, n_samples),
    'fasting_bs': np.random.binomial(1, 0.15, n_samples),  # 15% high
    'resting_ecg': np.random.randint(0, 3, n_samples),
    'max_hr': np.random.normal(150, 20, n_samples),
    'exercise_angina': np.random.binomial(1, 0.33, n_samples),
    'oldpeak': np.abs(np.random.normal(1, 1.5, n_samples)),
    'st_slope': np.random.randint(0, 3, n_samples),
}

df = pd.DataFrame(data)

# Create target based on features (simplified relationship)
risk_score = (
    0.03 * df['age'] +
    0.5 * df['sex'] +
    0.3 * df['chest_pain'] +
    0.01 * df['resting_bp'] +
    0.002 * df['cholesterol'] +
    0.5 * df['fasting_bs'] +
    0.2 * df['resting_ecg'] -
    0.02 * df['max_hr'] +
    0.8 * df['exercise_angina'] +
    0.4 * df['oldpeak'] +
    0.3 * df['st_slope'] +
    np.random.normal(0, 1, n_samples)
)

df['heart_disease'] = (risk_score > risk_score.median()).astype(int)

print(f"Dataset shape: {df.shape}")
print(f"\nFirst 5 rows:")
print(df.head())

print(f"\nFeature statistics:")
print(df.describe().round(2))

print(f"\nTarget distribution:")
print(df['heart_disease'].value_counts())
print(f"Heart Disease: {df['heart_disease'].mean()*100:.1f}%")

# ============================================================
# PART 2: DATA PREPARATION
# ============================================================
print("\n" + "=" * 70)
print("PART 2: DATA PREPARATION")
print("=" * 70)

# Separate features and target
X = df.drop('heart_disease', axis=1)
y = df['heart_disease']

feature_names = X.columns.tolist()
print(f"Features ({len(feature_names)}): {feature_names}")

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"\nTraining samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")
print(f"Train class distribution: {np.bincount(y_train)}")
print(f"Test class distribution: {np.bincount(y_test)}")

# Scale features (important for Logistic Regression)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("\n✅ Data prepared and scaled")

# ============================================================
# PART 3: MODEL TRAINING
# ============================================================
print("\n" + "=" * 70)
print("PART 3: MODEL TRAINING")
print("=" * 70)

# Define models
models = {
    'Logistic Regression': LogisticRegression(random_state=42, max_iter=1000),
    'Decision Tree': DecisionTreeClassifier(max_depth=5, random_state=42),
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42)
}

# Store results
results = {}

for name, model in models.items():
    print(f"\n--- Training {name} ---")
    
    # Use scaled data for Logistic Regression, original for trees
    X_tr = X_train_scaled if 'Logistic' in name else X_train
    X_te = X_test_scaled if 'Logistic' in name else X_test
    
    # Train
    model.fit(X_tr, y_train)
    
    # Predict
    y_pred = model.predict(X_te)
    
    # Calculate metrics
    results[name] = {
        'model': model,
        'y_pred': y_pred,
        'accuracy': accuracy_score(y_test, y_pred),
        'precision': precision_score(y_test, y_pred),
        'recall': recall_score(y_test, y_pred),
        'f1': f1_score(y_test, y_pred),
        'confusion_matrix': confusion_matrix(y_test, y_pred)
    }
    
    print(f"✅ {name} trained successfully")

# ============================================================
# PART 4: MODEL COMPARISON
# ============================================================
print("\n" + "=" * 70)
print("PART 4: MODEL COMPARISON")
print("=" * 70)

print("\n" + "-" * 70)
print(f"{'Model':<25} {'Accuracy':<12} {'Precision':<12} {'Recall':<12} {'F1 Score':<12}")
print("-" * 70)

for name, res in results.items():
    print(f"{name:<25} {res['accuracy']:<12.4f} {res['precision']:<12.4f} "
          f"{res['recall']:<12.4f} {res['f1']:<12.4f}")

print("-" * 70)

# Find best model
best_model_name = max(results, key=lambda x: results[x]['f1'])
print(f"\n🏆 Best Model (by F1 Score): {best_model_name}")

# ============================================================
# PART 5: CROSS-VALIDATION
# ============================================================
print("\n" + "=" * 70)
print("PART 5: CROSS-VALIDATION (5-Fold)")
print("=" * 70)

for name, model in models.items():
    X_data = scaler.fit_transform(X) if 'Logistic' in name else X
    scores = cross_val_score(model, X_data, y, cv=5, scoring='f1')
    print(f"{name:<25}: F1 = {scores.mean():.4f} (+/- {scores.std()*2:.4f})")

# ============================================================
# PART 6: CONFUSION MATRIX ANALYSIS
# ============================================================
print("\n" + "=" * 70)
print("PART 6: CONFUSION MATRIX ANALYSIS")
print("=" * 70)

# Create visualization for all models
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

for ax, (name, res) in zip(axes, results.items()):
    cm = res['confusion_matrix']
    disp = ConfusionMatrixDisplay(cm, display_labels=['No Disease', 'Disease'])
    disp.plot(ax=ax, cmap='Blues')
    ax.set_title(f'{name}\nF1: {res["f1"]:.4f}')

plt.tight_layout()
plt.savefig('/tmp/heart_disease_confusion_matrices.png', dpi=150, bbox_inches='tight')
plt.close()

print("✅ Confusion matrices saved to /tmp/heart_disease_confusion_matrices.png")

# Detailed analysis of best model
best_res = results[best_model_name]
cm = best_res['confusion_matrix']
TN, FP, FN, TP = cm.ravel()

print(f"\n--- {best_model_name} Detailed Analysis ---")
print(f"\nConfusion Matrix:")
print(cm)
print(f"""
True Negatives (TN):  {TN} - Correctly predicted NO disease
False Positives (FP): {FP} - Incorrectly predicted disease (false alarm)
False Negatives (FN): {FN} - Incorrectly predicted NO disease (MISSED!)
True Positives (TP):  {TP} - Correctly predicted disease

In medical context:
- FN is critical! Missing a heart disease case is dangerous.
- High recall is important for disease detection.
""")

# ============================================================
# PART 7: FEATURE IMPORTANCE
# ============================================================
print("\n" + "=" * 70)
print("PART 7: FEATURE IMPORTANCE")
print("=" * 70)

# Get feature importance from Random Forest
rf_model = results['Random Forest']['model']
importances = rf_model.feature_importances_

# Sort by importance
importance_df = pd.DataFrame({
    'feature': feature_names,
    'importance': importances
}).sort_values('importance', ascending=False)

print("\nFeature Importance (Random Forest):")
print("-" * 40)
for _, row in importance_df.iterrows():
    bar = "█" * int(row['importance'] * 50)
    print(f"{row['feature']:15s}: {row['importance']:.4f} {bar}")

# Visualize
plt.figure(figsize=(10, 6))
plt.barh(importance_df['feature'], importance_df['importance'], color='steelblue')
plt.xlabel('Importance')
plt.ylabel('Feature')
plt.title('Feature Importance for Heart Disease Prediction')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig('/tmp/heart_disease_feature_importance.png', dpi=150, bbox_inches='tight')
plt.close()

print("\n✅ Feature importance chart saved to /tmp/heart_disease_feature_importance.png")

# ============================================================
# PART 8: CLASSIFICATION REPORTS
# ============================================================
print("\n" + "=" * 70)
print("PART 8: CLASSIFICATION REPORTS")
print("=" * 70)

for name, res in results.items():
    print(f"\n--- {name} ---")
    print(classification_report(y_test, res['y_pred'],
                                target_names=['No Disease', 'Heart Disease']))

# ============================================================
# PART 9: MODEL INTERPRETATION
# ============================================================
print("\n" + "=" * 70)
print("PART 9: MODEL INTERPRETATION")
print("=" * 70)

# Logistic Regression coefficients
lr_model = results['Logistic Regression']['model']
coef_df = pd.DataFrame({
    'feature': feature_names,
    'coefficient': lr_model.coef_[0]
}).sort_values('coefficient', key=abs, ascending=False)

print("\nLogistic Regression Coefficients:")
print("-" * 50)
for _, row in coef_df.iterrows():
    direction = "↑ increases" if row['coefficient'] > 0 else "↓ decreases"
    print(f"{row['feature']:15s}: {row['coefficient']:+.4f}  {direction} risk")

# ============================================================
# PART 10: FINAL SUMMARY
# ============================================================
print("\n" + "=" * 70)
print("PART 10: FINAL SUMMARY")
print("=" * 70)

print(f"""
🏥 Heart Disease Classification Project Summary
================================================

Dataset:
- Total samples: {len(df)}
- Features: {len(feature_names)}
- Target: Heart disease presence (binary)
- Class balance: {df['heart_disease'].mean()*100:.1f}% positive

Best Performing Model: {best_model_name}
- Accuracy:  {best_res['accuracy']:.4f}
- Precision: {best_res['precision']:.4f}
- Recall:    {best_res['recall']:.4f}
- F1 Score:  {best_res['f1']:.4f}

Key Insights:
1. Top predictive features: {', '.join(importance_df['feature'].head(3).tolist())}
2. Model successfully identifies most heart disease cases
3. Focus on recall to minimize missed diagnoses

Recommendations:
1. Collect more data for better model performance
2. Consider feature engineering (e.g., BMI, lifestyle factors)
3. Use ensemble methods for production
4. Monitor model performance over time
5. Consider cost-sensitive learning for medical applications

Files Generated:
- /tmp/heart_disease_confusion_matrices.png
- /tmp/heart_disease_feature_importance.png
""")

print("\n" + "=" * 70)
print("✅ MINI PROJECT COMPLETE!")
print("=" * 70)
print("""
Congratulations! You've built a complete classification pipeline.

What you learned:
✅ Data exploration and preparation
✅ Training multiple classification models
✅ Model comparison using multiple metrics
✅ Cross-validation for reliable estimates
✅ Confusion matrix analysis
✅ Feature importance interpretation
✅ Model interpretation with coefficients

Next steps:
- Try hyperparameter tuning with GridSearchCV
- Experiment with other algorithms (SVM, Gradient Boosting)
- Add more sophisticated feature engineering
- Deploy the model as an API
""")
