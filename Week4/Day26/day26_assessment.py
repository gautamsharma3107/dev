"""
DAY 26 ASSESSMENT TEST
======================
Total: 14 points
Pass: 10+ points (70%)
Time: 15 minutes

Answer all questions. Good luck!
"""

print("=" * 60)
print("DAY 26 ASSESSMENT TEST - Classification Models")
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
Q1. What is the main difference between logistic regression and 
    linear regression?
a) Logistic regression predicts continuous values
b) Logistic regression predicts probabilities/classes
c) Linear regression is faster
d) There is no difference

Your answer: """)

print("""
Q2. In a confusion matrix, what does a False Positive (FP) represent?
a) Correctly predicted positive
b) Correctly predicted negative
c) Predicted positive when actually negative
d) Predicted negative when actually positive

Your answer: """)

print("""
Q3. Which metric is best when False Negatives are costly 
    (e.g., disease detection)?
a) Precision
b) Recall
c) Accuracy
d) Specificity

Your answer: """)

print("""
Q4. What is the formula for F1 Score?
a) (Precision + Recall) / 2
b) Precision * Recall
c) 2 * (Precision * Recall) / (Precision + Recall)
d) TP / (TP + FP + FN)

Your answer: """)

print("""
Q5. What is the main advantage of Random Forest over a single 
    Decision Tree?
a) Faster training
b) Simpler model
c) Reduced overfitting
d) Uses less memory

Your answer: """)

print("""
Q6. Which parameter controls the complexity (depth) of a 
    Decision Tree?
a) n_estimators
b) max_depth
c) learning_rate
d) C

Your answer: """)

# ============================================================
# SECTION B: Short Coding Challenges (6 points)
# 2 points each
# ============================================================

print("\n" + "=" * 60)
print("SECTION B: Coding Challenges (6 points)")
print("=" * 60)

print("""
Q7. (2 points) Train a logistic regression model on the 
    breast cancer dataset and print the accuracy.
    Use train_test_split with test_size=0.2, random_state=42.
""")

# Write your code here:
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# Load data
data = load_breast_cancer()
X, y = data.data, data.target

# Your code here:




print("""
Q8. (2 points) Given these predictions, calculate precision 
    and recall manually (show your work):
    
    y_true = [1, 1, 1, 0, 0, 0, 1, 0]
    y_pred = [1, 1, 0, 0, 1, 0, 1, 0]
    
    Count: TP=?, FP=?, TN=?, FN=?
    Precision = ?
    Recall = ?
""")

# Write your calculation here:




print("""
Q9. (2 points) Create and visualize a confusion matrix using 
    sklearn for the following:
    
    y_true = [0, 0, 1, 1, 0, 1, 1, 0, 0, 1]
    y_pred = [0, 1, 1, 1, 0, 0, 1, 0, 1, 1]
    
    Print the confusion matrix array.
""")

# Write your code here:
from sklearn.metrics import confusion_matrix

y_true = [0, 0, 1, 1, 0, 1, 1, 0, 0, 1]
y_pred = [0, 1, 1, 1, 0, 0, 1, 0, 1, 1]

# Your code here:




# ============================================================
# SECTION C: Conceptual Question (2 points)
# ============================================================

print("\n" + "=" * 60)
print("SECTION C: Conceptual Question (2 points)")
print("=" * 60)

print("""
Q10. (2 points) Explain why accuracy alone is not a good metric 
     for imbalanced datasets. Give an example scenario.

Your answer:
""")

# Write your explanation here as comments:
#




print("\n" + "=" * 60)
print("TEST COMPLETE!")
print("=" * 60)
print("""
When done, check your answers with the answer key below.
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
Q1: b) Logistic regression predicts probabilities/classes
Q2: c) Predicted positive when actually negative
Q3: b) Recall (catches all actual positives)
Q4: c) 2 * (Precision * Recall) / (Precision + Recall)
Q5: c) Reduced overfitting
Q6: b) max_depth

Section B (Coding):

Q7:
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

data = load_breast_cancer()
X, y = data.data, data.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LogisticRegression(random_state=42, max_iter=1000)
model.fit(X_train_scaled, y_train)
y_pred = model.predict(X_test_scaled)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.4f}")  # ~0.9737

Q8:
y_true = [1, 1, 1, 0, 0, 0, 1, 0]
y_pred = [1, 1, 0, 0, 1, 0, 1, 0]

Compare position by position:
Pos 0: true=1, pred=1 → TP
Pos 1: true=1, pred=1 → TP
Pos 2: true=1, pred=0 → FN
Pos 3: true=0, pred=0 → TN
Pos 4: true=0, pred=1 → FP
Pos 5: true=0, pred=0 → TN
Pos 6: true=1, pred=1 → TP
Pos 7: true=0, pred=0 → TN

TP=3, FP=1, TN=3, FN=1

Precision = TP / (TP + FP) = 3 / (3 + 1) = 3/4 = 0.75
Recall = TP / (TP + FN) = 3 / (3 + 1) = 3/4 = 0.75

Q9:
from sklearn.metrics import confusion_matrix

y_true = [0, 0, 1, 1, 0, 1, 1, 0, 0, 1]
y_pred = [0, 1, 1, 1, 0, 0, 1, 0, 1, 1]

cm = confusion_matrix(y_true, y_pred)
print(cm)
# Output:
# [[3, 2],
#  [1, 4]]

Section C:
Q10:
Accuracy can be misleading for imbalanced datasets because a model
can achieve high accuracy by simply predicting the majority class.

Example: Fraud detection with 99% non-fraud, 1% fraud
- A model that predicts "not fraud" for everything gets 99% accuracy
- But it catches 0% of actual fraud (completely useless!)
- Better metrics: Precision, Recall, F1-Score
- These metrics focus on the minority class performance
"""
