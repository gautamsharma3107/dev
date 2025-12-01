"""
DAY 28 ASSESSMENT TEST - Week 4 Comprehensive Review
=====================================================
Total: 100 points
Pass: 70+ points (70%)
Time: 60 minutes

This is your comprehensive Week 4 assessment covering:
- NumPy and Pandas
- Data Visualization
- Machine Learning with Scikit-learn
- Regression and Classification
- Model Evaluation

Good luck! 🚀
"""

import numpy as np
import pandas as pd

print("=" * 70)
print("DAY 28 ASSESSMENT - COMPREHENSIVE WEEK 4 REVIEW")
print("=" * 70)
print("Total Points: 100 | Passing Score: 70 (70%)")
print("Time: 60 minutes")
print("=" * 70)

# ============================================================
# SECTION A: NUMPY & PANDAS (20 points)
# ============================================================

print("\n" + "=" * 70)
print("SECTION A: NUMPY & PANDAS (20 points)")
print("=" * 70)

print("""
Q1. (2 points) What is the output of the following code?
    import numpy as np
    arr = np.array([1, 2, 3, 4, 5])
    print(arr[1:4])
    
    a) [1, 2, 3, 4]
    b) [2, 3, 4]
    c) [2, 3, 4, 5]
    d) [1, 2, 3]

Your answer: """)

print("""
Q2. (2 points) Which Pandas function is used to handle missing values?
    a) df.empty()
    b) df.fillna()
    c) df.null()
    d) df.missing()

Your answer: """)

print("""
Q3. (2 points) What does df.describe() return?
    a) Data types of each column
    b) First 5 rows of the DataFrame
    c) Statistical summary of numerical columns
    d) Shape of the DataFrame

Your answer: """)

print("""
Q4. (2 points) How do you select rows where column 'age' is greater than 30?
    a) df[df.age > 30]
    b) df.select(age > 30)
    c) df.filter(age > 30)
    d) df.where(age > 30)

Your answer: """)

print("""
Q5. (2 points) What is the difference between .loc and .iloc in Pandas?
    a) .loc uses labels, .iloc uses integer positions
    b) .loc uses integers, .iloc uses labels
    c) They are the same
    d) .loc is for rows, .iloc is for columns

Your answer: """)

print("""
Q6. (4 points - Coding) Create a NumPy array of 10 random integers between 1 and 100,
    then calculate and print the mean, median, and standard deviation.
""")

# Write your code here:
# arr = np.random.randint(...)




print("""
Q7. (6 points - Coding) Given the following DataFrame:
    data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
            'age': [25, 30, None, 45],
            'salary': [50000, 60000, 70000, None]}
    df = pd.DataFrame(data)
    
    a) Fill missing age with the mean age
    b) Fill missing salary with the median salary
    c) Print the cleaned DataFrame
""")

# Write your code here:




# ============================================================
# SECTION B: DATA VISUALIZATION (15 points)
# ============================================================

print("\n" + "=" * 70)
print("SECTION B: DATA VISUALIZATION (15 points)")
print("=" * 70)

print("""
Q8. (2 points) Which library is commonly used for creating statistical visualizations?
    a) NumPy
    b) Pandas
    c) Seaborn
    d) Scikit-learn

Your answer: """)

print("""
Q9. (2 points) What type of plot is best for showing the distribution of a single variable?
    a) Scatter plot
    b) Histogram
    c) Line plot
    d) Bar chart

Your answer: """)

print("""
Q10. (2 points) Which plot is best for detecting outliers?
    a) Pie chart
    b) Box plot
    c) Line chart
    d) Area chart

Your answer: """)

print("""
Q11. (3 points) What does a correlation heatmap show?
    a) The mean of each variable
    b) The relationship strength between variables
    c) The distribution of each variable
    d) The count of each category

Your answer: """)

print("""
Q12. (6 points - Coding) Write code to create a scatter plot showing the relationship
    between 'feature_x' and 'feature_y', with proper title, x-label, and y-label.
    Use matplotlib.
    
    Assume: feature_x = [1, 2, 3, 4, 5]
            feature_y = [2, 4, 5, 4, 5]
""")

