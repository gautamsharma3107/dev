"""
EXERCISES: Activation Functions
================================
Complete all 5 exercises below
"""

import numpy as np

# Exercise 1: Implement ReLU
# TODO: Implement the ReLU activation function
# Formula: f(x) = max(0, x)
# Test with values: [-2, -1, 0, 1, 2]

print("Exercise 1: ReLU Implementation")
print("-" * 40)
# Your code here


# Exercise 2: Implement Sigmoid
# TODO: Implement the Sigmoid activation function
# Formula: f(x) = 1 / (1 + e^(-x))
# Test with values: [-2, -1, 0, 1, 2]

print("\n\nExercise 2: Sigmoid Implementation")
print("-" * 40)
# Your code here


# Exercise 3: Implement Softmax
# TODO: Implement the Softmax function (numerically stable version)
# Formula: f(xi) = e^(xi) / sum(e^(xj))
# Tip: Subtract max(x) for numerical stability
# Test with values: [2.0, 1.0, 0.1]

print("\n\nExercise 3: Softmax Implementation")
print("-" * 40)
# Your code here


# Exercise 4: Compare Activations
# TODO: Create a comparison table showing output of ReLU, Sigmoid, and Tanh
# for inputs: [-3, -1, 0, 1, 3]
# Tanh formula: (e^x - e^(-x)) / (e^x + e^(-x))

print("\n\nExercise 4: Activation Comparison")
print("-" * 40)
# Your code here


# Exercise 5: Activation Derivatives
# TODO: Implement derivatives of ReLU and Sigmoid
# ReLU derivative: 1 if x > 0, else 0
# Sigmoid derivative: sigmoid(x) * (1 - sigmoid(x))
# Test both with x = [-2, -1, 0, 1, 2]

print("\n\nExercise 5: Activation Derivatives")
print("-" * 40)
# Your code here
