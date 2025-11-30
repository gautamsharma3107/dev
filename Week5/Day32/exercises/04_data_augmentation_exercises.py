"""
Day 32 - Exercise 4: Data Augmentation
======================================
Practice: Implementing data augmentation techniques

Instructions:
- Complete each exercise
- Visualize augmentation effects
- Build augmentation pipelines
"""

print("=" * 60)
print("EXERCISE 4: Data Augmentation")
print("=" * 60)

# ============================================================
# Exercise 4.1: Basic Augmentation Pipeline
# Create augmentation using Keras preprocessing layers
# ============================================================

print("\n--- Exercise 4.1: Basic Augmentation ---")

# TODO: Create augmentation with:
# - RandomFlip (horizontal)
# - RandomRotation (0.1)
# - RandomZoom (0.2)
# Your code here:

# Expected: Sequential augmentation model

# ============================================================
# Exercise 4.2: Advanced Augmentation
# Add more augmentation techniques
# ============================================================

print("\n--- Exercise 4.2: Advanced Augmentation ---")

# TODO: Create augmentation with all of:
# - RandomFlip
# - RandomRotation
# - RandomZoom
# - RandomContrast
# - RandomBrightness
# Your code here:

# Expected: More comprehensive augmentation pipeline

# ============================================================
# Exercise 4.3: ImageDataGenerator
# Create augmentation using the classic approach
# ============================================================

print("\n--- Exercise 4.3: ImageDataGenerator ---")

# TODO: Create ImageDataGenerator with:
# - rescale=1./255
# - rotation_range=20
# - width_shift_range=0.2
# - height_shift_range=0.2
# - horizontal_flip=True
# - zoom_range=0.2
# Your code here:

# Expected: Configured ImageDataGenerator

# ============================================================
# Exercise 4.4: Integrate Augmentation in Model
# Build a model with augmentation as first layer
# ============================================================

print("\n--- Exercise 4.4: Integrated Augmentation ---")

# TODO: Create a Sequential model that includes:
# - Augmentation layers
# - Rescaling layer
# - MobileNetV2 base
# - Classification head
# Your code here:

# Expected: Complete model with built-in augmentation

# ============================================================
# Exercise 4.5: Augmentation Choices
# Choose appropriate augmentation for different tasks
# ============================================================

print("\n--- Exercise 4.5: Augmentation Choices ---")

tasks = """
Choose appropriate augmentations for each task:

1. Cat vs Dog classification:
   [ ] Horizontal flip
   [ ] Vertical flip
   [ ] Rotation (large)
   [ ] Brightness
   
2. Handwritten digit recognition (MNIST):
   [ ] Horizontal flip
   [ ] Rotation (small)
   [ ] Scale variation
   [ ] Brightness
   
3. Satellite image classification:
   [ ] Horizontal flip
   [ ] Vertical flip
   [ ] Rotation (any angle)
   [ ] Color changes
   
4. Face detection:
   [ ] Horizontal flip
   [ ] Rotation (large)
   [ ] Brightness/Contrast
   [ ] Scale variation
"""
print(tasks)

print("\n" + "=" * 60)
print("SOLUTIONS")
print("=" * 60)

print("""
# Exercise 4.1
import tensorflow as tf
from tensorflow.keras import layers

basic_augmentation = tf.keras.Sequential([
    layers.RandomFlip("horizontal"),
    layers.RandomRotation(0.1),
    layers.RandomZoom(0.2),
])
print("Basic augmentation created!")

# Exercise 4.2
advanced_augmentation = tf.keras.Sequential([
    layers.RandomFlip("horizontal"),
    layers.RandomRotation(0.1),
    layers.RandomZoom(0.2),
    layers.RandomContrast(0.2),
    layers.RandomBrightness(0.1),
])
print("Advanced augmentation created!")

# Exercise 4.3
from tensorflow.keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    horizontal_flip=True,
    zoom_range=0.2
)
print("ImageDataGenerator created!")

# Exercise 4.4
from tensorflow.keras.applications import MobileNetV2

base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
base_model.trainable = False

model = tf.keras.Sequential([
    layers.Input(shape=(224, 224, 3)),
    basic_augmentation,
    layers.Rescaling(1./127.5, offset=-1),
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dense(256, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(10, activation='softmax')
])
print("Model with integrated augmentation created!")

# Exercise 4.5 Answers:
# 1. Cat vs Dog: [x] Horizontal flip, [ ] Vertical flip, [ ] Large rotation, [x] Brightness
# 2. MNIST: [ ] Horizontal flip, [x] Small rotation, [x] Scale, [x] Brightness
# 3. Satellite: [x] Horizontal flip, [x] Vertical flip, [x] Any rotation, [x] Color
# 4. Face detection: [ ] Horizontal flip (faces are asymmetric), [ ] Large rotation, [x] Brightness/Contrast, [x] Scale
""")

print("\n✅ Exercise 4 Complete!")
