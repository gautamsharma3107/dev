"""
Day 29 - Backward Propagation (Backpropagation)
================================================
Learn: How neural networks learn by adjusting weights

Key Concepts:
- Backpropagation calculates gradients of loss w.r.t. weights
- Uses chain rule from calculus
- Gradients tell us how to adjust weights to reduce error
"""

import numpy as np

# ========== WHAT IS BACKPROPAGATION? ==========
print("=" * 60)
print("WHAT IS BACKPROPAGATION?")
print("=" * 60)

print("""
🔄 BACKPROPAGATION (Backward Propagation of Errors):
The algorithm for calculating gradients in neural networks.

PURPOSE:
- Find out how much each weight contributed to the error
- Use this information to update weights and reduce error

THE PROCESS:
1. Forward Pass: Compute predictions
2. Calculate Loss: Compare predictions to actual values
3. Backward Pass: Calculate gradients (how much each weight affected the loss)
4. Update Weights: Adjust weights in the direction that reduces loss

KEY INSIGHT:
Backprop uses the CHAIN RULE to efficiently compute gradients
for all weights at once, layer by layer, from output to input.
""")

# ========== THE CHAIN RULE ==========
print("\n" + "=" * 60)
print("THE CHAIN RULE - FOUNDATION OF BACKPROP")
print("=" * 60)

print("""
📚 CHAIN RULE FROM CALCULUS:
If y = f(g(x)), then dy/dx = (dy/dg) × (dg/dx)

NEURAL NETWORK APPLICATION:
If Loss depends on Output, which depends on Weights:

    dLoss/dWeight = (dLoss/dOutput) × (dOutput/dWeight)

This lets us "chain" derivatives back through the network!

EXAMPLE:
    Loss = (y - ŷ)²
    ŷ = sigmoid(z)
    z = wx + b

    dLoss/dw = (dLoss/dŷ) × (dŷ/dz) × (dz/dw)
             = 2(y - ŷ)   × sigmoid'(z) × x
""")

# ========== SIMPLE BACKPROP EXAMPLE ==========
print("\n" + "=" * 60)
print("SIMPLE BACKPROP EXAMPLE: SINGLE NEURON")
print("=" * 60)

def sigmoid(z):
    return 1 / (1 + np.exp(-np.clip(z, -500, 500)))

def sigmoid_derivative(z):
    s = sigmoid(z)
    return s * (1 - s)

# Single neuron: y_pred = sigmoid(w*x + b)
# Loss = (y_true - y_pred)^2

# Sample data
x = 2.0       # Input
y_true = 1.0  # Target

# Initial parameters
w = 0.5       # Weight
b = 0.1       # Bias
lr = 0.1      # Learning rate

print("Single Neuron Backpropagation:")
print("-" * 40)
print(f"Input x = {x}, Target y = {y_true}")
print(f"Initial w = {w}, b = {b}")

for epoch in range(5):
    # Forward pass
    z = w * x + b
    y_pred = sigmoid(z)
    loss = (y_true - y_pred) ** 2
    
    # Backward pass (compute gradients)
    # dLoss/dy_pred = -2(y_true - y_pred)
    dL_dy = -2 * (y_true - y_pred)
    
    # dy_pred/dz = sigmoid_derivative(z)
    dy_dz = sigmoid_derivative(z)
    
    # dz/dw = x, dz/db = 1
    dz_dw = x
    dz_db = 1
    
    # Chain rule
    dL_dw = dL_dy * dy_dz * dz_dw
    dL_db = dL_dy * dy_dz * dz_db
    
    # Update weights
    w = w - lr * dL_dw
    b = b - lr * dL_db
    
    print(f"\nEpoch {epoch + 1}:")
    print(f"  Prediction: {y_pred:.4f}, Loss: {loss:.4f}")
    print(f"  dL/dw: {dL_dw:.4f}, dL/db: {dL_db:.4f}")
    print(f"  Updated w: {w:.4f}, b: {b:.4f}")

# ========== GRADIENT COMPUTATION FOR LAYERS ==========
print("\n" + "=" * 60)
print("GRADIENT COMPUTATION: LAYER BY LAYER")
print("=" * 60)

print("""
For a neural network with L layers:

FORWARD PASS (store for later):
    Z¹ = X·W¹ + b¹,  A¹ = g¹(Z¹)
    Z² = A¹·W² + b²,  A² = g²(Z²)
    ...
    Zᴸ = Aᴸ⁻¹·Wᴸ + bᴸ,  Aᴸ = gᴸ(Zᴸ) = Ŷ

BACKWARD PASS (compute gradients):
Starting from output layer L:
    
    dZᴸ = dLoss/dZᴸ (depends on loss function and activation)
    dWᴸ = (1/m) × Aᴸ⁻¹ᵀ · dZᴸ
    dbᴸ = (1/m) × sum(dZᴸ)
    
Then propagate back:
    dAᴸ⁻¹ = dZᴸ · Wᴸᵀ
    dZᴸ⁻¹ = dAᴸ⁻¹ ⊙ g'ᴸ⁻¹(Zᴸ⁻¹)   (⊙ = element-wise multiply)
    
Continue until layer 1.
""")

