"""
EXERCISES: Scikit-learn Workflow
=================================
Complete all 5 exercises below
"""

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report

# Exercise 1: Load and Explore Dataset
# TODO: Load the wine dataset from sklearn
# Print: number of samples, features, classes, and feature names

print("Exercise 1: Load and Explore Dataset")
print("-" * 40)
from sklearn.datasets import load_wine

# Your code here:



# Exercise 2: Complete Pipeline
# TODO: Build a complete ML pipeline for the wine dataset:
# 1. Split data (80-20)
# 2. Scale features
# 3. Train LogisticRegression
# 4. Evaluate accuracy

print("\n\nExercise 2: Complete Pipeline")
print("-" * 40)
from sklearn.linear_model import LogisticRegression

# Your code here:



# Exercise 3: Compare Multiple Algorithms
# TODO: Compare these algorithms on the wine dataset:
# - LogisticRegression
# - KNeighborsClassifier
# - DecisionTreeClassifier
# Print accuracy for each

print("\n\nExercise 3: Compare Multiple Algorithms")
print("-" * 40)
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

# Your code here:



# Exercise 4: Make Predictions on New Data
# TODO: After training a model, create a "fake" new sample
# Scale it properly and predict its class
# Show the probabilities for each class

print("\n\nExercise 4: Make Predictions on New Data")
print("-" * 40)

# Your code here:



# Exercise 5: Confusion Matrix Analysis
# TODO: Train a model on the digits dataset (load_digits)
# Print the confusion matrix
# Identify which digits are most often confused

print("\n\nExercise 5: Confusion Matrix Analysis")
print("-" * 40)
from sklearn.datasets import load_digits
from sklearn.metrics import confusion_matrix

# Your code here:

