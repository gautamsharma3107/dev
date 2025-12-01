"""
Day 22 - Data Inspection and Cleaning
=====================================
Learn: Exploring datasets and handling messy data

Key Concepts:
- Data inspection methods
- Handling missing values
- Dealing with duplicates
- Data type conversions
- Detecting and handling outliers
"""

import pandas as pd
import numpy as np

print("=" * 60)
print("DATA INSPECTION AND CLEANING")
print("=" * 60)

# ========== CREATE MESSY DATASET ==========
print("\n" + "=" * 60)
print("CREATING MESSY DATASET FOR PRACTICE")
print("=" * 60)

# Create dataset with common issues
np.random.seed(42)

messy_data = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10],  # Duplicate id=5
    'name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 
             'Eve', 'Frank', np.nan, 'Henry', 'Ivy', 'Jack'],
    'age': [25, 30, np.nan, 28, 32, 32, 150, 29, -5, 35, 27],  # Invalid ages
    'email': ['alice@email.com', 'bob@email.com', 'charlie@email.com',
              'diana@email.com', 'eve@email.com', 'eve@email.com',
              'frank@email.com', 'grace@email.com', 'henry@email.com',
              np.nan, 'jack@email.com'],
    'salary': ['50000', '60000', '75000', 'N/A', '65000',
               '65000', '80000', '55000', '70000', '72000', np.nan],
    'hire_date': ['2020-01-15', '2019-03-22', '2018-07-01', '2021-02-10',
                  '2017-11-05', '2017-11-05', '2022-06-15', '2020-09-30',
                  '2019-12-01', '2018-04-20', '2023-01-01'],
    'department': ['IT', 'hr', 'IT', 'Finance', 'HR',
                   'HR', 'it', 'Finance', 'FINANCE', 'IT', 'HR']
})

print("Messy Dataset (with intentional issues):")
print(messy_data)
print(f"\nIssues to fix:")
print("- Missing values (NaN)")
print("- Duplicate rows")
print("- Invalid ages (150, -5)")
print("- Inconsistent case ('IT' vs 'it')")
print("- Salary as string with 'N/A'")
print("- Hire date as string")

# ========== DATA INSPECTION ==========
print("\n" + "=" * 60)
print("DATA INSPECTION")
print("=" * 60)

df = messy_data.copy()

# Basic info
print("\n1. Shape and basic info:")
print(f"   Shape: {df.shape} (rows, columns)")
print(f"   Columns: {list(df.columns)}")

print("\n2. df.info():")
df.info()

print("\n3. df.describe():")
print(df.describe())

print("\n4. Data types:")
print(df.dtypes)

print("\n5. First and last rows:")
print(f"First 3:\n{df.head(3)}")
print(f"\nLast 3:\n{df.tail(3)}")

# ========== FINDING MISSING VALUES ==========
print("\n" + "=" * 60)
print("FINDING MISSING VALUES")
print("=" * 60)

print("\n1. Check for missing values:")
print(f"Total missing:\n{df.isnull().sum()}")

print(f"\n2. Percentage missing:")
missing_pct = (df.isnull().sum() / len(df) * 100).round(2)
print(missing_pct)

print(f"\n3. Total missing in dataset: {df.isnull().sum().sum()}")

print(f"\n4. Rows with any missing:")
print(df[df.isnull().any(axis=1)])

print(f"\n5. Rows with all values present:")
print(f"   Complete rows: {len(df.dropna())}")

# ========== HANDLING MISSING VALUES ==========
print("\n" + "=" * 60)
print("HANDLING MISSING VALUES")
print("=" * 60)

df_clean = df.copy()

print("\n1. Drop rows with any NaN:")
dropped_any = df_clean.dropna()
print(f"   Rows remaining: {len(dropped_any)} (from {len(df_clean)})")

print("\n2. Drop rows with NaN in specific columns:")
dropped_subset = df_clean.dropna(subset=['name', 'email'])
print(f"   Rows remaining: {len(dropped_subset)}")

print("\n3. Fill NaN with a value:")
filled = df_clean.copy()
filled['email'] = filled['email'].fillna('unknown@email.com')
print(f"   Email filled:\n{filled['email']}")

print("\n4. Fill NaN with mean/median (numeric):")
# First, we need to convert salary to numeric
df_clean['salary'] = pd.to_numeric(df_clean['salary'], errors='coerce')
mean_salary = df_clean['salary'].mean()
print(f"   Mean salary: {mean_salary:.2f}")
filled_mean = df_clean['salary'].fillna(mean_salary)
print(f"   Salary after fill:\n{filled_mean}")

print("\n5. Forward fill and backward fill:")
sample = pd.Series([1, np.nan, np.nan, 4, 5, np.nan, 7])
print(f"   Original:  {list(sample)}")
print(f"   Forward:   {list(sample.ffill())}")
print(f"   Backward:  {list(sample.bfill())}")

# ========== FINDING DUPLICATES ==========
print("\n" + "=" * 60)
print("FINDING AND HANDLING DUPLICATES")
print("=" * 60)

df_dup = messy_data.copy()

print("\n1. Check for duplicates:")
print(f"   Total duplicates: {df_dup.duplicated().sum()}")

print("\n2. Show duplicate rows:")
duplicates = df_dup[df_dup.duplicated(keep=False)]  # keep=False shows all duplicates
print(duplicates)

print("\n3. Check duplicates in specific column:")
print(f"   Duplicate IDs: {df_dup['id'].duplicated().sum()}")
print(f"   Duplicate names: {df_dup['name'].duplicated().sum()}")

