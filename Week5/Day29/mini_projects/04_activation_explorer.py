"""
MINI PROJECT 4: Activation Function Explorer
=============================================
Interactive exploration of different activation functions

Requirements:
1. Implement all major activation functions
2. Plot each function and its derivative
3. Compare functions side by side
4. Show properties (range, derivative at key points)
5. Demonstrate vanishing gradient problem with sigmoid
"""

import numpy as np

# Your code here
print("=" * 50)
print("ACTIVATION FUNCTION EXPLORER")
print("=" * 50)

# TODO: Implement all activation functions

def relu(x):
    """ReLU: max(0, x)"""
    pass

def relu_derivative(x):
    """Derivative of ReLU"""
    pass

def sigmoid(x):
    """Sigmoid: 1 / (1 + exp(-x))"""
    pass

def sigmoid_derivative(x):
    """Derivative of sigmoid: sig(x) * (1 - sig(x))"""
    pass

def tanh_activation(x):
    """Tanh: (exp(x) - exp(-x)) / (exp(x) + exp(-x))"""
    pass

def tanh_derivative(x):
    """Derivative of tanh: 1 - tanh^2(x)"""
    pass

def leaky_relu(x, alpha=0.01):
    """Leaky ReLU: x if x > 0, else alpha * x"""
    pass

def softmax(x):
    """Softmax for probability distribution"""
    pass


# TODO: Create comparison tables
def compare_activations(x_values):
    """
    Compare all activation functions at given x values
    Print a formatted table
    """
    pass


# TODO: Demonstrate vanishing gradient
def show_vanishing_gradient():
    """
    Show how sigmoid gradient vanishes for large |x|
    """
    pass


# Test with x values from -5 to 5
x_test = np.linspace(-5, 5, 11)
# TODO: Run comparisons and demonstrations
