"""
Day 30 - Exercise 2: Building Neural Networks
==============================================
Practice building and compiling neural networks.

Complete each exercise and run to check your answers.
"""

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, BatchNormalization
import numpy as np

print("=" * 60)
print("EXERCISE 2: BUILDING NEURAL NETWORKS")
print("=" * 60)

# ========== Exercise 2.1 ==========
print("\n📝 Exercise 2.1: Basic Model Structure")
print("-" * 40)

# TODO: Create a Sequential model with:
# - Input: 10 features
# - Hidden layer 1: 32 neurons, ReLU activation
# - Hidden layer 2: 16 neurons, ReLU activation
# - Output: 1 neuron, no activation (for regression)

# model_basic = Sequential([
#     # Your layers here
# ])

# Uncomment to test:
# model_basic.summary()
# print(f"Total layers: {len(model_basic.layers)}")  # Expected: 3


# ========== Exercise 2.2 ==========
print("\n📝 Exercise 2.2: Binary Classification Model")
print("-" * 40)

# TODO: Create a model for binary classification:
# - Input: 20 features
# - Hidden layer: 64 neurons, ReLU activation
# - Hidden layer: 32 neurons, ReLU activation
# - Output: 1 neuron with SIGMOID activation

# binary_model = Sequential([
#     # Your layers here
# ])

# Uncomment to test:
# binary_model.summary()
# print(f"Output activation: {binary_model.layers[-1].activation.__name__}")  # Expected: sigmoid


# ========== Exercise 2.3 ==========
print("\n📝 Exercise 2.3: Multi-class Classification Model")
print("-" * 40)

# TODO: Create a model for 5-class classification:
# - Input: 784 features (like flattened 28x28 images)
# - Hidden layer: 128 neurons, ReLU activation
# - Hidden layer: 64 neurons, ReLU activation
# - Output: 5 neurons with SOFTMAX activation

# multiclass_model = Sequential([
#     # Your layers here
# ])

# Uncomment to test:
# multiclass_model.summary()
# print(f"Output shape: {multiclass_model.output_shape}")  # Expected: (None, 5)


# ========== Exercise 2.4 ==========
print("\n📝 Exercise 2.4: Model with Regularization")
print("-" * 40)

# TODO: Create a model with Dropout and BatchNormalization:
# - Input: 50 features
# - Dense 128 with ReLU, then BatchNorm, then Dropout(0.3)
# - Dense 64 with ReLU, then BatchNorm, then Dropout(0.2)
# - Output: 1 neuron with sigmoid

# regularized_model = Sequential([
#     # Your layers here
# ])

# Uncomment to test:
# regularized_model.summary()
# print(f"Total layers: {len(regularized_model.layers)}")  # Expected: 8


# ========== Exercise 2.5 ==========
print("\n📝 Exercise 2.5: Compile for Binary Classification")
print("-" * 40)

# Create a simple binary classification model
compile_test_model = Sequential([
    Dense(32, activation='relu', input_shape=(10,)),
    Dense(1, activation='sigmoid')
])

# TODO: Compile the model with:
# - Optimizer: Adam with learning_rate=0.001
# - Loss: binary_crossentropy
# - Metrics: accuracy

# compile_test_model.compile(
#     # Your compilation settings
# )

# Uncomment to test:
# print(f"Optimizer: {compile_test_model.optimizer.__class__.__name__}")
# print(f"Loss: {compile_test_model.loss}")


# ========== Exercise 2.6 ==========
print("\n📝 Exercise 2.6: Compile for Multi-class")
print("-" * 40)

# Create a multi-class model
multiclass_compile_model = Sequential([
    Dense(32, activation='relu', input_shape=(10,)),
    Dense(5, activation='softmax')
])

# TODO: Compile for multi-class classification with integer labels:
# - Optimizer: 'adam'
# - Loss: sparse_categorical_crossentropy
# - Metrics: accuracy

# multiclass_compile_model.compile(
#     # Your compilation settings
# )

# Uncomment to test:
# print(f"Loss: {multiclass_compile_model.loss}")


# ========== Exercise 2.7 ==========
print("\n📝 Exercise 2.7: Compile for Regression")
print("-" * 40)

# Create a regression model
regression_model = Sequential([
    Dense(32, activation='relu', input_shape=(10,)),
    Dense(1)  # No activation for regression
])

# TODO: Compile for regression:
# - Optimizer: 'adam'
# - Loss: 'mse' (mean squared error)
# - Metrics: 'mae' (mean absolute error)

# regression_model.compile(
#     # Your compilation settings
# )

# Uncomment to test:
# print(f"Loss: {regression_model.loss}")


# ========== Exercise 2.8 ==========
print("\n📝 Exercise 2.8: Model Inspection")
print("-" * 40)

inspect_model = Sequential([
    Dense(64, activation='relu', input_shape=(20,), name='first_hidden'),
    Dense(32, activation='relu', name='second_hidden'),
    Dense(1, activation='sigmoid', name='output')
])

# TODO: Write code to print:
# 1. Number of layers in the model
# 2. Name of each layer
# 3. Total number of trainable parameters

# Your code here:



print("\n" + "=" * 60)
print("Complete the exercises above!")
print("Remove the # to uncomment and test your answers.")
print("=" * 60)


# ========== SOLUTIONS (Don't look until you try!) ==========
"""
SOLUTIONS:

Exercise 2.1:
model_basic = Sequential([
    Dense(32, activation='relu', input_shape=(10,)),
    Dense(16, activation='relu'),
    Dense(1)
])

Exercise 2.2:
binary_model = Sequential([
    Dense(64, activation='relu', input_shape=(20,)),
    Dense(32, activation='relu'),
    Dense(1, activation='sigmoid')
])

Exercise 2.3:
multiclass_model = Sequential([
    Dense(128, activation='relu', input_shape=(784,)),
    Dense(64, activation='relu'),
    Dense(5, activation='softmax')
])

Exercise 2.4:
regularized_model = Sequential([
    Dense(128, activation='relu', input_shape=(50,)),
    BatchNormalization(),
    Dropout(0.3),
    Dense(64, activation='relu'),
    BatchNormalization(),
    Dropout(0.2),
    Dense(1, activation='sigmoid')
])

Exercise 2.5:
from tensorflow.keras.optimizers import Adam
compile_test_model.compile(
    optimizer=Adam(learning_rate=0.001),
    loss='binary_crossentropy',
    metrics=['accuracy']
)

Exercise 2.6:
multiclass_compile_model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

Exercise 2.7:
regression_model.compile(
    optimizer='adam',
    loss='mse',
    metrics=['mae']
)

Exercise 2.8:
print(f"Number of layers: {len(inspect_model.layers)}")
for layer in inspect_model.layers:
    print(f"Layer name: {layer.name}")
print(f"Total params: {inspect_model.count_params()}")
"""
