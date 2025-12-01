"""
Day 25 Mini Project: House Price Prediction
============================================
Build a complete house price prediction model using regression techniques.

Objectives:
1. Load and explore the data
2. Prepare features and target
3. Train multiple regression models
4. Evaluate and compare models
5. Make predictions on new houses
"""

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

print("=" * 60)
print("HOUSE PRICE PREDICTION PROJECT")
print("=" * 60)

# ============================================================
# STEP 1: CREATE SYNTHETIC HOUSING DATA
# ============================================================
print("\n" + "=" * 60)
print("STEP 1: Create Dataset")
print("=" * 60)

np.random.seed(42)
n_samples = 500

# Features
sqft = np.random.uniform(800, 4000, n_samples)           # Square footage
bedrooms = np.random.randint(1, 6, n_samples)            # Number of bedrooms
bathrooms = np.random.randint(1, 4, n_samples)           # Number of bathrooms
age = np.random.uniform(0, 50, n_samples)                # Age of house in years
garage = np.random.randint(0, 3, n_samples)              # Garage spaces
lot_size = np.random.uniform(2000, 20000, n_samples)     # Lot size in sqft
has_pool = np.random.randint(0, 2, n_samples)            # Has pool (0/1)

# Target: Price (based on features with some noise)
price = (
    50000 +                              # Base price
    150 * sqft +                         # $150 per sqft
    15000 * bedrooms +                   # $15k per bedroom
    12000 * bathrooms +                  # $12k per bathroom
    -1000 * age +                        # Depreciation
    10000 * garage +                     # $10k per garage space
    5 * lot_size +                       # $5 per sqft of lot
    25000 * has_pool +                   # $25k for pool
    np.random.randn(n_samples) * 30000   # Market noise
)

# Combine features
X = np.column_stack([sqft, bedrooms, bathrooms, age, garage, lot_size, has_pool])
y = price

feature_names = ['sqft', 'bedrooms', 'bathrooms', 'age', 'garage', 'lot_size', 'has_pool']

print(f"Dataset created with {n_samples} houses")
print(f"Features: {feature_names}")
print(f"\nSample data (first 5 houses):")
print("-" * 80)
print(f"{'sqft':>8} {'beds':>6} {'baths':>6} {'age':>6} {'garage':>7} {'lot':>8} {'pool':>5} | {'price':>12}")
print("-" * 80)
for i in range(5):
    print(f"{X[i,0]:>8.0f} {X[i,1]:>6.0f} {X[i,2]:>6.0f} {X[i,3]:>6.1f} {X[i,4]:>7.0f} {X[i,5]:>8.0f} {X[i,6]:>5.0f} | ${y[i]:>11,.0f}")

print(f"\nPrice range: ${y.min():,.0f} - ${y.max():,.0f}")
print(f"Average price: ${y.mean():,.0f}")

# ============================================================
# STEP 2: PREPARE DATA
# ============================================================
print("\n" + "=" * 60)
print("STEP 2: Prepare Data")
print("=" * 60)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"Training samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("Features scaled using StandardScaler")

# ============================================================
# STEP 3: TRAIN MODELS
# ============================================================
print("\n" + "=" * 60)
print("STEP 3: Train Multiple Models")
print("=" * 60)

models = {
    'Linear Regression': LinearRegression(),
    'Ridge (α=1)': Ridge(alpha=1),
    'Ridge (α=10)': Ridge(alpha=10),
    'Lasso (α=100)': Lasso(alpha=100, max_iter=10000),
    'Lasso (α=1000)': Lasso(alpha=1000, max_iter=10000),
    'ElasticNet': ElasticNet(alpha=100, l1_ratio=0.5, max_iter=10000),
}

results = {}

for name, model in models.items():
    # Train
    model.fit(X_train_scaled, y_train)
    
    # Predict
    y_train_pred = model.predict(X_train_scaled)
    y_test_pred = model.predict(X_test_scaled)
    
    # Store results
    results[name] = {
        'model': model,
        'train_r2': r2_score(y_train, y_train_pred),
        'test_r2': r2_score(y_test, y_test_pred),
        'test_rmse': np.sqrt(mean_squared_error(y_test, y_test_pred)),
        'test_mae': mean_absolute_error(y_test, y_test_pred)
    }

print(f"\n{'Model':<25} {'Train R²':>10} {'Test R²':>10} {'RMSE':>15} {'MAE':>15}")
print("-" * 80)
for name, r in results.items():
    print(f"{name:<25} {r['train_r2']:>10.4f} {r['test_r2']:>10.4f} ${r['test_rmse']:>14,.0f} ${r['test_mae']:>14,.0f}")

