"""
Day 18 - PostgreSQL Setup
=========================
Learn: PostgreSQL basics, connection, and operations

Key Concepts:
- PostgreSQL vs SQLite comparison
- Connection management
- Basic CRUD operations
- Using psycopg2 driver

Note: We'll use SQLite for examples (no setup required)
      PostgreSQL concepts are explained throughout
"""

import sqlite3
import os

# ========== POSTGRESQL VS SQLITE ==========
print("=" * 60)
print("POSTGRESQL VS SQLITE COMPARISON")
print("=" * 60)

print("""
Feature          | SQLite              | PostgreSQL
-----------------|---------------------|----------------------
Type             | File-based          | Client-server
Setup            | No setup needed     | Requires installation
Concurrency      | Single writer       | Multiple connections
Scale            | Small-medium apps   | Large scale apps
Use Case         | Development, mobile | Production, enterprise
Data Types       | Flexible            | Strict typing
Features         | Basic SQL           | Advanced (JSON, arrays)

For Learning: SQLite is perfect!
For Production: PostgreSQL is recommended.
""")

# ========== BASIC CONNECTION ==========
print("=" * 60)
print("DATABASE CONNECTION")
print("=" * 60)

# SQLite - What we'll use (no setup required)
print("\n1. SQLite Connection (file-based):")
print("   conn = sqlite3.connect('database.db')")
print("   cursor = conn.cursor()")

# PostgreSQL - For reference
print("\n2. PostgreSQL Connection (requires installation):")
print("""
   import psycopg2
   
   conn = psycopg2.connect(
       host="localhost",
       port=5432,
       database="mydb",
       user="postgres",
       password="password"
   )
   cursor = conn.cursor()
""")

# ========== PRACTICAL EXAMPLE WITH SQLITE ==========
print("\n" + "=" * 60)
print("PRACTICAL EXAMPLE: Setting Up Database")
print("=" * 60)

# Create database and connect
db_file = "example.db"
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
print(f"✅ Connected to {db_file}")

# ========== CREATE TABLE ==========
print("\n--- Creating Tables ---")

# Drop if exists for clean demo
cursor.execute("DROP TABLE IF EXISTS users")

# Create users table
create_users = """
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
"""
cursor.execute(create_users)
conn.commit()
print("✅ Created 'users' table")

# Show table structure
print("\nTable Structure:")
cursor.execute("PRAGMA table_info(users)")
columns = cursor.fetchall()
print(f"{'Column':<15} {'Type':<15} {'Nullable':<10} {'Default'}")
print("-" * 55)
for col in columns:
    nullable = "Yes" if col[3] == 0 else "No"
    default = col[4] if col[4] else "None"
    print(f"{col[1]:<15} {col[2]:<15} {nullable:<10} {default}")

# ========== INSERT DATA ==========
print("\n" + "=" * 60)
print("INSERTING DATA")
print("=" * 60)

# Method 1: Single insert
print("\n1. Single Insert:")
cursor.execute(
    "INSERT INTO users (username, email) VALUES (?, ?)",
    ("alice", "alice@example.com")
)
conn.commit()
print("   ✅ Inserted alice")

# Method 2: Multiple inserts with executemany
print("\n2. Batch Insert (executemany):")
users_data = [
    ("bob", "bob@example.com"),
    ("charlie", "charlie@example.com"),
    ("diana", "diana@example.com"),
]
cursor.executemany(
    "INSERT INTO users (username, email) VALUES (?, ?)",
    users_data
)
conn.commit()
print(f"   ✅ Inserted {len(users_data)} users")

# ========== QUERY DATA ==========
print("\n" + "=" * 60)
print("QUERYING DATA")
print("=" * 60)

# fetchone - single row
print("\n1. fetchone() - Single row:")
cursor.execute("SELECT * FROM users WHERE username = ?", ("alice",))
user = cursor.fetchone()
print(f"   {user}")

# fetchall - all rows
print("\n2. fetchall() - All rows:")
cursor.execute("SELECT * FROM users ORDER BY id")
all_users = cursor.fetchall()
for u in all_users:
    print(f"   {u}")

# fetchmany - specific number
print("\n3. fetchmany(2) - Limited rows:")
cursor.execute("SELECT * FROM users")
some_users = cursor.fetchmany(2)
for u in some_users:
    print(f"   {u}")

# Row as dictionary (more readable)
print("\n4. Row Factory (dict-like access):")
conn.row_factory = sqlite3.Row
cursor = conn.cursor()
cursor.execute("SELECT * FROM users WHERE id = 1")
user_row = cursor.fetchone()
print(f"   ID: {user_row['id']}")
print(f"   Username: {user_row['username']}")
print(f"   Email: {user_row['email']}")

# Reset row factory
conn.row_factory = None
cursor = conn.cursor()

# ========== UPDATE DATA ==========
print("\n" + "=" * 60)
print("UPDATING DATA")
print("=" * 60)

