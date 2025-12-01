"""
Day 29 - Loss Functions and Optimization
=========================================
Learn: How to measure errors and update weights effectively

Key Concepts:
- Loss functions measure how wrong predictions are
- Optimization algorithms find the best weights
- Different tasks need different loss functions
"""

import numpy as np

# ========== WHAT ARE LOSS FUNCTIONS? ==========
print("=" * 60)
print("WHAT ARE LOSS FUNCTIONS?")
print("=" * 60)

print("""
📊 LOSS FUNCTION (Cost Function, Objective Function):
A function that measures how wrong the network's predictions are.

PURPOSE:
- Quantify the error between predictions and actual values
- Provide a signal for optimization
- Guide weight updates during training

GOAL:
Minimize the loss! Lower loss = better predictions.

TYPES:
1. REGRESSION losses (predicting continuous values)
2. CLASSIFICATION losses (predicting categories)
""")

# ========== MEAN SQUARED ERROR (MSE) ==========
print("\n" + "=" * 60)
print("MEAN SQUARED ERROR (MSE) - REGRESSION")
print("=" * 60)

def mse(y_true, y_pred):
    """Mean Squared Error"""
    return np.mean((y_true - y_pred) ** 2)

def mse_derivative(y_true, y_pred):
    """Derivative of MSE w.r.t. predictions"""
    return 2 * (y_pred - y_true) / len(y_true)

print("""
📊 MSE: L = (1/n) × Σ(y_true - y_pred)²

Properties:
- Always positive
- Penalizes large errors more (squared term)
- Differentiable everywhere

Best for: Regression tasks (predicting numbers)
""")

# Example
y_true = np.array([1.0, 2.0, 3.0, 4.0])
y_pred_good = np.array([1.1, 2.1, 2.9, 4.2])
y_pred_bad = np.array([2.0, 3.5, 1.0, 2.0])

print("\nMSE Examples:")
print("-" * 40)
print(f"True values:     {y_true}")
print(f"Good predictions: {y_pred_good}")
print(f"Bad predictions:  {y_pred_bad}")
print(f"\nMSE (good): {mse(y_true, y_pred_good):.4f}")
print(f"MSE (bad):  {mse(y_true, y_pred_bad):.4f}")

# ========== MEAN ABSOLUTE ERROR (MAE) ==========
print("\n" + "=" * 60)
print("MEAN ABSOLUTE ERROR (MAE) - REGRESSION")
print("=" * 60)

def mae(y_true, y_pred):
    """Mean Absolute Error"""
    return np.mean(np.abs(y_true - y_pred))

print("""
📊 MAE: L = (1/n) × Σ|y_true - y_pred|

Properties:
- Always positive
- Linear penalty (less sensitive to outliers than MSE)
- Not differentiable at y_pred = y_true

MSE vs MAE:
- MSE: Punishes large errors more
- MAE: Treats all errors equally
""")

print("\nMAE Examples:")
print("-" * 40)
print(f"MAE (good): {mae(y_true, y_pred_good):.4f}")
print(f"MAE (bad):  {mae(y_true, y_pred_bad):.4f}")

# ========== BINARY CROSS-ENTROPY ==========
print("\n" + "=" * 60)
print("BINARY CROSS-ENTROPY - BINARY CLASSIFICATION")
print("=" * 60)

def binary_crossentropy(y_true, y_pred):
    """Binary Cross-Entropy Loss"""
    epsilon = 1e-15
    y_pred = np.clip(y_pred, epsilon, 1 - epsilon)
    return -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))

def binary_crossentropy_derivative(y_true, y_pred):
    """Derivative of BCE w.r.t. predictions"""
    epsilon = 1e-15
    y_pred = np.clip(y_pred, epsilon, 1 - epsilon)
    return (-y_true / y_pred + (1 - y_true) / (1 - y_pred)) / len(y_true)

print("""
📊 BCE: L = -(1/n) × Σ[y×log(ŷ) + (1-y)×log(1-ŷ)]

Where:
    y = true label (0 or 1)
    ŷ = predicted probability (0 to 1)

Properties:
- Used with sigmoid output
- Heavily penalizes confident wrong predictions
- Output approaches infinity when confident and wrong

Best for: Binary classification (yes/no, spam/not spam)
""")

# Example
y_true_binary = np.array([1, 1, 0, 0])
y_pred_binary = np.array([0.9, 0.8, 0.2, 0.1])  # Good predictions
y_pred_bad_binary = np.array([0.2, 0.3, 0.8, 0.9])  # Bad predictions

