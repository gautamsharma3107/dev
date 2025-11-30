"""
Day 24 - Feature Scaling
=========================
Learn: StandardScaler, MinMaxScaler, when to scale

Key Concepts:
- Why feature scaling is important
- StandardScaler (Z-score normalization)
- MinMaxScaler (Min-Max normalization)
- When to use which scaler
- Common pitfalls to avoid
"""

import numpy as np

# ========== WHY FEATURE SCALING? ==========
print("=" * 60)
print("WHY FEATURE SCALING?")
print("=" * 60)

why_scaling = """
Feature Scaling: Bringing all features to similar ranges

Why is it needed?

Example WITHOUT scaling:
  Feature 1 (Age): 20-80 (small range)
  Feature 2 (Salary): 30,000-200,000 (large range)

Problem: Salary dominates because of larger values!
- Distance calculations are skewed
- Gradient descent converges slowly
- Some algorithms won't work properly

Solution: Scale features to similar ranges
"""
print(why_scaling)

# ========== PRACTICAL EXAMPLE ==========
print("\n" + "=" * 60)
print("PRACTICAL EXAMPLE: Unscaled Data")
print("=" * 60)

# Create sample data with different scales
np.random.seed(42)
ages = np.random.randint(20, 70, 5).reshape(-1, 1)        # 20-70
salaries = np.random.randint(30000, 200000, 5).reshape(-1, 1)  # 30k-200k
experience = np.random.randint(0, 30, 5).reshape(-1, 1)   # 0-30

X_unscaled = np.hstack([ages, salaries, experience])

print("Original Data (different scales):")
print("-" * 50)
print("Person | Age | Salary ($) | Experience (years)")
print("-" * 50)
for i, row in enumerate(X_unscaled):
    print(f"   {i+1}   | {row[0]:3} |  {row[1]:,}  |        {row[2]}")

print("\nProblem: Salary values (30k-200k) dominate over Age (20-70)!")
print("Distance calculations would be mostly influenced by Salary.")

# ========== STANDARDSCALER ==========
print("\n" + "=" * 60)
print("STANDARDSCALER (Z-Score Normalization)")
print("=" * 60)

standard_info = """
StandardScaler transforms data to have:
- Mean = 0
- Standard Deviation = 1

Formula: z = (x - mean) / std

When to use:
- Most ML algorithms (default choice)
- When data is normally distributed
- For algorithms using gradient descent
- SVM, Logistic Regression, Neural Networks
"""
print(standard_info)

from sklearn.preprocessing import StandardScaler

# Apply StandardScaler
scaler_standard = StandardScaler()
X_standard = scaler_standard.fit_transform(X_unscaled)

print("\nAfter StandardScaler:")
print("-" * 50)
print("Person |   Age   |  Salary  | Experience")
print("-" * 50)
for i, row in enumerate(X_standard):
    print(f"   {i+1}   | {row[0]:7.3f} | {row[1]:8.3f} | {row[2]:7.3f}")

print("\nStatistics after scaling:")
print(f"Mean of each column: {X_standard.mean(axis=0).round(10)}")
print(f"Std of each column: {X_standard.std(axis=0).round(3)}")

# ========== MINMAXSCALER ==========
print("\n" + "=" * 60)
print("MINMAXSCALER (Min-Max Normalization)")
print("=" * 60)

minmax_info = """
MinMaxScaler transforms data to range [0, 1] (default):

Formula: x_scaled = (x - min) / (max - min)

When to use:
- When you need bounded values [0, 1]
- Image data (pixels are 0-255)
- Neural Networks (especially for output layer)
- When data is NOT normally distributed
"""
print(minmax_info)

from sklearn.preprocessing import MinMaxScaler

# Apply MinMaxScaler
scaler_minmax = MinMaxScaler()
X_minmax = scaler_minmax.fit_transform(X_unscaled)

print("\nAfter MinMaxScaler [0, 1]:")
print("-" * 50)
print("Person |  Age  | Salary | Experience")
print("-" * 50)
for i, row in enumerate(X_minmax):
    print(f"   {i+1}   | {row[0]:.3f} |  {row[1]:.3f} |   {row[2]:.3f}")

print("\nMin and Max after scaling:")
print(f"Min of each column: {X_minmax.min(axis=0)}")
print(f"Max of each column: {X_minmax.max(axis=0)}")

# ========== COMPARISON ==========
print("\n" + "=" * 60)
print("STANDARDSCALER vs MINMAXSCALER")
print("=" * 60)

comparison = """
┌──────────────────┬─────────────────────┬─────────────────────┐
│ Aspect           │ StandardScaler      │ MinMaxScaler        │
├──────────────────┼─────────────────────┼─────────────────────┤
│ Output range     │ No bounds           │ [0, 1] default      │
│ Mean             │ 0                   │ Not fixed           │
│ Handles outliers │ Better              │ Sensitive           │
│ Preserves shape  │ Yes                 │ Yes                 │
│ Best for         │ Most ML algorithms  │ Neural Networks,    │
│                  │                     │ Image data          │
└──────────────────┴─────────────────────┴─────────────────────┘
"""
print(comparison)

# ========== FIT vs TRANSFORM ==========
print("\n" + "=" * 60)
print("CRITICAL: FIT vs TRANSFORM")
print("=" * 60)

