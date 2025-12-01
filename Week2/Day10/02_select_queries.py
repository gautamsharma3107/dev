"""
Day 10 - SELECT Queries
========================
Learn: SELECT, WHERE, ORDER BY, LIMIT

Key Concepts:
- SELECT: Choose which columns to retrieve
- WHERE: Filter rows based on conditions
- ORDER BY: Sort results
- LIMIT: Restrict number of results
"""

import sqlite3

# ========== SETUP DATABASE ==========
print("=" * 60)
print("SETUP: Creating Sample Database")
print("=" * 60)

conn = sqlite3.connect(':memory:')
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

# Create users table
cursor.execute("""
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE,
        age INTEGER,
        city TEXT,
        salary REAL,
        department TEXT,
        active INTEGER DEFAULT 1
    )
""")

# Insert sample data
users_data = [
    ("Alice Johnson", "alice@email.com", 28, "New York", 75000, "Engineering", 1),
    ("Bob Smith", "bob@email.com", 35, "Los Angeles", 85000, "Engineering", 1),
    ("Charlie Brown", "charlie@email.com", 22, "Chicago", 55000, "Marketing", 1),
    ("Diana Ross", "diana@email.com", 31, "Houston", 90000, "Engineering", 1),
    ("Eve Wilson", "eve@email.com", 27, "Phoenix", 62000, "Sales", 1),
    ("Frank Miller", "frank@email.com", 40, "New York", 95000, "Management", 1),
    ("Grace Lee", "grace@email.com", 29, "Chicago", 72000, "Marketing", 0),
    ("Henry Davis", "henry@email.com", 33, "Miami", 78000, "Sales", 1),
    ("Ivy Chen", "ivy@email.com", 25, "Seattle", 68000, "Engineering", 1),
    ("Jack Brown", "jack@email.com", 45, "Denver", 110000, "Management", 1),
    ("Kate Williams", "kate@email.com", 30, "New York", 82000, "Engineering", 1),
    ("Leo Martinez", "leo@email.com", 26, "Chicago", 58000, "Marketing", 0),
]

cursor.executemany("""
    INSERT INTO users (name, email, age, city, salary, department, active)
    VALUES (?, ?, ?, ?, ?, ?, ?)
""", users_data)
conn.commit()
print(f"✅ Created 'users' table with {len(users_data)} records\n")

# ========== BASIC SELECT ==========
print("=" * 60)
print("BASIC SELECT STATEMENTS")
print("=" * 60)

# Select all columns
print("\n1. SELECT * (All columns):")
print("-" * 40)
cursor.execute("SELECT * FROM users LIMIT 3")
for row in cursor.fetchall():
    print(f"   {row['id']}. {row['name']} | {row['email']} | Age: {row['age']}")

# Select specific columns
print("\n2. SELECT specific columns:")
print("-" * 40)
cursor.execute("SELECT name, department, salary FROM users LIMIT 5")
for row in cursor.fetchall():
    print(f"   {row['name']} - {row['department']} (${row['salary']:,.0f})")

# Select with alias
print("\n3. SELECT with column alias (AS):")
print("-" * 40)
cursor.execute("""
    SELECT name AS full_name, salary AS annual_salary 
    FROM users LIMIT 3
""")
for row in cursor.fetchall():
    print(f"   {row['full_name']}: ${row['annual_salary']:,.0f}")

# Select DISTINCT
print("\n4. SELECT DISTINCT (unique values):")
print("-" * 40)
cursor.execute("SELECT DISTINCT city FROM users")
cities = [row['city'] for row in cursor.fetchall()]
print(f"   Unique cities: {', '.join(cities)}")

cursor.execute("SELECT DISTINCT department FROM users")
departments = [row['department'] for row in cursor.fetchall()]
print(f"   Unique departments: {', '.join(departments)}")

# ========== WHERE CLAUSE ==========
print("\n" + "=" * 60)
print("WHERE CLAUSE (Filtering)")
print("=" * 60)

# Basic comparison
print("\n1. Basic comparison operators:")
print("-" * 40)