print("\nBinary Cross-Entropy Examples:")
print("-" * 40)
print(f"True labels:      {y_true_binary}")
print(f"Good predictions: {y_pred_binary}")
print(f"Bad predictions:  {y_pred_bad_binary}")
print(f"\nBCE (good): {binary_crossentropy(y_true_binary, y_pred_binary):.4f}")
print(f"BCE (bad):  {binary_crossentropy(y_true_binary, y_pred_bad_binary):.4f}")

# Show penalty for confidence
print("\nConfidence Penalty:")
print("-" * 40)
for conf in [0.1, 0.3, 0.5, 0.7, 0.9, 0.99]:
    loss = -np.log(conf)  # Loss when true label is 1
    print(f"Confidence {conf:.2f}: BCE loss = {loss:.4f}")

# ========== CATEGORICAL CROSS-ENTROPY ==========
print("\n" + "=" * 60)
print("CATEGORICAL CROSS-ENTROPY - MULTI-CLASS")
print("=" * 60)

def categorical_crossentropy(y_true, y_pred):
    """Categorical Cross-Entropy Loss (y_true is one-hot encoded)"""
    epsilon = 1e-15
    y_pred = np.clip(y_pred, epsilon, 1 - epsilon)
    return -np.sum(y_true * np.log(y_pred)) / len(y_true)

def softmax(z):
    """Softmax activation"""
    exp_z = np.exp(z - np.max(z, axis=-1, keepdims=True))
    return exp_z / np.sum(exp_z, axis=-1, keepdims=True)

print("""
📊 CCE: L = -(1/n) × Σ Σ y_true × log(y_pred)
        (sum over samples and classes)

Properties:
- Used with softmax output
- Y_true is one-hot encoded
- Only the correct class contributes to loss

Best for: Multi-class classification (3+ classes)
""")

# Example: 3 classes, 4 samples
y_true_cat = np.array([
    [1, 0, 0],  # Class 0
    [0, 1, 0],  # Class 1
    [0, 0, 1],  # Class 2
    [1, 0, 0]   # Class 0
])

# Good predictions (high probability for correct class)
y_pred_cat_good = np.array([
    [0.8, 0.1, 0.1],
    [0.1, 0.8, 0.1],
    [0.1, 0.1, 0.8],
    [0.7, 0.2, 0.1]
])

# Bad predictions
y_pred_cat_bad = np.array([
    [0.2, 0.5, 0.3],
    [0.4, 0.3, 0.3],
    [0.3, 0.4, 0.3],
    [0.3, 0.4, 0.3]
])

print("\nCategorical Cross-Entropy Examples:")
print("-" * 40)
print("True labels (one-hot):")
print(y_true_cat)
print(f"\nCCE (good predictions): {categorical_crossentropy(y_true_cat, y_pred_cat_good):.4f}")
print(f"CCE (bad predictions):  {categorical_crossentropy(y_true_cat, y_pred_cat_bad):.4f}")

# ========== OPTIMIZATION ALGORITHMS ==========
print("\n" + "=" * 60)
print("OPTIMIZATION ALGORITHMS")
print("=" * 60)

print("""
🎯 GOAL OF OPTIMIZATION:
Find weights that minimize the loss function.

Imagine you're on a hilly landscape (loss surface):
- Your position = current weights
- Height = loss value
- Goal = reach the lowest point

Optimization algorithms tell you which direction to step
and how far to go.
""")

# ========== GRADIENT DESCENT ==========
print("\n" + "=" * 60)
print("GRADIENT DESCENT (GD)")
print("=" * 60)

print("""
📊 BASIC GRADIENT DESCENT:
    w_new = w_old - learning_rate × gradient

The gradient points uphill (direction of steepest increase).
We go the opposite direction (downhill) to minimize loss.

TYPES:
1. Batch GD: Use all samples to compute gradient
2. Stochastic GD (SGD): Use one sample at a time
3. Mini-batch GD: Use a small batch of samples

LEARNING RATE (α):
- Too small: Very slow convergence
- Too large: May overshoot or diverge
- Just right: Steady progress toward minimum
""")