# ========== IMPLEMENTING BACKPROPAGATION ==========
print("\n" + "=" * 60)
print("IMPLEMENTING BACKPROPAGATION")
print("=" * 60)

def relu(z):
    return np.maximum(0, z)

def relu_derivative(z):
    return (z > 0).astype(float)

class SimpleNeuralNetwork:
    def __init__(self, layer_sizes):
        """
        Initialize network with given layer sizes
        layer_sizes: [input_size, hidden1_size, ..., output_size]
        """
        self.num_layers = len(layer_sizes) - 1
        self.weights = []
        self.biases = []
        
        # Initialize weights with Xavier initialization
        for i in range(self.num_layers):
            w = np.random.randn(layer_sizes[i], layer_sizes[i+1]) * np.sqrt(2.0 / layer_sizes[i])
            b = np.zeros((1, layer_sizes[i+1]))
            self.weights.append(w)
            self.biases.append(b)
    
    def forward(self, X):
        """Forward pass - returns output and caches"""
        self.cache = {'A0': X}
        A = X
        
        for i in range(self.num_layers):
            Z = np.dot(A, self.weights[i]) + self.biases[i]
            
            # Use ReLU for hidden layers, sigmoid for output
            if i == self.num_layers - 1:
                A = sigmoid(Z)
            else:
                A = relu(Z)
            
            self.cache[f'Z{i+1}'] = Z
            self.cache[f'A{i+1}'] = A
        
        return A
    
    def backward(self, Y):
        """
        Backward pass - compute gradients
        Y: true labels
        """
        m = Y.shape[0]  # batch size
        gradients = {}
        
        # Output layer gradient (for binary cross-entropy + sigmoid)
        A_final = self.cache[f'A{self.num_layers}']
        dZ = A_final - Y  # Simplified gradient for BCE + sigmoid
        
        # Backpropagate through layers
        for i in range(self.num_layers, 0, -1):
            A_prev = self.cache[f'A{i-1}']
            
            # Compute gradients for this layer
            dW = (1/m) * np.dot(A_prev.T, dZ)
            db = (1/m) * np.sum(dZ, axis=0, keepdims=True)
            
            gradients[f'dW{i}'] = dW
            gradients[f'db{i}'] = db
            
            # Propagate to previous layer (if not input layer)
            if i > 1:
                dA = np.dot(dZ, self.weights[i-1].T)
                Z_prev = self.cache[f'Z{i-1}']
                dZ = dA * relu_derivative(Z_prev)
        
        return gradients
    
    def update_weights(self, gradients, learning_rate):
        """Update weights using gradients"""
        for i in range(self.num_layers):
            self.weights[i] -= learning_rate * gradients[f'dW{i+1}']
            self.biases[i] -= learning_rate * gradients[f'db{i+1}']
    
    def train_step(self, X, Y, learning_rate):
        """One complete training step"""
        # Forward
        predictions = self.forward(X)
        
        # Compute loss (binary cross-entropy)
        epsilon = 1e-15
        loss = -np.mean(Y * np.log(predictions + epsilon) + 
                       (1 - Y) * np.log(1 - predictions + epsilon))
        
        # Backward
        gradients = self.backward(Y)
        
        # Update
        self.update_weights(gradients, learning_rate)
        
        return loss, predictions

# ========== TRAINING EXAMPLE ==========
print("\n" + "=" * 60)
print("TRAINING EXAMPLE: XOR PROBLEM")
print("=" * 60)

print("""
The XOR problem is a classic test - it's NOT linearly separable!
    Input    Output
    (0, 0) → 0
    (0, 1) → 1
    (1, 0) → 1
    (1, 1) → 0

A single perceptron cannot solve this, but a network with
a hidden layer can!
""")

# XOR training data
X_train = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])
Y_train = np.array([[0], [1], [1], [0]])

# Create network: 2 inputs → 4 hidden → 1 output
np.random.seed(42)
nn = SimpleNeuralNetwork([2, 4, 1])

# Train
print("Training on XOR problem:")
print("-" * 40)

losses = []
for epoch in range(1000):
    loss, predictions = nn.train_step(X_train, Y_train, learning_rate=1.0)
    losses.append(loss)
    
    if epoch % 200 == 0:
        accuracy = np.mean((predictions > 0.5) == Y_train) * 100
        print(f"Epoch {epoch:4d}: Loss = {loss:.4f}, Accuracy = {accuracy:.1f}%")

