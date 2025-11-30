"""
Day 32 - Exercise 3: Fine-Tuning
================================
Practice: Implementing fine-tuning strategies

Instructions:
- Complete each exercise
- Understand when to fine-tune
- Practice unfreezing layers
"""

print("=" * 60)
print("EXERCISE 3: Fine-Tuning")
print("=" * 60)

# ============================================================
# Exercise 3.1: Two-Phase Training Setup
# Set up a model for two-phase training
# ============================================================

print("\n--- Exercise 3.1: Two-Phase Training ---")

# TODO: Load MobileNetV2, freeze it, add classifier, compile for Phase 1
# Your code here:

# Expected: Model ready for feature extraction training

# ============================================================
# Exercise 3.2: Unfreeze Specific Layers
# Unfreeze only the last 20 layers of the base model
# ============================================================

print("\n--- Exercise 3.2: Unfreeze Specific Layers ---")

# TODO: Unfreeze the last 20 layers while keeping earlier layers frozen
# Your code here:

# Expected: Only last 20 layers trainable

# ============================================================
# Exercise 3.3: Different Learning Rates
# Compare learning rates for fine-tuning
# ============================================================

print("\n--- Exercise 3.3: Learning Rates ---")

# TODO: Recompile the model with a very low learning rate for fine-tuning
# Hint: Use 1e-5 or lower
# Your code here:

# Expected: Model compiled with low learning rate

# ============================================================
# Exercise 3.4: Layer Inspection
# Print all layers and their trainable status
# ============================================================

print("\n--- Exercise 3.4: Layer Inspection ---")

# TODO: Print layer name and trainable status for all layers
# Your code here:

# Expected: List of layers with trainable=True/False

# ============================================================
# Exercise 3.5: Callbacks Setup
# Set up appropriate callbacks for fine-tuning
# ============================================================

print("\n--- Exercise 3.5: Callbacks Setup ---")

# TODO: Create callbacks for:
# - EarlyStopping (patience=5)
# - ReduceLROnPlateau (factor=0.2, patience=2)
# - ModelCheckpoint (save best)
# Your code here:

# Expected: List of callbacks ready for training

print("\n" + "=" * 60)
print("SOLUTIONS")
print("=" * 60)

print("""
# Exercise 3.1
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense, Dropout
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam

base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
base_model.trainable = False

x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(256, activation='relu')(x)
x = Dropout(0.5)(x)
outputs = Dense(10, activation='softmax')(x)

model = Model(inputs=base_model.input, outputs=outputs)
model.compile(optimizer=Adam(1e-3), loss='categorical_crossentropy', metrics=['accuracy'])
print("Phase 1 ready!")

# Exercise 3.2
base_model.trainable = True
for layer in base_model.layers[:-20]:
    layer.trainable = False

trainable_layers = sum([1 for l in base_model.layers if l.trainable])
print(f"Trainable layers: {trainable_layers}")

# Exercise 3.3
model.compile(
    optimizer=Adam(learning_rate=1e-5),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)
print(f"Compiled with learning rate: 1e-5")

# Exercise 3.4
for i, layer in enumerate(base_model.layers[-25:]):
    status = "🔓" if layer.trainable else "🔒"
    print(f"{i}: {status} {layer.name}")

# Exercise 3.5
import tensorflow as tf

callbacks = [
    tf.keras.callbacks.EarlyStopping(
        monitor='val_loss',
        patience=5,
        restore_best_weights=True
    ),
    tf.keras.callbacks.ReduceLROnPlateau(
        monitor='val_loss',
        factor=0.2,
        patience=2,
        min_lr=1e-7
    ),
    tf.keras.callbacks.ModelCheckpoint(
        'best_model.keras',
        monitor='val_accuracy',
        save_best_only=True
    )
]
print(f"Created {len(callbacks)} callbacks")
""")

print("\n✅ Exercise 3 Complete!")
