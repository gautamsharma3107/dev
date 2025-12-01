"""
Day 30 - Understanding the Training Loop
=========================================
Learn: What happens during model.fit() and custom training loops

Key Concepts:
- Forward pass: input → predictions
- Loss calculation: predictions vs actual
- Backward pass: gradients computation
- Weight update: optimizer step
"""

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam, SGD
import numpy as np

# Set seeds for reproducibility
tf.random.set_seed(42)
np.random.seed(42)

# ========== TRAINING LOOP OVERVIEW ==========
print("=" * 60)
print("THE TRAINING LOOP")
print("=" * 60)

print("""
What happens in each training step:

┌─────────────────────────────────────────────────────────────┐
│  FORWARD PASS                                               │
│  Input (X) → Neural Network → Predictions (ŷ)               │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│  LOSS CALCULATION                                           │
│  Loss = f(predictions, actual_labels)                       │
│  How wrong are we?                                          │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│  BACKWARD PASS (Backpropagation)                            │
│  Calculate gradients: ∂Loss/∂weights for each layer         │
│  How much did each weight contribute to the error?          │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│  WEIGHT UPDATE                                              │
│  new_weight = old_weight - learning_rate × gradient         │
│  Adjust weights to reduce loss                              │
└─────────────────────────────────────────────────────────────┘

This happens for each BATCH, and all batches = one EPOCH.
""")

# ========== SIMPLE DEMONSTRATION ==========
print("=" * 60)
print("SIMPLE DEMONSTRATION")
print("=" * 60)

# Create simple data
X = np.array([[1], [2], [3], [4], [5]], dtype=np.float32)
y = np.array([[2], [4], [6], [8], [10]], dtype=np.float32)  # y = 2x

print("Simple linear relationship: y = 2x")
print(f"X: {X.flatten()}")
print(f"y: {y.flatten()}")

# Create simple model (1 input → 1 output, no activation)
simple_model = Sequential([
    Dense(1, input_shape=(1,), use_bias=True)
])

# Get initial weights
initial_weights = simple_model.get_weights()
print(f"\nInitial weights: {initial_weights[0][0][0]:.4f}")
print(f"Initial bias: {initial_weights[1][0]:.4f}")

# Compile and train
simple_model.compile(optimizer=SGD(learning_rate=0.01), loss='mse')
simple_model.fit(X, y, epochs=100, verbose=0)

# Get trained weights
final_weights = simple_model.get_weights()
print(f"\nTrained weights: {final_weights[0][0][0]:.4f} (should be ~2.0)")
print(f"Trained bias: {final_weights[1][0]:.4f} (should be ~0.0)")

# Test prediction
print(f"\nPrediction for x=6: {simple_model.predict([[6]], verbose=0)[0][0]:.2f} (expected: 12)")

# ========== MANUAL TRAINING LOOP ==========
print("\n" + "=" * 60)
print("MANUAL TRAINING LOOP (GradientTape)")
print("=" * 60)

print("""
tf.GradientTape records operations for automatic differentiation.
This is what happens "under the hood" in model.fit()!
""")

# Create model and optimizer
manual_model = Sequential([Dense(1, input_shape=(1,))])
optimizer = SGD(learning_rate=0.01)
loss_fn = tf.keras.losses.MeanSquaredError()

print("Manual training loop for 5 epochs:")

for epoch in range(5):
    with tf.GradientTape() as tape:
        # Forward pass
        predictions = manual_model(X, training=True)
        
        # Calculate loss
        loss = loss_fn(y, predictions)
    
    # Backward pass - calculate gradients
    gradients = tape.gradient(loss, manual_model.trainable_variables)
    
    # Update weights
    optimizer.apply_gradients(zip(gradients, manual_model.trainable_variables))
    
    print(f"  Epoch {epoch+1}: Loss = {loss.numpy():.4f}")

print("\n✅ This is exactly what model.fit() does internally!")

# ========== BATCHING EXPLAINED ==========
print("\n" + "=" * 60)
print("BATCHING EXPLAINED")
print("=" * 60)

print("""
Why use batches instead of all data at once?

Full Batch (Batch Gradient Descent):
- Use ALL data for each update
- Stable but slow
- May get stuck in local minima

Mini-Batch (Most Common):
- Use SUBSET of data (e.g., 32 samples)
- Balance between speed and stability
- Common sizes: 16, 32, 64, 128, 256

Stochastic (Single Sample):
- Use ONE sample per update
- Very noisy but can escape local minima
- Rarely used in practice

Example with 1000 samples, batch_size=32:
- 1000 / 32 = 31.25 → 32 batches per epoch
- Each batch: forward pass, loss, backward pass, update
- 32 weight updates per epoch
""")