cursor.execute(
    "UPDATE users SET email = ? WHERE username = ?",
    ("alice_new@example.com", "alice")
)
conn.commit()
print(f"✅ Updated {cursor.rowcount} row(s)")

# Verify update
cursor.execute("SELECT * FROM users WHERE username = 'alice'")
print(f"   After update: {cursor.fetchone()}")

# ========== DELETE DATA ==========
print("\n" + "=" * 60)
print("DELETING DATA")
print("=" * 60)

cursor.execute("DELETE FROM users WHERE username = ?", ("diana",))
conn.commit()
print(f"✅ Deleted {cursor.rowcount} row(s)")

# ========== TRANSACTION EXAMPLE ==========
print("\n" + "=" * 60)
print("TRANSACTIONS")
print("=" * 60)

print("""
Transactions ensure data integrity:
- All operations succeed, or all fail
- Use commit() to save, rollback() to undo
""")

try:
    cursor.execute("BEGIN TRANSACTION")
    cursor.execute(
        "INSERT INTO users (username, email) VALUES (?, ?)",
        ("eve", "eve@example.com")
    )
    cursor.execute(
        "INSERT INTO users (username, email) VALUES (?, ?)",
        ("frank", "frank@example.com")
    )
    conn.commit()
    print("✅ Transaction committed successfully")
except Exception as e:
    conn.rollback()
    print(f"❌ Transaction rolled back: {e}")

# ========== CONTEXT MANAGER PATTERN ==========
print("\n" + "=" * 60)
print("BEST PRACTICE: Context Manager")
print("=" * 60)

print("""
Using 'with' statement ensures proper cleanup:
""")

with sqlite3.connect(db_file) as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users")
    count = cursor.fetchone()[0]
    print(f"✅ Total users: {count}")
# Connection auto-committed and closed

# ========== POSTGRESQL-SPECIFIC FEATURES ==========
print("\n" + "=" * 60)
print("POSTGRESQL-SPECIFIC FEATURES (Reference)")
print("=" * 60)

print("""
PostgreSQL offers advanced features not in SQLite:

1. JSONB Data Type:
   CREATE TABLE events (
       id SERIAL PRIMARY KEY,
       data JSONB
   );
   
   INSERT INTO events (data) 
   VALUES ('{"type": "click", "page": "/home"}');
   
   SELECT data->>'type' FROM events;

2. Arrays:
   CREATE TABLE posts (
       id SERIAL PRIMARY KEY,
       tags TEXT[]
   );
   
   SELECT * FROM posts WHERE 'python' = ANY(tags);

3. Full Text Search:
   SELECT * FROM articles 
   WHERE to_tsvector(content) @@ to_tsquery('python & web');

4. Window Functions:
   SELECT username, 
          SUM(amount) OVER (PARTITION BY user_id) as total
   FROM orders;

5. UPSERT (INSERT or UPDATE):
   INSERT INTO users (username, email) 
   VALUES ('alice', 'alice@new.com')
   ON CONFLICT (username) 
   DO UPDATE SET email = EXCLUDED.email;
""")

# ========== ERROR HANDLING ==========
print("=" * 60)
print("ERROR HANDLING")
print("=" * 60)

def safe_insert(conn, username, email):
    """Safely insert user with error handling"""
    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (username, email) VALUES (?, ?)",
            (username, email)
        )
        conn.commit()
        return True, "User created successfully"
    except sqlite3.IntegrityError as e:
        return False, f"Integrity error: {e}"
    except sqlite3.Error as e:
        conn.rollback()
        return False, f"Database error: {e}"

# Test safe insert
conn = sqlite3.connect(db_file)

# This should work
success, msg = safe_insert(conn, "grace", "grace@example.com")
print(f"Insert grace: {msg}")

# This should fail (duplicate)
success, msg = safe_insert(conn, "grace", "grace2@example.com")
print(f"Insert duplicate: {msg}")

# ========== PARAMETERIZED QUERIES ==========
print("\n" + "=" * 60)
print("SECURITY: Parameterized Queries")
print("=" * 60)

print("""
ALWAYS use parameterized queries to prevent SQL injection!

❌ DANGEROUS (SQL Injection vulnerable):
   cursor.execute(f"SELECT * FROM users WHERE name = '{user_input}'")

✅ SAFE (Parameterized):
   cursor.execute("SELECT * FROM users WHERE name = ?", (user_input,))
""")

# Example
user_input = "alice' OR '1'='1"  # Malicious input
print(f"\nMalicious input: {user_input}")

# Safe query
cursor = conn.cursor()
cursor.execute("SELECT * FROM users WHERE username = ?", (user_input,))
result = cursor.fetchone()
print(f"Safe query result: {result}")  # Returns None, not all users!

# ========== CLEANUP ==========
print("\n" + "=" * 60)
print("CLEANUP")
print("=" * 60)

conn.close()
if os.path.exists(db_file):
    os.remove(db_file)
print("✅ Database closed and removed")

print("\n" + "=" * 60)
print("✅ PostgreSQL Setup - Complete!")
print("=" * 60)
