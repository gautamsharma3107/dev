"""
Day 29 - Activation Functions
==============================
Learn: ReLU, Sigmoid, Softmax, and other activation functions

Key Concepts:
- Activation functions introduce non-linearity
- Without them, neural networks would be just linear transformations
- Different functions for different purposes
"""

import numpy as np
import warnings
warnings.filterwarnings('ignore')

# ========== WHY ACTIVATION FUNCTIONS? ==========
print("=" * 60)
print("WHY DO WE NEED ACTIVATION FUNCTIONS?")
print("=" * 60)

print("""
🤔 THE PROBLEM WITH LINEAR TRANSFORMATIONS:

Without activation functions:
    Layer 1: y = W₁x + b₁
    Layer 2: y = W₂(W₁x + b₁) + b₂
           = W₂W₁x + W₂b₁ + b₂
           = Wx + b  (still linear!)

No matter how many layers, output is just a linear function!

✅ THE SOLUTION:
Activation functions introduce non-linearity, allowing networks
to learn complex patterns like curves, shapes, and relationships.

Without non-linearity: Can only draw straight lines
With non-linearity: Can draw any shape!
""")

# ========== RELU (RECTIFIED LINEAR UNIT) ==========
print("\n" + "=" * 60)
print("RELU (RECTIFIED LINEAR UNIT)")
print("=" * 60)

def relu(z):
    """ReLU activation function"""
    return np.maximum(0, z)

def relu_derivative(z):
    """Derivative of ReLU"""
    return (z > 0).astype(float)

print("""
📊 ReLU: f(z) = max(0, z)

Formula:
    f(z) = z  if z > 0
    f(z) = 0  if z ≤ 0

Derivative:
    f'(z) = 1  if z > 0
    f'(z) = 0  if z ≤ 0

ADVANTAGES:
✅ Simple and fast to compute
✅ Solves vanishing gradient problem
✅ Sparse activation (only some neurons fire)
✅ Most popular in hidden layers

DISADVANTAGES:
❌ "Dying ReLU" - neurons can get stuck at 0
❌ Not zero-centered
❌ Unbounded output (can explode)
""")

# Demonstrate ReLU
print("\nReLU Examples:")
print("-" * 40)
test_values = np.array([-3, -1, 0, 1, 3, 5])
print(f"Input:  {test_values}")
print(f"Output: {relu(test_values)}")

# Visual representation
print("\nReLU Graph (ASCII):")
print("""
    output
      │
    5 │         ╱
    4 │        ╱
    3 │       ╱
    2 │      ╱
    1 │     ╱
    0 ├────┼────────
   -1 │    │
      └────┴────────
        -2 0  2  4   input
""")

# ========== SIGMOID ==========
print("\n" + "=" * 60)
print("SIGMOID ACTIVATION")
print("=" * 60)

def sigmoid(z):
    """Sigmoid activation function"""
    return 1 / (1 + np.exp(-np.clip(z, -500, 500)))

def sigmoid_derivative(z):
    """Derivative of sigmoid"""
    s = sigmoid(z)
    return s * (1 - s)

print("""
📊 Sigmoid: f(z) = 1 / (1 + e^(-z))

Properties:
    Output range: (0, 1)
    f(0) = 0.5
    f(∞) = 1
    f(-∞) = 0

Derivative:
    f'(z) = f(z) × (1 - f(z))

ADVANTAGES:
✅ Output between 0 and 1 (like probability)
✅ Smooth gradient
✅ Clear interpretation

DISADVANTAGES:
❌ Vanishing gradient for large |z|
❌ Outputs not zero-centered
❌ Computationally expensive (exp)

BEST USED FOR:
- Output layer for binary classification
- Gates in LSTM/GRU
""")

# Demonstrate sigmoid
print("\nSigmoid Examples:")
print("-" * 40)
test_values = np.array([-5, -2, 0, 2, 5])
outputs = sigmoid(test_values)
print(f"Input:  {test_values}")
print(f"Output: {np.round(outputs, 4)}")

# Show gradient vanishing
print("\nVanishing Gradient Demonstration:")
print("-" * 40)
for z in [-10, -5, 0, 5, 10]:
    grad = sigmoid_derivative(z)
    print(f"z = {z:4d}: sigmoid = {sigmoid(z):.6f}, gradient = {grad:.6f}")

# ========== TANH ==========
print("\n" + "=" * 60)
print("TANH (HYPERBOLIC TANGENT)")
print("=" * 60)

def tanh(z):
    """Tanh activation function"""
    return np.tanh(z)

def tanh_derivative(z):
    """Derivative of tanh"""
    return 1 - np.tanh(z) ** 2

print("""
📊 Tanh: f(z) = (e^z - e^(-z)) / (e^z + e^(-z))

Properties:
    Output range: (-1, 1)
    f(0) = 0
    Zero-centered (unlike sigmoid)

Derivative:
    f'(z) = 1 - f(z)²

ADVANTAGES:
✅ Output between -1 and 1
✅ Zero-centered (better than sigmoid)
✅ Stronger gradients than sigmoid

DISADVANTAGES:
❌ Still has vanishing gradient problem
❌ Computationally expensive

BEST USED FOR:
- Hidden layers when zero-centered output needed
- RNN/LSTM cells
""")

# Demonstrate tanh
print("\nTanh Examples:")
print("-" * 40)
test_values = np.array([-5, -2, 0, 2, 5])
outputs = tanh(test_values)
print(f"Input:  {test_values}")
print(f"Output: {np.round(outputs, 4)}")

# ========== SOFTMAX ==========
print("\n" + "=" * 60)
print("SOFTMAX ACTIVATION")
print("=" * 60)

def softmax(z):
    """Softmax activation function (numerically stable)"""
    z_shifted = z - np.max(z, axis=-1, keepdims=True)
    exp_z = np.exp(z_shifted)
    return exp_z / np.sum(exp_z, axis=-1, keepdims=True)

print("""
📊 Softmax: f(zᵢ) = e^(zᵢ) / Σ(e^(zⱼ))

Properties:
    Output range: (0, 1) for each element
    Sum of outputs = 1 (probability distribution)
    Larger inputs → larger probabilities

KEY FEATURES:
✅ Converts raw scores to probabilities
✅ All outputs sum to 1
✅ Amplifies differences between inputs

BEST USED FOR:
- Output layer for multi-class classification
- Attention mechanisms
""")

# Demonstrate softmax
print("\nSoftmax Examples:")
print("-" * 40)

# Example 1: Class scores
scores = np.array([2.0, 1.0, 0.1])
probs = softmax(scores)
print(f"Raw scores:    {scores}")
print(f"Probabilities: {np.round(probs, 4)}")
print(f"Sum: {np.sum(probs):.4f}")

# Example 2: Clear winner
print("\nWith a clear winner:")
scores = np.array([10.0, 2.0, 1.0])
probs = softmax(scores)
print(f"Raw scores:    {scores}")
print(f"Probabilities: {np.round(probs, 4)}")

# Example 3: Close scores
print("\nWith close scores:")
scores = np.array([2.0, 2.1, 1.9])
probs = softmax(scores)
print(f"Raw scores:    {scores}")
print(f"Probabilities: {np.round(probs, 4)}")

# ========== LEAKY RELU ==========
print("\n" + "=" * 60)
print("LEAKY RELU AND VARIANTS")
print("=" * 60)

def leaky_relu(z, alpha=0.01):
    """Leaky ReLU activation function"""
    return np.where(z > 0, z, alpha * z)

def elu(z, alpha=1.0):
    """ELU (Exponential Linear Unit)"""
    return np.where(z > 0, z, alpha * (np.exp(z) - 1))

print("""
📊 Leaky ReLU: f(z) = max(αz, z) where α is small (e.g., 0.01)

Formula:
    f(z) = z      if z > 0
    f(z) = αz     if z ≤ 0

ADVANTAGE: Solves "dying ReLU" problem

📊 ELU (Exponential Linear Unit):
    f(z) = z              if z > 0
    f(z) = α(e^z - 1)     if z ≤ 0

ADVANTAGE: Smoother, pushes mean activations toward zero
""")

# Demonstrate Leaky ReLU
print("\nLeaky ReLU Examples:")
print("-" * 40)
test_values = np.array([-3, -1, 0, 1, 3])
print(f"Input:      {test_values}")
print(f"ReLU:       {relu(test_values)}")
print(f"Leaky ReLU: {leaky_relu(test_values, alpha=0.1)}")

# ========== CHOOSING ACTIVATION FUNCTIONS ==========
print("\n" + "=" * 60)
print("CHOOSING ACTIVATION FUNCTIONS")
print("=" * 60)

