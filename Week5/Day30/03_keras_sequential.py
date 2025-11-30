"""
Day 30 - Keras Sequential API
==============================
Learn: Building models with Keras Sequential API

Key Concepts:
- Sequential is a linear stack of layers
- Perfect for simple, layer-by-layer models
- Most common way to build neural networks in Keras
"""

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, BatchNormalization
import numpy as np

# ========== WHAT IS SEQUENTIAL? ==========
print("=" * 60)
print("KERAS SEQUENTIAL API")
print("=" * 60)

print("""
Sequential Model:
- Layers are stacked linearly (one after another)
- Each layer has exactly one input and one output
- Perfect for most neural network architectures

When to use Sequential:
✅ Simple feedforward networks
✅ Most classification/regression tasks
✅ Beginning deep learning projects

When NOT to use Sequential:
❌ Multiple inputs or outputs
❌ Layer sharing
❌ Non-linear topology (use Functional API)
""")

# ========== CREATING A SEQUENTIAL MODEL ==========
print("=" * 60)
print("CREATING A SEQUENTIAL MODEL")
print("=" * 60)

# Method 1: Pass layers to constructor
model1 = Sequential([
    Dense(64, activation='relu', input_shape=(10,)),  # Input layer
    Dense(32, activation='relu'),                      # Hidden layer
    Dense(1)                                           # Output layer
])

print("Method 1: Pass layers to constructor")
model1.summary()

# Method 2: Add layers one by one
print("\n" + "-" * 40)
print("Method 2: Add layers one by one")
model2 = Sequential()
model2.add(Dense(64, activation='relu', input_shape=(10,)))
model2.add(Dense(32, activation='relu'))
model2.add(Dense(1))
model2.summary()

# ========== UNDERSTANDING LAYERS ==========
print("\n" + "=" * 60)
print("UNDERSTANDING LAYERS")
print("=" * 60)

print("""
Dense Layer (Fully Connected):
- Every neuron connects to every neuron in next layer
- Most common layer type
- Parameters: units (neurons), activation, input_shape

Key Parameters:
- units: Number of neurons in the layer
- activation: Activation function (relu, sigmoid, softmax, etc.)
- input_shape: Required for first layer only
""")

# ========== COMMON ACTIVATION FUNCTIONS ==========
print("=" * 60)
print("COMMON ACTIVATION FUNCTIONS")
print("=" * 60)

# Demonstrate activations
x = tf.constant([-2.0, -1.0, 0.0, 1.0, 2.0])

print(f"Input: {x.numpy()}")
print(f"\nReLU: {tf.nn.relu(x).numpy()}")
print(f"Sigmoid: {tf.nn.sigmoid(x).numpy()}")
print(f"Tanh: {tf.nn.tanh(x).numpy()}")
print(f"Softmax: {tf.nn.softmax(x).numpy()}")

print("""
When to use each:

ReLU (relu):
- Hidden layers (most common)
- Avoids vanishing gradient problem
- Output range: [0, infinity)

Sigmoid:
- Binary classification output
- Output range: (0, 1) → probability

Softmax:
- Multi-class classification output
- Outputs sum to 1 (probability distribution)

Tanh:
- Hidden layers (less common now)
- Output range: (-1, 1)

Linear (None):
- Regression output layer
- Output range: (-infinity, infinity)
""")

# ========== BUILDING MODELS FOR DIFFERENT TASKS ==========
print("=" * 60)
print("MODELS FOR DIFFERENT TASKS")
print("=" * 60)

# Binary Classification (e.g., spam detection)
print("Binary Classification Model:")
binary_model = Sequential([
    Dense(64, activation='relu', input_shape=(20,)),
    Dense(32, activation='relu'),
    Dense(1, activation='sigmoid')  # Output: probability 0-1
])
print(f"  Output activation: sigmoid (probability)")
print(f"  Output shape: {binary_model.output_shape}")

