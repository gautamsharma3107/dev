"""
EXERCISES: Image Data Basics
============================
Complete all 5 exercises below
"""

import numpy as np

# Exercise 1: Understanding Image Shapes
# TODO: Create arrays representing different image types
# and print their shapes

print("Exercise 1: Image Shapes")
print("-" * 40)
# Create a grayscale image array (28x28)
# Create an RGB image array (32x32x3)
# Create a batch of 10 grayscale images (10, 28, 28, 1)
# Your code here



# Exercise 2: Normalization Practice
# TODO: Take the sample image below and normalize it to [0, 1] range
# Then normalize it to [-1, 1] range

print("\n\nExercise 2: Normalization")
print("-" * 40)

sample_image = np.array([
    [0, 64, 128, 192, 255],
    [32, 96, 160, 224, 128],
    [64, 128, 192, 64, 192]
], dtype=np.uint8)

print(f"Original image:\n{sample_image}")
print(f"Original range: [{sample_image.min()}, {sample_image.max()}]")

# TODO: Normalize to [0, 1]
# normalized_01 = ...

# TODO: Normalize to [-1, 1]
# normalized_11 = ...

# Your code here



# Exercise 3: Reshaping for CNN
# TODO: Take a batch of flattened images and reshape them for CNN input

print("\n\nExercise 3: Reshaping")
print("-" * 40)

# 100 images flattened to 784 (28*28) dimensions
flattened_batch = np.random.rand(100, 784)
print(f"Flattened shape: {flattened_batch.shape}")

# TODO: Reshape to (100, 28, 28, 1) for Keras CNN
# reshaped = ...

# Your code here



# Exercise 4: Adding Dimensions
# TODO: Take a single image and prepare it for model.predict()

print("\n\nExercise 4: Adding Batch Dimension")
print("-" * 40)

single_image = np.random.rand(28, 28, 1)  # Single image with channel
print(f"Single image shape: {single_image.shape}")

# TODO: Add batch dimension to make it (1, 28, 28, 1)
# Use np.expand_dims
# ready_for_predict = ...

# Your code here



# Exercise 5: Complete Preprocessing Pipeline
# TODO: Implement a complete preprocessing function

print("\n\nExercise 5: Complete Pipeline")
print("-" * 40)

def preprocess_mnist(x_train, x_test):
    """
    Complete preprocessing pipeline for MNIST data.
    
    Args:
        x_train: Training images, shape (60000, 28, 28)
        x_test: Test images, shape (10000, 28, 28)
    
    Returns:
        x_train_processed: Shape (60000, 28, 28, 1), normalized to [0, 1]
        x_test_processed: Shape (10000, 28, 28, 1), normalized to [0, 1]
    """
    # TODO: Implement the function
    # 1. Reshape to add channel dimension
    # 2. Convert to float32
    # 3. Normalize to [0, 1]
    pass

# Test with simulated data
x_train_sim = np.random.randint(0, 256, (60000, 28, 28), dtype=np.uint8)
x_test_sim = np.random.randint(0, 256, (10000, 28, 28), dtype=np.uint8)

# TODO: Call your function and verify the output shapes
# x_train_proc, x_test_proc = preprocess_mnist(x_train_sim, x_test_sim)
# print(f"Processed training shape: {x_train_proc.shape}")
# print(f"Processed test shape: {x_test_proc.shape}")

# Your code here

