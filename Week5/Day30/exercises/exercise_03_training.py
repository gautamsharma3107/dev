"""
Day 30 - Exercise 3: Training and Evaluation
=============================================
Practice training and evaluating neural networks.

Complete each exercise to build your skills!
"""

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Set seeds for reproducibility
tf.random.set_seed(42)
np.random.seed(42)

print("=" * 60)
print("EXERCISE 3: TRAINING AND EVALUATION")
print("=" * 60)

# Prepare data for exercises
X, y = make_classification(
    n_samples=1000,
    n_features=15,
    n_informative=10,
    n_classes=2,
    random_state=42
)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

print(f"Training samples: {len(X_train)}")
print(f"Test samples: {len(X_test)}")
print(f"Features: {X_train.shape[1]}")

# ========== Exercise 3.1 ==========
print("\n📝 Exercise 3.1: Build and Train a Model")
print("-" * 40)

# TODO: 
# 1. Create a Sequential model for binary classification
# 2. Compile it with appropriate settings
# 3. Train for 20 epochs with batch_size=32 and validation_split=0.2

# model = Sequential([
#     # Your architecture
# ])

# model.compile(
#     # Your compilation settings
# )

# history = model.fit(
#     # Your training settings
# )

# Uncomment to test:
# print(f"Final training accuracy: {history.history['accuracy'][-1]:.4f}")


# ========== Exercise 3.2 ==========
print("\n📝 Exercise 3.2: Evaluate on Test Data")
print("-" * 40)

# TODO: Use the model from 3.1 to:
# 1. Evaluate on test data
# 2. Print test loss and accuracy

# test_loss, test_accuracy = ???

# Uncomment to test:
# print(f"Test Loss: {test_loss:.4f}")
# print(f"Test Accuracy: {test_accuracy:.4f}")


# ========== Exercise 3.3 ==========
print("\n📝 Exercise 3.3: Make Predictions")
print("-" * 40)

# TODO:
# 1. Get predictions for the first 10 test samples
# 2. Convert probabilities to class labels (threshold 0.5)
# 3. Compare with actual labels

# predictions = ???
# predicted_classes = ???

# Uncomment to test:
# print(f"Probabilities: {predictions.flatten()[:10]}")
# print(f"Predicted: {predicted_classes[:10]}")
# print(f"Actual: {y_test[:10]}")


# ========== Exercise 3.4 ==========
print("\n📝 Exercise 3.4: Use Callbacks")
print("-" * 40)

# TODO: Create a new model and train with EarlyStopping:
# - Monitor 'val_loss'
# - Patience of 5 epochs
# - Restore best weights

# early_stopping = EarlyStopping(
#     # Your settings
# )

# callback_model = Sequential([
#     # Your architecture
# ])

# callback_model.compile(...)

# history = callback_model.fit(
#     X_train, y_train,
#     epochs=100,  # Set high - early stopping will handle it
#     batch_size=32,
#     validation_split=0.2,
#     callbacks=[early_stopping],
#     verbose=1
# )

# Uncomment to test:
# print(f"Training stopped at epoch: {len(history.history['loss'])}")


# ========== Exercise 3.5 ==========
print("\n📝 Exercise 3.5: Compare Different Architectures")
print("-" * 40)

# TODO: Create and compare two different architectures:
# Model A: Simple (1 hidden layer with 32 neurons)
# Model B: Deeper (3 hidden layers with 64, 32, 16 neurons)

# Train both for 20 epochs and compare test accuracy

# model_a = Sequential([...])
# model_b = Sequential([...])

# Compare their test accuracies


# ========== Exercise 3.6 ==========
print("\n📝 Exercise 3.6: Save and Load Model")
print("-" * 40)

# TODO:
# 1. Save your trained model to '/tmp/exercise_model.keras'
# 2. Load it back
# 3. Verify predictions match

# model.save(...)
# loaded_model = load_model(...)

# Verify predictions match


# ========== Exercise 3.7 ==========
print("\n📝 Exercise 3.7: Batch Size Experiment")
print("-" * 40)

# TODO: Train the same model with different batch sizes:
# - batch_size=16
# - batch_size=64
# - batch_size=128
# Compare training time and final accuracy

# Results for different batch sizes:


print("\n" + "=" * 60)
print("Complete the exercises above!")
print("=" * 60)


# ========== SOLUTIONS (Don't look until you try!) ==========
"""
SOLUTIONS:

Exercise 3.1:
model = Sequential([
    Dense(64, activation='relu', input_shape=(15,)),
    Dropout(0.2),
    Dense(32, activation='relu'),
    Dense(1, activation='sigmoid')
])

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

history = model.fit(
    X_train, y_train,
    epochs=20,
    batch_size=32,
    validation_split=0.2,
    verbose=1
)

Exercise 3.2:
test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=0)

Exercise 3.3:
predictions = model.predict(X_test[:10], verbose=0)
predicted_classes = (predictions > 0.5).astype(int).flatten()

Exercise 3.4:
early_stopping = EarlyStopping(
    monitor='val_loss',
    patience=5,
    restore_best_weights=True
)

callback_model = Sequential([
    Dense(64, activation='relu', input_shape=(15,)),
    Dropout(0.3),
    Dense(32, activation='relu'),
    Dense(1, activation='sigmoid')
])

callback_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

history = callback_model.fit(
    X_train, y_train,
    epochs=100,
    batch_size=32,
    validation_split=0.2,
    callbacks=[early_stopping],
    verbose=1
)

Exercise 3.5:
model_a = Sequential([
    Dense(32, activation='relu', input_shape=(15,)),
    Dense(1, activation='sigmoid')
])

model_b = Sequential([
    Dense(64, activation='relu', input_shape=(15,)),
    Dense(32, activation='relu'),
    Dense(16, activation='relu'),
    Dense(1, activation='sigmoid')
])

# Train and compare...

Exercise 3.6:
model.save('/tmp/exercise_model.keras')
from tensorflow.keras.models import load_model
loaded_model = load_model('/tmp/exercise_model.keras')
# Verify with predictions

Exercise 3.7:
# Run training with different batch sizes and compare
# Generally: smaller batch = slower but may generalize better
"""
