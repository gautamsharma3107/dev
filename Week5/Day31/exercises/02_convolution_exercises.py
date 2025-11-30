"""
EXERCISES: Convolutional Layers
===============================
Complete all 5 exercises below
"""

import numpy as np

# Exercise 1: Calculate Output Dimensions
# TODO: Calculate the output dimensions for different Conv2D configurations

print("Exercise 1: Output Dimension Calculations")
print("-" * 40)

def calculate_conv_output(input_size, kernel_size, stride=1, padding=0):
    """
    Calculate output size after convolution.
    Formula: output = (input - kernel + 2*padding) / stride + 1
    """
    # TODO: Implement this function
    pass

# Test cases:
# Input: 28x28, Kernel: 3x3, Stride: 1, Padding: 0 (valid)
# Expected output: 26x26

# Input: 28x28, Kernel: 3x3, Stride: 1, Padding: 1 (same)
# Expected output: 28x28

# Input: 32x32, Kernel: 5x5, Stride: 2, Padding: 0
# Expected output: 14x14

# Your code here



# Exercise 2: Count Parameters
# TODO: Calculate the number of parameters in Conv2D layers

print("\n\nExercise 2: Parameter Count")
print("-" * 40)

def count_conv_parameters(filters, kernel_size, input_channels, use_bias=True):
    """
    Count parameters in a Conv2D layer.
    Parameters = filters * kernel_h * kernel_w * input_channels + biases
    """
    # TODO: Implement this function
    pass

# Test cases:
# Conv2D(32, (3,3)) on grayscale image (1 channel): 32*(3*3*1) + 32 = 320
# Conv2D(64, (3,3)) on 32-channel input: 64*(3*3*32) + 64 = 18,496

# Your code here



# Exercise 3: Manual Convolution
# TODO: Implement a simple 2D convolution operation

print("\n\nExercise 3: Manual Convolution")
print("-" * 40)

def simple_convolve2d(image, kernel):
    """
    Apply 2D convolution (valid padding, stride=1).
    
    Args:
        image: 2D numpy array (height, width)
        kernel: 2D numpy array (kernel_height, kernel_width)
    
    Returns:
        output: 2D numpy array with convolution result
    """
    # TODO: Implement convolution
    # 1. Calculate output size
    # 2. Slide kernel over image
    # 3. Compute element-wise multiplication and sum
    pass

# Test with:
test_image = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [1, 2, 3, 4]
], dtype=np.float32)

edge_filter = np.array([
    [-1, 0, 1],
    [-1, 0, 1],
    [-1, 0, 1]
], dtype=np.float32)

# TODO: Apply your convolution function
# result = simple_convolve2d(test_image, edge_filter)
# print(f"Convolution result:\n{result}")

# Your code here



# Exercise 4: Understand Feature Maps
# TODO: Given a Conv2D specification, describe the feature maps

print("\n\nExercise 4: Feature Map Analysis")
print("-" * 40)

print("""
Given: 
- Input shape: (32, 32, 3) - RGB image
- Conv2D(64, (3, 3), padding='same', activation='relu')

Answer the following:
1. How many feature maps are produced?
2. What is the shape of each feature map?
3. What is the total output shape?
4. How many parameters does this layer have?

Write your answers as comments below:
""")

# TODO: Answer the questions
# 1. Number of feature maps: 
# 2. Shape of each feature map: 
# 3. Total output shape: 
# 4. Number of parameters: 

# Your code here



# Exercise 5: Design Filter Configurations
# TODO: Design Conv2D configurations for different tasks

print("\n\nExercise 5: Design Configurations")
print("-" * 40)

print("""
Design appropriate Conv2D configurations for:

1. First layer of MNIST classifier (28x28 grayscale)
2. First layer of CIFAR-10 classifier (32x32 RGB)
3. Second layer after MaxPooling (input: 14x14x32)

For each, specify:
- Number of filters
- Kernel size
- Padding (same/valid)
- Input shape (for first layer only)

Write your answers as comments below:
""")

# TODO: Write your configurations
# Example format:
# Conv2D(filters=32, kernel_size=(3,3), padding='same', input_shape=(28,28,1))

# 1. MNIST first layer:

# 2. CIFAR-10 first layer:

# 3. Second layer:

# Your code here