# Write your code here:
# import matplotlib.pyplot as plt




# ============================================================
# SECTION C: MACHINE LEARNING CONCEPTS (25 points)
# ============================================================

print("\n" + "=" * 70)
print("SECTION C: MACHINE LEARNING CONCEPTS (25 points)")
print("=" * 70)

print("""
Q13. (2 points) What is the purpose of train-test split?
    a) To make the dataset smaller
    b) To evaluate model performance on unseen data
    c) To remove outliers
    d) To scale the features

Your answer: """)

print("""
Q14. (2 points) What is overfitting?
    a) Model performs well on training data but poorly on test data
    b) Model performs poorly on both training and test data
    c) Model is too simple
    d) Model takes too long to train

Your answer: """)

print("""
Q15. (2 points) Which algorithm is used for predicting continuous values?
    a) Logistic Regression
    b) Decision Tree Classifier
    c) Linear Regression
    d) K-Means Clustering

Your answer: """)

print("""
Q16. (2 points) What is the purpose of feature scaling?
    a) To remove missing values
    b) To ensure features are on similar scales
    c) To add new features
    d) To remove outliers

Your answer: """)

print("""
Q17. (2 points) Which metric is NOT used for regression problems?
    a) Mean Squared Error (MSE)
    b) R-squared (R²)
    c) Accuracy
    d) Mean Absolute Error (MAE)

Your answer: """)

print("""
Q18. (3 points) What is cross-validation and why is it useful?
    Write a brief explanation (2-3 sentences).

Your answer:
""")

print("""
Q19. (4 points) Explain the difference between supervised and unsupervised learning.
    Give one example algorithm for each.

Your answer:
""")

print("""
Q20. (8 points - Coding) Write code to:
    a) Split data X, y into train and test sets (80-20 split)
    b) Scale the features using StandardScaler
    c) Fit scaler on training data and transform both train and test
    
    Assume X and y are already defined.
""")

# Write your code here:
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler




# ============================================================
# SECTION D: MODEL IMPLEMENTATION (25 points)
# ============================================================

print("\n" + "=" * 70)
print("SECTION D: MODEL IMPLEMENTATION (25 points)")
print("=" * 70)

print("""
Q21. (2 points) What is the correct order for ML pipeline?
    a) Train → Split → Scale → Evaluate
    b) Split → Scale → Train → Evaluate
    c) Scale → Split → Train → Evaluate
    d) Train → Scale → Split → Evaluate

Your answer: """)

print("""
Q22. (2 points) Which Random Forest parameter controls the number of trees?
    a) max_depth
    b) n_estimators
    c) min_samples_split
    d) criterion

Your answer: """)

print("""
Q23. (2 points) What does R² = 0.85 mean?
    a) The model is 85% accurate
    b) The model explains 85% of the variance in the target
    c) The model has 85% error
    d) The model uses 85% of the features

Your answer: """)

print("""
Q24. (3 points) What is GridSearchCV used for?
    a) Creating visualizations
    b) Splitting data
    c) Finding the best hyperparameters
    d) Scaling features

Your answer: """)

print("""
Q25. (6 points - Coding) Write code to train a Random Forest Classifier
    on training data and make predictions on test data.
    Calculate and print the accuracy score.
    
    Assume X_train, X_test, y_train, y_test are already defined.
""")

# Write your code here:
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score




print("""
Q26. (10 points - Coding) Complete ML Pipeline:
    Write a complete pipeline that:
    a) Loads a dataset (you can create sample data)
    b) Splits into train/test
    c) Scales features
    d) Trains a Linear Regression model
    e) Makes predictions
    f) Calculates and prints R², RMSE, and MAE
    
    Show your complete code:
""")

# Write your complete ML pipeline here:




# ============================================================
# SECTION E: CODE QUALITY & BEST PRACTICES (15 points)
# ============================================================

print("\n" + "=" * 70)
print("SECTION E: CODE QUALITY & BEST PRACTICES (15 points)")
print("=" * 70)

print("""
Q27. (3 points) Why should you fit the scaler only on training data?
    a) To save memory
    b) To prevent data leakage
    c) To speed up training
    d) To handle missing values

Your answer: """)

