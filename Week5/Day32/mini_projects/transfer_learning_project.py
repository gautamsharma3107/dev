"""
Day 32 Mini Project: Transfer Learning for Custom Image Classification
======================================================================

Project: Build an image classifier using transfer learning

This project demonstrates the complete workflow:
1. Load and preprocess custom image data
2. Apply data augmentation
3. Use a pre-trained model (MobileNetV2)
4. Fine-tune for custom classification
5. Evaluate and save the model

Requirements:
- tensorflow >= 2.0
- matplotlib
- numpy
"""

import os
import numpy as np

print("=" * 70)
print("MINI PROJECT: Transfer Learning Image Classifier")
print("=" * 70)

# ============================================================
# STEP 1: Setup and Configuration
# ============================================================

print("\n--- Step 1: Setup ---")

# Configuration
IMG_SIZE = (224, 224)
BATCH_SIZE = 32
NUM_CLASSES = 3  # Example: cats, dogs, birds
EPOCHS_PHASE1 = 5
EPOCHS_PHASE2 = 3

print(f"Image size: {IMG_SIZE}")
print(f"Batch size: {BATCH_SIZE}")
print(f"Number of classes: {NUM_CLASSES}")

# ============================================================
# STEP 2: Create Sample Data (for demonstration)
# In real projects, you'd use actual image directories
# ============================================================

print("\n--- Step 2: Create Sample Data ---")

# Create dummy data for demonstration
# In practice, use: tf.keras.utils.image_dataset_from_directory()

try:
    import tensorflow as tf
    
    # Generate random sample data
    np.random.seed(42)
    X_train = np.random.rand(100, 224, 224, 3).astype(np.float32)
    y_train = np.random.randint(0, NUM_CLASSES, 100)
    y_train = tf.keras.utils.to_categorical(y_train, NUM_CLASSES)
    
    X_val = np.random.rand(20, 224, 224, 3).astype(np.float32)
    y_val = np.random.randint(0, NUM_CLASSES, 20)
    y_val = tf.keras.utils.to_categorical(y_val, NUM_CLASSES)
    
    print(f"Training samples: {X_train.shape[0]}")
    print(f"Validation samples: {X_val.shape[0]}")
    print(f"Image shape: {X_train.shape[1:]}")
    
except ImportError:
    print("TensorFlow not installed. Install with: pip install tensorflow")
    exit()

# ============================================================
# STEP 3: Create Data Augmentation Pipeline
# ============================================================

print("\n--- Step 3: Data Augmentation ---")

from tensorflow.keras import layers

data_augmentation = tf.keras.Sequential([
    layers.RandomFlip("horizontal"),
    layers.RandomRotation(0.1),
    layers.RandomZoom(0.2),
    layers.RandomContrast(0.2),
], name="data_augmentation")

print("Augmentation pipeline created:")
for layer in data_augmentation.layers:
    print(f"  - {layer.name}")

# ============================================================
# STEP 4: Load Pre-trained Model
# ============================================================

print("\n--- Step 4: Load Pre-trained Model ---")

from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

# Load MobileNetV2 without top layer
base_model = MobileNetV2(
    weights='imagenet',
    include_top=False,
    input_shape=(224, 224, 3)
)

print(f"Loaded MobileNetV2")
print(f"  Layers: {len(base_model.layers)}")
print(f"  Parameters: {base_model.count_params():,}")

# ============================================================
# STEP 5: Build Complete Model
# ============================================================

print("\n--- Step 5: Build Model ---")

from tensorflow.keras.layers import GlobalAveragePooling2D, Dense, Dropout
from tensorflow.keras.models import Model

# Phase 1: Freeze base model
base_model.trainable = False

# Build model
inputs = tf.keras.Input(shape=(224, 224, 3))
x = data_augmentation(inputs)
x = preprocess_input(x)  # Preprocessing for MobileNetV2
x = base_model(x, training=False)
x = GlobalAveragePooling2D()(x)
x = Dense(256, activation='relu')(x)
x = Dropout(0.5)(x)
outputs = Dense(NUM_CLASSES, activation='softmax')(x)

model = Model(inputs, outputs)

# Count parameters
trainable_count = sum([tf.size(w).numpy() for w in model.trainable_weights])
total_count = model.count_params()

print(f"Model built successfully!")
print(f"  Total parameters: {total_count:,}")
print(f"  Trainable parameters: {trainable_count:,}")
print(f"  Non-trainable parameters: {total_count - trainable_count:,}")

# ============================================================
# STEP 6: Compile Model (Phase 1)
# ============================================================

print("\n--- Step 6: Compile Model (Phase 1 - Feature Extraction) ---")

from tensorflow.keras.optimizers import Adam

model.compile(
    optimizer=Adam(learning_rate=1e-3),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

print(f"Optimizer: Adam")
print(f"Learning rate: 0.001")
print(f"Loss: categorical_crossentropy")

# ============================================================
# STEP 7: Setup Callbacks
# ============================================================

print("\n--- Step 7: Setup Callbacks ---")

callbacks = [
    tf.keras.callbacks.EarlyStopping(
        monitor='val_loss',
        patience=3,
        restore_best_weights=True,
        verbose=1
    ),
    tf.keras.callbacks.ReduceLROnPlateau(
        monitor='val_loss',
        factor=0.2,
        patience=2,
        min_lr=1e-7,
        verbose=1
    )
]

print(f"Callbacks: EarlyStopping, ReduceLROnPlateau")

# ============================================================
# STEP 8: Train Phase 1 (Feature Extraction)
# ============================================================

print("\n--- Step 8: Train Phase 1 (Feature Extraction) ---")

history1 = model.fit(
    X_train, y_train,
    batch_size=BATCH_SIZE,
    epochs=EPOCHS_PHASE1,
    validation_data=(X_val, y_val),
    callbacks=callbacks,
    verbose=1
)

print(f"\nPhase 1 Complete!")
print(f"Final training accuracy: {history1.history['accuracy'][-1]:.4f}")
print(f"Final validation accuracy: {history1.history['val_accuracy'][-1]:.4f}")

# ============================================================
# STEP 9: Fine-Tuning (Phase 2)
# ============================================================

print("\n--- Step 9: Fine-Tuning (Phase 2) ---")

# Unfreeze base model
base_model.trainable = True

# Freeze early layers, unfreeze last 20
fine_tune_at = len(base_model.layers) - 20
for layer in base_model.layers[:fine_tune_at]:
    layer.trainable = False

# Count trainable parameters
trainable_count = sum([tf.size(w).numpy() for w in model.trainable_weights])
print(f"Unfrozen last {len(base_model.layers) - fine_tune_at} layers")
print(f"Trainable parameters now: {trainable_count:,}")

# Recompile with lower learning rate
model.compile(
    optimizer=Adam(learning_rate=1e-5),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

print(f"Recompiled with learning rate: 0.00001")

# Train Phase 2
history2 = model.fit(
    X_train, y_train,
    batch_size=BATCH_SIZE,
    epochs=EPOCHS_PHASE2,
    validation_data=(X_val, y_val),
    callbacks=callbacks,
    verbose=1
)

print(f"\nPhase 2 Complete!")
print(f"Final training accuracy: {history2.history['accuracy'][-1]:.4f}")
print(f"Final validation accuracy: {history2.history['val_accuracy'][-1]:.4f}")

# ============================================================
# STEP 10: Evaluate Model
# ============================================================

print("\n--- Step 10: Evaluate Model ---")

# Evaluate on validation set
val_loss, val_acc = model.evaluate(X_val, y_val, verbose=0)
print(f"Validation Loss: {val_loss:.4f}")
print(f"Validation Accuracy: {val_acc:.4f}")

# Make predictions
predictions = model.predict(X_val[:5], verbose=0)
predicted_classes = np.argmax(predictions, axis=1)
actual_classes = np.argmax(y_val[:5], axis=1)

print(f"\nSample Predictions:")
for i in range(5):
    print(f"  Sample {i+1}: Predicted={predicted_classes[i]}, Actual={actual_classes[i]}")

# ============================================================
# STEP 11: Save Model
# ============================================================

print("\n--- Step 11: Save Model ---")

# Save the complete model
model_path = "/tmp/transfer_learning_model.keras"
model.save(model_path)
print(f"Model saved to: {model_path}")

# Save only weights
weights_path = "/tmp/transfer_learning_weights.weights.h5"
model.save_weights(weights_path)
print(f"Weights saved to: {weights_path}")

# ============================================================
# PROJECT COMPLETE
# ============================================================

print("\n" + "=" * 70)
print("PROJECT COMPLETE! 🎉")
print("=" * 70)

summary = """
Summary:
--------
✅ Loaded pre-trained MobileNetV2
✅ Created data augmentation pipeline
✅ Built custom classification head
✅ Trained with two-phase approach:
   - Phase 1: Feature extraction (frozen base)
   - Phase 2: Fine-tuning (unfrozen top layers)
✅ Evaluated model performance
✅ Saved model and weights

Next Steps:
-----------
1. Use real image data instead of random samples
2. Experiment with different pre-trained models
3. Try different augmentation strategies
4. Tune hyperparameters for better performance
5. Deploy model with Flask/FastAPI
"""
print(summary)

# ============================================================
# TEMPLATE FOR REAL DATA
# ============================================================

real_data_template = """
# Template for loading real image data:

# From directory structure
train_ds = tf.keras.utils.image_dataset_from_directory(
    'data/train',
    image_size=(224, 224),
    batch_size=32,
    label_mode='categorical'
)

val_ds = tf.keras.utils.image_dataset_from_directory(
    'data/validation',
    image_size=(224, 224),
    batch_size=32,
    label_mode='categorical'
)

# Optimize performance
AUTOTUNE = tf.data.AUTOTUNE
train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)

# Train with datasets
model.fit(train_ds, epochs=10, validation_data=val_ds)
"""

print("\n--- Template for Real Data ---")
print(real_data_template)
