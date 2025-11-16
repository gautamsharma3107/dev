# Working with Databases in Python: Complete Guide

---

## Table of Contents
1. [Introduction](#introduction)
2. [sqlite3 Module](#sqlite3-module)
3. [Creating Databases](#creating-databases)
4. [Executing Queries](#executing-queries)
5. [Parameterized Queries](#parameterized-queries)
6. [Transactions](#transactions)
7. [Advanced Usage](#advanced-usage)
8. [Practical Examples](#practical-examples)
9. [Best Practices](#best-practices)
10. [Practice Exercises](#practice-exercises)

---

## Introduction

### Why Python Database Access?

1. **Data Persistence** - Save application data
2. **Query Data** - Retrieve and filter information
3. **Business Logic** - Complex data operations
4. **Integration** - Connect to external databases
5. **Automation** - Programmatic database management

### Database Options in Python

```python
# Built-in
import sqlite3  # Lightweight, file-based

# Third-party packages (require installation)
import mysql.connector  # MySQL/MariaDB
import psycopg2  # PostgreSQL
import pymongo  # MongoDB
from sqlalchemy import create_engine  # ORM (multiple databases)
```

### SQLite Advantages

- ✅ Built-in (no installation needed)
- ✅ Serverless (no separate server process)
- ✅ File-based (single file database)
- ✅ Perfect for learning and small projects
- ✅ Used in mobile apps (Android, iOS)

---

## sqlite3 Module

### Installation and Import

```python
# sqlite3 is built-in with Python
import sqlite3

print(sqlite3.version)  # Python interface version
print(sqlite3.sqlite_version)  # SQLite library version
```

### Connection and Cursor

```python
import sqlite3

# Create/connect to database file
connection = sqlite3.connect("myapp.db")

# Create cursor for executing queries
cursor = connection.cursor()

# Execute queries using cursor
cursor.execute("SELECT * FROM users")

# Get results
results = cursor.fetchall()

# Close cursor
cursor.close()

# Close connection
connection.close()
```

### Connection Object

```python
import sqlite3

conn = sqlite3.connect("myapp.db")

# Cursor object
cursor = conn.cursor()

# In-memory database (temporary)
temp_conn = sqlite3.connect(":memory:")

# Connection properties
print(conn.isolation_level)  # Transaction behavior
print(conn.total_changes)    # Total row changes

# Commit changes
conn.commit()

# Rollback changes
conn.rollback()

# Close connection
conn.close()
```

### Context Manager (Recommended)

```python
import sqlite3

# Automatically handles close()
with sqlite3.connect("myapp.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
    conn.commit()

# Connection closed automatically
```

---

## Creating Databases

### Creating Tables

```python
import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# Create users table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        age INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")

# Create courses table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS courses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        credits INTEGER DEFAULT 3,
        description TEXT
    )
""")

# Create enrollment table (junction table)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS enrollments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        course_id INTEGER NOT NULL,
        grade TEXT,
        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (course_id) REFERENCES courses(id),
        UNIQUE (user_id, course_id)
    )
""")

conn.commit()
conn.close()

print("✓ Database created successfully")
```

### Data Types in SQLite

```python
"""
SQLite Data Types:

NULL        - No value
INTEGER     - Whole numbers
REAL        - Floating point numbers
TEXT        - Text strings
BLOB        - Binary data
NUMERIC     - Numeric values (flexible)
"""

import sqlite3

conn = sqlite3.connect("types_example.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS examples (
        id INTEGER PRIMARY KEY,
        count INTEGER,
        price REAL,
        name TEXT,
        data BLOB,
        metadata NUMERIC
    )
""")

conn.commit()
conn.close()
```

### Constraints

```python
import sqlite3

conn = sqlite3.connect("constraints.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        
        -- NOT NULL constraint
        name TEXT NOT NULL,
        
        -- UNIQUE constraint
        email TEXT UNIQUE,
        
        -- CHECK constraint
        age INTEGER CHECK (age >= 18),
        
        -- DEFAULT value
        department TEXT DEFAULT 'General',
        
        -- FOREIGN KEY
        manager_id INTEGER REFERENCES employees(id),
        
        -- Composite UNIQUE
        UNIQUE (email, name)
    )
""")

conn.commit()
conn.close()
```

### Indexes

```python
import sqlite3

conn = sqlite3.connect("indexes.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT,
        age INTEGER
    )
""")

# Create indexes for faster queries
cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON users(email)")
cursor.execute("CREATE INDEX IF NOT EXISTS idx_name ON users(name)")
cursor.execute("CREATE INDEX IF NOT EXISTS idx_age ON users(age)")

# Composite index
cursor.execute("CREATE INDEX IF NOT EXISTS idx_name_age ON users(name, age)")

conn.commit()

# List indexes
cursor.execute("SELECT * FROM sqlite_master WHERE type='index'")
indexes = cursor.fetchall()
for index in indexes:
    print(index)

conn.close()
```

---

## Executing Queries

### Insert Operations

```python
import sqlite3

conn = sqlite3.connect("myapp.db")
cursor = conn.cursor()

# Insert single row
cursor.execute("""
    INSERT INTO users (name, email, age)
    VALUES ('Alice', 'alice@example.com', 25)
""")

# Insert multiple rows
rows = [
    ('Bob', 'bob@example.com', 30),
    ('Charlie', 'charlie@example.com', 28),
    ('Diana', 'diana@example.com', 26)
]
cursor.executemany("""
    INSERT INTO users (name, email, age)
    VALUES (?, ?, ?)
""", rows)

conn.commit()
print(f"✓ Inserted {cursor.rowcount} rows")
conn.close()
```

### Select Operations

```python
import sqlite3

conn = sqlite3.connect("myapp.db")
cursor = conn.cursor()

# Fetch all rows
cursor.execute("SELECT * FROM users")
all_rows = cursor.fetchall()
print(all_rows)

# Fetch one row
cursor.execute("SELECT * FROM users WHERE id = 1")
one_row = cursor.fetchone()
print(one_row)

# Fetch specific number of rows
cursor.execute("SELECT * FROM users")
first_three = cursor.fetchmany(3)
print(first_three)

# Get column names
cursor.execute("SELECT * FROM users")
column_names = [description[0] for description in cursor.description]
print(column_names)

# Iterate through results
cursor.execute("SELECT * FROM users")
for row in cursor:
    print(row)

conn.close()
```

### Select with Conditions

```python
import sqlite3

conn = sqlite3.connect("myapp.db")
cursor = conn.cursor()

# Simple WHERE
cursor.execute("SELECT * FROM users WHERE age > 25")
results = cursor.fetchall()

# Multiple conditions
cursor.execute("""
    SELECT * FROM users
    WHERE age > 25 AND name LIKE 'A%'
    ORDER BY age DESC
    LIMIT 5
""")
results = cursor.fetchall()

# IN clause
cursor.execute("""
    SELECT * FROM users
    WHERE age IN (25, 30, 35)
""")
results = cursor.fetchall()

# BETWEEN
cursor.execute("""
    SELECT * FROM users
    WHERE age BETWEEN 25 AND 35
""")
results = cursor.fetchall()

conn.close()
```

### Update Operations

```python
import sqlite3

conn = sqlite3.connect("myapp.db")
cursor = conn.cursor()

# Update single row
cursor.execute("""
    UPDATE users
    SET age = 26
    WHERE id = 1
""")

# Update multiple rows
cursor.execute("""
    UPDATE users
    SET department = 'IT'
    WHERE age > 30
""")

# Update with multiple columns
cursor.execute("""
    UPDATE users
    SET age = age + 1, department = 'HR'
    WHERE name = 'Alice'
""")

conn.commit()
print(f"✓ Updated {cursor.rowcount} rows")
conn.close()
```

### Delete Operations

```python
import sqlite3

conn = sqlite3.connect("myapp.db")
cursor = conn.cursor()

# Delete specific row
cursor.execute("DELETE FROM users WHERE id = 1")

# Delete multiple rows
cursor.execute("DELETE FROM users WHERE age > 60")

# Delete all rows
cursor.execute("DELETE FROM users")

conn.commit()
print(f"✓ Deleted {cursor.rowcount} rows")
conn.close()
```

### Aggregation Queries

```python
import sqlite3

conn = sqlite3.connect("myapp.db")
cursor = conn.cursor()

# Count
cursor.execute("SELECT COUNT(*) FROM users")
count = cursor.fetchone()[0]
print(f"Total users: {count}")

# Sum, Average, Min, Max
cursor.execute("""
    SELECT 
        COUNT(*) as total,
        AVG(age) as avg_age,
        MIN(age) as min_age,
        MAX(age) as max_age
    FROM users
""")
stats = cursor.fetchone()
print(f"Stats: {stats}")

# Group by
cursor.execute("""
    SELECT department, COUNT(*) as count
    FROM users
    GROUP BY department
    ORDER BY count DESC
""")
grouped = cursor.fetchall()
print(grouped)

conn.close()
```

### Joins

```python
import sqlite3

conn = sqlite3.connect("myapp.db")
cursor = conn.cursor()

# Inner join
cursor.execute("""
    SELECT u.name, c.name as course
    FROM users u
    INNER JOIN enrollments e ON u.id = e.user_id
    INNER JOIN courses c ON e.course_id = c.id
""")
results = cursor.fetchall()

# Left join
cursor.execute("""
    SELECT u.name, COUNT(e.id) as enrollment_count
    FROM users u
    LEFT JOIN enrollments e ON u.id = e.user_id
    GROUP BY u.id
""")
results = cursor.fetchall()

conn.close()
```

---

## Parameterized Queries

### Why Parameterized Queries?

```python
# ✗ BAD - SQL Injection vulnerability
user_input = "'; DROP TABLE users; --"
query = f"SELECT * FROM users WHERE name = '{user_input}'"
# This could delete the entire table!

# ✓ GOOD - Parameterized query
cursor.execute("SELECT * FROM users WHERE name = ?", (user_input,))
# User input is safely escaped
```

### Using Placeholders

```python
import sqlite3

conn = sqlite3.connect("myapp.db")
cursor = conn.cursor()

# Question mark placeholder (recommended for SQLite)
user_id = 1
cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
result = cursor.fetchone()

# Multiple parameters
name = "Alice"
age = 25
cursor.execute(
    "SELECT * FROM users WHERE name = ? AND age = ?",
    (name, age)
)
results = cursor.fetchall()

# Named placeholders (also supported)
cursor.execute(
    "SELECT * FROM users WHERE name = :name AND age = :age",
    {"name": "Alice", "age": 25}
)
results = cursor.fetchall()

# Insert with parameters
cursor.execute(
    "INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
    ("Bob", "bob@example.com", 30)
)
conn.commit()

conn.close()
```

### Parameterized Insert/Update/Delete

```python
import sqlite3

conn = sqlite3.connect("myapp.db")
cursor = conn.cursor()

# Insert
data = ("Charlie", "charlie@example.com", 28)
cursor.execute(
    "INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
    data
)

# Update
cursor.execute(
    "UPDATE users SET age = ? WHERE name = ?",
    (29, "Charlie")
)

# Delete
cursor.execute(
    "DELETE FROM users WHERE email = ?",
    ("charlie@example.com",)
)

conn.commit()
print(f"✓ Executed safely")
conn.close()
```

### Batch Operations

```python
import sqlite3

conn = sqlite3.connect("myapp.db")
cursor = conn.cursor()

# executemany for multiple rows
users = [
    ("Alice", "alice@example.com", 25),
    ("Bob", "bob@example.com", 30),
    ("Charlie", "charlie@example.com", 28)
]

cursor.executemany(
    "INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
    users
)

conn.commit()
print(f"✓ Inserted {cursor.rowcount} rows")
conn.close()
```

---

## Transactions

### Understanding Transactions

```python
import sqlite3

conn = sqlite3.connect("myapp.db")
cursor = conn.cursor()

# By default, sqlite3 auto-commits changes
# To use explicit transactions:

try:
    # Start transaction (implicit)
    cursor.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
                   ("Alice", "alice@example.com", 25))
    
    cursor.execute("INSERT INTO courses (name, credits) VALUES (?, ?)",
                   ("Python", 3))
    
    # All changes succeed together
    conn.commit()
    print("✓ Transaction committed")
    
except Exception as e:
    # Rollback if error
    conn.rollback()
    print(f"✗ Transaction rolled back: {e}")

finally:
    conn.close()
```

### Bank Transfer Example

```python
import sqlite3

def transfer_money(from_account, to_account, amount):
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()
    
    try:
        # Deduct from source account
        cursor.execute(
            "UPDATE accounts SET balance = balance - ? WHERE id = ?",
            (amount, from_account)
        )
        
        # Check if deduction was successful
        if cursor.rowcount == 0:
            raise ValueError(f"Account {from_account} not found")
        
        # Add to target account
        cursor.execute(
            "UPDATE accounts SET balance = balance + ? WHERE id = ?",
            (amount, to_account)
        )
        
        if cursor.rowcount == 0:
            raise ValueError(f"Account {to_account} not found")
        
        # Both succeeded, commit
        conn.commit()
        print(f"✓ Transferred ${amount} from {from_account} to {to_account}")
        
    except Exception as e:
        # If any error, rollback both operations
        conn.rollback()
        print(f"✗ Transfer failed: {e}")
        
    finally:
        conn.close()

# Usage
transfer_money(1, 2, 100)
```

### Savepoints

```python
import sqlite3

conn = sqlite3.connect("myapp.db")
cursor = conn.cursor()

try:
    # Insert first user
    cursor.execute(
        "INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
        ("Alice", "alice@example.com", 25)
    )
    
    # Create savepoint
    cursor.execute("SAVEPOINT sp1")
    
    # Insert second user
    cursor.execute(
        "INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
        ("Bob", "bob@example.com", 30)
    )
    
    # If error happens, rollback to savepoint
    if True:  # Some error condition
        cursor.execute("ROLLBACK TO sp1")
        print("Rolled back to savepoint")
    
    conn.commit()
    
except Exception as e:
    conn.rollback()
    print(f"Error: {e}")

finally:
    conn.close()
```

### Isolation Levels

```python
import sqlite3

# Default isolation level is DEFERRED
conn = sqlite3.connect("myapp.db", isolation_level="DEFERRED")

# Immediate locking
conn = sqlite3.connect("myapp.db", isolation_level="IMMEDIATE")

# Exclusive locking
conn = sqlite3.connect("myapp.db", isolation_level="EXCLUSIVE")

# Autocommit mode (no transactions)
conn = sqlite3.connect("myapp.db", isolation_level=None)
```

---

## Advanced Usage

### Row Factory

```python
import sqlite3

conn = sqlite3.connect("myapp.db")

# Default - returns tuples
cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
row = cursor.fetchone()
print(row)  # (1, 'Alice', 'alice@example.com', 25)

# Return dictionaries
conn.row_factory = sqlite3.Row
cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
row = cursor.fetchone()
print(row["name"])  # Access by column name

# Custom row factory
def dict_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return {field: value for field, value in zip(fields, row)}

conn.row_factory = dict_factory
cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
row = cursor.fetchone()
print(row)  # {'id': 1, 'name': 'Alice', ...}

conn.close()
```

### Error Handling

```python
import sqlite3

conn = sqlite3.connect("myapp.db")
cursor = conn.cursor()

try:
    # IntegrityError - constraint violation
    cursor.execute(
        "INSERT INTO users (id, email) VALUES (?, ?)",
        (1, "duplicate@example.com")
    )
except sqlite3.IntegrityError as e:
    print(f"Integrity error: {e}")

except sqlite3.OperationalError as e:
    print(f"Operational error: {e}")

except sqlite3.ProgrammingError as e:
    print(f"Programming error: {e}")

except sqlite3.DatabaseError as e:
    print(f"Database error: {e}")

finally:
    conn.close()
```

### Connection Pooling (Simple)

```python
import sqlite3
from contextlib import contextmanager

class DatabasePool:
    def __init__(self, database, pool_size=5):
        self.database = database
        self.connections = [
            sqlite3.connect(database) for _ in range(pool_size)
        ]
    
    @contextmanager
    def get_connection(self):
        conn = self.connections.pop()
        try:
            yield conn
        finally:
            self.connections.append(conn)

# Usage
pool = DatabasePool("myapp.db")

with pool.get_connection() as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
```

---

## Practical Examples

### Student Management System

```python
import sqlite3
from datetime import datetime

class StudentDatabase:
    def __init__(self, db_file="school.db"):
        self.db_file = db_file
        self.init_db()
    
    def init_db(self):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            
            # Students table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    enrollment_date DATE DEFAULT CURRENT_DATE
                )
            """)
            
            # Grades table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS grades (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    student_id INTEGER NOT NULL,
                    course TEXT NOT NULL,
                    grade TEXT NOT NULL,
                    FOREIGN KEY (student_id) REFERENCES students(id)
                )
            """)
            
            conn.commit()
    
    def add_student(self, name, email):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute(
                    "INSERT INTO students (name, email) VALUES (?, ?)",
                    (name, email)
                )
                conn.commit()
                return cursor.lastrowid
            except sqlite3.IntegrityError:
                print(f"Email {email} already exists")
                return None
    
    def add_grade(self, student_id, course, grade):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO grades (student_id, course, grade) VALUES (?, ?, ?)",
                (student_id, course, grade)
            )
            conn.commit()
    
    def get_student_grades(self, student_id):
        with sqlite3.connect(self.db_file) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM grades WHERE student_id = ?",
                (student_id,)
            )
            return cursor.fetchall()
    
    def get_average_grade(self, student_id):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT AVG(
                    CASE 
                        WHEN grade = 'A' THEN 4.0
                        WHEN grade = 'B' THEN 3.0
                        WHEN grade = 'C' THEN 2.0
                        WHEN grade = 'D' THEN 1.0
                        ELSE 0.0
                    END
                ) as avg_gpa
                FROM grades WHERE student_id = ?
            """, (student_id,))
            result = cursor.fetchone()
            return result[0] if result else None

# Usage
db = StudentDatabase()

# Add students
sid1 = db.add_student("Alice", "alice@school.com")
sid2 = db.add_student("Bob", "bob@school.com")

# Add grades
db.add_grade(sid1, "Math", "A")
db.add_grade(sid1, "Physics", "B")
db.add_grade(sid2, "Math", "B")

# Get grades
grades = db.get_student_grades(sid1)
print(grades)

# Get GPA
gpa = db.get_average_grade(sid1)
print(f"GPA: {gpa:.2f}")
```

---

## Best Practices

### 1. Always Use Context Managers

```python
# ✗ BAD
conn = sqlite3.connect("myapp.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
# Might not close if exception occurs

# ✓ GOOD
with sqlite3.connect("myapp.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    # Automatically closes
```

### 2. Use Parameterized Queries

```python
# ✗ BAD - SQL Injection risk
query = f"SELECT * FROM users WHERE name = '{name}'"

# ✓ GOOD - Safe
cursor.execute("SELECT * FROM users WHERE name = ?", (name,))
```

### 3. Handle Exceptions

```python
# ✓ GOOD
try:
    with sqlite3.connect("myapp.db") as conn:
        cursor = conn.cursor()
        cursor.execute(...)
        conn.commit()
except sqlite3.IntegrityError:
    print("Data already exists")
except sqlite3.OperationalError:
    print("Table not found")
```

### 4. Use Transactions

```python
# ✓ GOOD - All or nothing
try:
    with sqlite3.connect("myapp.db") as conn:
        cursor = conn.cursor()
        cursor.execute(...)
        cursor.execute(...)
        conn.commit()
except Exception:
    conn.rollback()
```

### 5. Create Indexes

```python
# ✓ GOOD - For frequently queried columns
cursor.execute("CREATE INDEX idx_email ON users(email)")
```

---

## Practice Exercises

### 1. Basic Database Operations
- Create a database with multiple tables
- Insert sample data
- Retrieve with various queries

### 2. CRUD Operations
- Implement Create, Read, Update, Delete
- Handle errors
- Use parameterized queries

### 3. Transactions
- Implement multi-step transactions
- Test rollback behavior
- Ensure data consistency

### 4. Relationships
- Create related tables
- Use foreign keys
- Perform joins

### 5. Real-World Project
- Build todo app with database
- Build expense tracker
- Build contact manager
- Implement complete CRUD system

---

# End of Notes
