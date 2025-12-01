"""
Day 25 - Regression Exercises
=============================
Practice exercises for regression concepts.
Complete each exercise and run to verify your solutions.
"""

import numpy as np
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# ============================================================
# EXERCISE 1: Simple Linear Regression
# ============================================================
print("=" * 60)
print("EXERCISE 1: Simple Linear Regression")
print("=" * 60)

"""
Task: Create a linear regression model to predict salary based 
on years of experience.

Given data:
- years: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
- salary: [30000, 35000, 42000, 48000, 55000, 61000, 68000, 75000, 81000, 88000]

Steps:
1. Reshape the data for sklearn
2. Create and fit a LinearRegression model
3. Print the slope and intercept
4. Predict salary for 5.5 years of experience
"""

print("\nYour code here:")
# TODO: Complete the exercise

years = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
salary = np.array([30000, 35000, 42000, 48000, 55000, 61000, 68000, 75000, 81000, 88000])

# Your solution:




print("\n--- Expected Output ---")
print("Slope: ~6400")
print("Intercept: ~24000")
print("Predicted salary for 5.5 years: ~$59,200")

# ============================================================
# EXERCISE 2: Calculate Evaluation Metrics
# ============================================================
print("\n" + "=" * 60)
print("EXERCISE 2: Calculate Evaluation Metrics")
print("=" * 60)

"""
Task: Calculate MSE, RMSE, MAE, and R² for the given predictions.

Given:
- y_actual: [100, 150, 200, 250, 300]
- y_predicted: [110, 145, 190, 260, 310]

Calculate and print all four metrics.
"""

print("\nYour code here:")
# TODO: Complete the exercise

y_actual = np.array([100, 150, 200, 250, 300])
y_predicted = np.array([110, 145, 190, 260, 310])

# Your solution:




print("\n--- Expected Output ---")
print("MSE: 90")
print("RMSE: 9.49")
print("MAE: 8.0")
print("R²: ~0.991")

# ============================================================
# EXERCISE 3: Polynomial Regression
# ============================================================
print("\n" + "=" * 60)
print("EXERCISE 3: Polynomial Regression")
print("=" * 60)

"""
Task: Fit a polynomial regression to the following non-linear data.

Given data (represents projectile motion):
- time: [0, 1, 2, 3, 4, 5]
- height: [0, 45, 80, 105, 120, 125]

Steps:
1. Create polynomial features (degree=2)
2. Fit linear regression on polynomial features
3. Calculate R² score
4. Predict height at time=2.5
"""

print("\nYour code here:")
# TODO: Complete the exercise

time = np.array([0, 1, 2, 3, 4, 5]).reshape(-1, 1)
height = np.array([0, 45, 80, 105, 120, 125])

# Your solution:




print("\n--- Expected Output ---")
print("R² Score: ~0.998")
print("Predicted height at time=2.5: ~93")

# ============================================================
# EXERCISE 4: Compare Linear vs Polynomial
# ============================================================
print("\n" + "=" * 60)
print("EXERCISE 4: Compare Linear vs Polynomial")
print("=" * 60)

"""
Task: Compare linear and polynomial (degree=3) regression on the data.

Given data:
X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]  # y = x²

Steps:
1. Fit linear regression, calculate R²
2. Fit polynomial regression (degree=3), calculate R²
3. Print which model is better and why
"""

print("\nYour code here:")
# TODO: Complete the exercise

X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
y = np.array([1, 4, 9, 16, 25, 36, 49, 64, 81, 100])

# Your solution:




print("\n--- Expected Output ---")
print("Linear R²: ~0.90")
print("Polynomial R²: ~1.00")
print("Polynomial is better because data follows y=x² pattern")

# ============================================================
# EXERCISE 5: Ridge vs Lasso Feature Selection
# ============================================================
print("\n" + "=" * 60)
print("EXERCISE 5: Ridge vs Lasso Feature Selection")
print("=" * 60)

"""
Task: Compare how Ridge and Lasso handle feature selection.

Given: A dataset with 3 useful features and 2 noise features.

Steps:
1. Create synthetic data (provided below)
2. Fit Ridge (alpha=1) and print coefficients
3. Fit Lasso (alpha=1) and print coefficients
4. Observe which model eliminates noise features
"""

print("\nYour code here:")
# TODO: Complete the exercise

np.random.seed(42)
n = 100

# Useful features
x1 = np.random.randn(n)
x2 = np.random.randn(n)
x3 = np.random.randn(n)
# Noise features
noise1 = np.random.randn(n) * 0.01
noise2 = np.random.randn(n) * 0.01

X = np.column_stack([x1, x2, x3, noise1, noise2])
y = 3*x1 + 2*x2 + 1*x3 + np.random.randn(n) * 0.1

feature_names = ['x1', 'x2', 'x3', 'noise1', 'noise2']

# Your solution:




print("\n--- Expected Output ---")
print("Ridge keeps all coefficients non-zero")
print("Lasso sets noise coefficients closer to zero")

# ============================================================
# BONUS EXERCISE: Find Optimal Alpha
# ============================================================
print("\n" + "=" * 60)
print("BONUS: Find Optimal Alpha")
print("=" * 60)

"""
Task: Use cross-validation to find the optimal alpha for Ridge.

Steps:
1. Use the X and y from Exercise 5
2. Split data into train/test
3. Use RidgeCV to find best alpha from [0.01, 0.1, 1, 10, 100]
4. Print the best alpha and test R²
"""

print("\nYour code here:")
# TODO: Complete the exercise

# Your solution:




print("\n--- Expected Output ---")
print("Best alpha found via cross-validation")
print("Test R² should be > 0.99 for this clean data")

print("\n" + "=" * 60)
print("EXERCISES COMPLETE!")
print("=" * 60)