print("\n4. Remove duplicates:")
df_no_dups = df_dup.drop_duplicates()
print(f"   Rows after removing duplicates: {len(df_no_dups)} (from {len(df_dup)})")

print("\n5. Remove duplicates based on specific columns:")
df_unique_id = df_dup.drop_duplicates(subset=['id'], keep='first')
print(f"   Rows after keeping first unique ID: {len(df_unique_id)}")

# ========== DATA TYPE CONVERSION ==========
print("\n" + "=" * 60)
print("DATA TYPE CONVERSION")
print("=" * 60)

df_types = messy_data.copy()

print(f"\nOriginal types:\n{df_types.dtypes}")

print("\n1. Convert salary to numeric (handling errors):")
df_types['salary'] = pd.to_numeric(df_types['salary'], errors='coerce')
print(f"   Salary dtype: {df_types['salary'].dtype}")
print(f"   Salary values:\n{df_types['salary']}")

print("\n2. Convert hire_date to datetime:")
df_types['hire_date'] = pd.to_datetime(df_types['hire_date'])
print(f"   hire_date dtype: {df_types['hire_date'].dtype}")
print(f"   Sample dates:\n{df_types['hire_date'].head()}")

print("\n3. Convert to specific type:")
df_types['id'] = df_types['id'].astype(str)
print(f"   id dtype: {df_types['id'].dtype}")

print(f"\nUpdated types:\n{df_types.dtypes}")

# ========== STRING CLEANING ==========
print("\n" + "=" * 60)
print("STRING CLEANING")
print("=" * 60)

df_str = messy_data.copy()

print(f"\nOriginal department values:\n{df_str['department'].unique()}")

print("\n1. Convert to lowercase:")
df_str['department'] = df_str['department'].str.lower()
print(f"   After lowercase: {df_str['department'].unique()}")

print("\n2. Strip whitespace:")
sample_with_spaces = pd.Series(['  hello  ', 'world  ', '  python'])
print(f"   Original: {list(sample_with_spaces)}")
print(f"   Stripped: {list(sample_with_spaces.str.strip())}")

print("\n3. Replace values:")
df_str['department'] = df_str['department'].replace('hr', 'human_resources')
print(f"   After replace: {df_str['department'].unique()}")

print("\n4. String contains:")
has_email = df_str['email'].str.contains('@', na=False)
print(f"   Rows with @ in email: {has_email.sum()}")

# ========== HANDLING OUTLIERS ==========
print("\n" + "=" * 60)
print("HANDLING OUTLIERS")
print("=" * 60)

df_outliers = messy_data.copy()
df_outliers['age'] = pd.to_numeric(df_outliers['age'], errors='coerce')

print(f"\nAge statistics:")
print(f"   Min: {df_outliers['age'].min()}")
print(f"   Max: {df_outliers['age'].max()}")
print(f"   Mean: {df_outliers['age'].mean():.2f}")

print("\n1. Identify outliers with IQR method:")
Q1 = df_outliers['age'].quantile(0.25)
Q3 = df_outliers['age'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
print(f"   Q1: {Q1}, Q3: {Q3}, IQR: {IQR}")
print(f"   Lower bound: {lower_bound}, Upper bound: {upper_bound}")

outliers = df_outliers[(df_outliers['age'] < lower_bound) | (df_outliers['age'] > upper_bound)]
print(f"   Outliers found:\n{outliers[['name', 'age']]}")

print("\n2. Filter out outliers (using domain knowledge):")
valid_age = df_outliers[(df_outliers['age'] >= 18) & (df_outliers['age'] <= 100)]
print(f"   Valid ages (18-100): {len(valid_age)} rows")

print("\n3. Cap outliers (winsorization):")
df_capped = df_outliers.copy()
df_capped['age'] = df_capped['age'].clip(lower=18, upper=65)
print(f"   Ages after capping to 18-65:\n{df_capped['age'].values}")

# ========== COMPLETE CLEANING EXAMPLE ==========
print("\n" + "=" * 60)
print("COMPLETE CLEANING EXAMPLE")
print("=" * 60)

df_final = messy_data.copy()
print(f"Starting with {len(df_final)} rows")

# Step 1: Remove duplicates
df_final = df_final.drop_duplicates()
print(f"1. After removing duplicates: {len(df_final)} rows")

# Step 2: Convert data types
df_final['salary'] = pd.to_numeric(df_final['salary'], errors='coerce')
df_final['hire_date'] = pd.to_datetime(df_final['hire_date'])
print("2. Converted salary and hire_date types")

# Step 3: Standardize strings
df_final['department'] = df_final['department'].str.lower()
df_final['name'] = df_final['name'].str.strip()
print("3. Standardized text columns")

# Step 4: Handle invalid ages
df_final.loc[(df_final['age'] < 18) | (df_final['age'] > 100), 'age'] = np.nan
print("4. Set invalid ages to NaN")

# Step 5: Fill missing values
df_final['age'] = df_final['age'].fillna(df_final['age'].median())
df_final['salary'] = df_final['salary'].fillna(df_final['salary'].median())
df_final['email'] = df_final['email'].fillna('unknown@email.com')
df_final['name'] = df_final['name'].fillna('Unknown')
print("5. Filled missing values")

# Step 6: Drop rows still missing critical data
df_final = df_final.dropna()
print(f"6. After dropping remaining NaN: {len(df_final)} rows")

print(f"\nCleaned Dataset:")
print(df_final)

print(f"\nData types:")
print(df_final.dtypes)

print(f"\nMissing values:")
print(df_final.isnull().sum())

print("\n" + "=" * 60)
print("✅ Data Inspection and Cleaning - Complete!")
print("=" * 60)
