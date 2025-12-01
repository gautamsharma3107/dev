"""
Day 25 - Linear Regression
==========================
Learn: Linear regression fundamentals and implementation

Key Concepts:
- Linear relationship between features and target
- Finding the best fit line
- Using scikit-learn for linear regression
- Simple vs Multiple linear regression
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# ========== WHAT IS LINEAR REGRESSION? ==========
print("=" * 60)
print("WHAT IS LINEAR REGRESSION?")
print("=" * 60)

print("""
Linear regression finds a straight line that best fits your data.

For one feature (Simple Linear Regression):
    y = mx + b
    
    where:
    - y = target/output (what we predict)
    - x = feature/input
    - m = slope (coefficient)
    - b = intercept

For multiple features (Multiple Linear Regression):
    y = b0 + b1*x1 + b2*x2 + ... + bn*xn
    
    where:
    - b0 = intercept
    - b1, b2, ... bn = coefficients for each feature

The goal: Find the values of m and b (or b0, b1, ...) that 
minimize the error between predictions and actual values.
""")

# ========== SIMPLE LINEAR REGRESSION ==========
print("\n" + "=" * 60)
print("SIMPLE LINEAR REGRESSION")
print("=" * 60)

# Create sample data: Study hours vs Exam score
np.random.seed(42)
hours_studied = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
exam_scores = np.array([52, 58, 65, 68, 73, 79, 84, 88, 92, 96])

# Add some noise
noise = np.random.randn(10) * 3
exam_scores = exam_scores + noise

print("Study Hours vs Exam Scores:")
print("-" * 30)
for h, s in zip(hours_studied.flatten(), exam_scores):
    print(f"Hours: {h:2d} | Score: {s:.1f}")

# Create and train the model
model = LinearRegression()
model.fit(hours_studied, exam_scores)

print(f"\nModel trained!")
print(f"Slope (coefficient): {model.coef_[0]:.2f}")
print(f"Intercept: {model.intercept_:.2f}")
print(f"\nEquation: Score = {model.coef_[0]:.2f} * Hours + {model.intercept_:.2f}")

# Make predictions
print("\nPredictions:")
print("-" * 30)
test_hours = np.array([[5], [7], [12]])
predictions = model.predict(test_hours)
for h, p in zip(test_hours.flatten(), predictions):
    print(f"Hours: {h:2d} | Predicted Score: {p:.1f}")

# ========== VISUALIZING LINEAR REGRESSION ==========
print("\n" + "=" * 60)
print("VISUALIZING LINEAR REGRESSION")
print("=" * 60)

plt.figure(figsize=(10, 6))
plt.scatter(hours_studied, exam_scores, color='blue', label='Actual Data')
plt.plot(hours_studied, model.predict(hours_studied), color='red', 
         linewidth=2, label='Best Fit Line')
plt.xlabel('Hours Studied')
plt.ylabel('Exam Score')
plt.title('Linear Regression: Study Hours vs Exam Score')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('linear_regression_plot.png', dpi=100, bbox_inches='tight')
plt.close()
print("✅ Plot saved as 'linear_regression_plot.png'")

# ========== MULTIPLE LINEAR REGRESSION ==========
print("\n" + "=" * 60)
print("MULTIPLE LINEAR REGRESSION")
print("=" * 60)

# Create sample data with multiple features
# Features: Hours studied, Previous score, Sleep hours
np.random.seed(42)
n_samples = 100

hours_studied_multi = np.random.uniform(1, 10, n_samples)
previous_score = np.random.uniform(40, 90, n_samples)
sleep_hours = np.random.uniform(4, 9, n_samples)

# Target: Exam score (based on all features + noise)
exam_scores_multi = (
    5 * hours_studied_multi + 
    0.5 * previous_score + 
    2 * sleep_hours + 
    20 +
    np.random.randn(n_samples) * 5
)

# Combine features
X = np.column_stack([hours_studied_multi, previous_score, sleep_hours])
y = exam_scores_multi

print("Dataset shape:")
print(f"Features (X): {X.shape}")
print(f"Target (y): {y.shape}")

print("\nFeature names: Hours Studied, Previous Score, Sleep Hours")
print(f"\nSample data (first 5 rows):")
print("-" * 60)
print("Hours | Prev Score | Sleep | Exam Score")
print("-" * 60)
for i in range(5):
    print(f"{X[i, 0]:5.1f} | {X[i, 1]:10.1f} | {X[i, 2]:5.1f} | {y[i]:6.1f}")

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"\nTrain set: {X_train.shape[0]} samples")
print(f"Test set: {X_test.shape[0]} samples")

# Train model
multi_model = LinearRegression()
multi_model.fit(X_train, y_train)

print("\nModel Coefficients:")
print("-" * 40)
feature_names = ['Hours Studied', 'Previous Score', 'Sleep Hours']
for name, coef in zip(feature_names, multi_model.coef_):
    print(f"{name:15s}: {coef:7.3f}")
print(f"{'Intercept':15s}: {multi_model.intercept_:.3f}")

# Predictions
y_pred = multi_model.predict(X_test)

print("\nPredictions vs Actual (first 5):")
print("-" * 40)
print("Predicted | Actual | Difference")
for pred, actual in list(zip(y_pred, y_test))[:5]:
    print(f"{pred:9.1f} | {actual:6.1f} | {pred - actual:+.1f}")

# ========== UNDERSTANDING COEFFICIENTS ==========
print("\n" + "=" * 60)
print("UNDERSTANDING COEFFICIENTS")
print("=" * 60)

print("""
Each coefficient tells you how much y changes when that feature 
increases by 1 unit (holding other features constant).