def gradient_descent_demo():
    """Demonstrate gradient descent on f(x) = x²"""
    x = 5.0  # Starting point
    learning_rate = 0.1
    
    print("Minimizing f(x) = x² (minimum at x = 0):")
    print("-" * 40)
    
    for i in range(10):
        gradient = 2 * x  # derivative of x²
        x = x - learning_rate * gradient
        loss = x ** 2
        print(f"Step {i+1}: x = {x:7.4f}, f(x) = {loss:7.4f}, gradient = {gradient:7.4f}")

gradient_descent_demo()

# ========== SGD WITH MOMENTUM ==========
print("\n" + "=" * 60)
print("SGD WITH MOMENTUM")
print("=" * 60)

print("""
📊 MOMENTUM:
Add a "velocity" that accumulates past gradients.
Like a ball rolling downhill - it gains momentum!

    v = β × v_prev + gradient
    w = w - learning_rate × v

Where β (typically 0.9) controls how much history to keep.

BENEFITS:
- Faster convergence
- Helps escape local minima
- Smooths out noisy gradients
""")

def sgd_momentum_demo():
    """Demonstrate SGD with momentum"""
    x = 5.0
    v = 0.0  # Velocity
    learning_rate = 0.1
    beta = 0.9
    
    print("SGD with Momentum (β = 0.9):")
    print("-" * 40)
    
    for i in range(10):
        gradient = 2 * x
        v = beta * v + gradient
        x = x - learning_rate * v
        loss = x ** 2
        print(f"Step {i+1}: x = {x:7.4f}, f(x) = {loss:7.4f}, velocity = {v:7.4f}")

sgd_momentum_demo()

# ========== ADAM OPTIMIZER ==========
print("\n" + "=" * 60)
print("ADAM OPTIMIZER (Adaptive Moment Estimation)")
print("=" * 60)

print("""
📊 ADAM:
Combines momentum with adaptive learning rates.
Most popular optimizer for deep learning!

Algorithm:
    m = β₁ × m + (1 - β₁) × g         # First moment (mean)
    v = β₂ × v + (1 - β₂) × g²        # Second moment (variance)
    m_hat = m / (1 - β₁ᵗ)              # Bias correction
    v_hat = v / (1 - β₂ᵗ)              # Bias correction
    w = w - lr × m_hat / (√v_hat + ε)  # Update

Default values: β₁ = 0.9, β₂ = 0.999, ε = 1e-8

BENEFITS:
✅ Adaptive learning rates per parameter
✅ Works well out of the box
✅ Good for sparse gradients
✅ Memory efficient
""")

class Adam:
    """Adam optimizer implementation"""
    def __init__(self, learning_rate=0.001, beta1=0.9, beta2=0.999, epsilon=1e-8):
        self.lr = learning_rate
        self.beta1 = beta1
        self.beta2 = beta2
        self.epsilon = epsilon
        self.m = 0  # First moment
        self.v = 0  # Second moment
        self.t = 0  # Timestep
        
    def update(self, w, gradient):
        self.t += 1
        
        # Update moments
        self.m = self.beta1 * self.m + (1 - self.beta1) * gradient
        self.v = self.beta2 * self.v + (1 - self.beta2) * (gradient ** 2)
        
        # Bias correction
        m_hat = self.m / (1 - self.beta1 ** self.t)
        v_hat = self.v / (1 - self.beta2 ** self.t)
        
        # Update weight
        w = w - self.lr * m_hat / (np.sqrt(v_hat) + self.epsilon)
        
        return w

def adam_demo():
    """Demonstrate Adam optimizer"""
    x = 5.0
    adam = Adam(learning_rate=0.5)
    
    print("Adam Optimizer:")
    print("-" * 40)
    
    for i in range(10):
        gradient = 2 * x
        x = adam.update(x, gradient)
        loss = x ** 2
        print(f"Step {i+1}: x = {x:7.4f}, f(x) = {loss:7.4f}")

adam_demo()

# ========== OTHER OPTIMIZERS ==========
print("\n" + "=" * 60)
print("OTHER POPULAR OPTIMIZERS")
print("=" * 60)

print("""
📊 RMSPROP (Root Mean Square Propagation):
    v = β × v + (1 - β) × g²
    w = w - lr × g / √(v + ε)
- Adapts learning rate based on recent gradients
- Good for RNNs

📊 ADAGRAD:
    v = v + g²
    w = w - lr × g / √(v + ε)
- Adapts learning rate based on all past gradients
- Good for sparse data
- Learning rate can become too small

📊 ADADELTA:
- Extension of Adagrad
- Doesn't require initial learning rate

COMPARISON:
┌───────────────┬─────────────────────────────────────────┐
│ Optimizer     │ Best Use Case                           │
├───────────────┼─────────────────────────────────────────┤
│ SGD           │ Simple problems, fine-tuning            │
│ SGD+Momentum  │ General purpose, convex problems        │
│ Adam          │ Default choice, works well everywhere   │
│ RMSprop       │ RNNs, non-stationary objectives         │
│ Adagrad       │ Sparse data (NLP, embeddings)           │
└───────────────┴─────────────────────────────────────────┘
""")

