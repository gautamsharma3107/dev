"""
Day 27 - Hyperparameter Tuning
===============================
Learn: GridSearchCV, RandomizedSearchCV, parameter optimization

Key Concepts:
- Hyperparameters are set before training (unlike parameters)
- Grid Search tests all combinations
- Random Search samples from distributions
- Cross-validation ensures reliable results
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import (
    GridSearchCV,
    RandomizedSearchCV,
    cross_val_score,
    train_test_split
)
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_breast_cancer
from scipy.stats import randint, uniform
import warnings
warnings.filterwarnings('ignore')

# ========== WHAT ARE HYPERPARAMETERS? ==========
print("=" * 60)
print("WHAT ARE HYPERPARAMETERS?")
print("=" * 60)

print("""
Hyperparameters vs Parameters:
- Parameters: Learned from data (e.g., weights in neural networks)
- Hyperparameters: Set before training (e.g., learning rate, n_estimators)

Examples of Hyperparameters:
- Random Forest: n_estimators, max_depth, min_samples_split
- SVM: C, kernel, gamma
- Neural Networks: learning_rate, batch_size, epochs

Why Tune Hyperparameters?
- Default values may not be optimal for your data
- Proper tuning can significantly improve performance
- Prevents overfitting/underfitting
""")

# ========== LOAD DATA ==========
print("\n" + "=" * 60)
print("LOAD BREAST CANCER DATASET")
print("=" * 60)

# Load data
data = load_breast_cancer()
X, y = data.data, data.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scale data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print(f"Training samples: {len(X_train)}")
print(f"Test samples: {len(X_test)}")
print(f"Features: {X.shape[1]}")
print(f"Classes: {np.unique(y)}")

# ========== GRID SEARCH BASICS ==========
print("\n" + "=" * 60)
print("GRID SEARCH CV - BASICS")
print("=" * 60)

print("""
Grid Search:
1. Define a grid of hyperparameter values
2. Try ALL combinations
3. Evaluate each with cross-validation
4. Select the best combination
""")

# Define parameter grid for Random Forest
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [3, 5, 7, None],
    'min_samples_split': [2, 5, 10]
}

print(f"Parameter Grid:")
for param, values in param_grid.items():
    print(f"  {param}: {values}")

# Calculate total combinations
total_combos = 1
for values in param_grid.values():
    total_combos *= len(values)
print(f"\nTotal combinations to try: {total_combos}")

# Create GridSearchCV
rf = RandomForestClassifier(random_state=42)
grid_search = GridSearchCV(
    estimator=rf,
    param_grid=param_grid,
    cv=5,                 # 5-fold cross-validation
    scoring='accuracy',   # Optimization metric
    n_jobs=-1,            # Use all CPU cores
    verbose=1,            # Show progress
    return_train_score=True
)

print("\nRunning Grid Search...")
grid_search.fit(X_train_scaled, y_train)

print(f"\nBest Parameters: {grid_search.best_params_}")
print(f"Best CV Score: {grid_search.best_score_:.4f}")

# Test on held-out data
best_model = grid_search.best_estimator_
test_score = best_model.score(X_test_scaled, y_test)
print(f"Test Score: {test_score:.4f}")

# ========== ANALYZING GRID SEARCH RESULTS ==========
print("\n" + "=" * 60)
print("ANALYZING GRID SEARCH RESULTS")
print("=" * 60)

# Get results as DataFrame
import pandas as pd
results_df = pd.DataFrame(grid_search.cv_results_)

print("\nTop 5 Parameter Combinations:")
print("-" * 60)
top_5 = results_df.nsmallest(5, 'rank_test_score')[
    ['params', 'mean_test_score', 'std_test_score', 'rank_test_score']
]
print(top_5.to_string())

# Visualize parameter effect
plt.figure(figsize=(12, 4))

# Effect of n_estimators
plt.subplot(1, 3, 1)
for depth in [3, 5, 7, None]:
    mask = results_df['param_max_depth'] == depth
    subset = results_df[mask].groupby('param_n_estimators')['mean_test_score'].mean()
    plt.plot(subset.index, subset.values, marker='o', label=f'depth={depth}')
plt.xlabel('n_estimators')
plt.ylabel('Mean CV Score')
plt.title('Effect of n_estimators')
plt.legend()
plt.grid(True, alpha=0.3)

# Effect of max_depth
plt.subplot(1, 3, 2)
depth_scores = results_df.groupby('param_max_depth')['mean_test_score'].mean()
plt.bar(range(len(depth_scores)), depth_scores.values)
plt.xticks(range(len(depth_scores)), ['3', '5', '7', 'None'])
plt.xlabel('max_depth')
plt.ylabel('Mean CV Score')
plt.title('Effect of max_depth')
plt.grid(True, alpha=0.3)

# Effect of min_samples_split
plt.subplot(1, 3, 3)
split_scores = results_df.groupby('param_min_samples_split')['mean_test_score'].mean()
plt.bar(range(len(split_scores)), split_scores.values)
plt.xticks(range(len(split_scores)), split_scores.index)
plt.xlabel('min_samples_split')
plt.ylabel('Mean CV Score')
plt.title('Effect of min_samples_split')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('01_grid_search_analysis.png', dpi=100, bbox_inches='tight')
plt.close()
print("\nPlot saved: 01_grid_search_analysis.png")

# ========== RANDOMIZED SEARCH ==========
print("\n" + "=" * 60)
print("RANDOMIZED SEARCH CV")
print("=" * 60)

print("""
Random Search:
- Samples random combinations from parameter distributions
- Faster than Grid Search for large search spaces
- Often finds good solutions quickly
- Recommended when many hyperparameters
""")

# Define parameter distributions
param_distributions = {
    'n_estimators': randint(50, 300),      # Random integers between 50-300
    'max_depth': randint(3, 20),           # Random integers between 3-20
    'min_samples_split': randint(2, 20),   # Random integers between 2-20
    'min_samples_leaf': randint(1, 10),    # Random integers between 1-10
    'max_features': uniform(0.1, 0.9)      # Random floats between 0.1-1.0
}

print("Parameter Distributions:")
for param, dist in param_distributions.items():
    print(f"  {param}: {dist}")

# Create RandomizedSearchCV
rf = RandomForestClassifier(random_state=42)
random_search = RandomizedSearchCV(
    estimator=rf,
    param_distributions=param_distributions,
    n_iter=50,            # Number of random combinations to try
    cv=5,
    scoring='accuracy',
    n_jobs=-1,
    random_state=42,
    verbose=1
)

print("\nRunning Random Search (50 iterations)...")
random_search.fit(X_train_scaled, y_train)

print(f"\nBest Parameters: {random_search.best_params_}")
print(f"Best CV Score: {random_search.best_score_:.4f}")

# Test score
best_model_random = random_search.best_estimator_
test_score_random = best_model_random.score(X_test_scaled, y_test)
print(f"Test Score: {test_score_random:.4f}")

# ========== COMPARING GRID VS RANDOM SEARCH ==========
print("\n" + "=" * 60)
print("GRID SEARCH VS RANDOM SEARCH")
print("=" * 60)

print(f"""
Comparison Summary:
------------------
                    Grid Search    Random Search
