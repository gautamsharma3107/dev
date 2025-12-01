"""
Day 25 - Ridge and Lasso Regression (Regularization)
=====================================================
Learn: How to prevent overfitting with regularization

Key Concepts:
- What is regularization?
- Ridge regression (L2 regularization)
- Lasso regression (L1 regularization)
- Choosing between Ridge and Lasso
- ElasticNet (combining both)
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# ========== WHAT IS REGULARIZATION? ==========
print("=" * 60)
print("WHAT IS REGULARIZATION?")
print("=" * 60)

print("""
PROBLEM: Overfitting
- Model learns training data too well
- Performs poorly on new data
- High variance in predictions

SOLUTION: Regularization
- Adds a penalty to the loss function
- Prevents coefficients from becoming too large
- Helps model generalize better

Types of Regularization:
1. Ridge (L2): Adds squared coefficients penalty
2. Lasso (L1): Adds absolute coefficients penalty
3. ElasticNet: Combination of both
""")

# ========== VISUALIZING THE OVERFITTING PROBLEM ==========
print("\n" + "=" * 60)
print("VISUALIZING THE OVERFITTING PROBLEM")
print("=" * 60)

# Create data with noise
np.random.seed(42)
n_samples = 20
X = np.linspace(0, 4, n_samples).reshape(-1, 1)
y = 2 + 0.5 * X.flatten() + np.random.randn(n_samples) * 0.5

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

print(f"Training samples: {len(X_train)}")
print(f"Test samples: {len(X_test)}")

# Fit high-degree polynomial (prone to overfitting)
degree = 10
poly = PolynomialFeatures(degree=degree, include_bias=False)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

# Regular linear regression
lr_model = LinearRegression()
lr_model.fit(X_train_poly, y_train)

train_r2 = r2_score(y_train, lr_model.predict(X_train_poly))
test_r2 = r2_score(y_test, lr_model.predict(X_test_poly))

print(f"\nLinear Regression (degree={degree}):")
print(f"  Train R²: {train_r2:.4f}")
print(f"  Test R²:  {test_r2:.4f}")
print(f"  Gap:      {train_r2 - test_r2:.4f}")
print("\n⚠️ Large gap indicates overfitting!")

# ========== RIDGE REGRESSION (L2) ==========
print("\n" + "=" * 60)
print("RIDGE REGRESSION (L2 REGULARIZATION)")
print("=" * 60)

print("""
Ridge adds a penalty based on squared coefficients:

Loss = MSE + α × Σ(coefficient²)

Where:
- MSE = Mean Squared Error (regular loss)
- α (alpha) = Regularization strength
- Higher α = Stronger regularization

Effect:
- Shrinks coefficients toward zero
- But never exactly to zero
- Good when all features are useful
""")

# Compare different alpha values
alphas = [0.001, 0.1, 1, 10, 100]

print("\nRidge with different alpha values:")
print("-" * 50)
print(f"{'Alpha':<10} {'Train R²':<12} {'Test R²':<12} {'Status'}")
print("-" * 50)

for alpha in alphas:
    ridge = Ridge(alpha=alpha)
    ridge.fit(X_train_poly, y_train)
    
    train_r2 = r2_score(y_train, ridge.predict(X_train_poly))
    test_r2 = r2_score(y_test, ridge.predict(X_test_poly))
    
    gap = train_r2 - test_r2
    if gap < 0.1 and test_r2 > 0:
        status = "✅ Good"
    elif test_r2 < 0:
        status = "❌ Underfit"
    else:
        status = "⚠️ Check"
    
    print(f"{alpha:<10} {train_r2:<12.4f} {test_r2:<12.4f} {status}")

print("""
Key Observations:
- Very low α → Still overfitting
- Very high α → Underfitting (too much penalty)
- Sweet spot → Balance between train and test performance
""")

# ========== LASSO REGRESSION (L1) ==========
print("\n" + "=" * 60)
print("LASSO REGRESSION (L1 REGULARIZATION)")
print("=" * 60)

print("""
Lasso adds a penalty based on absolute coefficients:

