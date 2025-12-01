"""
MINI PROJECT 2: Wine Quality Classifier
=========================================
Build a classifier to predict wine quality/type.

Objective:
Create an end-to-end ML pipeline for wine classification.

Requirements:
1. Load the wine dataset from sklearn
2. Perform exploratory data analysis
3. Split and scale data properly
4. Train multiple models
5. Use cross-validation for evaluation
6. Create a detailed comparison of models
7. Implement a prediction function
8. Generate a classification report

Bonus:
- Try different scaling methods
- Tune hyperparameters manually
- Create visualizations (if matplotlib available)
"""

# Your code here
print("=" * 60)
print("WINE QUALITY CLASSIFIER")
print("=" * 60)

import numpy as np
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# TODO: Step 1 - Load and explore wine dataset
print("\n--- Step 1: Load and Explore Data ---")


# TODO: Step 2 - Data exploration
print("\n--- Step 2: Data Exploration ---")


# TODO: Step 3 - Split data
print("\n--- Step 3: Split Data ---")


# TODO: Step 4 - Scale features
print("\n--- Step 4: Scale Features ---")


# TODO: Step 5 - Train multiple models
print("\n--- Step 5: Train Models ---")


# TODO: Step 6 - Evaluate with cross-validation
print("\n--- Step 6: Cross-Validation ---")


# TODO: Step 7 - Compare models
print("\n--- Step 7: Model Comparison ---")


# TODO: Step 8 - Create prediction function
print("\n--- Step 8: Prediction Function ---")


# TODO: Step 9 - Generate final report
print("\n--- Step 9: Final Report ---")

