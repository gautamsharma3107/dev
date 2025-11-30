"""
Day 24 - Supervised vs Unsupervised Learning
=============================================
Learn: Types of ML, classification, regression, clustering

Key Concepts:
- Supervised Learning uses labeled data
- Unsupervised Learning finds patterns without labels
- Different algorithms for different problem types
"""

import numpy as np

# ========== SUPERVISED LEARNING ==========
print("=" * 60)
print("SUPERVISED LEARNING")
print("=" * 60)

supervised_intro = """
Supervised Learning: Learning with a "teacher"

- We have INPUT data (features) AND OUTPUT labels (target)
- Model learns the relationship between inputs and outputs
- Goal: Predict output for new, unseen inputs

Think of it like learning from a textbook with answer keys!
"""
print(supervised_intro)

# ========== CLASSIFICATION ==========
print("\n" + "=" * 60)
print("CLASSIFICATION (Supervised)")
print("=" * 60)

classification = """
Classification: Predict CATEGORIES (discrete values)

Examples:
- Email: Spam or Not Spam
- Image: Cat, Dog, or Bird
- Medical: Disease Present or Absent
- Loan: Approved or Rejected

Common Algorithms:
- Logistic Regression
- Decision Trees
- Random Forest
- Support Vector Machines (SVM)
- K-Nearest Neighbors (KNN)
- Neural Networks
"""
print(classification)

# Practical example: Classification
print("\n--- Practical Example: Classification ---")
print("Email Spam Detection")
print("-" * 40)

# Sample email features (simplified)
emails = [
    {"has_free": 1, "has_money": 1, "has_click": 1, "spam": 1},
    {"has_free": 0, "has_money": 0, "has_click": 0, "spam": 0},
    {"has_free": 1, "has_money": 1, "has_click": 0, "spam": 1},
    {"has_free": 0, "has_money": 0, "has_click": 1, "spam": 0},
]

print("\nTraining Data:")
print("Email | 'Free' | 'Money' | 'Click' | Is Spam?")
print("-" * 50)
for i, email in enumerate(emails):
    print(f"  {i+1}   |   {email['has_free']}    |    {email['has_money']}    |    {email['has_click']}    |    {email['spam']}")

print("\nPattern learned: Emails with 'Free' AND 'Money' are likely spam!")

# ========== REGRESSION ==========
print("\n" + "=" * 60)
print("REGRESSION (Supervised)")
print("=" * 60)

regression = """
Regression: Predict CONTINUOUS values (numbers)

Examples:
- House price based on size, location
- Temperature tomorrow
- Sales forecast for next month
- Stock price prediction

Common Algorithms:
- Linear Regression
- Polynomial Regression
- Ridge/Lasso Regression
- Decision Tree Regressor
- Random Forest Regressor
- Neural Networks
"""
print(regression)

# Practical example: Regression
print("\n--- Practical Example: Regression ---")
print("House Price Prediction")
print("-" * 40)

# Sample house data
houses = [
    {"size_sqft": 1000, "bedrooms": 2, "price": 200000},
    {"size_sqft": 1500, "bedrooms": 3, "price": 300000},
    {"size_sqft": 2000, "bedrooms": 3, "price": 400000},
    {"size_sqft": 2500, "bedrooms": 4, "price": 500000},
]

print("\nTraining Data:")
print("House | Size (sqft) | Bedrooms | Price ($)")
print("-" * 50)
for i, house in enumerate(houses):
    print(f"  {i+1}   |    {house['size_sqft']}     |    {house['bedrooms']}     | {house['price']:,}")

print("\nPattern learned: Price ≈ 200 × Size (approximately)")
print("New house with 1800 sqft? Predicted price ≈ $360,000")

# ========== UNSUPERVISED LEARNING ==========
print("\n" + "=" * 60)
print("UNSUPERVISED LEARNING")
print("=" * 60)

unsupervised_intro = """
Unsupervised Learning: Learning without a "teacher"

- We have INPUT data ONLY (no labels)
- Model finds hidden patterns and structures
- Goal: Discover groupings or relationships

Think of it like exploring data to find insights!
"""
print(unsupervised_intro)

# ========== CLUSTERING ==========
print("\n" + "=" * 60)
print("CLUSTERING (Unsupervised)")
print("=" * 60)

clustering = """
Clustering: Group similar data points together

Examples:
- Customer segmentation (high-value, medium, low)
- Image grouping (similar images together)
- Document clustering (similar topics)
- Anomaly detection (unusual patterns)

Common Algorithms:
- K-Means Clustering
- Hierarchical Clustering
- DBSCAN
- Gaussian Mixture Models
"""
print(clustering)

