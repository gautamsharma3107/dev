"""
DAY 27 ASSESSMENT TEST
======================
Total: 14 points
Pass: 10+ points (70%)
Time: 15 minutes

Answer all questions. Good luck!
"""

print("=" * 60)
print("DAY 27 ASSESSMENT TEST - Unsupervised Learning & More")
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
Q1. What does K-Means clustering minimize?
a) Between-cluster variance
b) Within-cluster variance (inertia)
c) Number of clusters
d) Feature dimensions

Your answer: """)

print("""
Q2. What does PCA stand for?
a) Primary Component Analysis
b) Principal Component Analysis
c) Partial Component Analysis
d) Predictive Component Analysis

Your answer: """)

print("""
Q3. Why should you scale data before applying PCA?
a) PCA only works with scaled data
b) To make computation faster
c) Features with larger scales would dominate the principal components
d) To reduce the number of features

Your answer: """)

print("""
Q4. What is the purpose of cross-validation?
a) To train the model faster
b) To get a more reliable estimate of model performance
c) To increase model accuracy
d) To reduce overfitting

Your answer: """)

print("""
Q5. What does GridSearchCV do?
a) Randomly samples hyperparameter combinations
b) Tests all combinations in a parameter grid
c) Automatically selects the best model
d) Reduces the number of features

Your answer: """)

print("""
Q6. What is the Silhouette Score range?
a) 0 to 1
b) -1 to 1
c) 0 to 100
d) -100 to 100

Your answer: """)

# ============================================================
# SECTION B: Short Coding Challenges (6 points)
# 2 points each
# ============================================================

print("\n" + "=" * 60)
print("SECTION B: Coding Challenges (6 points)")
print("=" * 60)

print("""
Q7. (2 points) Write code to perform K-Means clustering with 3 clusters.
Given: X (feature matrix)
Use sklearn's KMeans and fit_predict to get cluster labels.
""")

# Write your code here:
# from sklearn.cluster import KMeans
# 
# Your code:



print("""
Q8. (2 points) Write code to apply PCA to reduce data to 2 dimensions.
Given: X_scaled (scaled feature matrix)
Use sklearn's PCA.
""")

# Write your code here:
# from sklearn.decomposition import PCA
# 
# Your code:



print("""
Q9. (2 points) Write code to perform 5-fold cross-validation and print mean score.
Given: model, X, y
Use sklearn's cross_val_score.
""")

# Write your code here:
# from sklearn.model_selection import cross_val_score
# 
# Your code:



# ============================================================
# SECTION C: Conceptual Question (2 points)
# ============================================================

print("\n" + "=" * 60)
print("SECTION C: Conceptual Question (2 points)")
print("=" * 60)

print("""
Q10. (2 points) Explain the difference between Grid Search and Random Search.
When would you use each?

Your answer:
""")

# Write your explanation here as comments:
# 



# ============================================================
# ANSWER KEY (For self-checking)
# ============================================================

print("\n" + "=" * 60)
print("TEST COMPLETE!")
print("=" * 60)
print("""
When done, check your answers with your professor.
You need at least 10 points to pass!

Remember:
- Review topics you got wrong
- Practice more on weak areas
- Ask questions if confused

Good luck! 🚀
""")

"""
ANSWER KEY (Don't look until you're done!)
============================================

Section A (MCQ):
Q1: b) Within-cluster variance (inertia)
Q2: b) Principal Component Analysis
Q3: c) Features with larger scales would dominate the principal components
Q4: b) To get a more reliable estimate of model performance
Q5: b) Tests all combinations in a parameter grid
Q6: b) -1 to 1

Section B (Coding):
Q7:
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3, random_state=42)
labels = kmeans.fit_predict(X)

Q8:
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

Q9:
from sklearn.model_selection import cross_val_score
scores = cross_val_score(model, X, y, cv=5)
print(f"Mean score: {scores.mean():.4f}")

Section C:
Q10: 
- Grid Search: Tests ALL combinations of hyperparameters in a predefined grid.
  Use when: Small parameter space, need exhaustive search, compute resources available.
  
- Random Search: Samples random combinations from parameter distributions.
  Use when: Large parameter space, limited time, many hyperparameters, 
  good-enough solution is acceptable.
  
Random Search is often more efficient because it explores a wider range
of values and can find good solutions faster than Grid Search.
"""