Loss = MSE + α × Σ|coefficient|

Key Difference from Ridge:
- Can set coefficients EXACTLY to zero
- Performs feature selection automatically
- Good when you have many irrelevant features
""")

print("\nLasso with different alpha values:")
print("-" * 50)
print(f"{'Alpha':<10} {'Train R²':<12} {'Test R²':<12} {'Non-zero Coefs'}")
print("-" * 50)

for alpha in [0.001, 0.01, 0.1, 1]:
    lasso = Lasso(alpha=alpha, max_iter=10000)
    lasso.fit(X_train_poly, y_train)
    
    train_r2 = r2_score(y_train, lasso.predict(X_train_poly))
    test_r2 = r2_score(y_test, lasso.predict(X_test_poly))
    non_zero = np.sum(lasso.coef_ != 0)
    
    print(f"{alpha:<10} {train_r2:<12.4f} {test_r2:<12.4f} {non_zero}/{len(lasso.coef_)}")

print("""
Key Observations:
- Higher α → Fewer non-zero coefficients
- Lasso automatically selects important features
- Useful for high-dimensional data
""")

# ========== RIDGE VS LASSO COMPARISON ==========
print("\n" + "=" * 60)
print("RIDGE VS LASSO COMPARISON")
print("=" * 60)

print("""
| Feature          | Ridge (L2)           | Lasso (L1)           |
|-----------------|----------------------|----------------------|
| Penalty         | Sum of squared coef   | Sum of absolute coef |
| Coefficients    | Shrinks toward zero   | Can be exactly zero  |
| Feature Select  | No                    | Yes                  |
| Correlated Feat | Handles well          | Picks one randomly   |
| Best For        | All features matter   | Feature selection    |
| Computational   | Fast (closed form)    | Iterative            |

When to use:
- Ridge: All features likely relevant, multicollinearity
- Lasso: Many features, need feature selection
- ElasticNet: Best of both worlds
""")

# ========== ELASTICNET ==========
print("\n" + "=" * 60)
print("ELASTICNET (COMBINING RIDGE AND LASSO)")
print("=" * 60)

print("""
ElasticNet combines both L1 and L2 penalties:

Loss = MSE + α × (l1_ratio × Σ|coef| + (1-l1_ratio) × Σcoef²)

Parameters:
- alpha: Overall regularization strength
- l1_ratio: Balance between L1 and L2
  - l1_ratio = 1 → Pure Lasso
  - l1_ratio = 0 → Pure Ridge
  - l1_ratio = 0.5 → Equal mix
