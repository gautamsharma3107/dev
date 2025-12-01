# Day 22 Quick Reference Cheat Sheet

## NumPy Basics

### Creating Arrays
```python
import numpy as np

# From Python lists
arr = np.array([1, 2, 3, 4, 5])
arr_2d = np.array([[1, 2], [3, 4]])

# Special arrays
zeros = np.zeros((3, 4))       # 3x4 zeros
ones = np.ones((2, 3))         # 2x3 ones
empty = np.empty((2, 2))       # Uninitialized
full = np.full((3, 3), 7)      # Fill with 7
eye = np.eye(3)                # 3x3 identity

# Ranges
range_arr = np.arange(0, 10, 2)        # [0, 2, 4, 6, 8]
linspace = np.linspace(0, 1, 5)        # 5 evenly spaced
random_arr = np.random.rand(3, 3)      # Random 3x3
random_int = np.random.randint(0, 10, (3, 3))  # Random ints
```

### Array Properties
```python
arr.shape       # Dimensions
arr.dtype       # Data type
arr.ndim        # Number of dimensions
arr.size        # Total elements
arr.itemsize    # Bytes per element
```

### Array Operations
```python
# Element-wise operations
arr + 2         # Add 2 to all
arr * 3         # Multiply all by 3
arr1 + arr2     # Element-wise addition
arr1 * arr2     # Element-wise multiplication

# Math functions
np.sqrt(arr)    # Square root
np.exp(arr)     # Exponential
np.log(arr)     # Natural log
np.sin(arr)     # Sine

# Aggregations
arr.sum()       # Sum all elements
arr.mean()      # Average
arr.std()       # Standard deviation
arr.min()       # Minimum
arr.max()       # Maximum
arr.argmax()    # Index of max
arr.cumsum()    # Cumulative sum
```

### Indexing and Slicing
```python
arr[0]          # First element
arr[-1]         # Last element
arr[1:4]        # Elements 1-3
arr[::2]        # Every other element

# 2D array
arr_2d[0, 1]    # Row 0, Col 1
arr_2d[0]       # First row
arr_2d[:, 0]    # First column
arr_2d[0:2, 1:3]  # Subarray
```

### Reshaping
```python
arr.reshape(3, 4)    # Reshape to 3x4
arr.flatten()        # Flatten to 1D
arr.T                # Transpose
np.concatenate([a, b], axis=0)  # Join arrays
np.stack([a, b])     # Stack arrays
```

### Boolean Indexing
```python
arr[arr > 5]         # Elements > 5
arr[arr % 2 == 0]    # Even elements
np.where(arr > 5, arr, 0)  # Replace
```

---

## Pandas Basics

### Creating DataFrames
```python
import pandas as pd

# From dictionary
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['NYC', 'LA', 'SF']
})

# From list of dicts
df = pd.DataFrame([
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30}
])
```

### Loading Data
```python
# CSV
df = pd.read_csv('file.csv')
df = pd.read_csv('file.csv', sep=';', header=0)

# Excel
df = pd.read_excel('file.xlsx', sheet_name='Sheet1')

# JSON
df = pd.read_json('file.json')

# Save data
df.to_csv('output.csv', index=False)
df.to_excel('output.xlsx', index=False)
```

### Data Inspection
```python
df.head()           # First 5 rows
df.tail()           # Last 5 rows
df.shape            # (rows, cols)
df.info()           # Column types and memory
df.describe()       # Statistics
df.columns          # Column names
df.dtypes           # Data types
df.isnull().sum()   # Missing values per column
```

### Selection
```python
# Single column
df['name']          # Series
df[['name', 'age']] # DataFrame

# By position
df.iloc[0]          # First row
df.iloc[0:3]        # First 3 rows
df.iloc[0, 1]       # Row 0, Col 1
df.iloc[:, 0:2]     # All rows, first 2 cols

# By label
df.loc[0]           # Row with index 0
df.loc[0, 'name']   # Specific cell
df.loc[:, ['name', 'age']]  # Specific columns
```

### Filtering
```python
# Conditional filtering
df[df['age'] > 25]
df[df['city'] == 'NYC']
df[(df['age'] > 25) & (df['city'] == 'NYC')]
df[df['city'].isin(['NYC', 'LA'])]

# Query syntax
df.query('age > 25 and city == "NYC"')
```

### Data Cleaning
```python
# Handle missing values
df.dropna()                      # Drop rows with NaN
df.dropna(subset=['col'])        # Drop if col is NaN
df.fillna(0)                     # Fill NaN with 0
df.fillna({'col': 0})            # Fill specific column
df['col'].fillna(df['col'].mean())  # Fill with mean

# Duplicates
df.drop_duplicates()
df.drop_duplicates(subset=['col'])

# Data types
df['col'] = df['col'].astype(int)
df['date'] = pd.to_datetime(df['date'])

# Rename columns
df.rename(columns={'old': 'new'})
df.columns = ['col1', 'col2', 'col3']
```

### Grouping & Aggregation
```python
# Group by
df.groupby('city').mean()
df.groupby('city')['age'].mean()
df.groupby(['city', 'status']).agg({'age': 'mean', 'salary': 'sum'})

# Aggregation functions
df.groupby('city').agg({
    'age': ['mean', 'min', 'max'],
    'salary': 'sum'
})

# Value counts
df['city'].value_counts()
```

### Sorting
```python
df.sort_values('age')                    # Ascending
df.sort_values('age', ascending=False)   # Descending
df.sort_values(['city', 'age'])          # Multiple columns
df.sort_index()                          # Sort by index
```

### Adding/Modifying Columns
```python
df['new_col'] = df['age'] * 2            # New column
df['category'] = df['age'].apply(lambda x: 'young' if x < 30 else 'old')
df['full_name'] = df['first'] + ' ' + df['last']
df.drop('col', axis=1, inplace=True)     # Drop column
```

### Merging & Joining
```python
# Merge (SQL-like join)
pd.merge(df1, df2, on='id')
pd.merge(df1, df2, on='id', how='left')  # left, right, outer, inner

# Concatenate
pd.concat([df1, df2])                    # Stack vertically
pd.concat([df1, df2], axis=1)            # Stack horizontally
```

### Quick Stats
```python
df['col'].mean()     # Average
df['col'].median()   # Median
df['col'].std()      # Standard deviation
df['col'].sum()      # Sum
df['col'].min()      # Minimum
df['col'].max()      # Maximum
df['col'].unique()   # Unique values
df['col'].nunique()  # Count unique
```

---
**Keep this handy for Day 22 topics!** 🚀