print("""
Q28. (3 points) What is data leakage in machine learning?
    Write a brief explanation.

Your answer:
""")

print("""
Q29. (3 points) What should you do before deploying a model to production?
    Select all that apply:
    a) Save the model and scaler
    b) Document the model
    c) Test on new data
    d) All of the above

Your answer: """)

print("""
Q30. (6 points) Describe 3 best practices for building a production-ready
    machine learning model. Be specific.

Your answer:
1. 

2. 

3. 
""")

# ============================================================
# ANSWER KEY
# ============================================================

print("\n" + "=" * 70)
print("TEST COMPLETE!")
print("=" * 70)

print("""
When done, check your answers and calculate your score.
You need at least 70 points to pass!

Scoring:
- Section A: NumPy & Pandas (20 points)
- Section B: Data Visualization (15 points)
- Section C: ML Concepts (25 points)
- Section D: Model Implementation (25 points)
- Section E: Best Practices (15 points)
- Total: 100 points

Good luck! 🚀
""")

# ============================================================
# ANSWER KEY (Don't look until you're done!)
# ============================================================

"""
ANSWER KEY
==========

SECTION A:
Q1: b) [2, 3, 4]
Q2: b) df.fillna()
Q3: c) Statistical summary of numerical columns
Q4: a) df[df.age > 30]
Q5: a) .loc uses labels, .iloc uses integer positions

Q6: 
arr = np.random.randint(1, 101, 10)
print(f"Mean: {arr.mean()}")
print(f"Median: {np.median(arr)}")
print(f"Std: {arr.std()}")

Q7:
data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'age': [25, 30, None, 45],
        'salary': [50000, 60000, 70000, None]}
df = pd.DataFrame(data)
df['age'].fillna(df['age'].mean(), inplace=True)
df['salary'].fillna(df['salary'].median(), inplace=True)
print(df)

SECTION B:
Q8: c) Seaborn
Q9: b) Histogram
Q10: b) Box plot
Q11: b) The relationship strength between variables

Q12:
import matplotlib.pyplot as plt
feature_x = [1, 2, 3, 4, 5]
feature_y = [2, 4, 5, 4, 5]
plt.scatter(feature_x, feature_y)
plt.title('Feature X vs Feature Y')
plt.xlabel('Feature X')
plt.ylabel('Feature Y')
plt.show()

SECTION C:
Q13: b) To evaluate model performance on unseen data
Q14: a) Model performs well on training data but poorly on test data
Q15: c) Linear Regression
Q16: b) To ensure features are on similar scales
Q17: c) Accuracy

Q18: Cross-validation is a technique that splits data into multiple folds
and trains/tests the model on different combinations. It provides a more
robust estimate of model performance and helps detect overfitting.

Q19: Supervised learning uses labeled data to learn a mapping from inputs
to outputs (e.g., Linear Regression, Random Forest). Unsupervised learning
finds patterns in unlabeled data (e.g., K-Means, PCA).

Q20:
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

SECTION D:
Q21: b) Split → Scale → Train → Evaluate
Q22: b) n_estimators
Q23: b) The model explains 85% of the variance in the target
Q24: c) Finding the best hyperparameters

Q25:
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.4f}")

Q26:
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

# Create sample data
np.random.seed(42)
X = np.random.rand(100, 3) * 100
y = X[:, 0] * 2 + X[:, 1] * 3 + np.random.randn(100) * 10

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train model
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# Make predictions
y_pred = model.predict(X_test_scaled)

# Calculate metrics
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
mae = mean_absolute_error(y_test, y_pred)

print(f"R²: {r2:.4f}")
print(f"RMSE: {rmse:.4f}")
print(f"MAE: {mae:.4f}")

SECTION E:
Q27: b) To prevent data leakage
Q28: Data leakage occurs when information from outside the training data
is used to create the model, leading to overly optimistic performance
estimates that don't generalize to new data.
Q29: d) All of the above

Q30:
1. Version control your code and track experiments (use git, MLflow)
2. Create comprehensive tests and validation procedures
3. Document model assumptions, limitations, and expected performance
   (Alternative answers: Monitor model in production, handle edge cases,
   create a reproducible pipeline, etc.)
"""
