"""
Day 29 - Neurons, Layers, Weights, and Biases
==============================================
Learn: The building blocks of neural networks

Key Concepts:
- Neurons are the basic units that process information
- Layers organize neurons at different processing stages
- Weights determine the importance of each input
- Biases allow neurons to activate even with zero input
"""

import numpy as np

# ========== THE NEURON ==========
print("=" * 60)
print("THE ARTIFICIAL NEURON")
print("=" * 60)

print("""
🧬 BIOLOGICAL INSPIRATION:
Real neurons receive signals through dendrites, process them 
in the cell body, and send output through axons.

Artificial neurons work similarly:
    Inputs (x) → Weighted Sum (z) → Activation (a) → Output

MATHEMATICAL REPRESENTATION:
    z = w₁x₁ + w₂x₂ + ... + wₙxₙ + b
    a = activation(z)

Where:
    x = inputs
    w = weights
    b = bias
    z = weighted sum (pre-activation)
    a = activated output
""")

# ========== IMPLEMENTING A NEURON ==========
print("\n" + "=" * 60)
print("IMPLEMENTING A SINGLE NEURON")
print("=" * 60)

def neuron(inputs, weights, bias, activation_fn):
    """
    A single artificial neuron
    
    Parameters:
    - inputs: array of input values
    - weights: array of weights (same size as inputs)
    - bias: single bias value
    - activation_fn: function to apply non-linearity
    
    Returns:
    - activated output value
    """
    # Step 1: Calculate weighted sum
    z = np.dot(inputs, weights) + bias
    
    # Step 2: Apply activation function
    a = activation_fn(z)
    
    return a, z

# Simple activation function (ReLU for now)
def relu(z):
    return max(0, z)

# Example neuron computation
inputs = np.array([1.0, 2.0, 3.0])   # Three input features
weights = np.array([0.5, -0.3, 0.2])  # Corresponding weights
bias = 0.1

output, z = neuron(inputs, weights, bias, relu)

print(f"Inputs:  {inputs}")
print(f"Weights: {weights}")
print(f"Bias:    {bias}")
print(f"\nCalculation:")
print(f"  z = (1.0 × 0.5) + (2.0 × -0.3) + (3.0 × 0.2) + 0.1")
print(f"  z = 0.5 - 0.6 + 0.6 + 0.1 = {z}")
print(f"  output = ReLU({z}) = {output}")

# ========== WEIGHTS ==========
print("\n" + "=" * 60)
print("UNDERSTANDING WEIGHTS")
print("=" * 60)

print("""
⚖️ WHAT ARE WEIGHTS?
Weights are learnable parameters that determine how much 
influence each input has on the neuron's output.

KEY PROPERTIES:
- Positive weights: Input and output move together
- Negative weights: Input and output move oppositely
- Large weights: Strong influence
- Small weights: Weak influence
- Zero weights: No influence (input ignored)

INITIALIZATION:
- Usually initialized randomly (small values)
- Poor initialization can cause training problems
""")

# Demonstrate weight effects
print("\nDemonstrating Weight Effects:")
print("-" * 40)

test_inputs = np.array([2.0, 3.0])

weight_scenarios = [
    ([0.5, 0.5], "Equal positive weights"),
    ([1.0, 0.0], "Only first input matters"),
    ([0.0, 1.0], "Only second input matters"),
    ([-0.5, 0.5], "First input has negative effect"),
    ([2.0, 2.0], "Large positive weights"),
]

for weights, description in weight_scenarios:
    weights = np.array(weights)
    z = np.dot(test_inputs, weights)
    print(f"{description}:")
    print(f"  weights = {weights}")
    print(f"  z = {test_inputs} · {weights} = {z}\n")

# ========== BIASES ==========
print("\n" + "=" * 60)
print("UNDERSTANDING BIASES")
print("=" * 60)

