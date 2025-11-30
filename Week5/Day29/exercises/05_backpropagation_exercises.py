"""
EXERCISES: Backpropagation Concepts
====================================
Complete all 5 exercises below
"""

import numpy as np

# Helper functions
def sigmoid(x):
    return 1 / (1 + np.exp(-np.clip(x, -500, 500)))

def sigmoid_derivative(x):
    s = sigmoid(x)
    return s * (1 - s)

def relu(x):
    return np.maximum(0, x)

def relu_derivative(x):
    return (x > 0).astype(float)


# Exercise 1: Chain Rule Practice
# TODO: Given y = (2x + 3)^2, calculate dy/dx using chain rule
# Let u = 2x + 3, so y = u^2
# dy/dx = dy/du * du/dx
# Calculate dy/dx at x = 2

print("Exercise 1: Chain Rule Practice")
print("-" * 40)
# Your code here


# Exercise 2: Gradient of Sigmoid
# TODO: Calculate the gradient of sigmoid at multiple points
# Use sigmoid_derivative function above
# Calculate for x = [-2, -1, 0, 1, 2]
# Verify that gradient is maximum at x=0

print("\n\nExercise 2: Sigmoid Gradient")
print("-" * 40)
# Your code here


# Exercise 3: Simple Backprop - Single Neuron
# TODO: Implement backprop for a single neuron with sigmoid activation
# Forward: z = w*x + b, a = sigmoid(z)
# Loss: L = (y_true - a)^2
# Calculate: dL/dw and dL/db
# Given: x=2, w=0.5, b=0.1, y_true=1

print("\n\nExercise 3: Single Neuron Backprop")
print("-" * 40)
# Your code here


# Exercise 4: Weight Update
# TODO: Perform one step of gradient descent
# Given initial weights w = [0.5, -0.3, 0.2]
# Gradients dw = [0.1, -0.05, 0.2]
# Learning rate = 0.1
# Calculate: w_new = w - learning_rate * dw

print("\n\nExercise 4: Weight Update")
print("-" * 40)
# Your code here


# Exercise 5: Numerical Gradient Check
# TODO: Verify analytical gradient using numerical approximation
# For f(x) = x^2, df/dx = 2x
# Numerical gradient: (f(x+eps) - f(x-eps)) / (2*eps)
# Calculate both at x=3 with eps=0.0001
# They should be very close!

print("\n\nExercise 5: Gradient Check")
print("-" * 40)
# Your code here
