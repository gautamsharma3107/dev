"""
Day 32 - Exercise 2: Pre-trained Models
=======================================
Practice: Working with different pre-trained models

Instructions:
- Complete each exercise
- Compare different models
- Understand their trade-offs
"""

print("=" * 60)
print("EXERCISE 2: Pre-trained Models")
print("=" * 60)

# ============================================================
# Exercise 2.1: Compare Model Sizes
# Load and compare VGG16, ResNet50, and MobileNetV2
# ============================================================

print("\n--- Exercise 2.1: Compare Model Sizes ---")

# TODO: Load all three models and compare their parameter counts
# Your code here:

# Expected output:
# VGG16: ~14.7M parameters
# ResNet50: ~23.5M parameters
# MobileNetV2: ~2.2M parameters

# ============================================================
# Exercise 2.2: Preprocessing Functions
# Use correct preprocessing for each model
# ============================================================

print("\n--- Exercise 2.2: Preprocessing Functions ---")

# TODO: Import and demonstrate the preprocessing function for each model
# Hint: from tensorflow.keras.applications.vgg16 import preprocess_input
# Your code here:

# Expected: Show how each model preprocesses input differently

# ============================================================
# Exercise 2.3: Feature Extraction Shapes
# Check output shape of each model
# ============================================================

print("\n--- Exercise 2.3: Feature Extraction Shapes ---")

# TODO: Create a sample input and get output shape from each model
# Your code here:

# Expected:
# VGG16: (None, 7, 7, 512)
# ResNet50: (None, 7, 7, 2048)
# MobileNetV2: (None, 7, 7, 1280)

# ============================================================
# Exercise 2.4: Model Selection Decision
# Choose the best model for different scenarios
# ============================================================

print("\n--- Exercise 2.4: Model Selection ---")

scenarios = """
Choose the best model for each scenario:

1. Mobile app with limited resources: _______________
2. Research project needing best accuracy: _______________
3. Learning/educational purposes: _______________
4. Cloud deployment with fast inference needed: _______________
5. Small dataset (500 images): _______________
"""
print(scenarios)

# Fill in your answers!

print("\n" + "=" * 60)
print("SOLUTIONS")
print("=" * 60)

print("""
# Exercise 2.1
from tensorflow.keras.applications import VGG16, ResNet50, MobileNetV2

vgg = VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
resnet = ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
mobilenet = MobileNetV2(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

print(f"VGG16: {vgg.count_params():,}")
print(f"ResNet50: {resnet.count_params():,}")
print(f"MobileNetV2: {mobilenet.count_params():,}")

# Exercise 2.2
from tensorflow.keras.applications.vgg16 import preprocess_input as vgg_preprocess
from tensorflow.keras.applications.resnet50 import preprocess_input as resnet_preprocess
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input as mobilenet_preprocess

import numpy as np
sample = np.random.rand(1, 224, 224, 3) * 255

print(f"VGG16 preprocessing: {vgg_preprocess(sample.copy()).min():.1f} to {vgg_preprocess(sample.copy()).max():.1f}")
print(f"ResNet50 preprocessing: {resnet_preprocess(sample.copy()).min():.1f} to {resnet_preprocess(sample.copy()).max():.1f}")
print(f"MobileNetV2 preprocessing: {mobilenet_preprocess(sample.copy()).min():.2f} to {mobilenet_preprocess(sample.copy()).max():.2f}")

# Exercise 2.3
print(f"VGG16 output shape: {vgg.output_shape}")
print(f"ResNet50 output shape: {resnet.output_shape}")
print(f"MobileNetV2 output shape: {mobilenet.output_shape}")

# Exercise 2.4 Answers:
# 1. Mobile app: MobileNetV2 (smallest, fastest)
# 2. Best accuracy: EfficientNetB7 or ResNet101
# 3. Learning: VGG16 (simple architecture)
# 4. Fast inference: MobileNetV2 or EfficientNetB0
# 5. Small dataset: MobileNetV2 (fewer params, less overfitting)
""")

print("\n✅ Exercise 2 Complete!")
