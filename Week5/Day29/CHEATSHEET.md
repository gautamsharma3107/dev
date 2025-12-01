# Day 29 Quick Reference Cheat Sheet - Neural Networks Fundamentals

## Neural Network Basics
```
Neural Network = Layers of connected neurons
                 that learn patterns from data

Architecture:
Input Layer → Hidden Layer(s) → Output Layer
```

## Neuron Components
```python
# Single Neuron Computation
output = activation(weights · inputs + bias)

# Components:
# - Inputs (x): Feature values
# - Weights (w): Learnable parameters
# - Bias (b): Offset term
# - Activation: Non-linear function
```

## Layer Types
```
1. Input Layer    - Receives raw features
2. Hidden Layers  - Process intermediate representations
3. Output Layer   - Produces final predictions
```

## Activation Functions

### ReLU (Rectified Linear Unit)
```python
def relu(x):
    return max(0, x)

# Properties:
# - Simple and fast
# - Solves vanishing gradient
# - Most commonly used in hidden layers
```

### Sigmoid
```python
def sigmoid(x):
    return 1 / (1 + exp(-x))

# Properties:
# - Output: 0 to 1
# - Used for binary classification
# - Suffers from vanishing gradient
```

### Softmax
```python
def softmax(x):
    exp_x = exp(x - max(x))
    return exp_x / sum(exp_x)

# Properties:
# - Output: probability distribution
# - Sum of outputs = 1
# - Used for multi-class classification
```

### Tanh
```python
def tanh(x):
    return (exp(x) - exp(-x)) / (exp(x) + exp(-x))

# Properties:
# - Output: -1 to 1
# - Zero-centered
# - Better than sigmoid in hidden layers
```

## Forward Propagation
```python
# Layer-by-layer computation
# Input → Layer 1 → Layer 2 → ... → Output

# For each layer:
z = weights @ inputs + bias  # Linear combination
a = activation(z)            # Apply activation
```

## Backward Propagation
```
1. Compute loss at output
2. Calculate gradients using chain rule
3. Propagate gradients backwards
4. Update weights: w = w - learning_rate * gradient
```

## Loss Functions

### Mean Squared Error (MSE) - Regression
```python
def mse(y_true, y_pred):
    return mean((y_true - y_pred) ** 2)
```

### Binary Cross-Entropy - Binary Classification
```python
def binary_crossentropy(y_true, y_pred):
    return -mean(y_true * log(y_pred) + (1-y_true) * log(1-y_pred))
```

### Categorical Cross-Entropy - Multi-class
```python
def categorical_crossentropy(y_true, y_pred):
    return -sum(y_true * log(y_pred))
```

## Optimization Algorithms
```
SGD       - Simple gradient descent
Momentum  - Accelerates convergence
Adam      - Adaptive learning rates (most popular)
RMSprop   - Per-parameter learning rates
```

## Hyperparameters
```python
learning_rate = 0.001    # How big each update step is
batch_size = 32          # Samples per training step
epochs = 100             # Complete passes through dataset
num_neurons = 128        # Neurons per layer
num_layers = 3           # Number of hidden layers
```

## Training Process
```
1. Initialize weights (randomly)
2. For each epoch:
   a. Forward pass: compute predictions
   b. Calculate loss
   c. Backward pass: compute gradients
   d. Update weights
3. Evaluate on validation set
4. Repeat until convergence
```

## Common Issues & Solutions
```
Overfitting        → Dropout, regularization, more data
Underfitting       → More neurons/layers, more epochs
Vanishing gradient → ReLU activation, batch normalization
Exploding gradient → Gradient clipping, weight initialization
Slow convergence   → Learning rate scheduling, Adam optimizer
```

## Key Formulas

### Weight Update Rule
```
w_new = w_old - learning_rate * gradient
```

### Chain Rule for Gradients
```
∂Loss/∂w = ∂Loss/∂output × ∂output/∂w
```

### Gradient Descent
```
w := w - α * ∂J/∂w
where α = learning rate, J = loss function
```

## NumPy Implementation Patterns
```python
import numpy as np

# Initialize weights
weights = np.random.randn(input_size, output_size) * 0.01
bias = np.zeros((1, output_size))

# Forward pass
z = np.dot(inputs, weights) + bias
a = np.maximum(0, z)  # ReLU

# Calculate gradients
dz = da * (z > 0)  # ReLU derivative
dw = np.dot(inputs.T, dz)
db = np.sum(dz, axis=0, keepdims=True)

# Update weights
weights -= learning_rate * dw
bias -= learning_rate * db
```

## Remember
- Start simple, add complexity gradually
- Normalize your input data
- Use appropriate activation for output layer
- Monitor loss during training
- Save model checkpoints

---
**Keep this handy for quick reference!** 🧠🚀
