"""
MINI PROJECT 5: Gradient Descent Optimizer Comparison
======================================================
Compare different optimization algorithms

Requirements:
1. Implement SGD, SGD with Momentum, and Adam
2. Optimize a simple function: f(x, y) = x^2 + y^2
3. Track path taken by each optimizer
4. Compare convergence speed
5. Visualize paths (as coordinate history)
"""

import numpy as np

# Your code here
print("=" * 50)
print("OPTIMIZER COMPARISON")
print("=" * 50)

# TODO: Implement optimizers

class SGD:
    """Standard Stochastic Gradient Descent"""
    def __init__(self, learning_rate=0.1):
        self.lr = learning_rate
    
    def update(self, params, grads):
        # params = params - lr * grads
        pass


class SGDMomentum:
    """SGD with Momentum"""
    def __init__(self, learning_rate=0.1, momentum=0.9):
        self.lr = learning_rate
        self.momentum = momentum
        self.velocity = None
    
    def update(self, params, grads):
        # v = momentum * v - lr * grads
        # params = params + v
        pass


class Adam:
    """Adam Optimizer"""
    def __init__(self, learning_rate=0.001, beta1=0.9, beta2=0.999, epsilon=1e-8):
        self.lr = learning_rate
        self.beta1 = beta1
        self.beta2 = beta2
        self.epsilon = epsilon
        self.m = None
        self.v = None
        self.t = 0
    
    def update(self, params, grads):
        # Implement Adam update rule
        pass


# Function to optimize: f(x, y) = x^2 + y^2
def loss_function(params):
    x, y = params
    return x**2 + y**2

def gradient(params):
    x, y = params
    return np.array([2*x, 2*y])


# TODO: Run optimization with each method
def run_optimization(optimizer, start_point, n_iterations=50):
    """
    Run optimization and return path history
    """
    pass


# Starting point
start = np.array([5.0, 5.0])

# TODO: Compare all three optimizers
# TODO: Print results and analysis
