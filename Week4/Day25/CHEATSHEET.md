# Day 25 Quick Reference Cheat Sheet

## Linear Regression
```python
from sklearn.linear_model import LinearRegression

# Simple linear regression
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)

# Access coefficients
print(model.coef_)       # Slope(s)
print(model.intercept_)  # Intercept
```

## Evaluation Metrics
```python
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np

# Mean Squared Error
mse = mean_squared_error(y_true, y_pred)

# Root Mean Squared Error
rmse = np.sqrt(mean_squared_error(y_true, y_pred))

# Mean Absolute Error
mae = mean_absolute_error(y_true, y_pred)

# R² Score (Coefficient of Determination)
r2 = r2_score(y_true, y_pred)
```

## Metric Interpretation
| Metric | Range | Interpretation |
|--------|-------|----------------|
| MSE | 0 to ∞ | Lower is better, penalizes large errors |
| RMSE | 0 to ∞ | Same units as target, easier to interpret |
| MAE | 0 to ∞ | Average absolute error, robust to outliers |
| R² | -∞ to 1 | 1 = perfect, 0 = baseline, <0 = terrible |

## Polynomial Regression
```python
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Create polynomial features
poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly.fit_transform(X)

# Fit model
model = LinearRegression()
model.fit(X_poly, y)

# For new predictions
X_new_poly = poly.transform(X_new)
predictions = model.predict(X_new_poly)
```

## Ridge Regression (L2)
```python
from sklearn.linear_model import Ridge, RidgeCV

# Basic Ridge
ridge = Ridge(alpha=1.0)
ridge.fit(X_train, y_train)

# With cross-validation
ridge_cv = RidgeCV(alphas=[0.1, 1, 10, 100])
ridge_cv.fit(X_train, y_train)
print(f"Best alpha: {ridge_cv.alpha_}")
```

## Lasso Regression (L1)
```python
from sklearn.linear_model import Lasso, LassoCV

# Basic Lasso
lasso = Lasso(alpha=1.0, max_iter=10000)
lasso.fit(X_train, y_train)

# With cross-validation
lasso_cv = LassoCV(cv=5, max_iter=10000)
lasso_cv.fit(X_train, y_train)
print(f"Best alpha: {lasso_cv.alpha_}")

# Feature selection (check non-zero coefficients)
selected = lasso.coef_ != 0
```

## ElasticNet
```python
from sklearn.linear_model import ElasticNet, ElasticNetCV

# Basic ElasticNet
elastic = ElasticNet(alpha=1.0, l1_ratio=0.5, max_iter=10000)
elastic.fit(X_train, y_train)

# With cross-validation
elastic_cv = ElasticNetCV(cv=5, max_iter=10000)
elastic_cv.fit(X_train, y_train)
```

## Train-Test Split
```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=0.2,    # 20% for testing
    random_state=42   # For reproducibility
)
```

## Feature Scaling
```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)  # Use transform, not fit_transform!
```

## Complete Workflow Example
```python
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import Ridge, RidgeCV
from sklearn.metrics import r2_score, mean_squared_error

# 1. Load and split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 2. Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 3. Find best alpha with cross-validation
ridge_cv = RidgeCV(alphas=[0.1, 1, 10, 100])
ridge_cv.fit(X_train_scaled, y_train)

# 4. Make predictions
y_pred = ridge_cv.predict(X_test_scaled)

# 5. Evaluate
print(f"R²: {r2_score(y_test, y_pred):.4f}")
print(f"RMSE: {np.sqrt(mean_squared_error(y_test, y_pred)):.4f}")
```

## When to Use Which Model

| Scenario | Recommended Model |
|----------|-------------------|
| Simple, few features | Linear Regression |
| Overfitting issues | Ridge or Lasso |
| Need feature selection | Lasso |
| Correlated features | Ridge or ElasticNet |
| Non-linear relationship | Polynomial + Regularization |
| Many irrelevant features | Lasso |

## Common R² Score Ranges
- R² > 0.9: Excellent fit
- R² > 0.7: Good fit
- R² > 0.5: Moderate fit
- R² < 0.3: Poor fit
- R² < 0: Model worse than baseline

## Tips for Better Models
1. Always scale features for regularized models
2. Use cross-validation to tune hyperparameters
3. Check for overfitting (compare train vs test scores)
4. Start simple, add complexity if needed
5. Visualize residuals to check assumptions

---
**Keep this handy for Day 25 topics!** 🚀
