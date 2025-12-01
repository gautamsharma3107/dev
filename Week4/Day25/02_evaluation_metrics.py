"""
Day 25 - Regression Evaluation Metrics
======================================
Learn: How to evaluate regression model performance

Key Concepts:
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score (Coefficient of Determination)
- Mean Absolute Error (MAE)
"""

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import matplotlib.pyplot as plt

# ========== WHY EVALUATION METRICS? ==========
print("=" * 60)
print("WHY DO WE NEED EVALUATION METRICS?")
print("=" * 60)

print("""
After training a model, we need to know:
- How good are our predictions?
- Is our model learning the patterns?
- Can we trust this model for new data?

Common Regression Metrics:
1. MSE  - Mean Squared Error
2. RMSE - Root Mean Squared Error
3. MAE  - Mean Absolute Error
4. R²   - R-Squared (Coefficient of Determination)

Each metric tells us something different about model performance.
""")

# ========== CREATE SAMPLE DATA ==========
print("\n" + "=" * 60)
print("CREATING SAMPLE DATA")
print("=" * 60)

np.random.seed(42)

# Create data: House size vs Price
house_size = np.array([1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800]).reshape(-1, 1)
actual_prices = np.array([150000, 175000, 210000, 245000, 275000, 310000, 340000, 375000, 410000, 445000])

# Add noise
actual_prices = actual_prices + np.random.randn(10) * 15000

print("House Size (sq ft) vs Price ($):")
print("-" * 40)
for size, price in zip(house_size.flatten(), actual_prices):
    print(f"Size: {size:4d} | Price: ${price:,.0f}")

# Train model
model = LinearRegression()
model.fit(house_size, actual_prices)
predicted_prices = model.predict(house_size)

print(f"\nModel: Price = ${model.coef_[0]:.2f} × Size + ${model.intercept_:,.0f}")

# ========== MEAN SQUARED ERROR (MSE) ==========
print("\n" + "=" * 60)
print("MEAN SQUARED ERROR (MSE)")
print("=" * 60)

print("""
MSE = Average of squared differences between predicted and actual

Formula: MSE = (1/n) × Σ(actual - predicted)²

Characteristics:
- Always positive
- Penalizes large errors more (due to squaring)
- Same units as target² (e.g., dollars²)
- Lower is better
""")

# Calculate MSE manually
errors = actual_prices - predicted_prices
squared_errors = errors ** 2
mse_manual = np.mean(squared_errors)

# Using sklearn
mse_sklearn = mean_squared_error(actual_prices, predicted_prices)

print("Step-by-step calculation:")
print("-" * 60)
print("Actual    | Predicted |    Error   | Squared Error")
print("-" * 60)
for act, pred, err, sq_err in zip(actual_prices, predicted_prices, errors, squared_errors):
    print(f"${act:>8,.0f} | ${pred:>8,.0f} | ${err:>+9,.0f} | ${sq_err:>15,.0f}")
print("-" * 60)
print(f"Sum of Squared Errors: ${sum(squared_errors):,.0f}")
print(f"MSE (manual): ${mse_manual:,.0f}")
print(f"MSE (sklearn): ${mse_sklearn:,.0f}")

# ========== ROOT MEAN SQUARED ERROR (RMSE) ==========
print("\n" + "=" * 60)
print("ROOT MEAN SQUARED ERROR (RMSE)")
print("=" * 60)

print("""
RMSE = Square root of MSE

Formula: RMSE = √MSE = √[(1/n) × Σ(actual - predicted)²]

Characteristics:
- Same units as target (e.g., dollars) - EASIER TO INTERPRET
- More intuitive than MSE
- Lower is better
- Also penalizes large errors
""")

rmse_manual = np.sqrt(mse_manual)
rmse_sklearn = np.sqrt(mean_squared_error(actual_prices, predicted_prices))

print(f"MSE:  ${mse_manual:,.0f}")
print(f"RMSE: ${rmse_manual:,.0f}")
print(f"\nInterpretation: On average, our predictions are off by about ${rmse_manual:,.0f}")

# ========== MEAN ABSOLUTE ERROR (MAE) ==========
print("\n" + "=" * 60)
print("MEAN ABSOLUTE ERROR (MAE)")
print("=" * 60)

print("""
MAE = Average of absolute differences

Formula: MAE = (1/n) × Σ|actual - predicted|

Characteristics:
- Same units as target (e.g., dollars)
- Treats all errors equally (no squaring)
- More robust to outliers than MSE/RMSE
- Lower is better
""")

absolute_errors = np.abs(errors)
mae_manual = np.mean(absolute_errors)
mae_sklearn = mean_absolute_error(actual_prices, predicted_prices)

print("Calculation:")
print("-" * 40)
print("Error      | Absolute Error")
print("-" * 40)
for err, abs_err in zip(errors, absolute_errors):
    print(f"${err:>+10,.0f} | ${abs_err:>10,.0f}")
print("-" * 40)
print(f"Sum: ${sum(absolute_errors):,.0f}")
print(f"MAE (manual): ${mae_manual:,.0f}")
print(f"MAE (sklearn): ${mae_sklearn:,.0f}")

print(f"\nInterpretation: On average, our predictions are off by ${mae_manual:,.0f}")

# ========== MSE vs MAE ==========
print("\n" + "=" * 60)
print("MSE vs MAE - WHEN TO USE WHICH?")
print("=" * 60)

print("""
MSE/RMSE:
- Use when large errors are particularly bad
- More sensitive to outliers
- Penalizes big mistakes heavily

MAE:
- Use when all errors matter equally
- More robust to outliers
- Easier to interpret

Example:
If predicting delivery time:
- MAE: "On average, we're off by 15 minutes"
- RMSE might be higher due to a few very late deliveries
""")

# Demonstrate with outliers
print("\nDemonstration with outliers:")
y_actual = np.array([100, 105, 110, 115, 120])
y_pred_normal = np.array([102, 103, 108, 117, 122])
y_pred_outlier = np.array([102, 103, 108, 117, 150])  # One big error

print("\nNormal predictions:")
print(f"  MAE:  {mean_absolute_error(y_actual, y_pred_normal):.2f}")
print(f"  RMSE: {np.sqrt(mean_squared_error(y_actual, y_pred_normal)):.2f}")

print("\nWith one outlier prediction:")
print(f"  MAE:  {mean_absolute_error(y_actual, y_pred_outlier):.2f}")
print(f"  RMSE: {np.sqrt(mean_squared_error(y_actual, y_pred_outlier)):.2f}")

print("\nNotice: RMSE increased much more than MAE due to the outlier!")

# ========== R² SCORE (COEFFICIENT OF DETERMINATION) ==========
print("\n" + "=" * 60)
print("R² SCORE (COEFFICIENT OF DETERMINATION)")
print("=" * 60)

print("""
R² measures how well the model explains variance in the data.

Formula: R² = 1 - (SS_res / SS_tot)

Where:
- SS_res = Sum of squared residuals = Σ(actual - predicted)²
- SS_tot = Total sum of squares = Σ(actual - mean)²

Interpretation:
- R² = 1.0  → Perfect predictions
- R² = 0.0  → Model is as good as predicting the mean
- R² < 0.0  → Model is worse than predicting the mean (bad!)

Common ranges:
- R² > 0.9  → Excellent
- R² > 0.7  → Good
- R² > 0.5  → Moderate
- R² < 0.3  → Poor
""")

# Calculate R² manually
mean_price = np.mean(actual_prices)
ss_tot = np.sum((actual_prices - mean_price) ** 2)
ss_res = np.sum((actual_prices - predicted_prices) ** 2)
r2_manual = 1 - (ss_res / ss_tot)

# Using sklearn
r2_sklearn = r2_score(actual_prices, predicted_prices)

print("Calculation:")
print("-" * 40)
print(f"Mean of actual prices: ${mean_price:,.0f}")
print(f"SS_tot (total variance): ${ss_tot:,.0f}")
print(f"SS_res (unexplained variance): ${ss_res:,.0f}")
print(f"R² = 1 - ({ss_res:,.0f} / {ss_tot:,.0f})")
print(f"R² (manual): {r2_manual:.4f}")
print(f"R² (sklearn): {r2_sklearn:.4f}")

print(f"\nInterpretation: Our model explains {r2_sklearn*100:.1f}% of the variance in house prices.")

# ========== VISUALIZING R² ==========
print("\n" + "=" * 60)
print("VISUALIZING R²")
print("=" * 60)

# Create visualizations
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# High R²
np.random.seed(42)
x_high = np.linspace(0, 10, 50)
y_high = 2 * x_high + 1 + np.random.randn(50) * 0.5
axes[0].scatter(x_high, y_high, alpha=0.6)
axes[0].plot(x_high, 2 * x_high + 1, color='red', linewidth=2)
axes[0].set_title(f'High R² ≈ 0.98\n(Points close to line)')
axes[0].set_xlabel('X')
axes[0].set_ylabel('Y')

# Medium R²
y_med = 2 * x_high + 1 + np.random.randn(50) * 3
axes[1].scatter(x_high, y_med, alpha=0.6)
axes[1].plot(x_high, 2 * x_high + 1, color='red', linewidth=2)
axes[1].set_title(f'Medium R² ≈ 0.70\n(More scatter)')
axes[1].set_xlabel('X')
axes[1].set_ylabel('Y')

# Low R²
y_low = 2 * x_high + 1 + np.random.randn(50) * 8
axes[2].scatter(x_high, y_low, alpha=0.6)
axes[2].plot(x_high, 2 * x_high + 1, color='red', linewidth=2)
axes[2].set_title(f'Low R² ≈ 0.35\n(High scatter)')
axes[2].set_xlabel('X')
axes[2].set_ylabel('Y')

plt.tight_layout()
plt.savefig('r2_comparison.png', dpi=100, bbox_inches='tight')
plt.close()
print("✅ R² comparison plot saved as 'r2_comparison.png'")

# ========== COMPLETE EXAMPLE ==========
print("\n" + "=" * 60)
print("COMPLETE EXAMPLE: Model Evaluation")
print("=" * 60)

# Create larger dataset
np.random.seed(42)
n = 100
X = np.random.uniform(500, 3500, n).reshape(-1, 1)
y = 150 * X.flatten() + 50000 + np.random.randn(n) * 30000

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

print("Model Performance:")
print("=" * 50)
print(f"{'Metric':<20} {'Train':>12} {'Test':>12}")
print("-" * 50)

# Calculate metrics
metrics = {
    'MSE': (mean_squared_error(y_train, y_train_pred), 
            mean_squared_error(y_test, y_test_pred)),
    'RMSE': (np.sqrt(mean_squared_error(y_train, y_train_pred)), 
             np.sqrt(mean_squared_error(y_test, y_test_pred))),
    'MAE': (mean_absolute_error(y_train, y_train_pred), 
            mean_absolute_error(y_test, y_test_pred)),
    'R²': (r2_score(y_train, y_train_pred), 
           r2_score(y_test, y_test_pred))
}

for name, (train_val, test_val) in metrics.items():
    if name == 'R²':
        print(f"{name:<20} {train_val:>12.4f} {test_val:>12.4f}")
    else:
        print(f"{name:<20} ${train_val:>11,.0f} ${test_val:>11,.0f}")

# ========== OVERFITTING VS UNDERFITTING ==========
print("\n" + "=" * 60)
print("DETECTING OVERFITTING VS UNDERFITTING")
print("=" * 60)

print("""
Compare Train vs Test metrics to detect problems:

GOOD MODEL:
- Train R² ≈ Test R² (similar performance)
- Both are reasonably high

OVERFITTING (model memorized training data):
- Train R² >> Test R² (much higher)
- High train, low test performance
- Solution: Regularization, more data, simpler model

UNDERFITTING (model too simple):
- Both Train R² and Test R² are low
- Model not capturing patterns
- Solution: More features, complex model

Example from our model:
""")

train_r2 = metrics['R²'][0]
test_r2 = metrics['R²'][1]
diff = abs(train_r2 - test_r2)

print(f"Train R²: {train_r2:.4f}")
print(f"Test R²:  {test_r2:.4f}")
print(f"Difference: {diff:.4f}")

if diff < 0.1 and test_r2 > 0.7:
    print("\n✅ Good fit! Train and test performance are similar and high.")
elif train_r2 > test_r2 + 0.15:
    print("\n⚠️ Possible overfitting. Train performance much better than test.")
elif train_r2 < 0.5 and test_r2 < 0.5:
    print("\n⚠️ Possible underfitting. Both scores are low.")

# ========== QUICK REFERENCE ==========
print("\n" + "=" * 60)
print("QUICK REFERENCE: WHEN TO USE EACH METRIC")
print("=" * 60)

print("""
| Metric | When to Use                    | Pros               | Cons               |
|--------|--------------------------------|--------------------|--------------------|
| MSE    | When large errors are costly   | Differentiable     | Hard to interpret  |
| RMSE   | Same as MSE, need same units   | Same units as y    | Sensitive to outliers |
| MAE    | Want robust to outliers        | Easy to interpret  | Not differentiable |
| R²     | Compare model quality          | Scale-independent  | Can be misleading  |

Best Practice: Report multiple metrics for complete picture!
""")

# Cleanup
import os
if os.path.exists('r2_comparison.png'):
    os.remove('r2_comparison.png')

print("\n" + "=" * 60)
print("✅ Evaluation Metrics - Complete!")
print("=" * 60)
