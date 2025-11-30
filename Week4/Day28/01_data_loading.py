"""
DATA LOADING - End-to-End ML Project
=====================================
Day 28: Week 4 Mini-Project

Learn how to load and inspect datasets for machine learning projects.
"""

import numpy as np
import pandas as pd

print("=" * 60)
print("DATA LOADING - ML Project Pipeline")
print("=" * 60)

# ============================================================
# 1. Loading Data from Different Sources
# ============================================================

print("\n1. LOADING DATA FROM CSV")
print("-" * 40)

# Method 1: Load from CSV file
# df = pd.read_csv('your_dataset.csv')

# For demonstration, let's create a sample dataset
np.random.seed(42)

# Create sample housing data
n_samples = 1000

data = {
    'square_feet': np.random.randint(500, 5000, n_samples),
    'bedrooms': np.random.randint(1, 7, n_samples),
    'bathrooms': np.random.randint(1, 5, n_samples),
    'age_years': np.random.randint(0, 100, n_samples),
    'location_score': np.random.uniform(1, 10, n_samples).round(2),
    'garage_spaces': np.random.randint(0, 4, n_samples),
    'has_pool': np.random.choice([0, 1], n_samples, p=[0.7, 0.3]),
    'neighborhood': np.random.choice(['A', 'B', 'C', 'D'], n_samples)
}

# Calculate price based on features (simulated relationship)
price = (
    data['square_feet'] * 100 +
    data['bedrooms'] * 15000 +
    data['bathrooms'] * 10000 -
    data['age_years'] * 500 +
    data['location_score'] * 5000 +
    data['garage_spaces'] * 8000 +
    data['has_pool'] * 20000 +
    np.random.normal(0, 20000, n_samples)  # Add noise
)

data['price'] = price.astype(int)

# Create DataFrame
df = pd.DataFrame(data)

# Add some missing values for realistic data
missing_indices = np.random.choice(n_samples, size=50, replace=False)
df.loc[missing_indices[:20], 'bathrooms'] = np.nan
df.loc[missing_indices[20:35], 'garage_spaces'] = np.nan
df.loc[missing_indices[35:], 'location_score'] = np.nan

print("Sample dataset created successfully!")
print(f"Shape: {df.shape}")

# ============================================================
# 2. Initial Data Inspection
# ============================================================

print("\n2. INITIAL DATA INSPECTION")
print("-" * 40)

# First few rows
print("\nFirst 5 rows:")
print(df.head())

# Last few rows
print("\nLast 5 rows:")
print(df.tail())

# ============================================================
# 3. Data Information and Types
# ============================================================

print("\n3. DATA INFORMATION")
print("-" * 40)

# Data types and non-null counts
print("\nDataFrame Info:")
print(df.info())

# Data types only
print("\nData Types:")
print(df.dtypes)

# ============================================================
# 4. Statistical Summary
# ============================================================

print("\n4. STATISTICAL SUMMARY")
print("-" * 40)

# Numerical columns summary
print("\nNumerical Statistics:")
print(df.describe())

# Include categorical columns
print("\nAll Columns Statistics:")
print(df.describe(include='all'))

# ============================================================
# 5. Missing Values Analysis
# ============================================================

print("\n5. MISSING VALUES ANALYSIS")
print("-" * 40)

# Count missing values
print("\nMissing Values Count:")
print(df.isnull().sum())

# Percentage of missing values
print("\nMissing Values Percentage:")
print((df.isnull().sum() / len(df) * 100).round(2))

# ============================================================
# 6. Data Shape and Memory
# ============================================================

print("\n6. DATA SHAPE AND MEMORY")
print("-" * 40)

print(f"\nNumber of rows: {df.shape[0]}")
print(f"Number of columns: {df.shape[1]}")
print(f"Total cells: {df.size}")
print(f"Memory usage: {df.memory_usage(deep=True).sum() / 1024:.2f} KB")

# ============================================================
# 7. Column Analysis
# ============================================================

print("\n7. COLUMN ANALYSIS")
print("-" * 40)

# Unique values in categorical columns
print("\nUnique values in 'neighborhood':")
print(df['neighborhood'].unique())

# Value counts
print("\nNeighborhood distribution:")
print(df['neighborhood'].value_counts())

# ============================================================
# 8. Save Dataset for Next Steps
# ============================================================

print("\n8. SAVING DATASET")
print("-" * 40)

# Save to CSV
df.to_csv('housing_data.csv', index=False)
print("Dataset saved to 'housing_data.csv'")

# ============================================================
# EXERCISES
# ============================================================

print("\n" + "=" * 60)
print("EXERCISES")
print("=" * 60)

print("""
1. Load a real dataset from a URL:
   - Use pd.read_csv() with a URL
   - Example: Iris dataset, Titanic dataset

2. Inspect the dataset:
   - Check shape, info, and describe
   - Identify missing values
   - Identify data types

3. Answer these questions about your dataset:
   - How many numerical vs categorical columns?
   - What's the percentage of missing data?
   - What are the unique values in categorical columns?

4. Practice loading different file formats:
   - CSV, Excel, JSON
   - Use appropriate pandas functions
""")

# ============================================================
# KEY TAKEAWAYS
# ============================================================

print("\n" + "=" * 60)
print("KEY TAKEAWAYS")
print("=" * 60)

print("""
✅ Use pd.read_csv() for CSV files
✅ Use df.head() and df.tail() for quick inspection
✅ Use df.info() for data types and missing values
✅ Use df.describe() for statistical summary
✅ Always check for missing values before modeling
✅ Understand your data before any preprocessing
✅ Save cleaned data for reproducibility
""")
