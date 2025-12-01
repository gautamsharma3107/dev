"""
Day 25 - Polynomial Regression
==============================
Learn: How to model non-linear relationships with polynomial features

Key Concepts:
- When linear isn't enough
- Creating polynomial features
- Avoiding overfitting with higher degrees
- Choosing the right polynomial degree
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# ========== WHY POLYNOMIAL REGRESSION? ==========
print("=" * 60)
print("WHY POLYNOMIAL REGRESSION?")
print("=" * 60)

print("""
Sometimes data doesn't follow a straight line!

Examples:
- Growth curves (population, bacteria)
- Physical phenomena (projectile motion)
- Economic trends (diminishing returns)
- Temperature changes (seasonal patterns)

Linear: y = b0 + b1*x

Polynomial: y = b0 + b1*x + b2*x² + b3*x³ + ...

The idea: Transform features into polynomial terms,
then use regular linear regression!
""")

# ========== VISUALIZING THE PROBLEM ==========
print("\n" + "=" * 60)
print("VISUALIZING THE PROBLEM")
print("=" * 60)

# Create non-linear data
np.random.seed(42)
X = np.linspace(-3, 3, 50).reshape(-1, 1)
y = 2 + 3*X.flatten() - 1.5*X.flatten()**2 + np.random.randn(50) * 1.5

print("Generated non-linear data (parabola with noise)")
print(f"X range: [{X.min():.1f}, {X.max():.1f}]")
print(f"y range: [{y.min():.1f}, {y.max():.1f}]")

# Fit linear regression
linear_model = LinearRegression()
linear_model.fit(X, y)
y_linear_pred = linear_model.predict(X)

r2_linear = r2_score(y, y_linear_pred)
print(f"\nLinear Regression R²: {r2_linear:.4f}")
print("Linear model can't capture the curve!")

# ========== CREATING POLYNOMIAL FEATURES ==========
print("\n" + "=" * 60)
print("CREATING POLYNOMIAL FEATURES")
print("=" * 60)

print("""
PolynomialFeatures transforms:
    x → [1, x, x², x³, ...]

Example with degree=2:
    Original: [3]
    Transformed: [1, 3, 9]  (1, x, x²)

Example with degree=3:
    Original: [2]
    Transformed: [1, 2, 4, 8]  (1, x, x², x³)
