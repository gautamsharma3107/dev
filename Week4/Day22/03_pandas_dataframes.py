"""
Day 22 - Pandas DataFrames Basics
=================================
Learn: Creating and working with Pandas DataFrames

Key Concepts:
- DataFrame = 2D labeled data structure
- Like a spreadsheet or SQL table
- Built on top of NumPy
- Most important data structure in data science
"""

import pandas as pd
import numpy as np

print("=" * 60)
print("PANDAS DATAFRAMES BASICS")
print("=" * 60)

# ========== WHY PANDAS? ==========
print("\n" + "=" * 60)
print("WHY PANDAS?")
print("=" * 60)

print("""
Pandas Benefits:
1. Labeled data - columns have names
2. Handles missing data gracefully
3. Powerful data manipulation
4. Easy file I/O (CSV, Excel, JSON)
5. SQL-like operations (merge, join)
6. Time series support
7. Foundation for data analysis & ML
""")

# ========== CREATING DATAFRAMES ==========
print("\n" + "=" * 60)
print("CREATING DATAFRAMES")
print("=" * 60)

# Method 1: From dictionary
print("\n1. From dictionary:")
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'age': [25, 30, 35, 28, 32],
    'city': ['NYC', 'LA', 'SF', 'NYC', 'LA'],
    'salary': [50000, 60000, 75000, 55000, 65000]
}
df = pd.DataFrame(data)
print(df)

# Method 2: From list of dictionaries
print("\n2. From list of dictionaries:")
data_list = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30},
    {'name': 'Charlie', 'age': 35}
]
df2 = pd.DataFrame(data_list)
print(df2)

# Method 3: From NumPy array
print("\n3. From NumPy array:")
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
df3 = pd.DataFrame(arr, columns=['A', 'B', 'C'])
print(df3)

# Method 4: From Series
print("\n4. From Series:")
s1 = pd.Series([1, 2, 3], name='col1')
s2 = pd.Series([4, 5, 6], name='col2')
df4 = pd.concat([s1, s2], axis=1)
print(df4)

# ========== SERIES (1D) ==========
print("\n" + "=" * 60)
print("PANDAS SERIES (1D)")
print("=" * 60)

# Series is like a single column
series = pd.Series([10, 20, 30, 40, 50], name='values')
print(f"Series:\n{series}")
print(f"\nSeries with custom index:")
series_custom = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(series_custom)

# Extract Series from DataFrame
print(f"\nExtract column as Series:")
print(f"Type: {type(df['name'])}")
print(df['name'])

# ========== DATAFRAME PROPERTIES ==========
print("\n" + "=" * 60)
print("DATAFRAME PROPERTIES")
print("=" * 60)

print(f"DataFrame:\n{df}\n")
print(f"shape:   {df.shape}        # (rows, columns)")
print(f"columns: {list(df.columns)}  # Column names")
print(f"index:   {list(df.index)}       # Row indices")
print(f"dtypes:\n{df.dtypes}")
print(f"\nvalues (NumPy array):\n{df.values}")

# ========== DATA INSPECTION ==========
print("\n" + "=" * 60)
print("DATA INSPECTION")
print("=" * 60)

print(f"head(3) - First 3 rows:\n{df.head(3)}\n")
print(f"tail(2) - Last 2 rows:\n{df.tail(2)}\n")
print(f"info():")
df.info()
print(f"\ndescribe() - Statistics:\n{df.describe()}")

# ========== COLUMN SELECTION ==========
print("\n" + "=" * 60)
print("COLUMN SELECTION")
print("=" * 60)

print(f"DataFrame:\n{df}\n")

# Single column (returns Series)
print(f"df['name'] (Series):\n{df['name']}\n")

# Multiple columns (returns DataFrame)
print(f"df[['name', 'age']] (DataFrame):\n{df[['name', 'age']]}\n")

# Using dot notation (only for valid Python identifiers)
print(f"df.name:\n{df.name}\n")

# ========== ROW SELECTION WITH iloc (Position) ==========
print("\n" + "=" * 60)
print("ROW SELECTION: iloc (Position-based)")
print("=" * 60)

print(f"DataFrame:\n{df}\n")

print(f"df.iloc[0] - First row:\n{df.iloc[0]}\n")
print(f"df.iloc[0:3] - Rows 0-2:\n{df.iloc[0:3]}\n")
print(f"df.iloc[-1] - Last row:\n{df.iloc[-1]}\n")
print(f"df.iloc[0, 1] - Row 0, Col 1: {df.iloc[0, 1]}")
print(f"df.iloc[:, 0] - First column:\n{df.iloc[:, 0]}\n")
print(f"df.iloc[0:2, 0:2] - Subset:\n{df.iloc[0:2, 0:2]}")

# ========== ROW SELECTION WITH loc (Label) ==========
print("\n" + "=" * 60)
print("ROW SELECTION: loc (Label-based)")
print("=" * 60)

# Create DataFrame with custom index
df_labeled = df.set_index('name')
print(f"DataFrame with name as index:\n{df_labeled}\n")

print(f"df_labeled.loc['Alice']:\n{df_labeled.loc['Alice']}\n")
print(f"df_labeled.loc['Alice', 'salary']: {df_labeled.loc['Alice', 'salary']}\n")
print(f"df_labeled.loc['Alice':'Charlie']:\n{df_labeled.loc['Alice':'Charlie']}\n")
print(f"df_labeled.loc[:, ['age', 'salary']]:\n{df_labeled.loc[:, ['age', 'salary']]}")

# ========== FILTERING DATA ==========
print("\n" + "=" * 60)
print("FILTERING DATA")
print("=" * 60)

print(f"DataFrame:\n{df}\n")

# Single condition
print(f"df[df['age'] > 28]:\n{df[df['age'] > 28]}\n")