fit_transform = """
IMPORTANT: Only fit on TRAINING data!

Correct workflow:
1. scaler.fit_transform(X_train)  # Fit AND transform training
2. scaler.transform(X_test)       # ONLY transform test (no fit!)

Why?
- fit() learns parameters (mean, std, min, max) from data
- If we fit on test data, we "leak" information
- Model could learn from test data indirectly

WRONG ❌: scaler.fit_transform(X_test)  # Never do this!
RIGHT ✅: scaler.transform(X_test)       # Only transform!
"""
print(fit_transform)

# Demonstrate proper workflow
print("\n--- Proper Scaling Workflow ---")

from sklearn.model_selection import train_test_split

# Create larger dataset
np.random.seed(42)
X_demo = np.random.randn(100, 3) * [10, 1000, 50] + [30, 50000, 15]
y_demo = np.random.randint(0, 2, 100)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X_demo, y_demo, test_size=0.2, random_state=42
)

print(f"Training samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")

# Proper scaling
scaler = StandardScaler()

# Step 1: Fit and transform on training data
X_train_scaled = scaler.fit_transform(X_train)
print(f"\nTraining data - Mean before: {X_train.mean(axis=0).round(2)}")
print(f"Training data - Mean after: {X_train_scaled.mean(axis=0).round(10)}")

# Step 2: Only transform on test data (using fitted scaler)
X_test_scaled = scaler.transform(X_test)
print(f"\nTest data - transformed using training parameters")
print(f"Test data - Mean after: {X_test_scaled.mean(axis=0).round(3)}")
print("(Test mean might not be exactly 0, and that's okay!)")

# ========== WHEN NOT TO SCALE ==========
print("\n" + "=" * 60)
print("WHEN NOT TO SCALE?")
print("=" * 60)

when_not = """
Scaling is NOT needed for:

1. Tree-based algorithms
   - Decision Trees
   - Random Forest
   - Gradient Boosting (XGBoost, LightGBM)
   - Trees split on thresholds, not distances

2. Naive Bayes
   - Works with probabilities

3. When features are already on similar scales

4. When interpretability matters
   - Scaled coefficients are harder to interpret

Scaling IS important for:
- Linear Regression (with regularization)
- Logistic Regression
- SVM
- K-Nearest Neighbors (KNN)
- Neural Networks
- K-Means Clustering
- PCA
"""
print(when_not)

# ========== OTHER SCALERS ==========
print("\n" + "=" * 60)
print("OTHER USEFUL SCALERS")
print("=" * 60)

other_scalers = """
1. RobustScaler
   - Uses median and IQR instead of mean and std
   - Better for data with outliers
   
   from sklearn.preprocessing import RobustScaler

2. MaxAbsScaler
   - Scales by maximum absolute value
   - Preserves sparsity (zeros stay zeros)
   - Good for sparse data
   
   from sklearn.preprocessing import MaxAbsScaler

3. Normalizer
   - Scales each SAMPLE (row) to unit norm
   - Different from other scalers (column-based)
   
   from sklearn.preprocessing import Normalizer
"""
print(other_scalers)

# Quick demo of RobustScaler
from sklearn.preprocessing import RobustScaler

print("\n--- RobustScaler Demo (handles outliers) ---")

# Data with outlier
X_outlier = np.array([[1], [2], [3], [4], [5], [1000]])  # 1000 is outlier
print(f"Data with outlier: {X_outlier.flatten()}")

# Compare scalers
standard_result = StandardScaler().fit_transform(X_outlier)
robust_result = RobustScaler().fit_transform(X_outlier)

print(f"StandardScaler result: {standard_result.flatten().round(2)}")
print(f"RobustScaler result: {robust_result.flatten().round(2)}")
print("\nRobustScaler is less affected by the outlier (1000)!")

# ========== COMPLETE WORKFLOW ==========
print("\n" + "=" * 60)
print("COMPLETE SCALING WORKFLOW")
print("=" * 60)

workflow_code = """
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# 1. Split data FIRST
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 2. Create scaler
scaler = StandardScaler()

# 3. Fit on training data and transform
X_train_scaled = scaler.fit_transform(X_train)

# 4. Transform test data (no fit!)
X_test_scaled = scaler.transform(X_test)

# 5. Train model on scaled training data
model.fit(X_train_scaled, y_train)

# 6. Predict on scaled test data
predictions = model.predict(X_test_scaled)

# For new data in production:
# X_new_scaled = scaler.transform(X_new)  # Use same scaler!
"""
print(workflow_code)

# ========== COMMON MISTAKES ==========
print("\n" + "=" * 60)
print("COMMON MISTAKES TO AVOID")
print("=" * 60)

mistakes = """
❌ MISTAKE 1: Fitting scaler on entire dataset before splitting
   → Leaks test information into training

❌ MISTAKE 2: Fitting scaler on test data
   → scaler.fit_transform(X_test) is WRONG!
   
❌ MISTAKE 3: Using different scalers for train and test
   → Must use the SAME fitted scaler

❌ MISTAKE 4: Not saving the scaler for production
   → Need to transform new data the same way

❌ MISTAKE 5: Scaling target variable (usually)
   → For regression, sometimes needed; for classification, never

✅ CORRECT: Split → Fit on train → Transform both → Train → Predict
"""
print(mistakes)

print("\n" + "=" * 60)
print("✅ Feature Scaling - Complete!")
print("=" * 60)