""")

# Demo transformation
sample_X = np.array([[2], [3], [4]])
poly = PolynomialFeatures(degree=3, include_bias=True)
sample_X_poly = poly.fit_transform(sample_X)

print("Demonstration:")
print("-" * 40)
print("Original X | Polynomial Features (degree=3)")
print("-" * 40)
for orig, transformed in zip(sample_X.flatten(), sample_X_poly):
    print(f"    {orig}      | {transformed}")

# ========== POLYNOMIAL REGRESSION STEP BY STEP ==========
print("\n" + "=" * 60)
print("POLYNOMIAL REGRESSION STEP BY STEP")
print("=" * 60)

print("""
Steps:
1. Create PolynomialFeatures transformer
2. Transform X into polynomial features
3. Fit LinearRegression on transformed features
4. Predict and evaluate
""")

# Step 1 & 2: Transform features
degree = 2
poly_features = PolynomialFeatures(degree=degree, include_bias=False)
X_poly = poly_features.fit_transform(X)

print(f"\nStep 1-2: Transform to degree {degree}")
print(f"Original shape: {X.shape}")
print(f"Polynomial shape: {X_poly.shape}")
print(f"Features: x, x²")

# Step 3: Fit model
poly_model = LinearRegression()
poly_model.fit(X_poly, y)

print("\nStep 3: Fit model")
print(f"Coefficients: {poly_model.coef_}")
print(f"Intercept: {poly_model.intercept_:.4f}")

# Step 4: Predict
y_poly_pred = poly_model.predict(X_poly)
r2_poly = r2_score(y, y_poly_pred)

print(f"\nStep 4: Evaluate")
print(f"Polynomial R²: {r2_poly:.4f}")
print(f"Improvement over linear: {(r2_poly - r2_linear)*100:.1f}%")

# ========== COMPARING DIFFERENT DEGREES ==========
print("\n" + "=" * 60)
print("COMPARING DIFFERENT POLYNOMIAL DEGREES")
print("=" * 60)

# Create comparison data
np.random.seed(42)
X_compare = np.linspace(0, 10, 100).reshape(-1, 1)
y_compare = np.sin(X_compare.flatten()) * 5 + np.random.randn(100) * 0.5

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X_compare, y_compare, test_size=0.2, random_state=42
)

print("Testing degrees 1 through 10:")
print("-" * 60)
print(f"{'Degree':<8} {'Train R²':<12} {'Test R²':<12} {'Status'}")
print("-" * 60)

results = []
for degree in range(1, 11):
    # Transform
    poly = PolynomialFeatures(degree=degree, include_bias=False)
    X_train_poly = poly.fit_transform(X_train)
    X_test_poly = poly.transform(X_test)
    
    # Fit
    model = LinearRegression()
    model.fit(X_train_poly, y_train)
    
    # Evaluate
    train_r2 = r2_score(y_train, model.predict(X_train_poly))
    test_r2 = r2_score(y_test, model.predict(X_test_poly))
    
    # Status
    if test_r2 < 0:
        status = "❌ Severe Overfit"
    elif train_r2 - test_r2 > 0.3:
        status = "⚠️ Overfitting"
    elif test_r2 > 0.8:
        status = "✅ Good"
    elif test_r2 > 0.5:
        status = "→ Moderate"
    else:
        status = "→ Underfitting"
    
    results.append((degree, train_r2, test_r2))
    print(f"{degree:<8} {train_r2:<12.4f} {test_r2:<12.4f} {status}")

print("""
Key Observations:
- Low degree → Underfitting (can't capture pattern)
- Right degree → Good fit (similar train/test scores)
- High degree → Overfitting (train >> test, test may be negative!)
""")

# ========== OVERFITTING DEMONSTRATION ==========
print("\n" + "=" * 60)
print("OVERFITTING DEMONSTRATION")
print("=" * 60)

# Small dataset to show overfitting clearly
np.random.seed(42)
X_small = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(-1, 1)
y_small = np.array([2.5, 3.5, 4.0, 5.5, 6.0, 7.5, 8.0, 9.5])

print("Small dataset (8 points):")
for x, y_val in zip(X_small.flatten(), y_small):
    print(f"  x={x}, y={y_val}")

print("\nFitting different polynomial degrees:")

# Plot setup
fig, axes = plt.subplots(1, 3, figsize=(15, 4))
X_plot = np.linspace(0.5, 8.5, 100).reshape(-1, 1)

for idx, degree in enumerate([1, 4, 7]):
    poly = PolynomialFeatures(degree=degree, include_bias=False)
    X_poly = poly.fit_transform(X_small)
    X_plot_poly = poly.transform(X_plot)
    
    model = LinearRegression()
    model.fit(X_poly, y_small)
    
    y_pred = model.predict(X_poly)
    y_plot = model.predict(X_plot_poly)
    
    mse = mean_squared_error(y_small, y_pred)
    
    axes[idx].scatter(X_small, y_small, color='blue', s=100, label='Data')
    axes[idx].plot(X_plot, y_plot, color='red', linewidth=2, label='Fit')
    axes[idx].set_title(f'Degree {degree}\nMSE: {mse:.4f}')
    axes[idx].set_xlabel('X')
    axes[idx].set_ylabel('Y')
    axes[idx].legend()
    axes[idx].set_ylim(0, 12)

plt.tight_layout()
plt.savefig('polynomial_comparison.png', dpi=100, bbox_inches='tight')
plt.close()
print("✅ Comparison plot saved as 'polynomial_comparison.png'")

print("""
Notice:
- Degree 1: Simple line, slightly underfit
- Degree 4: Good fit, captures trend
- Degree 7: Perfect fit on training data BUT wiggly curve!
  This will perform terribly on new data (overfitting)
""")

# ========== CHOOSING THE RIGHT DEGREE ==========
print("\n" + "=" * 60)
print("CHOOSING THE RIGHT POLYNOMIAL DEGREE")
print("=" * 60)

print("""
Methods to choose the right degree:

1. CROSS-VALIDATION
   - Split data multiple ways
   - Test on held-out data
   - Choose degree with best average test score

2. VISUAL INSPECTION
   - Plot the fit
   - Look for wiggly curves (overfit)
   - Look for missing patterns (underfit)

3. LEARNING CURVES
   - Plot train vs test error by degree
   - Gap indicates overfitting

4. DOMAIN KNOWLEDGE
   - Physics often suggests quadratic
   - Growth curves may be polynomial
   - Know your data!

Best Practice: Start simple, increase complexity only if needed.
""")

# ========== PRACTICAL EXAMPLE ==========
print("\n" + "=" * 60)
print("PRACTICAL EXAMPLE: Car Stopping Distance")
print("=" * 60)

# Create realistic stopping distance data
# Physics: stopping distance ∝ v² (kinetic energy)
np.random.seed(42)
speed = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]).reshape(-1, 1)  # mph
# Stopping distance follows quadratic relationship
stopping_dist = 0.01 * speed.flatten()**2 + 0.5 * speed.flatten() + np.random.randn(10) * 5

print("Speed (mph) vs Stopping Distance (feet):")
print("-" * 40)
for s, d in zip(speed.flatten(), stopping_dist):
    print(f"Speed: {s:3d} mph | Distance: {d:6.1f} ft")

# Compare linear vs quadratic
# Linear
linear_model = LinearRegression()
linear_model.fit(speed, stopping_dist)
linear_pred = linear_model.predict(speed)
linear_r2 = r2_score(stopping_dist, linear_pred)

# Quadratic
poly = PolynomialFeatures(degree=2, include_bias=False)
speed_poly = poly.fit_transform(speed)
quad_model = LinearRegression()
quad_model.fit(speed_poly, stopping_dist)
quad_pred = quad_model.predict(speed_poly)
quad_r2 = r2_score(stopping_dist, quad_pred)

print("\nModel Comparison:")
print("-" * 40)
print(f"Linear R²:    {linear_r2:.4f}")
print(f"Quadratic R²: {quad_r2:.4f}")

print("\nPredictions at 55 mph and 85 mph:")
test_speeds = np.array([[55], [85]])
test_poly = poly.transform(test_speeds)

for speed_val in [55, 85]:
    linear_p = linear_model.predict([[speed_val]])[0]
    quad_p = quad_model.predict(poly.transform([[speed_val]]))[0]
    print(f"\n{speed_val} mph:")
    print(f"  Linear prediction:    {linear_p:.1f} ft")
    print(f"  Quadratic prediction: {quad_p:.1f} ft")

print("""
The quadratic model better captures the physics:
- Kinetic energy = ½mv²
- Stopping distance proportional to energy
- This is why speeding is so dangerous at high speeds!
""")

# ========== COMPLETE WORKFLOW ==========
print("\n" + "=" * 60)
print("COMPLETE POLYNOMIAL REGRESSION WORKFLOW")
print("=" * 60)

print("""
1. EXPLORE DATA
   - Scatter plot to see relationship
   - Check if linear is appropriate

2. TRY POLYNOMIAL
   - Start with degree 2
   - Check train and test R²

3. INCREASE DEGREE IF NEEDED
   - Monitor for overfitting
   - Stop when test R² stops improving

4. VALIDATE
   - Cross-validation
   - Check predictions make sense
   
5. CONSIDER REGULARIZATION
   - Ridge/Lasso if overfitting persists
   - We'll cover this next!
""")

# Cleanup
import os
if os.path.exists('polynomial_comparison.png'):
    os.remove('polynomial_comparison.png')

print("\n" + "=" * 60)
print("✅ Polynomial Regression - Complete!")
print("=" * 60)