# Demonstrate batching
print("\nDemonstration of batch processing:")

# Create larger dataset
X_large = np.random.randn(100, 5).astype(np.float32)
y_large = np.random.randint(0, 2, 100).astype(np.float32)

batch_model = Sequential([
    Dense(16, activation='relu', input_shape=(5,)),
    Dense(1, activation='sigmoid')
])
batch_model.compile(optimizer='adam', loss='binary_crossentropy')

# Train with different batch sizes
print("\nTraining with batch_size=10:")
batch_model.fit(X_large, y_large, epochs=3, batch_size=10, verbose=1)

# ========== LEARNING RATE IMPACT ==========
print("\n" + "=" * 60)
print("LEARNING RATE IMPACT")
print("=" * 60)

print("""
Learning Rate (lr) controls step size:

Too Small (lr = 0.0001):
- Very slow convergence
- May never reach optimal solution

Just Right (lr = 0.001):
- Smooth convergence
- Finds good solution

Too Large (lr = 0.1 or higher):
- May overshoot optimal solution
- Loss may oscillate or diverge

Common values: 0.001 (default for Adam), 0.01
""")

# ========== CALLBACKS FOR TRAINING CONTROL ==========
print("=" * 60)
print("CALLBACKS FOR TRAINING CONTROL")
print("=" * 60)

print("""
Callbacks let you customize training behavior:

1. EarlyStopping: Stop training when metric stops improving
2. ModelCheckpoint: Save model during training
3. LearningRateScheduler: Adjust learning rate
4. TensorBoard: Visualize training
""")

from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

# Create callbacks
early_stopping = EarlyStopping(
    monitor='val_loss',      # What to monitor
    patience=5,              # How many epochs to wait
    restore_best_weights=True # Restore weights from best epoch
)

print("EarlyStopping configured:")
print("  - monitor: val_loss")
print("  - patience: 5 epochs")
print("  - restore_best_weights: True")

# Example usage (with callbacks)
print("\nTraining with callbacks:")

from sklearn.model_selection import train_test_split
X_train, X_val, y_train, y_val = train_test_split(
    X_large, y_large, test_size=0.2
)

callback_model = Sequential([
    Dense(32, activation='relu', input_shape=(5,)),
    Dense(1, activation='sigmoid')
])
callback_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

history = callback_model.fit(
    X_train, y_train,
    epochs=100,  # Set high - early stopping will handle it
    batch_size=16,
    validation_data=(X_val, y_val),
    callbacks=[early_stopping],
    verbose=1
)

print(f"\nTraining stopped at epoch {len(history.history['loss'])}")

# ========== EPOCHS VS ITERATIONS ==========
print("\n" + "=" * 60)
print("EPOCHS VS ITERATIONS")
print("=" * 60)

print("""
Terminology clarification:

ITERATION (Step):
- One forward + backward pass on ONE BATCH
- One weight update

EPOCH:
- One complete pass through ALL training data
- Multiple iterations per epoch

Example:
- 1000 training samples
- batch_size = 100
- iterations_per_epoch = 1000 / 100 = 10
- If epochs = 5: total iterations = 5 × 10 = 50
""")

# ========== TRAINING TIPS ==========
print("=" * 60)
print("TRAINING TIPS")
print("=" * 60)

print("""
Best Practices:

1. Normalize your data (very important!)
   - StandardScaler for features
   - Neural networks work best with small values

2. Start simple
   - Begin with few layers, add if needed
   - Overfitting? Add dropout or reduce model size

3. Monitor validation loss
   - If val_loss increases while loss decreases = OVERFITTING
   - Use early stopping to prevent

4. Learning rate tuning
   - Start with defaults (Adam: 0.001)
   - If training is unstable, reduce lr
   - If training is slow, increase lr

5. Batch size considerations
   - Larger batch = more stable but may generalize worse
   - Smaller batch = more noise but may generalize better
   - Common: 32, 64, 128

6. Use callbacks
   - EarlyStopping prevents overfitting
   - ModelCheckpoint saves best model
""")

print("\n" + "=" * 60)
print("✅ Training Loop - Complete!")
print("=" * 60)
print("\nNext: Learn about model evaluation in 06_model_evaluation.py")
