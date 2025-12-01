"""
Day 22 - Data Loading
=====================
Learn: Loading data from various file formats

Key Concepts:
- CSV files (most common)
- Excel files
- JSON files
- SQL databases (overview)
- Handling different delimiters and encodings
"""

import pandas as pd
import numpy as np
import os
import json

print("=" * 60)
print("DATA LOADING")
print("=" * 60)

# ========== CREATE SAMPLE FILES ==========
print("\n" + "=" * 60)
print("CREATING SAMPLE FILES FOR PRACTICE")
print("=" * 60)

# Create sample data
sample_data = pd.DataFrame({
    'id': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'age': [25, 30, 35, 28, 32],
    'salary': [50000, 60000, 75000, 55000, 65000],
    'department': ['IT', 'HR', 'IT', 'Finance', 'HR']
})

# Save as CSV
sample_data.to_csv('sample_data.csv', index=False)
print("✅ Created sample_data.csv")

# Save as JSON
sample_data.to_json('sample_data.json', orient='records', indent=2)
print("✅ Created sample_data.json")

# Save as Excel (if openpyxl is installed)
try:
    sample_data.to_excel('sample_data.xlsx', index=False, sheet_name='Employees')
    print("✅ Created sample_data.xlsx")
except ImportError:
    print("⚠️  Excel export requires: pip install openpyxl")

# Create CSV with different separator
sample_data.to_csv('sample_semicolon.csv', index=False, sep=';')
print("✅ Created sample_semicolon.csv (semicolon separated)")

# ========== READING CSV FILES ==========
print("\n" + "=" * 60)
print("READING CSV FILES")
print("=" * 60)

# Basic read
print("\n1. Basic CSV read:")
df = pd.read_csv('sample_data.csv')
print(df)

# With parameters
print("\n2. Read with parameters:")
print("""
Common parameters:
- sep/delimiter: Column separator (default: ',')
- header: Row number for headers (default: 0)
- names: Custom column names
- index_col: Column to use as index
- usecols: Specific columns to read
- dtype: Data types for columns
- nrows: Number of rows to read
- skiprows: Rows to skip
- na_values: Values to treat as NaN
- encoding: File encoding (utf-8, latin-1, etc.)
""")

# Using specific columns
df_subset = pd.read_csv('sample_data.csv', usecols=['name', 'age', 'salary'])
print(f"Reading specific columns:\n{df_subset}\n")

# Using nrows
df_partial = pd.read_csv('sample_data.csv', nrows=3)
print(f"Reading only 3 rows:\n{df_partial}\n")

# Reading semicolon-separated file
df_semi = pd.read_csv('sample_semicolon.csv', sep=';')
print(f"Reading semicolon-separated:\n{df_semi}")

# ========== HANDLING DIFFERENT FORMATS ==========
print("\n" + "=" * 60)
print("HANDLING DIFFERENT CSV FORMATS")
print("=" * 60)

# Create a messy CSV for demonstration
messy_csv = """# This is a comment line
name,age,salary,notes
Alice,25,50000,Good performer
Bob,30,N/A,Needs improvement
Charlie,35,75000,"Excellent, top performer"
Diana,,55000,New hire
Eve,32,65000,"""

with open('messy_data.csv', 'w') as f:
    f.write(messy_csv)

print("Messy CSV content:")
print(messy_csv)

# Read with options to handle mess
df_messy = pd.read_csv(
    'messy_data.csv',
    comment='#',           # Skip comment lines
    na_values=['N/A', ''], # Treat as NaN
    skip_blank_lines=True
)
print(f"\nCleaned read result:\n{df_messy}")

# ========== READING EXCEL FILES ==========
print("\n" + "=" * 60)
print("READING EXCEL FILES")
print("=" * 60)

try:
    # Basic read
    df_excel = pd.read_excel('sample_data.xlsx')
    print(f"Basic Excel read:\n{df_excel}\n")
    
    # With sheet name
    df_excel = pd.read_excel('sample_data.xlsx', sheet_name='Employees')
    print(f"Reading specific sheet:\n{df_excel}\n")
    
    print("""
Common Excel parameters:
- sheet_name: Sheet name or index (default: 0)
- header: Row for headers
- usecols: Columns to read (e.g., 'A:C' or [0, 1, 2])
- skiprows: Rows to skip
- nrows: Number of rows to read
- dtype: Data types
""")
except ImportError:
    print("⚠️  Excel reading requires: pip install openpyxl")
except FileNotFoundError:
    print("⚠️  Excel file not found")

# ========== READING JSON FILES ==========
print("\n" + "=" * 60)
print("READING JSON FILES")
print("=" * 60)

# Read JSON
df_json = pd.read_json('sample_data.json')
print(f"JSON read result:\n{df_json}\n")

# Create nested JSON
nested_json = {
    'company': 'TechCorp',
    'employees': [
        {'name': 'Alice', 'age': 25, 'skills': ['Python', 'SQL']},
        {'name': 'Bob', 'age': 30, 'skills': ['Java', 'AWS']},
    ]
}

