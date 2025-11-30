"""
Day 22 - NumPy Operations
=========================
Learn: Advanced NumPy operations and mathematical functions

Key Concepts:
- Element-wise operations
- Broadcasting
- Reshaping arrays
- Universal functions (ufuncs)
- Linear algebra basics
"""

import numpy as np

print("=" * 60)
print("NUMPY OPERATIONS")
print("=" * 60)

# ========== ELEMENT-WISE OPERATIONS ==========
print("\n" + "=" * 60)
print("ELEMENT-WISE OPERATIONS")
print("=" * 60)

arr = np.array([1, 2, 3, 4, 5])
print(f"Original array: {arr}")

# Arithmetic with scalars
print("\nArithmetic with scalars:")
print(f"   arr + 10:  {arr + 10}")
print(f"   arr * 3:   {arr * 3}")
print(f"   arr ** 2:  {arr ** 2}")
print(f"   arr / 2:   {arr / 2}")
print(f"   arr // 2:  {arr // 2}  # Floor division")
print(f"   arr % 2:   {arr % 2}   # Modulus")

# Arithmetic between arrays
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([10, 20, 30, 40])
print(f"\nArray arithmetic:")
print(f"   arr1: {arr1}")
print(f"   arr2: {arr2}")
print(f"   arr1 + arr2: {arr1 + arr2}")
print(f"   arr1 * arr2: {arr1 * arr2}")
print(f"   arr2 - arr1: {arr2 - arr1}")
print(f"   arr2 / arr1: {arr2 / arr1}")

# ========== MATHEMATICAL FUNCTIONS ==========
print("\n" + "=" * 60)
print("MATHEMATICAL FUNCTIONS (ufuncs)")
print("=" * 60)

arr = np.array([1, 4, 9, 16, 25])
print(f"Array: {arr}")

print("\nCommon math functions:")
print(f"   np.sqrt(arr):  {np.sqrt(arr)}")
print(f"   np.exp(arr):   {np.exp([1, 2, 3])}  # e^x")
print(f"   np.log(arr):   {np.log([1, np.e, np.e**2]).round(2)}  # Natural log")
print(f"   np.log10(arr): {np.log10([1, 10, 100])}  # Log base 10")

# Trigonometric
angles = np.array([0, np.pi/6, np.pi/4, np.pi/3, np.pi/2])
print(f"\nTrigonometric functions:")
print(f"   Angles (radians): {angles.round(2)}")
print(f"   np.sin(angles):   {np.sin(angles).round(2)}")
print(f"   np.cos(angles):   {np.cos(angles).round(2)}")

# Rounding
arr = np.array([1.2, 2.5, 3.7, 4.1, 5.9])
print(f"\nRounding functions:")
print(f"   Array: {arr}")
print(f"   np.round(arr):   {np.round(arr)}")
print(f"   np.floor(arr):   {np.floor(arr)}")
print(f"   np.ceil(arr):    {np.ceil(arr)}")
print(f"   np.trunc(arr):   {np.trunc(arr)}")

# Absolute and sign
arr = np.array([-3, -2, -1, 0, 1, 2, 3])
print(f"\nAbsolute and sign:")
print(f"   Array: {arr}")
print(f"   np.abs(arr):  {np.abs(arr)}")
print(f"   np.sign(arr): {np.sign(arr)}")

# ========== AGGREGATION FUNCTIONS ==========
print("\n" + "=" * 60)
print("AGGREGATION FUNCTIONS")
print("=" * 60)

arr = np.array([15, 23, 8, 42, 31, 19, 7, 36])
print(f"Array: {arr}")

print("\nBasic aggregations:")
print(f"   np.sum(arr):    {np.sum(arr)}")
print(f"   np.mean(arr):   {np.mean(arr)}")
print(f"   np.std(arr):    {np.std(arr):.2f}")
print(f"   np.var(arr):    {np.var(arr):.2f}")
print(f"   np.min(arr):    {np.min(arr)}")
print(f"   np.max(arr):    {np.max(arr)}")
print(f"   np.median(arr): {np.median(arr)}")

