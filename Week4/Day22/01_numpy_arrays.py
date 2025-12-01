"""
Day 22 - NumPy Arrays Basics
============================
Learn: Creating and working with NumPy arrays

Key Concepts:
- NumPy is the foundation of data science in Python
- Arrays are faster than Python lists
- Vectorized operations avoid loops
- Homogeneous data types (all same type)
"""

import numpy as np

print("=" * 60)
print("NUMPY ARRAYS BASICS")
print("=" * 60)

# ========== WHY NUMPY? ==========
print("\n" + "=" * 60)
print("WHY NUMPY?")
print("=" * 60)

print("""
NumPy Benefits:
1. Speed - Much faster than Python lists
2. Memory efficient - Stores data more compactly
3. Vectorization - Operations on entire arrays at once
4. Broadcasting - Smart element-wise operations
5. Foundation for Pandas, Scikit-learn, TensorFlow
""")

# Speed comparison (concept)
print("Speed Example (concept):")
print("Python list loop for 1M elements: ~100ms")
print("NumPy vectorized for 1M elements: ~1ms")
print("NumPy is ~100x faster!")

# ========== CREATING ARRAYS ==========
print("\n" + "=" * 60)
print("CREATING ARRAYS")
print("=" * 60)

# From Python list
print("\n1. From Python list:")
arr_1d = np.array([1, 2, 3, 4, 5])
print(f"   1D array: {arr_1d}")

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(f"   2D array:\n{arr_2d}")

arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(f"   3D array shape: {arr_3d.shape}")

# Special arrays
print("\n2. Special arrays:")

zeros = np.zeros((3, 4))
print(f"   Zeros (3x4):\n{zeros}")

ones = np.ones((2, 3))
print(f"   Ones (2x3):\n{ones}")

full = np.full((3, 3), 7)
print(f"   Full with 7 (3x3):\n{full}")

eye = np.eye(4)
print(f"   Identity (4x4):\n{eye}")

# Ranges
print("\n3. Ranges and sequences:")

arange = np.arange(0, 10, 2)  # start, stop, step
print(f"   arange(0, 10, 2): {arange}")

linspace = np.linspace(0, 1, 5)  # start, stop, num_points
print(f"   linspace(0, 1, 5): {linspace}")

# Random arrays
print("\n4. Random arrays:")

np.random.seed(42)  # For reproducibility
rand_float = np.random.rand(3, 3)  # 0 to 1
print(f"   Random floats (3x3):\n{rand_float.round(2)}")

rand_int = np.random.randint(0, 100, (3, 3))  # 0 to 99
print(f"   Random ints (3x3):\n{rand_int}")

rand_normal = np.random.randn(3, 3)  # Standard normal
print(f"   Random normal (3x3):\n{rand_normal.round(2)}")

# ========== ARRAY PROPERTIES ==========
print("\n" + "=" * 60)
print("ARRAY PROPERTIES")
print("=" * 60)

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(f"Array:\n{arr}")
print(f"\n   shape:    {arr.shape}    # (rows, cols)")
print(f"   dtype:    {arr.dtype}    # Data type")
print(f"   ndim:     {arr.ndim}         # Number of dimensions")
print(f"   size:     {arr.size}        # Total elements")
print(f"   itemsize: {arr.itemsize}         # Bytes per element")
print(f"   nbytes:   {arr.nbytes}        # Total bytes")

# ========== DATA TYPES ==========
print("\n" + "=" * 60)
print("DATA TYPES")
print("=" * 60)

print("""
Common dtypes:
- int32, int64    : Integers
- float32, float64: Floats
- bool            : True/False
- str_            : Strings (fixed length)
- object          : Any Python object
""")

# Specifying dtype
arr_int = np.array([1, 2, 3], dtype=np.int32)
print(f"int32 array: {arr_int}, dtype: {arr_int.dtype}")

arr_float = np.array([1, 2, 3], dtype=np.float64)
print(f"float64 array: {arr_float}, dtype: {arr_float.dtype}")

# Type conversion
arr_converted = arr_int.astype(np.float64)
print(f"Converted to float: {arr_converted}")

# ========== INDEXING ==========
print("\n" + "=" * 60)
print("INDEXING")
print("=" * 60)

arr_1d = np.array([10, 20, 30, 40, 50])
print(f"1D array: {arr_1d}")
print(f"   arr[0]:  {arr_1d[0]}   # First element")
print(f"   arr[-1]: {arr_1d[-1]}   # Last element")
print(f"   arr[2]:  {arr_1d[2]}   # Third element")

arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"\n2D array:\n{arr_2d}")
print(f"   arr[0, 0]: {arr_2d[0, 0]}  # Top-left")
print(f"   arr[1, 2]: {arr_2d[1, 2]}  # Row 1, Col 2")
print(f"   arr[-1, -1]: {arr_2d[-1, -1]}  # Bottom-right")
print(f"   arr[0]: {arr_2d[0]}  # First row")

# ========== SLICING ==========
print("\n" + "=" * 60)
print("SLICING")
print("=" * 60)

arr_1d = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90])
print(f"1D array: {arr_1d}")
print(f"   arr[2:5]:  {arr_1d[2:5]}    # Elements 2-4")
print(f"   arr[:4]:   {arr_1d[:4]}     # First 4")
print(f"   arr[6:]:   {arr_1d[6:]}     # From index 6")
print(f"   arr[::2]:  {arr_1d[::2]}    # Every other")
print(f"   arr[::-1]: {arr_1d[::-1]}   # Reversed")

arr_2d = np.array([[1, 2, 3, 4], 
                   [5, 6, 7, 8], 
                   [9, 10, 11, 12]])
print(f"\n2D array:\n{arr_2d}")
print(f"   arr[:2, :2] (top-left 2x2):\n{arr_2d[:2, :2]}")
print(f"   arr[:, 0] (first column): {arr_2d[:, 0]}")
print(f"   arr[1, :] (second row): {arr_2d[1, :]}")
print(f"   arr[1:, 2:] (bottom-right):\n{arr_2d[1:, 2:]}")

# ========== BOOLEAN INDEXING ==========
print("\n" + "=" * 60)
print("BOOLEAN INDEXING")
print("=" * 60)

arr = np.array([15, 22, 8, 35, 12, 45, 28, 5])
print(f"Array: {arr}")

# Create boolean mask
mask = arr > 20
print(f"   Mask (arr > 20): {mask}")
print(f"   Filtered: {arr[mask]}")

# Direct filtering
print(f"   arr[arr > 20]: {arr[arr > 20]}")
print(f"   arr[arr % 2 == 0]: {arr[arr % 2 == 0]}  # Even numbers")

# Multiple conditions
print(f"   arr[(arr > 10) & (arr < 30)]: {arr[(arr > 10) & (arr < 30)]}")

# ========== FANCY INDEXING ==========
print("\n" + "=" * 60)
print("FANCY INDEXING")
print("=" * 60)

arr = np.array([10, 20, 30, 40, 50, 60, 70])
print(f"Array: {arr}")

# Index with array of indices
indices = [1, 3, 5]
print(f"   arr[[1, 3, 5]]: {arr[indices]}")

# 2D fancy indexing
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"\n2D array:\n{arr_2d}")
print(f"   arr_2d[[0, 2]]: Select rows 0 and 2:\n{arr_2d[[0, 2]]}")

# ========== COPY VS VIEW ==========
print("\n" + "=" * 60)
print("COPY VS VIEW (Important!)")
print("=" * 60)

original = np.array([1, 2, 3, 4, 5])

# Slicing creates a view (shares memory)
view = original[1:4]
view[0] = 999
print(f"After modifying view:")
print(f"   View: {view}")
print(f"   Original also changed: {original}")

# To avoid this, use copy()
original = np.array([1, 2, 3, 4, 5])
copy = original[1:4].copy()
copy[0] = 999
print(f"\nAfter modifying copy:")
print(f"   Copy: {copy}")
print(f"   Original unchanged: {original}")

# ========== PRACTICAL EXAMPLE ==========
print("\n" + "=" * 60)
print("PRACTICAL EXAMPLE: Grade Analysis")
print("=" * 60)

# Student grades in 3 subjects
grades = np.array([
    [85, 90, 78],  # Student 1
    [92, 88, 95],  # Student 2
    [70, 75, 68],  # Student 3
    [88, 92, 90],  # Student 4
    [65, 70, 72],  # Student 5
])
subjects = ['Math', 'Science', 'English']
print("Grades (rows=students, cols=subjects):")
print(grades)

print(f"\nAnalysis:")
print(f"   Average per student: {grades.mean(axis=1)}")
print(f"   Average per subject: {grades.mean(axis=0)}")
print(f"   Highest grade: {grades.max()}")
print(f"   Lowest grade: {grades.min()}")
print(f"   Students with Math > 80: {(grades[:, 0] > 80).sum()}")

# Find passing grades (>= 70)
passing = grades >= 70
print(f"\n   Passing grades (>=70):\n{passing}")

print("\n" + "=" * 60)
print("✅ NumPy Arrays Basics - Complete!")
print("=" * 60)
