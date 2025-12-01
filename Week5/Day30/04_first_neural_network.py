"""
Day 30 - Building Your First Neural Network
=============================================
Learn: Create, compile, and understand a complete neural network

Key Concepts:
- Building a neural network from scratch
- Understanding model compilation
- Loss functions and optimizers
- Training on real data
"""

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam, SGD
import numpy as np

# Set random seed for reproducibility
tf.random.set_seed(42)
np.random.seed(42)

# ========== OVERVIEW ==========
print("=" * 60)
print("BUILDING YOUR FIRST NEURAL NETWORK")
print("=" * 60)

print("""
Steps to Build a Neural Network:

1. Prepare your data (X, y)
2. Define the model architecture
3. Compile the model (loss, optimizer, metrics)
4. Train the model (fit)
5. Evaluate and predict

Let's build a network to solve a classification problem!
""")

# ========== STEP 1: PREPARE DATA ==========
print("=" * 60)
print("STEP 1: PREPARE DATA")
print("=" * 60)

# Create synthetic dataset for binary classification
# Features: 2D points, Labels: 0 or 1
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

# Generate synthetic data
X, y = make_classification(
    n_samples=1000,
    n_features=20,
    n_informative=15,
    n_redundant=5,
    n_classes=2,
    random_state=42
)

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"Training samples: {X_train.shape[0]}")
print(f"Test samples: {X_test.shape[0]}")
print(f"Number of features: {X_train.shape[1]}")
print(f"Unique classes: {np.unique(y)}")

# Normalize features (important for neural networks!)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

print("\n✅ Data normalized (mean=0, std=1)")

# ========== STEP 2: DEFINE MODEL ==========
print("\n" + "=" * 60)
print("STEP 2: DEFINE MODEL ARCHITECTURE")
print("=" * 60)

# Build the neural network
model = Sequential([
    # Input layer: 20 features → 64 neurons
    Dense(64, activation='relu', input_shape=(20,), name='hidden_1'),
    Dropout(0.2),  # Prevent overfitting
    
    # Hidden layer: 64 → 32 neurons
    Dense(32, activation='relu', name='hidden_2'),
    Dropout(0.2),
    
    # Output layer: 1 neuron with sigmoid for binary classification
    Dense(1, activation='sigmoid', name='output')
], name='first_neural_network')

print("Model Architecture:")
model.summary()

print("""
Architecture Explanation:
- Layer 1: 20 inputs → 64 neurons (ReLU activation)
- Dropout: Randomly drops 20% of connections during training
- Layer 2: 64 → 32 neurons (ReLU activation)
- Dropout: Another 20% dropout
- Output: 32 → 1 neuron (Sigmoid for probability 0-1)
""")

# ========== STEP 3: COMPILE MODEL ==========
print("=" * 60)
print("STEP 3: COMPILE MODEL")
print("=" * 60)

print("""
Compilation Configuration:

1. OPTIMIZER: Algorithm to update weights
   - Adam: Adaptive learning rate (most popular)
   - SGD: Classic stochastic gradient descent
   - RMSprop: Good for RNNs

2. LOSS FUNCTION: What we minimize
   - binary_crossentropy: Binary classification
   - categorical_crossentropy: Multi-class (one-hot labels)
   - sparse_categorical_crossentropy: Multi-class (integer labels)
   - mse: Regression

3. METRICS: What we monitor (doesn't affect training)
   - accuracy: Classification accuracy
   - mae: Mean absolute error
   - Custom metrics
""")

# Compile the model
model.compile(
    optimizer=Adam(learning_rate=0.001),  # Adaptive learning rate
    loss='binary_crossentropy',            # For binary classification
    metrics=['accuracy']                   # Track accuracy during training
)

print("✅ Model compiled!")
print(f"   Optimizer: Adam (lr=0.001)")
print(f"   Loss: binary_crossentropy")
print(f"   Metrics: accuracy")

# ========== STEP 4: TRAIN MODEL ==========
print("\n" + "=" * 60)
print("STEP 4: TRAIN MODEL")
print("=" * 60)

