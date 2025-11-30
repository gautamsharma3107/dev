"""
EXERCISES: Neural Network Basics
=================================
Complete all 5 exercises below
"""

import numpy as np

# Exercise 1: Understanding Neural Network Components
# TODO: Create a dictionary that represents a simple neural network
# Include: input_size, hidden_layers (list of sizes), output_size, activation
# Print the network architecture

print("Exercise 1: Neural Network Architecture")
print("-" * 40)
# Your code here


# Exercise 2: Implement a Single Neuron
# TODO: Create a function that simulates a single neuron
# Parameters: inputs (list), weights (list), bias (float)
# Return: weighted sum + bias
# Test with inputs=[1, 2, 3], weights=[0.5, -0.3, 0.2], bias=0.1

print("\n\nExercise 2: Single Neuron")
print("-" * 40)
# Your code here


# Exercise 3: Weight Initialization
# TODO: Create a function that initializes weights using Xavier initialization
# Formula: weights = np.random.randn(input_size, output_size) * sqrt(2/input_size)
# Initialize weights for a layer with 4 inputs and 3 outputs

print("\n\nExercise 3: Weight Initialization")
print("-" * 40)
# Your code here


# Exercise 4: Layer Output Calculation
# TODO: Calculate the output of a layer given:
# inputs: np.array([[1, 2, 3]])
# weights: np.array([[0.1, 0.2], [0.3, 0.4], [0.5, 0.6]])
# bias: np.array([[0.1, 0.2]])
# Use: output = inputs @ weights + bias

print("\n\nExercise 4: Layer Output")
print("-" * 40)
# Your code here


# Exercise 5: Count Parameters
# TODO: Write a function that counts total trainable parameters in a network
# For a network with layers [784, 128, 64, 10]
# Parameters = weights + biases for each layer
# weights between layer i and i+1 = layer_i * layer_i+1
# biases for layer i+1 = layer_i+1

print("\n\nExercise 5: Parameter Count")
print("-" * 40)
# Your code here
