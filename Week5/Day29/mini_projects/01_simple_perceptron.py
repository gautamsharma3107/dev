"""
MINI PROJECT 1: Simple Perceptron
==================================
Build a perceptron from scratch that can learn logical gates

Requirements:
1. Implement a Perceptron class with:
   - __init__: Initialize weights and bias
   - predict: Compute output for given input
   - train: Update weights using perceptron learning rule
2. Train on AND gate truth table
3. Train on OR gate truth table
4. Show that XOR cannot be learned (explain why)
5. Display learning progress and final accuracy
"""

import numpy as np

# Your code here
print("=" * 50)
print("SIMPLE PERCEPTRON")
print("=" * 50)

# TODO: Implement the Perceptron class

class Perceptron:
    def __init__(self, n_inputs, learning_rate=0.1):
        # Initialize weights and bias
        pass
    
    def predict(self, x):
        # Compute weighted sum and apply step function
        pass
    
    def train(self, X, y, epochs=100):
        # Train using perceptron learning rule
        # w_new = w_old + learning_rate * (y_true - y_pred) * x
        pass


# Training data for AND gate
# TODO: Create AND gate truth table

# Training data for OR gate
# TODO: Create OR gate truth table

# Train and test both gates
# TODO: Implement training and testing
