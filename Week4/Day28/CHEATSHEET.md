# Week 4 ML Cheatsheet

## 📊 NumPy Quick Reference

```python
import numpy as np

# Array Creation
arr = np.array([1, 2, 3, 4, 5])
zeros = np.zeros((3, 3))
ones = np.ones((3, 3))
random_arr = np.random.rand(5, 5)
range_arr = np.arange(0, 10, 2)
linspace_arr = np.linspace(0, 1, 100)

# Array Operations
arr.shape          # Get shape
arr.reshape(5, 1)  # Reshape
arr.T              # Transpose
arr + arr          # Element-wise addition
arr * arr          # Element-wise multiplication
np.dot(arr, arr)   # Dot product

# Statistical Functions
arr.mean()         # Mean
arr.std()          # Standard deviation
arr.max()          # Maximum
arr.min()          # Minimum
np.median(arr)     # Median
np.percentile(arr, 75)  # Percentile
```

## 🐼 Pandas Quick Reference

```python
import pandas as pd

# DataFrame Creation
df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
df = pd.read_csv('file.csv')

# Data Inspection
df.head()          # First 5 rows
df.tail()          # Last 5 rows
df.info()          # Data types & missing values
df.describe()      # Statistical summary
df.shape           # (rows, columns)
df.columns         # Column names
df.dtypes          # Data types

# Selection
df['column']       # Single column
df[['col1', 'col2']]  # Multiple columns
df.loc[0]          # Row by label
df.iloc[0]         # Row by index
df[df['col'] > 5]  # Filter rows

# Missing Values
df.isnull().sum()  # Count missing
df.dropna()        # Drop missing
df.fillna(value)   # Fill missing

# Grouping & Aggregation
df.groupby('col').mean()
df.groupby('col').agg(['mean', 'sum'])

# Merging
pd.merge(df1, df2, on='key')
pd.concat([df1, df2])
```

## 📈 Matplotlib Quick Reference

```python
import matplotlib.pyplot as plt

# Basic Plots
plt.plot(x, y)              # Line plot
plt.scatter(x, y)           # Scatter plot
plt.bar(x, y)               # Bar chart
plt.hist(data, bins=30)     # Histogram
plt.boxplot(data)           # Box plot

# Customization
plt.title('Title')
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes[0, 0].plot(x, y)

# Save Figure
plt.savefig('plot.png', dpi=100, bbox_inches='tight')
plt.show()
```

## 📊 Seaborn Quick Reference

```python
import seaborn as sns

# Distribution Plots
sns.histplot(data, kde=True)
sns.kdeplot(data)
sns.boxplot(x='cat', y='num', data=df)

# Relationship Plots
sns.scatterplot(x='x', y='y', data=df, hue='category')
sns.lineplot(x='x', y='y', data=df)
sns.pairplot(df)

# Correlation
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')

# Categorical
sns.countplot(x='category', data=df)
sns.barplot(x='cat', y='num', data=df)
```

## 🤖 Scikit-learn Quick Reference

### Data Preparation

```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Feature Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)  # Only transform!

# Label Encoding
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# One-Hot Encoding
df_encoded = pd.get_dummies(df, columns=['category'])
```

### Regression Models

```python
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

# Linear Regression
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Ridge Regression (L2 regularization)
ridge = Ridge(alpha=1.0)

# Lasso Regression (L1 regularization)
lasso = Lasso(alpha=1.0)

# Random Forest
rf = RandomForestRegressor(n_estimators=100, max_depth=10, random_state=42)
```

### Classification Models

```python
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

# Logistic Regression
lr = LogisticRegression()

# Decision Tree
dt = DecisionTreeClassifier(max_depth=5)

# Random Forest
rf = RandomForestClassifier(n_estimators=100, random_state=42)
```

### Unsupervised Learning

```python
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# K-Means Clustering
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(X)

# PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)
```

### Model Evaluation

```python
from sklearn.metrics import (
    mean_squared_error, mean_absolute_error, r2_score,  # Regression
    accuracy_score, precision_score, recall_score, f1_score,  # Classification
    confusion_matrix, classification_report
)

# Regression Metrics
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Classification Metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
```

### Cross-Validation & Hyperparameter Tuning

```python
from sklearn.model_selection import cross_val_score, GridSearchCV

# Cross-Validation
scores = cross_val_score(model, X, y, cv=5, scoring='r2')
print(f"Mean: {scores.mean():.4f} (+/- {scores.std() * 2:.4f})")

# Grid Search
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [5, 10, 15]
}
grid_search = GridSearchCV(model, param_grid, cv=5, scoring='r2')
grid_search.fit(X_train, y_train)
best_model = grid_search.best_estimator_
```

### Save & Load Models

```python
import joblib

# Save
joblib.dump(model, 'model.pkl')
joblib.dump(scaler, 'scaler.pkl')

# Load
model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')
```

## 📋 ML Pipeline Template

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error
import joblib

# 1. Load Data
df = pd.read_csv('data.csv')

# 2. Prepare Features and Target
X = df.drop('target', axis=1)
y = df['target']

# 3. Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Scale Features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 5. Train Model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# 6. Make Predictions
y_pred = model.predict(X_test_scaled)

# 7. Evaluate
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f"R²: {r2:.4f}, RMSE: {rmse:.4f}")

# 8. Save Model
joblib.dump(model, 'model.pkl')
joblib.dump(scaler, 'scaler.pkl')
```

## 🎯 Common Mistakes to Avoid

| Mistake | Solution |
|---------|----------|
| Fitting scaler on test data | Only fit on train, transform both |
| Not handling missing values | Check and handle before modeling |
| Not scaling features | Scale for distance-based algorithms |
| Ignoring data leakage | Keep test data completely separate |
| Not using cross-validation | Use CV for robust evaluation |
| Overfitting | Use regularization, cross-validation |

## 📊 When to Use Which Model

| Problem Type | Model Options |
|--------------|---------------|
| Linear relationship | Linear Regression |
| Non-linear regression | Random Forest, Gradient Boosting |
| Binary classification | Logistic Regression, Random Forest |
| Multi-class classification | Random Forest, Neural Networks |
| Clustering | K-Means, DBSCAN |
| Dimensionality reduction | PCA, t-SNE |

## 🔑 Key Metrics Reference

### Regression
- **R² (R-squared)**: 0-1, higher is better (variance explained)
- **RMSE**: Same units as target, lower is better
- **MAE**: Same units as target, lower is better, robust to outliers

### Classification
- **Accuracy**: Overall correctness (use when balanced classes)
- **Precision**: Of predicted positives, how many are correct
- **Recall**: Of actual positives, how many did we find
- **F1-Score**: Harmonic mean of precision and recall

---

**Pro Tips:**
- Always visualize your data first
- Start with simple models, then increase complexity
- Document everything for reproducibility
- Use random_state for reproducible results
- Monitor for overfitting with train/test comparison
