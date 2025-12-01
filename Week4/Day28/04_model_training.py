"""
MODEL TRAINING - End-to-End ML Project
========================================
Day 28: Week 4 Mini-Project

Learn how to train machine learning models using Scikit-learn.
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import warnings
warnings.filterwarnings('ignore')

print("=" * 60)
print("MODEL TRAINING - ML Project Pipeline")
print("=" * 60)

# ============================================================
# 1. Prepare Data
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
print(f"Dataset shape: {df.shape}")

# Define features and target
feature_columns = ['square_feet', 'bedrooms', 'bathrooms', 'age_years',
                   'location_score', 'garage_spaces', 'has_pool']

X = df[feature_columns]
y = df['price']

print(f"\nFeatures: {feature_columns}")
print(f"Target: price")

# ============================================================
# 2. Train-Test Split
# ============================================================

print("\n2. TRAIN-TEST SPLIT")
print("-" * 40)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"Training set: {X_train.shape[0]} samples")
print(f"Test set: {X_test.shape[0]} samples")

# ============================================================
# 3. Feature Scaling
# ============================================================

print("\n3. FEATURE SCALING")
print("-" * 40)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("Features scaled using StandardScaler")
print(f"Training mean (should be ~0): {X_train_scaled.mean(axis=0).round(2)}")
print(f"Training std (should be ~1): {X_train_scaled.std(axis=0).round(2)}")

# ============================================================
# 4. Train Multiple Models
# ============================================================

print("\n4. TRAINING MULTIPLE MODELS")
print("-" * 40)

# Define models
models = {
    'Linear Regression': LinearRegression(),
    'Ridge Regression': Ridge(alpha=1.0),
    'Lasso Regression': Lasso(alpha=1.0),
    'Decision Tree': DecisionTreeRegressor(max_depth=10, random_state=42),
    'Random Forest': RandomForestRegressor(n_estimators=100, max_depth=10, random_state=42),
    'Gradient Boosting': GradientBoostingRegressor(n_estimators=100, max_depth=5, random_state=42)
}

# Train each model
trained_models = {}
for name, model in models.items():
    print(f"\nTraining {name}...")
    model.fit(X_train_scaled, y_train)
    trained_models[name] = model
    print(f"  ✓ {name} trained successfully")

# ============================================================
# 5. Model Evaluation
# ============================================================

print("\n5. MODEL EVALUATION")
print("-" * 40)

results = []

for name, model in trained_models.items():
    # Make predictions
    y_pred = model.predict(X_test_scaled)
    
    # Calculate metrics
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    results.append({
        'Model': name,
        'MSE': mse,
        'RMSE': rmse,
        'MAE': mae,
        'R²': r2
    })
    
    print(f"\n{name}:")
    print(f"  MSE:  {mse:,.2f}")
    print(f"  RMSE: {rmse:,.2f}")
    print(f"  MAE:  {mae:,.2f}")
    print(f"  R²:   {r2:.4f}")

# Create results DataFrame
results_df = pd.DataFrame(results)
results_df = results_df.sort_values('R²', ascending=False)

print("\n" + "=" * 60)
print("MODEL COMPARISON (sorted by R²)")
print("=" * 60)
print(results_df.to_string(index=False))

# ============================================================
# 6. Cross-Validation
# ============================================================

print("\n6. CROSS-VALIDATION")
print("-" * 40)

print("\n5-Fold Cross-Validation Results:")

X_scaled = scaler.fit_transform(X)

for name, model in models.items():
    cv_scores = cross_val_score(model, X_scaled, y, cv=5, scoring='r2')
    print(f"\n{name}:")
    print(f"  CV Scores: {cv_scores.round(4)}")
    print(f"  Mean R²: {cv_scores.mean():.4f} (+/- {cv_scores.std() * 2:.4f})")

# ============================================================
# 7. Feature Importance
# ============================================================

print("\n7. FEATURE IMPORTANCE")
print("-" * 40)

# Random Forest feature importance
rf_model = trained_models['Random Forest']
feature_importance = pd.DataFrame({
    'Feature': feature_columns,
    'Importance': rf_model.feature_importances_
}).sort_values('Importance', ascending=False)

print("\nRandom Forest Feature Importance:")
print(feature_importance.to_string(index=False))

# Linear Regression coefficients
lr_model = trained_models['Linear Regression']
coefficients = pd.DataFrame({
    'Feature': feature_columns,
    'Coefficient': lr_model.coef_
}).sort_values('Coefficient', ascending=False)

print("\nLinear Regression Coefficients:")
print(coefficients.to_string(index=False))

# ============================================================
# 8. Select Best Model
# ============================================================

print("\n8. SELECT BEST MODEL")
print("-" * 40)

best_model_name = results_df.iloc[0]['Model']
best_model = trained_models[best_model_name]
best_r2 = results_df.iloc[0]['R²']

print(f"\nBest Model: {best_model_name}")
print(f"R² Score: {best_r2:.4f}")

# ============================================================
# 9. Save Model for Predictions
# ============================================================

print("\n9. SAVE MODEL")
print("-" * 40)

import joblib

# Save the best model and scaler
joblib.dump(best_model, 'best_model.pkl')
joblib.dump(scaler, 'scaler.pkl')

print("Best model saved to 'best_model.pkl'")
print("Scaler saved to 'scaler.pkl'")

# ============================================================
# EXERCISES
# ============================================================

print("\n" + "=" * 60)
print("EXERCISES")
print("=" * 60)

print("""
1. Train additional models:
   - Support Vector Regression (SVR)
   - K-Nearest Neighbors Regressor
   - Neural Network (MLPRegressor)

2. Hyperparameter Tuning:
   - Use GridSearchCV to find best parameters
   - Compare before and after tuning

3. Feature Selection:
   - Try removing low-importance features
   - See if model performance improves

4. Try a Classification Problem:
   - Convert price to categories (Low, Medium, High)
   - Train classification models
   - Compare accuracy scores

5. Experiment with different train-test splits:
   - 70-30, 80-20, 90-10
   - Observe impact on model performance
""")

# ============================================================
# KEY TAKEAWAYS
# ============================================================

print("\n" + "=" * 60)
print("KEY TAKEAWAYS")
print("=" * 60)

print("""
✅ Always split data into train and test sets
✅ Scale features for algorithms that need it
✅ Train multiple models and compare
✅ Use appropriate metrics (RMSE, MAE, R² for regression)
✅ Use cross-validation for robust evaluation
✅ Analyze feature importance to understand the model
✅ Save trained models for future predictions
✅ Document model performance for reproducibility
""")
