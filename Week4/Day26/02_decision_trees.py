"""
Day 26 - Decision Trees
========================
Learn: Decision tree classification and visualization

Key Concepts:
- Trees split data based on feature thresholds
- Easy to interpret and visualize
- No feature scaling needed
- Can overfit easily - use pruning
"""

import numpy as np
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris, load_breast_cancer
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt

# ========== WHAT IS A DECISION TREE? ==========
print("=" * 60)
print("WHAT IS A DECISION TREE?")
print("=" * 60)

print("""
A Decision Tree makes decisions by asking a series of questions:

Example: Is this email spam?
    
    ┌─ Contains "FREE"? ─┐
    │                    │
   Yes                   No
    │                    │
  ┌─ Sender known? ─┐   Not Spam
  │                 │
 Yes               No
  │                 │
Not Spam          Spam

Key Terms:
- Root Node: First decision (top of tree)
- Internal Node: A decision/question
- Leaf Node: Final prediction (no more splits)
- Branch: Path from one node to another
- Depth: Number of levels in the tree

How it decides where to split:
- Gini Impurity: Measures how "impure" a node is
- Entropy: Information gain based measure
- Lower impurity = better split
""")

# ========== BASIC EXAMPLE ==========
print("\n" + "=" * 60)
print("BASIC EXAMPLE: Iris Classification")
print("=" * 60)

# Load dataset
iris = load_iris()
X, y = iris.data, iris.target
feature_names = iris.feature_names
target_names = iris.target_names

print(f"Dataset shape: {X.shape}")
print(f"Features: {feature_names}")
print(f"Classes: {target_names}")

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ========== TRAINING A DECISION TREE ==========
print("\n" + "=" * 60)
print("TRAINING A DECISION TREE")
print("=" * 60)

# Create and train model
tree = DecisionTreeClassifier(random_state=42)
tree.fit(X_train, y_train)

print("✅ Decision tree trained!")
print(f"Tree depth: {tree.get_depth()}")
print(f"Number of leaves: {tree.get_n_leaves()}")

# Make predictions
y_pred = tree.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.4f}")

# ========== UNDERSTANDING THE TREE ==========
print("\n" + "=" * 60)
print("UNDERSTANDING THE TREE")
print("=" * 60)

print("\nTree structure (text representation):")
print("-" * 40)


def print_tree_rules(tree, feature_names, class_names, indent=""):
    """Print simple tree rules."""
    tree_ = tree.tree_
    feature_name = [
        feature_names[i] if i != -2 else "undefined!"
        for i in tree_.feature
    ]

    def recurse(node, depth):
        if depth > 3:  # Limit depth for readability
            return
        indent = "  " * depth
        if tree_.feature[node] != -2:
            name = feature_name[node]
            threshold = tree_.threshold[node]
            print(f"{indent}if {name} <= {threshold:.2f}:")
            recurse(tree_.children_left[node], depth + 1)
            print(f"{indent}else ({name} > {threshold:.2f}):")
            recurse(tree_.children_right[node], depth + 1)
        else:
            class_idx = np.argmax(tree_.value[node])
            print(f"{indent}return {class_names[class_idx]}")

    recurse(0, 0)


print_tree_rules(tree, feature_names, target_names)

# ========== FEATURE IMPORTANCE ==========
print("\n" + "=" * 60)
print("FEATURE IMPORTANCE")
print("=" * 60)

print("""
Feature importance shows how valuable each feature is for predictions.
Higher importance = more useful for making decisions.
""")

importances = tree.feature_importances_
feature_importance = list(zip(feature_names, importances))
feature_importance.sort(key=lambda x: x[1], reverse=True)

print("Feature importances:")
for name, importance in feature_importance:
    bar = "█" * int(importance * 40)
    print(f"  {name:20s}: {importance:.4f} {bar}")

# ========== PREVENTING OVERFITTING ==========
print("\n" + "=" * 60)
print("PREVENTING OVERFITTING (Pruning)")
print("=" * 60)

print("""
Decision trees can easily overfit by creating very deep trees.
Use these parameters to control complexity:

1. max_depth: Maximum depth of the tree
2. min_samples_split: Minimum samples needed to split a node
3. min_samples_leaf: Minimum samples required in a leaf node
4. max_leaf_nodes: Maximum number of leaf nodes
""")

# Compare different max_depth values
print("\nEffect of max_depth on accuracy:")
print("-" * 50)

depths = [1, 2, 3, 5, 10, None]
for depth in depths:
    tree_d = DecisionTreeClassifier(max_depth=depth, random_state=42)
    tree_d.fit(X_train, y_train)
    train_score = tree_d.score(X_train, y_train)
    test_score = tree_d.score(X_test, y_test)
    depth_str = str(depth) if depth else "None"
    print(f"  max_depth={depth_str:4s}: Train={train_score:.3f}, Test={test_score:.3f}")

# ========== GINI VS ENTROPY ==========
print("\n" + "=" * 60)
print("GINI vs ENTROPY")
print("=" * 60)

print("""
Two methods to measure impurity and decide splits:

1. Gini Impurity (default):
   - Faster to compute
   - Gini = 1 - Σ(p_i)²
   - Range: 0 (pure) to 0.5 (for binary)

2. Entropy:
   - Information theory based
   - Entropy = -Σ(p_i * log2(p_i))
   - Range: 0 (pure) to 1 (for binary)

In practice, they often give similar results.
""")

# Compare criteria
for criterion in ['gini', 'entropy']:
    tree_c = DecisionTreeClassifier(criterion=criterion, random_state=42)
    tree_c.fit(X_train, y_train)
    score = tree_c.score(X_test, y_test)
    print(f"  {criterion}: Accuracy = {score:.4f}")

# ========== BINARY CLASSIFICATION EXAMPLE ==========
print("\n" + "=" * 60)
print("BINARY CLASSIFICATION: Breast Cancer")
print("=" * 60)

# Load breast cancer dataset
cancer = load_breast_cancer()
X_bc, y_bc = cancer.data, cancer.target

X_train_bc, X_test_bc, y_train_bc, y_test_bc = train_test_split(
    X_bc, y_bc, test_size=0.2, random_state=42
)

# Train with pruning
tree_pruned = DecisionTreeClassifier(
    max_depth=5,
    min_samples_split=10,
    min_samples_leaf=5,
    random_state=42
)
tree_pruned.fit(X_train_bc, y_train_bc)

y_pred_bc = tree_pruned.predict(X_test_bc)

print(f"Pruned tree depth: {tree_pruned.get_depth()}")
print(f"Number of leaves: {tree_pruned.get_n_leaves()}")
print(f"Accuracy: {accuracy_score(y_test_bc, y_pred_bc):.4f}")

print("\nClassification Report:")
print(classification_report(y_test_bc, y_pred_bc,
                            target_names=cancer.target_names))

# ========== VISUALIZING THE TREE ==========
print("\n" + "=" * 60)
print("VISUALIZING THE TREE")
print("=" * 60)

print("""
Decision trees can be visualized using matplotlib:

from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

plt.figure(figsize=(20, 10))
plot_tree(tree, 
          feature_names=feature_names,
          class_names=target_names,
          filled=True,
          rounded=True)
plt.show()
""")

# Create a simple tree for visualization
simple_tree = DecisionTreeClassifier(max_depth=3, random_state=42)
simple_tree.fit(X_train, y_train)

# Save visualization to file
plt.figure(figsize=(20, 10))
plot_tree(simple_tree,
          feature_names=feature_names,
          class_names=target_names,
          filled=True,
          rounded=True,
          fontsize=10)
plt.title("Decision Tree Visualization (max_depth=3)")
plt.tight_layout()
plt.savefig('/tmp/decision_tree_visualization.png', dpi=150, bbox_inches='tight')
plt.close()
print("✅ Tree visualization saved to /tmp/decision_tree_visualization.png")

# ========== ADVANTAGES AND DISADVANTAGES ==========
print("\n" + "=" * 60)
print("ADVANTAGES AND DISADVANTAGES")
print("=" * 60)

print("""
✅ ADVANTAGES:
- Easy to understand and interpret
- No feature scaling needed
- Can handle both numerical and categorical data
- Works well with non-linear relationships
- Feature importance built-in

❌ DISADVANTAGES:
- Can easily overfit
- Unstable (small changes = different tree)
- Can be biased with imbalanced data
- Not the best accuracy for complex problems
- Greedy algorithm (not globally optimal)

💡 WHEN TO USE:
- When interpretability is important
- As a baseline model
- When you need to explain predictions
- Part of ensemble methods (Random Forest)
""")

# ========== PRACTICAL EXAMPLE ==========
print("\n" + "=" * 60)
print("PRACTICAL EXAMPLE: Finding Best Parameters")
print("=" * 60)

from sklearn.model_selection import GridSearchCV

# Define parameter grid
param_grid = {
    'max_depth': [3, 5, 7, 10],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 5]
}

# Grid search
grid_search = GridSearchCV(
    DecisionTreeClassifier(random_state=42),
    param_grid,
    cv=5,
    scoring='accuracy'
)
grid_search.fit(X_train, y_train)

print(f"Best parameters: {grid_search.best_params_}")
print(f"Best cross-validation score: {grid_search.best_score_:.4f}")

# Test with best model
best_tree = grid_search.best_estimator_
test_score = best_tree.score(X_test, y_test)
print(f"Test accuracy with best model: {test_score:.4f}")

print("\n" + "=" * 60)
print("✅ Decision Trees - Complete!")
print("=" * 60)