# Practical example: Clustering
print("\n--- Practical Example: Clustering ---")
print("Customer Segmentation")
print("-" * 40)

# Sample customer data (no labels!)
customers = [
    {"spending": 100, "frequency": 2},
    {"spending": 150, "frequency": 3},
    {"spending": 500, "frequency": 10},
    {"spending": 600, "frequency": 12},
    {"spending": 50, "frequency": 1},
]

print("\nCustomer Data (no labels):")
print("Customer | Spending ($) | Purchases/Month")
print("-" * 50)
for i, c in enumerate(customers):
    print(f"    {i+1}    |     {c['spending']:3}      |       {c['frequency']}")

print("\nClustering discovers groups:")
print("  - Cluster A (High Value): Customers 3, 4")
print("  - Cluster B (Medium Value): Customers 1, 2")
print("  - Cluster C (Low Value): Customer 5")

# ========== DIMENSIONALITY REDUCTION ==========
print("\n" + "=" * 60)
print("DIMENSIONALITY REDUCTION (Unsupervised)")
print("=" * 60)

dim_reduction = """
Dimensionality Reduction: Reduce number of features

Why reduce dimensions?
- Visualization (can't visualize 100 features)
- Speed up training
- Remove noise
- Handle multicollinearity

Common Algorithms:
- PCA (Principal Component Analysis)
- t-SNE
- UMAP
- LDA (Linear Discriminant Analysis)

Example:
  100 features → PCA → 10 key features
  Keeps most important information!
"""
print(dim_reduction)

# ========== COMPARISON TABLE ==========
print("\n" + "=" * 60)
print("SUPERVISED vs UNSUPERVISED COMPARISON")
print("=" * 60)

comparison = """
┌─────────────────┬────────────────────┬────────────────────┐
│ Aspect          │ Supervised         │ Unsupervised       │
├─────────────────┼────────────────────┼────────────────────┤
│ Labels          │ Required (y)       │ Not required       │
│ Goal            │ Predict output     │ Find patterns      │
│ Types           │ Classification,    │ Clustering,        │
│                 │ Regression         │ Dim. Reduction     │
│ Examples        │ Spam detection,    │ Customer segments, │
│                 │ Price prediction   │ Anomaly detection  │
│ Evaluation      │ Accuracy, MSE      │ Silhouette score   │
│ Data needed     │ Labeled (costly)   │ Unlabeled (cheap)  │
└─────────────────┴────────────────────┴────────────────────┘
"""
print(comparison)

# ========== CHOOSING THE RIGHT APPROACH ==========
print("\n" + "=" * 60)
print("CHOOSING THE RIGHT APPROACH")
print("=" * 60)

choosing = """
Decision Tree for Choosing ML Type:

1. Do you have labeled data?
   ├─ YES → Supervised Learning
   │   ├─ Is target categorical? → Classification
   │   └─ Is target numerical? → Regression
   │
   └─ NO → Unsupervised Learning
       ├─ Want to group similar data? → Clustering
       └─ Want to reduce features? → Dim. Reduction

Today's Focus: SUPERVISED LEARNING
- We'll use classification for this course
- Same workflow applies to regression
"""
print(choosing)

# ========== SEMI-SUPERVISED & REINFORCEMENT ==========
print("\n" + "=" * 60)
print("OTHER TYPES (Brief Overview)")
print("=" * 60)

other_types = """
SEMI-SUPERVISED LEARNING
- Mix of labeled and unlabeled data
- Useful when labeling is expensive
- Example: Label 100 images, have 10,000 unlabeled

REINFORCEMENT LEARNING
- Agent learns through interaction with environment
- Receives rewards/penalties for actions
- Examples: Game AI, Robotics, Trading bots

SELF-SUPERVISED LEARNING
- Model creates its own labels from data
- Popular in NLP (GPT) and Computer Vision
- Example: Predict next word in sentence
"""
print(other_types)

# ========== PRACTICAL CODE EXAMPLE ==========
print("\n" + "=" * 60)
print("CODE PREVIEW: Supervised vs Unsupervised")
print("=" * 60)

code_preview = """
# SUPERVISED (Classification)
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, y_train)  # Uses labels!
predictions = model.predict(X_test)

# SUPERVISED (Regression)
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)  # Uses labels!
predictions = model.predict(X_test)

# UNSUPERVISED (Clustering)
from sklearn.cluster import KMeans
model = KMeans(n_clusters=3)
model.fit(X)  # No labels needed!
clusters = model.predict(X_new)
"""
print(code_preview)

print("\n" + "=" * 60)
print("✅ Supervised vs Unsupervised Learning - Complete!")
print("=" * 60)