Best CV Score:      {grid_search.best_score_:.4f}         {random_search.best_score_:.4f}
Test Score:         {test_score:.4f}         {test_score_random:.4f}
Combinations:       {total_combos}             50 (sampled)

When to use Grid Search:
- Small parameter spaces
- When you need exhaustive search
- Compute resources are not limited

When to use Random Search:
- Large parameter spaces
- Limited compute time
- Many hyperparameters
- Good-enough solution is acceptable
""")

# ========== TUNING SVM ==========
print("\n" + "=" * 60)
print("PRACTICAL: TUNING SVM")
print("=" * 60)

# SVM parameter grid
svm_param_grid = {
    'C': [0.1, 1, 10, 100],
    'kernel': ['rbf', 'linear', 'poly'],
    'gamma': ['scale', 'auto', 0.1, 0.01]
}

print("SVM Parameter Grid:")
for param, values in svm_param_grid.items():
    print(f"  {param}: {values}")

# Grid search for SVM
svm = SVC(random_state=42)
svm_grid = GridSearchCV(
    svm,
    svm_param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1,
    verbose=1
)

print("\nRunning SVM Grid Search...")
svm_grid.fit(X_train_scaled, y_train)

print(f"\nBest Parameters: {svm_grid.best_params_}")
print(f"Best CV Score: {svm_grid.best_score_:.4f}")
print(f"Test Score: {svm_grid.best_estimator_.score(X_test_scaled, y_test):.4f}")

# Heatmap of C vs gamma for RBF kernel
results_svm = pd.DataFrame(svm_grid.cv_results_)
rbf_mask = results_svm['param_kernel'] == 'rbf'
rbf_results = results_svm[rbf_mask]

plt.figure(figsize=(10, 6))
pivot_table = rbf_results.pivot_table(
    values='mean_test_score',
    index='param_C',
    columns='param_gamma',
    aggfunc='mean'
)
plt.imshow(pivot_table, cmap='viridis', aspect='auto')
plt.colorbar(label='Mean CV Score')
plt.xticks(range(len(pivot_table.columns)), pivot_table.columns)
plt.yticks(range(len(pivot_table.index)), pivot_table.index)
plt.xlabel('gamma')
plt.ylabel('C')
plt.title('SVM Hyperparameter Heatmap (RBF kernel)')

# Add text annotations
for i in range(len(pivot_table.index)):
    for j in range(len(pivot_table.columns)):
        plt.text(j, i, f'{pivot_table.iloc[i, j]:.3f}',
                ha='center', va='center', color='white', fontsize=8)

plt.savefig('02_svm_heatmap.png', dpi=100, bbox_inches='tight')
plt.close()
print("\nPlot saved: 02_svm_heatmap.png")

# ========== MULTIPLE METRICS ==========
print("\n" + "=" * 60)
print("TUNING WITH MULTIPLE METRICS")
print("=" * 60)

# Can optimize for different metrics
from sklearn.model_selection import cross_val_score

metrics = ['accuracy', 'precision', 'recall', 'f1']
best_params_per_metric = {}

for metric in metrics:
    grid = GridSearchCV(
        RandomForestClassifier(random_state=42),
        {'n_estimators': [50, 100], 'max_depth': [3, 5, 7]},
        cv=5,
        scoring=metric,
        n_jobs=-1
    )
    grid.fit(X_train_scaled, y_train)
    best_params_per_metric[metric] = {
        'params': grid.best_params_,
        'score': grid.best_score_
    }
    print(f"{metric}: {grid.best_params_} -> {grid.best_score_:.4f}")

# ========== NESTED CROSS-VALIDATION ==========
print("\n" + "=" * 60)
print("NESTED CROSS-VALIDATION")
print("=" * 60)

print("""
Nested CV prevents overfitting to the validation set:
- Outer loop: Evaluates the model
- Inner loop: Tunes hyperparameters

