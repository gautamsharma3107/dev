"""
Day 32 - Exercise 1: Transfer Learning Basics
=============================================
Practice: Understanding and implementing basic transfer learning

Instructions:
- Complete each exercise
- Run the code to verify your solution
- Check against the expected output
"""

print("=" * 60)
print("EXERCISE 1: Transfer Learning Basics")
print("=" * 60)

# ============================================================
# Exercise 1.1: Load Pre-trained Model
# Load VGG16 without top layer for 224x224 images
# ============================================================

print("\n--- Exercise 1.1: Load Pre-trained Model ---")

# TODO: Import VGG16 and load it with imagenet weights, without top
# Your code here:
# from tensorflow.keras.applications import VGG16
# base_model = VGG16(...)

# Expected: Model with ~14.7M parameters

# ============================================================
# Exercise 1.2: Freeze Base Model
# Make all layers in the base model non-trainable
# ============================================================

print("\n--- Exercise 1.2: Freeze Base Model ---")

# TODO: Freeze the base model
# Your code here:

# Expected: All layers should have trainable=False

# ============================================================
# Exercise 1.3: Count Parameters
# Count trainable vs non-trainable parameters
# ============================================================

print("\n--- Exercise 1.3: Count Parameters ---")

# TODO: Print the number of trainable and non-trainable parameters
# Hint: Use model.count_params() or sum trainable_weights
# Your code here:

# Expected: 0 trainable, ~14.7M non-trainable

# ============================================================
# Exercise 1.4: Add Custom Layers
# Add GlobalAveragePooling and Dense layers for 5-class classification
# ============================================================

print("\n--- Exercise 1.4: Add Custom Layers ---")

# TODO: Build a model with:
# - base_model
# - GlobalAveragePooling2D
# - Dense(256, activation='relu')
# - Dropout(0.5)
# - Dense(5, activation='softmax')
# Your code here:

# Expected: Complete model ready for training

# ============================================================
# Exercise 1.5: Compile Model
# Compile with appropriate optimizer, loss, and metrics
# ============================================================

print("\n--- Exercise 1.5: Compile Model ---")

# TODO: Compile the model with:
# - optimizer: adam
# - loss: categorical_crossentropy
# - metrics: accuracy
# Your code here:

# Expected: Model compiled successfully

print("\n" + "=" * 60)
print("SOLUTIONS")
print("=" * 60)

print("""
# Exercise 1.1
from tensorflow.keras.applications import VGG16
base_model = VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
print(f"Loaded VGG16 with {base_model.count_params():,} parameters")

# Exercise 1.2
base_model.trainable = False

# Exercise 1.3
import tensorflow as tf
trainable = sum([tf.size(w).numpy() for w in base_model.trainable_weights])
non_trainable = sum([tf.size(w).numpy() for w in base_model.non_trainable_weights])
print(f"Trainable: {trainable:,}, Non-trainable: {non_trainable:,}")

# Exercise 1.4
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense, Dropout
from tensorflow.keras.models import Model

x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(256, activation='relu')(x)
x = Dropout(0.5)(x)
outputs = Dense(5, activation='softmax')(x)
model = Model(inputs=base_model.input, outputs=outputs)

# Exercise 1.5
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
print("Model compiled successfully!")
""")

print("\n✅ Exercise 1 Complete!")
