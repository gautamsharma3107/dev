"""
DAY 22 ASSESSMENT TEST
======================
Total: 14 points
Pass: 10+ points (70%)
Time: 15 minutes
"""

print("=" * 60)
print("DAY 22 ASSESSMENT - NumPy & Pandas")
print("=" * 60)
print("Total Points: 14 | Passing Score: 10 (70%)")
print("=" * 60)

# ============================================================
# SECTION A: Multiple Choice Questions (6 points)
# ============================================================

print("\n" + "=" * 60)
print("SECTION A: Multiple Choice (6 points)")
print("=" * 60)

print("""
Q1. What does np.zeros((3, 4)) create?
a) A 1D array with 12 zeros
b) A 3x4 array filled with zeros
c) A 4x3 array filled with zeros
d) An error - invalid syntax

Your answer: """)

print("""
Q2. What is the result of arr[arr > 5] where arr = np.array([1, 6, 3, 8, 2, 9])?
a) [True, True, True]
b) [6, 8, 9]
c) [1, 3, 2]
d) [False, True, False, True, False, True]

Your answer: """)

print("""
Q3. Which method returns only the first 5 rows of a DataFrame?
a) df.first(5)
b) df.head(5)
c) df[0:5]
d) Both b and c

Your answer: """)

print("""
Q4. What does df.groupby('category')['price'].mean() return?
a) Average price for each category
b) Sum of all prices
c) Number of items per category
d) All prices in each category

Your answer: """)

print("""
Q5. Which method is used to handle missing values by filling them?
a) df.dropna()
b) df.fillna()
c) df.isna()
d) df.notna()

Your answer: """)

print("""
Q6. What is the correct way to merge two DataFrames on a common column?
a) df1.join(df2, on='id')
b) pd.merge(df1, df2, on='id')
c) df1 + df2
d) pd.concat([df1, df2])

Your answer: """)

# ============================================================
# SECTION B: Coding Challenges (6 points)
# ============================================================

print("\n" + "=" * 60)
print("SECTION B: Coding Challenges (6 points)")
print("=" * 60)

print("""
Q7. (2 points) Create a NumPy array with values [10, 20, 30, 40, 50].
    Then filter to get only values greater than 25.
    Print both the original and filtered array.
""")

# Write your code here:
import numpy as np
import pandas as pd




print("""
Q8. (2 points) Given this DataFrame:
    data = {'name': ['Alice', 'Bob', 'Charlie'], 
            'age': [25, 30, 35],
            'salary': [50000, 60000, 75000]}
    Create the DataFrame and calculate the average salary.
""")

# Write your code here:




print("""
Q9. (2 points) Given a sales DataFrame with columns ['product', 'region', 'revenue']:
    Write code to find the total revenue per region using groupby.
    
    (Use this sample data):
    sales = pd.DataFrame({
        'product': ['A', 'B', 'A', 'B'],
        'region': ['North', 'North', 'South', 'South'],
        'revenue': [100, 200, 150, 250]
    })
""")

# Write your code here:




# ============================================================
# SECTION C: Conceptual Question (2 points)
# ============================================================

print("\n" + "=" * 60)
print("SECTION C: Conceptual Question (2 points)")
print("=" * 60)

print("""
Q10. (2 points) Explain the difference between:
     - iloc (integer-location based indexing)
     - loc (label-based indexing)
     
     Give one example of when you would use each.

Your answer:
""")

# Write your explanation here as comments:
# 




print("\n" + "=" * 60)
print("TEST COMPLETE!")
print("=" * 60)

"""
ANSWER KEY
==========

Section A:
Q1: b) A 3x4 array filled with zeros
Q2: b) [6, 8, 9]
Q3: d) Both b and c
Q4: a) Average price for each category
Q5: b) df.fillna()
Q6: b) pd.merge(df1, df2, on='id')

Section B:
Q7:
import numpy as np
arr = np.array([10, 20, 30, 40, 50])
filtered = arr[arr > 25]
print(f"Original: {arr}")
print(f"Filtered: {filtered}")

Q8:
import pandas as pd
data = {'name': ['Alice', 'Bob', 'Charlie'], 
        'age': [25, 30, 35],
        'salary': [50000, 60000, 75000]}
df = pd.DataFrame(data)
avg_salary = df['salary'].mean()
print(f"Average salary: {avg_salary}")

Q9:
sales = pd.DataFrame({
    'product': ['A', 'B', 'A', 'B'],
    'region': ['North', 'North', 'South', 'South'],
    'revenue': [100, 200, 150, 250]
})
revenue_by_region = sales.groupby('region')['revenue'].sum()
print(revenue_by_region)

Section C:
Q10:
iloc uses integer positions (0, 1, 2, etc.) to select data.
loc uses labels (row/column names) to select data.

Example:
- iloc: df.iloc[0] gets the first row by position
- loc: df.loc['Alice'] gets the row with index label 'Alice'

Use iloc when you know the position/index number.
Use loc when you want to select by name/label.
"""
