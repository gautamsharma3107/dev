"""
EXERCISES: Loss Functions
==========================
Complete all 5 exercises below
"""

import numpy as np

# Exercise 1: Mean Squared Error
# TODO: Implement MSE loss function
# Formula: MSE = (1/n) * sum((y_true - y_pred)^2)
# Test with y_true = [1, 2, 3, 4], y_pred = [1.1, 2.2, 2.8, 4.1]

print("Exercise 1: Mean Squared Error")
print("-" * 40)
# Your code here


# Exercise 2: Binary Cross-Entropy
# TODO: Implement Binary Cross-Entropy loss
# Formula: BCE = -(1/n) * sum(y*log(p) + (1-y)*log(1-p))
# Add small epsilon (1e-15) to avoid log(0)
# Test with y_true = [1, 0, 1, 0], y_pred = [0.9, 0.2, 0.8, 0.3]

print("\n\nExercise 2: Binary Cross-Entropy")
print("-" * 40)
# Your code here


# Exercise 3: Categorical Cross-Entropy
# TODO: Implement Categorical Cross-Entropy
# y_true should be one-hot encoded
# Test with:
# y_true = [[1,0,0], [0,1,0], [0,0,1]]
# y_pred = [[0.8,0.1,0.1], [0.2,0.7,0.1], [0.1,0.2,0.7]]

print("\n\nExercise 3: Categorical Cross-Entropy")
print("-" * 40)
# Your code here


# Exercise 4: Loss Comparison
# TODO: Compare MSE and MAE on the same predictions
# Generate predictions with some outliers
# y_true = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# y_pred = [1.1, 2.1, 2.9, 4.2, 5.0, 6.1, 7.0, 8.2, 9.0, 25.0]  # Note the large outlier at end
# Calculate both MSE and MAE - which is more affected by the outlier?

print("\n\nExercise 4: Loss Comparison")
print("-" * 40)
# Your code here


# Exercise 5: Loss Function Derivatives
# TODO: Implement the derivative of MSE with respect to predictions
# Formula: d(MSE)/d(y_pred) = (2/n) * (y_pred - y_true)
# This is used in backpropagation
# Calculate gradient for y_true = [1, 2, 3], y_pred = [1.5, 2.5, 2.5]

print("\n\nExercise 5: Loss Derivatives")
print("-" * 40)
# Your code here
