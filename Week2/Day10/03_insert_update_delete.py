"""
Day 10 - INSERT, UPDATE, DELETE
================================
Learn: Data manipulation operations in SQL

Key Concepts:
- INSERT: Add new data to tables
- UPDATE: Modify existing data
- DELETE: Remove data from tables
- Transactions and safety practices
"""

import sqlite3

# ========== SETUP DATABASE ==========
print("=" * 60)
print("SETUP: Creating Sample Database")
print("=" * 60)

conn = sqlite3.connect(':memory:')
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

# Create employees table
cursor.execute("""
    CREATE TABLE employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE,
        department TEXT,
        salary REAL,
        hire_date TEXT,
        active INTEGER DEFAULT 1
    )
""")
print("✅ Created 'employees' table\n")

# ========== INSERT STATEMENTS ==========
print("=" * 60)
print("INSERT STATEMENTS")
print("=" * 60)

# 1. Basic INSERT
print("\n1. Basic INSERT (specifying columns):")
print("-" * 40)

cursor.execute("""
    INSERT INTO employees (name, email, department, salary, hire_date)
    VALUES ('Alice Johnson', 'alice@company.com', 'Engineering', 75000, '2022-01-15')
""")
conn.commit()
print("   Inserted: Alice Johnson")

# 2. INSERT without specifying columns (all values)
print("\n2. INSERT without column names (provide all values):")
print("-" * 40)
cursor.execute("""
    INSERT INTO employees VALUES (NULL, 'Bob Smith', 'bob@company.com', 'Marketing', 65000, '2022-03-20', 1)
""")
conn.commit()
print("   Inserted: Bob Smith (using NULL for auto-increment ID)")

# 3. INSERT multiple rows
print("\n3. INSERT multiple rows:")
print("-" * 40)

new_employees = [
    ('Charlie Brown', 'charlie@company.com', 'Engineering', 72000, '2022-05-10'),
    ('Diana Ross', 'diana@company.com', 'Sales', 68000, '2022-06-01'),
    ('Eve Wilson', 'eve@company.com', 'Marketing', 61000, '2022-07-15'),
    ('Frank Miller', 'frank@company.com', 'Engineering', 80000, '2021-11-01'),
    ('Grace Lee', 'grace@company.com', 'HR', 55000, '2023-01-10'),
]

cursor.executemany("""
    INSERT INTO employees (name, email, department, salary, hire_date)
    VALUES (?, ?, ?, ?, ?)
""", new_employees)
conn.commit()
print(f"   Inserted {len(new_employees)} employees")

# 4. INSERT with parameterized queries (SAFE!)
print("\n4. INSERT with parameters (prevents SQL injection):")
print("-" * 40)

# User input simulation
user_name = "Henry Davis"
user_email = "henry@company.com"
user_dept = "Finance"
user_salary = 70000
user_hire = "2023-02-01"

# SAFE way - using placeholders
cursor.execute("""
    INSERT INTO employees (name, email, department, salary, hire_date)
    VALUES (?, ?, ?, ?, ?)
""", (user_name, user_email, user_dept, user_salary, user_hire))
conn.commit()
print(f"   Safely inserted: {user_name}")

# Show all employees
print("\n📊 Current employees table:")
print("-" * 60)
cursor.execute("SELECT id, name, department, salary FROM employees")
for row in cursor.fetchall():
    print(f"   {row['id']}. {row['name']:<20} | {row['department']:<12} | ${row['salary']:,.0f}")

# 5. INSERT and get the new ID
print("\n5. Get the ID of the last inserted row:")
print("-" * 40)

cursor.execute("""
    INSERT INTO employees (name, email, department, salary, hire_date)
    VALUES ('Ivy Chen', 'ivy@company.com', 'Engineering', 73000, '2023-03-15')
""")
conn.commit()

new_id = cursor.lastrowid
print(f"   New employee ID: {new_id}")

# ========== UPDATE STATEMENTS ==========
print("\n" + "=" * 60)
print("UPDATE STATEMENTS")
print("=" * 60)

print("\n⚠️  IMPORTANT: Always use WHERE clause with UPDATE!")
print("    Without WHERE, ALL rows will be updated!\n")

# 1. Update single row
print("1. UPDATE single row:")
print("-" * 40)

# Check before update
cursor.execute("SELECT name, salary FROM employees WHERE id = 1")
before = cursor.fetchone()
print(f"   Before: {before['name']} - ${before['salary']:,.0f}")

# Update salary
cursor.execute("""
    UPDATE employees 
    SET salary = 80000 
    WHERE id = 1
""")
conn.commit()

# Check after update
cursor.execute("SELECT name, salary FROM employees WHERE id = 1")
after = cursor.fetchone()
print(f"   After: {after['name']} - ${after['salary']:,.0f}")
print("   ✅ Updated!")

# 2. Update multiple columns
print("\n2. UPDATE multiple columns:")
print("-" * 40)

cursor.execute("""
    UPDATE employees 
    SET department = 'Senior Engineering', salary = 85000 
    WHERE name = 'Frank Miller'
""")
conn.commit()

cursor.execute("SELECT name, department, salary FROM employees WHERE name = 'Frank Miller'")
row = cursor.fetchone()
print(f"   {row['name']}: {row['department']} - ${row['salary']:,.0f}")

# 3. Update with calculation
print("\n3. UPDATE with calculation (10% raise):")
print("-" * 40)

print("   Engineering department salaries before raise:")
cursor.execute("SELECT name, salary FROM employees WHERE department LIKE '%Engineering%'")
for row in cursor.fetchall():
    print(f"      - {row['name']}: ${row['salary']:,.0f}")

# Give 10% raise
cursor.execute("""
    UPDATE employees 
    SET salary = salary * 1.10 
    WHERE department LIKE '%Engineering%'
""")
conn.commit()

print("\n   After 10% raise:")
cursor.execute("SELECT name, salary FROM employees WHERE department LIKE '%Engineering%'")
for row in cursor.fetchall():
    print(f"      - {row['name']}: ${row['salary']:,.0f}")

# 4. Update based on condition
print("\n4. UPDATE based on multiple conditions:")
print("-" * 40)

cursor.execute("""
    UPDATE employees 
    SET active = 0 
    WHERE department = 'Marketing' AND salary < 63000
""")
conn.commit()
print(f"   Deactivated employees in Marketing with salary < $63,000")

cursor.execute("SELECT name, active FROM employees WHERE department = 'Marketing'")
for row in cursor.fetchall():
    status = "Active" if row['active'] else "Inactive"
    print(f"      - {row['name']}: {status}")

# 5. Count rows affected
print("\n5. Check rows affected by UPDATE:")
print("-" * 40)

cursor.execute("""
    UPDATE employees 
    SET department = 'Sales' 
    WHERE department = 'Sales'
""")
conn.commit()

print(f"   Rows affected: {cursor.rowcount}")

# ========== DELETE STATEMENTS ==========
print("\n" + "=" * 60)
print("DELETE STATEMENTS")
print("=" * 60)

print("\n⚠️  IMPORTANT: Always use WHERE clause with DELETE!")
print("    Without WHERE, ALL rows will be deleted!\n")

# Add some test data to delete
cursor.execute("""
    INSERT INTO employees (name, email, department, salary, hire_date, active)
    VALUES ('Test User 1', 'test1@company.com', 'Test', 40000, '2023-01-01', 0)
""")
cursor.execute("""
    INSERT INTO employees (name, email, department, salary, hire_date, active)
    VALUES ('Test User 2', 'test2@company.com', 'Test', 40000, '2023-01-01', 0)
""")
conn.commit()

# 1. Delete single row
print("1. DELETE single row:")
print("-" * 40)

cursor.execute("SELECT COUNT(*) as count FROM employees")
before_count = cursor.fetchone()['count']

cursor.execute("DELETE FROM employees WHERE email = 'test1@company.com'")
conn.commit()

cursor.execute("SELECT COUNT(*) as count FROM employees")
after_count = cursor.fetchone()['count']

print(f"   Before: {before_count} employees")
print(f"   After: {after_count} employees")
print(f"   Deleted: {before_count - after_count} row(s)")

# 2. Delete based on condition
print("\n2. DELETE based on condition:")
print("-" * 40)

cursor.execute("DELETE FROM employees WHERE department = 'Test'")
conn.commit()
print(f"   Deleted all employees in 'Test' department")
print(f"   Rows deleted: {cursor.rowcount}")

# 3. Delete inactive employees
print("\n3. DELETE inactive employees:")
print("-" * 40)

cursor.execute("SELECT name FROM employees WHERE active = 0")
inactive = cursor.fetchall()
print(f"   Inactive employees to delete: {[row['name'] for row in inactive]}")

cursor.execute("DELETE FROM employees WHERE active = 0")
conn.commit()
print(f"   Deleted {cursor.rowcount} inactive employees")

# ========== SAFE PRACTICES ==========
print("\n" + "=" * 60)
print("SAFE PRACTICES FOR DATA MODIFICATION")
print("=" * 60)

print("""
1. ALWAYS use WHERE clause with UPDATE and DELETE

   ❌ DANGEROUS:
   DELETE FROM users;          -- Deletes ALL rows!
   UPDATE users SET active=0;  -- Updates ALL rows!

   ✅ SAFE:
   DELETE FROM users WHERE id = 5;
   UPDATE users SET active=0 WHERE id = 5;

2. Use SELECT first to verify which rows will be affected:

   -- Before DELETE:
   SELECT * FROM users WHERE status = 'inactive';
   
   -- If the results look correct, then:
   DELETE FROM users WHERE status = 'inactive';

3. Use LIMIT with DELETE for safety:

   DELETE FROM users WHERE status = 'inactive' LIMIT 100;

4. Use transactions for multiple operations:

   BEGIN TRANSACTION;
   DELETE FROM orders WHERE user_id = 5;
   DELETE FROM users WHERE id = 5;
   COMMIT;  -- or ROLLBACK; if something goes wrong

5. Always use parameterized queries:

   ✅ cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
   ❌ cursor.execute(f"DELETE FROM users WHERE id = {user_id}")
""")

# ========== TRANSACTIONS ==========
print("\n" + "=" * 60)
print("TRANSACTIONS")
print("=" * 60)

# Demonstrate transactions
cursor.execute("""
    INSERT INTO employees (name, email, department, salary, hire_date)
    VALUES ('Jack Brown', 'jack@company.com', 'Engineering', 95000, '2023-04-01')
""")

try:
    # Start a transaction (implicit in sqlite3)
    cursor.execute("UPDATE employees SET salary = 100000 WHERE name = 'Jack Brown'")
    
    # Simulate checking if update is valid
    cursor.execute("SELECT salary FROM employees WHERE name = 'Jack Brown'")
    new_salary = cursor.fetchone()['salary']
    
    if new_salary > 150000:
        raise ValueError("Salary exceeds maximum allowed!")
    
    conn.commit()  # Save changes
    print("   ✅ Transaction committed successfully!")
    
except Exception as e:
    conn.rollback()  # Undo changes
    print(f"   ❌ Transaction rolled back: {e}")

# Final state
print("\n📊 Final employees table:")
print("-" * 60)
cursor.execute("SELECT id, name, department, salary FROM employees ORDER BY id")
for row in cursor.fetchall():
    print(f"   {row['id']}. {row['name']:<20} | {row['department']:<18} | ${row['salary']:,.0f}")

# Close connection
conn.close()

print("\n" + "=" * 60)
print("✅ INSERT, UPDATE, DELETE - Complete!")
print("=" * 60)

print("""
Summary:
--------
1. INSERT INTO table (columns) VALUES (values) - Add data
2. Use executemany() for multiple inserts
3. UPDATE table SET column=value WHERE condition
4. DELETE FROM table WHERE condition
5. ALWAYS use WHERE with UPDATE/DELETE!
6. Use parameterized queries (?) for safety
7. Use transactions for multiple operations
8. Test with SELECT before modifying data
""")