print("""
⚡ WHAT IS BIAS?
Bias is a learnable parameter that allows the neuron to 
shift its activation function left or right.

WHY BIAS IS IMPORTANT:
- Allows neuron to output non-zero even when all inputs are zero
- Gives the neuron flexibility to fit data better
- Without bias, the decision boundary must pass through origin

ANALOGY:
Think of bias like the y-intercept in y = mx + b
It shifts the line up or down.
""")

# Demonstrate bias effects
print("\nDemonstrating Bias Effects:")
print("-" * 40)

weights = np.array([1.0, 1.0])
test_inputs = np.array([0.0, 0.0])  # Zero inputs

bias_values = [-1.0, 0.0, 1.0, 5.0]

for b in bias_values:
    z = np.dot(test_inputs, weights) + b
    output = relu(z)
    print(f"Bias = {b:5.1f}: z = {z:5.1f}, ReLU output = {output}")

print("\nWith zero inputs and positive bias, neuron can still activate!")

# ========== LAYERS ==========
print("\n" + "=" * 60)
print("UNDERSTANDING LAYERS")
print("=" * 60)

print("""
📚 WHAT ARE LAYERS?
A layer is a collection of neurons that process data at 
the same level of abstraction.

LAYER TYPES:

1. INPUT LAYER
   - Receives raw features
   - No computation (just passes data)
   - Size = number of features

2. HIDDEN LAYERS
   - Perform the actual learning
   - Transform data through multiple stages
   - Can have multiple hidden layers (deep learning)

3. OUTPUT LAYER
   - Produces final predictions
   - Size depends on task:
     * Regression: 1 neuron
     * Binary classification: 1 neuron (sigmoid)
     * Multi-class: n neurons (softmax)
""")

# ========== IMPLEMENTING A LAYER ==========
print("\n" + "=" * 60)
print("IMPLEMENTING A LAYER")
print("=" * 60)

class DenseLayer:
    """
    A fully connected (dense) layer
    """
    def __init__(self, input_size, output_size, activation='relu'):
        """
        Initialize layer with random weights and zero biases
        """
        # Initialize weights using Xavier/Glorot initialization
        self.weights = np.random.randn(input_size, output_size) * np.sqrt(2.0 / input_size)
        self.biases = np.zeros((1, output_size))
        self.activation = activation
        
    def forward(self, inputs):
        """
        Compute forward pass through the layer
        """
        # Linear transformation
        z = np.dot(inputs, self.weights) + self.biases
        
        # Apply activation
        if self.activation == 'relu':
            a = np.maximum(0, z)
        elif self.activation == 'sigmoid':
            a = 1 / (1 + np.exp(-z))
        elif self.activation == 'linear':
            a = z
        else:
            a = z
            
        return a

# Create and use a layer
print("Creating a Dense Layer:")
print("-" * 40)

# Layer: 3 inputs → 4 neurons
layer = DenseLayer(input_size=3, output_size=4, activation='relu')

print(f"Input size: 3")
print(f"Output size (neurons): 4")
print(f"Weights shape: {layer.weights.shape}")
print(f"Biases shape: {layer.biases.shape}")

# Forward pass
sample_input = np.array([[1.0, 2.0, 3.0]])  # 1 sample, 3 features
output = layer.forward(sample_input)

print(f"\nSample input: {sample_input}")
print(f"Layer output: {output}")

# ========== BUILDING A SIMPLE NETWORK ==========
print("\n" + "=" * 60)
print("BUILDING A SIMPLE NEURAL NETWORK")
print("=" * 60)

class SimpleNeuralNetwork:
    """
    A simple neural network with configurable layers
    """
    def __init__(self, layer_sizes, activations):
        """
        layer_sizes: list of sizes [input, hidden1, hidden2, ..., output]
        activations: list of activation functions for each layer
        """
        self.layers = []
        
        for i in range(len(layer_sizes) - 1):
            layer = DenseLayer(
                input_size=layer_sizes[i],
                output_size=layer_sizes[i + 1],
                activation=activations[i]
            )
            self.layers.append(layer)
    
    def forward(self, x):
        """
        Forward pass through all layers
        """
        for layer in self.layers:
            x = layer.forward(x)
        return x

