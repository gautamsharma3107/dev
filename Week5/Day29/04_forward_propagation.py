"""
Day 29 - Forward Propagation
=============================
Learn: How data flows through a neural network

Key Concepts:
- Forward propagation is the process of computing output from input
- Data flows from input layer through hidden layers to output
- Each layer performs: linear transformation + activation
"""

import numpy as np

# ========== WHAT IS FORWARD PROPAGATION? ==========
print("=" * 60)
print("WHAT IS FORWARD PROPAGATION?")
print("=" * 60)

print("""
🔄 FORWARD PROPAGATION:
The process of passing input data through the neural network 
to generate an output (prediction).

FLOW:
Input → Layer 1 → Layer 2 → ... → Output

At each layer:
1. Multiply inputs by weights (linear transformation)
2. Add biases
3. Apply activation function
4. Pass result to next layer

MATHEMATICAL NOTATION:
For layer l:
    z⁽ˡ⁾ = W⁽ˡ⁾ · a⁽ˡ⁻¹⁾ + b⁽ˡ⁾    (linear step)
    a⁽ˡ⁾ = g⁽ˡ⁾(z⁽ˡ⁾)              (activation step)

Where:
    W = weight matrix
    b = bias vector
    a = activation (output)
    z = pre-activation (weighted sum)
    g = activation function
""")

# ========== STEP-BY-STEP FORWARD PASS ==========
print("\n" + "=" * 60)
print("STEP-BY-STEP FORWARD PASS")
print("=" * 60)

# Define activation functions
def relu(z):
    return np.maximum(0, z)

def sigmoid(z):
    return 1 / (1 + np.exp(-np.clip(z, -500, 500)))

def softmax(z):
    exp_z = np.exp(z - np.max(z, axis=1, keepdims=True))
    return exp_z / np.sum(exp_z, axis=1, keepdims=True)

# Example network: 3 inputs → 4 hidden → 2 outputs
print("""
Network Architecture:
    Input Layer: 3 neurons (features)
    Hidden Layer: 4 neurons (ReLU activation)
    Output Layer: 2 neurons (Sigmoid activation)

Task: Binary classification
""")

# Initialize weights and biases (normally random, using fixed for clarity)
np.random.seed(42)

# Layer 1 (Input → Hidden)
W1 = np.array([
    [0.1, 0.2, -0.1, 0.3],
    [-0.2, 0.1, 0.3, -0.1],
    [0.3, -0.2, 0.1, 0.2]
])  # Shape: (3, 4)
b1 = np.array([[0.1, -0.1, 0.2, 0.0]])  # Shape: (1, 4)

# Layer 2 (Hidden → Output)
W2 = np.array([
    [0.2, -0.3],
    [-0.1, 0.4],
    [0.3, 0.1],
    [0.1, -0.2]
])  # Shape: (4, 2)
b2 = np.array([[0.0, 0.1]])  # Shape: (1, 2)

# Input data (1 sample with 3 features)
X = np.array([[1.0, 2.0, 0.5]])

print("=" * 40)
print("STEP 1: Input Layer")
print("=" * 40)
print(f"Input X: {X}")
print(f"Shape: {X.shape}")

print("\n" + "=" * 40)
print("STEP 2: Hidden Layer Computation")
print("=" * 40)

# Linear transformation
z1 = np.dot(X, W1) + b1
print(f"\nLinear step: z1 = X · W1 + b1")
print(f"z1 = {np.round(z1, 4)}")

# Detailed calculation
print("\nDetailed calculation:")
print(f"  z1[0] = 1.0×0.1 + 2.0×(-0.2) + 0.5×0.3 + 0.1 = {1.0*0.1 + 2.0*(-0.2) + 0.5*0.3 + 0.1:.2f}")
print(f"  z1[1] = 1.0×0.2 + 2.0×0.1 + 0.5×(-0.2) + (-0.1) = {1.0*0.2 + 2.0*0.1 + 0.5*(-0.2) + (-0.1):.2f}")

# Activation
a1 = relu(z1)
print(f"\nActivation step: a1 = ReLU(z1)")
print(f"a1 = {np.round(a1, 4)}")
print(f"(Negative values become 0)")

print("\n" + "=" * 40)
print("STEP 3: Output Layer Computation")
print("=" * 40)

# Linear transformation
z2 = np.dot(a1, W2) + b2
print(f"\nLinear step: z2 = a1 · W2 + b2")
print(f"z2 = {np.round(z2, 4)}")

