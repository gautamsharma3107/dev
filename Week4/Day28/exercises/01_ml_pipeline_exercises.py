"""
ML PIPELINE EXERCISES - Day 28
================================
Practice building end-to-end ML pipelines.
"""

import numpy as np
import pandas as pd

print("=" * 60)
print("ML PIPELINE EXERCISES")
print("=" * 60)

# ============================================================
# EXERCISE 1: Data Loading and Inspection
# ============================================================

print("\n" + "=" * 60)
print("EXERCISE 1: Data Loading and Inspection")
print("=" * 60)

print("""
Task: Create a sample dataset and perform initial data inspection.

Requirements:
1. Create a DataFrame with at least 5 columns (mix of numerical and categorical)
2. Include at least 100 rows
3. Add some missing values intentionally
4. Perform the following inspections:
   - Check shape
   - Display first 5 rows
   - Check data types
   - Count missing values
   - Display statistical summary
""")

# YOUR CODE HERE:
# np.random.seed(42)
# data = {...}
# df = pd.DataFrame(data)
# ...




# ============================================================
# EXERCISE 2: Data Cleaning
# ============================================================

print("\n" + "=" * 60)
print("EXERCISE 2: Data Cleaning")
print("=" * 60)

print("""
Task: Clean the dataset you created in Exercise 1.

Requirements:
1. Handle missing values (choose appropriate strategy for each column)
2. Check for and remove duplicates
3. Detect outliers using IQR method
4. Convert data types if necessary
5. Display cleaned data statistics
""")

# YOUR CODE HERE:




# ============================================================
# EXERCISE 3: Feature Engineering
# ============================================================

print("\n" + "=" * 60)
print("EXERCISE 3: Feature Engineering")
print("=" * 60)

print("""
Task: Create new features from existing ones.

Requirements:
1. Create at least 3 new features from existing columns
2. Encode categorical variables
3. Create interaction features (e.g., multiply two columns)
4. Create binned features (e.g., age groups)
""")

# YOUR CODE HERE:




# ============================================================
# EXERCISE 4: Train-Test Split and Scaling
# ============================================================

print("\n" + "=" * 60)
print("EXERCISE 4: Train-Test Split and Scaling")
print("=" * 60)

print("""
Task: Prepare data for modeling.

Requirements:
1. Define features (X) and target (y)
2. Split data into train and test sets (80-20)
3. Apply StandardScaler to features
4. Print shapes of all resulting datasets
""")

# YOUR CODE HERE:
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler




# ============================================================
# EXERCISE 5: Model Training and Comparison
# ============================================================

print("\n" + "=" * 60)
print("EXERCISE 5: Model Training and Comparison")
print("=" * 60)

print("""
Task: Train multiple models and compare their performance.

Requirements:
1. Train at least 3 different models (e.g., Linear Regression, Random Forest, Gradient Boosting)
2. Make predictions on test data
3. Calculate R², RMSE, and MAE for each model
4. Create a comparison DataFrame showing all metrics
5. Identify the best model
""")

# YOUR CODE HERE:
# from sklearn.linear_model import LinearRegression
# from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
# from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error




# ============================================================
# EXERCISE 6: Cross-Validation
# ============================================================

print("\n" + "=" * 60)
print("EXERCISE 6: Cross-Validation")
print("=" * 60)

print("""
Task: Perform cross-validation on your best model.

Requirements:
1. Use 5-fold cross-validation
2. Calculate mean and standard deviation of scores
3. Try different values of k (3, 5, 10)
4. Compare results
""")

# YOUR CODE HERE:
# from sklearn.model_selection import cross_val_score




# ============================================================
# EXERCISE 7: Hyperparameter Tuning
# ============================================================

print("\n" + "=" * 60)
print("EXERCISE 7: Hyperparameter Tuning")
print("=" * 60)

print("""
Task: Tune hyperparameters using GridSearchCV.

Requirements:
1. Define a parameter grid for your best model
2. Use GridSearchCV with 5-fold CV
3. Find the best parameters
4. Compare performance before and after tuning
""")

# YOUR CODE HERE:
# from sklearn.model_selection import GridSearchCV




# ============================================================
# EXERCISE 8: Model Evaluation Deep Dive
# ============================================================

print("\n" + "=" * 60)
print("EXERCISE 8: Model Evaluation Deep Dive")
print("=" * 60)

print("""
Task: Perform comprehensive model evaluation.

Requirements:
1. Create residual plots
2. Analyze prediction errors by ranges
3. Plot actual vs predicted values
4. Create learning curves
5. Check for overfitting
""")

# YOUR CODE HERE:
# import matplotlib.pyplot as plt




# ============================================================
# EXERCISE 9: Feature Importance Analysis
# ============================================================

print("\n" + "=" * 60)
print("EXERCISE 9: Feature Importance Analysis")
print("=" * 60)

print("""
Task: Analyze which features are most important.

Requirements:
1. Extract feature importances from Random Forest
2. Create a bar chart of feature importances
3. Try removing low-importance features
4. Compare model performance with reduced features
""")

# YOUR CODE HERE:




# ============================================================
# EXERCISE 10: Complete Pipeline
# ============================================================

print("\n" + "=" * 60)
print("EXERCISE 10: Complete Pipeline")
print("=" * 60)

print("""
Task: Create a complete, reusable ML pipeline.

Requirements:
1. Create a function that takes raw data and returns trained model
2. Include all preprocessing steps
3. Add model training and evaluation
4. Save the model and scaler
5. Create a prediction function
""")

# YOUR CODE HERE:
# def ml_pipeline(df, target_column):
#     """
#     Complete ML pipeline from raw data to trained model.
#     """
#     pass




# ============================================================
# BONUS EXERCISE: Classification Pipeline
# ============================================================

print("\n" + "=" * 60)
print("BONUS: Classification Pipeline")
print("=" * 60)

print("""
Task: Build a classification pipeline.

Requirements:
1. Create a binary classification dataset
2. Train Logistic Regression, Decision Tree, and Random Forest
3. Calculate accuracy, precision, recall, and F1-score
4. Create confusion matrices
5. Plot ROC curves and calculate AUC
""")

# YOUR CODE HERE:
# from sklearn.linear_model import LogisticRegression
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
# from sklearn.metrics import confusion_matrix, roc_curve, auc




print("\n" + "=" * 60)
print("EXERCISES COMPLETE!")
print("=" * 60)

print("""
Great job completing these exercises!

Key Skills Practiced:
- Data loading and inspection
- Data cleaning and preprocessing
- Feature engineering
- Model training and comparison
- Cross-validation
- Hyperparameter tuning
- Model evaluation
- Feature importance analysis
- Building complete ML pipelines

Next Steps:
1. Try with real datasets (Kaggle, UCI ML Repository)
2. Build more complex pipelines
3. Deploy a model using Flask/FastAPI
""")
