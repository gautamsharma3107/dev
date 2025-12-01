"""
Day 24 - Train-Test Split
==========================
Learn: Data splitting for model evaluation

Key Concepts:
- Why we need to split data
- Train set vs Test set
- Validation set for tuning
- Stratified splitting for imbalanced data
"""

import numpy as np

# ========== WHY SPLIT DATA? ==========
print("=" * 60)
print("WHY SPLIT DATA?")
print("=" * 60)

why_split = """
The Golden Rule of ML: Never test on training data!

Why?
- Training data teaches the model patterns
- Testing data evaluates how well it learned
- Using same data for both = cheating (overfitting)

Analogy:
  - Training: Studying with practice problems
  - Testing: Taking the actual exam
  - Using same problems for both? Not a real test!
"""
print(why_split)

# ========== OVERFITTING EXPLAINED ==========
print("\n" + "=" * 60)
print("OVERFITTING EXPLAINED")
print("=" * 60)

overfitting = """
Overfitting: Model memorizes training data instead of learning patterns

Signs of overfitting:
- Great performance on training data (99%!)
- Poor performance on new data (60%...)

Example:
  A student memorizes all practice exam answers
  But fails when questions are slightly different
  
Solution: Always evaluate on UNSEEN test data!
"""
print(overfitting)

# ========== TRAIN-TEST SPLIT ==========
print("\n" + "=" * 60)
print("TRAIN-TEST SPLIT")
print("=" * 60)

split_info = """
Typical Split Ratios:
- 80% Training, 20% Testing (most common)
- 70% Training, 30% Testing (smaller datasets)
- 90% Training, 10% Testing (large datasets)

Dataset: 1000 samples
├── Training Set: 800 samples (learn patterns)
└── Test Set: 200 samples (evaluate model)
"""
print(split_info)

# ========== PRACTICAL EXAMPLE: MANUAL SPLIT ==========
print("\n" + "=" * 60)
print("MANUAL SPLIT EXAMPLE")
print("=" * 60)

# Create sample data
np.random.seed(42)
X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], 
              [6, 7], [7, 8], [8, 9], [9, 10], [10, 11]])
y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

print("Original Data:")
print(f"X shape: {X.shape} (10 samples, 2 features)")
print(f"y shape: {y.shape} (10 labels)")
print(f"\nX:\n{X}")
print(f"y: {y}")

# Manual split (80-20)
split_index = int(len(X) * 0.8)
X_train_manual = X[:split_index]
X_test_manual = X[split_index:]
y_train_manual = y[:split_index]
y_test_manual = y[split_index:]

print(f"\n--- Manual Split (80-20) ---")
print(f"Training samples: {len(X_train_manual)}")
print(f"Testing samples: {len(X_test_manual)}")

# ========== SKLEARN TRAIN_TEST_SPLIT ==========
print("\n" + "=" * 60)
print("SKLEARN train_test_split")
print("=" * 60)

from sklearn.model_selection import train_test_split

# Basic split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=0.2,     # 20% for testing
    random_state=42    # For reproducibility
)

print("Using sklearn train_test_split:")
print(f"X_train shape: {X_train.shape}")
print(f"X_test shape: {X_test.shape}")
print(f"y_train: {y_train}")
print(f"y_test: {y_test}")

# ========== RANDOM_STATE EXPLAINED ==========
print("\n" + "=" * 60)
print("RANDOM_STATE PARAMETER")
print("=" * 60)

random_state_info = """
random_state ensures reproducibility:

- Data is shuffled before splitting
- Different random_state = different split
- Same random_state = same split every time

Why use it?
- Reproduce results for debugging
- Compare models fairly
- Share results with others

Common practice: Use 42 (it's arbitrary, any number works)
"""
print(random_state_info)

# Demonstrate random_state
print("Different random_state values:")
for rs in [1, 2, 42]:
    _, _, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=rs)
    print(f"  random_state={rs}: y_test = {y_te}")

# ========== STRATIFIED SPLITTING ==========
print("\n" + "=" * 60)
print("STRATIFIED SPLITTING")
print("=" * 60)

stratified_info = """
Stratified Split: Preserve class distribution

Why needed?
- Imbalanced datasets (e.g., 90% class A, 10% class B)
- Without stratification, test set might have no class B!
- Stratification ensures both classes are represented

Use stratify=y parameter in train_test_split
"""
print(stratified_info)

# Create imbalanced data
y_imbalanced = np.array([0, 0, 0, 0, 0, 0, 0, 0, 1, 1])  # 80% class 0

print("Imbalanced data distribution:")
print(f"Class 0: {np.sum(y_imbalanced == 0)} samples")
print(f"Class 1: {np.sum(y_imbalanced == 1)} samples")

