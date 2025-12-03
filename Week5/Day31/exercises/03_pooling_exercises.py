"""
EXERCISES: Pooling Layers
=========================
Complete all 5 exercises below
"""

import numpy as np

# Exercise 1: Manual Max Pooling
# TODO: Implement max pooling from scratch

print("Exercise 1: Manual Max Pooling")
print("-" * 40)

def max_pool_2d(image, pool_size=2):
    """
    Apply 2x2 max pooling to an image.
    
    Args:
        image: 2D numpy array (height, width)
        pool_size: Size of pooling window (default 2)
    
    Returns:
        output: Pooled image (height//pool_size, width//pool_size)
    """
    # TODO: Implement max pooling
    # 1. Calculate output dimensions
    # 2. For each pool_size x pool_size window, take max value
    pass

# Test with:
test_image = np.array([
    [1, 3, 2, 4],
    [5, 9, 7, 8],
    [4, 2, 6, 3],
    [3, 6, 1, 9]
], dtype=np.float32)

print(f"Input:\n{test_image}")

# TODO: Apply your max pooling function
# result = max_pool_2d(test_image)
# print(f"Max Pooled:\n{result}")

# Your code here



# Exercise 2: Manual Average Pooling
# TODO: Implement average pooling from scratch

print("\n\nExercise 2: Manual Average Pooling")
print("-" * 40)

def avg_pool_2d(image, pool_size=2):
    """
    Apply 2x2 average pooling to an image.
    
    Args:
        image: 2D numpy array (height, width)
        pool_size: Size of pooling window (default 2)
    
    Returns:
        output: Pooled image (height//pool_size, width//pool_size)
    """
    # TODO: Implement average pooling
    pass

# Test with the same image
# result = avg_pool_2d(test_image)
# print(f"Average Pooled:\n{result}")

# Your code here



# Exercise 3: Calculate Output Dimensions
# TODO: Calculate output dimensions after pooling

print("\n\nExercise 3: Pooling Output Dimensions")
print("-" * 40)

def calculate_pooling_output(input_size, pool_size=2, stride=None):
    """
    Calculate output size after pooling.
    Default stride equals pool_size.
    """
    # TODO: Implement this function
    pass

# Test cases:
# Input: 28x28, Pool: 2x2 -> 14x14
# Input: 14x14, Pool: 2x2 -> 7x7
# Input: 7x7, Pool: 3x3 -> ?

# Your code here



# Exercise 4: Track Dimensions Through Network
# TODO: Track how dimensions change through a CNN

print("\n\nExercise 4: Track Network Dimensions")
print("-" * 40)

def track_dimensions(input_shape):
    """
    Track dimensions through a simple CNN:
    Conv2D(32, 3x3, valid) -> MaxPool(2x2) -> Conv2D(64, 3x3, valid) -> MaxPool(2x2)
    
    Args:
        input_shape: Tuple (height, width, channels)
    
    Returns:
        List of shapes after each layer
    """
    # TODO: Implement dimension tracking
    # Example: [(28, 28, 1), (26, 26, 32), (13, 13, 32), ...]
    pass

# Test with MNIST input (28, 28, 1)
# shapes = track_dimensions((28, 28, 1))
# for i, shape in enumerate(shapes):
#     print(f"Layer {i}: {shape}")

# Your code here



# Exercise 5: Compare Pooling Methods
# TODO: Compare max pooling vs average pooling on different inputs

print("\n\nExercise 5: Compare Pooling Methods")
print("-" * 40)

# Create different test cases
uniform_image = np.ones((4, 4)) * 5
gradient_image = np.array([
    [1, 2, 3, 4],
    [2, 3, 4, 5],
    [3, 4, 5, 6],
    [4, 5, 6, 7]
], dtype=np.float32)

sparse_image = np.array([
    [0, 0, 10, 10],
    [0, 0, 10, 10],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
], dtype=np.float32)

print("""
For each image type below, apply both max and average pooling,
then analyze when each method preserves more information.

Test Images:
1. Uniform image (all 5s)
2. Gradient image (smoothly increasing values)
3. Sparse image (mostly zeros with some high values)

Write your analysis as comments below:
""")

# TODO: Apply pooling to each image and analyze
# For uniform image:
# max_result = max_pool_2d(uniform_image)
# avg_result = avg_pool_2d(uniform_image)
# Analysis: ...

# For gradient image:
# Analysis: ...

# For sparse image:
# Analysis: ...

# Your code here

