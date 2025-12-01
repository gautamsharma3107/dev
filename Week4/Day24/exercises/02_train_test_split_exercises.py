"""
EXERCISES: Train-Test Split
============================
Complete all 5 exercises below
"""

import numpy as np
from sklearn.model_selection import train_test_split

# Exercise 1: Basic Split
# TODO: Load the iris dataset
# Split it with 70% training and 30% testing
# Print the number of samples in each set

print("Exercise 1: Basic Split")
print("-" * 40)
from sklearn.datasets import load_iris

# Your code here:



# Exercise 2: Stratified Split
# TODO: Create an imbalanced dataset (80% class 0, 20% class 1)
# Split with and without stratification
# Compare the class distribution in test sets

print("\n\nExercise 2: Stratified Split")
print("-" * 40)

# Your code here:



# Exercise 3: Three-way Split
# TODO: Split the iris dataset into:
# 60% training, 20% validation, 20% testing
# Print the sizes of all three sets

print("\n\nExercise 3: Three-way Split")
print("-" * 40)

# Your code here:



# Exercise 4: Random State Effect
# TODO: Split the same dataset multiple times with different random_state values
# Observe how the splits differ
# Then show that same random_state gives same split

print("\n\nExercise 4: Random State Effect")
print("-" * 40)

# Your code here:



# Exercise 5: Cross-Validation
# TODO: Use cross_val_score to perform 5-fold cross-validation
# on a LogisticRegression model with the iris dataset
# Print all 5 scores and the mean

print("\n\nExercise 5: Cross-Validation")
print("-" * 40)
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression

# Your code here:

