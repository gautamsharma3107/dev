"""
Day 10 - Database Basics
========================
Learn: What are databases, SQL fundamentals, SQLite3 setup

Key Concepts:
- Database: Organized collection of data stored electronically
- SQL: Structured Query Language for managing databases
- SQLite: Lightweight, file-based database built into Python
- Tables: Store data in rows and columns
"""

import sqlite3
import os

# ========== WHAT IS A DATABASE? ==========
print("=" * 60)
print("WHAT IS A DATABASE?")
print("=" * 60)

print("""
A DATABASE is an organized collection of structured data.

Key Terms:
- RDBMS (Relational Database Management System)
  Examples: MySQL, PostgreSQL, SQLite, Oracle
  
- Table: A collection of related data organized in rows and columns
- Row (Record): A single entry in a table
- Column (Field): An attribute of data (like 'name', 'email')
- Primary Key: Unique identifier for each row
- Foreign Key: A field that links to another table
- Schema: The structure/blueprint of a database

SQL (Structured Query Language):
- Standard language for interacting with databases
- Used for: Creating tables, inserting data, querying data
- Same core syntax across most databases
""")

# ========== SQLITE3 SETUP ==========
print("\n" + "=" * 60)
print("SQLITE3 SETUP")
print("=" * 60)

# SQLite3 comes built-in with Python
print("SQLite3 is included in Python's standard library!")
print("No installation needed!")

# Create a database (or connect to existing one)
# Using :memory: for demonstration (in-memory database)
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

print("\n✅ Connected to SQLite database (in-memory)")
print(f"SQLite Version: {sqlite3.sqlite_version}")

# ========== CREATING A TABLE ==========
print("\n" + "=" * 60)
print("CREATING A TABLE")
print("=" * 60)

# SQL to create a table
create_table_sql = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    age INTEGER,
    city TEXT,
    active INTEGER DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
"""

cursor.execute(create_table_sql)
conn.commit()

print("Created 'users' table with columns:")
print("- id (INTEGER, Primary Key)")
print("- name (TEXT, Not Null)")
print("- email (TEXT, Unique)")
print("- age (INTEGER)")
print("- city (TEXT)")
print("- active (INTEGER, Default 1)")
print("- created_at (TIMESTAMP)")

# ========== DATA TYPES IN SQLITE ==========
print("\n" + "=" * 60)
print("SQLITE DATA TYPES")
print("=" * 60)

print("""
SQLite Data Types:
------------------
1. TEXT      - String data
2. INTEGER   - Whole numbers
3. REAL      - Floating-point numbers
4. BLOB      - Binary data
5. NULL      - No value

Constraints:
------------
- PRIMARY KEY - Unique identifier
- NOT NULL    - Cannot be empty
- UNIQUE      - Must be unique across all rows
- DEFAULT     - Default value if not provided
- AUTOINCREMENT - Auto-generates next number
""")

# ========== INSERT SAMPLE DATA ==========
print("\n" + "=" * 60)
print("INSERTING DATA")
print("=" * 60)

# Insert single row
insert_sql = """
INSERT INTO users (name, email, age, city) 
VALUES (?, ?, ?, ?)
"""

# Sample data
sample_users = [
    ("Alice Johnson", "alice@email.com", 28, "New York"),
    ("Bob Smith", "bob@email.com", 35, "Los Angeles"),
    ("Charlie Brown", "charlie@email.com", 22, "Chicago"),
    ("Diana Ross", "diana@email.com", 31, "Houston"),
    ("Eve Wilson", "eve@email.com", 27, "Phoenix"),
    ("Frank Miller", "frank@email.com", 40, "New York"),
    ("Grace Lee", "grace@email.com", 29, "Chicago"),
    ("Henry Davis", "henry@email.com", 33, "Miami"),
    ("Ivy Chen", "ivy@email.com", 25, "Seattle"),
    ("Jack Brown", "jack@email.com", 45, "Denver"),
]

# Insert using parameterized queries (SAFE from SQL injection)
cursor.executemany(insert_sql, sample_users)
conn.commit()

print(f"✅ Inserted {len(sample_users)} users into database")

# ========== BASIC SELECT ==========
print("\n" + "=" * 60)
print("BASIC SELECT QUERY")
print("=" * 60)

# Select all columns
cursor.execute("SELECT * FROM users")
all_users = cursor.fetchall()

print("\nAll users in the database:")
print("-" * 60)
for user in all_users:
    print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}, Age: {user[3]}, City: {user[4]}")

# ========== SELECT SPECIFIC COLUMNS ==========
print("\n" + "=" * 60)
print("SELECT SPECIFIC COLUMNS")
print("=" * 60)

cursor.execute("SELECT name, email FROM users")
results = cursor.fetchall()

print("\nNames and emails only:")
for row in results:
    print(f"  {row[0]} - {row[1]}")

# ========== USING ROW_FACTORY FOR BETTER ACCESS ==========
print("\n" + "=" * 60)
print("USING ROW_FACTORY")
print("=" * 60)

# Enable dictionary-like access to rows
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

cursor.execute("SELECT * FROM users LIMIT 3")
rows = cursor.fetchall()

print("\nAccessing columns by name:")
for row in rows:
    print(f"  {row['name']} is {row['age']} years old from {row['city']}")

# ========== TABLE INFO ==========
print("\n" + "=" * 60)
print("TABLE INFORMATION")
print("=" * 60)

# Get table structure
cursor.execute("PRAGMA table_info(users)")
columns = cursor.fetchall()

print("\nTable 'users' structure:")
print("-" * 40)
for col in columns:
    print(f"  {col['name']}: {col['type']}")

# ========== PRACTICAL EXAMPLE ==========
print("\n" + "=" * 60)
print("PRACTICAL EXAMPLE: Create a Products Table")
print("=" * 60)

# Create products table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT,
        price REAL,
        stock INTEGER DEFAULT 0
    )
""")

# Insert sample products
products = [
    ("Laptop", "Electronics", 999.99, 50),
    ("Smartphone", "Electronics", 699.99, 100),
    ("Headphones", "Electronics", 149.99, 200),
    ("Coffee Maker", "Appliances", 79.99, 30),
    ("Blender", "Appliances", 49.99, 45),
    ("Running Shoes", "Sports", 89.99, 75),
    ("Yoga Mat", "Sports", 29.99, 100),
]

cursor.executemany(
    "INSERT INTO products (name, category, price, stock) VALUES (?, ?, ?, ?)",
    products
)
conn.commit()

print("Created 'products' table with sample data:")
cursor.execute("SELECT * FROM products")
for product in cursor.fetchall():
    print(f"  {product['name']}: ${product['price']} (Stock: {product['stock']})")

# Close connection
conn.close()

print("\n" + "=" * 60)
print("✅ Database Basics - Complete!")
print("=" * 60)

print("""
Summary:
--------
1. SQLite is a lightweight, built-in database in Python
2. Use sqlite3.connect() to create/connect to a database
3. Use cursor.execute() to run SQL commands
4. Use conn.commit() to save changes
5. Always use parameterized queries (?) to prevent SQL injection
6. Use row_factory = sqlite3.Row for named column access
""")