print("""
Training Parameters:

- epochs: Number of times to go through entire dataset
- batch_size: Number of samples per gradient update
- validation_split: Fraction of data for validation
- verbose: 0=silent, 1=progress bar, 2=one line per epoch
""")

# Train the model
print("\nTraining started...\n")

history = model.fit(
    X_train, y_train,
    epochs=20,
    batch_size=32,
    validation_split=0.2,  # Use 20% of training data for validation
    verbose=1
)

print("\n✅ Training complete!")

# ========== UNDERSTANDING TRAINING OUTPUT ==========
print("\n" + "=" * 60)
print("UNDERSTANDING TRAINING OUTPUT")
print("=" * 60)

print("""
Each epoch shows:
- loss: Training loss (what we minimize)
- accuracy: Training accuracy
- val_loss: Validation loss (monitor for overfitting)
- val_accuracy: Validation accuracy

Good signs:
✅ Both loss values decreasing
✅ Both accuracy values increasing
✅ val_loss close to loss (no overfitting)

Warning signs:
⚠️ val_loss increasing while loss decreases = OVERFITTING
⚠️ Large gap between training and validation = OVERFITTING
""")

# ========== STEP 5: EVALUATE MODEL ==========
print("=" * 60)
print("STEP 5: EVALUATE MODEL")
print("=" * 60)

# Evaluate on test set
test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=0)

print(f"\nTest Results:")
print(f"  Loss: {test_loss:.4f}")
print(f"  Accuracy: {test_accuracy:.4f} ({test_accuracy*100:.2f}%)")

# ========== MAKING PREDICTIONS ==========
print("\n" + "=" * 60)
print("MAKING PREDICTIONS")
print("=" * 60)

# Predict probabilities
predictions = model.predict(X_test[:5], verbose=0)
print("Predictions (probabilities):")
for i, pred in enumerate(predictions):
    print(f"  Sample {i+1}: {pred[0]:.4f} → Class: {1 if pred[0] > 0.5 else 0}")

# Actual labels
print(f"\nActual labels: {y_test[:5]}")

# For binary classification, convert probabilities to classes
predicted_classes = (predictions > 0.5).astype(int)
print(f"Predicted classes: {predicted_classes.flatten()}")

# ========== TRAINING HISTORY ==========
print("\n" + "=" * 60)
print("TRAINING HISTORY")
print("=" * 60)

print("History contains metrics from each epoch:")
print(f"  Keys: {list(history.history.keys())}")

print(f"\nFinal training loss: {history.history['loss'][-1]:.4f}")
print(f"Final training accuracy: {history.history['accuracy'][-1]:.4f}")
print(f"Final validation loss: {history.history['val_loss'][-1]:.4f}")
print(f"Final validation accuracy: {history.history['val_accuracy'][-1]:.4f}")

# ========== VISUALIZE TRAINING (Optional) ==========
print("\n" + "=" * 60)
print("VISUALIZE TRAINING")
print("=" * 60)

# Code to visualize (uncomment if matplotlib is available)
print("""
# Visualize training history (run this code separately)

import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# Plot loss
axes[0].plot(history.history['loss'], label='Training Loss')
axes[0].plot(history.history['val_loss'], label='Validation Loss')
axes[0].set_title('Model Loss')
axes[0].set_xlabel('Epoch')
axes[0].set_ylabel('Loss')
axes[0].legend()

# Plot accuracy
axes[1].plot(history.history['accuracy'], label='Training Accuracy')
axes[1].plot(history.history['val_accuracy'], label='Validation Accuracy')
axes[1].set_title('Model Accuracy')
axes[1].set_xlabel('Epoch')
axes[1].set_ylabel('Accuracy')
axes[1].legend()

plt.tight_layout()
plt.savefig('training_history.png')
plt.show()
""")

print("\n" + "=" * 60)
print("✅ Your First Neural Network - Complete!")
print("=" * 60)
print("\nNext: Dive deeper into training loops in 05_training_loop.py")
