"""
DAY 24 ASSESSMENT TEST
=======================
Total: 14 points
Pass: 10+ points (70%)
Time: 15 minutes

Answer all questions. Good luck!
"""

print("=" * 60)
print("DAY 24 ASSESSMENT TEST - ML Fundamentals & Scikit-learn")
print("=" * 60)
print("Total Points: 14 | Passing Score: 10 (70%)")
print("=" * 60)

# ============================================================
# SECTION A: Multiple Choice Questions (6 points)
# 1 point each
# ============================================================

print("\n" + "=" * 60)
print("SECTION A: Multiple Choice (6 points)")
print("=" * 60)

print("""
Q1. Which type of Machine Learning uses labeled data?
a) Unsupervised Learning
b) Supervised Learning
c) Reinforcement Learning
d) Semi-supervised Learning

Your answer: """)

print("""
Q2. What is the main purpose of train-test split?
a) To make training faster
b) To reduce dataset size
c) To evaluate model on unseen data
d) To balance classes

Your answer: """)

print("""
Q3. Which of the following is a classification problem?
a) Predicting house prices
b) Forecasting temperature
c) Predicting if an email is spam
d) Estimating sales revenue

Your answer: """)

print("""
Q4. What does StandardScaler do to the data?
a) Scales values to [0, 1]
b) Makes mean=0 and std=1
c) Removes outliers
d) Converts to integers

Your answer: """)

print("""
Q5. When using train_test_split, what should you do with the scaler?
a) Fit on entire dataset, then split
b) Fit on test set, transform train set
c) Fit on train set, transform both sets
d) Fit and transform separately on each set

Your answer: """)

print("""
Q6. Which algorithm does NOT require feature scaling?
a) Logistic Regression
b) K-Nearest Neighbors
c) Decision Tree
d) Support Vector Machine

Your answer: """)

# ============================================================
# SECTION B: Short Coding Challenges (6 points)
# 2 points each
# ============================================================

print("\n" + "=" * 60)
print("SECTION B: Coding Challenges (6 points)")
print("=" * 60)

print("""
Q7. (2 points) Write code to load the iris dataset and print:
- Number of samples
- Number of features
- Target class names
""")

# Write your code here:
from sklearn.datasets import load_iris

# Your code:




print("""
Q8. (2 points) Write code to perform a proper train-test split:
- Use 80% for training, 20% for testing
- Set random_state=42
- Use stratification
- Print the sizes of train and test sets
""")

# Write your code here:
from sklearn.model_selection import train_test_split

# Your code:




print("""
Q9. (2 points) Write code to:
- Create a StandardScaler
- Fit it on X_train and transform X_train
- Transform X_test (without fitting!)
- Print the mean of X_train before and after scaling
""")

# Write your code here:
from sklearn.preprocessing import StandardScaler

# Your code:




# ============================================================
# SECTION C: Conceptual Question (2 points)
# ============================================================

print("\n" + "=" * 60)
print("SECTION C: Conceptual Question (2 points)")
print("=" * 60)

print("""
Q10. (2 points) Explain the difference between Classification and Regression.
Give one real-world example of each.

Your answer:
""")

# Write your explanation here as comments:
# Classification:
# 
# Example:
#
# Regression:
#
# Example:




# ============================================================
# ANSWER KEY (For self-checking)
# ============================================================

print("\n" + "=" * 60)
print("TEST COMPLETE!")
print("=" * 60)
print("""
When done, check your answers with the answer key below.
You need at least 10 points to pass!

Remember:
- Review topics you got wrong
- Practice more on weak areas
- Build the mini projects to solidify learning

Good luck! 🚀
""")

"""
ANSWER KEY (Don't look until you're done!)
============================================

Section A (MCQ):
Q1: b) Supervised Learning
Q2: c) To evaluate model on unseen data
Q3: c) Predicting if an email is spam
Q4: b) Makes mean=0 and std=1
Q5: c) Fit on train set, transform both sets
Q6: c) Decision Tree

Section B (Coding):
Q7:
from sklearn.datasets import load_iris
iris = load_iris()
print(f"Samples: {iris.data.shape[0]}")
print(f"Features: {iris.data.shape[1]}")
print(f"Classes: {iris.target_names}")

Q8:
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target,
    test_size=0.2,
    random_state=42,
    stratify=iris.target
)
print(f"Train size: {len(X_train)}")
print(f"Test size: {len(X_test)}")

Q9:
scaler = StandardScaler()
print(f"Before scaling mean: {X_train.mean(axis=0)}")
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
print(f"After scaling mean: {X_train_scaled.mean(axis=0)}")

Section C:
Q10:
Classification: Predicts discrete categories/classes
Example: Email spam detection (spam/not spam), disease diagnosis (positive/negative)

Regression: Predicts continuous numerical values
Example: House price prediction, temperature forecasting, sales forecasting
"""