print("""
🎯 GUIDELINES FOR CHOOSING:

HIDDEN LAYERS:
1. Start with ReLU (most common, works well)
2. Try Leaky ReLU if you have dying neurons
3. Use ELU for potentially better results
4. Tanh if you need zero-centered outputs

OUTPUT LAYER:
1. Binary Classification → Sigmoid (outputs probability 0-1)
2. Multi-class Classification → Softmax (outputs probability distribution)
3. Regression → Linear (no activation, or ReLU for positive values)
4. Multi-label Classification → Sigmoid (independent probabilities)

SUMMARY TABLE:
┌──────────────────┬─────────────────┬─────────────────────┐
│ Task             │ Output Layer    │ Loss Function       │
├──────────────────┼─────────────────┼─────────────────────┤
│ Binary Class     │ Sigmoid         │ Binary Cross-Entropy│
│ Multi-class      │ Softmax         │ Categorical CE      │
│ Regression       │ Linear          │ MSE                 │
│ Multi-label      │ Sigmoid         │ Binary CE           │
└──────────────────┴─────────────────┴─────────────────────┘
""")

# ========== PRACTICAL EXAMPLE ==========
print("\n" + "=" * 60)
print("PRACTICAL EXAMPLE: COMPLETE FORWARD PASS")
print("=" * 60)

# Simulate a network for multi-class classification
np.random.seed(42)

# Input features (e.g., image features)
x = np.array([[0.5, 0.3, 0.8, 0.2]])

# Layer 1: Input(4) → Hidden(3) with ReLU
w1 = np.random.randn(4, 3) * 0.1
b1 = np.zeros((1, 3))

# Layer 2: Hidden(3) → Output(3) with Softmax
w2 = np.random.randn(3, 3) * 0.1
b2 = np.zeros((1, 3))

print("Network: 4 features → 3 hidden (ReLU) → 3 classes (Softmax)")
print("-" * 60)

# Forward pass
print(f"\nInput: {x}")

# Layer 1
z1 = np.dot(x, w1) + b1
a1 = relu(z1)
print(f"\nLayer 1 (ReLU):")
print(f"  Pre-activation (z1): {np.round(z1, 4)}")
print(f"  Post-activation (a1): {np.round(a1, 4)}")

# Layer 2
z2 = np.dot(a1, w2) + b2
a2 = softmax(z2)
print(f"\nLayer 2 (Softmax):")
print(f"  Pre-activation (z2): {np.round(z2, 4)}")
print(f"  Probabilities (a2): {np.round(a2, 4)}")
print(f"  Sum of probabilities: {np.sum(a2):.4f}")

# Prediction
predicted_class = np.argmax(a2)
print(f"\nPredicted class: {predicted_class} (probability: {a2[0, predicted_class]:.4f})")

# ========== VISUALIZATION OF ALL FUNCTIONS ==========
print("\n" + "=" * 60)
print("COMPARISON OF ALL ACTIVATION FUNCTIONS")
print("=" * 60)

# Generate range of values
z_range = np.linspace(-5, 5, 11)

print("\nFunction values at different inputs:")
print("-" * 70)
print(f"{'z':>6} | {'ReLU':>8} | {'Sigmoid':>8} | {'Tanh':>8} | {'Leaky':>8}")
print("-" * 70)

for z in z_range:
    r = relu(z)
    s = sigmoid(z)
    t = tanh(z)
    l = leaky_relu(z, 0.1)
    print(f"{z:6.1f} | {r:8.4f} | {s:8.4f} | {t:8.4f} | {l:8.4f}")

# ========== SUMMARY ==========
print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
✅ RELU: f(z) = max(0, z)
   - Most common in hidden layers
   - Simple, fast, effective
   - Watch for dying neurons

✅ SIGMOID: f(z) = 1/(1+e^(-z))
   - Outputs 0-1 (probability)
   - Used for binary classification output
   - Suffers from vanishing gradient

✅ TANH: f(z) = (e^z - e^(-z))/(e^z + e^(-z))
   - Outputs -1 to 1
   - Zero-centered
   - Better than sigmoid for hidden layers

✅ SOFTMAX: f(zᵢ) = e^(zᵢ) / Σe^(zⱼ)
   - Outputs probability distribution
   - Used for multi-class classification output
   - All outputs sum to 1

✅ LEAKY RELU: f(z) = max(αz, z)
   - Solves dying ReLU problem
   - Small negative slope for z < 0
""")

print("\n" + "=" * 60)
print("✅ Activation Functions - Complete!")
print("=" * 60)