# Multiple conditions (use & for AND, | for OR)
print(f"df[(df['age'] > 25) & (df['city'] == 'NYC')]:")
print(df[(df['age'] > 25) & (df['city'] == 'NYC')])
print()

print(f"df[(df['city'] == 'NYC') | (df['city'] == 'LA')]:")
print(df[(df['city'] == 'NYC') | (df['city'] == 'LA')])
print()

# Using isin()
print(f"df[df['city'].isin(['NYC', 'SF'])]:")
print(df[df['city'].isin(['NYC', 'SF'])])
print()

# Using query() - cleaner syntax
print(f"df.query('age > 28 and salary > 55000'):")
print(df.query('age > 28 and salary > 55000'))

# ========== ADDING & MODIFYING COLUMNS ==========
print("\n" + "=" * 60)
print("ADDING & MODIFYING COLUMNS")
print("=" * 60)

# Copy to avoid modifying original
df_copy = df.copy()
print(f"Original:\n{df_copy}\n")

# Add new column
df_copy['bonus'] = df_copy['salary'] * 0.1
print(f"After adding 'bonus' column:\n{df_copy}\n")

# Modify existing column
df_copy['age'] = df_copy['age'] + 1
print(f"After adding 1 to 'age':\n{df_copy}\n")

# Conditional column
df_copy['senior'] = df_copy['age'] > 30
print(f"After adding 'senior' boolean:\n{df_copy}\n")

# Using apply() for custom functions
df_copy['age_group'] = df_copy['age'].apply(
    lambda x: 'young' if x < 30 else 'middle' if x < 35 else 'senior'
)
print(f"After adding 'age_group':\n{df_copy}")

# ========== DROPPING COLUMNS & ROWS ==========
print("\n" + "=" * 60)
print("DROPPING COLUMNS & ROWS")
print("=" * 60)

df_drop = df.copy()
print(f"Original:\n{df_drop}\n")

# Drop column
df_dropped = df_drop.drop('salary', axis=1)
print(f"After dropping 'salary' column:\n{df_dropped}\n")

# Drop multiple columns
df_dropped = df_drop.drop(['salary', 'city'], axis=1)
print(f"After dropping multiple columns:\n{df_dropped}\n")

# Drop rows by index
df_dropped = df_drop.drop([0, 2])
print(f"After dropping rows 0 and 2:\n{df_dropped}")

# ========== SORTING ==========
print("\n" + "=" * 60)
print("SORTING")
print("=" * 60)

print(f"Original:\n{df}\n")

# Sort by column
print(f"Sorted by age:\n{df.sort_values('age')}\n")

# Sort descending
print(f"Sorted by salary (descending):\n{df.sort_values('salary', ascending=False)}\n")

# Sort by multiple columns
print(f"Sorted by city, then age:\n{df.sort_values(['city', 'age'])}")

# ========== RENAME COLUMNS ==========
print("\n" + "=" * 60)
print("RENAME COLUMNS")
print("=" * 60)

df_renamed = df.copy()
print(f"Original columns: {list(df_renamed.columns)}")

# Rename specific columns
df_renamed = df_renamed.rename(columns={'name': 'full_name', 'city': 'location'})
print(f"After rename: {list(df_renamed.columns)}")

# Rename all columns
df_renamed.columns = ['Name', 'Age', 'Location', 'Salary']
print(f"After changing all: {list(df_renamed.columns)}")

# ========== BASIC STATISTICS ==========
print("\n" + "=" * 60)
print("BASIC STATISTICS")
print("=" * 60)

print(f"DataFrame:\n{df}\n")

# Numerical columns only
print(f"Mean:\n{df[['age', 'salary']].mean()}\n")
print(f"Sum: {df['salary'].sum()}")
print(f"Min: {df['age'].min()}")
print(f"Max: {df['salary'].max()}")
print(f"Median: {df['age'].median()}")
print(f"Std: {df['salary'].std():.2f}")

# Value counts
print(f"\nValue counts for 'city':\n{df['city'].value_counts()}")

# Unique values
print(f"\nUnique cities: {df['city'].unique()}")
print(f"Number of unique cities: {df['city'].nunique()}")

# ========== PRACTICAL EXAMPLE ==========
print("\n" + "=" * 60)
print("PRACTICAL EXAMPLE: Employee Analysis")
print("=" * 60)

# Create employee data
employees = pd.DataFrame({
    'emp_id': [101, 102, 103, 104, 105, 106, 107, 108],
    'name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank', 'Grace', 'Henry'],
    'department': ['IT', 'HR', 'IT', 'Finance', 'HR', 'IT', 'Finance', 'IT'],
    'salary': [75000, 55000, 80000, 70000, 52000, 85000, 72000, 78000],
    'years': [3, 5, 7, 4, 2, 8, 6, 4]
})

print(f"Employee Data:\n{employees}\n")

# Analysis
print("Analysis:")
print(f"   Total employees: {len(employees)}")
print(f"   Average salary: ${employees['salary'].mean():.2f}")
print(f"   Salary range: ${employees['salary'].min()} - ${employees['salary'].max()}")
print(f"\n   Employees by department:\n{employees['department'].value_counts()}")
print(f"\n   IT employees:\n{employees[employees['department'] == 'IT']}")
print(f"\n   High earners (>70000):\n{employees[employees['salary'] > 70000][['name', 'salary']]}")

# Calculate salary per year
employees['salary_per_year'] = (employees['salary'] / employees['years']).round(2)
print(f"\n   With salary per year of experience:\n{employees[['name', 'salary', 'years', 'salary_per_year']]}")

print("\n" + "=" * 60)
print("✅ Pandas DataFrames Basics - Complete!")
print("=" * 60)
