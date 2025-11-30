"""
Day 30 - Exercise 1: Tensor Basics
===================================
Practice creating and manipulating tensors.

Complete each exercise and run to check your answers.
"""

import tensorflow as tf
import numpy as np

print("=" * 60)
print("EXERCISE 1: TENSOR BASICS")
print("=" * 60)

# ========== Exercise 1.1 ==========
print("\n📝 Exercise 1.1: Create Tensors")
print("-" * 40)

# TODO: Create a 1D tensor with values [10, 20, 30, 40, 50]
# tensor_1d = ???

# Uncomment to test:
# print(f"1D Tensor: {tensor_1d}")
# print(f"Shape: {tensor_1d.shape}")  # Expected: (5,)


# ========== Exercise 1.2 ==========
print("\n📝 Exercise 1.2: Create 2D Tensor")
print("-" * 40)

# TODO: Create a 2x3 matrix with values [[1, 2, 3], [4, 5, 6]]
# tensor_2d = ???

# Uncomment to test:
# print(f"2D Tensor:\n{tensor_2d}")
# print(f"Shape: {tensor_2d.shape}")  # Expected: (2, 3)


# ========== Exercise 1.3 ==========
print("\n📝 Exercise 1.3: Special Tensors")
print("-" * 40)

# TODO: Create a 4x4 tensor filled with zeros
# zeros_tensor = ???

# TODO: Create a 3x3 tensor filled with ones
# ones_tensor = ???

# TODO: Create a tensor with values from 0 to 9
# range_tensor = ???

# Uncomment to test:
# print(f"Zeros 4x4:\n{zeros_tensor}")
# print(f"Ones 3x3:\n{ones_tensor}")
# print(f"Range 0-9: {range_tensor}")


# ========== Exercise 1.4 ==========
print("\n📝 Exercise 1.4: Tensor Operations")
print("-" * 40)

a = tf.constant([[1, 2], [3, 4]], dtype=tf.float32)
b = tf.constant([[5, 6], [7, 8]], dtype=tf.float32)

# TODO: Calculate element-wise sum of a and b
# sum_result = ???

# TODO: Calculate matrix multiplication of a and b
# matmul_result = ???

# TODO: Calculate element-wise multiplication
# multiply_result = ???

# Uncomment to test:
# print(f"a + b:\n{sum_result}")      # Expected: [[6, 8], [10, 12]]
# print(f"a @ b:\n{matmul_result}")   # Expected: [[19, 22], [43, 50]]
# print(f"a * b:\n{multiply_result}") # Expected: [[5, 12], [21, 32]]


# ========== Exercise 1.5 ==========
print("\n📝 Exercise 1.5: Reduction Operations")
print("-" * 40)

x = tf.constant([[1, 2, 3], [4, 5, 6]], dtype=tf.float32)

# TODO: Calculate the sum of all elements
# total_sum = ???

# TODO: Calculate the mean of all elements
# mean_value = ???

# TODO: Find the maximum value
# max_value = ???

# TODO: Sum along axis 0 (columns)
# col_sum = ???

# Uncomment to test:
# print(f"Total sum: {total_sum}")  # Expected: 21
# print(f"Mean: {mean_value}")       # Expected: 3.5
# print(f"Max: {max_value}")         # Expected: 6
# print(f"Column sums: {col_sum}")   # Expected: [5, 7, 9]


# ========== Exercise 1.6 ==========
print("\n📝 Exercise 1.6: Reshaping")
print("-" * 40)

original = tf.range(12)

# TODO: Reshape to (3, 4)
# reshaped_3x4 = ???

# TODO: Reshape to (2, 2, 3)
# reshaped_2x2x3 = ???

# TODO: Flatten back to 1D
# flattened = ???

# Uncomment to test:
# print(f"Original: {original}")
# print(f"Reshaped (3, 4):\n{reshaped_3x4}")
# print(f"Reshaped (2, 2, 3):\n{reshaped_2x2x3}")
# print(f"Flattened: {flattened}")


# ========== Exercise 1.7 ==========
print("\n📝 Exercise 1.7: NumPy Interoperability")
print("-" * 40)

np_array = np.array([[1, 2, 3], [4, 5, 6]])

# TODO: Convert NumPy array to TensorFlow tensor
# tf_tensor = ???

# TODO: Create a tensor and convert it to NumPy
# my_tensor = tf.constant([[10, 20], [30, 40]])
# back_to_numpy = ???

# Uncomment to test:
# print(f"NumPy to Tensor:\n{tf_tensor}")
# print(f"Type: {type(tf_tensor)}")
# print(f"Tensor to NumPy:\n{back_to_numpy}")
# print(f"Type: {type(back_to_numpy)}")


print("\n" + "=" * 60)
print("Complete the exercises above!")
print("Remove the # to uncomment and test your answers.")
print("=" * 60)


# ========== SOLUTIONS (Don't look until you try!) ==========
"""
SOLUTIONS:

Exercise 1.1:
tensor_1d = tf.constant([10, 20, 30, 40, 50])

Exercise 1.2:
tensor_2d = tf.constant([[1, 2, 3], [4, 5, 6]])

Exercise 1.3:
zeros_tensor = tf.zeros((4, 4))
ones_tensor = tf.ones((3, 3))
range_tensor = tf.range(10)

Exercise 1.4:
sum_result = a + b  # or tf.add(a, b)
matmul_result = a @ b  # or tf.matmul(a, b)
multiply_result = a * b  # or tf.multiply(a, b)

Exercise 1.5:
total_sum = tf.reduce_sum(x)
mean_value = tf.reduce_mean(x)
max_value = tf.reduce_max(x)
col_sum = tf.reduce_sum(x, axis=0)

Exercise 1.6:
reshaped_3x4 = tf.reshape(original, (3, 4))
reshaped_2x2x3 = tf.reshape(original, (2, 2, 3))
flattened = tf.reshape(reshaped_3x4, [-1])

Exercise 1.7:
tf_tensor = tf.constant(np_array)
back_to_numpy = my_tensor.numpy()
"""