# ========== LEARNING RATE SCHEDULING ==========
print("\n" + "=" * 60)
print("LEARNING RATE SCHEDULING")
print("=" * 60)

print("""
📊 WHY SCHEDULE LEARNING RATE?
- Start high to make quick progress
- Reduce over time for fine-tuning
- Helps reach better minima

COMMON SCHEDULES:

1. STEP DECAY: Reduce by factor every N epochs
   lr = initial_lr × decay_rate^(epoch // step_size)

2. EXPONENTIAL DECAY: Continuous reduction
   lr = initial_lr × exp(-decay_rate × epoch)

3. COSINE ANNEALING: Smooth oscillation
   lr = min_lr + 0.5×(max_lr - min_lr)×(1 + cos(π×t/T))

4. REDUCE ON PLATEAU: Reduce when stuck
   If no improvement for N epochs, reduce lr
""")

# Demonstrate schedules
print("\nLearning Rate Schedules Comparison:")
print("-" * 50)

initial_lr = 0.1
epochs_to_show = [0, 5, 10, 15, 20, 25, 30]

print(f"{'Epoch':>6} | {'Step':>8} | {'Exp':>8} | {'Cosine':>8}")
print("-" * 50)

for epoch in epochs_to_show:
    # Step decay (reduce by 0.5 every 10 epochs)
    step_lr = initial_lr * (0.5 ** (epoch // 10))
    
    # Exponential decay
    exp_lr = initial_lr * np.exp(-0.1 * epoch)
    
    # Cosine annealing (T = 30)
    cosine_lr = 0.001 + 0.5 * (initial_lr - 0.001) * (1 + np.cos(np.pi * epoch / 30))
    
    print(f"{epoch:>6} | {step_lr:>8.5f} | {exp_lr:>8.5f} | {cosine_lr:>8.5f}")

# ========== CHOOSING LOSS AND OPTIMIZER ==========
print("\n" + "=" * 60)
print("CHOOSING LOSS FUNCTION AND OPTIMIZER")
print("=" * 60)

print("""
🎯 QUICK GUIDE:

TASK                    LOSS FUNCTION          OUTPUT ACTIVATION
─────────────────────────────────────────────────────────────────
Regression              MSE or MAE              Linear (none)
Binary Classification   Binary Cross-Entropy    Sigmoid
Multi-class (single)    Categorical CE          Softmax
Multi-class (multi)     Binary CE per class     Sigmoid

OPTIMIZER SELECTION:
─────────────────────────────────────────────────────────────────
General starting point          → Adam
Very large dataset              → SGD + Momentum  
Fine-tuning pretrained model    → SGD with small lr
RNNs/LSTMs                      → RMSprop or Adam
Sparse features                 → Adagrad

HYPERPARAMETER TIPS:
─────────────────────────────────────────────────────────────────
Learning rate      Start with 0.001 for Adam, 0.01 for SGD
Batch size         32 or 64 for most tasks
Momentum           0.9 is standard
Adam betas         (0.9, 0.999) works for most cases
""")

# ========== SUMMARY ==========
print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
✅ LOSS FUNCTIONS measure prediction error:
   - MSE/MAE for regression
   - Binary Cross-Entropy for binary classification
   - Categorical Cross-Entropy for multi-class

✅ GRADIENT DESCENT minimizes loss:
   w_new = w_old - learning_rate × gradient

✅ OPTIMIZERS improve on basic GD:
   - SGD + Momentum: Faster, smoother
   - Adam: Adaptive learning rates (most popular)
   - RMSprop: Good for RNNs

✅ LEARNING RATE SCHEDULING:
   - Start high, reduce over time
   - Helps reach better solutions

✅ KEY HYPERPARAMETERS:
   - Learning rate (most important!)
   - Batch size
   - Optimizer choice
""")

print("\n" + "=" * 60)
print("✅ Loss Functions and Optimization - Complete!")
print("=" * 60)