# ============================================================
# STEP 4: ANALYZE BEST MODEL
# ============================================================
print("\n" + "=" * 60)
print("STEP 4: Analyze Best Model")
print("=" * 60)

# Find best model by test R²
best_name = max(results, key=lambda x: results[x]['test_r2'])
best_model = results[best_name]['model']

print(f"Best model: {best_name}")
print(f"Test R²: {results[best_name]['test_r2']:.4f}")
print(f"Test RMSE: ${results[best_name]['test_rmse']:,.0f}")

# Show feature importance (coefficients)
print("\nFeature Importance (Coefficients):")
print("-" * 40)

# Get coefficients (adjust for scaling)
coefs = best_model.coef_
for name, coef in sorted(zip(feature_names, coefs), key=lambda x: abs(x[1]), reverse=True):
    print(f"  {name:<12}: {coef:>12,.2f}")

# ============================================================
# STEP 5: ANALYZE LASSO FEATURE SELECTION
# ============================================================
print("\n" + "=" * 60)
print("STEP 5: Lasso Feature Selection")
print("=" * 60)

lasso = results['Lasso (α=1000)']['model']

print("Lasso (α=1000) Coefficient Analysis:")
print("-" * 40)
for name, coef in zip(feature_names, lasso.coef_):
    status = "✅ Important" if abs(coef) > 1 else "❌ Eliminated"
    print(f"  {name:<12}: {coef:>12.2f} {status}")

# ============================================================
# STEP 6: MAKE PREDICTIONS
# ============================================================
print("\n" + "=" * 60)
print("STEP 6: Make Predictions on New Houses")
print("=" * 60)

# New houses to predict
new_houses = np.array([
    [2000, 3, 2, 10, 2, 8000, 1],   # Medium house with pool
    [1200, 2, 1, 30, 1, 5000, 0],   # Small old house
    [3500, 5, 3, 5, 2, 15000, 1],   # Large new house with pool
])

new_house_descriptions = [
    "Medium house (2000sqft, 3bed/2bath, 10yrs, pool)",
    "Small old house (1200sqft, 2bed/1bath, 30yrs)",
    "Large new house (3500sqft, 5bed/3bath, 5yrs, pool)"
]

# Scale and predict
new_houses_scaled = scaler.transform(new_houses)
predictions = best_model.predict(new_houses_scaled)

print(f"Using {best_name} for predictions:\n")
for desc, pred in zip(new_house_descriptions, predictions):
    print(f"  {desc}")
    print(f"  Predicted Price: ${pred:,.0f}\n")

# ============================================================
# STEP 7: MODEL COMPARISON VISUALIZATION (Text-based)
# ============================================================
print("\n" + "=" * 60)
print("STEP 7: Model Performance Summary")
print("=" * 60)

print("\nTest R² Comparison (higher is better):")
print("-" * 60)
for name, r in sorted(results.items(), key=lambda x: x[1]['test_r2'], reverse=True):
    bar_length = int(r['test_r2'] * 50)
    bar = "█" * bar_length + "░" * (50 - bar_length)
    print(f"{name:<25} |{bar}| {r['test_r2']:.4f}")

print("\nOverfitting Check (Train R² - Test R²):")
print("-" * 60)
for name, r in results.items():
    gap = r['train_r2'] - r['test_r2']
    status = "✅ OK" if gap < 0.05 else "⚠️ Check"
    print(f"{name:<25}: Gap = {gap:.4f} {status}")

# ============================================================
# STEP 8: CONCLUSIONS
# ============================================================
print("\n" + "=" * 60)
print("STEP 8: Conclusions")
print("=" * 60)

print("""
Key Findings:

1. MODEL PERFORMANCE
   - All models performed similarly on this well-structured data
   - Linear regression works well when features have clear linear relationships
   - Regularization (Ridge/Lasso) helps prevent overfitting

2. FEATURE IMPORTANCE
   - Square footage has the largest impact on price
   - Number of bedrooms and bathrooms are significant
   - Age negatively affects price (depreciation)
   - Having a pool adds value

3. RECOMMENDATIONS
   - For this dataset, Linear Regression is sufficient
   - Use Lasso if you need automatic feature selection
   - Use Ridge if you have multicollinearity concerns
   
4. IMPROVEMENTS TO CONSIDER
   - Add more features (location, school district, etc.)
   - Try polynomial features for non-linear relationships
   - Collect more data for better generalization
   - Use cross-validation for more robust evaluation
""")

print("\n" + "=" * 60)
print("PROJECT COMPLETE!")
print("=" * 60)