print("\nPosition-based:")
print(f"   np.argmin(arr): {np.argmin(arr)}  # Index of min")
print(f"   np.argmax(arr): {np.argmax(arr)}  # Index of max")

print("\nCumulative:")
print(f"   np.cumsum(arr): {np.cumsum(arr)}")
print(f"   np.cumprod([1,2,3,4]): {np.cumprod([1, 2, 3, 4])}")

# Axis operations on 2D
arr_2d = np.array([[1, 2, 3], 
                   [4, 5, 6], 
                   [7, 8, 9]])
print(f"\n2D array:\n{arr_2d}")
print(f"   Sum all: {np.sum(arr_2d)}")
print(f"   Sum axis=0 (columns): {np.sum(arr_2d, axis=0)}")
print(f"   Sum axis=1 (rows): {np.sum(arr_2d, axis=1)}")
print(f"   Mean axis=0: {np.mean(arr_2d, axis=0)}")
print(f"   Mean axis=1: {np.mean(arr_2d, axis=1)}")

# ========== RESHAPING ARRAYS ==========
print("\n" + "=" * 60)
print("RESHAPING ARRAYS")
print("=" * 60)

arr = np.arange(12)
print(f"Original: {arr}")

# Reshape
reshaped = arr.reshape(3, 4)
print(f"\nreshaped to (3, 4):\n{reshaped}")

reshaped = arr.reshape(4, 3)
print(f"\nreshaped to (4, 3):\n{reshaped}")

reshaped = arr.reshape(2, 2, 3)
print(f"\nreshaped to (2, 2, 3):\n{reshaped}")

# Using -1 for auto-calculation
reshaped = arr.reshape(3, -1)  # -1 means "figure it out"
print(f"\nreshaped with -1 (3, -1) → (3, 4):\n{reshaped}")

# Flatten
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(f"\n2D array:\n{arr_2d}")
print(f"   flatten(): {arr_2d.flatten()}")
print(f"   ravel():   {arr_2d.ravel()}")

# Transpose
print(f"\nTranspose:")
print(f"   Original shape: {arr_2d.shape}")
print(f"   Transposed (arr.T):\n{arr_2d.T}")
print(f"   Transposed shape: {arr_2d.T.shape}")

# ========== BROADCASTING ==========
print("\n" + "=" * 60)
print("BROADCASTING")
print("=" * 60)

print("""
Broadcasting rules:
1. Arrays with different shapes can be operated together
2. Dimensions are compared right-to-left
3. Dimensions must match or one must be 1
""")

# Scalar broadcasting
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Array:\n{arr}")
print(f"\nScalar broadcast (arr + 10):\n{arr + 10}")

# 1D to 2D broadcasting
row_add = np.array([10, 20, 30])
print(f"\nRow to add: {row_add}")
print(f"Broadcast add (arr + row):\n{arr + row_add}")

col_add = np.array([[100], [200]])
print(f"\nColumn to add:\n{col_add}")
print(f"Broadcast add (arr + col):\n{arr + col_add}")

# ========== CONCATENATION & STACKING ==========
print("\n" + "=" * 60)
print("CONCATENATION & STACKING")
print("=" * 60)

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(f"Array a:\n{a}")
print(f"Array b:\n{b}")

# Concatenate
print(f"\nnp.concatenate([a, b], axis=0):\n{np.concatenate([a, b], axis=0)}")
print(f"\nnp.concatenate([a, b], axis=1):\n{np.concatenate([a, b], axis=1)}")

# vstack and hstack
print(f"\nnp.vstack([a, b]):\n{np.vstack([a, b])}")
print(f"\nnp.hstack([a, b]):\n{np.hstack([a, b])}")

# Stack (adds new dimension)
print(f"\nnp.stack([a, b]).shape: {np.stack([a, b]).shape}")

# ========== SPLITTING ARRAYS ==========
print("\n" + "=" * 60)
print("SPLITTING ARRAYS")
print("=" * 60)

arr = np.arange(12).reshape(4, 3)
print(f"Array:\n{arr}")

# Split into equal parts
parts = np.split(arr, 2)  # Split into 2 along axis 0
print(f"\nnp.split(arr, 2):")
for i, part in enumerate(parts):
    print(f"   Part {i}:\n{part}")