This gives an unbiased estimate of model performance.
""")

# Outer CV for evaluation
outer_cv = 5

# Inner CV for hyperparameter tuning (Grid Search)
inner_cv = GridSearchCV(
    RandomForestClassifier(random_state=42),
    {'n_estimators': [50, 100], 'max_depth': [3, 5, 7]},
    cv=3,  # Inner folds
    scoring='accuracy',
    n_jobs=-1
)

# Nested CV scores
nested_scores = cross_val_score(inner_cv, X_train_scaled, y_train, cv=outer_cv)

print(f"Nested CV Scores: {nested_scores}")
print(f"Mean: {nested_scores.mean():.4f} (+/- {nested_scores.std():.4f})")

# Compare with non-nested (potentially optimistic)
simple_grid = GridSearchCV(
    RandomForestClassifier(random_state=42),
    {'n_estimators': [50, 100], 'max_depth': [3, 5, 7]},
    cv=5,
    scoring='accuracy',
    n_jobs=-1
)
simple_grid.fit(X_train_scaled, y_train)

print(f"\nNon-nested CV Score: {simple_grid.best_score_:.4f}")
print("(May be slightly optimistic due to data leakage)")

# ========== BEST PRACTICES ==========
print("\n" + "=" * 60)
print("HYPERPARAMETER TUNING BEST PRACTICES")
print("=" * 60)

print("""
1. Start with default parameters
   - Establish a baseline first
   
2. Understand your hyperparameters
   - Know what each one does
   - Know reasonable ranges
   
3. Use Random Search for exploration
   - Quickly identify promising regions
   
4. Use Grid Search for fine-tuning
   - Narrow down around best values
   
5. Use cross-validation
   - Get reliable performance estimates
   
6. Watch for overfitting
   - Large gap between train and test scores
   - Use regularization parameters
   
7. Consider computation time
   - More complex models need more tuning time
   
8. Use nested CV for final evaluation
   - Unbiased estimate of performance
   
9. Document your experiments
   - Track what you tried and results
   
10. Don't over-tune
    - Marginal gains may not be worth the effort
""")

print("\n" + "=" * 60)
print("✅ Hyperparameter Tuning - Complete!")
print("=" * 60)
