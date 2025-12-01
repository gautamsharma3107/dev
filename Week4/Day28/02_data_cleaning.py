"""
DATA CLEANING - End-to-End ML Project
======================================
Day 28: Week 4 Mini-Project

Learn how to clean and preprocess data for machine learning.
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder, MinMaxScaler

print("=" * 60)
print("DATA CLEANING - ML Project Pipeline")
print("=" * 60)

# Load the dataset (from previous step)
# df = pd.read_csv('housing_data.csv')

# For demonstration, recreate the sample dataset
np.random.seed(42)
n_samples = 1000

data = {
    'square_feet': np.random.randint(500, 5000, n_samples),
    'bedrooms': np.random.randint(1, 7, n_samples),
    'bathrooms': np.random.randint(1, 5, n_samples).astype(float),
    'age_years': np.random.randint(0, 100, n_samples),
    'location_score': np.random.uniform(1, 10, n_samples).round(2),
    'garage_spaces': np.random.randint(0, 4, n_samples).astype(float),
    'has_pool': np.random.choice([0, 1], n_samples, p=[0.7, 0.3]),
    'neighborhood': np.random.choice(['A', 'B', 'C', 'D'], n_samples)
}

price = (
    data['square_feet'] * 100 +
    data['bedrooms'] * 15000 +
    data['bathrooms'] * 10000 -
    data['age_years'] * 500 +
    data['location_score'] * 5000 +
    data['garage_spaces'] * 8000 +
    data['has_pool'] * 20000 +
    np.random.normal(0, 20000, n_samples)
)
data['price'] = price.astype(int)

df = pd.DataFrame(data)

# Add missing values
missing_indices = np.random.choice(n_samples, size=50, replace=False)
df.loc[missing_indices[:20], 'bathrooms'] = np.nan
df.loc[missing_indices[20:35], 'garage_spaces'] = np.nan
df.loc[missing_indices[35:], 'location_score'] = np.nan

# Add duplicates
df = pd.concat([df, df.iloc[:10]], ignore_index=True)

# Add outliers
df.loc[1001, 'price'] = 10000000  # Extreme outlier

print("Dataset loaded with imperfections!")
print(f"Shape: {df.shape}")

# ============================================================
# 1. Handling Missing Values
# ============================================================

print("\n1. HANDLING MISSING VALUES")
print("-" * 40)

# Check missing values
print("\nMissing values before cleaning:")
print(df.isnull().sum())

# Strategy 1: Drop rows with missing values
df_dropped = df.dropna()
print(f"\nAfter dropna(): {len(df_dropped)} rows remain")

# Strategy 2: Fill with mean (numerical)
df_filled = df.copy()
df_filled['bathrooms'].fillna(df_filled['bathrooms'].mean(), inplace=True)
df_filled['garage_spaces'].fillna(df_filled['garage_spaces'].median(), inplace=True)
df_filled['location_score'].fillna(df_filled['location_score'].mean(), inplace=True)

print("\nMissing values after filling:")
print(df_filled.isnull().sum())

# Use the filled version
df = df_filled

# ============================================================
# 2. Handling Duplicates
# ============================================================

print("\n2. HANDLING DUPLICATES")
print("-" * 40)

# Check duplicates
print(f"\nDuplicate rows: {df.duplicated().sum()}")

# Remove duplicates
df = df.drop_duplicates()
print(f"After removing duplicates: {len(df)} rows")

# ============================================================
# 3. Handling Outliers
# ============================================================

print("\n3. HANDLING OUTLIERS")
print("-" * 40)

# Method 1: IQR method
def remove_outliers_iqr(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    print(f"\n{column}: {len(outliers)} outliers detected")
    print(f"  Range: [{lower_bound:.2f}, {upper_bound:.2f}]")
    
    return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]

# Method 2: Z-score method
def remove_outliers_zscore(df, column, threshold=3):
    mean = df[column].mean()
    std = df[column].std()
    z_scores = np.abs((df[column] - mean) / std)
    
    outliers = df[z_scores > threshold]
    print(f"\n{column}: {len(outliers)} outliers (z-score > {threshold})")
    
    return df[z_scores <= threshold]

print("\nDetecting outliers in price column:")
df_clean = remove_outliers_iqr(df.copy(), 'price')
print(f"\nAfter outlier removal: {len(df_clean)} rows")

# ============================================================
# 4. Data Type Conversions
# ============================================================

print("\n4. DATA TYPE CONVERSIONS")
print("-" * 40)

print("\nOriginal data types:")
print(df.dtypes)

# Convert appropriate columns
df['bedrooms'] = df['bedrooms'].astype(int)
df['has_pool'] = df['has_pool'].astype(bool)
df['bathrooms'] = df['bathrooms'].astype(int)
df['garage_spaces'] = df['garage_spaces'].astype(int)

print("\nAfter conversion:")
print(df.dtypes)

# ============================================================
# 5. Encoding Categorical Variables
# ============================================================

print("\n5. ENCODING CATEGORICAL VARIABLES")
print("-" * 40)

# Method 1: Label Encoding
le = LabelEncoder()
df['neighborhood_encoded'] = le.fit_transform(df['neighborhood'])

print("\nLabel Encoding:")
print(df[['neighborhood', 'neighborhood_encoded']].drop_duplicates())

# Method 2: One-Hot Encoding
df_encoded = pd.get_dummies(df, columns=['neighborhood'], prefix='nbhd')

print("\nOne-Hot Encoded columns:")
print([col for col in df_encoded.columns if 'nbhd' in col])

# ============================================================
# 6. Feature Scaling
# ============================================================

print("\n6. FEATURE SCALING")
print("-" * 40)

numerical_cols = ['square_feet', 'bedrooms', 'bathrooms', 'age_years', 
                  'location_score', 'garage_spaces']

# Method 1: StandardScaler (mean=0, std=1)
scaler_standard = StandardScaler()
df_scaled_standard = df.copy()
df_scaled_standard[numerical_cols] = scaler_standard.fit_transform(df[numerical_cols])

print("\nStandardScaler (first 3 rows):")
print(df_scaled_standard[numerical_cols].head(3))

# Method 2: MinMaxScaler (0-1 range)
scaler_minmax = MinMaxScaler()
df_scaled_minmax = df.copy()
df_scaled_minmax[numerical_cols] = scaler_minmax.fit_transform(df[numerical_cols])

print("\nMinMaxScaler (first 3 rows):")
print(df_scaled_minmax[numerical_cols].head(3))

# ============================================================
# 7. Feature Engineering
# ============================================================

print("\n7. FEATURE ENGINEERING")
print("-" * 40)

# Create new features
df['price_per_sqft'] = df['price'] / df['square_feet']
df['total_rooms'] = df['bedrooms'] + df['bathrooms']
df['is_new'] = (df['age_years'] < 5).astype(int)

print("\nNew features created:")
print(df[['price_per_sqft', 'total_rooms', 'is_new']].head())

# ============================================================
# 8. Final Clean Dataset
# ============================================================

print("\n8. FINAL CLEAN DATASET")
print("-" * 40)

# Select final features for modeling
final_features = ['square_feet', 'bedrooms', 'bathrooms', 'age_years',
                  'location_score', 'garage_spaces', 'has_pool', 
                  'neighborhood_encoded', 'price']

df_final = df[final_features].copy()

print(f"\nFinal dataset shape: {df_final.shape}")
print("\nFinal dataset info:")
print(df_final.info())

# Save cleaned dataset
df_final.to_csv('housing_data_cleaned.csv', index=False)
print("\nCleaned dataset saved to 'housing_data_cleaned.csv'")

# ============================================================
# EXERCISES
# ============================================================

print("\n" + "=" * 60)
print("EXERCISES")
print("=" * 60)

print("""
1. Handle missing values in a dataset:
   - Try different strategies (drop, fill with mean/median/mode)
   - Compare results

2. Detect and handle outliers:
   - Use IQR method
   - Use Z-score method
   - Visualize before and after

3. Encode categorical variables:
   - Use Label Encoding
   - Use One-Hot Encoding
   - Know when to use each

4. Scale features:
   - Apply StandardScaler
   - Apply MinMaxScaler
   - Understand when each is appropriate

5. Create 3 new features from existing columns
""")

# ============================================================
# KEY TAKEAWAYS
# ============================================================

print("\n" + "=" * 60)
print("KEY TAKEAWAYS")
print("=" * 60)

print("""
✅ Always handle missing values before modeling
✅ Remove or cap outliers based on business context
✅ Convert data types appropriately
✅ Encode categorical variables for ML algorithms
✅ Scale features for algorithms that are sensitive to scale
✅ Feature engineering can improve model performance
✅ Document all preprocessing steps for reproducibility
""")
