"""
DAY 25 ASSESSMENT TEST
======================
Total: 14 points
Pass: 10+ points (70%)
Time: 15 minutes
"""

print("=" * 60)
print("DAY 25 ASSESSMENT - Regression Models")
print("=" * 60)
print("Total Points: 14 | Passing Score: 10 (70%)")
print("=" * 60)

# ============================================================
# SECTION A: Multiple Choice Questions (6 points)
# ============================================================

print("\n" + "=" * 60)
print("SECTION A: Multiple Choice (6 points)")
print("=" * 60)

print("""
Q1. In linear regression y = mx + b, what does 'm' represent?
a) The y-intercept
b) The slope (coefficient)
c) The mean of y
d) The error term

Your answer: """)

print("""
Q2. Which metric is in the same units as the target variable?
a) MSE (Mean Squared Error)
b) R² (R-squared)
c) RMSE (Root Mean Squared Error)
d) Coefficient of variation

Your answer: """)

print("""
Q3. An R² score of 0.85 means:
a) 85% of predictions are correct
b) The model explains 85% of variance in the data
c) 85% of data points are on the regression line
d) The model has 85% accuracy

Your answer: """)

print("""
Q4. When should you use polynomial regression?
a) When the relationship between X and y is linear
b) When you have too many features
c) When the relationship between X and y is non-linear
d) When you need feature selection

Your answer: """)

print("""
Q5. What is the main difference between Ridge and Lasso?
a) Ridge is faster than Lasso
b) Lasso can set coefficients exactly to zero, Ridge cannot
c) Ridge works with larger datasets
d) Lasso requires more data

Your answer: """)

print("""
Q6. If train R² is 0.95 and test R² is 0.60, this indicates:
a) Underfitting
b) Overfitting
c) Good generalization
d) Perfect model

Your answer: """)

# ============================================================
# SECTION B: Coding Challenges (6 points)
# ============================================================

print("\n" + "=" * 60)
print("SECTION B: Coding Challenges (6 points)")
print("=" * 60)

print("""
Q7. (2 points) Write code to train a linear regression model
    and calculate its R² score on test data.
    Given: X_train, X_test, y_train, y_test are already defined.
""")

# Write your code here:




print("""
Q8. (2 points) Write code to calculate RMSE (Root Mean Squared Error)
    given y_true and y_pred arrays.
    Use sklearn metrics.
""")

# Write your code here:




print("""
Q9. (2 points) Write code to apply polynomial features (degree=2)
    to X_train and X_test, then fit a Ridge regression model.
""")

# Write your code here:




# ============================================================
# SECTION C: Conceptual Question (2 points)
# ============================================================

print("\n" + "=" * 60)
print("SECTION C: Conceptual Question (2 points)")
print("=" * 60)

print("""
Q10. (2 points) Explain when you would choose Lasso over Ridge
     regression. Give a specific use case example.

Your answer:
""")

# Write your explanation here as comments:
#




print("\n" + "=" * 60)
print("TEST COMPLETE!")
print("=" * 60)

"""
ANSWER KEY
==========

Section A:
Q1: b) The slope (coefficient)
Q2: c) RMSE (Root Mean Squared Error)
Q3: b) The model explains 85% of variance in the data
Q4: c) When the relationship between X and y is non-linear
Q5: b) Lasso can set coefficients exactly to zero, Ridge cannot
Q6: b) Overfitting

Section B:
Q7:
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
print(f"R² Score: {r2}")

Q8:
from sklearn.metrics import mean_squared_error
import numpy as np

mse = mean_squared_error(y_true, y_pred)
rmse = np.sqrt(mse)
print(f"RMSE: {rmse}")

# Or using squared=False (sklearn >= 0.24)
rmse = mean_squared_error(y_true, y_pred, squared=False)

Q9:
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import Ridge

# Create polynomial features
poly = PolynomialFeatures(degree=2, include_bias=False)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

# Fit Ridge model
ridge = Ridge(alpha=1.0)
ridge.fit(X_train_poly, y_train)

Section C:
Q10:
Choose Lasso over Ridge when:
- You have many features and suspect some are irrelevant
- You need automatic feature selection
- You want a sparse model (fewer non-zero coefficients)
- Interpretability is important

Example use case:
In predicting house prices with 50 features (including noise),
Lasso can automatically identify the 10 most important features
by setting irrelevant coefficients to zero, while Ridge would
keep all 50 features with small but non-zero weights.
"""
