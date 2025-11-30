"""
MINI PROJECT 3: Breast Cancer Diagnosis
=========================================
Build a classifier for breast cancer diagnosis (benign vs malignant).

Objective:
Create a binary classification model for medical diagnosis.

Requirements:
1. Load the breast cancer dataset from sklearn
2. Understand the medical context (binary classification)
3. Handle the imbalanced nature of data appropriately
4. Train and evaluate multiple models
5. Focus on recall (catching all positive cases is crucial)
6. Create confusion matrix analysis
7. Implement risk assessment function

Important Note:
In medical diagnosis, missing a cancer case (False Negative) is worse
than a false alarm (False Positive). Optimize for recall!

Bonus:
- Adjust classification threshold for higher recall
- Implement probability-based risk scoring
"""

# Your code here
print("=" * 60)
print("BREAST CANCER DIAGNOSIS CLASSIFIER")
print("=" * 60)

import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import (
    accuracy_score, 
    classification_report, 
    confusion_matrix,
    recall_score,
    precision_score,
    f1_score
)

# TODO: Step 1 - Load and understand the data
print("\n--- Step 1: Load and Understand Data ---")


# TODO: Step 2 - Check class distribution (imbalance)
print("\n--- Step 2: Class Distribution ---")


# TODO: Step 3 - Split with stratification
print("\n--- Step 3: Split Data ---")


# TODO: Step 4 - Scale features
print("\n--- Step 4: Scale Features ---")


# TODO: Step 5 - Train models
print("\n--- Step 5: Train Models ---")


# TODO: Step 6 - Focus on recall for evaluation
print("\n--- Step 6: Evaluate (Focus on Recall) ---")


# TODO: Step 7 - Confusion matrix analysis
print("\n--- Step 7: Confusion Matrix Analysis ---")


# TODO: Step 8 - Risk assessment function
print("\n--- Step 8: Risk Assessment Function ---")


# TODO: Step 9 - Final recommendations
print("\n--- Step 9: Final Recommendations ---")