with open('nested_data.json', 'w') as f:
    json.dump(nested_json, f, indent=2)

print("Nested JSON content:")
print(json.dumps(nested_json, indent=2))

# Read nested JSON
with open('nested_data.json', 'r') as f:
    nested = json.load(f)
    df_employees = pd.DataFrame(nested['employees'])
    print(f"\nExtracted employees:\n{df_employees}")

# Using json_normalize for nested data
from pandas import json_normalize
df_normalized = json_normalize(nested, 'employees')
print(f"\nUsing json_normalize:\n{df_normalized}")

# ========== WRITING FILES ==========
print("\n" + "=" * 60)
print("WRITING FILES")
print("=" * 60)

output_df = pd.DataFrame({
    'product': ['Laptop', 'Phone', 'Tablet'],
    'price': [999.99, 699.99, 449.99],
    'quantity': [50, 100, 75]
})

# Write CSV
output_df.to_csv('output.csv', index=False)
print("✅ Saved to output.csv")

# Write with index
output_df.to_csv('output_with_index.csv', index=True)
print("✅ Saved to output_with_index.csv (with index)")

# Write specific columns
output_df.to_csv('output_subset.csv', columns=['product', 'price'], index=False)
print("✅ Saved subset to output_subset.csv")

# Write JSON
output_df.to_json('output.json', orient='records', indent=2)
print("✅ Saved to output.json")

# Write Excel
try:
    output_df.to_excel('output.xlsx', index=False, sheet_name='Products')
    print("✅ Saved to output.xlsx")
except ImportError:
    print("⚠️  Excel export requires: pip install openpyxl")

# Show file contents
print("\nContent of output.csv:")
with open('output.csv', 'r') as f:
    print(f.read())

# ========== READING FROM URL ==========
print("\n" + "=" * 60)
print("READING FROM URL (Example)")
print("=" * 60)

print("""
Pandas can read directly from URLs:

# Read CSV from URL
url = 'https://example.com/data.csv'
df = pd.read_csv(url)

# Read JSON from URL
url = 'https://api.example.com/data.json'
df = pd.read_json(url)

This works with any public URL that returns valid data.
""")

# ========== CHUNKED READING FOR LARGE FILES ==========
print("\n" + "=" * 60)
print("CHUNKED READING FOR LARGE FILES")
print("=" * 60)

print("""
For large files, read in chunks to save memory:

# Read in chunks
chunk_size = 10000
chunks = []
for chunk in pd.read_csv('large_file.csv', chunksize=chunk_size):
    # Process each chunk
    processed = chunk[chunk['value'] > 100]
    chunks.append(processed)

# Combine results
result = pd.concat(chunks)

This is useful when:
- File is too large for memory
- You only need a subset of data
- Processing can be done incrementally
""")

# ========== PRACTICAL EXAMPLE ==========
print("\n" + "=" * 60)
print("PRACTICAL EXAMPLE: Load and Initial Exploration")
print("=" * 60)

# Create a more realistic dataset
np.random.seed(42)
n_rows = 100

sales_data = pd.DataFrame({
    'date': pd.date_range('2024-01-01', periods=n_rows, freq='D'),
    'product': np.random.choice(['Laptop', 'Phone', 'Tablet', 'Watch'], n_rows),
    'region': np.random.choice(['North', 'South', 'East', 'West'], n_rows),
    'units': np.random.randint(1, 50, n_rows),
    'unit_price': np.random.uniform(100, 1000, n_rows).round(2)
})
sales_data['revenue'] = (sales_data['units'] * sales_data['unit_price']).round(2)

# Save it
sales_data.to_csv('sales_data.csv', index=False)
print("✅ Created sales_data.csv with 100 rows\n")

# Load and explore
df = pd.read_csv('sales_data.csv', parse_dates=['date'])
print("Data loaded from sales_data.csv")
print(f"\nShape: {df.shape}")
print(f"\nFirst 5 rows:\n{df.head()}")
print(f"\nData types:\n{df.dtypes}")
print(f"\nBasic statistics:\n{df.describe()}")
print(f"\nUnique products: {df['product'].unique()}")
print(f"Unique regions: {df['region'].unique()}")

# ========== CLEANUP ==========
print("\n" + "=" * 60)
print("CLEANUP")
print("=" * 60)

# Clean up created files
files_to_remove = [
    'sample_data.csv', 'sample_data.json', 'sample_data.xlsx',
    'sample_semicolon.csv', 'messy_data.csv', 'nested_data.json',
    'output.csv', 'output_with_index.csv', 'output_subset.csv',
    'output.json', 'output.xlsx', 'sales_data.csv'
]

for f in files_to_remove:
    if os.path.exists(f):
        os.remove(f)
        print(f"✅ Removed {f}")

print("\n" + "=" * 60)
print("✅ Data Loading - Complete!")
print("=" * 60)
