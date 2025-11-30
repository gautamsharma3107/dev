"""
EXERCISES: ML Fundamentals
===========================
Complete all 5 exercises below
"""

# Exercise 1: Identify ML Problem Types
# TODO: For each scenario, determine if it's Classification, Regression, or Clustering
# Print your answers

print("Exercise 1: Identify ML Problem Types")
print("-" * 40)

scenarios = [
    "1. Predicting house prices based on size and location",
    "2. Categorizing emails as spam or not spam",
    "3. Grouping customers by purchasing behavior",
    "4. Predicting if a patient has diabetes",
    "5. Forecasting stock prices for next month",
    "6. Organizing news articles by topic",
    "7. Predicting customer churn (will leave or stay)",
    "8. Estimating the age of a person from their photo",
]

for scenario in scenarios:
    print(scenario)
    # Your answer here (Classification, Regression, or Clustering):
    

print()

# Exercise 2: Create a Simple Dataset
# TODO: Create a numpy array with 10 samples and 3 features
# Features: study_hours, sleep_hours, attendance_percentage
# Target: exam_score (continuous) or passed (binary)
# Print the shapes of X and y

print("\n\nExercise 2: Create a Simple Dataset")
print("-" * 40)
import numpy as np

# Your code here:



# Exercise 3: Train-Test Split Practice
# TODO: Use sklearn to split your dataset from Exercise 2
# Use 80-20 split with random_state=42
# Print the shapes of all resulting arrays

print("\n\nExercise 3: Train-Test Split Practice")
print("-" * 40)
from sklearn.model_selection import train_test_split

# Your code here:



# Exercise 4: Feature Scaling Comparison
# TODO: Create data with different scales (like age vs salary)
# Apply both StandardScaler and MinMaxScaler
# Compare the results

print("\n\nExercise 4: Feature Scaling Comparison")
print("-" * 40)
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Your code here:



# Exercise 5: Supervised vs Unsupervised
# TODO: Explain in comments when you would use:
# 1. Supervised Learning
# 2. Unsupervised Learning
# Give one real-world example for each

print("\n\nExercise 5: Supervised vs Unsupervised")
print("-" * 40)

# Your explanation here:
# Supervised Learning:
# When to use:
# Example:

# Unsupervised Learning:
# When to use:
# Example:

print("Write your answers as comments in the code!")
