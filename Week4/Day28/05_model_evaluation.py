"""
MODEL EVALUATION - End-to-End ML Project
==========================================
Day 28: Week 4 Mini-Project

Learn how to evaluate machine learning models comprehensively.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score, learning_curve
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (
    mean_squared_error, mean_absolute_error, r2_score,
    mean_absolute_percentage_error
)
import warnings
warnings.filterwarnings('ignore')

print("=" * 60)
print("MODEL EVALUATION - ML Project Pipeline")
print("=" * 60)

# ============================================================
# 1. Prepare Data and Train Model
# ============================================================

print("\n1. DATA PREPARATION")
print("-" * 40)

# Create sample dataset
np.random.seed(42)
n_samples = 1000

data = {
    'square_feet': np.random.randint(500, 5000, n_samples),
    'bedrooms': np.random.randint(1, 7, n_samples),
    'bathrooms': np.random.randint(1, 5, n_samples),
    'age_years': np.random.randint(0, 100, n_samples),
    'location_score': np.random.uniform(1, 10, n_samples).round(2),
    'garage_spaces': np.random.randint(0, 4, n_samples),
    'has_pool': np.random.choice([0, 1], n_samples, p=[0.7, 0.3])
}

price = (
    data['square_feet'] * 100 +
    data['bedrooms'] * 15000 +
    data['bathrooms'] * 10000 -
    data['age_years'] * 500 +
    data['location_score'] * 5000 +
    data['garage_spaces'] * 8000 +
    data['has_pool'] * 20000 +
    np.random.normal(0, 20000, n_samples)
)
data['price'] = price.astype(int)

df = pd.DataFrame(data)

feature_columns = ['square_feet', 'bedrooms', 'bathrooms', 'age_years',
                   'location_score', 'garage_spaces', 'has_pool']

X = df[feature_columns]
y = df['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train model
model = RandomForestRegressor(n_estimators=100, max_depth=10, random_state=42)
model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)

print("Model trained and predictions made!")

# ============================================================
# 2. Regression Metrics
# ============================================================

print("\n2. REGRESSION METRICS")
print("-" * 40)

# Calculate all metrics
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_pred)
mape = mean_absolute_percentage_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nRegression Metrics:")
print(f"  Mean Squared Error (MSE):           {mse:,.2f}")
print(f"  Root Mean Squared Error (RMSE):     {rmse:,.2f}")
print(f"  Mean Absolute Error (MAE):          {mae:,.2f}")
print(f"  Mean Absolute Percentage Error:     {mape:.2%}")
print(f"  R-squared (R²):                     {r2:.4f}")

# Interpretation
print("\n📊 Interpretation:")
print(f"  - On average, predictions are off by ${mae:,.0f} (MAE)")
print(f"  - The model explains {r2*100:.1f}% of price variance (R²)")
print(f"  - Predictions are off by ~{mape*100:.1f}% on average (MAPE)")

# ============================================================
# 3. Residual Analysis
# ============================================================

print("\n3. RESIDUAL ANALYSIS")
print("-" * 40)

residuals = y_test - y_pred

print(f"\nResidual Statistics:")
print(f"  Mean: {residuals.mean():,.2f} (should be ~0)")
print(f"  Std:  {residuals.std():,.2f}")
print(f"  Min:  {residuals.min():,.2f}")
print(f"  Max:  {residuals.max():,.2f}")

# Residual plots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Residual Analysis', fontsize=14)

# 1. Residuals vs Predicted
axes[0, 0].scatter(y_pred, residuals, alpha=0.5)
axes[0, 0].axhline(y=0, color='r', linestyle='--')
axes[0, 0].set_xlabel('Predicted Values')
axes[0, 0].set_ylabel('Residuals')
axes[0, 0].set_title('Residuals vs Predicted')

# 2. Residual Distribution
axes[0, 1].hist(residuals, bins=30, edgecolor='black', alpha=0.7)
axes[0, 1].axvline(x=0, color='r', linestyle='--')
axes[0, 1].set_xlabel('Residuals')
axes[0, 1].set_ylabel('Frequency')
axes[0, 1].set_title('Residual Distribution')

# 3. Actual vs Predicted
axes[1, 0].scatter(y_test, y_pred, alpha=0.5)
min_val = min(y_test.min(), y_pred.min())
max_val = max(y_test.max(), y_pred.max())
axes[1, 0].plot([min_val, max_val], [min_val, max_val], 'r--', label='Perfect Prediction')
axes[1, 0].set_xlabel('Actual Values')
axes[1, 0].set_ylabel('Predicted Values')
axes[1, 0].set_title('Actual vs Predicted')
axes[1, 0].legend()

# 4. Q-Q Plot (approximate)
sorted_residuals = np.sort(residuals)
theoretical_quantiles = np.linspace(0.01, 0.99, len(sorted_residuals))
theoretical_values = np.percentile(sorted_residuals, theoretical_quantiles * 100)
axes[1, 1].scatter(theoretical_values, sorted_residuals, alpha=0.5)
axes[1, 1].plot([sorted_residuals.min(), sorted_residuals.max()], 
                 [sorted_residuals.min(), sorted_residuals.max()], 'r--')
axes[1, 1].set_xlabel('Theoretical Quantiles')
axes[1, 1].set_ylabel('Sample Quantiles')
axes[1, 1].set_title('Q-Q Plot')

plt.tight_layout()
plt.savefig('residual_analysis.png', dpi=100, bbox_inches='tight')
plt.close()
print("\nResidual plots saved to 'residual_analysis.png'")

# ============================================================
# 4. Cross-Validation
# ============================================================

print("\n4. CROSS-VALIDATION")
print("-" * 40)

X_scaled = scaler.fit_transform(X)

# K-Fold Cross-Validation
for k in [3, 5, 10]:
    cv_scores = cross_val_score(model, X_scaled, y, cv=k, scoring='r2')
    print(f"\n{k}-Fold Cross-Validation:")
    print(f"  Scores: {cv_scores.round(4)}")
    print(f"  Mean R²: {cv_scores.mean():.4f} (+/- {cv_scores.std() * 2:.4f})")

# Different metrics
print("\nDifferent Scoring Metrics (5-Fold CV):")
for metric in ['r2', 'neg_mean_squared_error', 'neg_mean_absolute_error']:
    scores = cross_val_score(model, X_scaled, y, cv=5, scoring=metric)
    if 'neg' in metric:
        scores = -scores
        metric_name = metric.replace('neg_', '')
    else:
        metric_name = metric
    print(f"  {metric_name}: {scores.mean():.4f}")

# ============================================================
# 5. Learning Curves
# ============================================================

print("\n5. LEARNING CURVES")
print("-" * 40)

train_sizes, train_scores, test_scores = learning_curve(
    model, X_scaled, y, cv=5, 
    train_sizes=np.linspace(0.1, 1.0, 10),
    scoring='r2', random_state=42
)

train_mean = train_scores.mean(axis=1)
train_std = train_scores.std(axis=1)
test_mean = test_scores.mean(axis=1)
test_std = test_scores.std(axis=1)

plt.figure(figsize=(10, 6))
plt.plot(train_sizes, train_mean, 'o-', label='Training Score', color='blue')
plt.fill_between(train_sizes, train_mean - train_std, train_mean + train_std, alpha=0.2, color='blue')
plt.plot(train_sizes, test_mean, 'o-', label='Cross-Validation Score', color='green')
plt.fill_between(train_sizes, test_mean - test_std, test_mean + test_std, alpha=0.2, color='green')
plt.xlabel('Training Set Size')
plt.ylabel('R² Score')
plt.title('Learning Curves')
plt.legend(loc='lower right')
plt.grid(True)
plt.tight_layout()
plt.savefig('learning_curves.png', dpi=100, bbox_inches='tight')
plt.close()
print("Learning curves saved to 'learning_curves.png'")

# ============================================================
# 6. Overfitting Detection
# ============================================================

print("\n6. OVERFITTING DETECTION")
print("-" * 40)

# Train score vs Test score
y_train_pred = model.predict(X_train_scaled)
train_r2 = r2_score(y_train, y_train_pred)
test_r2 = r2_score(y_test, y_pred)

print(f"\nTraining R²: {train_r2:.4f}")
print(f"Test R²:     {test_r2:.4f}")
print(f"Difference:  {abs(train_r2 - test_r2):.4f}")

if train_r2 - test_r2 > 0.1:
    print("\n⚠️ Warning: Possible overfitting detected!")
    print("   Training score is significantly higher than test score.")
else:
    print("\n✅ Model appears to generalize well.")

# ============================================================
# 7. Prediction Error Analysis
# ============================================================

print("\n7. PREDICTION ERROR ANALYSIS")
print("-" * 40)

# Analyze errors by ranges
error_df = pd.DataFrame({
    'actual': y_test.values,
    'predicted': y_pred,
    'residual': residuals.values,
    'abs_error': np.abs(residuals.values),
    'pct_error': np.abs(residuals.values) / y_test.values * 100
})

# Group by price ranges
bins = [0, 200000, 400000, 600000, float('inf')]
labels = ['< 200K', '200K-400K', '400K-600K', '> 600K']
error_df['price_range'] = pd.cut(error_df['actual'], bins=bins, labels=labels)

print("\nError Analysis by Price Range:")
error_summary = error_df.groupby('price_range').agg({
    'abs_error': ['mean', 'std'],
    'pct_error': 'mean'
}).round(2)
print(error_summary)

# ============================================================
# 8. Model Comparison Report
# ============================================================

print("\n8. MODEL EVALUATION REPORT")
print("-" * 40)

print("""
╔══════════════════════════════════════════════════════════╗
║                MODEL EVALUATION REPORT                   ║
╠══════════════════════════════════════════════════════════╣
""")

print(f"║  Model: Random Forest Regressor                         ║")
print(f"║  Training Samples: {len(y_train):,}                               ║")
print(f"║  Test Samples: {len(y_test):,}                                   ║")
print(f"╠══════════════════════════════════════════════════════════╣")
print(f"║  Performance Metrics:                                    ║")
print(f"║    - R² Score:    {r2:.4f}                               ║")
print(f"║    - RMSE:        ${rmse:,.0f}                            ║")
print(f"║    - MAE:         ${mae:,.0f}                            ║")
print(f"║    - MAPE:        {mape*100:.1f}%                                  ║")
print(f"╠══════════════════════════════════════════════════════════╣")
print(f"║  Cross-Validation (5-Fold): {cv_scores.mean():.4f} (+/- {cv_scores.std()*2:.4f})    ║")
print(f"╚══════════════════════════════════════════════════════════╝")

# ============================================================
# EXERCISES
# ============================================================

print("\n" + "=" * 60)
print("EXERCISES")
print("=" * 60)

print("""
1. Evaluate a classification model:
   - Use accuracy, precision, recall, F1-score
   - Create confusion matrix
   - Plot ROC curve and calculate AUC

2. Compare multiple models:
   - Train 3+ different models
   - Compare using cross-validation
   - Create a comparison visualization

3. Perform hyperparameter tuning:
   - Use GridSearchCV or RandomizedSearchCV
   - Evaluate before and after tuning

4. Analyze prediction errors:
   - Identify samples with largest errors
   - Investigate why model struggles with them

5. Create a complete evaluation report:
   - Include all metrics
   - Add visualizations
   - Provide recommendations
""")

# ============================================================
# KEY TAKEAWAYS
# ============================================================

print("\n" + "=" * 60)
print("KEY TAKEAWAYS")
print("=" * 60)

print("""
✅ Use multiple metrics to evaluate model performance
✅ Analyze residuals to check model assumptions
✅ Use cross-validation for robust evaluation
✅ Plot learning curves to detect overfitting
✅ Compare train vs test scores for generalization
✅ Document all evaluation results
✅ Create visualizations to communicate results
✅ Consider business context when interpreting metrics
""")