""")

elastic = ElasticNet(alpha=0.1, l1_ratio=0.5, max_iter=10000)
elastic.fit(X_train_poly, y_train)

train_r2 = r2_score(y_train, elastic.predict(X_train_poly))
test_r2 = r2_score(y_test, elastic.predict(X_test_poly))

print(f"\nElasticNet (alpha=0.1, l1_ratio=0.5):")
print(f"  Train R²: {train_r2:.4f}")
print(f"  Test R²:  {test_r2:.4f}")
print(f"  Non-zero coefficients: {np.sum(elastic.coef_ != 0)}/{len(elastic.coef_)}")

# ========== PRACTICAL EXAMPLE ==========
print("\n" + "=" * 60)
print("PRACTICAL EXAMPLE: House Price Prediction")
print("=" * 60)

# Create house data with many features
np.random.seed(42)
n = 100

# Features (some useful, some noise)
sqft = np.random.uniform(1000, 3000, n)  # Important
bedrooms = np.random.randint(1, 6, n)    # Important
bathrooms = np.random.randint(1, 4, n)   # Important
age = np.random.uniform(0, 50, n)        # Moderately important
noise1 = np.random.randn(n)              # Noise
noise2 = np.random.randn(n)              # Noise
noise3 = np.random.randn(n)              # Noise

# Target
price = 50000 + 150 * sqft + 10000 * bedrooms + 8000 * bathrooms - 500 * age + np.random.randn(n) * 20000

# Combine features
X = np.column_stack([sqft, bedrooms, bathrooms, age, noise1, noise2, noise3])
feature_names = ['sqft', 'bedrooms', 'bathrooms', 'age', 'noise1', 'noise2', 'noise3']

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, price, test_size=0.2, random_state=42)

print("Dataset: 7 features (4 useful, 3 noise)")
print("-" * 60)

# Compare models
models = {
    'Linear Regression': LinearRegression(),
    'Ridge (α=1)': Ridge(alpha=1),
    'Lasso (α=100)': Lasso(alpha=100, max_iter=10000),
    'ElasticNet': ElasticNet(alpha=100, l1_ratio=0.5, max_iter=10000)
}

print(f"\n{'Model':<25} {'Test R²':<10} {'RMSE':>12}")
print("-" * 60)

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    test_r2 = r2_score(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    print(f"{name:<25} {test_r2:<10.4f} ${rmse:>11,.0f}")

# Show Lasso feature selection
print("\nLasso Feature Selection:")
print("-" * 40)
lasso = Lasso(alpha=100, max_iter=10000)
lasso.fit(X_train, y_train)

for name, coef in zip(feature_names, lasso.coef_):
    status = "✅ Selected" if coef != 0 else "❌ Eliminated"
    print(f"  {name:<12}: {coef:>12.2f} {status}")

print("\nLasso correctly identified and eliminated noise features!")

# ========== CHOOSING THE RIGHT ALPHA ==========
print("\n" + "=" * 60)
print("CHOOSING THE RIGHT ALPHA (Cross-Validation)")
print("=" * 60)

print("""
Use cross-validation to find optimal alpha:

from sklearn.linear_model import RidgeCV, LassoCV

# Automatically finds best alpha
ridge_cv = RidgeCV(alphas=[0.1, 1, 10, 100])
ridge_cv.fit(X_train, y_train)
print(f"Best alpha: {ridge_cv.alpha_}")

lasso_cv = LassoCV(cv=5)
lasso_cv.fit(X_train, y_train)
print(f"Best alpha: {lasso_cv.alpha_}")
""")

from sklearn.linear_model import RidgeCV, LassoCV

ridge_cv = RidgeCV(alphas=[0.1, 1, 10, 100, 1000])
ridge_cv.fit(X_train, y_train)

lasso_cv = LassoCV(cv=5, max_iter=10000)
lasso_cv.fit(X_train, y_train)

print(f"\nCross-validation results:")
print(f"  Best Ridge alpha: {ridge_cv.alpha_}")
print(f"  Best Lasso alpha: {lasso_cv.alpha_:.4f}")

# ========== QUICK REFERENCE ==========
print("\n" + "=" * 60)
print("QUICK REFERENCE: WHEN TO USE WHAT")
print("=" * 60)

print("""
1. LINEAR REGRESSION
   - When: Simple problems, no overfitting
   - Pros: Simple, interpretable
   - Cons: Can overfit

2. RIDGE REGRESSION
   - When: Multicollinearity, all features matter
   - Pros: Handles correlated features
   - Cons: Keeps all features

3. LASSO REGRESSION
   - When: Feature selection needed, sparse models
   - Pros: Automatic feature selection
   - Cons: May drop useful correlated features

4. ELASTICNET
   - When: Many features, some correlated
   - Pros: Best of both Ridge and Lasso
   - Cons: Two parameters to tune

Typical Workflow:
1. Start with Linear Regression
2. If overfitting → Try Ridge or Lasso
3. If need feature selection → Use Lasso
4. If have correlated features → Use Ridge or ElasticNet
5. Always use cross-validation to tune alpha!
""")

print("\n" + "=" * 60)
print("✅ Ridge and Lasso Regression - Complete!")
print("=" * 60)
