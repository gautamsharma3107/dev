# Day 24 Quick Reference Cheat Sheet

## Machine Learning Basics
```python
# Machine Learning is about learning patterns from data
# to make predictions or decisions without being explicitly programmed

# Key Terms:
# - Features (X): Input variables used for prediction
# - Target (y): Output variable we want to predict
# - Model: Algorithm that learns patterns from data
# - Training: Process of learning from data
# - Inference: Making predictions on new data
```

## Types of Machine Learning
```python
# SUPERVISED LEARNING (labeled data)
# - Classification: Predict categories (spam/not spam)
# - Regression: Predict continuous values (price)

# UNSUPERVISED LEARNING (no labels)
# - Clustering: Group similar data (customer segments)
# - Dimensionality Reduction: Reduce features (PCA)

# REINFORCEMENT LEARNING
# - Agent learns through trial and error
# - Used in games, robotics
```

## Train-Test Split
```python
from sklearn.model_selection import train_test_split

# Basic split (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# With stratification (for classification)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# With validation set
X_temp, X_test, y_temp, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
X_train, X_val, y_train, y_val = train_test_split(
    X_temp, y_temp, test_size=0.25, random_state=42
)
```

## Feature Scaling
```python
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# StandardScaler: Mean=0, Std=1 (best for most cases)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)  # Only transform!

# MinMaxScaler: Scale to range [0, 1]
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# When to scale:
# - Distance-based algorithms (KNN, SVM, K-Means)
# - Gradient descent algorithms (Neural Networks, Linear Regression)
# - NOT needed for tree-based models (Decision Trees, Random Forest)
```

## Scikit-learn Workflow
```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# 1. Load Data
import pandas as pd
df = pd.read_csv('data.csv')
X = df.drop('target', axis=1)
y = df['target']

# 2. Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. Scale Features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 4. Create Model
model = LogisticRegression()

# 5. Train Model
model.fit(X_train_scaled, y_train)

# 6. Make Predictions
y_pred = model.predict(X_test_scaled)

# 7. Evaluate Model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
print(classification_report(y_test, y_pred))
```

## Common Algorithms
```python
# Classification
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

# Regression
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR

# Clustering
from sklearn.cluster import KMeans, DBSCAN
from sklearn.mixture import GaussianMixture
```

## Model Evaluation Metrics
```python
from sklearn.metrics import (
    # Classification
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
    
    # Regression
    mean_squared_error,
    mean_absolute_error,
    r2_score
)

# Classification metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')

# Regression metrics
mse = mean_squared_error(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred, squared=False)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
```

## Dataset Loading
```python
from sklearn.datasets import (
    load_iris,           # Classification (3 classes)
    load_digits,         # Classification (10 digits)
    load_breast_cancer,  # Binary classification
    load_wine,           # Classification (3 wine types)
    load_boston,         # Regression (house prices)
    make_classification, # Generate synthetic classification data
    make_regression      # Generate synthetic regression data
)

# Load built-in dataset
data = load_iris()
X = data.data
y = data.target
feature_names = data.feature_names
target_names = data.target_names
```

## Common Patterns
```python
# Cross-validation
from sklearn.model_selection import cross_val_score
scores = cross_val_score(model, X, y, cv=5)
print(f"CV Scores: {scores}")
print(f"Mean: {scores.mean():.2f} (+/- {scores.std() * 2:.2f})")

# GridSearchCV for hyperparameter tuning
from sklearn.model_selection import GridSearchCV
param_grid = {'C': [0.1, 1, 10], 'kernel': ['linear', 'rbf']}
grid_search = GridSearchCV(SVC(), param_grid, cv=5)
grid_search.fit(X_train, y_train)
print(f"Best params: {grid_search.best_params_}")

# Pipeline
from sklearn.pipeline import Pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', LogisticRegression())
])
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)

# Save and load model
import joblib
joblib.dump(model, 'model.pkl')
loaded_model = joblib.load('model.pkl')
```

---
**Keep this handy for quick reference!** 🚀