# Activation (sigmoid for binary classification)
a2 = sigmoid(z2)
print(f"\nActivation step: a2 = Sigmoid(z2)")
print(f"a2 = {np.round(a2, 4)}")

print("\n" + "=" * 40)
print("STEP 4: Final Output (Prediction)")
print("=" * 40)
print(f"Output probabilities: {np.round(a2, 4)}")
prediction = (a2 > 0.5).astype(int)
print(f"Binary predictions (threshold=0.5): {prediction}")

# ========== COMPLETE FORWARD PASS FUNCTION ==========
print("\n" + "=" * 60)
print("IMPLEMENTING COMPLETE FORWARD PASS")
print("=" * 60)

class NeuralNetwork:
    def __init__(self):
        """Initialize the network with layers"""
        self.layers = []
        
    def add_layer(self, weights, biases, activation):
        """Add a layer to the network"""
        self.layers.append({
            'W': weights,
            'b': biases,
            'activation': activation
        })
    
    def forward(self, X, verbose=False):
        """
        Perform forward propagation
        
        Parameters:
        - X: input data
        - verbose: if True, print intermediate values
        
        Returns:
        - output: final prediction
        - cache: intermediate values (for backprop later)
        """
        cache = {'a0': X}  # Store input as a0
        a = X
        
        for i, layer in enumerate(self.layers, 1):
            W = layer['W']
            b = layer['b']
            activation_fn = layer['activation']
            
            # Linear transformation
            z = np.dot(a, W) + b
            
            # Activation
            if activation_fn == 'relu':
                a = relu(z)
            elif activation_fn == 'sigmoid':
                a = sigmoid(z)
            elif activation_fn == 'softmax':
                a = softmax(z)
            else:  # linear
                a = z
            
            # Cache for backpropagation
            cache[f'z{i}'] = z
            cache[f'a{i}'] = a
            
            if verbose:
                print(f"\nLayer {i}:")
                print(f"  z{i} shape: {z.shape}")
                print(f"  a{i} shape: {a.shape}")
                print(f"  z{i}: {np.round(z, 4)}")
                print(f"  a{i}: {np.round(a, 4)}")
        
        return a, cache

# Create and test the network
print("\nCreating network: 3 → 4 → 2")
print("-" * 40)

nn = NeuralNetwork()
nn.add_layer(W1, b1, 'relu')
nn.add_layer(W2, b2, 'sigmoid')

output, cache = nn.forward(X, verbose=True)

print(f"\nFinal output: {np.round(output, 4)}")

# ========== BATCH FORWARD PROPAGATION ==========
print("\n" + "=" * 60)
print("BATCH FORWARD PROPAGATION")
print("=" * 60)

print("""
In practice, we process multiple samples at once (a batch).
This is more efficient due to matrix operations.

Single sample: X shape = (1, n_features)
Batch of m samples: X shape = (m, n_features)

The same forward pass works for both!
""")

# Create a batch of 4 samples
X_batch = np.array([
    [1.0, 2.0, 0.5],
    [0.5, 1.0, 1.5],
    [2.0, 0.0, 1.0],
    [-1.0, 1.5, 0.5]
])

print(f"Batch input shape: {X_batch.shape}")
print(f"Input batch:\n{X_batch}\n")

output_batch, _ = nn.forward(X_batch)

print(f"Output batch shape: {output_batch.shape}")
print(f"Output probabilities:\n{np.round(output_batch, 4)}")
print(f"\nPredictions (threshold=0.5):\n{(output_batch > 0.5).astype(int)}")

# ========== MULTI-CLASS FORWARD PROPAGATION ==========
print("\n" + "=" * 60)
print("MULTI-CLASS CLASSIFICATION EXAMPLE")
print("=" * 60)

print("""
For multi-class classification (e.g., MNIST digits 0-9):
- Output layer has 10 neurons (one per class)
- Use Softmax activation (outputs sum to 1)
""")

# Network for 3-class classification
# Input: 4 features → Hidden: 5 neurons → Output: 3 classes

np.random.seed(123)

# Initialize weights
W1_mc = np.random.randn(4, 5) * 0.1
b1_mc = np.zeros((1, 5))
W2_mc = np.random.randn(5, 3) * 0.1
b2_mc = np.zeros((1, 3))

# Create network
nn_mc = NeuralNetwork()
nn_mc.add_layer(W1_mc, b1_mc, 'relu')
nn_mc.add_layer(W2_mc, b2_mc, 'softmax')

# Sample input (4 features)
X_mc = np.array([[0.5, 1.2, -0.3, 0.8]])

print("Network: 4 features → 5 hidden (ReLU) → 3 classes (Softmax)")
print(f"\nInput: {X_mc}")