# Create a network: 3 inputs → 4 hidden → 2 outputs
print("Creating Network: 3 → 4 → 2")
print("-" * 40)

network = SimpleNeuralNetwork(
    layer_sizes=[3, 4, 2],
    activations=['relu', 'sigmoid']
)

# Forward pass
sample_input = np.array([[1.0, 2.0, 3.0]])
output = network.forward(sample_input)

print(f"Network architecture:")
print(f"  Input layer:  3 features")
print(f"  Hidden layer: 4 neurons (ReLU)")
print(f"  Output layer: 2 neurons (Sigmoid)")
print(f"\nSample input: {sample_input}")
print(f"Network output: {output}")

# ========== VISUALIZING CONNECTIONS ==========
print("\n" + "=" * 60)
print("VISUALIZING NETWORK CONNECTIONS")
print("=" * 60)

print("""
Network: 3 inputs → 4 hidden → 2 outputs

    INPUT           HIDDEN          OUTPUT
    LAYER           LAYER           LAYER
    
    ○─────────────►○──────────────►○
    x₁   w[0][0]   h₁    w'[0][0]  y₁
     ╲             ╱ ╲             ╱
      ╲           ╱   ╲           ╱
    ○──╲─────────╱─────╲─────────╱──►○
    x₂  ╲       ╱○      ╲       ╱    y₂
         ╲     ╱  h₂     ╲     ╱
          ╲   ╱           ╲   ╱
    ○──────╲─╱─────────────╲─╱
    x₃      ╳○              ╳
           ╱ h₃            ╱
          ╱               ╱
         ╱    ○──────────╱
              h₄

Total connections (weights):
    Input → Hidden: 3 × 4 = 12 weights
    Hidden → Output: 4 × 2 = 8 weights
    Total weights: 20

Total biases:
    Hidden layer: 4 biases
    Output layer: 2 biases
    Total biases: 6

TOTAL LEARNABLE PARAMETERS: 26
""")

# ========== PARAMETER COUNT ==========
print("\n" + "=" * 60)
print("COUNTING PARAMETERS")
print("=" * 60)

def count_parameters(layer_sizes):
    """Count total trainable parameters in a network"""
    total_weights = 0
    total_biases = 0
    
    for i in range(len(layer_sizes) - 1):
        weights = layer_sizes[i] * layer_sizes[i + 1]
        biases = layer_sizes[i + 1]
        total_weights += weights
        total_biases += biases
        print(f"Layer {i + 1}: {layer_sizes[i]} → {layer_sizes[i + 1]}")
        print(f"  Weights: {layer_sizes[i]} × {layer_sizes[i + 1]} = {weights}")
        print(f"  Biases: {biases}")
    
    return total_weights + total_biases

print("Parameter Count Examples:")
print("-" * 40)

# Small network
print("\nSmall Network [3, 4, 2]:")
total = count_parameters([3, 4, 2])
print(f"Total Parameters: {total}")

# Larger network
print("\nLarger Network [784, 128, 64, 10]:")
total = count_parameters([784, 128, 64, 10])
print(f"Total Parameters: {total}")

# ========== SUMMARY ==========
print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
✅ NEURON: Basic unit - computes weighted sum + activation
   output = activation(Σ(weight × input) + bias)

✅ WEIGHTS: Determine importance of each input
   - Learnable through training
   - Initialized randomly

✅ BIASES: Allow shifting of activation
   - Also learnable
   - Usually initialized to zero

✅ LAYERS: Collections of neurons
   - Input layer: receives data
   - Hidden layers: transform data
   - Output layer: makes predictions

✅ DENSE LAYER: Every neuron connected to all inputs
   - Most common layer type
   - Parameters = (input_size × output_size) + output_size
""")

print("\n" + "=" * 60)
print("✅ Neurons, Layers, Weights, and Biases - Complete!")
print("=" * 60)