In our model:
""")

for name, coef in zip(feature_names, multi_model.coef_):
    direction = "increases" if coef > 0 else "decreases"
    print(f"- {name}: For each 1-unit increase, score {direction} by {abs(coef):.2f}")

# ========== TRAINING PROCESS ==========
print("\n" + "=" * 60)
print("HOW LINEAR REGRESSION WORKS")
print("=" * 60)

print("""
Linear regression uses 'Ordinary Least Squares' (OLS):

1. Start with a random line
2. Calculate error = actual - predicted for each point
3. Square the errors (to make all positive)
4. Sum all squared errors (SSE)
5. Find the line that minimizes this sum

The math finds the optimal coefficients directly!

Loss Function: Sum of Squared Errors (SSE)
    SSE = Σ(y_actual - y_predicted)²

Goal: Minimize SSE
""")

# ========== ASSUMPTIONS OF LINEAR REGRESSION ==========
print("\n" + "=" * 60)
print("ASSUMPTIONS OF LINEAR REGRESSION")
print("=" * 60)

print("""
For best results, linear regression assumes:

1. LINEARITY
   - Relationship between X and y is linear
   - Check: Scatter plot should show linear pattern

2. INDEPENDENCE
   - Observations are independent of each other
   - No autocorrelation

3. HOMOSCEDASTICITY
   - Variance of errors is constant
   - Check: Residuals plot should be uniform

4. NORMALITY
   - Errors are normally distributed
   - Check: Histogram of residuals

5. NO MULTICOLLINEARITY
   - Features shouldn't be highly correlated with each other
   - Check: Correlation matrix

When assumptions are violated:
- Use regularization (Ridge, Lasso)
- Transform features
- Use different algorithms
""")

# ========== PRACTICAL EXAMPLE ==========
print("\n" + "=" * 60)
print("PRACTICAL EXAMPLE: Salary Prediction")
print("=" * 60)

# Create salary data
np.random.seed(42)
years_exp = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
salary = np.array([
    35000, 42000, 48000, 55000, 62000, 68000, 75000, 82000,
    88000, 95000, 102000, 108000, 115000, 122000, 130000
])

# Add some noise
salary = salary + np.random.randn(15) * 3000

print("Years of Experience vs Salary:")
print("-" * 40)
for y_exp, sal in zip(years_exp, salary):
    print(f"Years: {y_exp:2d} | Salary: ${sal:,.0f}")

# Reshape for sklearn
X_salary = years_exp.reshape(-1, 1)
y_salary = salary

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X_salary, y_salary, test_size=0.2, random_state=42
)

# Train model
salary_model = LinearRegression()
salary_model.fit(X_train, y_train)

print(f"\nModel: Salary = {salary_model.coef_[0]:,.0f} * Years + {salary_model.intercept_:,.0f}")

# Predictions
print("\nSalary Predictions:")
new_years = [[3], [7], [15], [20]]
for years in new_years:
    pred = salary_model.predict([years])[0]
    print(f"  {years[0]} years experience: ${pred:,.0f}")

# Calculate R² score
from sklearn.metrics import r2_score
y_pred = salary_model.predict(X_test)
r2 = r2_score(y_test, y_pred)
print(f"\nModel R² Score: {r2:.4f}")
print(f"This means our model explains {r2*100:.1f}% of the variance in salary.")

# Cleanup
import os
if os.path.exists('linear_regression_plot.png'):
    os.remove('linear_regression_plot.png')

print("\n" + "=" * 60)
print("✅ Linear Regression - Complete!")
print("=" * 60)