# hsplit and vsplit
arr = np.arange(12).reshape(3, 4)
print(f"\nArray for hsplit:\n{arr}")
left, right = np.hsplit(arr, 2)
print(f"   Left half:\n{left}")
print(f"   Right half:\n{right}")

# ========== COMPARISON OPERATIONS ==========
print("\n" + "=" * 60)
print("COMPARISON OPERATIONS")
print("=" * 60)

a = np.array([1, 2, 3, 4, 5])
b = np.array([1, 0, 3, 2, 5])
print(f"a: {a}")
print(f"b: {b}")

print(f"\nComparisons:")
print(f"   a == b: {a == b}")
print(f"   a > b:  {a > b}")
print(f"   a >= b: {a >= b}")

print(f"\nArray equality:")
print(f"   np.array_equal(a, b): {np.array_equal(a, b)}")
print(f"   np.allclose(a, a + 0.00001): {np.allclose(a, a + 0.00001)}")

# np.where
arr = np.array([1, 5, 2, 8, 3, 9])
print(f"\narr: {arr}")
print(f"np.where(arr > 4): {np.where(arr > 4)}")  # Indices
print(f"np.where(arr > 4, 'big', 'small'): {np.where(arr > 4, 'big', 'small')}")

# ========== SORTING ==========
print("\n" + "=" * 60)
print("SORTING")
print("=" * 60)

arr = np.array([3, 1, 4, 1, 5, 9, 2, 6])
print(f"Original: {arr}")
print(f"np.sort(arr): {np.sort(arr)}")
print(f"np.argsort(arr): {np.argsort(arr)}  # Indices that sort")

# 2D sorting
arr_2d = np.array([[3, 1, 4], [1, 5, 9], [2, 6, 5]])
print(f"\n2D array:\n{arr_2d}")
print(f"Sort axis=1 (each row):\n{np.sort(arr_2d, axis=1)}")
print(f"Sort axis=0 (each column):\n{np.sort(arr_2d, axis=0)}")

# ========== LINEAR ALGEBRA BASICS ==========
print("\n" + "=" * 60)
print("LINEAR ALGEBRA BASICS")
print("=" * 60)

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(f"Matrix A:\n{a}")
print(f"Matrix B:\n{b}")

# Matrix multiplication
print(f"\nMatrix multiplication:")
print(f"np.dot(a, b):\n{np.dot(a, b)}")
print(f"a @ b:\n{a @ b}")  # Same as np.dot

# Other operations
print(f"\nOther operations:")
print(f"   Determinant of A: {np.linalg.det(a):.2f}")
print(f"   Trace of A: {np.trace(a)}")
print(f"   Inverse of A:\n{np.linalg.inv(a)}")

# ========== PRACTICAL EXAMPLE ==========
print("\n" + "=" * 60)
print("PRACTICAL EXAMPLE: Sales Data Analysis")
print("=" * 60)

# Monthly sales data for 4 products over 6 months
np.random.seed(42)
sales = np.random.randint(100, 500, (4, 6))
products = ['Product A', 'Product B', 'Product C', 'Product D']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']

print("Sales data (rows=products, cols=months):")
print(sales)

print(f"\nAnalysis:")
print(f"   Total sales: {sales.sum()}")
print(f"   Sales per product: {sales.sum(axis=1)}")
print(f"   Sales per month: {sales.sum(axis=0)}")
print(f"   Best month index: {sales.sum(axis=0).argmax()} ({months[sales.sum(axis=0).argmax()]})")
print(f"   Best product index: {sales.sum(axis=1).argmax()} ({products[sales.sum(axis=1).argmax()]})")
print(f"   Average monthly sales per product: {sales.mean(axis=1).round(1)}")

# Normalize sales (0-1 scale)
normalized = (sales - sales.min()) / (sales.max() - sales.min())
print(f"\nNormalized sales (0-1 scale):\n{normalized.round(2)}")

print("\n" + "=" * 60)
print("✅ NumPy Operations - Complete!")
print("=" * 60)
