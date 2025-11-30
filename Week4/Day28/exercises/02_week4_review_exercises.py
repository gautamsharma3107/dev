"""
WEEK 4 REVIEW EXERCISES - Day 28
=================================
Practice all Week 4 concepts: NumPy, Pandas, Visualization, ML.
"""

import numpy as np
import pandas as pd

print("=" * 60)
print("WEEK 4 REVIEW EXERCISES")
print("=" * 60)

# ============================================================
# PART A: NUMPY EXERCISES
# ============================================================

print("\n" + "=" * 60)
print("PART A: NUMPY EXERCISES")
print("=" * 60)

print("""
A1. Create a 5x5 matrix with values from 1 to 25, then:
    - Calculate the sum of each row
    - Calculate the mean of each column
    - Find the maximum value in the diagonal
""")

# YOUR CODE HERE:




print("""
A2. Create two arrays of 10 random numbers each.
    - Calculate their dot product
    - Calculate element-wise multiplication
    - Stack them vertically and horizontally
""")

# YOUR CODE HERE:




print("""
A3. Create a 1D array of 100 random numbers.
    - Reshape to 10x10
    - Replace all values > 0.5 with 1 and <= 0.5 with 0
    - Count how many 1s and 0s
""")

# YOUR CODE HERE:




# ============================================================
# PART B: PANDAS EXERCISES
# ============================================================

print("\n" + "=" * 60)
print("PART B: PANDAS EXERCISES")
print("=" * 60)

print("""
B1. Create a DataFrame with columns: 'name', 'department', 'salary', 'years'.
    - Add 10 employees
    - Calculate average salary by department
    - Find employee with highest salary
    - Add a 'bonus' column (10% of salary for years > 5, else 5%)
""")

# YOUR CODE HERE:




print("""
B2. Create a sales DataFrame with columns: 'date', 'product', 'quantity', 'price'.
    - Add 20 sales records over 5 different products
    - Calculate total revenue per product
    - Find the best-selling product by quantity
    - Calculate daily sales total
""")

# YOUR CODE HERE:




print("""
B3. Create two DataFrames and practice merging:
    - df1: customer_id, customer_name
    - df2: customer_id, order_id, amount
    - Perform inner join, left join, right join
    - Calculate total order amount per customer
""")

# YOUR CODE HERE:




# ============================================================
# PART C: VISUALIZATION EXERCISES
# ============================================================

print("\n" + "=" * 60)
print("PART C: VISUALIZATION EXERCISES")
print("=" * 60)

print("""
C1. Create 4 different visualizations for a dataset:
    - Histogram of a numerical variable
    - Scatter plot of two variables
    - Box plot by category
    - Bar chart of averages
    
    Save all plots to files.
""")

# YOUR CODE HERE:
# import matplotlib.pyplot as plt
# import seaborn as sns




print("""
C2. Create a dashboard-style figure with 4 subplots:
    - Top-left: Line plot
    - Top-right: Bar chart
    - Bottom-left: Scatter plot
    - Bottom-right: Pie chart
    
    Use proper titles, labels, and legends.
""")

# YOUR CODE HERE:




print("""
C3. Create a correlation heatmap:
    - Use at least 5 numerical variables
    - Annotate with correlation values
    - Use an appropriate color scheme
    - Add a title
""")

# YOUR CODE HERE:




# ============================================================
# PART D: ML EXERCISES
# ============================================================

print("\n" + "=" * 60)
print("PART D: MACHINE LEARNING EXERCISES")
print("=" * 60)

print("""
D1. Regression Problem:
    - Create a dataset for house price prediction
    - Include at least 5 features
    - Train Linear Regression, Ridge, and Random Forest
    - Compare using R², RMSE, MAE
    - Use cross-validation
""")

# YOUR CODE HERE:




print("""
D2. Classification Problem:
    - Create a binary classification dataset
    - Train Logistic Regression, Decision Tree, Random Forest
    - Calculate accuracy, precision, recall, F1
    - Create confusion matrix
""")

# YOUR CODE HERE:




print("""
D3. Clustering Problem:
    - Create a dataset with natural clusters
    - Apply K-Means with different k values
    - Use elbow method to find optimal k
    - Visualize the clusters
""")

# YOUR CODE HERE:




print("""
D4. Complete Pipeline:
    - Load/create a dataset
    - Clean and preprocess
    - Engineer features
    - Train multiple models
    - Evaluate and compare
    - Save best model
""")

# YOUR CODE HERE:




# ============================================================
# PART E: CODING CHALLENGES
# ============================================================

print("\n" + "=" * 60)
print("PART E: CODING CHALLENGES")
print("=" * 60)

print("""
E1. Write a function that:
    - Takes a DataFrame
    - Automatically identifies numerical and categorical columns
    - Fills numerical NaN with median
    - Fills categorical NaN with mode
    - Returns cleaned DataFrame
""")

# YOUR CODE HERE:
# def auto_clean(df):
#     pass




print("""
E2. Write a function that:
    - Takes features X and target y
    - Trains 5 different models
    - Uses cross-validation
    - Returns a DataFrame with model names and scores
""")

# YOUR CODE HERE:
# def compare_models(X, y):
#     pass




print("""
E3. Write a function that:
    - Takes a trained model and test data
    - Returns a dictionary with all evaluation metrics
    - Includes visualization of residuals
""")

# YOUR CODE HERE:
# def evaluate_model(model, X_test, y_test):
#     pass




# ============================================================
# SOLUTIONS HINTS
# ============================================================

print("\n" + "=" * 60)
print("SOLUTIONS HINTS")
print("=" * 60)

print("""
Hints for difficult exercises:

A1: Use arr.sum(axis=1) for row sums, arr.mean(axis=0) for column means
    np.diag() extracts diagonal elements

B1: Use groupby('department')['salary'].mean() for average by department

C1: Use fig, axes = plt.subplots(2, 2) for multiple plots

D1: Use cross_val_score(model, X, y, cv=5, scoring='r2')

E1: Use df.select_dtypes(include=[np.number]) for numerical columns

Remember:
- Always set random_state for reproducibility
- Scale features before certain algorithms
- Split data before fitting scaler
- Use cross-validation for robust evaluation
""")

print("\n" + "=" * 60)
print("REVIEW EXERCISES COMPLETE!")
print("=" * 60)