# Without stratification
X_tr, X_te, y_tr, y_te = train_test_split(
    X, y_imbalanced, test_size=0.2, random_state=42
)
print(f"\nWithout stratification:")
print(f"  y_test: {y_te}")
print(f"  Class 0 in test: {np.sum(y_te == 0)}, Class 1 in test: {np.sum(y_te == 1)}")

# With stratification
X_tr, X_te, y_tr, y_te = train_test_split(
    X, y_imbalanced, test_size=0.2, random_state=42, stratify=y_imbalanced
)
print(f"\nWith stratification (stratify=y):")
print(f"  y_test: {y_te}")
print(f"  Class 0 in test: {np.sum(y_te == 0)}, Class 1 in test: {np.sum(y_te == 1)}")

# ========== VALIDATION SET ==========
print("\n" + "=" * 60)
print("TRAIN-VALIDATION-TEST SPLIT")
print("=" * 60)

validation_info = """
Three-way split for model tuning:

Dataset: 1000 samples
├── Training Set: 600 samples (learn patterns)
├── Validation Set: 200 samples (tune hyperparameters)
└── Test Set: 200 samples (final evaluation)

Why validation set?
- Test set should only be used ONCE at the end
- Validation set is used for tuning without "cheating"
- Prevents overfitting to the test set

Typical ratios: 60-20-20 or 70-15-15
"""
print(validation_info)

# Three-way split
print("\n--- Three-way Split Example ---")

# First split: separate test set
X_temp, X_test_final, y_temp, y_test_final = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Second split: separate validation from training
X_train_final, X_val, y_train_final, y_val = train_test_split(
    X_temp, y_temp, test_size=0.25, random_state=42  # 0.25 of 80% = 20%
)

print(f"Training samples: {len(X_train_final)}")
print(f"Validation samples: {len(X_val)}")
print(f"Test samples: {len(X_test_final)}")

# ========== CROSS-VALIDATION PREVIEW ==========
print("\n" + "=" * 60)
print("CROSS-VALIDATION PREVIEW")
print("=" * 60)

cv_info = """
Cross-validation: Use ALL data for training AND testing

K-Fold Cross-Validation (K=5):
┌─────────┬─────────┬─────────┬─────────┬─────────┐
│ Fold 1  │ Train   │ Train   │ Train   │ Train   │  → Test
│ Train   │ Fold 2  │ Train   │ Train   │ Train   │  → Test
│ Train   │ Train   │ Fold 3  │ Train   │ Train   │  → Test
│ Train   │ Train   │ Train   │ Fold 4  │ Train   │  → Test
│ Train   │ Train   │ Train   │ Train   │ Fold 5  │  → Test
└─────────┴─────────┴─────────┴─────────┴─────────┘

Average all 5 test scores for final evaluation!

Benefits:
- Uses all data for training and testing
- More reliable performance estimate
- Better for small datasets
"""
print(cv_info)

# Quick cross-validation example
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression

print("Cross-validation example:")
model = LogisticRegression()

# Create larger dataset for CV
np.random.seed(42)
X_cv = np.random.randn(100, 2)
y_cv = (X_cv[:, 0] + X_cv[:, 1] > 0).astype(int)

scores = cross_val_score(model, X_cv, y_cv, cv=5)
print(f"5-Fold CV scores: {scores}")
print(f"Mean accuracy: {scores.mean():.2f} (+/- {scores.std() * 2:.2f})")

# ========== BEST PRACTICES ==========
print("\n" + "=" * 60)
print("BEST PRACTICES")
print("=" * 60)

best_practices = """
1. Always shuffle before splitting (train_test_split does this)

2. Use stratification for classification problems

3. Set random_state for reproducibility

4. Common split ratios:
   - Large data (>100k): 90-10 or 95-5
   - Medium data (1k-100k): 80-20
   - Small data (<1k): Use cross-validation

5. Never look at test data during training/tuning

6. Use validation set for hyperparameter tuning

7. Report results on test set only once at the end
"""
print(best_practices)

# ========== COMPLETE WORKFLOW ==========
print("\n" + "=" * 60)
print("COMPLETE SPLITTING WORKFLOW")
print("=" * 60)

workflow_code = """
from sklearn.model_selection import train_test_split

# Load your data
# X = features, y = target

# Step 1: Split off test set (keep untouched until final evaluation)
X_temp, X_test, y_temp, y_test = train_test_split(
    X, y, 
    test_size=0.2, 
    random_state=42,
    stratify=y  # For classification
)

# Step 2: Split remaining into train and validation
X_train, X_val, y_train, y_val = train_test_split(
    X_temp, y_temp, 
    test_size=0.25,  # 25% of 80% = 20% of original
    random_state=42,
    stratify=y_temp
)

# Now you have:
# X_train, y_train - for training (60%)
# X_val, y_val - for tuning (20%)  
# X_test, y_test - for final evaluation (20%)
"""
print(workflow_code)

print("\n" + "=" * 60)
print("✅ Train-Test Split - Complete!")
print("=" * 60)