# Equal to
print("   Users from New York:")
cursor.execute("SELECT name FROM users WHERE city = 'New York'")
for row in cursor.fetchall():
    print(f"      - {row['name']}")

# Greater than
print("\n   Users older than 30:")
cursor.execute("SELECT name, age FROM users WHERE age > 30")
for row in cursor.fetchall():
    print(f"      - {row['name']} (Age: {row['age']})")

# Less than or equal
print("\n   Users with salary <= $70,000:")
cursor.execute("SELECT name, salary FROM users WHERE salary <= 70000")
for row in cursor.fetchall():
    print(f"      - {row['name']}: ${row['salary']:,.0f}")

# Not equal
print("\n   Users NOT in Engineering:")
cursor.execute("SELECT name, department FROM users WHERE department <> 'Engineering'")
for row in cursor.fetchall():
    print(f"      - {row['name']} ({row['department']})")

# ========== LOGICAL OPERATORS ==========
print("\n" + "=" * 60)
print("LOGICAL OPERATORS (AND, OR, NOT)")
print("=" * 60)

# AND
print("\n1. AND - Both conditions must be true:")
print("-" * 40)
cursor.execute("""
    SELECT name, age, city FROM users 
    WHERE age > 25 AND city = 'New York'
""")
for row in cursor.fetchall():
    print(f"   {row['name']} - Age {row['age']} in {row['city']}")

# OR
print("\n2. OR - Either condition can be true:")
print("-" * 40)
cursor.execute("""
    SELECT name, department FROM users 
    WHERE department = 'Engineering' OR department = 'Marketing'
""")
for row in cursor.fetchall():
    print(f"   {row['name']} - {row['department']}")

# NOT
print("\n3. NOT - Negates condition:")
print("-" * 40)
cursor.execute("""
    SELECT name, active FROM users 
    WHERE NOT active
""")
print("   Inactive users:")
for row in cursor.fetchall():
    print(f"      - {row['name']}")

# Complex condition
print("\n4. Complex conditions (combined):")
print("-" * 40)
cursor.execute("""
    SELECT name, age, salary, department FROM users 
    WHERE (age > 25 AND salary > 70000) OR department = 'Management'
""")
for row in cursor.fetchall():
    print(f"   {row['name']} - Age {row['age']}, ${row['salary']:,.0f} ({row['department']})")

# ========== BETWEEN AND IN ==========
print("\n" + "=" * 60)
print("BETWEEN AND IN")
print("=" * 60)

# BETWEEN
print("\n1. BETWEEN - Range of values:")
print("-" * 40)
cursor.execute("""
    SELECT name, age FROM users 
    WHERE age BETWEEN 25 AND 32
    ORDER BY age
""")
print("   Users aged 25-32:")
for row in cursor.fetchall():
    print(f"      - {row['name']} (Age: {row['age']})")

cursor.execute("""
    SELECT name, salary FROM users 
    WHERE salary BETWEEN 60000 AND 80000
    ORDER BY salary
""")
print("\n   Salary between $60K-$80K:")
for row in cursor.fetchall():
    print(f"      - {row['name']}: ${row['salary']:,.0f}")

# IN
print("\n2. IN - Match any value in list:")
print("-" * 40)
cursor.execute("""
    SELECT name, city FROM users 
    WHERE city IN ('New York', 'Chicago', 'Miami')
""")
print("   Users in NYC, Chicago, or Miami:")
for row in cursor.fetchall():
    print(f"      - {row['name']} ({row['city']})")

# ========== LIKE (Pattern Matching) ==========
print("\n" + "=" * 60)
print("LIKE (Pattern Matching)")
print("=" * 60)

print("""
Wildcards:
- %  matches any sequence of characters
- _  matches any single character
""")

# Starts with
print("\n1. Names starting with 'J':")
print("-" * 40)
cursor.execute("SELECT name FROM users WHERE name LIKE 'J%'")
for row in cursor.fetchall():
    print(f"   - {row['name']}")

# Ends with
print("\n2. Names ending with 'son':")
print("-" * 40)
cursor.execute("SELECT name FROM users WHERE name LIKE '%son'")
for row in cursor.fetchall():
    print(f"   - {row['name']}")

# Contains
print("\n3. Names containing 'e' (lowercase):")
print("-" * 40)
cursor.execute("SELECT name FROM users WHERE name LIKE '%e%'")
for row in cursor.fetchall():
    print(f"   - {row['name']}")

# Single character
print("\n4. Emails with pattern '_ve@email.com':")
print("-" * 40)
cursor.execute("SELECT name, email FROM users WHERE email LIKE '_ve@email.com'")
for row in cursor.fetchall():
    print(f"   - {row['name']}: {row['email']}")

# ========== ORDER BY ==========
print("\n" + "=" * 60)
print("ORDER BY (Sorting)")
print("=" * 60)

# Ascending (default)
print("\n1. ORDER BY name (ascending - default):")
print("-" * 40)
cursor.execute("SELECT name FROM users ORDER BY name LIMIT 5")
for row in cursor.fetchall():
    print(f"   - {row['name']}")

# Descending
print("\n2. ORDER BY age DESC (descending):")
print("-" * 40)
cursor.execute("SELECT name, age FROM users ORDER BY age DESC LIMIT 5")
print("   Top 5 oldest users:")
for row in cursor.fetchall():
    print(f"   - {row['name']} (Age: {row['age']})")

# Multiple columns
print("\n3. ORDER BY multiple columns (department, salary DESC):")
print("-" * 40)
cursor.execute("""
    SELECT name, department, salary FROM users 
    ORDER BY department ASC, salary DESC
""")
for row in cursor.fetchall():
    print(f"   {row['department']}: {row['name']} - ${row['salary']:,.0f}")

# ========== LIMIT AND OFFSET ==========
print("\n" + "=" * 60)
print("LIMIT AND OFFSET (Pagination)")
print("=" * 60)

# Basic LIMIT
print("\n1. LIMIT - Get first N rows:")
print("-" * 40)
cursor.execute("SELECT name, salary FROM users ORDER BY salary DESC LIMIT 3")
print("   Top 3 highest salaries:")
for row in cursor.fetchall():
    print(f"   - {row['name']}: ${row['salary']:,.0f}")

# LIMIT with OFFSET
print("\n2. LIMIT with OFFSET (skip rows):")
print("-" * 40)
cursor.execute("SELECT name FROM users ORDER BY name LIMIT 3 OFFSET 0")
print("   Page 1 (offset 0):")
for row in cursor.fetchall():
    print(f"   - {row['name']}")

cursor.execute("SELECT name FROM users ORDER BY name LIMIT 3 OFFSET 3")
print("\n   Page 2 (offset 3):")
for row in cursor.fetchall():
    print(f"   - {row['name']}")

cursor.execute("SELECT name FROM users ORDER BY name LIMIT 3 OFFSET 6")
print("\n   Page 3 (offset 6):")
for row in cursor.fetchall():
    print(f"   - {row['name']}")

# ========== COMBINING EVERYTHING ==========
print("\n" + "=" * 60)
print("COMBINING CLAUSES")
print("=" * 60)

print("\n1. Complex query combining all clauses:")
print("-" * 40)
cursor.execute("""
    SELECT name, age, city, salary, department
    FROM users
    WHERE age >= 25 
      AND salary > 60000 
      AND active = 1
    ORDER BY salary DESC
    LIMIT 5
""")

print("   Active users, 25+, salary > $60K (Top 5 by salary):")
for row in cursor.fetchall():
    print(f"   - {row['name']} ({row['age']}) - {row['city']}")
    print(f"     ${row['salary']:,.0f} | {row['department']}")

# Close connection
conn.close()

print("\n" + "=" * 60)
print("✅ SELECT Queries - Complete!")
print("=" * 60)

print("""
Summary:
--------
1. SELECT columns FROM table - Basic retrieval
2. WHERE condition - Filter rows
3. AND, OR, NOT - Combine conditions
4. BETWEEN, IN - Range and list matching
5. LIKE with % and _ - Pattern matching
6. ORDER BY column ASC/DESC - Sort results
7. LIMIT N OFFSET M - Pagination
""")
