"""
MINI PROJECT 3: XOR Neural Network
===================================
Build a neural network that can solve the XOR problem

Requirements:
1. Implement a 2-layer neural network (2 -> 2 -> 1)
2. Use sigmoid activation
3. Implement forward propagation
4. Implement backpropagation
5. Train on XOR truth table
6. Display learning curve (loss over epochs)
7. Show final predictions

The XOR problem:
    (0, 0) -> 0
    (0, 1) -> 1
    (1, 0) -> 1
    (1, 1) -> 0
"""

import numpy as np

# Your code here
print("=" * 50)
print("XOR NEURAL NETWORK")
print("=" * 50)

# TODO: Implement the XOR solver

class XORNetwork:
    def __init__(self):
        # Initialize weights for 2->2->1 network
        np.random.seed(42)
        # Layer 1: 2 inputs -> 2 hidden
        # Layer 2: 2 hidden -> 1 output
        pass
    
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    
    def sigmoid_derivative(self, x):
        return x * (1 - x)
    
    def forward(self, X):
        # Forward pass through both layers
        pass
    
    def backward(self, X, y, output):
        # Backpropagation to compute gradients
        pass
    
    def train(self, X, y, epochs=10000, learning_rate=1.0):
        # Training loop
        pass
    
    def predict(self, X):
        # Make predictions
        pass


# XOR training data
X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])

y = np.array([[0], [1], [1], [0]])

# TODO: Create network, train, and test
