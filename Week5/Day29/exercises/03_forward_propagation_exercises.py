"""
EXERCISES: Forward Propagation
===============================
Complete all 5 exercises below
"""

import numpy as np

# Helper functions (use these in your exercises)
def relu(x):
    return np.maximum(0, x)

def sigmoid(x):
    return 1 / (1 + np.exp(-np.clip(x, -500, 500)))

def softmax(x):
    exp_x = np.exp(x - np.max(x, axis=-1, keepdims=True))
    return exp_x / np.sum(exp_x, axis=-1, keepdims=True)


# Exercise 1: Single Layer Forward Pass
# TODO: Implement forward pass for a single layer
# Given: inputs (2,3), weights (3,4), bias (1,4)
# Calculate: z = inputs @ weights + bias
# Apply ReLU activation

print("Exercise 1: Single Layer Forward Pass")
print("-" * 40)
np.random.seed(42)
inputs = np.random.randn(2, 3)
weights = np.random.randn(3, 4)
bias = np.zeros((1, 4))
# Your code here


# Exercise 2: Two Layer Network
# TODO: Implement forward pass for a 2-layer network
# Layer 1: 3 inputs -> 4 hidden (ReLU)
# Layer 2: 4 hidden -> 2 outputs (Sigmoid)
# Use the same random seed for reproducibility

print("\n\nExercise 2: Two Layer Network")
print("-" * 40)
np.random.seed(42)
X = np.array([[1.0, 2.0, 3.0]])
# Your code here


# Exercise 3: Batch Processing
# TODO: Process a batch of 4 samples through a single layer
# Input shape: (4, 3) - 4 samples, 3 features each
# Layer: 3 inputs -> 2 outputs
# Apply softmax to get probability distribution

print("\n\nExercise 3: Batch Processing")
print("-" * 40)
np.random.seed(42)
X_batch = np.array([
    [1.0, 2.0, 0.5],
    [0.5, 1.0, 1.5],
    [2.0, 0.0, 1.0],
    [-1.0, 1.5, 0.5]
])
# Your code here


# Exercise 4: Multi-class Classification Forward Pass
# TODO: Build a network for 3-class classification
# Architecture: 4 features -> 5 hidden (ReLU) -> 3 classes (Softmax)
# Print the probability for each class

print("\n\nExercise 4: Multi-class Classification")
print("-" * 40)
np.random.seed(42)
X_sample = np.array([[0.5, 1.2, -0.3, 0.8]])
# Your code here


# Exercise 5: Forward Pass with Caching
# TODO: Implement forward pass that stores intermediate values
# Create a dictionary 'cache' that stores Z and A for each layer
# This will be needed for backpropagation later

print("\n\nExercise 5: Forward Pass with Caching")
print("-" * 40)
# Your code here