# Final results
print("\n" + "-" * 40)
print("Final Results:")
final_preds = nn.forward(X_train)

for i in range(len(X_train)):
    x_str = f"({X_train[i][0]}, {X_train[i][1]})"
    pred = final_preds[i][0]
    actual = Y_train[i][0]
    pred_class = 1 if pred > 0.5 else 0
    status = "✓" if pred_class == actual else "✗"
    print(f"Input {x_str} → Pred: {pred:.3f} → Class: {pred_class} (Actual: {actual}) {status}")

# ========== GRADIENT CHECKING ==========
print("\n" + "=" * 60)
print("GRADIENT CHECKING (VERIFICATION)")
print("=" * 60)

print("""
Gradient checking helps verify backprop implementation is correct.

NUMERICAL GRADIENT:
    dL/dw ≈ [L(w + ε) - L(w - ε)] / (2ε)

Compare with analytical gradient from backprop.
If close (< 1e-5), implementation is likely correct!
""")

def compute_loss(nn, X, Y):
    """Compute loss for gradient checking"""
    pred = nn.forward(X)
    epsilon = 1e-15
    return -np.mean(Y * np.log(pred + epsilon) + (1 - Y) * np.log(1 - pred + epsilon))

# Check gradient for first weight
eps = 1e-4
original_weight = nn.weights[0][0, 0]

# Numerical gradient
nn.weights[0][0, 0] = original_weight + eps
loss_plus = compute_loss(nn, X_train, Y_train)

nn.weights[0][0, 0] = original_weight - eps
loss_minus = compute_loss(nn, X_train, Y_train)

numerical_grad = (loss_plus - loss_minus) / (2 * eps)

# Analytical gradient (from backprop)
nn.weights[0][0, 0] = original_weight
nn.forward(X_train)
gradients = nn.backward(Y_train)
analytical_grad = gradients['dW1'][0, 0]

print(f"Numerical gradient:  {numerical_grad:.6f}")
print(f"Analytical gradient: {analytical_grad:.6f}")
print(f"Difference: {abs(numerical_grad - analytical_grad):.2e}")
print(f"{'✓ Gradients match!' if abs(numerical_grad - analytical_grad) < 1e-4 else '✗ Gradients differ!'}")

# ========== BACKPROP INTUITION ==========
print("\n" + "=" * 60)
print("BACKPROPAGATION INTUITION")
print("=" * 60)

print("""
🎯 INTUITIVE UNDERSTANDING:

Imagine you're adjusting a recipe that's too salty:

1. FORWARD PASS = Making the dish
   - Mix ingredients according to proportions (weights)
   - Taste the result (prediction)

2. LOSS = How wrong is it?
   - Compare to ideal taste (target)
   - Calculate "saltiness error"

3. BACKWARD PASS = Finding culprits
   - Which ingredient contributed most to saltiness?
   - How much did each step amplify the salt?
   - Track blame back through each step

4. UPDATE = Fix the recipe
   - Reduce salt-contributing ingredients
   - Increase others to balance
   - Try again!

The chain rule lets us track how each weight's change 
ripples through the network to affect the final output.
""")

# ========== COMMON ISSUES ==========
print("\n" + "=" * 60)
print("COMMON BACKPROP ISSUES")
print("=" * 60)

print("""
⚠️ VANISHING GRADIENTS:
Problem: Gradients become tiny as they propagate back
Cause: Sigmoid/tanh in deep networks
Solution: Use ReLU, batch normalization, skip connections

⚠️ EXPLODING GRADIENTS:
Problem: Gradients become huge, causing unstable updates
Cause: Large weights, bad initialization
Solution: Gradient clipping, proper initialization

⚠️ DYING RELU:
Problem: ReLU neurons output 0 for all inputs
Cause: Large negative weights
Solution: Leaky ReLU, careful learning rate

⚠️ SLOW CONVERGENCE:
Problem: Training takes too long
Cause: Poor learning rate, bad initialization
Solution: Adaptive optimizers (Adam), learning rate scheduling
""")

# ========== SUMMARY ==========
print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
✅ Backpropagation computes gradients efficiently using chain rule

✅ Process:
   1. Forward pass: compute predictions, cache values
   2. Compute loss at output
   3. Backward pass: compute gradients layer by layer
   4. Update weights: w = w - learning_rate × gradient

✅ Key formulas for layer l:
   dZ = dA ⊙ g'(Z)  (element-wise multiply with activation derivative)
   dW = (1/m) × A_prev.T · dZ
   db = (1/m) × sum(dZ)
   dA_prev = dZ · W.T

✅ Use gradient checking to verify implementation

✅ Watch out for vanishing/exploding gradients in deep networks
""")

print("\n" + "=" * 60)
print("✅ Backward Propagation - Complete!")
print("=" * 60)