output_mc, _ = nn_mc.forward(X_mc)

print(f"\nClass probabilities: {np.round(output_mc, 4)}")
print(f"Sum of probabilities: {np.sum(output_mc):.4f}")
print(f"Predicted class: {np.argmax(output_mc)}")

# ========== FORWARD PROPAGATION IN MATRIX FORM ==========
print("\n" + "=" * 60)
print("FORWARD PROPAGATION: MATRIX FORM SUMMARY")
print("=" * 60)

print("""
For a network with L layers:

INPUT: X with shape (m, n_features)
       m = batch size, n = number of input features

LAYER 1:
    Z¹ = X · W¹ + b¹           # (m, n1)
    A¹ = g¹(Z¹)                 # (m, n1)

LAYER 2:
    Z² = A¹ · W² + b²          # (m, n2)
    A² = g²(Z²)                 # (m, n2)

...

LAYER L (output):
    Zᴸ = Aᴸ⁻¹ · Wᴸ + bᴸ        # (m, n_L)
    Aᴸ = gᴸ(Zᴸ)                 # (m, n_L)

OUTPUT: Aᴸ with shape (m, n_output)

MATRIX DIMENSIONS:
    If layer l has nₗ₋₁ inputs and nₗ outputs:
    - Wˡ shape: (nₗ₋₁, nₗ)
    - bˡ shape: (1, nₗ)
    - Zˡ shape: (m, nₗ)
    - Aˡ shape: (m, nₗ)
""")

# ========== EFFICIENCY OF VECTORIZATION ==========
print("\n" + "=" * 60)
print("EFFICIENCY: VECTORIZED VS LOOP")
print("=" * 60)

import time

# Create larger network for timing
W_large = np.random.randn(100, 100)
b_large = np.zeros((1, 100))
X_large = np.random.randn(1000, 100)

# Vectorized forward pass
start = time.time()
for _ in range(100):
    Z_vec = np.dot(X_large, W_large) + b_large
    A_vec = relu(Z_vec)
vec_time = time.time() - start

# Loop-based forward pass
def forward_loop(X, W, b):
    m = X.shape[0]
    n_out = W.shape[1]
    Z = np.zeros((m, n_out))
    for i in range(m):
        for j in range(n_out):
            Z[i, j] = np.sum(X[i, :] * W[:, j]) + b[0, j]
    return relu(Z)

start = time.time()
for _ in range(1):  # Only 1 iteration (it's slow!)
    A_loop = forward_loop(X_large, W_large, b_large)
loop_time = time.time() - start

print(f"Vectorized (100 iterations): {vec_time:.4f} seconds")
print(f"Loop-based (1 iteration): {loop_time:.4f} seconds")
print(f"\nVectorization speedup: ~{loop_time * 100 / vec_time:.0f}x faster!")
print("\n⚠️ Always use vectorized operations (NumPy) for neural networks!")

# ========== COMPLETE FORWARD PASS VISUALIZATION ==========
print("\n" + "=" * 60)
print("FORWARD PASS VISUALIZATION")
print("=" * 60)

print("""
        FORWARD PROPAGATION FLOW
        
    ┌─────────────┐
    │   INPUT X   │  [x₁, x₂, x₃]
    └──────┬──────┘
           │
           ▼  Z¹ = X·W¹ + b¹
    ┌──────────────┐
    │   LAYER 1    │  Hidden Layer
    │    ReLU      │  
    └──────┬───────┘
           │  A¹ = ReLU(Z¹)
           ▼
    ┌──────────────┐
    │   LAYER 2    │  Z² = A¹·W² + b²
    │   Softmax    │  A² = Softmax(Z²)
    └──────┬───────┘
           │
           ▼
    ┌─────────────┐
    │  OUTPUT Ŷ  │  Predictions/Probabilities
    └─────────────┘
    
Each layer transforms the data, extracting more 
abstract features as we go deeper.
""")

# ========== SUMMARY ==========
print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
✅ Forward propagation = passing data through network

✅ At each layer:
   1. Linear: z = W·a + b
   2. Activation: a = g(z)

✅ Data flows: Input → Hidden(s) → Output

✅ Cache intermediate values for backpropagation

✅ Use vectorization for efficiency

✅ Same code works for single samples and batches

✅ Final output depends on task:
   - Regression: Linear activation
   - Binary classification: Sigmoid
   - Multi-class: Softmax
""")

print("\n" + "=" * 60)
print("✅ Forward Propagation - Complete!")
print("=" * 60)
