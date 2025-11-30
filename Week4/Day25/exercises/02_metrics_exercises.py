"""
Day 25 - Evaluation Metrics Exercises
=====================================
Practice exercises for understanding regression metrics.
"""

import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# ============================================================
# EXERCISE 1: Manual MSE Calculation
# ============================================================
print("=" * 60)
print("EXERCISE 1: Manual MSE Calculation")
print("=" * 60)

"""
Task: Calculate MSE manually (without sklearn) for these predictions.

Given:
- y_actual: [10, 20, 30, 40, 50]
- y_predicted: [12, 18, 32, 38, 52]

Steps:
1. Calculate error for each point (actual - predicted)
2. Square each error
3. Calculate mean of squared errors
4. Verify with sklearn's mean_squared_error
"""

print("\nYour code here:")
y_actual = np.array([10, 20, 30, 40, 50])
y_predicted = np.array([12, 18, 32, 38, 52])

# Your solution:




print("\n--- Expected Output ---")
print("Manual MSE: 4.0")
print("sklearn MSE: 4.0")

# ============================================================
# EXERCISE 2: Interpret R² Values
# ============================================================
print("\n" + "=" * 60)
print("EXERCISE 2: Interpret R² Values")
print("=" * 60)

"""
Task: Calculate R² for different prediction scenarios and interpret.

Given 3 sets of predictions for the same actual values:
- y_actual: [100, 200, 300, 400, 500]

Model A predictions: [110, 195, 305, 398, 502]
Model B predictions: [150, 220, 280, 420, 480]
Model C predictions: [300, 300, 300, 300, 300]  # Predicts mean always

Calculate R² for each and rank the models.
"""

print("\nYour code here:")
y_actual = np.array([100, 200, 300, 400, 500])
model_a = np.array([110, 195, 305, 398, 502])
model_b = np.array([150, 220, 280, 420, 480])
model_c = np.array([300, 300, 300, 300, 300])

# Your solution:




print("\n--- Expected Output ---")
print("Model A R²: ~0.998 (Excellent)")
print("Model B R²: ~0.960 (Good)")
print("Model C R²: 0.0 (Just predicting mean)")

# ============================================================
# EXERCISE 3: MSE vs MAE with Outliers
# ============================================================
print("\n" + "=" * 60)
print("EXERCISE 3: MSE vs MAE with Outliers")
print("=" * 60)

"""
Task: Compare MSE and MAE sensitivity to outliers.

Scenario 1 (no outliers):
- y_actual: [10, 20, 30, 40, 50]
- y_pred: [11, 21, 29, 41, 49]

Scenario 2 (one outlier prediction):
- y_actual: [10, 20, 30, 40, 50]
- y_pred: [11, 21, 29, 41, 80]  # Last one is 30 off!

Calculate MSE and MAE for both. Which metric changes more with the outlier?
"""

print("\nYour code here:")
# Scenario 1
y_actual_1 = np.array([10, 20, 30, 40, 50])
y_pred_1 = np.array([11, 21, 29, 41, 49])

# Scenario 2
y_actual_2 = np.array([10, 20, 30, 40, 50])
y_pred_2 = np.array([11, 21, 29, 41, 80])

# Your solution:




print("\n--- Expected Output ---")
print("Scenario 1: MSE=1.0, MAE=1.0")
print("Scenario 2: MSE=181.0, MAE=7.0")
print("MSE increased 181x, MAE only 7x - MSE more sensitive to outliers!")

# ============================================================
# EXERCISE 4: When R² is Negative
# ============================================================
print("\n" + "=" * 60)
print("EXERCISE 4: When R² is Negative")
print("=" * 60)

"""
Task: Create predictions that result in negative R².

Given:
- y_actual: [10, 20, 30, 40, 50]

Create y_predicted values that result in R² < 0
(Hint: predictions worse than just predicting the mean)
"""

print("\nYour code here:")
y_actual = np.array([10, 20, 30, 40, 50])

# Your solution (create y_predicted that gives negative R²):
# y_predicted = ???




print("\n--- Expected Output ---")
print("A model that predicts opposite of the trend")
print("e.g., predicting [50, 40, 30, 20, 10] gives R² = -3.0")

# ============================================================
# EXERCISE 5: Complete Metrics Report
# ============================================================
print("\n" + "=" * 60)
print("EXERCISE 5: Complete Metrics Report")
print("=" * 60)

"""
Task: Create a function that generates a complete metrics report.

Function should:
1. Take y_actual and y_predicted as inputs
2. Calculate MSE, RMSE, MAE, R²
3. Print a formatted report
4. Return a dictionary with all metrics
"""

print("\nYour code here:")

def metrics_report(y_actual, y_predicted):
    """
    Generate a complete metrics report for regression predictions.
    
    Args:
        y_actual: Array of actual values
        y_predicted: Array of predicted values
    
    Returns:
        Dictionary with all metrics
    """
    # Your solution:
    pass




# Test your function
y_actual = np.array([100, 200, 300, 400, 500])
y_pred = np.array([110, 190, 310, 390, 510])

# result = metrics_report(y_actual, y_pred)

print("\n--- Expected Output ---")
print("=" * 40)
print("REGRESSION METRICS REPORT")
print("=" * 40)
print("MSE:  200.00")
print("RMSE: 14.14")
print("MAE:  10.00")
print("R²:   0.9900")
print("=" * 40)

print("\n" + "=" * 60)
print("EXERCISES COMPLETE!")
print("=" * 60)
