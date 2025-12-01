"""
EXERCISES: Feature Scaling
===========================
Complete all 5 exercises below
"""

import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler

# Exercise 1: StandardScaler Practice
# TODO: Create data with age (20-70) and income (20000-150000)
# Apply StandardScaler and verify mean=0, std=1

print("Exercise 1: StandardScaler Practice")
print("-" * 40)

# Your code here:



# Exercise 2: MinMaxScaler Practice
# TODO: Scale the same data to range [0, 1] using MinMaxScaler
# Verify min=0, max=1

print("\n\nExercise 2: MinMaxScaler Practice")
print("-" * 40)

# Your code here:



# Exercise 3: Proper Scaling Workflow
# TODO: Load iris dataset
# Split into train/test
# Apply proper scaling (fit on train, transform on both)
# Show that you're doing it correctly

print("\n\nExercise 3: Proper Scaling Workflow")
print("-" * 40)
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Your code here:



# Exercise 4: RobustScaler with Outliers
# TODO: Create data with outliers
# Compare StandardScaler vs RobustScaler results
# Which handles outliers better?

print("\n\nExercise 4: RobustScaler with Outliers")
print("-" * 40)

# Your code here:



# Exercise 5: Impact on Model Performance
# TODO: Train a KNeighborsClassifier on iris dataset
# Compare accuracy WITH scaling vs WITHOUT scaling
# Which performs better?

print("\n\nExercise 5: Impact on Model Performance")
print("-" * 40)
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Your code here:

