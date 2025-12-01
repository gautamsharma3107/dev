"""
Day 30 - Tensors and Basic Operations
=====================================
Learn: Creating tensors and performing operations

Key Concepts:
- Tensors are multi-dimensional arrays
- Similar to NumPy arrays but with GPU support
- Foundation for all deep learning operations
"""

import tensorflow as tf
import numpy as np

# ========== WHAT ARE TENSORS? ==========
print("=" * 60)
print("WHAT ARE TENSORS?")
print("=" * 60)

print("""
Tensors are the fundamental data structure in TensorFlow.

Tensor Dimensions:
- 0D tensor (scalar): Single number → 5
- 1D tensor (vector): Array → [1, 2, 3]
- 2D tensor (matrix): 2D array → [[1,2], [3,4]]
- 3D tensor: Cube of numbers (e.g., image with RGB)
- nD tensor: Higher dimensional data

Think of tensors like NumPy arrays with superpowers!
""")

# ========== CREATING TENSORS ==========
print("=" * 60)
print("CREATING TENSORS")
print("=" * 60)

# 0D Tensor (Scalar)
scalar = tf.constant(5)
print(f"Scalar (0D): {scalar}")
print(f"  Value: {scalar.numpy()}")
print(f"  Shape: {scalar.shape}")
print(f"  Rank/ndim: {scalar.ndim}")

# 1D Tensor (Vector)
vector = tf.constant([1, 2, 3, 4, 5])
print(f"\nVector (1D): {vector}")
print(f"  Shape: {vector.shape}")
print(f"  Rank/ndim: {vector.ndim}")

# 2D Tensor (Matrix)
matrix = tf.constant([[1, 2, 3],
                      [4, 5, 6]])
print(f"\nMatrix (2D):\n{matrix}")
print(f"  Shape: {matrix.shape}")
print(f"  Rank/ndim: {matrix.ndim}")

# 3D Tensor
tensor_3d = tf.constant([[[1, 2], [3, 4]],
                         [[5, 6], [7, 8]]])
print(f"\n3D Tensor:\n{tensor_3d}")
print(f"  Shape: {tensor_3d.shape}")
print(f"  Rank/ndim: {tensor_3d.ndim}")

# ========== TENSOR DATA TYPES ==========
print("\n" + "=" * 60)
print("TENSOR DATA TYPES")
print("=" * 60)

# Different dtypes
int_tensor = tf.constant([1, 2, 3], dtype=tf.int32)
float_tensor = tf.constant([1.0, 2.0, 3.0], dtype=tf.float32)
bool_tensor = tf.constant([True, False, True])
string_tensor = tf.constant(["hello", "world"])

print(f"Integer tensor: {int_tensor}, dtype: {int_tensor.dtype}")
print(f"Float tensor: {float_tensor}, dtype: {float_tensor.dtype}")
print(f"Boolean tensor: {bool_tensor}, dtype: {bool_tensor.dtype}")
print(f"String tensor: {string_tensor}, dtype: {string_tensor.dtype}")

# Type casting
casted = tf.cast(int_tensor, dtype=tf.float32)
print(f"\nCasted int to float: {casted}, dtype: {casted.dtype}")

# ========== CREATING SPECIAL TENSORS ==========
print("\n" + "=" * 60)
print("SPECIAL TENSOR CREATION")
print("=" * 60)

# Zeros
zeros = tf.zeros((3, 4))
print(f"Zeros (3x4):\n{zeros}")

# Ones
ones = tf.ones((2, 3))
print(f"\nOnes (2x3):\n{ones}")

# Fill with value
filled = tf.fill((2, 2), 7)
print(f"\nFilled with 7 (2x2):\n{filled}")

# Range
range_tensor = tf.range(0, 10, 2)
print(f"\nRange (0 to 10, step 2): {range_tensor}")

# Random tensors
random_uniform = tf.random.uniform((2, 3), minval=0, maxval=10)
print(f"\nRandom Uniform (2x3):\n{random_uniform}")

random_normal = tf.random.normal((2, 3), mean=0, stddev=1)
print(f"\nRandom Normal (2x3):\n{random_normal}")

# ========== TENSOR OPERATIONS ==========
print("\n" + "=" * 60)
print("TENSOR OPERATIONS")
print("=" * 60)

a = tf.constant([[1, 2], [3, 4]], dtype=tf.float32)
b = tf.constant([[5, 6], [7, 8]], dtype=tf.float32)

print(f"Tensor a:\n{a}")
print(f"\nTensor b:\n{b}")

# Element-wise operations
print(f"\na + b:\n{a + b}")
print(f"\na - b:\n{a - b}")
print(f"\na * b (element-wise):\n{a * b}")
print(f"\na / b:\n{a / b}")

# Using tf functions
print(f"\ntf.add(a, b):\n{tf.add(a, b)}")
print(f"\ntf.multiply(a, b):\n{tf.multiply(a, b)}")

# Matrix multiplication
print(f"\nMatrix multiplication (a @ b):\n{a @ b}")
print(f"Or tf.matmul(a, b):\n{tf.matmul(a, b)}")

# ========== REDUCTION OPERATIONS ==========
print("\n" + "=" * 60)
print("REDUCTION OPERATIONS")
print("=" * 60)

x = tf.constant([[1, 2, 3], [4, 5, 6]], dtype=tf.float32)
print(f"Tensor x:\n{x}")

print(f"\nSum all: {tf.reduce_sum(x)}")
print(f"Sum along axis 0 (columns): {tf.reduce_sum(x, axis=0)}")
print(f"Sum along axis 1 (rows): {tf.reduce_sum(x, axis=1)}")

print(f"\nMean: {tf.reduce_mean(x)}")
print(f"Max: {tf.reduce_max(x)}")
print(f"Min: {tf.reduce_min(x)}")
print(f"Argmax (index of max): {tf.argmax(x, axis=1)}")

# ========== RESHAPING TENSORS ==========
print("\n" + "=" * 60)
print("RESHAPING TENSORS")
print("=" * 60)

original = tf.range(12)
print(f"Original (12 elements): {original}")

# Reshape
reshaped = tf.reshape(original, (3, 4))
print(f"\nReshaped to (3, 4):\n{reshaped}")

reshaped2 = tf.reshape(original, (2, 2, 3))
print(f"\nReshaped to (2, 2, 3):\n{reshaped2}")

# Automatic dimension with -1
auto_reshaped = tf.reshape(original, (4, -1))  # -1 means "figure it out"
print(f"\nReshaped with -1 (4, -1) → (4, 3):\n{auto_reshaped}")

# Flatten
flattened = tf.reshape(reshaped, [-1])
print(f"\nFlattened: {flattened}")

# ========== INDEXING AND SLICING ==========
print("\n" + "=" * 60)
print("INDEXING AND SLICING")
print("=" * 60)

t = tf.constant([[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 10, 11, 12]])
print(f"Tensor t:\n{t}")

print(f"\nt[0]: {t[0]}")
print(f"t[0, 0]: {t[0, 0]}")
print(f"t[:, 0]: {t[:, 0]}")  # First column
print(f"t[0:2, 1:3]:\n{t[0:2, 1:3]}")

# ========== NUMPY INTEROPERABILITY ==========
print("\n" + "=" * 60)
print("NUMPY INTEROPERABILITY")
print("=" * 60)

# Tensor to NumPy
tensor = tf.constant([[1, 2], [3, 4]])
numpy_array = tensor.numpy()
print(f"Tensor to NumPy:\n{numpy_array}")
print(f"Type: {type(numpy_array)}")

# NumPy to Tensor
np_array = np.array([[5, 6], [7, 8]])
from_numpy = tf.constant(np_array)
print(f"\nNumPy to Tensor:\n{from_numpy}")
print(f"Type: {type(from_numpy)}")

# Operations work together
result = tensor + np_array
print(f"\nTensor + NumPy array:\n{result}")

# ========== VARIABLES (MUTABLE TENSORS) ==========
print("\n" + "=" * 60)
print("TENSORFLOW VARIABLES")
print("=" * 60)

# Variables are mutable tensors (for weights in neural networks)
var = tf.Variable([[1, 2], [3, 4]], dtype=tf.float32)
print(f"Variable:\n{var}")

# Modify in-place
var.assign([[5, 6], [7, 8]])
print(f"\nAfter assign:\n{var}")

var.assign_add([[1, 1], [1, 1]])
print(f"\nAfter assign_add:\n{var}")

# This is how neural network weights are updated during training!

print("\n" + "=" * 60)
print("✅ Tensors and Basic Operations - Complete!")
print("=" * 60)
print("\nNext: Learn about Keras Sequential API in 03_keras_sequential.py")