# Multi-class Classification (e.g., digit recognition)
print("\nMulti-class Classification Model (10 classes):")
multiclass_model = Sequential([
    Dense(64, activation='relu', input_shape=(784,)),  # 28x28 image flattened
    Dense(32, activation='relu'),
    Dense(10, activation='softmax')  # Output: 10 class probabilities
])
print(f"  Output activation: softmax (10 probabilities sum to 1)")
print(f"  Output shape: {multiclass_model.output_shape}")

# Regression (e.g., house price prediction)
print("\nRegression Model:")
regression_model = Sequential([
    Dense(64, activation='relu', input_shape=(13,)),  # 13 features
    Dense(32, activation='relu'),
    Dense(1)  # Output: single continuous value
])
print(f"  Output activation: None/linear (continuous value)")
print(f"  Output shape: {regression_model.output_shape}")

# ========== ADDING REGULARIZATION ==========
print("\n" + "=" * 60)
print("ADDING REGULARIZATION")
print("=" * 60)

print("""
Regularization prevents overfitting:

1. Dropout: Randomly sets neurons to 0 during training
   - Common: 0.2 to 0.5 dropout rate
   
2. BatchNormalization: Normalizes layer outputs
   - Speeds up training
   - Acts as regularizer
""")

# Model with regularization
regularized_model = Sequential([
    Dense(128, activation='relu', input_shape=(50,)),
    BatchNormalization(),
    Dropout(0.3),
    Dense(64, activation='relu'),
    BatchNormalization(),
    Dropout(0.3),
    Dense(1, activation='sigmoid')
])

print("Model with Dropout and BatchNormalization:")
regularized_model.summary()

# ========== NAMING LAYERS ==========
print("\n" + "=" * 60)
print("NAMING LAYERS AND MODELS")
print("=" * 60)

named_model = Sequential([
    Dense(32, activation='relu', input_shape=(10,), name='hidden_1'),
    Dense(16, activation='relu', name='hidden_2'),
    Dense(1, name='output')
], name='my_named_model')

print(f"Model name: {named_model.name}")
named_model.summary()

# Access layers by name
print(f"\nAccessing layer by name: {named_model.get_layer('hidden_1')}")

# ========== INSPECTING MODELS ==========
print("\n" + "=" * 60)
print("INSPECTING MODELS")
print("=" * 60)

model = Sequential([
    Dense(64, activation='relu', input_shape=(10,)),
    Dense(32, activation='relu'),
    Dense(1)
])

print(f"Number of layers: {len(model.layers)}")
print(f"\nLayer details:")
for i, layer in enumerate(model.layers):
    print(f"  Layer {i}: {layer.name}")
    print(f"    - Type: {type(layer).__name__}")
    print(f"    - Units: {layer.units}")
    print(f"    - Activation: {layer.activation.__name__}")
    print(f"    - Parameters: {layer.count_params()}")

# Get layer by index
print(f"\nFirst layer: {model.layers[0]}")
print(f"Last layer: {model.layers[-1]}")

# Model configuration
print(f"\nModel config: {model.get_config()['name']}")

# ========== PRACTICAL EXAMPLE ==========
print("\n" + "=" * 60)
print("PRACTICAL EXAMPLE: COMPLETE MODEL SETUP")
print("=" * 60)

# Build a practical model for a binary classification problem
practical_model = Sequential([
    # Input layer (100 features)
    Dense(256, activation='relu', input_shape=(100,), name='input_dense'),
    BatchNormalization(),
    Dropout(0.3),
    
    # Hidden layers
    Dense(128, activation='relu', name='hidden_1'),
    BatchNormalization(),
    Dropout(0.3),
    
    Dense(64, activation='relu', name='hidden_2'),
    Dropout(0.2),
    
    # Output layer
    Dense(1, activation='sigmoid', name='output')
], name='practical_classifier')

print("Practical Binary Classifier:")
practical_model.summary()

print(f"\nTotal parameters: {practical_model.count_params():,}")

print("\n" + "=" * 60)
print("✅ Keras Sequential API - Complete!")
print("=" * 60)
print("\nNext: Build your first neural network in 04_first_neural_network.py")
