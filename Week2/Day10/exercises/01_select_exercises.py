"""
Day 10 - SQL Exercise 1: SELECT Queries
=======================================
Practice: Basic SELECT, WHERE, ORDER BY, LIMIT

Complete each exercise by writing the SQL query.
Run this file to see if your queries are correct!
"""

import sqlite3

# Setup database
conn = sqlite3.connect(':memory:')
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

# Create employees table
cursor.execute("""
    CREATE TABLE employees (
        id INTEGER PRIMARY KEY,
        name TEXT,
        department TEXT,
        salary REAL,
        hire_date TEXT,
        city TEXT
    )
""")

# Insert sample data
employees = [
    (1, 'Alice Johnson', 'Engineering', 85000, '2020-01-15', 'New York'),
    (2, 'Bob Smith', 'Marketing', 65000, '2019-03-20', 'Los Angeles'),
    (3, 'Charlie Brown', 'Engineering', 92000, '2018-06-10', 'Chicago'),
    (4, 'Diana Ross', 'Sales', 72000, '2021-02-01', 'Houston'),
    (5, 'Eve Wilson', 'Engineering', 78000, '2020-07-15', 'New York'),
    (6, 'Frank Miller', 'Marketing', 58000, '2022-01-10', 'Phoenix'),
    (7, 'Grace Lee', 'Sales', 81000, '2019-09-05', 'Chicago'),
    (8, 'Henry Davis', 'Engineering', 95000, '2017-11-20', 'Seattle'),
    (9, 'Ivy Chen', 'Marketing', 62000, '2021-04-15', 'New York'),
    (10, 'Jack Brown', 'Sales', 68000, '2020-08-01', 'Miami'),
]

cursor.executemany(
    "INSERT INTO employees VALUES (?, ?, ?, ?, ?, ?)",
    employees
)
conn.commit()

print("=" * 60)
print("SQL EXERCISE 1: SELECT Queries")
print("=" * 60)
print("\nTable: employees (id, name, department, salary, hire_date, city)")
print("-" * 60)

# ============================================================
# EXERCISE 1: Select all columns from employees table
# ============================================================
print("\n📝 Exercise 1: Select all employees")
print("-" * 40)

# YOUR QUERY HERE:
query1 = """
SELECT * FROM employees
"""

cursor.execute(query1)
results = cursor.fetchall()
print(f"Found {len(results)} employees")
for row in results[:3]:
    print(f"   {row['id']}. {row['name']} - {row['department']}")
print("   ...")

# ============================================================
# EXERCISE 2: Select only name and salary columns
# ============================================================
print("\n📝 Exercise 2: Select name and salary only")
print("-" * 40)

# YOUR QUERY HERE:
query2 = """
SELECT name, salary FROM employees
"""

cursor.execute(query2)
results = cursor.fetchall()
for row in results[:5]:
    print(f"   {row['name']}: ${row['salary']:,.0f}")

# ============================================================
# EXERCISE 3: Select employees from Engineering department
# ============================================================
print("\n📝 Exercise 3: Engineering department employees")
print("-" * 40)

# YOUR QUERY HERE:
query3 = """
SELECT name, department FROM employees WHERE department = 'Engineering'
"""

cursor.execute(query3)
results = cursor.fetchall()
for row in results:
    print(f"   {row['name']} - {row['department']}")

# ============================================================
# EXERCISE 4: Select employees with salary > $75,000
# ============================================================
print("\n📝 Exercise 4: Employees with salary > $75,000")
print("-" * 40)

# YOUR QUERY HERE:
query4 = """
SELECT name, salary FROM employees WHERE salary > 75000
"""

cursor.execute(query4)
results = cursor.fetchall()
for row in results:
    print(f"   {row['name']}: ${row['salary']:,.0f}")

# ============================================================
# EXERCISE 5: Select employees from New York OR Chicago
# ============================================================
print("\n📝 Exercise 5: Employees from New York or Chicago")
print("-" * 40)

# YOUR QUERY HERE:
query5 = """
SELECT name, city FROM employees WHERE city IN ('New York', 'Chicago')
"""

cursor.execute(query5)
results = cursor.fetchall()
for row in results:
    print(f"   {row['name']} - {row['city']}")

# ============================================================
# EXERCISE 6: Select all employees ordered by salary (highest first)
# ============================================================
print("\n📝 Exercise 6: Employees ordered by salary DESC")
print("-" * 40)

# YOUR QUERY HERE:
query6 = """
SELECT name, salary FROM employees ORDER BY salary DESC
"""

cursor.execute(query6)
results = cursor.fetchall()
for row in results[:5]:
    print(f"   {row['name']}: ${row['salary']:,.0f}")

# ============================================================
# EXERCISE 7: Select top 3 highest paid employees
# ============================================================
print("\n📝 Exercise 7: Top 3 highest paid employees")
print("-" * 40)

# YOUR QUERY HERE:
query7 = """
SELECT name, salary FROM employees ORDER BY salary DESC LIMIT 3
"""

cursor.execute(query7)
results = cursor.fetchall()
for i, row in enumerate(results, 1):
    print(f"   #{i} {row['name']}: ${row['salary']:,.0f}")

# ============================================================
# EXERCISE 8: Select employees whose name starts with 'J'
# ============================================================
print("\n📝 Exercise 8: Employees whose name starts with 'J'")
print("-" * 40)

# YOUR QUERY HERE:
query8 = """
SELECT name FROM employees WHERE name LIKE 'J%'
"""

cursor.execute(query8)
results = cursor.fetchall()
for row in results:
    print(f"   {row['name']}")

# ============================================================
# EXERCISE 9: Select employees hired between 2019 and 2020
# ============================================================
print("\n📝 Exercise 9: Employees hired in 2019-2020")
print("-" * 40)

# YOUR QUERY HERE:
query9 = """
SELECT name, hire_date FROM employees 
WHERE hire_date BETWEEN '2019-01-01' AND '2020-12-31'
ORDER BY hire_date
"""

cursor.execute(query9)
results = cursor.fetchall()
for row in results:
    print(f"   {row['name']}: {row['hire_date']}")

# ============================================================
# EXERCISE 10: Complex query - Engineering in NYC, salary > 80K
# ============================================================
print("\n📝 Exercise 10: Engineering employees in NYC with salary > $80K")
print("-" * 40)

# YOUR QUERY HERE:
query10 = """
SELECT name, department, city, salary 
FROM employees 
WHERE department = 'Engineering' 
  AND city = 'New York' 
  AND salary > 80000
"""

cursor.execute(query10)
results = cursor.fetchall()
if results:
    for row in results:
        print(f"   {row['name']}: {row['department']}, {row['city']}, ${row['salary']:,.0f}")
else:
    print("   No employees match this criteria")

conn.close()

print("\n" + "=" * 60)
print("✅ Exercise 1 Complete!")
print("=" * 60)
print("""
Practice Tips:
- Try modifying the queries to explore different results
- Change the WHERE conditions
- Experiment with different ORDER BY columns
- Combine multiple conditions with AND/OR
""")
