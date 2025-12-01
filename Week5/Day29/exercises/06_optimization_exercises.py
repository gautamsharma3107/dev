"""
EXERCISES: Optimization
========================
Complete all 5 exercises below
"""

import numpy as np

# Exercise 1: Basic Gradient Descent
# TODO: Implement gradient descent to find minimum of f(x) = x^2
# Starting point: x = 5
# Learning rate: 0.1
# Run for 10 iterations
# Print x and f(x) at each step

print("Exercise 1: Basic Gradient Descent")
print("-" * 40)
# Your code here


# Exercise 2: Gradient Descent with Momentum
# TODO: Implement gradient descent with momentum
# Same function f(x) = x^2
# Starting point: x = 5
# Learning rate: 0.1, Momentum (beta): 0.9
# Compare convergence with basic GD

print("\n\nExercise 2: Gradient Descent with Momentum")
print("-" * 40)
# Your code here


# Exercise 3: Learning Rate Comparison
# TODO: Run gradient descent with different learning rates
# Test: lr = 0.01, 0.1, 0.5, 1.0
# Function: f(x) = x^2, starting x = 5
# Run 20 iterations each
# Print final x value for each learning rate

print("\n\nExercise 3: Learning Rate Comparison")
print("-" * 40)
# Your code here


# Exercise 4: Learning Rate Schedule
# TODO: Implement exponential decay learning rate
# Initial lr = 0.5
# Decay formula: lr = initial_lr * exp(-0.1 * epoch)
# Calculate lr for epochs 0, 5, 10, 15, 20

print("\n\nExercise 4: Learning Rate Schedule")
print("-" * 40)
# Your code here


# Exercise 5: Mini-batch vs Full Batch
# TODO: Simulate the difference between mini-batch and full batch gradient descent
# Create "data" as 100 random points
# For full batch: average gradient over all points
# For mini-batch (size 10): average gradient over batch
# Show that mini-batch gradient is noisier but faster

print("\n\nExercise 5: Mini-batch vs Full Batch")
print("-" * 40)
# Your code here
